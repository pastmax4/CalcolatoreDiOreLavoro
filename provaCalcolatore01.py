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
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------

str_DurataTeorica="7:12:00"

str_entr01="9:10:00"
str_usct01="12:15:00"

str_entr02="13:05:00"
str_usct02="15:30:00"

diff01 = diffTimeInterval(str_inStart=str_entr01,str_inEnd=str_usct01 )
diff02 = diffTimeInterval(str_inStart=str_entr02,str_inEnd=str_usct02 )
diffPranzo = diffTimeInterval(str_inStart=str_usct01, str_inEnd=str_entr02 )
durataGiornata= diff01 + diff02

#diffDurataTeorica = diffTimeInterval(str_inStart=str_DurataTeorica, str_inEnd= str(durataGiornata))

print('Ingresso  Mattino:',str_entr01)
print('Uscita     Pranzo:',str_usct01)
print('Ingresso   Pranzo:',str_entr02)
print('Uscita Pomeriggio:',str_usct02)
print('')
print('Numero ore Mattina   :',diff01)
print('Numero ore Poneriggio:',diff02)
print('Durata giornata      :',durataGiornata)
print('Durata pausa Pranzo  :',diffPranzo)


str_durataGiornata=str(durataGiornata)
lst_durataGiornata=str_durataGiornata.split(':')

ore   = int(lst_durataGiornata[0])
minuti= int(lst_durataGiornata[1])

if ore > 7:
    diffTeorica=dt.timedelta( minutes=minuti ,hours= ore)- dt.timedelta(minutes=12,hours=7)
    print('Differenza teorica   :', '+'+str(diffTeorica))

elif ore == 7:
    if minuti>12:
        diffTeorica = dt.timedelta(minutes=minuti, hours=ore) - dt.timedelta(minutes=12, hours=7)
        print('Differenza teorica   :', '+' + str(diffTeorica))
    else:
        diffTeorica = dt.timedelta(minutes=12, hours=7) - dt.timedelta(minutes=minuti, hours=ore)
        print('Differenza teorica   :', '-' + str(diffTeorica))
        bool_recupero = True
else:
    diffTeorica = dt.timedelta(minutes=12, hours=7) - dt.timedelta(minutes=minuti, hours=ore)
    print('Differenza teorica   :', '-'+str(diffTeorica))
    bool_recupero=True




if bool_recupero == True:
    str_diffTeorica=str(diffTeorica)
    lst_diffTeorica = str_diffTeorica.split(':')
    oreTeo = int(lst_diffTeorica[0])
    minutiTeo = int(lst_diffTeorica[1])
    dt_uscitaReale = dt.datetime.strptime(str_usct02, '%H:%M:%S')
    uscitaTeorica = dt_uscitaReale + dt.timedelta(minutes=minutiTeo, hours=oreTeo)
    str_uscitaTeorica=str(uscitaTeorica)[10:]
    print('')
    print('Uscita teorica:   ',str_uscitaTeorica)

print('---------=======----------------')
print('Finito')
