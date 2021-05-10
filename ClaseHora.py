class Hora:
    __horass= 0
    __minutoss= 0
    __segundoss= 0
    def __init__(self,hh=0,mm=0,ss=0):
        if (hh >= 0)and(hh <= 23)and(mm >= 0)and(mm <= 59)and(ss >= 0)and(ss <= 59):
            self.__horass = hh
            self.__minutoss = mm
            self.__segundoss = ss
        else:
            print("ERROR, datos de hora incorrectos")
            self.__horass = -1
    def test(self):
        print("TEST DE HORA\n")
        Correcta1= Hora(23,59,59)
        Incorrecta1= Hora(24,30,22)
        Correcta2= Hora(0,0,0)
        Incorrecta2= Hora(10,67,1)
        Correcta1.Mostrar()
        input()
        Incorrecta1.Mostrar()
        input()
        Correcta2.Mostrar()
        input()
        Incorrecta2.Mostrar()
        input()
        print("\nTEST DE HORA REALIZADO CORRECTAMENTE\n")
    def Mostrar(self):
        if self.__horass != -1:
            print(str(self.__horass)+'/',str(self.__minutoss)+'/',str(self.__segundoss))
        else:
            print("No es posible mostrar la Hora ya que los datos ingresados fueron incorrectos")
    def getHora(self):
        return self.__horass
    def getMinutos(self):
        return self.__minutoss
    def getSegundos(self):
        return self.__segundoss


