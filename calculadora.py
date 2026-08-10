"""
Crea un programa que calcule el precio final de una compra en un negocio local.

"""

productos = {
    "Jugo Especial":0,
    "Jugo de Arandano":0,
    "Jugo de Papaya":0,
    "Jugo de Fresa":0,
    "Jugo de Mango":0,
    "Jugo de Piña":0,
}

print("-------BIENVENIDO A  LA JUGUERIA DELI--------")

cantidad_1,cantidad_2,cantidad_3,cantidad_4,cantidad_5,cantidad_6 = 0,0,0,0,0,0
costo_1,costo_2,costo_3,costo_4,costo_5,costo_6 = 0,0,0,0,0,0

while True:
    print("             MENÚ\n" 
"      1.Jugo Especial  -> $4.5 dolares\n"
"      2.Jugo de Arandano  -> $3.5 dolares\n"
"      3.Jugo de Papaya  -> $2.5 dolares\n"
"      4.Jugo de Fresa  -> $5 dolares\n"
"      5.Jugo de Mango  -> $3 dolares\n"
"      6.jugo de Piña  -> $3 dolares\n"
"      7.Orden finalizada.      ")

    print("\nPor compras mayores a $50 dolares obtiene un descuento del 20%.\n")

    option = int(input("Que opcion elige: "))
    match option:
        case 1:
            cantidad_1 += float(input("Cantidad: "))
            costo_1 = 4.5*cantidad_1
            productos["Jugo Especial"] = costo_1
            valor_especial = productos["Jugo Especial"]
        case 2:
            cantidad_2 += float(input("Cantidad: "))
            costo_2 = 3.5*cantidad_2
            productos["Jugo de Arandano"] = costo_2
            valor_arandano = productos["Jugo de Arandano"]

        case 3:
            cantidad_3 += float(input("Cantidad: "))
            costo_3 = 2.5*cantidad_3
            productos["Jugo de Papaya"] = costo_3
            valor_papaya = productos["Jugo de Papaya"]
        case 4:
            cantidad_4 += float(input("Cantidad: "))
            costo_4 = 5 * cantidad_4
            productos["Jugo de Fresa"] = costo_4
            valor_fresa = productos["Jugo de Fresa"]

        case 5:
            cantidad_5 += float(input("Cantidad: "))
            costo_5 = 3 * cantidad_5
            productos["Jugo de Mango"] = costo_5
            valor_mango = productos["Jugo de Mango"]

        case 6: 
            cantidad_6 += float(input("Cantidad: "))
            costo_6 = 3 * cantidad_6
            productos["Jugo de Piña"] = costo_6
            valor_piña = productos["Jugo de Piña"]
            
        case 7:
            print("Orden finalizada.")
            break

        case _:
            print("Ingrese una opcion valida.")
            

Precio_final = (productos['Jugo Especial']+productos['Jugo de Arandano']+productos['Jugo de Fresa']+productos['Jugo de Mango']+productos['Jugo de Papaya']+productos['Jugo de Piña'])                 

if(Precio_final>50):
    Precio_final = Precio_final - 0.2*(Precio_final)

print("--------IMPRIMIENDO BOLETA---------")
print(f"""
        Producto            Precio          Cantidad     Precio_F
        Jugo Especial       $4.5    dolares        {cantidad_1}            ${productos["Jugo Especial"]}
        Jugo de Arandano    $3.5    dolares        {cantidad_2}            ${productos["Jugo de Arandano"]}
        Jugo de Papaya      $2.5    dolares        {cantidad_3}            ${productos["Jugo de Papaya"]}
        Jugo de Fresa       $5      dolares        {cantidad_4}            ${productos["Jugo de Fresa"]}
        Jugo de Mango       $3      dolares        {cantidad_5}            ${productos["Jugo de Mango"]}
        Jugo de Piña        $3      dolares        {cantidad_6}            ${productos["Jugo de Piña"]}
        -------------------------------------------Precio Final : ${Precio_final}
""")