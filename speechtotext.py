import speech_recognition
import speech_recognition as sr
import pyttsx3


class SpeechToText():
    def __init__(self):
        self.r = sr.Recognizer()
        self.dictionary = {
            'three 3': ['tree', 'free', 'shri', 'treat'],
            'stop stop': ['top'],
            'six 6': ['six', 'sex'],
            'no no': ['lo', 'low'],
            'fifty 50': ['shifty', 'chitti', 'city'],
            'eighty 80': ['iti', 'priti'],
            'two 2': ['tu', 'too', 'to'],
            'forty 40': ['potty', 'kutty'],
            'eleven 11': ['vivek'],
            'thirtytwo 32': ['kaddu'],
            'eightytwo 82': ['attitude'],
            'four 4': ['ko', 'oppo'],
            'fortyfive 45': ['fortified'],

        }

        self.chance = 10

    def SpeakText(self, command):
        engine = pyttsx3.init()
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[1].id)
        engine.setProperty('rate', 174)
        engine.say(command)
        engine.runAndWait()
        engine.stop()
        # except:
        #     print("Speech Engine access error")

    def get_input(self):
        while True:
            try:
                with sr.Microphone() as source2:
                    # wait for a second to let recognizer adjust the energy threshold based on the surrounding noise level
                    self.r.adjust_for_ambient_noise(source2, duration=0.05)
                    # listens for the user's input
                    audio2 = self.r.listen(source2)
                    print("Recognizing Now... ")
                    # Using google to recognize audio
                    MyText = self.r.recognize_google(audio2)
                    MyText = MyText.lower()
                    for key, value in self.dictionary.items():
                        for item in value:
                            if MyText == item:
                                MyText = key.split()[1]
                    print(MyText)
                    self.SpeakText("You said " + MyText + "?")
                    return MyText
            except sr.UnknownValueError:
                self.SpeakText("Couldn't recognize the voice input")
