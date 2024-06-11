#Problema 2: Enviar dos documentos a diferentes lugares
(define (problem enviar_docs_mediano)
  (:domain envio_correspondencia)
  (:objects robot1 - robot doc1 doc2 - correspondencia oficina1 oficina2 oficina3 - loc)
  (:init (en robot1 oficina1) (en_doc doc1 oficina1) (en_doc doc2 oficina2))
  (:goal (and (entregado doc1) (entregado doc2)))
)
