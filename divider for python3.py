print("                       [+]Scripted By Mohamed Hassan[+]\n")
url=input(str(("[+]Enter the dir of list with out "".txt"" as ""c:\\users\pc\desktop\list[+]\n")))
dev=int(input("[+]Enter the number of the elements in one list[+]\n"))
with open(url+".txt",mode="r") as f:
        a=f.readlines()
maxm=len(a)
b=1
c=1
while not c ==((maxm/dev)+1):
        for mail in a:
                if mail == a[b-1]:
                        with open(url+"_"+str(c)+".txt",mode="a")as f:
                                f.write(mail)
                        if b==dev*c:
                                break
                        b=b+1
        c=c+1
print("[+]Done------>Scripted By Mohamed Hassan[+]")
input("{=}Press Enter To Exit[=]")

