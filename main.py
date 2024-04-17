import tkinter as tk
from tkinter import filedialog
import speech_recognition as sr

def recognize_speech():
    audio_file_path = file_path_entry.get()
    try:
        r = sr.Recognizer()
        with sr.AudioFile(audio_file_path) as source:
            audio = r.record(source)
        recognized_text_label.config(text="The audio file contains: " + r.recognize_google(audio))
    except sr.UnknownValueError:
        recognized_text_label.config(text="GSR failed to understand the audio contents.")
    except sr.RequestError:
        recognized_text_label.config(text="Couldn't get result from GSR...")

def browse_file():
    file_path = filedialog.askopenfilename(filetypes=[("Wave files", "*.wav")])
    if file_path:
        file_path_entry.delete(0, tk.END)
        file_path_entry.insert(0, file_path)

# Create the main window
window = tk.Tk()
window.title("Speech Recognition Program")

# Create a frame for input elements
input_frame = tk.Frame(window)
input_frame.pack(padx=10, pady=10)

# Entry for file path
file_path_label = tk.Label(input_frame, text="File Path:")
file_path_label.grid(row=0, column=0, sticky="w")

file_path_entry = tk.Entry(input_frame, width=50)
file_path_entry.grid(row=0, column=1, padx=5)

browse_button = tk.Button(input_frame, text="Browse", command=browse_file)
browse_button.grid(row=0, column=2, padx=5)

# Button to recognize speech
recognize_button = tk.Button(window, text="Recognize Speech", command=recognize_speech)
recognize_button.pack(pady=5)

# Label to display recognized text
recognized_text_label = tk.Label(window, wraplength=400)
recognized_text_label.pack(pady=5)

window.mainloop()
