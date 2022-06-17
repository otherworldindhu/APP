import tkinter as tk   
root=tk.Tk()      #The second line created an instance of the tkinter.Tk class. This created what is called the "root" window 

root.title("I am a top level widget,parent to other widgets")
#label=Label(root,text="I am a label widget") #added a new instance named label for the Label widget. The first parameter defined root as its parent or container. The second parameter configured its text option as I am a label widget.
#button=Button(root,text="I am a button") #we defined an instance of a Button widget. This is also bound to the root window as its parent.
#label.pack() #We used the pack() method, which is essentially required to position the label and button widgets within the window. 
#button.pack()
indhu=tk.Frame(root,relief="raised",bd=25)
indhu.pack(fill=tk.X)
snega=tk.Menubutton(indhu,text="Snake babu",)
snega.pack(side=tk.LEFT)
thanishka=tk.Menu(snega,tearoff=35)
snega["menu"]=thanishka
thanishka.add("command",label="Niranchana")

vandana=tk.Menubutton(indhu,text="Vand bunz")
vandana.pack(side=tk.TOP)
twovand=tk.Menu(vandana,tearoff=100)
vandana["menu"]=twovand
twovand.add("command",label="surya")

my_frame_1=tk.Frame(root,bd=75,relief=tk.SUNKEN)
my_frame_1.pack(side=tk.LEFT)
tk.Label(my_frame_1,text="just chill just chill").pack()
tv=tk.StringVar()
tk.Entry(my_frame_1,textvariable=tv).pack()
tv.set("I am an antry widget")
tk.Button(my_frame_1,text="button widget").pack()
tk.Checkbutton(my_frame_1,text="Check button widget").pack()
tk.Radiobutton(my_frame_1,text="rb 1",value=1).pack()
tk.Radiobutton(my_frame_1,text="rb 2",value=2).pack()
tk.Radiobutton(my_frame_1,text="rb 3",value=3).pack()

tk.Label(my_frame_1,text="OptionMenu widget example").pack()
tk.OptionMenu(my_frame_1,'',"Option A","Option B","Option C").pack()

tk.Label(my_frame_1,text="Image fun with Bitmap Class").pack()
my_image=tk.BitmapImage(file="D:\sem4\APP\project\sample.xbm")

my_label=tk.Label(my_frame_1,image=my_image)
my_label.image=my_image
my_label.pack()

my_frame_2=tk.Frame(root,bd=10,relief=tk.GROOVE)
my_frame_2.pack(side=tk.LEFT)
tk.Label(my_frame_2,text="Image displayed with\n PhotoImage class widget").pack()
yen_photo=tk.PhotoImage(file="D:\sem4\APP\project\cir.gif")

yen_photo_label=tk.Label(my_frame_2,image=yen_photo)
yen_photo_label.pack()

root.mainloop()  
"""The  line executed the mainloop (that is, the event loop) method of the root object. The mainloop method is what keeps the root window visible. 
If you remove the third line, the window created in line 2 will disappear 
immediately as soon as the script stops running. This will happen so fast that 
you will not even see the window appearing on your screen. Keeping the 
mainloop method running also lets you keep the program running until you 
press the close button, which exits the main loop.
• Tkinter also exposed the mainloop method as tkinter.mainloop(). So, you 
can even call mainloop() directly instead of calling root.mainloop()."""
