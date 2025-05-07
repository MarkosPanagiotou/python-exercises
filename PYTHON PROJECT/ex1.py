grades = []

for i in range(5):
    while True:
        try:
            grade = float(input(f"Εισάγετε τον βαθμό #{i+1} (0 έως 100): "))
            if 0 <= grade <= 100:
                grades.append(grade)
                break
            else:
                print("Ο βαθμός πρέπει να είναι μεταξύ 0 και 100.")
        except ValueError:
            print("Παρακαλώ εισάγετε έναν έγκυρο αριθμό.")

average = sum(grades) / len(grades)
maximum = max(grades)
minimum = min(grades)

print("\nΑποτελέσματα:")
print(f"Μέσος όρος βαθμών: {average:.2f}")
print(f"Μεγαλύτερος βαθμός: {maximum}")
print(f"Μικρότερος βαθμός: {minimum}")