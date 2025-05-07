import re

# Συνάρτηση για τον έλεγχο του email
def is_valid_email(email):
    # Ελέγχουμε αν το email περιέχει το σύμβολο "@" και αν τελειώνει σε .com, .cy ή .gr
    if '@' in email and (email.endswith('.com') or email.endswith('.cy') or email.endswith('.gr')):
        return True
    return False

# Λίστα για αποθήκευση των valid emails
valid_emails = []

# Ζητάμε από τον χρήστη να εισάγει 5 email addresses
for i in range(5):
    email = input(f"Εισάγετε το {i+1}ο email: ")
    
    # Έλεγχος εγκυρότητας του email
    if is_valid_email(email):
        print(f"✅ Το email {email} είναι έγκυρο.")
        valid_emails.append(email)
    else:
        print(f"❌ Το email {email} δεν είναι έγκυρο.")

# Αποθήκευση των valid emails σε αρχείο
with open("valid_emails.txt", "w") as file:
    for email in valid_emails:
        file.write(email + "\n")

print("\n💾 Τα έγκυρα emails αποθηκεύτηκαν στο αρχείο 'valid_emails.txt'.")


