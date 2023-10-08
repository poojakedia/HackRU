import tkinter as tk
from tkinter import ttk
from tkinter import *
from PIL import Image, ImageTk
import organizing

global count_correct


class tkinterApp(tk.Tk):

  def __init__(self, *args, **kwargs):
    tk.Tk.__init__(self, *args, **kwargs)

    container = tk.Frame(self)
    container.pack(side="top", fill="both", expand=True)
    container.grid_rowconfigure(0, weight=1)
    container.grid_columnconfigure(0, weight=1)
    self.frames = {}

    for F in (Landing, Q1, Q2, Q3, Q4, Q5, Ending):

      frame = F(container, self)

      # initializing frame of that object from
      # startpage, page1, page2 respectively with
      # for loop

      self.frames[F] = frame

      frame.grid(row=0, column=0, sticky="nsew")

      self.show_frame(Landing)
      #self.show_frame(StartPage)
  def show_frame(self, cont):
    frame = self.frames[cont]
    frame.tkraise()


class Landing(tk.Frame):

  def __init__(self, parent, controller):
    tk.Frame.__init__(self, parent)
    color_dustypink = '#A04668'
    color_darkestpink = '#DF125A'
    color_darkerpink = '#F0296E'
    color_darkpink = '#FF4888'
    color_pink = '#fa82ac'
    color_lightpink = '#EC99B6'
    color_lightestpink = '#FFD7E5'
    frame1 = Frame(self, height=30, width=400, bg=color_lightpink)
    frame1.grid(row=0, column=0)

    # label of frame Layout 2
    logo_img = ImageTk.PhotoImage(Image.open('logo.png').resize((500, 100)))
    label = tk.Label(frame1, image=logo_img, bg=color_lightpink)
    label.image = logo_img
    label.grid(row=1, column=1, padx=10, pady=10)
    # buttons
    buttonQ1 = tk.Button(frame1,
                         text="Question 1",
                         fg=color_lightpink,
                         command=lambda: controller.show_frame(Q1))
    buttonQ1.grid(row=2, column=1, padx=30, pady=30)

    buttonQ2 = tk.Button(frame1,
                         text="Question 2",
                         fg=color_pink,
                         command=lambda: controller.show_frame(Q2))
    buttonQ2.grid(row=3, column=1, padx=10, pady=10)

    buttonQ3 = tk.Button(frame1,
                         text="Question 3",
                         fg=color_darkpink,
                         command=lambda: controller.show_frame(Q3))
    buttonQ3.grid(row=4, column=1, padx=10, pady=10)

    buttonQ4 = tk.Button(frame1,
                         text="Question 4",
                         fg=color_darkerpink,
                         command=lambda: controller.show_frame(Q4))
    buttonQ4.grid(row=5, column=1, padx=10, pady=10)

    buttonQ5 = tk.Button(frame1,
                         text="Question 5",
                         fg=color_darkestpink,
                         command=lambda: controller.show_frame(Q5))
    buttonQ5.grid(row=6, column=1, padx=10, pady=10)
    bunny_left_img = ImageTk.PhotoImage(Image.open('landing_rabbit.png').resize((100, 100)))
    bunny_left_lbl = tk.Label(frame1, image=bunny_left_img, bg=color_lightpink)
    bunny_left_lbl.image = bunny_left_img
    bunny_left_lbl.grid(row = 6, column = 0)
    bunny_rt_img = ImageTk.PhotoImage(Image.open('landing_bunny.png').resize((100, 100)))
    bunny_rt_lbl = tk.Label(frame1, image=bunny_rt_img, bg=color_lightpink)
    bunny_rt_lbl.image = bunny_rt_img
    bunny_rt_lbl.grid(row = 6, column = 3)


