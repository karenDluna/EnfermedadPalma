# -*- coding: utf-8 -*-
"""
Created on Sat Sep 17 10:41:01 2022

@author: KAREN
"""

import tkinter as tk
from tkinter import ttk
from tkinter import IntVar
from tkinter import StringVar
from tkinter import messagebox


root= tk.Tk()
root.title("Palma de aceite")
root.geometry("1200x1200")

# Variables CheckBox Hojas
hpudricionc = tk.IntVar()
hamarilloj = tk.IntVar()
hcolapsoj = tk.IntVar()
hquebrada = tk.IntVar()
hpequeña = tk.IntVar()
hlesionesn = tk.IntVar()
hausencian = tk.IntVar()
hmordiscos = tk.IntVar()
hdecoloracionc = tk.IntVar()
hdeshidratacion = tk.IntVar()
hfoliolosc = tk.IntVar()
hdecoloracionr = tk.IntVar()
hpalidez = tk.IntVar()
hdobladas = tk.IntVar()
hflechasa = tk.IntVar()
hflechasc = tk.IntVar()
hmanchasfoli = tk.IntVar()
hmanchashojasj = tk.IntVar()
hnecrosisf = tk.IntVar()
hmanchasmarron = tk.IntVar()
hmanchasblanco = tk.IntVar()
hmanchasaceitosas = tk.IntVar()
hpuntosnegros = tk.IntVar()
hrayasf = tk.IntVar()

# Variables CheckBox Tallo
tpudricionc = tk.IntVar()
thongos = tk.IntVar()
tanillo = tk.IntVar()
tdescomposicion = tk.IntVar()
tpecas = tk.IntVar()

# Variables CheckBox Raíces
rpardo = tk.IntVar()
rmicelio = tk.IntVar()
rmanchas = tk.IntVar()

# Variables CheckBox Inflorencias
iddesarrollo = tk.IntVar()
ipudricion = tk.IntVar()

# Variables CheckBox Frutos
fbrillo = tk.IntVar()
fpudricion = tk.IntVar()
fmanchas = tk.IntVar()


