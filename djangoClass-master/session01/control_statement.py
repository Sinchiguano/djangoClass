medical_exam=True
knowleged=74



if medical_exam is True:
    print(f"The exam was giving successfully!")
else:
    print("The exam was never taken....")



if medical_exam is True and knowleged>=60:
    print(f"The exam was taken and the score is acceptable !")
else:
    print("The exam was never taken, therefore it does not pass....")


score_student=80

if score_student>=75:
    print("The license is granted successfully....")
elif score_student<70 and score_student<50:
    print('Try again to take the exam')
else:
    print('Start again the process ..')



language="dark"


if language=="Python":
    print("I suggest you to use Django....")

elif language=="PHP":
    print('Use Laravel')
elif language=="dark":
    print("Use Flutter")
elif language=="Javascrip":
    print("I suggest you to use Angular")
else:
    print("No framework for you")
 
 
# from 3,10

# match language:
#     case "Python":
#         print("I suggest to use Django")
#     case "Dark":
#         print("Flutter")
#     case "Javascript":
#         print("angular")
#     case _:
#         print("no framework for you ")


score =10

message="You are done"

if score>=60:
    print (message)



messageOne="You approved" if score>=60 else "You failed"