class Q1(tk.Frame):

  def __init__(self, parent, controller):
    tk.Frame.__init__(self, parent)
    key_1 = ["count = 0", "heights[i]", "heights[i+1]", "count++", "count"]
    frame2 = Frame(self, height=30, width=400, bg = "pink")
    frame2.grid(row=1, column=0)
    # label of frame Layout 2
    label = tk.Label(frame2, text="Question 1", bg = "pink")
    label.grid(row=1, column=0)
    randomized_word_bank = organizing.randomize(key_1)
    wordbank_label = tk.Label(frame2,
                              text=randomized_word_bank,
                              font=("Times", 12), bg = "pink")
    wordbank_label.grid(row=0, column=0)
    code = '''
    Directions: In the textbox below write out the missing lines of code. 
    Seperate answers with a single comma (,). 
    Answers are case sensitive. Do not use spaces after the comma.
    
We have an array of heights, representing the altitude along a walking 
trail. Given start/end indexes into the array, return the number of "big" 
steps for a walk starting at the start index and ending at the end index. 
We'll say that step is big if it is 5 or more up or down. The start end end 
index will both be valid indexes into the array with start <= end.

public int bigHeights(int[] heights, int start, int end) {
    int _________;
    
    for(int i = start; i < end; i++) {
        if(Math.abs(__________ - ____________) >= 5)
            _______;
    }
                    
    return _____;
}'''

    def submit_answer():
      correct = True
      words = user_ans.get()
      user_ans_list = words.split(", ")
      count_correct = 0
      count_loop = 0
      while count_loop < len(user_ans_list):
        if user_ans_list[count_loop] == key_1[count_loop]:
          correct = True
          count_correct += 1
        else:
          correct = False
        count_loop += 1
      win = tk.Toplevel(background="pink")
      string = "You got " + str(count_correct) + " correct"
      feedback1 = "Congrats! Phill is so happy that you're getting better at JAVA"
      feedback2 = "Awww not quite... Phill is a little sad but maybe try again"

      l = tk.Label(win, text=string, font=("Times", 25), bg="pink")
      l.grid(row=2, column=0, padx=10, pady=10)
      logo_img = ImageTk.PhotoImage(Image.open('logo.png').resize((500, 100)))
      label = tk.Label(win, image=logo_img, bg="pink")
      label.image = logo_img
      label.grid(row=1, column=0, padx=10, pady=10)
      if count_correct == len(key_1):
        phill_img = ImageTk.PhotoImage(
            Image.open('cute-rabbit.png').resize((100, 100)))
        feedback_lbl = tk.Label(win, text=feedback1, bg="pink")
        feedback_lbl.grid(row=3, column=0)
      else:
        phill_img = ImageTk.PhotoImage(
            Image.open('sad-rabbit.png').resize((100, 100)))
        feedback_lbl = tk.Label(win, text=feedback2, bg="pink")
        feedback_lbl.grid(row=3, column=0)
      label_pill = tk.Label(win, image=phill_img, bg="pink")
      label_pill.image = phill_img
      label_pill.grid(row=4, column=0)
      try_again_btn = tk.Button(win, text="try again", bg="pink", command = lambda: [controller.show_frame(Q1), win.destroy()])
      try_again_btn.grid(row=5, column=0)
      

    label_code = tk.Label(frame2, text=code, wraplength=700, bg = "pink")
    label_code.grid(row=1, column=0)
    user_ans = tk.StringVar()

    ans_entry = tk.Entry(frame2,
                         textvariable=user_ans,
                         width=70,
                         font=("Times", 15))
    ans_entry.grid(row=2, column=0)
    print(user_ans.get())
    submit_button = tk.Button(
        frame2,
        width=20,
        text="Submit",
        command=lambda: [controller.show_frame(Ending),
                         submit_answer()])
    submit_button.grid(row=3, column=0)
    home_button = tk.Button(frame2,
                             width=20,
                             text="Return",
                             command=lambda: controller.show_frame(Landing))
    home_button.grid(row=4, column=0)


