#vlan normales  entre 1 y 1005
#vlan extendida  entre 1006 y 4094
#> y <
print ("VERIFICADOR DE VLANS")
print (".")
print ("ingrese la vlan que desee verificar")
vlan = int(input("#####:"))

if vlan  <= 1005:
    print ("La vlan: ",vlan,"es de rango normal")


elif vlan <= 4094:
    print ("La vlan: ",vlan,"es de rango extendida")

else:
    print("Error opcion invalida")
    print("o vlan incorrecta")