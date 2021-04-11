def AnalyseStudents(SN):
    try:
        if(len(SN)!=8):
            return 0
        else:
            sum = 0
            count = 8
            for digit in SN:
                sum = sum + int(digit)*count
                count = count - 1
            if(sum%11==0):
                return 1
            else:
                return 0
    except:
        return 0

def Read(list):
    try:
        FILE = open("Data.txt",'r')
        count = 0
        for line in FILE:
            list.append(line.rstrip())
            count = count + 1
        FILE.close()
        return count
    except:
        print("Error! File could not be read")
        exit()



def Write(num,status):
    if(status==1):
        FILE=open("ValidNumbers.txt",'a')
        FILE.write(num+'\n')
        FILE.close()
        print(num,"is an VALID student number")
    else:
        FILE = open("InvalidNumbers.txt",'a')
        FILE.write(num+'\n')
        FILE.close()
        print(num,"is an INVALID student number")

numb = []
print("Number of lines read: ",Read(numb))

for numg in numb:
    Write(numg,AnalyseStudents(numg))

print("-->See output files for more details")
