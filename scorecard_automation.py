import tkinter as tk
from tkinter import *
from os import closerange
import requests
import bs4


import sched, time
s = sched.scheduler(time.time, time.sleep)
def do_something(sc): 
    link = 'https://www.cricbuzz.com/live-cricket-scorecard/36056/engw-vs-indw-3rd-t20i-india-women-tour-of-england-2021'
    res = requests.get(link)
    soup = bs4.BeautifulSoup(res.text ,'html.parser')
    details = soup.select('.cb-col .cb-col-100 .cb-scrd-hdr-rw')
    root = tk.Tk()
    root.title("Scorecard")
    root.configure(bg ="black")
    T = tk.Text(root, height=5, width=40)
    T.pack()
    quote =""

    for x in details[::-1]:
        quote = x.text.lstrip()
        q ="\n"
        T.insert(tk.END,quote)
        T.insert(tk.END, q)
    tk.mainloop()
    s.enter(60, 1, do_something, (sc,))

s.enter(60, 1, do_something, (s,))
s.run()





