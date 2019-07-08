from tkinter import *
import admin_back

def insert_text():
       admin_back.insert(trainnumber_text.get(),berthpreference_text.get(),coach_text.get(),departuretime_text.get(),arrivaltime_text.get())
       list1.delete(0,END)
       list1.insert(END,trainnumber_text.get(),berthpreference_text.get(),coach_text.get(),departuretime_text.get(),arrivaltime_text.get())

def view_text():
    list1.delete(0,END)
    for rows_view in admin_back.view():
        list1.insert(END,rows_view)

def delete_text():
    admin_back.delete(trainnumber_text.get())


def update_text():
    admin_back.update(trainnumber_text.get(),berthpreference_text.get(),coach_text.get(),departuretime_text.get(),arrival_text.get())


def search_text():
    admin_back.search(trainnumber_text.get(),berthpreference_text.get())
    list1.delete(0, END)
    for rows_search in admin_back.search(trainnumber_text.get(),berthpreference_text.get()):
        list1.insert(END, rows_search)

window=Tk()


window.configure(bg="light yellow")


l0=Label(window,text="ONLINETRAINBOOKING",bg="white",fg="purple",font="Times 16")
l0.grid(row=0,column=1)

l1=Label(window,text="trainnumber",bg="white",fg="gray",font=" Gabriola 16")
l1.grid(row=1,column=1)

l2=Label(window,text="berthpreference",bg="white",fg="gray",font="Gabriola 16")
l2.grid(row=2,column=1)

l3=Label(window,text="coach",bg="white",fg="gray",font="Gabriola 16")
l3.grid(row=3,column=1)

l4=Label(window,text="departuretime",bg="white",fg="gray",font="Gabriola 16" )
l4.grid(row=4,column=1)

l5=Label(window,text="arrivaltime",bg="white",fg="gray",font="Gabriola 16 ")
l5.grid(row=5,column=1)


trainnumber_text= StringVar()
e1=Entry(window,textvariable=trainnumber_text,bg="white",fg="red",font=" Gabriola 16" )
e1.grid(row=1,column=2)

berthpreference_text= StringVar()
e2=Entry(window,textvariable=berthpreference_text,bg="white",fg="red",font=" Gabriola 16",)
e2.grid(row=2,column=2)

coach_text= StringVar()
e3=Entry(window,textvariable=coach_text,bg="white",fg="red",font=" Gabriola 16")
e3.grid(row=3,column=2)

departuretime_text= StringVar()
e4=Entry(window,textvariable=departuretime_text,bg="white",fg="red",font=" Gabriola 16")
e4.grid(row=4,column=2)

arrivaltime_text= StringVar()
e5=Entry(window,textvariable=arrivaltime_text,bg="white",fg="red",font=" Gabriola 16")
e5.grid(row=5,column=2)


list1=Listbox(window,height=6,width=37)
list1.grid(row=12,column=0,rowspan=6,columnspan=10)

sb1=Scrollbar(window)
sb1.grid(row=12,column=3,rowspan=40,columnspan=50)


b1=Button(window,text="insert",command=insert_text,bg="white",fg="gray",font=" Gabriola 16 ")
b1.grid(row=10,column=0)


b2=Button(window,text="delete",command=delete_text,bg="white",fg="gray",font=" Gabriola 16 ")
b2.grid(row=10,column=1)

b3=Button(window,text="update",command=update_text,bg="white",fg="gray",font=" Gabriola 16 ")
b3.grid(row=10,column=2)

b4=Button(window,text="search",command=search_text,bg="white",fg="gray",font=" Gabriola 16 ")
b4.grid(row=10,column=3)

b5=Button(window,text="view",command=view_text,bg="white",fg="gray",font=" Gabriola 16 ")
b5.grid(row=10,column=4)

window.mainloop()