def analizar():
    
    if (hpudricionc.get()==1):

        if (hamarilloj.get()==1) | (hcolapsoj.get()==1) | (hquebrada.get()==1) | (hpequeña.get()==1) | (hlesionesn.get()==1) | (hausencian.get()==1) | (hmordiscos.get()==1) | (tpudricionc.get()==1) | (thongos.get()==1):
            labelcolor = tk.Label(root, bg= '#F9E79F', height = 1, width=15,).place(x=600, y=650)   
            win1= tk.Tk()
            win1.title("Enfermedad")
            win1.geometry("300x300")
            
            scroll = tk.Scrollbar(win1)  
            texto = tk.Text(win1, height = 50, width= 50)
            
            scroll.pack(side=tk.RIGHT, fill=tk.Y)
            texto.pack(side=tk.LEFT, fill=tk.Y)
            
            scroll.config(command=texto.yview)
            
            texto.config(yscrollcommand=scroll.set)
            
            mensaje= """PUDRICIÓN DEL COGOLLO 

    CONTROL 
    diagnóstico temprano, la remoción del tejido enfermo y la protección del tejido expuesto con insecticidas, fungicidas y bactericidas.
    Este procedimiento se complementa con un programa de aspersión para proteger las plantas vecinas, la eliminación de los estados avanzados de la enfermedad y la renovación temprana de lotes afectados.
    Este trabajo se complementa con el control de Rhynchophorus palmarum, el picudo de la palma.

     """
            
            texto.insert(tk.END, mensaje)


            
            win1.mainloop()
            win1.destroy
            
        elif (hrayasf.get()==1) | (tpecas.get()==1):
            labelcolor = tk.Label(root, bg= '#D35400', height = 1, width=15,).place(x=600, y=650)
            win1= tk.Tk()
            win1.title("Enfermedad")
            win1.geometry("300x300")
            
            scroll = tk.Scrollbar(win1)  
            texto = tk.Text(win1, height = 50, width= 50)
            
            scroll.pack(side=tk.RIGHT, fill=tk.Y)
            texto.pack(side=tk.LEFT, fill=tk.Y)
            
            scroll.config(command=texto.yview)
            
            texto.config(yscrollcommand=scroll.set)
            
            mensaje= """MOTEADO DEL COGOLLO 

    CONTROL 
    Utilización de cascarilla de arroz para cubrir las fundas 
    Eliminación de todas las malezas gramíneas, tanto en vivero como en campo 
    Las plantas infectadas se deben incinerar  
     
     """
            
            texto.insert(tk.END, mensaje)


            
            win1.mainloop()
            win1.destroy
            
    if (hpequeña.get()==1):
        if (hfoliolosc.get()==1) | (hdecoloracionr.get()==1) | (tanillo.get()==1):
            labelcolor = tk.Label(root, bg= '#85C1E9', height = 1, width=15,).place(x=600, y=650)

            win1= tk.Tk()
            win1.title("Enfermedad")
            win1.geometry("300x300")
            
            scroll = tk.Scrollbar(win1)  
            texto = tk.Text(win1, height = 50, width= 50)
            
            scroll.pack(side=tk.RIGHT, fill=tk.Y)
            texto.pack(side=tk.LEFT, fill=tk.Y)
            
            scroll.config(command=texto.yview)
            
            texto.config(yscrollcommand=scroll.set)
            
            mensaje= """EL ANILLO ROJO 

    CONTROL 
    El mejor método para el manejo de esta enfermedad ha sido la detección temprana y la eliminación de todas las palmas afectadas, así como la implementación de programas para el control del vector.
    Es necesario reducir las fuentes de inóculo de los nematodos y los sitios de reproducción del insecto, así como la implementación de trampas para su captura.
    monitorear las poblaciones del vector, con inspecciones frecuentes, el trampeo de adultos con el uso de trampas con feromonas de agregación y kariomonales. 
    Estas trampas no son suficientes para el control del insecto cuando las poblaciones son demasiado altas. Las poblaciones del insecto se incrementan cuando no se eliminan correctamente las palmas viejas o enfermas, 
    lo cual permite que se conviertan en sitios de reproducción de vectores y del nematodo.
     
     """
            
            texto.insert(tk.END, mensaje)


            
            win1.mainloop()
            win1.destroy
            
    if (hdecoloracionc.get()==1) & (hdeshidratacion.get()==1):
        
        labelcolor = tk.Label(root, bg= '#F970F9', height = 1, width=15,).place(x=600, y=650)
        
        if (fbrillo.get()==1) | (fpudricion.get()==1):
            
            labelcolor = tk.Label(root, bg= '#F970F9', height = 1, width=15,).place(x=600, y=6650)
            if (iddesarrollo.get()==0): 
                labelcolor = tk.Label(root, bg= '#F970F9', height = 1, width=15,).place(x=600, y=650)
                win1= tk.Tk()
                win1.title("Enfermedad")
                win1.geometry("300x300")
            
                scroll = tk.Scrollbar(win1)  
                texto = tk.Text(win1, height = 50, width= 50)
            
                scroll.pack(side=tk.RIGHT, fill=tk.Y)
                texto.pack(side=tk.LEFT, fill=tk.Y)
            
                scroll.config(command=texto.yview)
            
                texto.config(yscrollcommand=scroll.set)
            
                mensaje= """LA MARCHITEZ LETAL

        CONTROL 
        Como se ha mencionado antes, la enfermedad se está controlando con una detección temprana de los síntomas y la erradicación de las palmas enfermas. 
        En parcelas experimentales se ha demostrado la ventaja del control de gramíneas y de potenciales vectores como Myndus crudus
        """
            
                texto.insert(tk.END, mensaje)


            
                win1.mainloop()
                win1.destroy
                
            elif (iddesarrollo.get()==1):
                labelcolor = tk.Label(root, bg= '#58D68D', height = 1, width=15,).place(x=600, y=650)
                win1= tk.Tk()
                win1.title("Enfermedad")
                win1.geometry("300x300")
                
                scroll = tk.Scrollbar(win1)  
                texto = tk.Text(win1, height = 50, width= 50)
                
                scroll.pack(side=tk.RIGHT, fill=tk.Y)
                texto.pack(side=tk.LEFT, fill=tk.Y)
                
                scroll.config(command=texto.yview)
                
                texto.config(yscrollcommand=scroll.set)
                
                mensaje= """LA MARCHITEZ SORPRESIVA

        CONTROL 
        realizar campañas de identificación temprana de las palmas enfermas y se procede a su rápida erradicación, 
        complementada con el manejo adecuado de las gramíneas presentes en los lotes afectados y la aplicación de insecticidas en el área, 
        para reducir la población de los insectos que pueden estar involucrados en su diseminación.
         """
                
                texto.insert(tk.END, mensaje)
                
        
                
    elif (hdobladas.get()==1):
        if (hpalidez.get()==1) | (hflechasa.get()==1) | (hflechasc.get()==1) | (tdescomposicion.get()==1) | (rmicelio.get()==1) | (rpardo.get()==1) | (ipudricion.get()==1) | (fpudricion.get()==1):
            labelcolor = tk.Label(root, bg= '#E74C3C', height = 1, width=15,).place(x=600, y=650)
            win1= tk.Tk()
            win1.title("Enfermedad")
            win1.geometry("300x300")
            
            scroll = tk.Scrollbar(win1)  
            texto = tk.Text(win1, height = 50, width= 50)
            
            scroll.pack(side=tk.RIGHT, fill=tk.Y)
            texto.pack(side=tk.LEFT, fill=tk.Y)
            
            scroll.config(command=texto.yview)
            
            texto.config(yscrollcommand=scroll.set)
            
            mensaje= """PUDRICION BASAL  

    CONTROL 
    Destrucción y quema de las palmas que presenten los síntomas de la enfermedad y un mes antes de la siembra desinfectar el suelo con cal viva 

     """
            
            texto.insert(tk.END, mensaje)


            
            win1.mainloop()
            win1.destroy
            
        elif (hmanchashojasj.get()==1) | (hmanchasfoli.get()==1) | (hnecrosisf.get()==1):
            labelcolor = tk.Label(root, bg= '#1B4F72', height = 1, width=15,).place(x=600, y=650)

            win1= tk.Tk()
            win1.title("Enfermedad")
            win1.geometry("300x300")
            
            scroll = tk.Scrollbar(win1)  
            texto = tk.Text(win1, height = 50, width= 50)
            
            scroll.pack(side=tk.RIGHT, fill=tk.Y)
            texto.pack(side=tk.LEFT, fill=tk.Y)
            
            scroll.config(command=texto.yview)
            
            texto.config(yscrollcommand=scroll.set)
            
            mensaje= """ARCO DEFOLIADO   

    CONTROL 
    Eliminación de los tejidos afectados en asocio con una fertilización adecuada que ayuda a la recuperación de la planta como medida 
    complementaria aplicar a todo el cogollo carboxin + captan y befuracarb. La palma generalmente se recupera después de unos meses sin que sea necesaria ninguna intervención.

     """
            
            texto.insert(tk.END, mensaje)


            
            win1.mainloop()
            win1.destroy
            
    elif (hnecrosisf.get()==1):
        if  (hmanchasmarron.get()==1) | (hmanchasblanco.get()==1) | (hmanchasaceitosas.get()==1) | (hpuntosnegros.get()==1):
            labelcolor = tk.Label(root, bg= '#7D3C98', height = 1, width=15,).place(x=600, y=650)

            win1= tk.Tk()
            win1.title("Enfermedad")
            win1.geometry("300x300")
        
            scroll = tk.Scrollbar(win1)  
            texto = tk.Text(win1, height = 50, width= 50)
        
            scroll.pack(side=tk.RIGHT, fill=tk.Y)
            texto.pack(side=tk.LEFT, fill=tk.Y)
        
            scroll.config(command=texto.yview)
        
            texto.config(yscrollcommand=scroll.set)
            
            mensaje= """PESTALOTIOPSIS 

    CONTROL 
    Se puede combatir con aspersiones simultáneas de fungicida. 
    Obtener un desarrollo vigoroso de las plantas mediante espaciamiento adecuado entre ellas no menos de 80 cm. Fertilización y suministro adecuado de agua 
    """
        
            texto.insert(tk.END, mensaje)


        
            win1.mainloop()
            win1.destroy
            
    elif (rmanchas.get()==1) | (fmanchas.get()==1):
            
         labelcolor = tk.Label(root, bg= '#145A32', height = 1, width=15,).place(x=600, y=650)
         win1= tk.Tk()
         win1.title("Enfermedad")
         win1.geometry("300x300")
         
         scroll = tk.Scrollbar(win1)  
         texto = tk.Text(win1, height = 50, width= 50)
         
         scroll.pack(side=tk.RIGHT, fill=tk.Y)
         texto.pack(side=tk.LEFT, fill=tk.Y)
         
         scroll.config(command=texto.yview)
         
         texto.config(yscrollcommand=scroll.set)
         
         mensaje= """GERMEN PARDO 

 CONTROL 
 Se puede combatir con aspersiones simultáneas de fungicida. 
 Obtener un desarrollo vigoroso de las plantas mediante espaciamiento adecuado entre ellas no menos de 80 cm. Fertilización y suministro adecuado de agua 
  """
         
         texto.insert(tk.END, mensaje)


         
         win1.mainloop()
         win1.destroy
         
         
    #elif (hpudricionc.get()==1) & (hamarilloj.get()==1) & (hcolapsoj.get()==1) & (hquebrada.get()==1) & (hpequeña.get()==1) & (hlesionesn.get()==1) & (hausencian.get()==1) & (hmordiscos.get()==1) & (hdecoloracionc.get()==1)& (hdeshidratacion.get()==1) & (hfoliolosc.get()==1) & (hdecoloracionc.get()==1):
    #    messagebox.showerror("error", "try again")
            
    #elif (hpalidez.get()==1) & (hdobladas.get()==1) & (hflechasa.get()==1) & (hflechasc.get()==1) & (hmanchasfoli.get()==1) & (hmanchashojasj.get()==1) & (hnecrosisf.get()==1) & (hmanchasmarron.get()==1) & (hmanchasblanco.get()==1) & (hmanchasaceitosas.get()==1) & (hpuntosnegros.get()==1) & (hrayasf.get()==1) & (tpudricionc.get()==1) & (thongos.get()==1) & (tanillo.get()==1) & (tdescomposicion.get()==1) & (tpecas.get()==1) & (rpardo.get()==1) & (rmicelio.get()==1) & (rmanchas.get()==1) & (iddesarrollo.get()==1) & (ipudricion.get()==1) & (fbrillo.get()==1) & (fpudricion.get()==1) & (fmanchas.get()==1):
    #    messagebox.showerror("error", "try again")
            
            
            
        
            
        
        




