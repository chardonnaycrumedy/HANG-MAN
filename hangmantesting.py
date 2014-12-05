from Tkinter import *
root = Tk()
drawpad = Canvas(root, width=800,height=600, background='white')
drawpad.pack()
class MyApp:
	def __init__(self, parent):
	        # Make sure the drawpad is accessible from inside the function
	        global drawpad
		self.myParent = parent
		self.myContainer1 = Frame(parent)
		self.myContainer1.pack()
#------------------BUNCH OF GARBAGE WE SHOULD NOT TOUCH------------
#oval = drawpad.create_oval(420,90,490,190, fill = "black")  #head
#rectangle = drawpad.create_rectangle(400,190,510,400, fill = "black")  #body
#line = drawpad.create_line(510,230,530,400, fill = "black")   #right arm
#line = drawpad.create_line(400,190,380,400, fill = "black")   #left arm
#rectangle = drawpad.create_rectangle(410,400,430,460, fill = "black")
#rectangle = drawpad.create_rectangle(480,400,500,460, fill = "black")

wordbank = ['s, t, r, a, w, b, b, e, r, r, y'] 

for item in wordbank:
    print wordbank
print "Topic is Fruit"
while True:
    answer = raw_input()
    if answer == 's' or answer == 't' or answer == 'r' or answer == 'a' or answer == 'w' or answer == 'b' or answer == 'e' or answer == 'r' or answer == 'y':
        print "correct"
    else:
         oval = drawpad.create_oval(420,90,490,190, fill = "black")
    if answer == 's' or answer == 't' or answer == 'r' or answer == 'a' or answer == 'w' or answer == 'b' or answer == 'e' or answer == 'r' or answer == 'y':
        print "correct"
    else:
         rectangle = drawpad.create_rectangle(400,190,510,400, fill = "black")  #body
    if answer == 's' or answer == 't' or answer == 'r' or answer == 'a' or answer == 'w' or answer == 'b' or answer == 'e' or answer == 'r' or answer == 'y':
        print "correct"
    #else:
        #line = drawpad.create_line(510,230,530,400, fill = "black") #right arm
    #if answer == 't':
        #print "correct"
    #else:
        #line = drawpad.create_line(510,230,530,400, fill = "black")   #right arm
    #if answer == 'a':
       # print "correct"
   # else:
       # line = drawpad.create_line(400,190,380,400, fill = "black")   #left arm
    #if answer == 'w':
     #   print "correct"
   # else:
    #    rectangle = drawpad.create_rectangle(410,400,430,460, fill = "black")
    break
        

 





#-----------MORE GARBAGE WE SHOULD NOT TOUCH----------------------
myapp = MyApp(root)
root.mainloop()


















































