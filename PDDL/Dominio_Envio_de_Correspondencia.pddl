(define (domain envio_correspondencia)
  (:predicates 
    (en ?robot ?loc)        ; El robot está en una ubicación
    (correspondencia ?doc)  ; El documento existe
    (en_doc ?doc ?loc)      ; El documento está en una ubicación
    (entregado ?doc)        ; El documento ha sido entregado
  )

  (:action mover
    :parameters (?robot ?de ?a)
    :precondition (and (en ?robot ?de))
    :effect (and (en ?robot ?a) (not (en ?robot ?de)))
  )

  (:action recoger
    :parameters (?robot ?doc ?loc)
    :precondition (and (en ?robot ?loc) (en_doc ?doc ?loc))
    :effect (and (not (en_doc ?doc ?loc)) (en ?robot ?doc))
  )

  (:action entregar
    :parameters (?robot ?doc ?loc)
    :precondition (and (en ?robot ?loc) (en ?robot ?doc))
    :effect (and (entregado ?doc) (not (en ?robot ?doc)))
  )
)
