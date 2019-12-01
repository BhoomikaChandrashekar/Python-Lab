from operator import itemgetter
sentences=[]
l=[]
class rev:
    def __init__(self,sentence):
        self.sentence=sentence
    
    def reve(self):
        temp=""
        tempar=[]
        tempar=self.sentence.split(" ")
        tempar.reverse()
        for i in tempar:
            temp=temp+i+" "
        count=0;
        for i in range(0,len(temp)):
            ch=temp[i]
            if(ch=='a' or ch=='e' or ch=='o' or ch=='u'):
                count+=1
        sentences.append({"count":count,"sentence":temp})

s1=rev(input("Enter the string:"))
s1.reve()
s2=rev(input("Enter the string:"))
s2.reve()
s3=rev(input("Enter the string:"))
s3.reve()
print(sentences)
sortedArr=sorted(sentences,key=itemgetter('count'),reverse=True)

for s in sortedArr:
    print(s['sentence'])



            

    