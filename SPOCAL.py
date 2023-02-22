import tkinter as tk
import pyaudio
import speech_recognition as sr

# Initialize variables to keep track of score and current question
score = 0
current_question = 0
questions = [
    {"question": "1. What is the capital of France?", "answer": "paris"},
    {"question": "2. Which is the oldest language?", "answer": "tamil"},
    {"question": "3. What is the most popular search engine?", "answer": "google"},
    {"question": "4. Which is the smallest state in India?", "answer": "goa"},
    {"question": "5. Which is the biggest state in USA?", "answer": "alaska"},
    {"question": "6. Which is the largest planet in the solar system?", "answer": "jupiter"}
]

def get_audio_input():
    # Set up SpeechRecognition
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something!")
        audio = r.listen(source)
    try:
        return r.recognize_google(audio).lower()
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
        return ""
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
        return ""

def answer_question():
    global score
    answer = get_audio_input()
    if answer == questions[current_question]["answer"]:
        score += 100
        result_label.config(text="Correct!", fg="green", bg="white")
    else:
        result_label.config(text="Wrong!", fg="red", bg="white")
def get_name():
    name = get_audio_input().upper()
    name_label.config(text="Hi " + name)

def start_quiz():
    start_button.pack_forget()
    namey.pack_forget()
    question_label.pack()
    answer_button.pack()
    next_button.pack()
    quit_button.pack()


def next_question():
    global current_question
    current_question += 1
    if current_question == len(questions):
        end_quiz()
    else:
        question_label.config(text=questions[current_question]["question"])
        result_label.config(text="")

def end_quiz():
    
    question_label.config(text="Thanks for participating. Quiz complete! Your score is {}.".format(score), font=("Aerial",16),bg="red",fg="yellow")
    answer_button.config(state="disabled")
    next_button.config(state="disabled")

# Set up tkinter GUI
root = tk.Tk()
root.title("Spocal - Quiz Contest involving voice input")
root.config(bg="#87CEEB")
root.geometry("{}x{}".format(root.winfo_screenwidth(), root.winfo_screenheight()))
title_label = tk.Label(root, text="SPOCAL - Quiz Contest involving Voice Input", font=("Times New Roman", 24), bg="magenta", fg="black")
title_label.pack(pady=20)

name_label = tk.Label(root, text="Tell your name through mic after clicking name button below", font=("Helvetica", 20), bg="pink", fg="purple")
name_label.pack(pady=20)
namey = tk.Button(root, text="NAME",command=get_name, bg="yellow", fg="black", activebackground="#87CEEB", activeforeground="black", font=("TkDefaultFont", 16), width=10, height=2) 
namey.pack(pady=20)
start_button = tk.Button(root, text="START", command=start_quiz, bg="white", fg="dark blue", activebackground="#87CEEB", activeforeground="black", font=("TkDefaultFont", 16), width=10, height=2)
start_button.pack(pady=20)
question_label = tk.Label(root, text=questions[current_question]["question"], font=("Algerian", 20), bg="white", fg="blue")
question_label.pack(pady=50)
result_label = tk.Label(root, text="Click Answer button and Tell the Answer in Mic", font=("Aerial", 10), bg="white", fg="red")
result_label.pack()
answer_button = tk.Button(root, text="Answer", command=answer_question, bg="yellow", fg="red", activebackground="#87CEEB", activeforeground="black", font=("Aerial", 16), width=10, height=2)
answer_button.pack(pady=20)
next_button = tk.Button(root, text="Next", command=next_question, bg="green", fg="yellow", activebackground="#87CEEB", activeforeground="black", font=("Aerial", 16), width=10, height=2)
next_button.pack(pady=20)
quit_button = tk.Button(root, text="Quit", command=root.quit, bg="black", fg="white", activebackground="#87CEEB", activeforeground="black", font=("Aerial", 16), width=10, height=2)
quit_button.pack(pady=20)
root.mainloop()

