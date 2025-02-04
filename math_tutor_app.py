import streamlit as st
from transformers import pipeline

# Load the T5 model for text-to-text tasks
model_name = "t5-small"
generator = pipeline("text2text-generation", model=model_name)

# Function to solve a math problem
def solve_math_problem(problem):
    prompt = f"solve {problem}"
    result = generator(prompt, max_length=50)[0]['generated_text']
    return result

import streamlit as st

# Function to solve a math problem using eval
def solve_math_problem(problem):
    try:
        # Use eval to evaluate the math expression
        solution = eval(problem)
        return solution
    except Exception as e:
        return f"Error: {str(e)}"

# Streamlit UI setup
st.title("AI Math Tutor")

st.write("Enter a math problem, and I'll solve it for you!")

# Input box for the math problem
problem_input = st.text_input("Math Problem", "99+3434-444")

# When the button is pressed, solve the problem
if st.button("Solve"):
    if problem_input:
        # Get the solution from the function
        solution = solve_math_problem(problem_input)
        st.write(f"Solution: {solution}")
    else:
        st.write("Please enter a math problem!")


