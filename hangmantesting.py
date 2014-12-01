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
wordbank = [porcupine, baboon, eagle, lamb, cow, beaver, camel, cat, clam, cobra, bat, coyote, crow, deer, dog, donkey, duck, eagle, ferret, fox, frog, goat, goose, hawk, lion, lizard, llama, mole, monkey, moose, mouse, mule, newt, otter, owl, panda, parrot, pigeon, python, rabbit, ram, rat, raven, rhino, salmon, seal, shark, sheep, skunk, sloth, snake, spider, stork, swan, tiger, toad, trout, turkey, turtle, weasel, whale, wolf, wombat, zebra]
if raw_input() == i in wordbank:
    print correct
else:
    print wrong
def getRandomWord(wordbank):
    # This function returns a random string from the passed list of strings.
    index = random.randint(0, len(wordbank) - 1)
    return wordList[wordIndex]


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


















































