import random
who = [
    'sita, gita, sunita have been',
    'ram, shyam, rahul have been',
    'five old person is ',
    'A young girl',
    'My math teacher is'
]
what = [
    'playing guitar',
    'reading books behind people',
    'telling story to everyone',
    'drinking wine',
    'playing in park'
]
when = [
    'in the moring',
    'in the mood',
    'in alone',
    'in happy mood',
    'once in a week',
]
why = [
    'because they like it more then anything else',
    'it is their passion and dont want to accept other habit',
    'because this is habit so that he cannot change this',
    'because they want to be cool',
    'bacause they want to pretend'
]
print(
    random.choice(who) + ' ' + random.choice(what) + ' ' +
    random.choice(when) + ' ' + random.choice(why)
    )