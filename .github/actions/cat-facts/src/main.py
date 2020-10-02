import requests
import random
import sys

#make http GET request to fetch the cat-fact API
cat_url =  "https://cat-fact.herokuapp.com/facts"
r = requests.get(cat_url)
r_obj_list = r.json()["all"]

#create an empty list to store individual facts
fact_list = []

# add the text of each object into the fact_list
for fact in r_obj_list:
    fact_list.append(fact["text"])

# select random variable from the fact list and return it into the variable
# called random_fact so that we can use it
def select_random_fact(fact_arr):
    return fact_arr[random.randint(0, len(fact_list)+1)]

random_fact = select_random_fact(fact_list)

print(random_fact)

print(f"::set-output name=fact::{random_fact}")
