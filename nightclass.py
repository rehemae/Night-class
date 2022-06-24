a="I am AkiraChix"
new=a.split()
start=0
end=len(new)-1
while start<end:
    new[start],new[end]=new[end], new[start]
    start+=1
    end -=1
    str=""
x=(a.join(str))
if (x==a):
        print("true")
else:
        print("false")






x="my name is Rehema Ephraim"
# creating new variable for slip
new_word=x.split()
start=0
end=len(new_word)-1
while start<end:
    new_word[start],new_word[end]=new_word[end],new_word[start]
    start+=1
    end-=1
# creating new string so as the variable which changed to list to return to string
new_strng=""  
a=(x.join(new_strng))
print(a)  
 
if (x==new_strng):
    print("parindrome")
else:
     print("not parindrome")



