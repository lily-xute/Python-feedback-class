import os
print("Student feedback generator")

#region folder work
# try and make a folder in the current directory called feedback
try:
	os.mkdir("feedback")
	print("\033[92mDirectory 'feedback' created successfully.\033[00m")
except FileExistsError:
	print("\033[91mDirectory 'feedback' already exists.\033[00m")

# change working directory for saving later
os.chdir("./feedback")
#endregion

#region dictonary template
# template sentences with placeholders
general_template = "{learner_name} {overall_comment} {general_understanding} {contribution_comment}"
learner_template = "{learner_name} on lab work {lab_level} {learner_name} was {punctuality} and {engagement_level} throughout the module."
recommended_template = "To build on current knowledge, {recommendation}"

# replacement dictionaries for performance levels (1 = lowest, 4 = highest)
overall_dict = {
	1: "struggled with key aspects of the module.",
	2: "had some difficulty grasping certain concepts.",
	3: "showed a solid understanding of most topics.",
	4: "excelled throughout the module and consistently demonstrated depth of knowledge."
}
genreal_dict = {
	1: "Further support is needed with foundational concepts.",
	2: "There is a growing understanding of the core ideas.",
	3: "Demonstrated confidence in applying concepts covered.",
	4: "Showed advanced insight and applied concepts with ease."
}
contribute_dict = {
	1: "Rarely participated in discussions.",
	2: "Participated occasionally but could engage more.",
	3: "Contributed thoughtful questions and responses.",
	4: "Regularly initiated insightful discussions and demonstrated leadership."
}
lab_dict = {
	1: "had difficulty completing lab work independently.",
	2: "managed lab exercises with some guidance.",
	3: "completed lab work confidently.",
	4: "demonstrated strong proficiency during lab sessions."
}
punctuality_dict = {
	1: "frequently late or missed sessions",
	2: "occasionally missed or was late to sessions",
	3: "usually punctual and reliable",
	4: "consistently punctual and well-prepared"
}
engagement_dict = {
	1: "showed limited engagement in activities",
	2: "engaged sporadically in module activities",
	3: "was engaged and focused during sessions",
	4: "actively participated and contributed meaningfully throughout"
}
further_dict = {
	1: "Review foundational concepts and practice applying them in simple projects.",
	2: "Strengthen understanding of key tools like Docker and explore simple pipelines.",
	3: "Continue building experience with Kubernetes and pipelines.",
	4: "Tackle advanced scenarios in container orchestration and continuous integration workflows."
}
list_of_questions = ["overal performance","General understanding","Contribution level","lab completion","punctuality","engagement","further study level"]
answer = [None]*7
#endregion

#region enter student names
list_of_students = []
print("Enter student name or leave blank and hit enter to end input")
while True:
	user_input = input("Name: ")
	if user_input == "":
		break
	list_of_students.append(user_input)
#endregion

for student in list_of_students:
	answer_index = 0
	print(f"\r\nReview for {student}:")
	print("Please input scores 1-4 for following attrubutes (1-low,4-high):")

	for question in list_of_questions:
		while True:
			try:
				user_input = int(input(f"{question}: "))
				if user_input < 1 or user_input > 4:
					raise ValueError
				answer[answer_index] = user_input
				answer_index += 1
				break
			except ValueError:
				print("Invaild input. Please enter 1-4")

	output = general_template + "\r\n\r\n" + learner_template + "\r\n\r\n" + recommended_template

	# Replace place holder with selected values
	output = output.format(
		learner_name = student,
		overall_comment = overall_dict[answer[0]],
		general_understanding = genreal_dict[answer[1]],
		contribution_comment = contribute_dict[answer[2]],
		lab_level = lab_dict[answer[3]],
		punctuality = punctuality_dict[answer[4]],
		engagement_level = engagement_dict[answer[5]],
		recommendation = further_dict[answer[6]]
	)

	# output to file with student name
	with open(f"{student}.txt", "w") as f:
		f.write(output)

	# open file in notepad
	os.system(f"notepad {student}.txt")

	input("Next student: ")