class Q2(tk.Frame):

  def __init__(self, parent, controller):
    tk.Frame.__init__(self, parent)
    key_2 = [
        "vacation", "day == 0 || day == 6", '"off"', '"10:00"',
        "day == 0 || day == 6", '"10:00"', '"7:00"'
    ]

    frame2 = Frame(self, height=30, width=400)
    frame2.grid(row=1, column=0)
    # label of frame Layout 2
    label = tk.Label(frame2, text="Question 2", bg = "pink")
    label.grid(row=0, column=0)
    randomized_word_bank = organizing.randomize(key_2)
    wordbank_label = tk.Label(frame2,
                              text=randomized_word_bank,
                              font=("Times", 12))
    wordbank_label.grid(row=0, column=0)
    code = '''
    Directions: In the textbox below write out the missing lines of code. 
    Seperate answers with a single comma (,). 
    Answers are case sensitive. Do not use spaces after the comma.
    
Given a day of the week encoded as 0=Sun, 1=Mon, 2=Tue, ...6=Sat, and a 
boolean indicating if we are on vacation, return a string of the form 
"7:00" indicating when the alarm clock should ring. Weekdays, the alarm 
should be "7:00" and on the weekend it should be "10:00". Unless we are on 
vacation -- then on weekdays it should be "10:00" and weekends it should 
be "off".

public String alarmClock(int day, boolean vacation) {
    if(________) {
        if(____________________)
            return _____;
        else
            return _______;
    }
                          
    if(____________________)
        return _______;
                                    
    return ______;
}'''

    def submit_answer():
      correct = True
      words = user_ans.get()
      user_ans_list = words.split(", ")
      count_correct = 0
      count_loop = 0
      while count_loop < len(user_ans_list):
        if user_ans_list[count_loop] == key_1[count_loop]:
          correct = True
          count_correct += 1
        else:
          correct = False
        count_loop += 1
      win = tk.Toplevel(background="pink")
      string = "You got " + str(count_correct) + " correct"
      feedback1 = "Congrats! Phill is so happy that you're getting better at JAVA"
      feedback2 = "Awww not quite... Phill is a little sad but maybe try again"

      l = tk.Label(win, text=string, font=("Times", 25), bg="pink")
      l.grid(row=2, column=0, padx=10, pady=10)
      logo_img = ImageTk.PhotoImage(Image.open('logo.png').resize((500, 100)))
      label = tk.Label(win, image=logo_img, bg="pink")
      label.image = logo_img
      label.grid(row=1, column=0, padx=10, pady=10)
      if count_correct == len(key_1):
        phill_img = ImageTk.PhotoImage(
            Image.open('cute-rabbit.png').resize((100, 100)))
        feedback_lbl = tk.Label(win, text=feedback1, bg="pink")
        feedback_lbl.grid(row=3, column=0)
      else:
        phill_img = ImageTk.PhotoImage(
            Image.open('sad-rabbit.png').resize((100, 100)))
        feedback_lbl = tk.Label(win, text=feedback2, bg="pink")
        feedback_lbl.grid(row=3, column=0)
      label_pill = tk.Label(win, image=phill_img, bg="pink")
      label_pill.image = phill_img
      label_pill.grid(row=4, column=0)
      try_again_btn = tk.Button(win, text="try again", bg="pink", command = lambda: [controller.show_frame(Q2), win.destroy()])
      try_again_btn.grid(row=5, column=0)

    label_code = tk.Label(frame2, text=code, wraplength=700)
    label_code.grid(row=1, column=0)
    user_ans = tk.StringVar()

    ans_entry = tk.Entry(frame2,
                         textvariable=user_ans,
                         width=70,
                         font=("Times", 15))
    ans_entry.grid(row=2, column=0)
    print(user_ans.get())
    submit_button = tk.Button(
        frame2,
        width=20,
        text="Submit",
        command=lambda: [controller.show_frame(Ending),
                         submit_answer()])
    submit_button.grid(row=3, column=0)
    home_button = tk.Button(frame2,
                             width=20,
                             text="Return",
                             command=lambda: [controller.show_frame(Landing)])
    home_button.grid(row=4, column=0)


