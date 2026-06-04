def main():
    LIGHT_SPEED = int(300000000) # "c" is representing the speed of light.
    mass = int(input('m: ')) # "m" is representing mass.
    energy = int(mass * pow(LIGHT_SPEED, 2)) # "E" is representing energy.
    print(f'E: {energy}')

main()
