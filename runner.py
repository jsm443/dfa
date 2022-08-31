from matchee import Matchee
from match_maker import match

res1 = Matchee("res1", [])
res2 = Matchee("res2", [])
res3 = Matchee("res3", [])

hos1 = Matchee("hos1", [res1, res2, res3])
hos2 = Matchee("hos2", [res2, res3, res1])
hos3 = Matchee("hos3", [res2, res1, res3])

res1.priorities = [hos1, hos2, hos3]
res2.priorities = [hos1, hos3, hos2]
res3.priorities = [hos3, hos1, hos2]

hospitals = [hos1, hos2, hos3]
residents = [res1, res2, res3]

match(residents, hospitals)
