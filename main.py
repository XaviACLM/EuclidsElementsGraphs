from urllib.request import urlopen
import re
import pickle
from PIL import Image as image

global rom
rom=["I","II","III","IV","V","VI","VII","VIII","IX","X","XI","XII","XIII"]

"""
rprop = re.compile(r"href=.*?prop([I,V,X]*)(.+?).html", re.IGNORECASE)
rdef= re.compile(r"href=.*?>([I,V,X]+)\.Def\.(.+?)<", re.IGNORECASE)
rpost= re.compile(r"href=.*?>I?\.?Post\.(.)<", re.IGNORECASE)
rcn = re.compile(r"href=.*?>C\.N\.(.)</a", re.IGNORECASE)

def l2p(bookn,propn):
    return urlopen("https://mathcs.clarku.edu/~djoyce/java/elements/book"
                   +rom[bookn-1]
                   +"/prop"
                   +rom[bookn-1]
                   +str(propn)
                   +".html").read().decode('utf-8')

rdict=["B1POST1","B1POST2","B1POST3","B1POST4","B1POST5","B1CN1","B1CN2","B1CN3","B1CN4","B1CN5"]
nec=[]
deffn=[]
propn=[]
for i in range(len(rdict)):
    nec.append([])
for i in range(1,5):
    bsurl = urlopen("https://mathcs.clarku.edu/~djoyce/java/elements/book{0}/book{0}.html".format(rom[i-1])).read().decode('utf-8')
    deffn.append((lambda x:0 if x==None else int(x.group(1)))(re.search(r"Definitions.+?\((.+?)\)", bsurl, re.IGNORECASE)))
    propn.append(int(re.search(r"propositions.+?\((.+?)\)", bsurl, re.IGNORECASE).group(1)))
    for k in range(1,deffn[i-1]+1):
        rdict.append("B"+str(i)+"DEF"+str(k))
        nec.append([])
    for j in range(1,propn[i-1]+1):
        rdict.append("B"+str(i)+"PROP"+str(j))
        print("Book",rom[i-1],"Proposition",j)
        cprop=l2p(i,j)
        cprop=re.split(r"h2>Guide</h2",cprop)[0]
        cnec=["B1POST"+str(a[0]) for a in rpost.findall(cprop)]
        cnec+=["B1CN"+str(a) for a in rcn.findall(cprop)]
        cnec+=["B"+str(rom.index(a[0])+1)+"DEF"+i for a in rdef.findall(cprop) for i in re.split(',', a[1])]
        cnec+=["B"+str(rom.index(a[0])+1)+"PROP"+str(a[1]) for a in rprop.findall(cprop)]
        nec.append([rdict.index(a) for a in cnec])
for i in range(len(rdict)): print(rdict[i]+":", ", ".join(rdict[j] for j in nec[i]), "\n")
for i in range(len(nec)):
    j=0
    while j<len(nec[i]):
        if nec[i].index(nec[i][j])!=j:
            nec[i].pop(j)
        else:j+=1
            
#rick.dump((nec,rdict,deffn,propn),open("yoqueselol","wb"))
        
imp=[]
for i in range(len(nec)):
    imp.append([])
    for j in range(i,len(nec)):
        if i in nec[j]:
            imp[-1].append(j)
print(imp)

"""
nec,imp,rdict,deffn,propn=pickle.load(open("cache","rb"))

#########
def isculled(index):
    #if "DEF" in rdict[index]:
    #    return True
    #if "PROP" in rdict[index]:
    #    if int(rdict[index][1:rdict[index].index("P")])>4:
    #        return True
    return False

#for i in range(len(nec)):print(i,nec[i],imp[i])




for i in range(len(deffn)):deffn[i]=0
for i in range(4,len(propn)):propn[i]=0
i=0
while i<len(rdict):
    if isculled(i):
        rdict.pop(i)
        nec.pop(i)
        j=i
        while j<len(nec):
            k=0
            while k<len(nec[j]):
                if nec[j][k]>i:
                    nec[j][k]-=1
                if nec[j][k]==i:
                    nec[j].pop(k)
                else:
                    k+=1
            j+=1
        j=0
        while j<i:
            k=0
            while k<len(imp[j]):
                if imp[j][k]>i:
                    imp[j][k]-=1
                    k+=1
                else:
                    if imp[j][k]==i:
                        imp[j].pop(k)
                    else:
                        k+=1
            j+=1
        imp.pop(j)
        while j<len(imp):
            k=0
            while k<len(imp[j]):
                if imp[j][k]>i:
                    imp[j][k]-=1
                k+=1
            j+=1
    else:
        i+=1
