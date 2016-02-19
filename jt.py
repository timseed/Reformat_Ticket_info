import re
from easygui import *
from airport_codes import airport_codes

Airports=airport_codes()

cnv=''

def MakeData(s):
    global cnv
    cnv=cnv+s

def ffr_out(Airline,Agent,Passenger):
    global cnv
    MakeData('\n')
    MakeData(str.format('Airline\t{}\n',Airline))
    MakeData(str.format('\tPassenger\t{}\n',Passenger))
    MakeData(str.format('\t\tAgent\t{}\n',Agent))
    MakeData('\n\n')
    MakeData('Airline\tFlight-Code\tDay\tMonth\tFrom\tTo\tTake-Off\tLand\tLand_Date\n')

def format_flight(m):
    MakeData(str.format("{}\t" ,m.group(1)))
    MakeData(str.format("{}\t" ,m.group(2)))
    MakeData(str.format("{}\t" ,m.group(3)))
    MakeData(str.format("{}\t" ,m.group(4)))
    MakeData(str.format("{} {} \t" ,m.group(5),Airports.get_Name(m.group(5))))
    MakeData(str.format("{} {} \t" ,m.group(6),Airports.get_Name(m.group(6))))
    MakeData(str.format("{}\t",m.group(7)))
    MakeData(str.format("{}\t",m.group(8)))
    #There may not be the Next Day
    if m.lastindex >8:
        MakeData(str.format("{}\n",m.group(9)))
    else:
        MakeData('\n')


def Convert(flight):
    test_flight = "Emirates\n\
    GAISYP\n\
     1.1DRIEMAN/BARTHOLOMEUS T H MR  2.1DONKELAAR/RONNIE MR\n\
    EK 150 20FEB  AMSDXB*  2200  0735  21FEB\n\
    EK 370 21FEB  DXBBKK*  1520  0020   22FEB\n\
    EK 371 04MAR  BKKDXB*  0155  0545\n\
    EK 147 04MAR  DXBAMS*  0810  1240\n"

    flight_re=re.compile('^([\w]+)[\s]+([\d]+)[\s]+([\d]{2})([A-Z]{3})[\s\d]+([\w]{3})([\w]{3})[*][\s]+([\d]{4})[\s]+([\d]{4})'
                         '([\s]+[\d]{2}[\w]{3})?')

    flight2_re=re.compile('^^([\w]+)[\s]+([\d]+)[\s]+([\d]{2})([\w]{3})[\s\d]+([\w]{3})([\w]{3})[\s]+([\d]+)[\s]+([\d]{4})[\s]?([\w\d]+)?')
    airline_re=re.compile('^[A-Z][a-z]+$')
    agent_re=re.compile('^[A-Z]+$')
    passenger_re=re.compile('^[\s][\d][\.][\d]')


    AIRLINE=''
    AGENT=''
    PASSENGERS=''
    ffr=True        #First Flight Record


    for a in flight.split('\n'):

        if airline_re.match(a):
            AIRLINE=a
        elif agent_re.match(a):
            AGENT=a
        elif passenger_re.match(a):
            PASSENGERS=a
            if ffr:
                ffr_out(AIRLINE,AGENT,PASSENGERS)
                ffr=False
        elif flight_re.match(a):
            if ffr:
                ffr_out(AIRLINE,AGENT,PASSENGERS)
                ffr=False
            m=flight_re.match(a)
            format_flight(m)
        elif flight2_re.match(a):
            if ffr:
                ffr_out(AIRLINE,AGENT,PASSENGERS)
                ffr=False
            m=flight2_re.match(a)
            format_flight(m)
    global cnv
    return cnv

flight_from_email=enterbox(msg='Paste the flight Info here', title='Enter Indeff Flight Details ', default='')
if len(flight_from_email)>10:
    new_data=Convert(flight_from_email)
    codebox(msg="Paste this into Excel",title="Converted Flight Data", text=new_data)
