from tkinter import *
import tkinter as tk
from tkinter.ttk import *
from estimate import LSTM_prediction
from svm import SVM_prediction
from crawlscrape import get_stocks, get_excel, crawl_scrape
import time

window = Tk()
window.resizable(False,False)
window.title("Stock Market Prediction")
window.geometry('600x900')

lbl1 = Label(window, text="enter the stock name you want:", font=("arail bold", 15))
lbl1.place(x=150, y=50)

txt1 = Entry(window, width=20)
txt1.place(x=220, y=100)



def get_text():
    return txt1.get()


# to scraope stocks
def check():
    crawl_scrape(get_text())


# to call tarin and prediction
def predict():
    if combo.get() == 'LSTM':
        lstm_dict = LSTM_prediction(stock_name=get_text())
        lbl4.config(text="The value predicted: "+str(lstm_dict["prediction"])+"\nWith RMSE rate: "+str(lstm_dict["error"]))


    elif combo.get() == 'SVM':
        cj = SVM_prediction(stock_name=get_text())
        lbl4.config(text=cj.to_string())


seprator = Separator(window, orient="horizontal")
seprator.place(relx=0, rely=0.30, relwidth=1, relheight=8)
btn1 = tk.Button(window, text="Statues Check", bg="silver", fg='black', command=lambda: check())
btn1.place(x=240, y=200)

combo = Combobox(window, width =25)
combo['values'] = ('Choose a training method','SVM','LSTM')
combo.current(0)
combo.place(x=400, y=300)


btn2 = tk.Button(window, text="Predict", bg="silver", fg='black', command=predict)
btn2.place(x=255, y=400)


lbl4 = Label(window, text="results",font=("arail bold", 10))
lbl4.place(x=250, y=450)

btn3=tk.Button(window, text="save Excel", bg="silver", fg='black', command=lambda: get_excel(stock_name=get_text()))
btn3.place(x=250,y=550)



window.mainloop()