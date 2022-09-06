
import streamlit
import pandas

streamlit.title('My parents new healthy dinner')
streamlit.header('\N{banana}My Mom''s Breakfast Menu\N{egg}')
streamlit.text('\N{blueberries}Omega 3 & Blueberry Oatmeal')
streamlit.text('Kale, Spinach and Rocket smoothie')

my_fruit_list = pandas.read_csv('https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt')
steamlit.dataframe(my_fruit_list)
