# Typeed

Basically Typeed is short form of Typing Speed. It monitors your typing speed and gives you WPM, Accuracy.

**WPM** means "Words per minute" and is based on this calculation:
```
wpm=int((len(s)*60)/(elapsed_time*5))
```
**Accuracy** is based on the calculation:
```
accuracy=(correct_characters)*100/(total_characters_in_sentence)
```