class Q3(tk.Frame):

  def __init__(self, parent, controller):
    tk.Frame.__init__(self, parent)
    key_3 = [
        "str.length() == 0", '"@@"', "str.length() == 1", 'str + "@"',
        "str.substring(0, 2)"
    ]
    frame2 = Frame(self, height=30, width=400)
    frame2.grid(row=1, column=0)
    # label of frame Layout 2
    label = tk.Label(frame2, text="Question 3", bg = "pink")
    label.grid(row=0, column=0)
    randomized_word_bank = organizing.randomize(key_3)
    wordbank_label = tk.Label(frame2,
                              text=randomized_word_bank,
                              font=("Times", 12))
    wordbank_label.grid(row=0, column=0)
    code = '''
    Directions: In the textbox below write out the missing lines of code. 
    Seperate answers with a single comma (,). 
    Answers are case sensitive. Do not use spaces after the comma.
    
Given a string, return a string length 2 made of its first 2 chars. If the 
string length is less than 2, use '@' for the missing chars.

public String atFirst(String str) {
    if(_________________)
        return ____;
          
    if(_________________)
        return _________;
                    
    return __________________;
}'''

    def submit_answer():
      correct = True
      words = user_ans.get()
      user_ans_list = words.split(", ")
      count_correct = 0
      count_loop = 0
      while count_loop < len(user_ans_list):
        if user_ans_list[count_loop] == key_1[count_loop]:
          correct = True
          count_correct += 1
        else:
          correct = False
        count_loop += 1
      win = tk.Toplevel(background="pink")
      string = "You got " + str(count_correct) + " correct"
      feedback1 = "Congrats! Phill is so happy that you're getting better at JAVA"
      feedback2 = "Awww not quite... Phill is a little sad but maybe try again"

      l = tk.Label(win, text=string, font=("Times", 25), bg="pink")
      l.grid(row=2, column=0, padx=10, pady=10)
      logo_img = ImageTk.PhotoImage(Image.open('logo.png').resize((500, 100)))
      label = tk.Label(win, image=logo_img, bg="pink")
      label.image = logo_img
      label.grid(row=1, column=0, padx=10, pady=10)
      if count_correct == len(key_1):
        phill_img = ImageTk.PhotoImage(
            Image.open('cute-rabbit.png').resize((100, 100)))
        feedback_lbl = tk.Label(win, text=feedback1, bg="pink")
        feedback_lbl.grid(row=3, column=0)
      else:
        phill_img = ImageTk.PhotoImage(
            Image.open('sad-rabbit.png').resize((100, 100)))
        feedback_lbl = tk.Label(win, text=feedback2, bg="pink")
        feedback_lbl.grid(row=3, column=0)
      label_pill = tk.Label(win, image=phill_img, bg="pink")
      label_pill.image = phill_img
      label_pill.grid(row=4, column=0)
      try_again_btn = tk.Button(win, text="try again", bg="pink", command = lambda: [controller.show_frame(Q3), win.destroy()])
      try_again_btn.grid(row=5, column=0)

    label_code = tk.Label(frame2, text=code, wraplength=700)
    label_code.grid(row=1, column=0)
    user_ans = tk.StringVar()

    ans_entry = tk.Entry(frame2,
                         textvariable=user_ans,
                         width=70,
                         font=("Times", 15))
    ans_entry.grid(row=2, column=0)
    print(user_ans.get())
    submit_button = tk.Button(
        frame2,
        width=20,
        text="Submit",
        command=lambda: [controller.show_frame(Ending),
                         submit_answer()])
    submit_button.grid(row=3, column=0)
    home_button = tk.Button(frame2,
                             width=20,
                             text="Return",
                             command=lambda: [controller.show_frame(Landing)])
    home_button.grid(row=4, column=0)


