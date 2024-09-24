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
how to make my html work on the app and on streamlit host 
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

.highlight {
 color: greenyellow ;
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
        .gold-text {
            color: gold;
            }
            .box {
              border: outset gold 5px;
              margin: auto;
              width: 15%;
              background-color:#870606;
              padding: 10px;
            }
              .box2{
                border: gold outset 5px;
                margin: auto;
                width: 15%;
                background-color:#f8f8f8;
  
            }
            .imgborder {
              border: gold outset 15px;
              box-shadow: 0 0 50px #9ecaed;
            }
                .description {
                padding: 10px;
                float: none;
                margin: auto;
                background-color: #200101;
                border: gold outset 5px;
                width: 50%;
                text-align: center;
                box-shadow: 0 0 10px #9ecaed;      
    }   
                .amazify {
                  letter-spacing: 2px;
                  font-family: Arial, Helvetica, sans-serif;
                }
                .thesubmitbutton {
                    border: gold outset 5px;
                margin: auto;
                width: 25%;
                background-color:#663401;
                }
    </style>
</head>
<body>
    <section class="container">
        <h1>Prelim Grade Calculator</h1>
        <form method="POST" action="/">
            <label for="absences" class="box amazify gold-text" style="font-size: large;">Number of Absences:</label>
            <input type="number" id="absences" name="absences" required class="box2">
            <br><br>
            <label for="prelim_exam" class="box amazify gold-text" style="font-size: large;">Prelim Exam Grade:</label>
            <input type="number" step="0.01" id="prelim_exam" name="prelim_exam" required class="box2">
            <br><br>
            <label for="quizzes" class="box amazify gold-text" style="font-size: large;">Quizzes Grade:</label>
            <input type="number" step="0.01" id="quizzes" name="quizzes" required class="box2">
            <br><br>
            <label for="requirements" class="box amazify gold-text" style="font-size: large;">Requirements Grade:</label>
            <input type="number" step="0.01" id="requirements" name="requirements" required class="box2">
            <br><br>
            <label for="recitation" class="box amazify gold-text" style="font-size: large;">Recitation Grade:</label>
            <input type="number" step="0.01" id="recitation" name="recitation" required class="box2">
            <br><br>
            <button type="submit" class="thesubmitbutton gold-text"><h1><strong style="font-size: 50px;">▷</strong></h1></button>
        </form>
        <br>
        
        <!-- Error message -->
        <div class="error description" style="font-size: larger;"> <h2>Results:</h2><br></div>

        <!-- Result message -->
        <div class="result description" style="font-size: 25px;">
            <h1 style="font-size: 50px;">Results:</h1>
            <br>
            <h2>Prelim Grade:</h2>
            <p class="highlight"></p>
            <br><p class="gold-text" style="font-family: Arial, Helvetica, sans-serif;">To pass with an overall grade of <strong style="color: greenyellow;">75</strong>, you need at least:</p>
            <br>
            <h2>Midterm Required:</h2>
            <p class="highlight"></p>
            <h2>Final Required:</h2>
            <p class="highlight"></p>
            {% if result.deans_list %}
            <h2>Dean's List Status:</h2>
            <p style="font-size: larger; color: #e2cead;"></p>
            <p class="gold-text">Get this Midterm and Final to attain Dean's list overall grade of <br> <span style="color: greenyellow;">90</span> requirement (assuming both equal grades):<strong class="highlight"><br>  </strong>
                <br>
            </p>
        </div>
    </section>
</body>
</html>
