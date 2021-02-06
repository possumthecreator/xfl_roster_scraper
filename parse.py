import get_rosters
import regex as re

dallas = get_rosters.run_dalren()

#p1 = re.compile('(a(b)c)d')


p = re.compile(r'\W+')
p.split(str(dallas))
#print(dallas[1])


#for i in dallas:
#    print(i)

#run_dalren()
#run_dcdef()
#run_hourou() #dif & name reversed
#run_lawil()
#run_nygau() #dif
#run_stlbat() #dif
#run_seadra() #dif
#run_tbvip() #dif

