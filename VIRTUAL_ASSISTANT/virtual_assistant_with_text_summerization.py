from tkinter import *
import wolframalpha
import wikipedia
from tkinter import messagebox
import transformers
from transformers import pipeline

#main function

def text_summary():
    summary_extraction = pipeline("summarization")
    article = text_input.get()
    ami = summary_extraction(article,max_length = 120,min_length = 40,do_sample = False)
    messagebox.showinfo("Result",ami)

def jarvis():
    #store the input in query variable
    query = query_input.get()
    print(query)
    try:
        #it will try wolframalpha
        app_id = "T5VEJ9-KXP684Q2A4"
        client = wolframalpha.Client(app_id)
        res = client.query(query)
        answer = next(res.results).text
    except:
        #wikipedia we cawrite whole summary but it will be hard to read.
        #we are displaying summary upto 5 sentence only
        answer =  wikipedia.summary(query,sentences = 5)
    #displays the output to the user
    messagebox.showinfo("Result",answer)
    print(answer)

text_input = Entry(root,width=50)
text_input.pack(ipady=6,pady=(1,15))
text_sumarry = Button(root,text ="TEXT SUMMARY",bg="white",fg='black',padx=4,pady=4,
                      borderwidth=6,font='Helvetica 10 bold', command = text_summary)
text_sumarry.pack()

root.mainloop()


root = Tk()
#background colour
root.configure(bg='orange')
root.geometry("600x300")
root.title("JARVIS")
root_label = Label(root, text = "Hello! How can i assist you",bg="purple",fg = "black",
                   padx=10,pady=10,borderwidth=7,
                   relief = RAISED,font='Helvetica 10 bold')
root_label.pack()
#takes input
query_input = Entry(root,width=50)
query_input.pack(ipady=6,pady=(1,15))
btn = Button(root,text = "ENTER QUERY",bg="white",fg='black',padx=4,pady=4,borderwidth=6,font='Helvetica 10 bold',
             command = jarvis)
btn.pack()
#new  text summary button