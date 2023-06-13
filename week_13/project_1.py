import pandas as pd

# Create an empty DataFrame
df = pd.DataFrame(columns=['Student Name', 'Matric Number', 'Department', 'Level'])

# Get the number of students
num_students = int(input("Enter the number of students: "))

# Input personal details of each student
for i in range(num_students):
    print(f"\nEnter details for student {i+1}:")
    name = input("Name: ")
    matric_number = input("Matric Number: ")
    department = input("Department: ")
    level = input("Level: ")

    # Add the student's details to the DataFrame
    df = df.append({'Student Name': name,
                    'Matric Number': matric_number,
                    'Department': department,
                    'Level': level}, ignore_index=True)

# Display the DataFrame
print("\nStudent Details:")
print(df)

# Save DataFrame to Excel file
file_name = input("\nEnter the file name to save (e.g., student_details.xlsx): ")
df.to_excel(file_name, index=False)
print(f"\nStudent details saved to {file_name} successfully.")



