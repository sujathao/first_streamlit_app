import streamlit
streamlit.title('my parents first diner')
streamlit.header('BreakFast Menu')
streamlit.text('🐔 dosa and Idly')
streamlit.text('🥗 oatmeal, bread butter, jam and croissants, smoothie')
streamlit.text('🍞puri, vada');

import pandas

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

streamlit.dataframe(my_fruit_list)

# Let's put a pick list here so they can pick the fruit they want to include 
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))

# Display the table on the page.
