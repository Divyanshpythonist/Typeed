import random
import time
import timeit
print("TYPING SPEED TEST")
k=0
random_sentences=['The fish listened intently to what the frogs had to say.','It was the best sandcastle he had ever seen.','Wisdom is easily acquired when hiding under the bed with a saucepan on your head.',"The elephant didn't want to talk about the person in the room.",'She traveled because it cost the same as therapy and was a lot more enjoyable.','When transplanting seedlings, candied teapots will make the task easier.',"Now I need to ponder my existence and ask myself if I'm truly real",'Never underestimate the willingness of the greedy to throw you under the bus.','There were white out conditions in the town; subsequently, the roads were impassable.','The Japanese yen for commerce is still well-known.']
#r=random.randint(0, 9)
w=random.choice(random_sentences)
total_characters_in_sentence=len(w)
correct_characters=0
print(w)
s=''
start_time=time.time()
#elapsed_time=timeit.timeit('s=input("Type the above test : ")',number=1)
s=input("Type the above test : ")
end_time=time.time()
for i in range(0,len(s)):
    if w[i]==s[i]:
        correct_characters+=1
elapsed_time = end_time-start_time
accuracy=(correct_characters)*100/(total_characters_in_sentence)
wpm=int((len(s)*60)/(elapsed_time*5))
print("Time : ",elapsed_time," secs \t Accuracy : ",accuracy," % \t Wpm : ",wpm)
