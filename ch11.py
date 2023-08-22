
import re
print('-------------start-------------')

counts = dict()
fname = 'mbox-short.txt'
#open file
try :
    fopen = open(fname,'r')
    print('Can open!\n')
except :
    print('File cannot be opened: ', fname)

x = fopen.read()
# # print(x)
# x = 'From: Using the : chaiya@gmail.com asdawddce'
# y = re.findall('[a+]', x)
# print('\nFind number 0-9 in file\n',y)
# y = re.findall('[AEIOU]+', x)
# print('\nFind character in file\n',y)
# y = re.findall('^I.+?t', x) #? is Non-Greedy คือการเลือกเอาที่ลงท้ายด้วย t ตัวแรก(ไม่ใช่ตัวที่2ของประโยค)
# print('\nFind first Char is I and last char is t \n',y)
# y = re.findall('\S+u\S+', x) #\S is blank
# print('\nFind word when left side and right side are blank\n',y)
# y = re.findall('the \S+a\S+', x) #\S is blank
# print('\nFind word when start with "the" and left side and right side are blank\n',y)
# y = re.findall('@([^ ]*)', x) #[^ ] is Match non-blank character
# print('\n1 find host of email\n',y)
# y = re.findall('From .*@([^ ]*)', x) #[^ ] is Match non-blank character
# print('\n2 find host of email\n',y)

# print('hello world')
# print('hello world')


# #Check if the string starts with "The" and ends with "Spain":


# print(re.findall('From .*@([^ ]*)', x))
for line in x:
    if not line.startswith('From: '): continue
    pieces = line.split()
    email = pieces[1]
    print(email)


fopen.close()
print('--------------end--------------')




















