def calculate_overall_grade(grades):
    """Calculate the overall grade as a percentage."""
    return sum(grades) / len(grades)

def determine_letter_grade(overall_percentage):
    """Determine the letter grade based on the overall percentage."""
    if overall_percentage < 40:
        return 'Fail'
    elif 40 <= overall_percentage < 60:
        return 'C'
    elif 60 <= overall_percentage < 80:
        return 'B'
    else:
        return 'A'

def main():
    # Initialize a list to store grades
    grades = []
    print("Enter your grades for five subjects:")

    # Input grades from the user
    for i in range(1, 6):
        while True:
            try:
                grade = float(input(f"Grade for subject {i} (0-100): "))
                if 0 <= grade <= 100:
                    grades.append(grade)
                    break
                else:
                    print("Please enter a grade between 0 and 100.")
            except ValueError:
                print("Invalid input. Please enter a numerical value.")

    # Calculate the overall percentage
    overall_percentage = calculate_overall_grade(grades)

    # Determine the letter grade
    letter_grade = determine_letter_grade(overall_percentage)

    # Print the results
    print(f"\nOverall Percentage: {overall_percentage:.2f}%")
    print(f"Letter Grade: {letter_grade}")

if __name__ == "__main__":
    main()
