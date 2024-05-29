import time
import pyaudio
import numpy as np

import MorseCodeModule as mc

FREQ = 850 # C5=Do
RATE = 44100 # times/sec

class soundGen():


  def make_sin(self,length):
      length = int(length * RATE)
      factor = FREQ * np.pi * 2 / RATE
      return np.sin(np.arange(length) * factor)


  def play_tone(self,length):
    sin = self.make_sin(float(length))
    self.stream.write(sin.astype(np.float32).tobytes())

  def bit_check(self,letter):
    if letter == " ":
      time.sleep(0.5)

    if letter != " ":
      for num in self.morseDict[letter]:
        if num == 0:
          self.play_tone(0.08)
        else:
          self.play_tone(0.2)

        time.sleep(0.1)
      time.sleep(0.1)



  def scan_dict(self,string):
    for i in string.lower():
      if i in self.morseDict:
          self.bit_check(i)
                 
  def mainGen(self,string):

    morseGenerator = mc.morseCode()
    self.morseDict = morseGenerator.morseIntDict(morseGenerator.morse_dict())

    p = pyaudio.PyAudio()
    self.stream = p.open(format=pyaudio.paFloat32, channels=1, rate=RATE, output=1)

    self.scan_dict(string)

    self.stream.close()
    p.terminate()

  def terminateProgram(self):
    self.terminateProgramFlag = True


if __name__ == "__main__":
  soundGenerator = soundGen()
  soundGenerator.mainGen()

