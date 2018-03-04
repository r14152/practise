import tkinter as tk
import multiprocessing as mp
import time


#use some class related coding to see that tk work in class based or not

class Root(tk.Tk):
	def __init__(self):
		super().__init__()
		
		self.label = tk.Label(self,
						text="My name is Ravi singh", padx=10,
						pady=10)
		self.label.pack() 

def showTheMessage(context):
	root = tk.Tk()
	root.title("Message")
	lable = tk.Label(root, fg='green',
					text=context,
					padx=10, pady=10)
	lable.pack()
	info =tk.Button(root,
					text = "info",
					command=root.destroy)
	info.pack()
	root.after(5000,root.destroy)
	root.mainloop()

def printMessage():
	data = 0
	for i in range(0,10):
		print("Hey ravi singh, %d"%i)
	time.sleep(1)

def main():
	
	show = mp.Process(target=showTheMessage,
				name="showName",
				args=("Hello every one how are you",))
	flag=0
	while 1:
		print(flag)
		show = mp.Process(target=showTheMessage,
				name="showName",
				args=("Hello every one how are you",))
		show.start()
		print("Parent_Id %d",show.getppid())
		print("Parent_Id %d",show.getpid())
		print("Process start")
		show.join()
		if flag == 5:
			break
		else:
			flag += 1
		print("See its come here or not")
		printData = mp.Process(target=printMessage,
					name="printMessage",)
		printData.start()
		print("function working well")
		time.sleep(3)
		printData.join()

if __name__ == '__main__':
	main()
	
