-- How many different policies are in the data set? 
SELECT count(ref) as policy_count FROM `ds-de-sandbox-66.pi.policies`; 
-- policy_count
-- 8643


--What is the average number of pets per policy in the data set? 

with pets_per_policy as(
SELECT p.ref,count(*) as pets FROM `ds-de-sandbox-66.pi.policies` p cross join unnest(data.insured_entities)
group by 1)
select avg(pets) as avg_no_of_pets from pets_per_policy

--avg_no_of_pets
--1.2479793838584998
