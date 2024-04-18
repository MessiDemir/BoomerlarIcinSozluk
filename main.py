def add_word(dictionary):
    new_word = input("Eklemek istediğiniz kelimeyi yazın (hepsini büyük harflerle yazın!): ")
    new_definition = input("Bu kelimenin açıklamasını yazın: ")
    dictionary[new_word] = new_definition
    print(new_word + " kelimesi başarıyla eklendi.")

def lookup_word(dictionary):
    word = input("Anlamadığınız bir kelime yazın (hepsini büyük harflerle yazın!): ")
    if word in dictionary:
        print(word + ": " + dictionary[word])
    else:
        print("Bu kelimeyi tanımıyorum.")

def main():
    meme_dict = {
        "CRINGE": "Garip ya da utandırıcı bir şey",
        "LOL": "Komik bir şeye verilen cevap",
        "TBT": "Throwback Thursday'in kısaltması, geçmişteki anıları hatırlatan bir paylaşım",
        "FTW": "For The Win'in kısaltması, bir şeyin en iyisi olduğunu ifade eder",
        "BRB": "Be Right Back'in kısaltması, hemen geri döneceğini belirtir",
    }

    while True:
        print("\n[1] Kelime Ekle")
        print("[2] Kelime Ara")
        print("[3] Çıkış")

        choice = input("Yapmak istediğiniz işlemi seçin: ")

        if choice == "1":
            add_word(meme_dict)
        elif choice == "2":
            lookup_word(meme_dict)
        elif choice == "3":
            print("Programdan çıkılıyor...")
            break
        else:
            print("Geçersiz bir seçim yaptınız. Lütfen tekrar deneyin.")

if __name__ == "__main__":
    main()