#----------------------------------------------------------------------------------------------------------------------------------------------------------
 

label = tk.Label(root,text = 'HOJAS', 
                 bg= '#20b4d8',
                 fg ='#2088d8', 
                 height = 1, width=15, font=("Serif",16)).place(x=10, y=10)

HpudricionC = tk.Checkbutton(root,text = 'Podrida ',variable=hpudricionc,onvalue=1, offvalue=0).place(x=10, y=50)
HamarilloJ = tk.Checkbutton(root,text = 'Amarillamiento de las hojas más jóvenes',variable=hamarilloj,onvalue=1, offvalue=0).place(x=10, y=75)
HcolapsoJ = tk.Checkbutton(root,text = 'Colapso hojas jóvenes',variable=hcolapsoj,onvalue=1, offvalue=0).place(x=10, y=100)
Hquebrada = tk.Checkbutton(root,text = ' Quebrada',variable=hquebrada,onvalue=1, offvalue=0).place(x=10, y=125)
Hpequeña = tk.Checkbutton(root,text = ' Pequeña ',variable=hpequeña,onvalue=1, offvalue=0).place(x=10, y=150)
HlesionesN = tk.Checkbutton(root,text = 'Lesiones necróticas las flechas más jóvenes ',variable=hlesionesn,onvalue=1, offvalue=0).place(x=10, y=175)
HausenciaN = tk.Checkbutton(root,text = 'Ausencia de hojas nuevas ',variable=hausencian,onvalue=1, offvalue=0).place(x=10, y=200)
Hmordiscos = tk.Checkbutton(root,text = 'Mordiscos sin ser insectos ',variable=hmordiscos,onvalue=1, offvalue=0).place(x=10, y=225)
HdecoloracionC = tk.Checkbutton(root,text = 'Decoloración café de los foliolos ',variable=hdecoloracionc,onvalue=1, offvalue=0).place(x=10, y=250)
Hdeshidratacion = tk.Checkbutton(root,text = 'Deshidratación de los foliolos ',variable=hdeshidratacion,onvalue=1, offvalue=0).place(x=10, y=275)
HfoliolosC = tk.Checkbutton(root,text = 'Foliolos cortos  ',variable=hfoliolosc,onvalue=1, offvalue=0).place(x=10, y=300)
HdecoloracionR = tk.Checkbutton(root,text = 'Decoloración interna de raquis ',variable=hdecoloracionr,onvalue=1, offvalue=0).place(x=10, y=325)
Hpalidez = tk.Checkbutton(root,text = 'Palida',variable=hpalidez,onvalue=1, offvalue=0).place(x=10, y=350)
Hdobladas = tk.Checkbutton(root,text = 'Doblada',variable=hdobladas,onvalue=1, offvalue=0).place(x=10, y=375)
HflechasA = tk.Checkbutton(root,text = 'Flechas no abren  ',variable=hflechasa,onvalue=1, offvalue=0).place(x=10, y=400)
HflechasC = tk.Checkbutton(root,text = 'Flechas cortas ',variable=hflechasc,onvalue=1, offvalue=0).place(x=10, y=425)
HmanchasFoli = tk.Checkbutton(root,text = 'Manchas marrones o pardas rojizas entre los foliolos ',variable=hmanchasfoli,onvalue=1, offvalue=0).place(x=10, y=450)
HmanchashojasJ = tk.Checkbutton(root,text = 'Manchas marrones o pardas rojizas en las hojas jóvenes  ',variable=hmanchashojasj,onvalue=1, offvalue=0).place(x=10, y=475)
HnecrosisF = tk.Checkbutton(root,text = 'Necrosis de los foliolos  ',variable=hnecrosisf,onvalue=1, offvalue=0).place(x=10, y=500)
HmanchasMarron = tk.Checkbutton(root,text = 'Manchas irregulares marrón purpura ',variable=hmanchasmarron,onvalue=1, offvalue=0).place(x=10, y=525)

