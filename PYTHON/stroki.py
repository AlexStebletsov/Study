


string = input("ss")
print(string[::-1])

string = input("s's'")
Enter = False
word = False
string1 = ""


for i in range (0,len(string)-1):
    if(string[i] == '\''):
        if(Enter == False):
            word = True
            Enter = True
            continue
        if(Enter == True):
            word = False
            continue
    if(word):
        print(string[i])
        string1 += string[i]

print (string1)
string = input("Число")
print(int(string)**2)

string, string1 = input("2 строки").split()

print(string1,string)

string= input("Номер")
string1 = ""

for i in range (0,len(string)-1):
    if(string[i] == '-') or (string[i] == ' ') or (string[i] == ')') or (string[i] == '('):
        continue
    string1 += string[i]

print(string1)

string= input("Полиндром")

if (string[::-1] == string):
    print(True)
else:
    print(False)

string = ""
string1 = ""
for i in range (1,123):
    string += str(i)


for i in range (0,123):
    if(string[i] == '9') :
        continue
    string1 += string[i]

print(string1)


for num in range(100, 1000):
    sum1=0
    numcp=num
    if(num>=10 and num<100):
        while(num>0):
            digit=int(num%10)
            d2=digit*digit
            sum1=sum1+d2
            num=int(num/10)

    if(num>=100 and num<1000):
        while(num>0):
            digit=int(num%10)
            d2=digit*digit*digit
            sum1=sum1+d2
            num=int(num/10)
    if(numcp==sum1):
        print("Число Армстронга : ",sum1)


N = input("Введите N")

mod = 10
for i in range(1, int(N) + 1):
    if i == mod:
        mod *= 10
    if (i * i) % mod == i:
        print(i)

count = 0
for i in range(1, 13):
    for j in range(1,11):
        for k in range(1,9):
            if(i*15 + j*17 + k*21 == 185):
                print (i,"-первой", j,"-второй", k,"-третьей")
                count += 1
print(count)