import requests
import json
import random
import html

#Quiz categories and diffuculty
categories = ["General Knoledge","Books","Film","Music","Sport","History"]
difficulty = ["easy", "medium", "hard"]
score = 0

print("Welcome to the quiz game.")

#Select number of questions
valid_number = False
while valid_number == False:
    numQuestions = input("How many questions would you like to answer? Type a number betweeen 1 an 10: ")
    try:
        numberQuestions = int(numQuestions)
        if numberQuestions < 1 or numberQuestions > 10:
            print("Invalid number. Please enter a number between 1 and 10. " )
        else:
            valid_number = True
    except:
        print("Invalid input. Please enter a number between 1 and 10. ")

#Select category
print("Select a category from the list:")
count = 1
for category in categories:
    print(str(count) + ' ' + category)
    count += 1

valid_category = False
while valid_category == False:
    selected = input("Type the category number: ")
    try:
        numSelected = int(selected)
        if numSelected < 1 or numSelected > len(categories):
            print("Invalid number. Please enter a number between 1 and " +str(len(categories)))
        else:
            valid_category = True
    except:
        print("Invalid input. Please enter a number between 1 and " +str(len(categories)))

selectedCategory = categories[int(selected)-1]

#select difficulty level
print("Select your difficulty level")
count = 1
for diff in difficulty:
    print(str(count) + ' ' + diff)
    count += 1
valid_difficulty_level = False
while valid_difficulty_level == False:
    level = input("Type the appropriate number (1, 2 or 3): ")
    try:
        numLevel = int(level)
        if numLevel < 1 or numLevel > 3:
            print("Invalid number. Please enter a number between 1 and 3.")
        else:
            valid_difficulty_level = True
    except:
        print("Invalid input. Please enter a number between 1 and 3.")

difficultyLevel = difficulty[int(level)-1]

print("You have selected", selectedCategory, "with a difficulty level of", difficultyLevel)

#build quiz url from user selections
urlCategory = 0
if selectedCategory == "General knowledge":
    urlCategory = 9
elif selectedCategory == "Books":
    urlCategory = 10
elif selectedCategory == "Film":
    urlCategory = 11
elif selectedCategory == "Music":
    urlCategory = 12
elif selectedCategory == "Sport":
    urlCategory = 21
elif selectedCategory == "History":
    urlCategory = 23


url="https://opentdb.com/api.php?amount="+numQuestions+"&category="+str(urlCategory)+"&difficulty="+difficultyLevel+"&type=multiple"

#get url and parse using json
r = requests.get(url)
data = json.loads(r.text)
questions = data['results']

#sort each question and relevant answers
i = 0
for question in questions:
    print("Question " +str(i + 1))
    question = questions[i]['question']

    correct_answer = questions[i]['correct_answer']
    answers = questions[i]['incorrect_answers']
    answers.append(correct_answer)
    random.shuffle(answers)
    print(html.unescape(question) + "\n")

    answer_number = 1
    for answer in answers:
        print(str(answer_number) +": " +html.unescape(answer))
        answer_number += 1

    valid_answer = False
    while not valid_answer:
        user_answer = input("\nType the number of your chosen answer: ")
        try:
            user_answer = int(user_answer)
            if user_answer > len(answers) or user_answer <= 0:
                print("Invalid answer. Please type a number between 1 and " +str(len(answers)))
            else:
                valid_answer = True
        except:
            print("Invalid answer. Please use numbers only.")

    user_answer = answers[int(user_answer) -1]
    if user_answer == correct_answer:
        print("Your answer is correct!")
        score += 1
    else:
        print("Your answer is incorrect. The correct answer is " +html.unescape(correct_answer))

    i += 1

print("You got " +str(score) +" questions correct.")
