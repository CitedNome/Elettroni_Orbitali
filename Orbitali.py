
print("Elettroni per Orbitale\nCode by Cited ~ https://github.com/CitedNome")

while True:
    e = 0
    def get_n():
        print("\n=================================================================")
        n = input("Inserisci il numero dell'orbitale o premi \"q\" per uscire: ")
        if n == "q":
            quit()
        n = int(n)
        if n < 0:
            print("n deve essere un numero positivo, bestia!")
            quit()
        else:
            return n

    n = get_n()

    for l in range(0, n):
        for m in range(-l, l+1):
            #print(f"[{e+1}] ({n};{l};{m};0.5)")
            #print(f"[{e+2}] ({n};{l};{m};-0.5)")
            eo = f"[{e+1}]"
            et = f"[{e+2}]"
            print(f"{eo : <5} ({n};{l};{m};0.5)")
            print(f"{et : <5} ({n};{l};{m};-0.5)")
            e += 2

    print(f"\nCi sono {e} elettroni nell'orbitale numero {n}")