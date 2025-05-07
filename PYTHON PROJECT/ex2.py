import random
import string

def generate_password(length, use_special_chars):
    characters = string.ascii_letters + string.digits
    if use_special_chars:
        characters += string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password


while True:
    try:
        length = int(input("Δώσε το επιθυμητό μήκος του κωδικού: "))
        if length <= 0:
            print("Το μήκος πρέπει να είναι θετικός αριθμός.")
        else:
            break
    except ValueError:
        print("Παρακαλώ δώσε έναν έγκυρο ακέραιο αριθμό.")


while True:
    choice = input("Να περιέχει ειδικούς χαρακτήρες; (ναι/όχι): ").strip().lower()
    if choice in ['ναι', 'ν']:
        use_special = True
        break
    elif choice in ['όχι', 'ο']:
        use_special = False
        break
    else:
        print("Παρακαλώ απάντησε με 'ναι' ή 'όχι'.")


password = generate_password(length, use_special)
print("\nΟ παραγόμενος κωδικός είναι:", password)