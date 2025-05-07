import pandas as pd
import random

# Δημιουργία τυχαίων δεδομένων χρηστών
data = {
    'ID': range(1, 501),
    'Όνομα': [f'Όνομα{i}' for i in range(1, 501)],
    'Επίθετο': [f'Επίθετο{i}' for i in range(1, 501)],
    'Ηλικία': [random.randint(18, 65) for _ in range(500)],
    'Email': [f'user{i}@example.com' for i in range(1, 501)],
    'Πόλη': [f'Πόλη{i}' for i in range(1, 501)],
    'Χώρα': ['Ελλάδα' for _ in range(500)],
    'Μισθός (€)': [random.randint(1000, 5000) for _ in range(500)],
    'Τμήμα': ['Τμήμα' + str(random.randint(1, 5)) for _ in range(500)],
    'Ενεργός': ['Ναι' if random.random() > 0.2 else 'Όχι' for _ in range(500)]  # 80% ενεργοί
}

# Δημιουργία DataFrame
df = pd.DataFrame(data)

# Αποθήκευση στο αρχείο Excel
df.to_excel("users.xlsx", index=False, engine='openpyxl')
print("✅ Το αρχείο 'users.xlsx' δημιουργήθηκε επιτυχώς.")

import pandas as pd

# 1. Διαβάζουμε το αρχείο Excel
try:
    df = pd.read_excel("users.xlsx", engine="openpyxl")
    print("✅ Το αρχείο φορτώθηκε επιτυχώς.")
except FileNotFoundError:
    print("❌ Το αρχείο 'users.xlsx' δεν βρέθηκε.")
    exit()

# 2. Φιλτράρουμε ενεργούς χρήστες άνω των 30
filtered_df = df[(df["Ηλικία"] > 30) & (df["Ενεργός"] == "Ναι")]

# 3. Εμφάνιση αποτελεσμάτων
print("\n📋 Ενεργοί χρήστες άνω των 30:\n")
print(filtered_df)

# 4. Υπολογισμός μέσου όρου ηλικίας όλων των χρηστών
mean_age = df["Ηλικία"].mean()
print(f"\n📊 Μέσος όρος ηλικίας όλων των χρηστών: {mean_age:.2f} έτη")

# 5. Υπολογισμός μέσου όρου μισθού ενεργών χρηστών
active_users = df[df["Ενεργός"] == "Ναι"]
mean_salary = active_users["Μισθός (€)"].mean()
print(f"📊 Μέσος όρος μισθού ενεργών χρηστών: €{mean_salary:.2f}")

# 6. Αποθήκευση των ενεργών χρηστών άνω των 30 σε νέο αρχείο Excel
filtered_df.to_excel("active_users_over30.xlsx", index=False)
print("\n💾 Το αρχείο 'active_users_over30.xlsx' αποθηκεύτηκε επιτυχώς.")