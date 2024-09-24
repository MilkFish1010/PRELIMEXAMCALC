import streamlit as st
import streamlit.components.v1 as components

# Grade Compositions (same as your previous logic)
def the_computer(prelim_grade):
    overall_passing_grade = 75
    must_deannlister = 90
    prelim_percentage = 0.20
    midterm_percentage = 0.30
    final_percentage = 0.50

    if prelim_grade >= 50:
        must_deannlister = 90.0
        scored_deannlister = must_deannlister - (0.20 * prelim_grade)
        must_fart_deannlister = scored_deannlister / 0.80
        deans_list_status = "🎉It is possible to achieve Dean's list with that Prelim grade!"
        deans_list_status2 = round(must_fart_deannlister, 2)
    else:
        deans_list_status = "Sorry, it's not possible to have dean's list regardless of Midterm and Final grade with that Prelim grade 😔"
        deans_list_status2 = f"❌Not Possible❌"

    student_prelim_grade = prelim_grade * prelim_percentage
    remaining_required = overall_passing_grade - student_prelim_grade
    midterm_required = remaining_required / (midterm_percentage + final_percentage)
    final_required = remaining_required / (midterm_percentage + final_percentage)

    return {
        "prelim": round(prelim_grade, 2),
        "midterm": round(midterm_required, 2),
        "final": round(final_required, 2),
        "deans_list": deans_list_status,
        "deans_list2": deans_list_status2,
    }

# Grade Calculation Function (same as your previous logic)
def compute_grade(absences, prelim_exam, quizzes, requirements, recitation):
    if absences >= 4:
        return None
    attendance = max(0, 100 - 10 * absences)
    class_standing = (quizzes * 0.40) + (requirements * 0.30) + (recitation * 0.30)
    prelim_grade = (prelim_exam * 0.60) + (attendance * 0.10) + (class_standing * 0.30)
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

# Adding your custom HTML for styling with CSS in string format
html_code = """
<!DOCTYPE html>
<html lang="en" data-theme="dark">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Prelim Grade Calculator</title>
    <style>
        .error {
            color: red;
            font-weight: bold;
            margin-top: 10px;
        }
        .result {
            background-color: #e7f3e7;
            padding: 10px;
            border-left: 5px solid #ffe100;
            font-size: 18px;
        }
        body {
            background-image: url('https://i.pinimg.com/originals/ec/b4/9a/ecb49ae237029ebb64c56f7ec5e8c978.gif');
            background-size: cover;
        }
        h1 {
            color: gold;
            text-align: center;
        }
        .container {
            width: 80%;
            margin: 20px auto;
            background-color: #370000;
            padding: 20px;
            border: 10px outset rgb(255, 217, 0);
            text-align: center;
            color: rgb(241, 9, 9);
            box-shadow: 0 0 100px #f50000;
        }
        h2 {
            color: rgb(226, 178, 2);
        }
    </style>
</head>
<body>
    <section class="container">
        <h1>Prelim Grade Calculator</h1>
        <!-- Form elements should be replaced by Streamlit input elements -->
        <br>
        <div class="result description">
            <h2>Results:</h2>
        </div>
    </section>
</body>
</html>
"""

components.html(html_code, height=600)