HmanchasBlanco = tk.Checkbutton(root,text = 'Manchas marrón claro o blanco grisáceo  ',variable=hmanchasblanco,onvalue=1, offvalue=0).place(x=10, y=550)
HmanchasAceitosas = tk.Checkbutton(root,text = 'Manchas aceitosas',variable=hmanchasaceitosas,onvalue=1, offvalue=0).place(x=10, y=575)
HpuntosNegros = tk.Checkbutton(root,text = 'Puntos negros ',variable=hpuntosnegros,onvalue=1, offvalue=0).place(x=10, y=600)
HrayasF = tk.Checkbutton(root,text = 'Rayas cloróticas a lo largo del foliolo ',variable=hrayasf,onvalue=1, offvalue=0).place(x=10, y=625)

#----------------------------------------------------------------------------------------------------------------------------------------------------------

label_n2 = tk.Label(root,text = 'TALLO', 
                 bg= '#20b4d8',
                 fg ='#2088d8', 
                 height = 1, width=15, font=("Serif",16)).place(x=600, y=10)

TpudricionC = tk.Checkbutton(root,text = 'Pudrición de los tejidos del cogollo',variable=tpudricionc,onvalue=1, offvalue=0).place(x=600, y=50)
Thongos = tk.Checkbutton(root,text = 'Hongo',variable=thongos,onvalue=1, offvalue=0).place(x=600, y=75)
Tanillo = tk.Checkbutton(root,text = 'Anillo color café al cortar el tronco',variable=tanillo,onvalue=1, offvalue=0).place(x=600, y=100)
Tdescomposicion = tk.Checkbutton(root,text = 'Descomposición interna del estipite',variable=tdescomposicion,onvalue=1, offvalue=0).place(x=600, y=125)
Tpecas = tk.Checkbutton(root,text = 'Pecas o rayas color verde claro o clorótico',variable=tpecas,onvalue=1, offvalue=0).place(x=600, y=150)

