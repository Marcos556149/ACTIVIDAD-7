from ClaseHora import Hora
class FechaHora:                                      #ejercicio 7
    __year = 0
    __mes = 0
    __dia = 0
    __hora = 0
    __minutos = 0
    __segundos = 0
    __meses = [1,2,3,4,5,6,7,8,9,10,11,12]
    def __init__(self,a=2020,mess=1,d=1,h=0,m=0,s=0):
        if (self.verificarHora(h,m,s))and(self.verificarFecha(a,mess,d)):
            self.__year=a
            self.__mes=mess
            self.__dia=d
            self.__hora=h
            self.__minutos=m
            self.__segundos=s
        else:
            print("ERROR, Los datos que ingreso son invalidos")
            self.__year = -1
    def test(self):
        print("TEST DE FECHA HORA\n")
        datosCorrectos1= FechaHora(2020,5,17,20,50,58)
        datosIncorrectos1= FechaHora(2017,13,18,5,13,51)
        datosCorrectos2= FechaHora(2016,2,29,1,4,0)
        datosIncorrectos2= FechaHora(2015,2,29,23,59,59)
        datosCorrectos1.Mostrar()
        input()
        datosIncorrectos1.Mostrar()
        input()
        datosCorrectos2.Mostrar()
        input()
        datosIncorrectos2.Mostrar()
        print("\nTEST DE FECHA HORA REALIZADO EXITOSAMENTE\n")
    def Mostrar(self):
        if self.__year != -1:
            print(str(self.__hora)+'/',str(self.__minutos)+'/',str(self.__segundos),'  ',str(self.__dia)+'/',str(self.__mes)+'/',str(self.__year))
        else:
            print("No es posible Mostrar por pantalla la Fecha y la Hora ya que los datos de ingreso son incorrectos")
    def verificarHora(self,h,m,s):
        if (h>=0)and(h<=23)and(m>=0)and(m<=59)and(s>=0)and(s<=59) :
            return True
        else:
            return False
    def verificarFecha(self,a,mess,d):
        if (a>0)and(mess>=1)and(mess<=12)and(d>=1)and(d<=31):
            if (mess==2)and(d==29)and(self.verificarBisiesto(a)):
                return True
            elif self.verificarMesDia(mess,d) == 0:
                return True
            else:
                return False
    def verificarBisiesto(self,a):
        if a % 4 !=0:
            return False
        elif (a % 4 == 0)and(a % 100 != 0):
            return True
        elif (a % 4 == 0)and(a % 100 == 0)and(a % 400 != 0):
            return False
        elif (a % 4 == 0)and(a % 100 == 0)and(a % 400 == 0):
            return True
    def verificarMesDia(self,mess,d):
        if ((mess==self.__meses[0])or(mess==self.__meses[2])or(mess==self.__meses[4])or(mess==self.__meses[6])or(mess==self.__meses[7])or(mess==self.__meses[9])or(mess==self.__meses[11]))and(d>31):
            return 1
        elif ((mess==self.__meses[3])or(mess==self.__meses[5])or(mess==self.__meses[8])or(mess==self.__meses[10]))and(d>30):
            return 2
        elif (mess==self.__meses[1])and(d>28):
            return 3
        else:
            return 0
    def verificarMesDiaParaLista(self,listaFechaHora):
        if ((listaFechaHora[4]==1)or(listaFechaHora[4]==3)or(listaFechaHora[4]==5)or(listaFechaHora[4]==7)or(listaFechaHora[4]==8)or(listaFechaHora[4]==10)or(listaFechaHora[4]==12))and(listaFechaHora[3]>31):
            return 1
        elif ((listaFechaHora[4]==4)or(listaFechaHora[4]==6)or(listaFechaHora[4]==9)or(listaFechaHora[4]==11))and(listaFechaHora[3]>30):
            return 2
        elif (listaFechaHora[4]==2)and(listaFechaHora[3]>28):
            return 3
        else:
            return 0
    def AdelantarHora(self,listaFechaHora):
            if (listaFechaHora[0] > 59)or(listaFechaHora[1] > 59)or(listaFechaHora[2] > 23):
                cont1=0
                cont2=0
                cont3=0
                while listaFechaHora[0] > 59:
                    cont1 += 1
                    listaFechaHora[0] -= 60
                listaFechaHora[1] += cont1
                while listaFechaHora[1] > 59:
                    cont2 += 1
                    listaFechaHora[1] -= 60
                listaFechaHora[2] += cont2
                while listaFechaHora[2] > 23:
                    cont3 += 1
                    listaFechaHora[2] -= 24
                listaFechaHora[3] += cont3
                if cont3 == 1:
                    self.AdelantarFecha(listaFechaHora)
    def AdelantarFecha(self,listaFechaHora):
        if (self.verificarMesDiaParaLista(listaFechaHora) == 1):
            listaFechaHora[3] -= 31
            listaFechaHora[4] += 1
            if listaFechaHora[4] > 12:
                listaFechaHora[4] -= 12
                listaFechaHora[5] += 1
        elif (self.verificarMesDiaParaLista(listaFechaHora) == 2):
            listaFechaHora[3] -= 30
            listaFechaHora[4] += 1
        elif (self.verificarMesDiaParaLista(listaFechaHora) == 3):
            if self.verificarBisiesto(listaFechaHora[5]):
                if listaFechaHora[3] > 29:
                    listaFechaHora[3] -= 29
                    listaFechaHora[4] += 1
            else:
                listaFechaHora[3] -= 28
                listaFechaHora[4] += 1
    def RestarFecha(self,listaFecha):
        if listaFecha[0] == 0:
            if ((listaFecha[1] - 1) == 1)or((listaFecha[1] - 1) == 3)or((listaFecha[1] - 1) == 5)or((listaFecha[1] - 1) == 7)or((listaFecha[1] - 1) == 8)or((listaFecha[1] - 1) == 10):
                listaFecha[0]= 31
                listaFecha[1] -= 1
            elif ((listaFecha[1] - 1) == 4)or((listaFecha[1] - 1) == 6)or((listaFecha[1] - 1) == 9)or((listaFecha[1] - 1) == 11):
                listaFecha[0]= 30
                listaFecha[1] -= 1
            elif ((listaFecha[1] - 1) == 2):
                if self.verificarBisiesto(listaFecha[2]):
                    listaFecha[0]= 29
                    listaFecha[1] -= 1
                else:
                    listaFecha[0]= 28
                    listaFecha[1] -= 1
            elif (listaFecha[1] == 1):
                listaFecha[0]= 31
                listaFecha[1] = 12
                listaFecha[2] -= 1
    def getSegundos(self):
        return self.__segundos
    def getMinutos(self):
        return self.__minutos
    def getHora(self):
        return self.__hora
    def getDia(self):
        return self.__dia
    def getMes(self):
        return self.__mes
    def getYear(self):
        return self.__year
    def __add__(self,UnaHora):
        horaa= self.__hora + UnaHora.getHora()
        minutoo= self.__minutos + UnaHora.getMinutos()
        segundoo= self.__segundos + UnaHora.getSegundos()
        diass= self.__dia
        mees= self.__mes
        yearr= self.__year
        listaFechaHora= [segundoo,minutoo,horaa,diass,mees,yearr]
        self.AdelantarHora(listaFechaHora)
        return FechaHora(listaFechaHora[5],listaFechaHora[4],listaFechaHora[3],listaFechaHora[2],listaFechaHora[1],listaFechaHora[0])
    def __radd__(self,otro):
        if type (otro) == Hora:
            horaa1= self.__hora + otro.getHora()
            minutoo1= self.__minutos + otro.getMinutos()
            segundoo1= self.__segundos + otro.getSegundos()
            diass1= self.__dia
            mees1= self.__mes
            yearr1= self.__year
            listaFechaHora1= [segundoo1,minutoo1,horaa1,diass1,mees1,yearr1]
            self.AdelantarHora(listaFechaHora1)
            return FechaHora(listaFechaHora1[5],listaFechaHora1[4],listaFechaHora1[3],listaFechaHora1[2],listaFechaHora1[1],listaFechaHora1[0])
        elif type (otro) == int:
            segg= self.__segundos
            minn= self.__minutos
            horr= self.__hora
            diaaa= self.__dia + otro
            messss= self.__mes
            yea= self.__year
            listaFechaHora3= [segg,minn,horr,diaaa,messss,yea]
            self.AdelantarFecha(listaFechaHora3)
            return FechaHora(listaFechaHora3[5],listaFechaHora3[4],listaFechaHora3[3],listaFechaHora3[2],listaFechaHora3[1],listaFechaHora3[0])
    def __sub__(self,entero):
        yearrr= self.__year
        messs= self.__mes
        diasss= self.__dia - entero
        listaFecha= [diasss,messs,yearrr]
        self.RestarFecha(listaFecha)
        if listaFecha[2] == 0:
            print("ERROR, el calculo de la resta da como resultado año 0, la cual es una fecha no valida")
            listaFecha[2] = -1
        return FechaHora(listaFecha[2],listaFecha[1],listaFecha[0],self.__hora,self.__minutos,self.__segundos)



