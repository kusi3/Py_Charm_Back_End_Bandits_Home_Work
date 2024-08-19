# შეიყვანე ციფრი 1-7 -მდე და შეუსაბამე კვირის დღეები,
number = int(input('enter number between 1-7: '))

counting = 0
while number > 7 or number < 1:
    counting += 1
    number = int(input('enter number between 1-7: '))
    if counting == 2:
        print('იუზერო, ნუ დაგვღალე!')
        break
if number == 1:
    print('mon')
elif number == 2:
    print('Tue')
elif number == 3:
    print('Wen')
elif number == 4:
    print('The')
elif number == 5:
    print('Fry')
elif number == 6:
    print('Sat')
elif number == 7:
    print('Sun')





# 1. ვიქტორინა 1. შუმერთა 2. სელჩუკთა 3. რომის 4. მონღოლთა

builder = input('enter correct word or number for answer: ' \
                'Which one Is the water supply system (aqueduct)' \
                'built by \nthe empire still functioning today?' \
                '\n 1. Sumerians' \
                '\n 2. Seljuks' \
                '\n 3. Rome' \
                '\n 4. Mongols')

if builder == '3' or builder.lower() == 'rome':
    print('Your answer is correct!')
else:
    print('No, correct answer is Rome!')



# 2. ონლაინ მაღაზია

category = input('please chois category: hp, samsung or apple')
money = int(input('how much amount do you have?'))

leptops = ('hp','samsung', 'apple')
leptops_prices = (1200, 1800, 4500)

pc = ('lenovo', 'dell', 'lg')
pc_prices = (450, 890, 1100)

phone = ('nokia', 'xiaomi', 'iphone18')
phone_prices = (120, 520, 9800)


if category == 'leptops':
    if money >= leptops_prices[2]:
        print(f'you can buy {leptops[2]} leptop')
    elif money >= leptops_prices[1] and money < leptops_prices[2]:
        print(f'you can buy {leptops[1]} leptop')
    elif money >= leptops_prices[0] and money < leptops_prices[1]:
        print(f'you can buy {leptops[0]} leptop')
    else:
        print('work more, you do not have enough money')

if category == 'pc':
    if money >= pc_prices[2]:
        print(f'you can buy {pc[2]} leptop')
    elif money >= pc_prices[1] and money < pc_prices[2]:
        print(f'you can buy {pc[1]} leptop')
    elif money >= pc_prices[0] and money < pc_prices[1]:
        print(f'you can buy {pc[0]} leptop')
    else:
        print('work more, you do not have enough money')

if category == 'phone':
    if money >= phone_prices[2]:
        print(f'you can buy {phone[2]} leptop')
    elif money >= phone_prices[1] and money < phone_prices[2]:
        print(f'you can buy {phone[1]} leptop')
    elif money >= phone_prices[0] and money < phone_prices[1]:
        print(f'you can buy {phone[0]} leptop')
    else:
        print('work more, you do not have enough money')



# 4. კარიერის შემრჩევი

question_gender = input("What is your gender? (male/female ")
question_place = input("Where are you from?  ")
question_skills = input("What special skills do you possess? coding, painting, arting")

gender_values = ('male', 'female')
place_value = ('georgia', 'russia')
skils_value = ('coding', 'painting', 'arting')

if question_gender == gender_values[0]:
    if question_place == place_value[0]:
        if question_skills == skils_value[0]:
            print('hah, you will be great proggramet, boy!')
        else:
            print('so good artist you will be!')
    elif question_place == place_value[1]:
        print('Russia is occupante and you must know it')
    else:
        print('you are trying to become proggramer')
elif question_gender == gender_values[1]:
    if question_place == place_value[0]:
        if question_skills == skils_value[0]:
            print('if you study very hard, you will became programer lady!')
        else:
            print('you can be painter or artist boss')
    elif question_place == place_value[1]:
        print('Russia is occupante and you must know it')
    else:
        print('you are trying to become proggramer')
