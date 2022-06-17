from tkinter import *   # imported all (*) the classes, attributes, and methods of Tkinter into the current workspace.
root=Tk()      #The second line created an instance of the tkinter.Tk class. This created what is called the "root" window 
root.mainloop()  
"""The third line executed the mainloop (that is, the event loop) method of the root object. The mainloop method is what keeps the root window visible. 
If you remove the third line, the window created in line 2 will disappear 
immediately as soon as the script stops running. This will happen so fast that 
you will not even see the window appearing on your screen. Keeping the 
mainloop method running also lets you keep the program running until you 
press the close button, which exits the main loop.
• Tkinter also exposed the mainloop method as tkinter.mainloop(). So, you 
can even call mainloop() directly instead of calling root.mainloop()."""
