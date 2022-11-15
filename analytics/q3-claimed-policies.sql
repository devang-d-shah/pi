-- How many policies have claimed? 

SELECT count(distinct policy_reference) as claimed_policies FROM `ds-de-sandbox-66.pi.claims` 

-- claimed_policies
-- 3153
