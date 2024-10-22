#zad2

def reactor_efficiency(voltage, current, theoretical_max_power):

    generated_power = voltage * current
    efficiency = (generated_power / theoretical_max_power)*100

    if efficiency >= 80:
        return "Zielony"
    elif efficiency <80 and efficiency >= 60:
        return "Pomarańczowy"
    elif efficiency <60 and efficiency >= 30:
        return "Czerwony"
    elif efficiency <30:
        return "Czarny"
    else:
        return "Nieprawidłowa wartość"

    return efficiency


print( "Sprawdzanie wydajności reaktora")

voltage = float(input("Podaj napięcie (V): "))
current = float(input("Podaj natężenie (A): "))

theoretical_max_power = float(input("Podaj teoretyczną moc maksymalną (W): "))
efficiency_value = reactor_efficiency(voltage, current, theoretical_max_power)

print(f"Sprawnośc reaktora mieści się w paśmie: {efficiency_value}")