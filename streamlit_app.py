import streamlit
streamlit.title('my parents first diner')
streamlit.header('BreakFast Menu')
streamlit.text('🐔 dosa and Idly')
streamlit.text('🥗 oatmeal, bread butter, jam and croissants, smoothie')
streamlit.text('🍞puri, vada');

Import Pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
