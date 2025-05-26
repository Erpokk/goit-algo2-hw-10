class Teacher:
    def __init__(self, first_name, last_name, age, email, can_teach_subjects):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email
        self.can_teach_subjects = set(can_teach_subjects)
        self.assigned_subjects = set()


def create_schedule(subjects, teachers):
    remaining_subjects = set(subjects)
    schedule = []

    while remaining_subjects:
        best_teacher = None
        best_coverage = set()

        for teacher in teachers:
            coverage = teacher.can_teach_subjects & remaining_subjects
            if len(coverage) > len(best_coverage) or (
                len(coverage) == len(best_coverage)
                and teacher.age < (best_teacher.age if best_teacher else float("inf"))
            ):
                best_teacher = teacher
                best_coverage = coverage

        if not best_teacher:
            print("It is impossible to cover all subjects with the available teachers.")
            return None

        best_teacher.assigned_subjects = best_coverage
        schedule.append(best_teacher)
        remaining_subjects -= best_coverage

    return schedule


if __name__ == "__main__":
    subjects = {"Math", "Physics", "Chemistry", "Information_technology", "Biology"}
    teachers = [
        Teacher(
            "Jack",
            "Daniels",
            45,
            "jack_danaiels@example.com",
            {"Math", "Physics"},
        ),
        Teacher("Jame", "Son", 38, "jameson@example.com", {"Chemistry"}),
        Teacher(
            "Glen ",
            "Fiddich",
            50,
            "glenFiddich@example.com",
            {"Information_technology", "Math"},
        ),
        Teacher(
            "Glen", "Livet", 29, "glenlivet@example.com", {"Biology", "Chemistry"}
        ),
        Teacher(
            "Ball",
            "Antines",
            35,
            "Ballantines@example.com",
            {"Physics", "Information_technology"},
        ),
        Teacher("Tullamore", "Dew", 42, "tullamoredew@example.com", {"Biology"}),
    ]

    schedule = create_schedule(subjects, teachers)

    if schedule:
        print("Lessons schedule:")
        for teacher in schedule:
            print(f"{teacher.first_name} {teacher.last_name}, {teacher.age} age, email: {teacher.email}")
            print(f"Study next: {', '.join(teacher.assigned_subjects)}\n")