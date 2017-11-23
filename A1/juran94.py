#Ran Ju
#CSE 415 Autumn 2017
#Assignment B1

from re import *
import random
import datetime

now = datetime.datetime.now()
noon = now.replace(hour = 12, minute = 0, second = 0, microsecond = 0)
five = now.replace(hour = 17, minute = 0, second = 0, microsecond = 0)
#Return the agent name
def agentName():
    return 'Ran'

def introduce():
    now = datetime.datetime.now();
    'introduction of the agent'
    return ("Hello, my name is Ran, and I am the waitress in this restaurant."\
            + "\n"+ "I was programmed by Ran Ju. If you don't like me, "\
            +"\n" + "contact her at juran94@uw.edu."\
           +"\n"+"How can I help you today?")




CASE_MAP = {'i':'you','me':'you','my':'your','your':'my','am':'are',
           'are':'am','mine':'yours','yours':'mine'}
Drinks = ['coke','dr.pepper','sprite','beer','ice-water','coffee',\
          'lemonade','fanta','whiskey','vodka','green-tea','black-tea',\
          'bubble-milk-tea','hot-water','orange-juice']
Meals = ['burger','French Fries','sandwich','chicken-rice','kimichi','tofu-soup',\
        'sushi','poke','little-hot-pot','double-cheese-burger','fish-and-chips','vegan-sandwich']

DrinkOrder =[]
MealOrder =[]
def you_me(word):
    try:
        res = CASE_MAP[word]
    except KeyError:
        res = word
    return res

def you_me_map(wordlist):
    return [you_me(word) for word in wordlist]

def isQuestion(words):
    return (words.lower() in ['what','when','who','how','which','whose','where','why'])

def toString(wordlist):
    return ''.join(wordlist)

def isVerb(word):
    return (word in ['go', 'have', 'be', 'try', 'eat', 'take', 'help',\
                  'make', 'get', 'jump', 'write', 'type', 'fill',\
                  'put', 'turn', 'compute', 'think', 'drink',\
                  'blink', 'crash', 'crunch', 'add'])
punctuation_pattern = compile(r"\,|\.|\?|\!|\;|\:")
def remove_punctuation(text):
    return sub(punctuation_pattern,'', text)
#Respond method that can reply to different users
def respond(theInput):
    if match('bye',theInput):
        return 'Have a nice day! thank you!'
    #initalize
    wordlist = split(' ',remove_punctuation(theInput).lower())
    mapped_wordlilst = you_me_map(wordlist)
    mapped_wordlilst[0] = mapped_wordlilst[0].capitalize()
    #Rule1: When user say nothing
    if wordlist[0] == ''or len(wordlist) == 0:
        return 'Please say something.'

    #Rule2: Tell user who am I
    if wordlist[0:3] == ['who','are','you']:
        return 'I am Ran. Hope you have a great day!'

    #Rule3: Give some suggestions to user (Random-chioce feature)
    if wordlist[0:3] == ['do','you','recommend'] or 'anything' in wordlist:
        randDrink = random.randint(0,len(Drinks)-1)
        randMeal = random.randint(0,len(Meals)-1)
        return "I think you can choose " + toString(Drinks[randDrink]) +" to drink. And order one "+ \
            toString(Meals[randMeal])+" to eat."
    # Rule4: when user say something positive
    if 'love' in wordlist or 'like' in wordlist:
        return 'Appreciate that!'
    #Rule 5: when user say somthing negative
    if 'dislike' in wordlist or 'tolerate'in wordlist or 'hate' in wordlist:
        return 'Sorry about that. I will imporve it!'

    #Rule 6: when user want somthing, if in the menu then order it, otherwise say sorry (Cycle Feature)
    if wordlist[0:2] == ['i','want']:
        if wordlist[2] in Drinks :
            DrinkOrder.append(wordlist[2])
            return "Great! " + toString(wordlist[2]) + " has been added! Anything else?"
        elif  wordlist[2] in Meals:
            MealOrder.append(wordlist[2])
            return "Great! "  +toString(wordlist[2])+ " has been added! Anything else?"
        else:
            return "Sorry, we don\'t have this yet!"
    #Rule 7: when user need something to drink
    if 'drink' in wordlist and ('somthing'in wordlist or theInput.endswith('?')):
        randDrink = random.randint(0,len(Drinks)-1)
        return "Well, I think "+ Drinks[randDrink]+" is better for you!"
    #Rule 8: when user need something to eat
    if 'eat' in wordlist and ('something'in wordlist or theInput.endswith('?')):
        randMeal = random.randint(0,len(Meals)-1)
        return "Well, I think "+ Meals[randMeal]+ " is good! You can try it!"
    #Rule 9:when user say thank you
    if 'thanks' in wordlist or 'thank' in wordlist:
        return "You are welcome!"
    #Rule10: when user is a vegan
    if 'vegan' in wordlist or 'vegetarian' in wordlist:
        return ("I think you should order vegan sandwich.")
    if wordlist[0] in Drinks or wordlist[0] in Meals:
        return "You want to order "+ toString(wordlist[0]) + "? You can enter \"I want ...\" to order it!"

    #Rule 11: enter "order" can show which meal and drink already be added in the list (Memory Feature)
    if 'order'in wordlist:
        if len(MealOrder) > 0 or len(DrinkOrder) > 0:
            print("You already order ",end="")
            for string in MealOrder:
                if string not in MealOrder[-1]:
                    print(string + " and ",end="")
                else:
                    print(string,end=" for eat.")
            for string in DrinkOrder:
                if string not in DrinkOrder[-1]:
                    print(string + " and ",end="")
                else:
                    print(string, end=" for drink.")
            return ("It is great!")
        else:
            return "You still does not order yet."
    #Rule 12: enter "menus' to show which meal and drink sell
    if wordlist[0] == "menus":
        print("Here is our restaurant's menus, our meal is", end=" ")
        for string in Meals:
            if string not in Meals[-1]:
                print(string, end=",")
            else:
                print(string, end ="")
        print(" and we offer some drinks like ",end="")
        for string in Drinks:
            if string not in Drinks[-1]:
                print(string, end=',')
            else:
                print(string,end=".")
        return "Enjoy!"
    #Rule 13: enter "i feel"
    if wordlist[0:2] == ['i','feel']:
        return "Oh, I feel good, isn\'t it?"
    #Rule 14: enter "tips" ot "tip":
    if "tips" in wordlist or "tip" in wordlist:
        return "Thank you if you can give me more tip!"
    #Rule 15: when the question cannot be touched
    if isQuestion(wordlist[0]) and theInput.endswith('?'):
        return 'Good question! but I cannot answer you right now. Sorry!'
    return punt()

PUNTS = ['What can I do for you?',
         'hope you can enjoy your meal!',
         'What\'s up, bro?',
         'Sounds great!',
         'Give me some suggestions, thanks you!',
         'Delicious food, isn\'t it ?']

punt_count = 0


def punt():
    'Returns one from a list of default responses.'
    now = datetime.datetime.now()
    if now < noon:
        PUNTS[2] = 'How you doing in this morning?'
    elif now > noon and now < five:
        PUNTS[2] = 'How you doing in this afternoon?'
    else:
        PUNTS[2] = 'How you doing to tonight?'

    global punt_count
    punt_count += 1
    return PUNTS[punt_count % 6]