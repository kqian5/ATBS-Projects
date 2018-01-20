#! python 3
# randomQuizGenerator.py - Creates quizzes with questions and answers in random order, along with answer key

import random
capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix',
   'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver',
   'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee',
   'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois':
   'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas':
   'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine':
   'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan':
   'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri':
   'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada':
   'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton',
            'New Mexico': 'Santa Fe', 'New York': 'Albany', 'North Carolina': 'Raleigh',
   'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City',
   'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence',
   'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee':
   'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont':
   'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia',
            'West Virginia': 'Charleston', 'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}

for quizNum in range(35):
    quizFile = open("quiz%s.txt" % (quizNum + 1), "w")
    answerFile = open("answer%s.txt" % (quizNum + 1), "w")
    quizFile.write("Name:\nDate:\n")
    random.shuffle(capitals)
    count = 1
    for state in capitals:
        correct = capitals[state]
        answers = [correct]
        wrong = capitals.values()
        for i in range(3):
            wrong_answer = capitals[random.randint(0,49)]
            while wrong_answer in answers:
                wrong_answer = capitals[random.randint(0, 49)]
            answers.append(wrong_answer)
        random.shuffle(answers)
        quizFile.write("%d. What is the capital of %s?\n1. %s\n2. %s\n3. %s\n4. %s\n" % (count, state, answers[0], answers[1], answers[2], answers[3]))
        answerFile.write("%d. %s" % (count, "ABCD"[answers.index(correct)]))
        count += 1
    quizFile.close()
    answerFile.close()