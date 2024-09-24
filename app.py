from flask import Flask, render_template, os, request

app = Flask(__name__)

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

# POST from flask to submit data from HTML
@app.route("/", methods=["GET", "POST"])
def index():
    error = None
    result = None
    if request.method == "POST":
        try:
            # Get inputs
            absences = int(request.form["absences"])
            prelim_exam = float(request.form["prelim_exam"])
            quizzes = float(request.form["quizzes"])
            requirements = float(request.form["requirements"])
            recitation = float(request.form["recitation"])

            # Validate input ranges
            if prelim_exam < 0 or prelim_exam > 100 or quizzes < 0 or quizzes > 100 or requirements < 0 or requirements > 100 or recitation < 0 or recitation > 100:
                error = "ERROR ⚠️: Grades must be between 0 and 100."
            elif absences < 0:
                error = "ERROR ⚠️: Absences cannot be negative."
            else:
                # Calculate the final result
                prelim_grade = compute_grade(absences, prelim_exam, quizzes, requirements, recitation)
                if prelim_grade is None:
                    error = "😔 You Failed the Prelim because of your absences. 😔"
                else:
                    result = the_computer(prelim_grade)

        except ValueError:
            error = "ERROR ⚠️: Please enter valid numeric values."

    return render_template("index.html", error=error, result=result)

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



# this one runs flask
if __name__ == "__main__":
    app.run(debug=True)
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
   
