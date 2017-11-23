#  Ran Ju #1621899
# Assignment 1 Basic of Python and String Manipulation
# Autumn 2017
#Assignment 1

# Part A question 1

def three_x_cubed_plus_7(x):
    print(3 * x * x * x + 7)

#question 2
def mystery_code(s):
    res = list(s)
    i = 0
    for x in s:
        if x.isalpha():

            if x.islower():
                n = ord(x) % 26
                res[i] = chr(65 + n)
            else:
                n = (ord(x)+6) % 26
                res[i] = chr(97 + n)
        else:
            res[i] = x
        i += 1

    x = ''.join(res)
    print(x)

#question 3
def pair_off(array):
    res = []
    length = len(array)
    i = 0;
    while i < length:
        bucket = []
        bucket.append(array[i])
        if i+1 < length:
            bucket.append(array[i + 1])
        res.append(bucket)
        i +=2
    print(res)
#question 4
def past_tense(array):
    res = []
    for i in array:
        if i in ('have','be','eat','go'):
            if i == 'have':
                res.append('had')
            elif i == 'be':
                res.append('was')
            elif i == 'eat':
                res.append('ate')
            else:
                res.append('went')
        elif i[-1] == 'e':
            res.append(i+'d')
        elif i[-1] == 'y' and i[-2] in 'aeiou':
            res.append(i[:-1]+'ied')
        elif i[-2] in 'aeiou'and i[-3] not in 'aeiou' and i[-1] not in 'aeiouyw':
            res.append(i + i[-1] +'ed')
        else:
            res.append(i + 'ed')
    print(res)


