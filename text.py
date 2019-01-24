
import tkinter
from tkinter import *
import search
global hq
hq={}
root =tkinter.Tk()
root.title("周报表数据查询")
hq["tw"]="本周累计"
hq["lw"]="上周累计"
hq["ly"]="去年同期"
hq["lmw"]="上月同期"
hq["tm"]="本月累计"
hq["lm"]="上月累计"
i=0
for k,v in hq.items():
            k.__init__()
            Checkbutton(root,text = v,width=8,command=k).grid(row=0,column =i+1)
            i+=1
def tw():
    print("123544555454")
for k,v in enumerate(["促销收入：","储值卡消费：","交易次数：","客单价："]):
    Label(root,text = v).grid(row=k+8+2,column = 0,sticky=E )

Checkbutton(root,text =12333,width=8,command=tw).grid(row=0,column =3)

root.mainloop()