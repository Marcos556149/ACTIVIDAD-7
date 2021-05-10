from ClaseFechaHora import FechaHora
from ClaseHora import Hora
if __name__=='__main__':
    pruebaTest= FechaHora()
    pruebaTest.test()
    pruebaTest1= Hora()
    pruebaTest1.test()
    a= int(input('Ingrese año: '))
    mes= int(input('Ingrese mes: '))
    d= int(input('Ingrese dia: '))
    h= int(input('Ingrese hora: '))
    m= int(input('Ingrese minutos: '))
    s= int(input('Ingrese segundos: '))
    f= FechaHora(a,mes,d,h,m,s)
    f.Mostrar()
    input()
    h1= int(input('Ingrese hora: '))
    m1= int(input('Ingrese minutos: '))
    s1= int(input('Ingrese segundos: '))
    r= Hora(h1,m1,s1)
    r.Mostrar()
    input()
    f2= f+r
    f2.Mostrar()
    input()
    f3= r+f
    f3.Mostrar()
    input()
    f4= f3-1
    f4.Mostrar()
    f4= 1+f2
    f4.Mostrar()
    input()

