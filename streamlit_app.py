
import streamlit
import pandas
import requests


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


streamlit.header('Fruityvice Fruit Advice')


fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
streamlit.write('The user entered ', fruit_choice)


fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice )
#streamlit.text(fruityvice_response.json())

fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
streamlit.dataframe (fruityvice_normalized)

import snowflake.connector
my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")
my_data_row = my_cur.fetchone()
streamlit.text("Hello from Snowflake:")
streamlit.text(my_data_row)
