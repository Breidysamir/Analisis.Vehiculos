import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

datos = pd.read_excel("/Users/aquin/OneDrive/Documentos/Python.com/Vehiculos1.xlsx") 

fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(11,6), facecolor = "skyblue")

# Grafico Lineal
datos.plot(x="Año", y="Kilometraje (km)", marker="o", linestyle="--", color="green", ax=ax2)
ax2.set_title("Gráfico Lineal de Kilometraje de Vehiculos", color="red")
ax2.set_xlabel("Año", color="red")
ax2.set_ylabel("Kilometraje del Vehículo", color="red")
ax2.legend(['Kilometraje'], loc='best')
ax2.grid(True)

# Grafico Pastel
datos_pie = datos.groupby("Marca")['Ventas'].sum()
datos_pie.plot.pie(autopct='%1.1f%%', shadow=True, textprops={"color":"blue","size":"smaller"}, ax=ax3)
ax3.set_title("Porcentaje de Vehículos más Vendidos", color="red")
ax3.legend(datos_pie.index, loc="best", bbox_to_anchor=(0, 0, 0, 0))
ax3.set_ylabel("")

# Grafico de Barras
datos.plot.bar(x = "Marca", y="Precio ($)", edgecolor="black", ax=ax1)
ax1.set_title("Ventas de Vehiculos (Breidy-Car)", color="red")
ax1.set_xlabel("Marcas de Vehiculos", color="red")
ax1.set_ylabel("Precio de Vehiculos", color="red")
ax1.legend(["Precio"], loc="best")
plt.grid(True)

ax1.set_xticklabels(ax1.get_xticklabels(), rotation=60, color="blue")
ax2.set_xticklabels(ax2.get_xticklabels(), rotation=0, color="blue")

ax1.set_yticklabels(ax1.get_yticklabels(), rotation=0, color="blue")
ax2.set_yticklabels(ax2.get_yticklabels(), rotation=0, color="blue")

plt.suptitle("Análisis de Vehículos Breidy Auto World :)", fontsize=16, color="blue")
plt.tight_layout()
plt.show()