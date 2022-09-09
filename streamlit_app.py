import streamlit
streamlit.title('My Hubby is best')
streamlit.header('😊Qualities of good husband')
streamlit.text('😍Loving')
streamlit.text('🥰Caring')
streamlit.header('How to build your own smoothies')
import pandas
my_fruit_list=pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