#----------------------------------------------------------------------------------------------------------------------------------------------------------

label_n3 = tk.Label(root,text = 'RAÍCES', 
                 bg= '#20b4d8',
                 fg ='#2088d8', 
                 height = 1, width=15, font=("Serif",16)).place(x=600, y=225)

Rpardo = tk.Checkbutton(root,text = 'Coloración parda con porciones negras  ',variable=rpardo,onvalue=1, offvalue=0).place(x=600, y=275)
Rmicelio = tk.Checkbutton(root,text = 'Con micelio (hongo)',variable=rmicelio,onvalue=1, offvalue=0).place(x=600, y=300)
Rmanchas = tk.Checkbutton(root,text = 'Manchas hundidas de color pardo oscuro en la radícula',variable=rmanchas,onvalue=1, offvalue=0).place(x=600, y=325)

#----------------------------------------------------------------------------------------------------------------------------------------------------------

label_n4 = tk.Label(root,text = 'INFLORESCENCIAS', 
                 bg= '#20b4d8',
                 fg ='#2088d8', 
                 height = 1, width=20, font=("Serif",16)).place(x=10, y=800)

IdDesarrollo = tk.Checkbutton(root,text = 'Detención del desarrollo ',variable=iddesarrollo,onvalue=1, offvalue=0).place(x=10, y=850)
Ipudricion = tk.Checkbutton(root,text = 'Pudrición ',variable=ipudricion,onvalue=1, offvalue=0).place(x=10, y=875)

#----------------------------------------------------------------------------------------------------------------------------------------------------------

label_n5 = tk.Label(root,text = 'FRUTOS', 
                 bg= '#20b4d8',
                 fg ='#2088d8', 
                 height = 1, width=15, font=("Serif",16)).place(x=600, y=400)

Fbrillo = tk.Checkbutton(root,text = 'Sin brillo ',variable=fbrillo,onvalue=1, offvalue=0).place(x=600, y=450)
Fpudricion = tk.Checkbutton(root,text = 'Pudrición ',variable=fpudricion,onvalue=1, offvalue=0).place(x=600, y=475)
Fmanchas = tk.Checkbutton(root,text = 'Manchas hundidas de color pardo oscuro ',variable=fmanchas,onvalue=1, offvalue=0).place(x=600, y=500)

#----------------------------------------------------------------------------------------------------------------------------------------------------------


Button = tk.Button(root,text = 'Analizar',height = 2, width=20, font=("Serif",12), bg= '#20dbd3', fg ='#d8efd4', command=analizar).place(x=600, y=700)

root.mainloop()
root.destroy