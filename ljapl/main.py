print("""
L       J    A    PPPP L
L       J   A A   P  P L
L       J  AAAAA  PPPP L
LLLL JJJ  A     A P    LLLL
Literally Just A Programing Language""")
n="\n"
while True:
  ce=f"0123456789{n} abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!#$%&'()*+,-./:;<=>?@[\]`|~"
  s=[];nc=0;b=[];e=0;num=[]
  out=[];inp=input(">>")
  for _ in range(10):num.append(str(_))
  if inp=="exit":break
  while len(inp)>nc:
    if inp[nc]=="+":s.append(int(s.pop(0))+int(s.pop(0)))
    elif inp[nc]in num[0:9]:s.append(int(inp[nc]))
    elif inp[nc]=="a":s.append(10)
    elif inp[nc]=="|":e=1;break
    elif inp[nc]=="n":out.append(int(s.pop(0)))
    elif inp[nc]=="c":out.append(ce[int(s.pop(0))])
    elif inp[nc]=="*":s.append(int(s.pop(0))*int(s.pop(0)))
    elif inp[nc]=="=":s.reverse();s.append(s[len(s)-1]);s.reverse()
    elif inp[nc]==";":s.append(s.pop(0))
    else:print("found an unknown command at",nc+1);break
    nc+=1
  if e==1:print("".join(str(out))+"\n")
