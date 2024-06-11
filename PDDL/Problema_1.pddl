#Problema 1: Enviar un documento de un lugar a otro
(define (problem enviar_doc_sencillo)
  (:domain envio_correspondencia)
  (:objects robot1 - robot doc1 - correspondencia oficina1 oficina2 - loc)
  (:init (en robot1 oficina1) (en_doc doc1 oficina1))
  (:goal (entregado doc1))
)
