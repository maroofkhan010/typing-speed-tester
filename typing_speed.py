import random
import time
import json
with open("sentences.json",'r') as f:
    data=json.load(f)
new=data["sentences"]
while True:
    text=random.choice(new)
    print("TEXT:\n"+text)  
    start_time=time.time()  
    type=input("TYPE HERE:\n")
    end_time=time.time()
    total_time=end_time-start_time
    wpm=len(text.split())/total_time*60
    correct_char=0
    for i in range(min(len(text),len(type))):
        if text[i]==type[i]:
            correct_char+=1
    accuracy=correct_char/len(text)*100
    print()     
    print("RESULT")
    print(f"Time taken:{round(total_time,2)} seconds")
    print(f"Word Per Minute:{round(wpm,2)} WPM")
    print(f"Accuracy:{round(accuracy,2)} %")
    print()
    play_again=input("Do you want to play again yes/no").lower()
    if play_again=="no":
        print("Thanks for playing")
        break