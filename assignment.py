students=[]

questions=['whats the capital of abuja a) Abuja b) Cairo' ,
           'what is osun state capital a.) ikeja b.) osogbo' ,
           'what is the capital of ekiti state a.)Akure b.) Ado-Ekiti'
]

answers=['a', 'b', 'b']

examiner = int(input('How many students are taking this test: '))
for i in range(examiner):
    name = input(f'Enter student {i+1} name: ')
    students.append(name)

print(students)

scores={}

for student in students:
    print(f'{student} welcome to the test')

    score = 0
    x=1
    for que, ans1 in (zip(questions, answers)):
        print(f'\n{x}.{que}\n')
        x+=1
        ans= input('Enter your answer: ')
        
        if ans1 == ans:
            print ("correct!")
            score+=1
        else:
            print('wrong')
    scores[student] = score

print("\nScoresheet:")
for student, score in scores.items():
    print(f"{student}: {score} points")

    
min_score = min(scores.values())

max_score =max(scores.values())

# Print the minimum score
print(f"Lowest score: {min_score}")
print(f"highest score: {max_score}")

total_scores = sum(scores.values())
num_of_students = len(students)

average_score = total_scores / num_of_students

print (f'average score is :{average_score}')

# var = scores.index(min(scores))
# print(var)

print(min(scores))
    
            



