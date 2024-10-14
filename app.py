import streamlit as st
import math
import numpy as np
import matplotlib.pyplot as plt

# Scientific operations
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    else:
        return x / y

def power(x, y):
    return x ** y

def sqrt(x):
    return math.sqrt(x)

def log(x, base=10):
    return math.log(x, base)

def sin(x):
    return math.sin(math.radians(x))

def cos(x):
    return math.cos(math.radians(x))

def tan(x):
    return math.tan(math.radians(x))

def factorial(x):
    return math.factorial(int(x))

# Streamlit app
def main():
    # Custom CSS for styling
    st.markdown("""
        <style>
        body {
            background-color: #f0f2f6;
        }
        .stApp {
            background-color: #f7f7f7;
        }
        .title {
            text-align: center;
            color: #4b7bec;
            font-family: 'Arial', sans-serif;
        }
        .stButton button {
            background-color: #4b7bec;
            color: white;
            font-size: 16px;
            padding: 0.5em 1em;
            border-radius: 8px;
        }
        .result-box {
            background-color: #ebeff5;
            padding: 20px;
            margin-top: 20px;
            border-radius: 8px;
            font-weight: bold;
            color: #2d3436;
        }
        </style>
    """, unsafe_allow_html=True)

    # Title with styling
    st.markdown("<h1 class='title'>Scientific Calculator with Plotting</h1>", unsafe_allow_html=True)
    st.write("An enhanced scientific calculator with function plotting, powered by **Streamlit**.")

    # Input fields
    col1, col2 = st.columns(2)
    
    with col1:
        num1 = st.number_input("Enter the first number", value=0.0, step=1.0)
    
    with col2:
        num2 = st.number_input("Enter the second number (optional for single operand operations)", value=0.0, step=1.0)

    # Operation selection
    st.markdown("<h3>Select an operation:</h3>", unsafe_allow_html=True)
    
    # Arithmetic operations
    st.markdown("**Basic Operations**")
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        add_clicked = st.button("➕ Add")
    with col2:
        sub_clicked = st.button("➖ Subtract")
    with col3:
        mul_clicked = st.button("✖️ Multiply")
    with col4:
        div_clicked = st.button("➗ Divide")

    # Scientific operations
    st.markdown("**Scientific Operations**")
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        sqrt_clicked = st.button("√ Square Root")
    with col2:
        pow_clicked = st.button("^ Power")
    with col3:
        log_clicked = st.button("Log")
    with col4:
        fact_clicked = st.button("n! Factorial")

    # Trigonometric operations with plot buttons
    st.markdown("**Trigonometric Functions with Plotting**")
    col1, col2, col3 = st.columns(3)
    with col1:
        sin_clicked = st.button("sin")
    with col2:
        cos_clicked = st.button("cos")
    with col3:
        tan_clicked = st.button("tan")

    # Perform calculation based on the selected operation
    result = None

    # Basic operations
    if add_clicked:
        result = add(num1, num2)
    elif sub_clicked:
        result = subtract(num1, num2)
    elif mul_clicked:
        result = multiply(num1, num2)
    elif div_clicked:
        result = divide(num1, num2)

    # Scientific operations
    elif sqrt_clicked:
        result = sqrt(num1)
    elif pow_clicked:
        result = power(num1, num2)
    elif log_clicked:
        result = log(num1)
    elif fact_clicked:
        result = factorial(num1)

    # Trigonometric functions
    elif sin_clicked:
        result = sin(num1)
        plot_function(np.sin, "Sine Wave", num1)
    elif cos_clicked:
        result = cos(num1)
        plot_function(np.cos, "Cosine Wave", num1)
    elif tan_clicked:
        result = tan(num1)
        plot_function(np.tan, "Tangent Wave", num1)

    # Display the result
    if result is not None:
        st.markdown("<div class='result-box'>The result is: {}</div>".format(result), unsafe_allow_html=True)

    # Footer
    st.markdown("""
        <hr>
        <footer style='text-align: center;'>
            <small>Made with ❤️ using Streamlit</small>
        </footer>
    """, unsafe_allow_html=True)

def plot_function(func, title, angle=None):
    """Plot a trigonometric function (sin, cos, tan) for visualization"""
    st.markdown(f"### Plotting: {title}")
    x = np.linspace(-2 * np.pi, 2 * np.pi, 500)
    y = func(x)
    
    # Create the plot
    fig, ax = plt.subplots()
    ax.plot(x, y, label=f"{title}")
    
    # If angle provided, plot a specific point
    if angle is not None:
        angle_rad = math.radians(angle)
        ax.plot(angle_rad, func(angle_rad), 'ro', label=f'Angle: {angle}°')

    ax.legend(loc="upper right")
    ax.axhline(0, color='black',linewidth=0.5)
    ax.axvline(0, color='black',linewidth=0.5)
    st.pyplot(fig)

if __name__ == '__main__':
    main()
