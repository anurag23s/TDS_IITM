import streamlit as st

def largest_of_three(a, b, c):
    return max(a, b, c)

def main():
    st.title("Largest of Three Numbers Calculator")
    st.write("Created by Anurag Sinha")
    st.write("@21f3002198")
    
    # Input fields for the three numbers
    number1 = st.number_input("Enter the first number:")
    number2 = st.number_input("Enter the second number:")
    number3 = st.number_input("Enter the third number:")
    
    # Button to calculate the largest number
    if st.button("Calculate"):
        largest = largest_of_three(number1, number2, number3)
        st.success(f"The largest number is: {largest}")

if __name__ == "__main__":
    main()
