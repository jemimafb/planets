def fahr_to_kelvin(temp):
    return ((temp - 32) * (5/9)) + 273.15

print('freezing point of water:', fahr_to_kelvin(32))
print('freezing point of water:', fahr_to_kelvin(212))

def kelvin_to_celcius(temp_k):
    return temp_k - 273.15

print('absolute zero in Celcius', kelvin_to_celcius(0.0))

def fahr_to_celcius(temp_f):
    temp_k = fahr_to_kelvin(temp_f)
    result = kelvin_to_celcius(temp_k)
    return(result)

print('freexing point of water in celcius:', fahr_to_celcius(32))

