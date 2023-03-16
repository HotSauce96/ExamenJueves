#Ejercicio de cuentas de banco

cuentasdeBanco =[]

contador = 1

vueltas = int(input("Ingrese num vueltas: "))

for i in range (0, vueltas):
    cuentaBancaria = {}
    cuentaBancaria["numeroCuenta"] = contador
    contador +=1
    cuentaBancaria["saldo"] = int(input("Ingrese por favor un saldo: "))
    cuentasdeBanco.append(cuentaBancaria)
listaCuentas = sorted(cuentasdeBanco, key=lambda x: x["saldo"], reverse=True)
print(f"Los saldos de las cuentas bancarias de mayor a menor son: {listaCuentas}")
