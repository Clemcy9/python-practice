def toBase10(num,base):
    num = str(num)
    sum=0
    for i in range(0,len(num)):
        sum+=int(num[i])*(base**(len(num)-(i+1)))
    return sum  

print(toBase10(10000,2))


def from10toAnyBase(num,base):
    # result = num%base
    result =[num%base]
    # print('first res is:',result)
    Stresult = str(result)
    test=num//base
    # print('first test is:',test)
    while test !=0:
        
        result.append(test%base)
        test//=base 
        # print('2nd test is:', test)
        # print('result is: ',result)
    # result = result[-1::-1]
    # print('final value is:',result)
    if(base==16):
        for i in range(len(result)-1):
            if result[i]==10:
                result[i]='A'
            elif result[i]==11:
                result[i]='B'
            elif result[i]==12:
                result[i]='C'
            elif result[i]==13:
                result[i]='D'
            elif result[i]==14:
                result[i]='E'
            elif result[i]==15:
                result[i]='F'
    result = result[-1::-1]
    print('final value is:'+"".join(map(str, result)))

# from10toAnyBase(90,16)
from10toAnyBase(toBase10(10000,2),8)

# just testing git
