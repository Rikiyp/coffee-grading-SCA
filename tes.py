print("=== KALKULATOR SEDERHANA ===")

while True:
    try:
        angka1 = float(input("\nMasukkan angka pertama: "))
        operator = input("Masukkan operator (+, -, *, /): ")
        angka2 = float(input("Masukkan angka kedua: "))

        if operator == "+":
            hasil = angka1 + angka2
        elif operator == "-":
            hasil = angka1 - angka2
        elif operator == "*":
            hasil = angka1 * angka2
        elif operator == "/":
            if angka2 == 0:
                print("Error: tidak dapat membagi dengan nol.")
                continue
            hasil = angka1 / angka2
        else:
            print("Operator tidak valid.")
            continue

        print(f"Hasil: {hasil}")

        ulangi = input("\nHitung lagi? (y/n): ").lower()
        if ulangi != "y":
            print("Program selesai.")
            break

    except ValueError:
        print("Input tidak valid. Masukkan angka dengan benar.")