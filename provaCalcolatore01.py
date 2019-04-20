'''
19Aprile2019
Massimo Pasteris
https://stackoverflow.com/questions/3096953/how-to-calculate-the-time-interval-between-two-time-strings
'''
import datetime as dt
#from datetime import timedelta

#--------------------------------------------------------------------------
def diffTimeInterval(str_inStart,str_inEnd):
    dt_startT = dt.datetime.strptime(str_inStart, '%H:%M:%S')
    dt_endT = dt.datetime.strptime(str_inEnd, '%H:%M:%S')
    diff = (dt_endT - dt_startT)
    #print(diff)
    return diff

#--------------------------------------------------------------------------
str_DurataTeorica="7:12:00"

str_entr01="9:10:00"
str_usct01="12:15:00"

str_entr02="13:05:00"
str_usct02="16:30:00"

diff01 = diffTimeInterval(str_inStart=str_entr01,str_inEnd=str_usct01 )
diff02 = diffTimeInterval(str_inStart=str_entr02,str_inEnd=str_usct02 )
diffPranzo = diffTimeInterval(str_inStart=str_usct01, str_inEnd=str_entr02 )
durataGiornata= diff01 + diff02

#diffDurataTeorica = diffTimeInterval(str_inStart=str_DurataTeorica, str_inEnd= str(durataGiornata))

print('Numero ore Mattina   :',diff01)
print('Numero ore Poneriggio:',diff02)
print('Durata giornata      :',durataGiornata)
print('Durata pausa Pranzo  :',diffPranzo)
#print('Diffrenza teorica    :',diffDurataTeorica)


str_durataGiornata=str(durataGiornata)
lst_durataGiornata=str_durataGiornata.split(':')

ore   = int(lst_durataGiornata[0])
minuti= int(lst_durataGiornata[1])

if ore > 7:
    diffTeorica=dt.timedelta( minutes=minuti ,hours= ore)- dt.timedelta(minutes=12,hours=7)
else:
    diffTeorica = dt.timedelta(minutes=12, hours=7) - dt.timedelta(minutes=minuti, hours=ore)
    print('Differenza teorica   :', '-'+str(diffTeorica))


print('---------=======----------------')



print('Finito')


