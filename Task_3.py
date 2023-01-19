def coding(file):
    count = 1
    result = ''
    for i in range(len(file)-1):
        if file[i] == file[i+1]:
            count += 1
        else:
            result = result + str(count) + file[i]
            count = 1
    if count > 1 or (file[len(file)-2] != file[-1]):
        result = result + str(count) + file[i-1]
    return result

def decoding(file):
    num=''
    res=''
    for i in range(len(file)):
        if not file[i].isalpha():
            num+=file[i]
        else:
            res=res + file[i]*int(num)
            num=''
    return res
with open('file.txt') as data:
     trans1=data.read()
with open('transform.txt','w') as data:
    data.writelines(coding(trans1))
with open('transform.txt','r') as data:
     trans2=data.read()
with open('transform2.txt','w') as data:
    data.writelines(decoding(trans2))  


