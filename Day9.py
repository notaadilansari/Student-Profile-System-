#creating class
class student:
	def __init__(self,name,roll_num,marks):
		self.name=name
		self.roll_num=roll_num
		self.marks=marks
	#method of display info	
	def display_info(self):
		print("\n---STUDENT PROFILE---")
		print(f"Name : {self.name}")
		print(f"Roll : {self.roll_num}")
		print(f"Marks : {self.marks}")
	#method of check result
	def check_result(self):
		if self.marks>40:
			print("\n🔥Result : Pass")
		else:
			print("\n🤡Result : Fail")
#creating an object to store info of student
def object():
	print("💠---WELCOME TO STUDENT PROFILE SYSTEM---")
	name=input("Enter student name : ")
	roll_num=int(input("Enter Roll Number : "))
	marks=int(input("Enter marks : "))
	if type(marks)!=type(7):
		print("Invalid data type")
		print("\nEnter Valid Marks ")
		object()
	else:
		user=student(name,roll_num,marks)
		def user_task():
			print("\nWhat task you want to perform ??")
			print("1.Student Info")
			print("2.Check result")
			print("3.Exit")
			user_choice=int(input("Choose option(1-3) : "))
			if user_choice==1:
				user.display_info()
				user_task()
			elif user_choice==2:
				user.check_result()
				user_task()
			elif user_choice==3:
				print("\nExiting...")
				print("🌀Thanks For Using Student Profile System")
			else:
				print("❌No such options ")
				print("\n⏳TRY AGAIN - ")
				user_task()
		user_task()
object()
