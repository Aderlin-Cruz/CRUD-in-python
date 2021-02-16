from tkinter import *
from tkinter import messagebox
import sqlite3
#------------------------funciones--------------------------------------------------------------------
def conexionBDD():
	miconexion=sqlite3.connect("Usuarios")
	micursor=miconexion.cursor()
	try:
	    micursor.execute('''
		    CREATE TABLE DATOSUSUARIOS(
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            NOMBRE_USUARIO VARCHAR(50),
            PASSWORD VARCHAR(50),
            APELLIDO VARCHAR(10),
            DIRECCION VARCHAR(50),
            COMENTARIOS VARCHAR(100))
            ''')
	    messagebox.showinfo("BBDD","BBDD Creada con éxito")
	except:
		messagebox.showwarning("!Atención¡", "La BBDD ya existe")
def salirApp():

	valor=messagebox.askquestion("Salir","Deseas Salir de la Aplicación")
	if valor=="yes":
		root.destroy()

def borrarCampos():
	miNombre.set("")
	miID.set("")
	miDireccion.set("")
	miApellido.set("")
	miPass.set("")
	textoComentario.delete(1.0,END)

#-----FUNCIONES CRUD ----------------------------------------------------------

def Crear():
	miconexion=sqlite3.connect("Usuarios")
	micursor=miconexion.cursor()


	micursor.execute("INSERT INTO DATOSUSUARIOS VALUES(NULL, '"+ miNombre.get()+
		"','" + miPass.get()+
		"','" + miApellido.get()+ 
		"','" + miDireccion.get()+
        "','" + textoComentario.get("1.0",END)+ "')")

    #datos=miNombre.get(),miPass.get(),miApellido.get(),miDireccion.get(), textoComentario.get("1.0",END)
    #micursor.execute("INSERT INTO DATOSUSUARIOS VALUES(NULL,?,?,?,?,?)",(datos))

	miconexion.commit()
	messagebox.showwarning("BBDD","Registro Insertado con éxito")     

def leer():
	miconexion=sqlite3.connect("Usuarios")
	micursor=miconexion.cursor()

	micursor.execute("SELECT * FROM DATOSUSUARIOS WHERE  ID=" + miID.get())
	elUsuario=micursor.fetchall()


	for usuario in elUsuario:
		miID.set(usuario[0])
		miNombre.set(usuario[1])
		miPass.set(usuario[2])
		miApellido.set(usuario[3])
		miDireccion.set(usuario[4])
		textoComentario.insert(1.0,usuario[5])


	miconexion.commit()


def Actualizar():
	miconexion=sqlite3.connect("Usuarios")
	micursor=miconexion.cursor()

	#datos=miNombre.get(),miPass.get(),miApellido.get(),miDireccion.get(), textoComentario.get("1.0",END)
	micursor.execute("UPDATE DATOSUSUARIOS SET NOMBRE_USUARIO='"+ miNombre.get()+ 
    	"', PASSWORD='" + miPass.get() + 
    	"', APELLIDO='" + miApellido.get() + 
    	"', DIRECCION='" + miDireccion.get() +
    	"', COMENTARIOS='" + textoComentario.get("1.0",END) +
    	"' WHERE ID=" + miID.get()) 
	 
	micursor.commit()
	messagebox.showinfo("BBDD","Registro azctualizado con exito")

	

def borrar():
	miconexion=sqlite3.connect("Usuarios")
	micursor=miconexion.cursor()

	micursor.execute("DELETE FROM DATOSUSUARIOS WHERE ID="+ miID.get())

	miconexion.commit()
	messagebox.showinfo("BBDD","Se ha borrado el registro con éxito")




root=Tk()

barraMenu=Menu(root)
root.config(menu=barraMenu,width=300,height=300)


bbddMenu=Menu(barraMenu,tearoff=0)
bbddMenu.add_command(label="Conectar",command=conexionBDD)
bbddMenu.add_command(label="Salir",command=salirApp)

