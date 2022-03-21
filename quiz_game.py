print("Welcome to the Quiz game:")

playing=input("Do You Want To Play?(type 'yes' to keep playing):")
if playing.lower()!="yes":
    quit()
name=input("Enter your name:")
questions=["what is IP","Who is father of computer","What is WWW"]
answers=["internet protocol","charles babbage","world wide web"]
score=0
for i in range(len(questions)):
    ans=input(questions[i]+":")
    if ans.lower()==answers[i]:
        print("correct")
        score+=1
    else:
        print("incorrect")
print("The score of "+ name + " is:"+str(score))