class Q4(tk.Frame):

  def __init__(self, parent, controller):
    tk.Frame.__init__(self, parent)
    key_4 = ["str.length() - 1", "last", "str", "last"]
    frame2 = Frame(self, height=30, width=400)
    frame2.grid(row=1, column=0)
    # label of frame Layout 2
    label = tk.Label(frame2, text="Question 4", bg = "pink")
    label.grid(row=0, column=0)
    randomized_word_bank = organizing.randomize(key_4)
    wordbank_label = tk.Label(frame2,
                              text=randomized_word_bank,
                              font=("Times", 12))
    wordbank_label.grid(row=0, column=0)
    code = '''
    Directions: In the textbox below write out the missing lines of code. 
    Seperate answers with a single comma (,).
    Answers are case sensitive. Do not use spaces after the comma.
    
Given a string, take the last char and return a new string with the last 
char added at the front and back, so "cat" yields "tcatt". The original 
string will be length 1 or more.

public String backAround(String str) {
    char last = str.charAt(________________);
    return ____ + ___ + ____;
}'''

    def submit_answer():
      correct = True
      words = user_ans.get()
      user_ans_list = words.split(", ")
      count_correct = 0
      count_loop = 0
      while count_loop < len(user_ans_list):
        if user_ans_list[count_loop] == key_1[count_loop]:
          correct = True
          count_correct += 1
        else:
          correct = False
        count_loop += 1
      win = tk.Toplevel(background="pink")
      string = "You got " + str(count_correct) + " correct"
      feedback1 = "Congrats! Phill is so happy that you're getting better at JAVA"
      feedback2 = "Awww not quite... Phill is a little sad but maybe try again"

      l = tk.Label(win, text=string, font=("Times", 25), bg="pink")
      l.grid(row=2, column=0, padx=10, pady=10)
      logo_img = ImageTk.PhotoImage(Image.open('logo.png').resize((500, 100)))
      label = tk.Label(win, image=logo_img, bg="pink")
      label.image = logo_img
      label.grid(row=1, column=0, padx=10, pady=10)
      if count_correct == len(key_1):
        phill_img = ImageTk.PhotoImage(
            Image.open('cute-rabbit.png').resize((100, 100)))
        feedback_lbl = tk.Label(win, text=feedback1, bg="pink")
        feedback_lbl.grid(row=3, column=0)
      else:
        phill_img = ImageTk.PhotoImage(
            Image.open('sad-rabbit.png').resize((100, 100)))
        feedback_lbl = tk.Label(win, text=feedback2, bg="pink")
        feedback_lbl.grid(row=3, column=0)
      label_pill = tk.Label(win, image=phill_img, bg="pink")
      label_pill.image = phill_img
      label_pill.grid(row=4, column=0)
      try_again_btn = tk.Button(win, text="try again", bg="pink", command = lambda: [controller.show_frame(Q4), win.destroy()])
      try_again_btn.grid(row=5, column=0)

    label_code = ttk.Label(frame2, text=code, wraplength=700)
    label_code.grid(row=1, column=0)
    user_ans = tk.StringVar()

    ans_entry = tk.Entry(frame2,
                         textvariable=user_ans,
                         width=70,
                         font=("Times", 15))
    ans_entry.grid(row=2, column=0)
    print(user_ans.get())
    submit_button = tk.Button(
        frame2,
        width=20,
        text="Submit",
        command=lambda: [controller.show_frame(Ending),
                         submit_answer()])
    submit_button.grid(row=3, column=0)
    home_button = tk.Button(frame2,
                             width=20,
                             text="Return",
                             command=[lambda: controller.show_frame(Landing)])
    home_button.grid(row=4, column=0)


