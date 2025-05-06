import time

question = "my name is _____: "
answer = "jeff"

while True:
    time.sleep(1)
    print("hello") 
    time.sleep(1)
    print("fill in the blank")
    time.sleep(1)
    user_input = input(question)
    if user_input == answer:
        time.sleep(1)
        print("good job")
        break
    else:
        time.sleep(1)
        print("nope try again")
    