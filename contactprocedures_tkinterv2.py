from tkinter import *
from tkinter import ttk

ticket_info = {"Name":[], "Ticket#":[], "Reason":[], "MyName":[], "MyPhone":[], "MyHours":[]}
def magic(*args):
    ticket_info["Name"] = (cg_name.get())
    ticket_info["Ticket#"] = (ticket_number.get())
    ticket_info["Reason"] = (reason.get())
    ticket_info["MyName"] = (myname.get())
    ticket_info["MyPhone"] = (myphone.get())
    ticket_info["MyHours"] = (myhours.get())
    with open("contact_procedures.txt", 'r') as input:
        with open("contact_procedures_output.txt", 'w') as output:
            for line in input:
                line = line.replace('TICKETNUMBER', (ticket_info["Ticket#"]))
                line = line.replace('CAREGIVER', (ticket_info["Name"]))
                line = line.replace('MYNAME', (ticket_info["MyName"]))
                line = line.replace('MYPHONE', (ticket_info["MyPhone"]))
                line = line.replace('MYHOURS', (ticket_info["MyHours"]))
                line = line.replace('ISSUE', (ticket_info["Reason"]))
                output.write(line)
    text.delete('1.0', END)
    with open('contact_procedures_output.txt', 'r') as g:
        text.insert('1.0', g.read())

def donothing():
    x = 0

root = Tk()
root.title('Contact Template Auto-Fill')


mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

#menubar
root.option_add('*tearOff', FALSE)
menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label='New', command=donothing)
filemenu.add_command(label='Open', command=donothing)
filemenu.add_command(label='Save', command=donothing)
filemenu.add_separator()
filemenu.add_command(label='Exit', command=root.quit)
menubar.add_cascade(label='File', menu=filemenu)

helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label='Help Index', command=donothing)
helpmenu.add_command(label='About...', command=donothing)
menubar.add_cascade(label='Help', menu=helpmenu)



#CG name
cg_name = StringVar()
cg_name_entry = ttk.Entry(mainframe, width=20, textvariable=cg_name)
cg_name_entry.grid(column=2, row=1, sticky=(W, E))

#ticket number
ticket_number = StringVar()
ticket_number_entry = ttk.Entry(mainframe, width=20, textvariable=ticket_number)
ticket_number_entry.grid(column=2, row=2, sticky=(W, E))

#Reason for ticket
reason = StringVar()
reason_entry = ttk.Entry(mainframe, width=40, textvariable=reason)
reason_entry.grid(column=2, row=3, sticky=(W, E))

#My Name
myname = StringVar()
myname_entry = ttk.Entry(mainframe, width=40, textvariable=myname)
myname_entry.grid(column=4, row=1, sticky=(W, E))

#My phone number
myphone = StringVar()
myphone_entry = ttk.Entry(mainframe, width=40, textvariable=myphone)
myphone_entry.grid(column=4, row=2, sticky=(W, E))

#My hours
myhours = StringVar()
myhours_entry = ttk.Entry(mainframe, width=40, textvariable=myhours)
myhours_entry.grid(column=4, row=3, sticky=(W, E))

#Labels
ttk.Label(mainframe, text="CG name?: ").grid(column=1, row=1, sticky=W)
ttk.Label(mainframe, text="Ticket #?: ").grid(column=1, row=2, sticky=W)
ttk.Label(mainframe, text="Reason for ticket?: ").grid(column=1, row=3, sticky=W)
ttk.Label(mainframe, text="My Name: ").grid(column=3, row=1, sticky=W)
ttk.Label(mainframe, text="My Phone #: ").grid(column=3, row=2, sticky=W)
ttk.Label(mainframe, text="My Hours: ").grid(column=3, row=3, sticky=W)

#textbox
text = Text(mainframe, width=100, height=40, wrap = "word")
with open('contact_procedures.txt', 'r') as f:
    text.insert('1.0', f.read())

text.grid(column = 0, row = 5, columnspan=5, sticky = 'nwes')
ys = ttk.Scrollbar(root, orient = 'vertical', command = text.yview)
xs = ttk.Scrollbar(root, orient = 'horizontal', command = text.xview)
text['yscrollcommand'] = ys.set
text['xscrollcommand'] = xs.set
xs.grid(column = 0, row = 1, sticky = 'we')
ys.grid(column = 1, row = 0, sticky = 'ns')

#Go! button
ttk.Button(mainframe, text="GO!", command=magic).grid(column=3, row=4, sticky=W)

for child in mainframe.winfo_children(): 
    child.grid_configure(padx=5, pady=5)

cg_name_entry.focus()
root.bind("<Return>", magic)

root.config(menu=menubar)
root.mainloop()