borrarMenu=Menu(barraMenu,tearoff=0)
borrarMenu.add_command(label="Borrar Campos",command=borrarCampos)


crudMenu=Menu(barraMenu,tearoff=0)
crudMenu.add_command(label="Crear",command=Crear)
crudMenu.add_command(label="Leer",command=leer)
crudMenu.add_command(label="Actualizar",command=Actualizar)
crudMenu.add_command(label="Borrar",command=borrar)


AyudaMenu=Menu(barraMenu,tearoff=0)
AyudaMenu.add_command(label="Licencia")
AyudaMenu.add_command(label="Acerca de...")

barraMenu.add_cascade(label="BBDD", menu=bbddMenu)
barraMenu.add_cascade(label="Borrar", menu=borrarMenu)
barraMenu.add_cascade(label="CRUD", menu=crudMenu)
barraMenu.add_cascade(label="Ayuda", menu=AyudaMenu)

#----------------------------------comienzo de los campos----------------------------------

miFrame=Frame(root)

miFrame.pack()#empaquetamos el frame

miID=StringVar()
miNombre=StringVar()
miApellido=StringVar()
miPass=StringVar()
miDireccion=StringVar()


cuadroID=Entry(miFrame,textvariable=miID)
cuadroID.grid(row=0,column=1, padx=10,pady=10)


cuadroNombre=Entry(miFrame,textvariable=miNombre)
cuadroNombre.grid(row=1,column=1, padx=10,pady=10)
cuadroNombre.config(fg="red",justify="right")


cuadroPassword=Entry(miFrame,textvariable=miPass)
cuadroPassword.grid(row=2,column=1, padx=10,pady=10)
cuadroPassword.config(show="*")



cuadroApellido=Entry(miFrame,textvariable=miApellido)
cuadroApellido.grid(row=3,column=1, padx=10,pady=10)

cuadroDireccion=Entry(miFrame,textvariable=miDireccion)
cuadroDireccion.grid(row=4,column=1, padx=10,pady=10)

textoComentario=Text(miFrame,width=16,height=5)
textoComentario.grid(row=5,column=1, padx=10,pady=10)
scrollvert=Scrollbar(miFrame,command=textoComentario.yview)
scrollvert.grid(row=5,column=2,sticky="nsew")
textoComentario.config(yscrollcommand=scrollvert.set)


#.--------------------------------------aqui comienan las etiquetas-----------------------------------------------
idLabel=Label(miFrame,text="ID: ")
idLabel.grid(row=0,column=0,sticky="e",padx=10,pady=10)

NombreLabel=Label(miFrame,text="Nombre: ")
NombreLabel.grid(row=1,column=0,sticky="e",padx=10,pady=10)

PasswordLabel=Label(miFrame,text="Password: ")
PasswordLabel.grid(row=2,column=0,sticky="e",padx=10,pady=10)


ApellidoLabel=Label(miFrame,text="Apellido: ")
ApellidoLabel.grid(row=3,column=0,sticky="e",padx=10,pady=10)

DireccionLabel=Label(miFrame,text="Dirección: ")
DireccionLabel.grid(row=4,column=0,sticky="e",padx=10,pady=10)

ComentariosLabel=Label(miFrame,text="Comentarios: ")
ComentariosLabel.grid(row=5,column=0,sticky="e",padx=10,pady=10)



#----------------------Aqui van los botones-------------------------


miframe2=Frame()
miframe2.pack()

botonCrear=Button(miframe2,text="Crear",command=Crear)
botonCrear.grid(row=1,column=0,sticky="e",padx=10,pady=10)

botonLeer=Button(miframe2,text="Leer",command=leer)
botonLeer.grid(row=1,column=1,sticky="e",padx=10,pady=10)

botonActualizar=Button(miframe2,text="Actualizar",command=Actualizar)
botonActualizar.grid(row=1,column=2,sticky="e",padx=10,pady=10)

botonBorrar=Button(miframe2,text="Borrar",command=borrar)
botonBorrar.grid(row=1,column=3,sticky="e",padx=10,pady=10)




root.mainloop()