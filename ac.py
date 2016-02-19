import pprint
import pickle
codes=[]

#Quick hack to get the airport codes from the NET into a Python Pickle Object

#wget http://www.nationsonline.org/oneworld/IATA_Codes/airport_code_list.htm 
ifp=open('airport_code_list.htm','r')
for line in ifp:
    fld=line.split('\t')
    if len(fld)==3:
        fld[2]=fld[2].replace('\n','')
        codes.append(fld)


keys=[a[2] for a in codes]
data=[ [a[0],a[1]] for a in codes]
acodes=dict(zip(keys, data))
pickle.dump( acodes, open( "airport_codes.pickle", "wb" ) )
