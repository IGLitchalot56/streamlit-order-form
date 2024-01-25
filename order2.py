import streamlit as st

# Dictionary to store calorie values for each item
calories_dict = {
    'Hamburger': 250,
    'Big Mac': 563,
    'Hot Dog': 272,
    'Slice Of Pizza': 277,
    'Slice with Pepperoni': 309,
    'Ham Sandwich': 447,
    'PB&J sandwich': 376,
    'French Fries': 400,
    'Can of Coke': 140,
    'Sports / energy drink (16 oz)': 52,
    'Milkshake': 690,
}

# Create checkboxes
with st.sidebar:
    st.write('MENU:')
    quantity1 = st.number_input('Hamburger', min_value=0, step=1, value=0)
    quantity2 = st.number_input('Big Mac', min_value=0, step=1, value=0)
    quantity3 = st.number_input('Hot Dog', min_value=0, step=1, value=0)
    quantity4 = st.number_input('Slice of Pizza', min_value=0, step=1, value=0)
    quantity5 = st.number_input('Slice with Pepperoni', min_value=0, step=1, value=0)
    quantity6 = st.number_input('Ham Sandwich', min_value=0, step=1, value=0)
    quantity7 = st.number_input('PB&J', min_value=0, step=1, value=0)
    quantity8 = st.number_input('French Fries', min_value=0, step=1, value=0)
    quantity9 = st.number_input('Can of Coke', min_value=0, step=1, value=0)
    quantity10 = st.number_input('Sports / energy drink (16 oz)', min_value=0, step=1, value=0)
    quantity11 = st.number_input('Milkshake', min_value=0, step=1, value=0)

total_calories = sum(quantity * calories_dict[item] for quantity, item in zip([quantity1, quantity2, quantity3, quantity4, quantity5, quantity6, quantity7, quantity8, quantity9, quantity10, quantity11], calories_dict.keys()))
walking = round(float(total_calories / 177), 1)
running = total_calories / 596
biking = total_calories / 650
sit = total_calories / 68

# Display total calories
st.write(f'Total Calories: {total_calories}')
st.write('Time to burn off:')
st.write(f'Walking: {walking}')
st.write(f'Running: {format(running, ".1f")}')
st.write(f'Biking: {format(biking, ".1f")}')
st.write(f'Sitting on couch: {format(sit, ".1f")}')







