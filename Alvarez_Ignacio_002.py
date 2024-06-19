import csv
lista=[]

def estadisticas(listita):
    acum=0
    prom=0
    mayor=0
    for i in listita:
        acum=acum+int(i[2])
        if int(i[2])>mayor:
            mayor=int(i[2])
        prom=acum/len(listita)
        print("promedio de puntajes: ",prom)
        print("puntaje mas alto: ",mayor)

def buscar(id_e,listita):
    encontrado=False
    for i in listita:
        if id_e==i[0]:
            print ("equipo encontrado \n")
            print(f"id: {i[0]},nombre: {i[1]},puntos: {i[2]},categoria: {i[3]}")
            encontrado=True
            break
        if encontrado==False:
            print ("Equipo no encontrado...")

def confirmar ():
    resp=input("Desea hacer esta operacion? (si/no): ".lower())
    if resp=="si":
        return True
    else:
        return False

def categoria(punt):
    while punt<0 or punt>150:
        punt=int(input("El puntaje debe ser entre 0 y 150, intente denuevo"))
    if punt>-1 and punt<150:

        if punt==0:
            cat=('Amateur')
            return cat
        
        elif punt<=40:
            cat=('Amateur')
            return cat
        
        elif punt<=80:
            cat=('Principiante')
            return cat
        
        elif punt<=120:
            cat=('Avanzado')
            return cat
        
        elif punt>120:
            cat=('Idolo')
            return cat
        
        else:
            print ("Categoria invalida")
    




def menu():
    print ("")
    print ("MENU")
    print ("1.- agregar equipo")
    print ("2.- listar equipo")
    print ("3.- actualizar nombre del equipo por id")
    print ("4.- generar base de datos")
    print ("5.- cargar base de datos")
    print ("6.- estadisticas")
    print ("0.- Salir")

    
while True:
    try:
        encontrado=False

        menu()
        op=int(input("Por favor, elija una opcion: "))

        if op==1:
            print("menu agregar")
            ide=int(input("numero del equipo: "))
            nombre=input("Nombre del equipo: ")
            puntos=int(input("Puntos del equipo: "))
            cat=categoria(puntos)

            equipo=[ide,nombre,puntos,cat]

            lista.append(equipo)
            print ("equipo agregado correctamente")
            

        elif op==2:
            print ("menu lista equipos")
            for x in lista:
                print (f"numero: {x[0]} nombre: {x[1]} puntos: {x[2]} categoria: {x[3]}")

        elif op==3:
            print ("actualizar nombre del equipo por id")
            busq=int(input("que equipo busca para modificar?"))
            encontrado=False

            for i in lista:
                if busq==i[0]:
                    print ("equipo encontrado \n")
                    print(f"id: {i[0]},nombre: {i[1]},puntos: {i[2]},categoria: {i[3]}")
                    confirmar()
                    if confirmar:
                        i[1]=input("Ingrese el nuevo nombre: ")
                        print("cambio realizado correctamente...")
                    encontrado=True
                    break
                if encontrado==False:
                    print ("Equipo no encontrado...")

        elif op==4:
            print ("Generar base de datos")
            print ("")
            with open ('bbdd.csv','w',newline='') as bbdd:
                escritor_csv = csv.writer(bbdd)
                escritor_csv.writerow(['id','nombre','puntos','categoria'])
                escritor_csv.writerows(lista)
                print ("base de datos generada correctamente")
                

        elif op==5:
            print ("cargar base de datos")
            print ("")
            lista.clear()
            cont=0
            with open ('bbdd.csv','r',newline='') as bbdd:
                lector_csv = csv.reader(bbdd)
                for fila in lector_csv:
                    if cont==0:
                        cont+=1
                        continue
                    ide=int(fila[0])
                    nombre=fila[1]
                    puntos=int(fila[2])
                    categoria=fila[3]
                    lista_añadir=[ide,nombre,puntos,categoria]
                    lista.append(lista_añadir)

        elif op==6:
            print ("estadisticas")
            estadisticas(lista)

        elif op==0:
            print ("Adios!")
            break
        else:
            print ("Por favor, elija una opcion valida")
    except:
        print ("Ha ocurrido un error!, intento realizar una operacion no valida?")

