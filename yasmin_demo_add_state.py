#!/usr/bin/env python3
import time
import rclpy
from rclpy.node import Node
from yasmin import State
from yasmin import Blackboard
from yasmin import StateMachine
from yasmin_viewer import YasminViewerPub
from std_msgs.msg import String


# Define state Foo
class FooState(State):
    def __init__(self, node: Node) -> None:
        super().__init__(["outcome1", "outcome2"])
        self.counter = 0
        self.node = node

    def execute(self, blackboard: Blackboard) -> str:
        print("Executing state FOO")
        time.sleep(3)

        if self.counter < 3:
            self.counter += 1
            blackboard.foo_str = f"Counter: {self.counter}"
            self.node.get_logger().info(f"Publishing from FooState: {blackboard.foo_str}")
            self.node.publish_message(blackboard.foo_str)
            return "outcome1"
        else:
            return "outcome2"


# Define state Bar
class BarState(State):
    def __init__(self, node: Node) -> None:
        super().__init__(outcomes=["outcome3"])
        self.node = node

    def execute(self, blackboard: Blackboard) -> str:
        print("Executing state BAR")
        time.sleep(3)

        self.node.get_logger().info(f"Publishing from BarState: Hello from BarState")
        self.node.publish_message("Hello from BarState")
        return "outcome3"


# Define state Baz
class BazState(State):
    def __init__(self, node: Node) -> None:
        super().__init__(outcomes=["outcome4", "outcome5"])
        self.node = node

    def execute(self, blackboard: Blackboard) -> str:
        print("Executing state BAZ")
        time.sleep(3)

        # Example logic for BazState
        if blackboard.foo_str.endswith("3"):
            self.node.get_logger().info(f"Publishing from BazState: {blackboard.foo_str}")
            self.node.publish_message(blackboard.foo_str)
            return "outcome4"
        else:
            self.node.get_logger().info(f"Publishing from BazState: Hello from BazState")
            self.node.publish_message("Hello from BazState")
            return "outcome5"


# Define state NewState
class NewState(State):
    def __init__(self, node: Node) -> None:
        super().__init__(outcomes=["outcome6"])  # 1. Se agrega un nuevo outcome
        self.node = node

    def execute(self, blackboard: Blackboard) -> str:
        print("Executing state NEWSTATE")
        time.sleep(3)

        self.node.get_logger().info(f"Publishing from NewState: New message from NewState")  # 2. Mensaje nuevo
        self.node.publish_message("New message from NewState")  # 3. Publica un nuevo mensaje
        return "outcome6"  # 4. Retorna el nuevo outcome


class StateMachineNode(Node):
    def __init__(self):
        super().__init__("state_machine_node")
        self.publisher_ = self.create_publisher(String, "state_machine_topic", 10)
        self.sm = StateMachine(outcomes=["outcome4"])
        self.add_states()

    def add_states(self):
        self.sm.add_state(
            "FOO",
            FooState(self),
            transitions={
                "outcome1": "BAR",
                "outcome2": "outcome4"
            }
        )
        self.sm.add_state(
            "BAR",
            BarState(self),
            transitions={
                "outcome3": "BAZ"
            }
        )
        self.sm.add_state(
            "BAZ",
            BazState(self),
            transitions={
                "outcome4": "outcome4",
                "outcome5": "NEWSTATE"  # 5. Transición hacia el nuevo estado
            }
        )
        self.sm.add_state(
            "NEWSTATE",  # 6. Agrega el nuevo estado a la máquina de estados
            NewState(self),
            transitions={
                "outcome6": "FOO"  # 7. Transición de regreso al estado original
            }
        )

    def publish_message(self, msg):
        msg = String(data=msg)
        self.publisher_.publish(msg)

    def execute_fsm(self):
        return self.sm()

    def get_logger(self):
        return super().get_logger()


def main():
    print("yasmin_demo")

    # Init ROS 2
    rclpy.init()

    # Create a StateMachineNode
    node = StateMachineNode()

    # Pub FSM info
    YasminViewerPub("YASMIN_DEMO", node.sm)

    # Execute FSM
    outcome = node.execute_fsm()
    print(outcome)

    # Shutdown ROS 2
    rclpy.shutdown()


if __name__ == "__main__":
    main()
