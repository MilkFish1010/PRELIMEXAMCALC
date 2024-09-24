import streamlit as st

# Grade Compositions
def the_computer(prelim_grade):
    overall_passing_grade = 75
    must_deannlister = 90
    prelim_percentage = 0.20  # 20%
    midterm_percentage = 0.30  # 30%
    final_percentage = 0.50  # 50%

    if prelim_grade >= 50:
        must_deannlister = 90.0
        scored_deannlister = must_deannlister - (0.20 * prelim_grade)
        must_fart_deannlister = scored_deannlister / 0.80
        deans_list_status = "🎉It is possible to achieve Dean's list with that Prelim grade!"
        deans_list_status2 = round(must_fart_deannlister, 2)
    else:
        deans_list_status = "Sorry, it's not possible to have dean's list regardless of Midterm and Final grade with that Prelim grade man 😔"
        deans_list_status2 = f"❌Not Possible❌"

    # Gets the 20% of the prelim grade of student and make it into a variable
    student_prelim_grade = prelim_grade * prelim_percentage
    # Converts or contains the prelim grade to an overall grade and also making a variable for checking the possibility to pass
    remaining_required = overall_passing_grade - student_prelim_grade

    # I'll Assume equal distribution as answers
    midterm_required = remaining_required / (midterm_percentage + final_percentage)
    final_required = remaining_required / (midterm_percentage + final_percentage)

    # Limit the decimals to 2
    return {
        "prelim": round(prelim_grade, 2),
        "midterm": round(midterm_required, 2),
        "final": round(final_required, 2),
        "deans_list": deans_list_status,
        "deans_list2": deans_list_status2,
    }

# Grade Calculation Function
def compute_grade(absences, prelim_exam, quizzes, requirements, recitation):
    # Attendance logic
    if absences >= 4:
        return None  # Immediate fail if 4 or more absences
    attendance = max(0, 100 - 10 * absences)  # Subtract 10 points per absence

    # Class standing calculation (40% quizzes, 30% requirements, 30% recitation)
    class_standing = (quizzes * 0.40) + (requirements * 0.30) + (recitation * 0.30)

    # Prelim grade calculation (60% exam, 10% attendance, 30% class standing)
    prelim_grade = (prelim_exam * 0.60) + (attendance * 0.10) + (class_standing * 0.30)

    # Return rounded result
    return round(prelim_grade, 2)

# Streamlit app
st.title("Prelim Grade Calculator")

absences = st.number_input("Number of Absences:", min_value=0, step=1)
prelim_exam = st.number_input("Prelim Exam Grade:", min_value=0.0, max_value=100.0, step=0.01)
quizzes = st.number_input("Quizzes Grade:", min_value=0.0, max_value=100.0, step=0.01)
requirements = st.number_input("Requirements Grade:", min_value=0.0, max_value=100.0, step=0.01)
recitation = st.number_input("Recitation Grade:", min_value=0.0, max_value=100.0, step=0.01)

if st.button("Calculate"):
    if prelim_exam < 0 or prelim_exam > 100 or quizzes < 0 or quizzes > 100 or requirements < 0 or requirements > 100 or recitation < 0 or recitation > 100:
        st.error("ERROR ⚠️: Grades must be between 0 and 100.")
    elif absences < 0:
        st.error("ERROR ⚠️: Absences cannot be negative.")
    else:
        prelim_grade = compute_grade(absences, prelim_exam, quizzes, requirements, recitation)
        if prelim_grade is None:
            st.error("😔 You Failed the Prelim because of your absences. 😔")
        else:
            result = the_computer(prelim_grade)
            st.success("Results:")
            st.write(f"Prelim Grade: {result['prelim']}")
            st.write(f"To pass with an overall grade of 75, you need at least:")
            st.write(f"Midterm Required: {result['midterm']}")
            st.write(f"Final Required: {result['final']}")
            st.write(f"Dean's List Status: {result['deans_list']}")
            st.write(f"Get this Midterm and Final to attain Dean's list overall grade of 90 requirement (assuming both equal grades): {result['deans_list2']}")

html_file_path = "templates/index.html"

# Read the HTML file
with open(html_file_path, 'r', encoding='utf-8') as file:
    html_content = file.read()

# Display the HTML content in Streamlit
components.html(html_content, height=600)
