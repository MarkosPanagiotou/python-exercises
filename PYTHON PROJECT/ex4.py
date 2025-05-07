import pandas as pd

# Διαβάζουμε το Excel αρχείο
df = pd.read_excel("users.xlsx")

# Φιλτράρουμε τους χρήστες που είναι άνω των 30 και ενεργοί
active_over30 = df[(df["Ηλικία"] > 30) & (df["Ενεργός"] == "Ναι")]

# Εμφάνιση των ενεργών χρηστών άνω των 30 ετών
print("Ενεργοί χρήστες άνω των 30:\n")
print(active_over30)

# Υπολογισμός μέσου όρου ηλικίας όλων των χρηστών
mean_age = df["Ηλικία"].mean()
print(f"\nΜέσος όρος ηλικίας όλων των χρηστών: {mean_age:.2f} έτη")

# Υπολογισμός μέσου όρου μισθού των ενεργών χρηστών
active_users = df[df["Ενεργός"] == "Ναι"]
mean_salary_active = active_users["Μισθός (€)"].mean()
print(f"Μέσος όρος μισθού των ενεργών χρηστών: €{mean_salary_active:.2f}")

# Αποθήκευση των ενεργών χρηστών άνω των 30 σε νέο αρχείο Excel
active_over30.to_excel("active_users_over30.xlsx", index=False)

print("\nΤο αρχείο 'active_users_over30.xlsx' αποθηκεύτηκε επιτυχώς.")