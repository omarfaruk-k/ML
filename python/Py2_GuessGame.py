import random

num = random.randint(1,100)
count =1

while True:
    in_num = int(input('Enter any Number: '))
    
    if in_num == num:
        print(f'You have gussed correct after {count} attempt\n')
        break 
    elif abs(num-in_num)<10:
        count+=1
        print('HOTTER')
    
    elif abs(num-in_num)>10:
        count+=1
        print('COLDER')

    