def main():
    import random

    print("--Welcome to the word guessing game--")

    easy_words = ["bird","acid","have","hair","hide","hear","iron","jump","kick","kill","life","like","love"]
    medium_words = ["apple", "brave", "charm", "dream", "eagle", "flame", "grape", "house", "sorry", "knock"]
    hard_words = ["academy", "balance", "cabinet", "diamond", "elegant", "freedom", "gallery", "harmony", "journey", "kingdom"]
    extreme_words = ["adventure","beautiful","challenge","dangerous","education","forgotten","happiness","important","knowledge",
                     "necessary","residence","treatment","valuedome","wonderful","embracing"]

    mode = input("Choose dificulty level.(Easy,Medium,Hard,extreme): ").lower()

    if mode == "easy":
        secret = random.choice(easy_words)

    if mode == "medium":
        secret = random.choice(medium_words)

    elif mode == "hard":
        secret = random.choice(hard_words)

    elif mode == "extreme":
        secret = random.choice(extreme_words)

    else:
        print ("Invalid input.Defaulting to easy mode.")
        secret = random.choice(easy_words)

    print("The lenght of the word is:",len(secret))
    print(f"The word starts with {secret[0]}.")

    attempt = 0

    while True:
        guess = input("Enter your guess: ").lower()
        attempt += 1
        hint = ""

        if guess == secret:
            print(f"\nCongratulation.You guess the word in {attempt} attempts!")
            break
        
        else:
            for i in range(len(secret)):
                if  i < len(guess) and guess[i] == secret[i]:
                    hint += guess[i]
                else:
                    hint += "_"
        print(f"Hint: {hint}")
main()
while True:
    user_input = input("\nDo you want to exit the game [exit] or (press a key to continue): ").lower()

    if user_input == "exit":
        print("Game Over.Thank you for playing.Good Bye!")
        break

    else:
        main()
    
    



