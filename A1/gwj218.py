

from re import *   # Loads the regular expression module.
import random
import datetime
#def Shrink():
    #'Shrink is the top-level function, containing the main loop.'
    #print('They call me the Shrink.  Welcome to my sofa!')
    #print('So what is your problem?')
    #while True:
    #    the_input = input('TYPE HERE:&gt;&gt; ')
    #    if match('bye',the_input):
    #        print('Goodbye!')
    #        return

# introduces agent
now = datetime.datetime.now()
def introduce():
    return ' Hi, my name is Bruno, I am a DJ from music Radio: Melody FM. \n\
    If there is anything I cannot deal for you, please contact \n\
    Wenjin at gwj218@uw.edu. What kind of music do you like?  We have folk, jazz, pop, blues, rock, \n\
    country music, classical, hip hop, soul music, heavy metal, punk, funk, electronic, opera, reggae, singing.'

GENRES = [['folk'], ['jazz'], ['pop'], ['blues'], ['rock'], ['country'],\
           ['classical'], ['hiphop'], ['soul'], ['heavymetal'], ['punk'], ['funk'], ['electronic'],\
           ['opera'],['reggae'],['singing']]

GREETINGS = ['great', 'I am fine', 'aloha', 'how\'s going']

ADJECTIVES = ['popular', 'cool', 'smart', 'great', 'brilliant', 'talent', 'fascinating']

MUSIC_DEMAND = []

def respond(the_input):
    if match('bye', the_input):
        return 'See you next time at Melody FM!'

    wordlist = split(' ', remove_punctuation(the_input).lower())
        # undo any initial capitalization:
    #wordlist[0]=wordlist[0].lower()
    mapped_wordlist = you_me_map(wordlist)
    mapped_wordlist[0] = mapped_wordlist[0].capitalize()
     #   respond(the_input, wordlist, mapped_wordlist)