#########

amt=len(rdict)

print(amt,sum([len(x) for x in nec]))
##print(dppd)
#for i in range(len(nec)):print(i,nec[i],imp[i])

groups=[]
cind=0
while cind<amt:
    cmin=amt
    groups.append([])
    while cind<cmin:
        groups[-1].append(cind)
        cmin=min(cmin,amt if not imp[cind] else min(imp[cind]))
        cind+=1

#for i in groups: print(i)

for i in range(len(rdict)):
    print(rdict[i],len(imp[i]),len(nec[i]))
##print(gu)

rightgroups=[]
leftgroups=[]
for i in groups:
    rightgroups.append([])
    leftgroups.append([])
    for j in i:
        if "PROP" in rdict[j]:
            rightgroups[-1].append(j)
        else:
            leftgroups[-1].append(j)

isrequired=[]
for i in range(len(groups)):
    for j in groups[i]:
        c=0
        for k in imp[j]:
            if k not in groups[i+1]:
                c=1
        isrequired.append(c==1)

bus=[]
for i in range(len(groups)-1):
    #bus.append([-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1])#,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1])
    bus.append([-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1])
for i in range(len(groups)-1):
    for j in leftgroups[i]:
        if imp[j]:
            k=0
            while bus[i][k]>=0:
                k+=1
            u=i
            while max(imp[j]) not in groups[u]:
                bus[u][k]=j
                u+=1
    for j in rightgroups[i]:#[::-1]:
        if isrequired[j]:
            k=len(bus[1])-1
            while bus[i][k]>=0:
                k-=1
            u=i
            while max(imp[j]) not in groups[u]:
                bus[u][k]=j
                u+=1
                
#for i in bus:print(i)

busleftx=45*(max([len(x) for x in leftgroups]))
busrightx=busleftx+15*len(bus[0])
grouptopy=[0]
for i in range(len(rightgroups)-1):
    grouptopy.append(grouptopy[-1]+15*(1+max(len(leftgroups[i]),[isrequired[x] for x in rightgroups[i]].count(True))+len(rightgroups[i+1])))
#print(grouptopy,busleftx,busrightx)

#####################################################################################################################################################################################################################################
im=image.new("RGB",(busrightx+45*(max([len(x) for x in rightgroups])),15+grouptopy[-1]),"white")

propbox=image.new("RGB",(30,15),(212,54,22))
postbox=image.new("RGB",(30,15),(4,38,78))
commbox=image.new("RGB",(30,15),(4,38,78))
deffbox=image.new("RGB",(30,15),(222,163,6))

verwire=image.new("RGB",(15,15),"white")
verwire.paste(image.new("RGB",(5,15),(150,150,150)),(5,0))
verwirecr=image.new("RGB",(9,15),"white")
verwirecr.paste(image.new("RGB",(5,15),(150,150,150)),(2,0))
horwire=image.new("RGB",(15,15),"white")
horwire.paste(image.new("RGB",(15,5),(150,150,150)),(0,5))
horwirecr=image.new("RGB",(15,9),"white")
horwirecr.paste(image.new("RGB",(15,5),(150,150,150)),(0,2))
ULwire=image.open("resources/ULwire.png")
DLwire=image.open("resources/DLwire.png")
URwire=image.open("resources/URwire.png")
DRwire=image.open("resources/DRwire.png")
URwireD=image.open("resources/URwireD.png")
URwireL=image.open("resources/URwireL.png")
URwireLcr=image.open("resources/URwireLcr.png")
ULwireD=image.open("resources/ULwireD.png")
ULwireR=image.open("resources/ULwireR.png")
DLRwire=image.open("resources/DLRwire.png")
ULwireRcr=image.open("resources/ULwireRcr.png")
proprom=[]
deffrom=[]
commrom=[]
postrom=[]
propnum=[]
deffnum=[]
commnum=[]
postnum=[]
for i in range(1,14):
    proprom.append(image.open("resources/prop"+str(i)+"rom.png"))
    deffrom.append(image.open("resources/deff"+str(i)+"rom.png"))
    commrom.append(image.open("resources/comm"+str(i)+"rom.png"))
    postrom.append(image.open("resources/post"+str(i)+"rom.png"))
for i in range(0,10):
    propnum.append(image.open("resources/prop"+str(i)+"num.png"))
    deffnum.append(image.open("resources/deff"+str(i)+"num.png"))
    commnum.append(image.open("resources/comm"+str(i)+"num.png"))
    postnum.append(image.open("resources/post"+str(i)+"num.png"))
    

