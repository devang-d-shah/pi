
-- What are the most popular breeds ? 


SELECT breed,count(*) as entities FROM `ds-de-sandbox-66.pi.policies` p cross join unnest(data.insured_entities)
group by 1
order by 2 desc
limit 10

/*
breed	entities
MOGGY	1191
COCKERPOO	737
COCKER_SPANIEL	717
LABRADOR_RETRIEVER	684
MEDIUM_MONGREL_(10KG-20KG)	472
SMALL_MONGREL_(UP_TO_10KG)	325
FRENCH_BULLDOG	308
CAVAPOO	267
DACHSHUND_SHORT_HAIRED_(MINIATURE)	236
LARGE_MONGREL_(MORE_THAN_20KG)	227
*/
