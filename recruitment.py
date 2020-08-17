def main():
	#write your code here
  skills=["Python","C++","Javascript","Juggling","Running","Eating"]
  cv={}
  print("Welcome to the special recruitment program, please answer the following questions:")
  name=input("What's your name?")
  cv["name"]=name
  age=input("How old are you?")
  cv["age"]=int(age)
  experience=input("How many years of experience do you have?")
  cv["experience"]=int(experience)
  cv["skills"]=[]
  print("Skills:")
  s=1
  for k in skills:
    
    print("%d. %s"%(s,k))
    s=s+1
  sk1=input("Choose a skill from above by entering its number:") 
  sk2=input("Choose another skill from above by entering its number:") 
  cv["skills"].append(skills[(int(sk1)-1)])
  cv["skills"].append(skills[(int(sk2)-1)])
 
  if cv["age"]>=25 and cv["age"]<=40 and cv["experience"]>5 and skills[5] in cv["skills"]:
    # for k in cv["skills"]:
    #   if skills[5] == cv["skills"]:
      print("You have been accepted, %s"%(cv["name"]))


  else:
    print("You have been rejected %s"%(cv["name"]))  

if __name__ == '__main__':
	main()
