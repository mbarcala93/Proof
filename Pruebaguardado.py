import pickle

class depuradora:
    def __init__(self, municipio, habitantes):

        self.municipio=municipio
        self.habitantes=habitantes
        print("Se ha creado una depuradora en el municipio de ",self.municipio)

    def __str__(self):
        return "{}  {}".format(self.municipio, self.habitantes)

class ListaDepuradoras:

    EDAR=[]

    def __init__(self):

        listaEDAR=open("Inventario.csv", "ab+")
        listaEDAR.seek(0)#mover el cursor al inicio del fichero externo "Inventario" para cuando se lea, lo haga desde el principio

        try:
            self.EDAR=pickle.load(listaEDAR)
            print("Existen {} depuradoras en el inventario".format(len(self.EDAR)))

        except:
            print("El fichero está vacío")

        finally:
            listaEDAR.close()
            del(listaEDAR)

    def agregarDEP(self, edar):
        self.EDAR.append(edar)
        self.guardarDEP()

    def guardarDEP(self):
        listaEDAR=open("Inventario.csv", "wb")
        pickle.dump(self.EDAR, listaEDAR)
        listaEDAR.close()
        del(listaEDAR)

    def mostrarDEP(self):
        if len(self.EDAR)<1:
            print("El inventario está sin empezar, deberías ponerte al turrón")
        else:
            print("La información del inventario es la siguiente:\nMunicipio    Habitantes")
        for i in self.EDAR:
            print(i)


print("¿Qué desea realizar? Marque el número de la opción y pulse Enter\n1) Ver inventario de depuradoras\n2) Agregar depuradora\n3) Salir")
op=(int(input("Marque el código de la opción: ")))
while op<1 or op>3:
    print("Código no encontrado")
    print("¿Qué desea realizar? Marque el número de la opción y pulse Enter\n1) Ver inventario de depuradoras\n2) Agregar depuradora\n3) Salir")
    op=(int(input("Marque el código de la opción: ")))
#def eleccion(op):
if op==1:
    milista=ListaDepuradoras()
    milista.mostrarDEP()

elif op==2:
    milista=ListaDepuradoras()
    municipio=(input("Nombre del municipio de la nueva EDAR: "))
    habitantes=input("Capacidad de la EDAR en habitantes equivalentes: ")
    newedar=depuradora(municipio, habitantes)
    milista.agregarDEP(newedar)

elif op==3:
    print("Saliendo...")

print("\nGracias por su participación, que la fuerza le acompañe")
