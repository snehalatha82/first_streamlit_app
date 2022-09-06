
import streamlit
import pandas

streamlit.title('My parents new healthy dinner')
streamlit.header('\N{banana}My Mom''s Breakfast Menu\N{egg}')
streamlit.text('Omega 3 & Blueberry Oatmeal')
streamlit.text('Kale, Spinach and Rocket smoothie')

# Load the data from the CSV to Pandas Dataframe
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")


#set index to Fruit instead of default number
my_fruit_list = my_fruit_list.set_index('Fruit')

# select the  fruit and list them
fruits_selected = streamlit.multiselect('Pick Some Fruits ',  list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show  = my_fruit_list.loc[fruits_selected]
streamlit.dataframe(fruits_to_show)
