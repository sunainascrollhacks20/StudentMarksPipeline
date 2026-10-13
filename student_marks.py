
def calculate_total(marks):
    if len(marks) != 3:
        raise ValueError("Enter marks for exactly 3 subjects")

    if any(mark < 0 or mark > 100 for mark in marks):
        raise ValueError("Marks must be between 0 and 100")

    return sum(marks)


def calculate_percentage(marks):
    total = calculate_total(marks)
    return (total / 300) * 100


def get_result(marks):
    calculate_total(marks)

    if all(mark >= 35 for mark in marks):
        return "Pass"

    return "Fail"


if __name__ == "__main__":
    marks = [75, 80, 65]

    print("Total:", calculate_total(marks))
    print("Percentage:", calculate_percentage(marks))
    print("Result:", get_result(marks))