for i in range(len(bus[0])):
    for j in range(1,len(bus)-1):
        if bus[j][i]!=-1 and bus[j][i] == bus[j-1][i] == bus[j+1][i]:
            for k in range(grouptopy[j],grouptopy[j+1],15):
                im.paste(verwire,(busleftx+15*i,k))
        if bus[j][i]!=-1 and bus[j][i]==bus[j-1][i] and bus[j][i]!=bus[j+1][i]:
            for k in range(grouptopy[j],grouptopy[j+1]-15*[nec[x]!=[] for x in rightgroups[j+1]].count(True),15):
                im.paste(verwire,(busleftx+15*i,k))
            try:
                for k in range(grouptopy[j],grouptopy[j+1]-15*rightgroups[j+1].index(min([x if bus[j][i] in nec[x] else 10000 for x in rightgroups[j+1]])),15):
                    im.paste(verwire,(busleftx+15*i,k))
            except:
                pass
                #no estem segurs de que dona aquest problema, i com que son dos o tres línies en total ho arreglarem a ma
        
                
for i in range(len(rightgroups)):
    if i!=len(rightgroups)-1 and i!=0:
        n=grouptopy[i]
        for j in range(len(rightgroups[i])):
            if(nec[rightgroups[i][j]]):
                n-=15
                k=grouptopy[i]-15
                ax=busrightx+45*j
                while k>n:
                    im.paste(verwirecr,(ax+3,k))
                    k-=15
                auxl=[]
                auxt=[]
                for u in nec[rightgroups[i][j]]:
                    if u in bus[i-1]:
                        auxl.append(busleftx+15*bus[i-1].index(u))
                        auxt.append(u)
                    else:
                        auxl.append(busrightx+15+45*rightgroups[i-1].index(u))
                        auxt.append(u)
                #print(i,j,rightgroups[i][j])
                #print("curgroups",rightgroups[i])
                #print("nec",nec[rightgroups[i][j]])
                #print("pregroup",rightgroups[i-1])
                #print("bus",bus[i-1])
                #input()
                h=min(min(auxl),ax)
                while h<max(max(auxl),ax)+15:
                    im.paste(horwirecr,(h,k+3))
                    h+=15
                if max(auxl)<ax:
                    im.paste(DLwire,(ax,k))
                elif min(auxl)>ax:
                    im.paste(DRwire,(ax,k))
                else:
                    im.paste(DLRwire,(ax,k))
                for auxi in auxl:
                    if auxi<ax and auxi<busrightx:
                        if auxi==min(auxl):
                            if auxt[auxl.index(auxi)] not in bus[i]+sum([nec[x] for x in rightgroups[i][:j]],[]):
                                im.paste(URwire,(auxi,k))
                            else:
                                im.paste(URwireD,(auxi,k))
                        else:
                            if auxt[auxl.index(auxi)] not in bus[i]+sum([nec[x] for x in rightgroups[i][:j]],[]):
                                im.paste(URwireL,(auxi,k))
                            else:
                                im.paste(URwireLcr,(auxi,k))
                    if auxi<ax and auxi>=busrightx:
                        #print([(auxt[auxl.index(auxi)]) for x in rightgroups[i]])
                        #print([(auxt[auxl.index(auxi)] in nec[x]) for x in rightgroups[i]])
                        if [(auxt[auxl.index(auxi)] in nec[x]) for x in rightgroups[i][:j]].count(True):
                            if auxi==min(auxl):
                                im.paste(URwireD,(auxi,k))
                            else:
                                im.paste(URwireLcr,(auxi,k))
                        else:
                            im.paste(URwireL,(auxi,k))
                        for h in range(k-15,grouptopy[i-1],-15):
                            im.paste(verwirecr,(auxi+3,h))
                    if auxi>=ax:
                        if auxi==max(auxl):
                            if [(auxt[auxl.index(auxi)] in nec[x]) for x in rightgroups[i][:j]].count(True):
                                im.paste(ULwireD,(auxi,k))
                            else:
                                im.paste(ULwire,(auxi,k))
                        else:
                            if [(auxt[auxl.index(auxi)] in nec[x]) for x in rightgroups[i][:j]].count(True):
                                im.paste(ULwireRcr,(auxi,k))
                            else:
                                im.paste(ULwireR,(auxi,k))
                        for h in range(k-15,grouptopy[i-1],-15):
                            im.paste(verwirecr,(auxi+3,h))
    n=grouptopy[i]
    for j in range(len(rightgroups[i])):
        rum=int(rdict[rightgroups[i][j]][1:rdict[rightgroups[i][j]].index("P")])-1
        dec=int(rdict[rightgroups[i][j]][rdict[rightgroups[i][j]].index("R")+3:])
        im.paste(propbox,(busrightx+45*j,grouptopy[i]))
        im.paste(proprom[rum],(busrightx+45*j,grouptopy[i]))
        im.paste(propnum[dec//10],(busrightx+45*j+15,grouptopy[i]))
        im.paste(propnum[dec%10],(busrightx+45*j+22,grouptopy[i]))
        if(isrequired[rightgroups[i][j]]):
            n+=15
            k=grouptopy[i]+15
            ax=busrightx+45*j
            while k<n:
                im.paste(verwire,(ax,k))
                k+=15
            h=u=-15*(len(bus[0])-bus[i].index(rightgroups[i][j]))+busrightx
            im.paste(DRwire,(u,k))
            u+=15
            while u<ax:
                im.paste(horwirecr,(u,k+3))
                u+=15
            #if [True if x in rightgroups[i+1] else False for x in imp[rightgroups[i][j]]].count(1):im.paste(ULwireD,(u,k))
            #else:im.paste(ULwire,(u,k))
            im.paste(ULwire,(u,k))
            k+=15
            while k<grouptopy[i+1]:
                im.paste(verwire,(h,k))
                k+=15
    n=grouptopy[i]
    for j in range(len(leftgroups[i])):
        if "POST" in rdict[leftgroups[i][j]]:
            rum=int(rdict[leftgroups[i][j]][1:rdict[leftgroups[i][j]].index("P")])-1
            dec=int(rdict[leftgroups[i][j]][rdict[leftgroups[i][j]].index("O")+3:])
            im.paste(postbox,(busleftx-45*(j+1),grouptopy[i]))
            im.paste(postrom[rum],(busleftx-45*(j+1),grouptopy[i]))
            im.paste(postnum[dec//10],(busleftx-45*(j+1)+15,grouptopy[i]))
            im.paste(postnum[dec%10],(busleftx-45*(j+1)+22,grouptopy[i]))
        elif "CN" in rdict[leftgroups[i][j]]:
            rum=int(rdict[leftgroups[i][j]][1:rdict[leftgroups[i][j]].index("C")])-1
            dec=int(rdict[leftgroups[i][j]][rdict[leftgroups[i][j]].index("N")+1:])
            im.paste(commbox,(busleftx-45*(j+1),grouptopy[i]))
            im.paste(commrom[rum],(busleftx-45*(j+1),grouptopy[i]))
            im.paste(commnum[dec//10],(busleftx-45*(j+1)+15,grouptopy[i]))
            im.paste(commnum[dec%10],(busleftx-45*(j+1)+22,grouptopy[i]))
        elif "DEF" in rdict[leftgroups[i][j]]:
            rum=int(rdict[leftgroups[i][j]][1:rdict[leftgroups[i][j]].index("D")])-1
            dec=int(rdict[leftgroups[i][j]][rdict[leftgroups[i][j]].index("E")+2:])
            im.paste(deffbox,(busleftx-45*(j+1),grouptopy[i]))
            im.paste(deffrom[rum],(busleftx-45*(j+1),grouptopy[i]))
            im.paste(deffnum[dec//10],(busleftx-45*(j+1)+15,grouptopy[i]))
            im.paste(deffnum[dec%10],(busleftx-45*(j+1)+22,grouptopy[i]))
        #im.paste()
        #im.paste()
        #im.paste()
        if(imp[leftgroups[i][j]]):
            n+=15
            k=15+grouptopy[i]
            h=busleftx-45*(j+1)+15
            while k<n:
                im.paste(verwire,(h,k))
                k+=15
            im.paste(URwire,(h,k))
            u=busleftx+15*(bus[i].index(leftgroups[i][j]))
            h+=15
            while h<u:
                im.paste(horwirecr,(h,k+3))
                h+=15
            im.paste(DLwire,(h,k))
            k+=15
            #AAAAAAAAAAAAAAAAAAAAAAAAAA
            if leftgroups[i][j]==bus[i+1][bus[i].index(leftgroups[i][j])]:
                while k<grouptopy[i+1]:
                    im.paste(verwire,(h,k))
                    k+=15
            else:
                while k<grouptopy[i+1]-15*rightgroups[i+1].index(min([x if leftgroups[i][j] in nec[x] else 10000 for x in rightgroups[i+1]])):
                    im.paste(verwire,(h,k))
                    k+=15
im.show()
#im.save("results/euc.png")