#def respond(the_input, wordlist, mapped_wordlist):

    ###Rule 0: reply when audience has nothing input
    if wordlist[0] == '' and len(MUSIC_DEMAND) < 1:
        return "Would you like to have some rythem?"

        ###Rule 1: reply when audience want music in GENRES

    if wordlist[0] in GENRES:
        music = mapped_wordlist[0:]
        if not (wordlist[0:] in MUSIC_DEMAND):
            MUSIC_DEMAND.append(wordlist[0:])
        return "Great! I just want to play some " + stringify(music) + " for you."

        ###Rule 2: reply when audience's request contains "I like"
    if wordlist[0:2] == ['i', 'like']:
        music = mapped_wordlist[2:]
        if music in GENRES:
            if not (wordlist[2:] in MUSIC_DEMAND):
                MUSIC_DEMAND.append(wordlist[3:])
                return stringify(music) + " is coming soon!"
        else:
            return "You have a unique taste."

            ###Rule 3: reply randomly from GREETINGS when greetings
    if wordlist[0] in ['hi', 'hello', 'hey'] or \
                    wordlist[0:2] in [['what\'s', 'up']] or \
                    wordlist[0:3] in [['how', 'are', 'you']]:
        return random.choice(GREETINGS).title() + ', want a song?'
        # song = input('Input a song\'s name:>>')
        # if len(reply) > 0:
        # return "Let me check if" + stringify(song) + "is on the playlist."

        # Rule 4: reply when audience change from last music genre to a new one(momory function)
    if wordlist[0:2] == ['i', 'want']:
        if wordlist[2] in MUSIC_DEMAND:
            return "You are listening to" + stringify(mapped_wordlist[2:]) + "."
        else:
            return "You said you like " + stringify(mapped_wordlist[2:]) + ", are you sure you want it now?"
            # answer = input('Type Yes or No:>> ')
            # if answer.lower().startswith('yes'):
            # MUSIC_DEMAND.append(wordlist[2])
            # return "Alright, I will shift it for you."
            # else:
            # return "Yay, music won\'t stop."

            # Rule 5: reply the explaination of music genre to audience
    if wordlist[0:3] == ['what', 'is', 'a'] and wordlist[3:] in GENRES:
        randInt = random.randint(0, 6)
        return "The " + stringify(wordlist[3:]) + " is a " + ADJECTIVES[randInt] + " music genre!"

        ###Rule 6: reply when audience start with "you are"
    if wordlist[0:2] == ['you', 'are']:
        comments = wordlist[2:]
        return "I don\'t know why you think I am" + stringify(comments) + ", but I like to know the reason."

        ###Rule 7: reply time when audience mentioned "now"
    if wordlist[0:2] == ['what', 'time'] or 'now' in wordlist:
        nowtime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        return "it is " + stringify(nowtime) + "now."

        ###Rule 8: reply when audience starts with " I feel"
    if wordlist[0:2] == ['i', 'feel']:
        selfdescript = wordlist[2:]
        agent_prefer = random.randint(0, 15)
        return "When I am" + stringify(selfdescript) + ", I listen to " + stringify(GENRES[agent_prefer]) + '.'

        ### Rule 9: reply when audience ask agent's preference
    if wordlist[0:4] == ['what', 'do', 'you', 'like']:
        agent_prefer = random.randint(0, 15)
        return "I think " + stringify(GENRES[agent_prefer]) + "is great!"

        ### Rule 10: reply when audience ask something
    if wpred(wordlist[0]):
        return "Who knows " + wordlist[0] + ", I am just a DJ."

        ### Rule 11: reply when audience use verb
    if verbp(wordlist[0]):
        return "I believe you can" + stringify(mapped_wordlist) + "by yourself."

        ### Rule 12: reply when audience ask personality on agent
    if wordlist[0:2] == ['are', 'you']:
        return "Yes, I am " + stringify(mapped_wordlist[2:]) + '.'

        ### Rule 13: reply welcome if audience say thanks
    if 'thank' in wordlist:
        return "You are welcomed, bro."

        ### Rule 14: reply name
    if 'name' in wordlist:
        return "My name is Bruno, I'd like to know yours."
    print(punt())

def stringify(wordlist):
    'Create a string from wordlist, but with spaces between words.'
    return ' '.join(wordlist)

punctuation_pattern = compile(r"\,|\.|\?|\!|\;|\:")    

def remove_punctuation(text):
    'Returns a string without any punctuation.'
    return sub(punctuation_pattern,'', text)

def wpred(w):
    'Returns True if w is one of the question words.'
    return (w in ['when','why','where','how'])

def dpred(w):
    'Returns True if w is an auxiliary verb.'
    return (w in ['do','can','should','would'])

PUNTS = ['Are you listening?',
         'Try it.',
         'What do you think?',
         'Can you tell more about it?',
         'I am happy to chat with you',
         'You could put your hands up and dance.']


punt_count = 0
def punt():
    'Returns one from a list of default responses.'
    global punt_count
    punt_count += 1
    return PUNTS[punt_count % 6]

CASE_MAP = {'i':'you', 'I':'you', 'me':'you','you':'me',
            'my':'your','your':'my',
            'yours':'mine','mine':'yours','am':'are'}

def you_me(w):
    'Changes a word from 1st to 2nd person or vice-versa.'
    try:
        result = CASE_MAP[w]
    except KeyError:
        result = w
    return result

def you_me_map(wordlist):
    'Applies YOU-ME to a whole sentence or phrase.'
    return [you_me(w) for w in wordlist]

def verbp(w):
    'Returns True if w is one of these known verbs.'
    return (w in ['go', 'have', 'be', 'try', 'eat', 'take', 'help',
                  'make', 'get', 'jump', 'write', 'type', 'fill',
                  'put', 'turn', 'compute', 'think', 'drink',
                  'blink', 'crash', 'crunch', 'add'])

#Shrink() # Launch the program.
def agentName():
    return "Bruno"