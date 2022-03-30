#Evaluation
dic={'one':'1','two':'2','three':'3','four':'4','five':'5','six':'6','seven':'7','eight':'8','nine':'9','zero':'0','minus':'-','plus':'+','mutiply':'*','divide':'/'}
ques1='minusfiveminuseightminusminusseven'
counter=0
new_string=''
while len(ques1)!=0:
    if ques1[:counter] in dic:
        new_string +=dic[ques1[:counter]]
        ques1=ques1[counter:]
        counter=0
    else:
        counter+=1
    if len(ques1)==0:
        break
print (new_string)
print (eval(new_string))
x=str(int(eval(new_string)))
for i in dic:
   x=x.replace(str(dic.get(i)),i)
print(x)
