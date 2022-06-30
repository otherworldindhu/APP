import tkinter as tk   
root=tk.Tk()      

root.title("Journaling")

indhu=tk.Frame(root,relief="raised",bd=12)
indhu.pack(fill=tk.X)
snega=tk.Menubutton(indhu,text="All entries",)
snega.pack(side=tk.LEFT)
thanishka=tk.Menu(snega,tearoff=35)
snega["menu"]=thanishka
thanishka.add("command",label="Timeline")

vandana=tk.Menubutton(indhu,text="Calendar")
vandana.pack(side=tk.TOP)
twovand=tk.Menu(vandana,tearoff=100)
vandana["menu"]=twovand
twovand.add("command",label="Today")

my_frame_1=tk.Frame(root,bd=15,relief=tk.SUNKEN)
my_frame_1.pack(side=tk.LEFT)
tk.Label(my_frame_1,text="How was your day?").pack()
tv=tk.StringVar()
tk.Entry(my_frame_1,textvariable=tv).pack()
tv.set("fascinating!")
tk.Button(my_frame_1,text="OK").pack()
tk.Checkbutton(my_frame_1,text="Rate your day").pack()
tk.Radiobutton(my_frame_1,text="Happy",value=1).pack()
tk.Radiobutton(my_frame_1,text="Okay",value=2).pack()
tk.Radiobutton(my_frame_1,text="Not so good",value=3).pack()

tk.Label(my_frame_1,text="Checklist").pack()
tk.OptionMenu(my_frame_1,'',"SLeep schedule","Calorie count","Pedometer").pack()
'''tk.Label(my_frame_1,text="Image fun with Bitmap Class").pack()
my_image=tk.BitmapImage(file="D:\sem4\APP\project\sample.xbm")

my_label=tk.Label(my_frame_1,image=my_image)
my_label.image=my_image
my_label.pack()'''



my_frame_2=tk.Frame(root,bd=10,relief=tk.GROOVE)
my_frame_2.pack(side=tk.LEFT,)
'''tk.Label(my_frame_2,text="Jornaling").pack()
yen_photo=tk.PhotoImage(file="D:\sem4\APP\project\jou.gif")
yen_photo_label=tk.Label(my_frame_2,image=yen_photo)
yen_photo_label.pack()'''

tk.Label(my_frame_2,text="Meals today").pack()
my_listbox=tk.Listbox(my_frame_2,height=4)
for line in ['Breakfast','Lunch','Snack','Supper']:
    my_listbox.insert(tk.END,line)
my_listbox.pack()

tk.Label(my_frame_2,text="How much would you rate your day?").pack()
tk.Spinbox(my_frame_2,values=(1,2,4,8,10)).pack()

tk.Scale(my_frame_2,from_=0.0,to=100.0,label='Scale of Happiness',orient=tk.HORIZONTAL).pack()

label_frame=tk.LabelFrame(my_frame_2,text="Word of the day ",padx=10,pady=10)
label_frame.pack(padx=10,pady=10)
tk.Entry(label_frame).pack()

tk.Message(my_frame_2,text="Hope you have a great week :))))))").pack()

my_frame_3=tk.Frame(root,bd=3,relief=tk.SUNKEN)

my_text=tk.Text(my_frame_3,height=1,width=4)
file_object=open('D:\sem4\APP\project\my_text_doc.txt')
file_content=file_object.read()
file_object.close()
my_text.insert(tk.END,file_content)
my_text.pack(side=tk.LEFT,fill=tk.X,padx=5)

my_scrollbar = tk.Scrollbar(my_frame_3, orient=tk.VERTICAL, command=my_text.yview)
my_scrollbar.pack()
my_text.configure(yscrollcommand=my_scrollbar.set)
my_frame_3.pack()

my_frame_4=tk.Frame(root)
my_frame_4.pack()
my_canvas=tk.Canvas(my_frame_4,bg='purple',width=340,height=80)
my_canvas.pack()
my_canvas.create_oval(20,15,60,60,fill='white')
my_canvas.create_oval(40,15,60,60,fill='yellow')
my_canvas.create_text(130,38,text="Let's do it",font=("arial",8,'bold'))


tk.Label(root, text="Enter today's entry:").pack()
tk.Label(
    root,
    text='Dear Diary,').pack()
my_paned_window_1 = tk.PanedWindow()
my_paned_window_1.pack(fill=tk.BOTH, expand=2)
left_pane_text = tk.Text(my_paned_window_1, height=6, width=15)
my_paned_window_1.add(left_pane_text)
my_paned_window_2 = tk.PanedWindow(my_paned_window_1, orient=tk.VERTICAL)
my_paned_window_1.add(my_paned_window_2)
top_pane_text = tk.Text(my_paned_window_2, height=3, width=3)
my_paned_window_2.add(top_pane_text)
bottom_pane_text = tk.Text(my_paned_window_2, height=3, width=3)
my_paned_window_2.add(bottom_pane_text)

root.mainloop()  

