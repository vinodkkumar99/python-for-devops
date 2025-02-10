import sys

type=sys.argv[1]

if type == 't2.micro':
    print('This is a free tier instance')
elif type == 't2.small':
    print('This is a not free tier instance,but we can create it')
else:
    print('This is not a free tier instance')