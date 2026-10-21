import pandas as pd

datos = {
    "producto": ["Cuaderno", "lapicera", "mochila", "Regla", "Cartuchera",
                 "Calculadora", "Auriculares", "Resaltadores", "Goma", "Lapiz"],
    "categoria": ["Libreria", "libreria", "Accesorios", "Libreria", "accesorios",
                  "Tecnologia", "tecnologia", "Libreria", "Indumentaria", "libreria"],
    "precio": [1500, 800, 12000, 600, 9500, 15000, 22000, 2500, 400, 300],
    "cantidad_vendida": [2, 24, 7, 25, 3, 12, 8, 20, 5, 30],
    "sucursal": ["Centro", "Centro", "Norte", "Sur", "Norte",
                 "Centro", "Sur", "Centro", "Sur", "Centro"],
    "forma_pago": ["Efectivo", "debito", "Credito", "Efectivo", "Debito",
                   "credito", "Credito", "Debito", "Efectivo", "debito"],
    "fecha": ["2024-03-01", "2024-03-01", "2024-03-02", "2024-03-02", "2024-03-03",
              "2024-03-03", "2024-03-04", "2024-03-04", "2024-03-05", "2024-03-05"],
}
df = pd.DataFrame(datos)


df["forma_pago"] = df["forma_pago"].str.strip().str.lower()

# Normalización de categoría (del Módulo 5)
reemplazos_categoria = {
    "libreria": "Libreria",
    "accesorios": "Accesorios",
    "tecnologia": "Tecnologia",
    "indumentaria": "Indumentaria",
}
df["categoria_limpia"] = (
    df["categoria"]
    .str.strip()
    .str.lower()
    .replace(reemplazos_categoria)
)


filtro = (
    (df["categoria_limpia"] == "Libreria")
    & (df["forma_pago"] == "debito")
    & (df["cantidad_vendida"] >= 20)
)

resultado_final = df[filtro][["producto", "precio", "sucursal"]]
print(resultado_final)


print(type(resultado_final))   
print(resultado_final.shape)   