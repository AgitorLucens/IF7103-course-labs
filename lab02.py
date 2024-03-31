import pandas as pd
from tkinter import filedialog
import tkinter as tk
from tkinter import ttk

resultados = {}
#Reglas que usaremos en el motor de inferencia
reglas = [
    {
        "nombre": "Antracnosis",
        "sintomas_presentes": ["Manchas oscuras en frutos","Manchas oscuras en hojas", "Pudrición"],
        "sintomas_ausentes": ["Polvo blanco y gris en hojas"],
        "diagnostico": "La planta sufre de Antracnosis.",
        "explicacion": "Detectadas manchas oscuras sin presencia de polvo blanco."
    },
    {
        "nombre": "Sigatoka Negra (en banano)",
        "sintomas_presentes": ["Manchas negras alargadas", "Reduccion area foliar"],
        "sintomas_ausentes": [],
        "diagnostico": "La planta sufre de Sigatoka Negra (en banano).",
        "explicacion": "Presencia de manchas negras alargadas en hojas y reducción del área foliar."
    },
    {
        "nombre": "Pudrición del Cogollo (en palma aceitera)",
        "sintomas_presentes": ["Marchitez", "Necrosis del cogollo", "Hojas jovenes no abren"],
        "sintomas_ausentes": [],
        "diagnostico": "La planta sufre de Pudrición del Cogollo (en palma aceitera).",
        "explicacion": "Presencia de marchitez y necrosis del cogollo, hojas jóvenes que no se abren."
    },
    {
        "nombre": "Roya del Café",
        "sintomas_presentes": ["Pústulas naranjas", "defoliacion"],
        "sintomas_ausentes": [],
        "diagnostico": "La planta sufre de Roya del Café.",
        "explicacion": "Presencia de pústulas de color naranja en la parte inferior de las hojas y defoliación."
    },
    {
        "nombre": "Mancha de Asfalto (en cítricos)",
        "sintomas_presentes": ["Manchas negras circulares", "Caída prematura de hojas","Caída prematura de frutos"],
        "sintomas_ausentes": [],
        "diagnostico": "La planta sufre de Mancha de Asfalto (en cítricos).",
        "explicacion": "Presencia de manchas negras circulares en frutos y hojas, caída prematura de frutos."
    },
    {
        "nombre": "Marchitez por Fusarium (en tomates)",
        "sintomas_presentes": ["Marchitez", "decoloracion_tallos_raices", "Pérdida de vigor"],
        "sintomas_ausentes": [],
        "diagnostico": "La planta sufre de Marchitez por Fusarium (en tomates).",
        "explicacion": "Presencia de marchitez, decoloración de tallos y raíces, pérdida de vigor."
    },
    {
        "nombre": "Podredumbre Negra (en piña)",
        "sintomas_presentes": ["Manchas oscuras en frutos", "Pudrición acuosa"],
        "sintomas_ausentes": [],
        "diagnostico": "La planta sufre de Podredumbre Negra (en piña).",
        "explicacion": "Presencia de manchas oscuras en la base del fruto y pudrición acuosa."
    },
    {
        "nombre": "Mancha Angular (en frijoles)",
        "sintomas_presentes": ["Manchas amarillas/marrones en hojas", "Lesiones"],
        "sintomas_ausentes": [],
        "diagnostico": "La planta sufre de Mancha Angular (en frijoles).",
        "explicacion": "Presencia de manchas amarillas o marrones en hojas y formación de lesiones."
    },
    {
        "nombre": "Oídio",
        "sintomas_presentes": ["Polvo blanco y gris en hojas", "Tallos deformes"],
        "sintomas_ausentes": [],
        "diagnostico": "La planta sufre de Oídio.",
        "explicacion": "Presencia de polvo blanco o gris en las hojas y tallos deformes."
    },
    {
        "nombre": "Mancha Negra",
        "sintomas_presentes": ["Manchas negras en hojas", "Caída prematura de hojas"],
        "sintomas_ausentes": [],
        "diagnostico": "La planta sufre de Mancha Negra.",
        "explicacion": "Presencia de manchas negras en las hojas y caída prematura de las hojas."
    },
    {
        "nombre": "Virosis (Virus del Mosaico)",
        "sintomas_presentes": ["Mosaico en las hojas", "Deformacion"],
        "sintomas_ausentes": [],
        "diagnostico": "La planta sufre de Virosis (Virus del Mosaico).",
        "explicacion": "Presencia de patrones de mosaico en las hojas y deformación de hojas y frutos."
    },
    {
        "nombre": "Fusariosis (Fusarium)",
        "sintomas_presentes": ["Marchitez", "Decoloracion de tallo y raiz"],
        "sintomas_ausentes": [],
        "diagnostico": "La planta sufre de Fusariosis (Fusarium).",
        "explicacion": "Presencia de marchitez y decoloración de tallos y raíces."
    }
]
def evaluar_reglas(sintomas, reglas):
    diagnosticos = []
    explicaciones = []
    for regla in reglas:
        if all(s in sintomas for s in regla["sintomas_presentes"]) and \
        not any(s in sintomas for s in regla["sintomas_ausentes"]):
            diagnosticos.append(regla["diagnostico"])
            explicaciones.append(regla["explicacion"])
    return diagnosticos, explicaciones

# Especifica la ruta del archivo Excel
def cargar_datos_excel():
    filename = filedialog.askopenfilename(title="Seleccionar archivo Excel", filetypes=(("Archivos Excel", "*.xlsx"),("Todos los archivos", "*.*")))
    # Verificar si se seleccionó un archivo
    if filename:
        # Cargar datos desde el archivo Excel
        df = pd.read_excel(filename)

        # Obtener síntomas y valores de las plantas desde el DataFrame
        sintomas = df.columns.tolist()
        valores = df.values.tolist()
        for i, planta in enumerate(valores):
            sintomas_planta = [sintoma for j, sintoma in enumerate(sintomas) if planta[j]]
            print(f"Síntomas de la Planta {i+1}: {sintomas_planta}")
        # Evaluar las reglas de diagnóstico para cada planta
        
        for i, planta in enumerate(valores):
            sintomas_planta = [sintoma for j, sintoma in enumerate(sintomas) if planta[j]]
            diagnosticos = evaluar_reglas(sintomas_planta, reglas)
            resultados[f"Planta {i+1}"] = diagnosticos
           
# Mostrar los diagnósticos en la GUI        
cargar_datos_excel()
# Función para crear la tabla
def crear_tabla(root, datos):
    tabla = ttk.Treeview(root)
    tabla["columns"] = ("Nombre de Planta", "Enfermedad", "Descripción")
    tabla.heading("#0", text="Índice")
    tabla.heading("Nombre de Planta", text="Nombre de Planta")
    tabla.heading("Enfermedad", text="Enfermedad")
    tabla.heading("Descripción", text="Descripción")
    
    # Agregar datos a la tabla
    for i, (planta, (enfermedad, descripcion)) in enumerate(datos.items()):
        if enfermedad:
            enfermedad_str = ", ".join(enfermedad)
            descripcion_str = ", ".join(descripcion)
        else:
            enfermedad_str = "No tiene enfermedad"
            descripcion_str = "N/A"
        tabla.insert("", "end", text=str(i+1), values=(planta, enfermedad_str, descripcion_str))
    
    tabla.pack(expand=True, fill="both")

# Crear ventana
root = tk.Tk()
root.title("Tabla de Diagnóstico de Enfermedades en Plantas")

# Crear y mostrar tabla
crear_tabla(root, resultados)

root.mainloop()