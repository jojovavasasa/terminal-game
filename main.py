import time

while True:
    time.sleep(1)
    print("hello") 
    time.sleep(1)
    print("fill in the blank")
    time.sleep(1)
    user_input = input("my name is _____: ")
    if user_input == "jeff":
        time.sleep(1)
        print("good job")
        break
    else:
        time.sleep(1)
        print("nope try again")
    