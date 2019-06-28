from gtts import gTTS
import os
mytext="Welcome!! Supriyo to your platform"
Language="en"
myobj=gTTS(text=mytext, lang=Language, slow=False)
myobj.save("Welcome1.mp3")
os.system("mpg321 Welcome1.mp3")