class Q5(tk.Frame):

  def __init__(self, parent, controller):
    tk.Frame.__init__(self, parent)
    key_5 = [
        "str.length()", "count = 0", "i = 0", "inc = 1", "str.length()",
        "result[count]", "str.charAt(i)", "count++", "inc", "1", "3", "1",
        "result", "0", "count"
    ]
    frame2 = Frame(self, height=30, width=400)
    frame2.grid(row=1, column=0)
    # label of frame Layout 2
    label = tk.Label(frame2, text="Question 5", bg = "pink")
    label.grid(row=0, column=0)
    randomized_word_bank = organizing.randomize(key_5)
    wordbank_label = tk.Label(frame2,
                              text=randomized_word_bank,
                              font=("Times", 12), bg = "pink")
    wordbank_label.grid(row=0, column=0)
    code = '''
    Directions: In the textbox below write out the missing lines of code. 
    Seperate answers with a single comma (,). 
    Answers are case sensitive. Do not use spaces after the comma.
    
Given a string, return a string made of the chars at indexes 
0,1, 4,5, 8,9 ... so "kittens" yields "kien".

public String altPairs(String str) {
    char[] result = new char[____________];
    int _________;
      
    int _____;
    int _______;
    while(i < ____________) {
        ____________ = _____________;
        _______;
        i += ___;
                            
        if(inc == _)
            inc = _;
        else
            inc = _;
    }
                                                    
    return new String(______, _, _____);
}'''

    def submit_answer():
      correct = True
      words = user_ans.get()
      user_ans_list = words.split(", ")
      count_correct = 0
      count_loop = 0
      while count_loop < len(user_ans_list):
        if user_ans_list[count_loop] == key_1[count_loop]:
          correct = True
          count_correct += 1
        else:
          correct = False
        count_loop += 1
      win = tk.Toplevel(background="pink")
      string = "You got " + str(count_correct) + " correct"
      feedback1 = "Congrats! Phill is so happy that you're getting better at JAVA"
      feedback2 = "Awww not quite... Phill is a little sad but maybe try again"

      l = tk.Label(win, text=string, font=("Times", 25), bg="pink")
      l.grid(row=2, column=0, padx=10, pady=10)
      logo_img = ImageTk.PhotoImage(Image.open('logo.png').resize((500, 100)))
      label = tk.Label(win, image=logo_img, bg="pink")
      label.image = logo_img
      label.grid(row=1, column=0, padx=10, pady=10)
      if count_correct == len(key_1):
        phill_img = ImageTk.PhotoImage(
            Image.open('cute-rabbit.png').resize((100, 100)))
        feedback_lbl = tk.Label(win, text=feedback1, bg="pink")
        feedback_lbl.grid(row=3, column=0)
      else:
        phill_img = ImageTk.PhotoImage(
            Image.open('sad-rabbit.png').resize((100, 100)))
        feedback_lbl = tk.Label(win, text=feedback2, bg="pink")
        feedback_lbl.grid(row=3, column=0)
      label_pill = tk.Label(win, image=phill_img, bg="pink")
      label_pill.image = phill_img
      label_pill.grid(row=4, column=0)
      try_again_btn = tk.Button(win, text="try again", bg="pink", command = lambda: [controller.show_frame(Q5), win.destroy()])
      try_again_btn.grid(row=5, column=0)

    label_code = tk.Label(frame2, text=code, wraplength=700, bg = "pink")
    label_code.grid(row=1, column=0)
    user_ans = tk.StringVar()

    ans_entry = tk.Entry(frame2,
                         textvariable=user_ans,
                         width=70,
                         font=("Times", 15))
    ans_entry.grid(row=2, column=0)
    print(user_ans.get())
    submit_button = tk.Button(
        frame2,
        width=20,
        text="Submit",
        command=lambda: [controller.show_frame(Ending),
                         submit_answer()])
    submit_button.grid(row=3, column=0)
    home_button = tk.Button(frame2,
                             width=20,
                             text="Return",
                             command=[lambda: controller.show_frame(Landing)])
    home_button.grid(row=4, column=0)


class Ending(tk.Frame):

  def __init__(self, parent, controller):
    color_dustypink = '#A04668'
    color_darkestpink = '#DF125A'
    color_darkerpink = '#F0296E'
    color_darkpink = '#FF4888'
    color_pink = '#fa82ac'
    color_lightpink = '#EC99B6'
    color_lightestpink = '#FFD7E5'
    tk.Frame.__init__(self, parent)
    frame1 = Frame(self, height=30, width=400)
    frame1.grid(row=1, column=0)


app = tkinterApp()
app.mainloop()
