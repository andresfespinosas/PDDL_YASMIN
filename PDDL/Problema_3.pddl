#Problema 3: Enviar varios documentos a varias ubicaciones, con el robot comenzando en una posición diferente
(define (problem enviar_docs_complejo)
  (:domain envio_correspondencia)
  (:objects robot1 - robot doc1 doc2 doc3 - correspondencia oficina1 oficina2 oficina3 oficina4 - loc)
  (:init (en robot1 oficina3) (en_doc doc1 oficina1) (en_doc doc2 oficina2) (en_doc doc3 oficina4))
  (:goal (and (entregado doc1) (entregado doc2) (entregado doc3)))
)
