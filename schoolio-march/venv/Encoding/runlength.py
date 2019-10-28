def runlength(str1):
    count = 0
    lastletter = str1[0]

    for letter in str1:
        if letter == lastletter:
            count += 1
        elif letter != lastletter:
            print(lastletter,count)
            count = 1
            lastletter = letter
    print(lastletter, count)

runlength("aaabbbccccddddddeeeeaaaaa")
print("")

def runlength2(str1, length):
    currentstr = str1[0]
    first = False

    for letter in str1:
        if letter == currentstr[0]:
            currentstr += letter
        else:
            if first == False:
                if len(currentstr) > length + 1:
                    print(currentstr[0], len(currentstr) -1)
                    currentstr = letter
                else:
                    print(currentstr[:-1])
                    currentstr = letter
                first = True
            else:
                if len(currentstr) > length:
                    print(currentstr[0], len(currentstr))
                    currentstr = letter
                else:
                    print(currentstr)
                    currentstr = letter

    if len(currentstr) > length:
        print(currentstr[0], len(currentstr))
        currentstr = letter
    else:
        print(currentstr)
        currentstr = letter

runlength2("aaaabbbccccddddddeeeeaaaaa", 3)
print("")

def reverserunlength(str1):
    strout = ""
    for i in range(len(str1)):
        if str1[i].isalpha():
            strout += str1[i]
            previous = str1[i]
        elif str1[i].isdigit():
            if i < len(str1) - 1:
                if str1[i + 1].isdigit():
                    strout += previous * (int(str1[i] + str1[i + 1]) - 1)
            strout += previous * (int(str1[i]) - 1)
    print(strout)

reverserunlength("BBA4EB6AAAC12A14E")