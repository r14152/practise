#this example is basically used to check that is key board or keypress work or notin python
import time
import os
import logging
from multiprocessing import Pool,Queue,Process
import multiprocessing as mp
#practise with some class type of coding

def addValue(a, b, c):
	print("Final Addittion : %d"%(a+b+c))
	print('module_name: ',__name__)
	print('Parent Process: ',os.getppid())
	print('Process id:', os.getpid())
	time.sleep(4)
	return (a+b+c)


class Student(object):
	'''
		create class constructor
	'''
	def __init__(self, name, age, city):
		self.name = name
		self.age  = age
		self.city = city
	'''
		function to return information related to the student
	'''
	def getInformation(self):
		print("Name : %s \nage : %d \ncity : %s"%(self.name, self.age,
				self.city))
		return

#try to do some multithreading and multiprocess concept

def processExample():
	storeProcess_q = Queue()
	manage_addition = Process(target=addValue,
				name = 'addition',
				args = (1,2,3))
	manage_addition.start()
	manage_addition.join()

def f(x, q):
	q.put(x*x)
	return x*x

#try to change the queue value
def printQ(q):
	print("Come into the printQ")
	q.put("Ravi singh")

def poolExample():
	q = Queue()
	p = Process(target=f,
				name = 'addition',
				args = (2,q))
	p.start()
	print(q.get())
	newData = Process(target = printQ,
					name = 'print process detail',
					args = (q,))
	newData.start()
	print(q.get())
	print("Name: %s"%newData.name)
	print("Is alive ",newData.is_alive())
	newData.join()
	p.join()

def main():
	base_dir = os.path.dirname(os.path.abspath(__file__))
	print(base_dir)
	#now add other folder with this path
	audio_dir = os.path.join(base_dir, 'audio')
	print(audio_dir)
	newStudent = Student('Ravi Singh', 24, 'Ballia')
	newStudent.getInformation()
	nameDetail = dict(
				name = 'Ravi singh',
				age  = '24',
				address = 'Ballia')
	print(nameDetail)
	processExample()
	poolExample()
	return
#start from here
if __name__ == "__main__":
	main()
