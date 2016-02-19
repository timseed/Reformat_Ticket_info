import pprint
import pickle
codes=[]

ifp=open('junk','r')
for line in ifp:
    fld=line.split('\t')
    if len(fld)==3:
        fld[2]=fld[2].replace('\n','')
        codes.append(fld)


keys=[a[2] for a in codes]
data=[ [a[0],a[1]] for a in codes]
acodes=dict(zip(keys, data))
pickle.dump( acodes, open( "airport_codes.pickle", "wb" ) )
