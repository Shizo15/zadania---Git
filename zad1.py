#zad1
def is_criticality_balanced(temperature, neutron_emission):

    if temperature <800:
        print("Temperatura jest ok")
    else:
        print("Temperatura jest za duża")

    if neutron_emission >500:
        print("Liczba emitowanych neutronów jest ok")
    else:
        print("Liczba emitowanych neutronów jest za mała")

    if (temperature*neutron_emission)<500000:
        print("Iloczyn temperatury i ilości eimtowanych neutronów jest ok")
    else:
        print("Iloczyn temperatury i ilości emitowanych neutronów jest za duży!")

    return temperature<800 and neutron_emission>500 and (temperature*neutron_emission)<500000

print("Podaj temperaturę w Kelvinach i liczbę emitowanych neutronów: ")
temperature = float(input("Temperatura: "))
neutron_emission = float(input("Podaj liczbę emitowanych neutronów: "))

if is_criticality_balanced(temperature, neutron_emission):
    print(True)
else:
    print(False)

