#zad3

def fail_safe(temperature, neutrons_per_second, threshold):
    product = temperature * neutrons_per_second

    lower = threshold * neutrons_per_second*0.9
    upper = threshold * neutrons_per_second*1.1

    if product < lower:
        return "LOW"
    elif product >= lower and product <= upper:
        return "NORMAL"
    else:
        return "HIGH"

print("Sprawdzianie progu krytyczności")

temperature = float(input("Podaj temperaturę w Kelwinach: "))
neutrons_per_second = float(input("Podaj przepływ neutronów na sekundę: "))
threshold = float(input("Podaj wartość progową: "))
print(fail_safe(temperature, neutrons_per_second, threshold))