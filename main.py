from speechtotext import SpeechToText
import random
import time


num_to_guess = random.randint(1, 100)
# num_to_guess = 3
# print(num_to_guess)
stt = SpeechToText()
stop_speech = '......stopping the program now'
not_valid = True
confirm = 'random'
chance = stt.chance
while not_valid:
    time.sleep(0.5)
    stt.SpeakText("Please say number from 0-100 only")
    user_guess = stt.get_input()
    if user_guess == 'stop':
        stt.SpeakText(stop_speech)
        # time.sleep(5)
        break
    try:
        guess_num = int(user_guess)
    except ValueError:
        continue
    if (guess_num > 0) and (guess_num < 101):
        if guess_num == num_to_guess:
            stt.SpeakText("Congratulations!!!!!!!!You got it!!")
            time.sleep(0.3)
            stt.SpeakText("Want to play again??")
            while confirm != 'yes' and confirm != 'no':
                stt.SpeakText(" please say yes or no")
                confirm = stt.get_input()
            if confirm == 'yes':
                chance = stt.chance
                num_to_guess = random.randint(1, 100)
            else:
                stt.SpeakText("Thank you for playing")
                not_valid = False
        else:
            chance -= 1
            time.sleep(1)
            if guess_num > num_to_guess:
                print(f"You have {chance} guess left!   {guess_num}     HIGH")
                stt.SpeakText("Your guess was high")
            else:
                print(f"You have {chance} guess left!   {guess_num}     LOW")
                stt.SpeakText("Your guess was low")
        if chance == 0:
            not_valid = False
            stt.SpeakText("Game Over")
