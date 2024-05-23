from art import logo, vs
from game_data import data
import random
print(logo)

def format_data(account):
  first_name=account["name"]
  first_des=account["description"]
  first_country=account["country"]
  return f" {first_name}, a {first_des}, from {first_country}"

def check_answer(follower_a,follower_b,guess):
  if follower_a>follower_b:
    return guess=="a"
  else:
    return guess=="b"
  
game_continue=True
score=0
second=random.choice(data)
while game_continue:
  first=second
  second=random.choice(data)
  while first==second:
    second=random.choice(data)
  
  
  print(f"Compare A:{format_data(first)}")
  print(vs)
  print(f"Against B:{format_data(second)}")
  choice=input("Who has more followers? Type 'A' or 'B':").lower()
  
  follower_a=first["follower_count"]
  follower_b=second["follower_count"]
  is_check=check_answer(follower_a,follower_b,choice)
  print(logo)
  if is_check:
    score+=1
    print(f"You are correct! Your current score: {score}")
  else:
    game_continue=False
    print(f"Sorry you are wrong! Your final score: {score}")
    


