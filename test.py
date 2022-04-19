# pointer = 'string'
# int(pointer)

# keys = []
# dictionary = {
#             'three': ['tree', 'free', 'shri', 'treat'],
#             'stop': ['top'],
#             'six': ['six', 'sex'],
#             'no': ['lo', 'low']
# }
# for key in dictionary.keys():
#     keys.append(key)
# print(keys)
# print(len(dictionary))
# print(dictionary.items())

import pyttsx3
engine = pyttsx3.init()
voices = engine.getProperty('voices')
for voice in voices:
    print(voice, voice.id)
    engine.setProperty('voice', voice.id)
    engine.say("Hello World!")
    engine.runAndWait()
    engine.stop()