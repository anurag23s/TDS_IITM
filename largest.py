import streamlit as st

def largest_of_three(a, b, c):
    return max(a, b, c)

def main():
    st.title("Largest of Three Numbers Calculator")
    st.markdown(
        """
        **Created by:** Anurag Sinha (21f3002198)
        """
    )
    st.write("This simple app calculates the largest of three numbers entered by the user.")
    
    # Input fields for the three numbers
    st.sidebar.header("Enter Numbers")
    number1 = st.sidebar.number_input("First Number" )
    number2 = st.sidebar.number_input("Second Number" )
    number3 = st.sidebar.number_input("Third Number")
    
    # Button to calculate the largest number
    st.sidebar.markdown("---")
    st.sidebar.header("Options")
    if st.sidebar.button("Calculate"):
        largest = largest_of_three(number1, number2, number3)
        st.success(f"The largest number is: {largest}")

if __name__ == "__main__":
    main()
