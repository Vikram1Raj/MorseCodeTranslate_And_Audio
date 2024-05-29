import tkinter as tk
# from tkinter import ttk
import ttkbootstrap as ttk

import MorseCodeModule as mcm
import MorseAudioModule as mam

# import threading 
# import queue


morseGenerator = mcm.morseCode()
morseLetter = morseGenerator.morse_dict()

# audio_queue = queue.Queue()

def textTranslate():
  input_res = input_string.get().lower()
  input_conv = ""

  for i in input_res:
    if i in morseLetter:
      input_conv += morseLetter[i] + "  "


  output_string.set(input_conv)
  audioCallback()

def getAudio():
  input_res = input_string.get().lower()

  audioGenerator = mam.soundGen()
  audioGenerator.mainGen(input_res)

def audioCallback():
  # threading.Thread(target=getAudio).start()
  root.after(500,lambda: getAudio())


def stopAudio():

  # audio_queue.put("stop")
  root.destroy()


root = ttk.Window(themename="darkly")
root.title("Morse Code Generator")
root.geometry("1000x200")

#Label
title_lab = ttk.Label(master=root,text = "Enter Text ",font="Roboto 20 bold")
title_lab.pack()

#Input
inputFrame = ttk.Frame(master=root)
input_string = tk.StringVar()
input_entry = ttk.Entry(
  master=inputFrame, 
  textvariable=input_string,
  bootstyle = "info")
input_entry.pack(side="left",padx=10)

#Button
translate_button = ttk.Button(
  master=inputFrame,
  text="Translate",
  bootstyle = "info",
  command=textTranslate)

translate_button.pack(side="left")
inputFrame.pack(pady = 10)

#Output
output_string = tk.StringVar()
output_text = ttk.Label(
  master=root,
  text = "OUTPUT",
  font="Roboto 30 bold",
  textvariable=output_string)
output_text.pack(pady = 10)

root.protocol("WM_DELETE_WINDOW",stopAudio)

root.mainloop()



