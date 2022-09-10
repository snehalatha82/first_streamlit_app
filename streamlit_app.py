
import streamlit
import pandas
import requests
import snowflake.connector
from urllib.error import URLError


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

def get_fruityvice_data(this_fruit_choice):
  fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + this_fruit_choice )
  fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
  return(fruityvice_normalized)

streamlit.header('Fruityvice Fruit Advice')
try:
  fruit_choice = streamlit.text_input('What fruit would you like information about?')
  if not fruit_choice:
    streamlit.error('Select the fruit of your choice')
  else:
    back_from_function = get_fruityvice_data(fruit_choice)
    streamlit.dataframe (back_from_function)
except UrlError as  e:
    streamlit.error()

def get_fruit_list():
  with my_cnx.cursor() as my_cur:
    my_cur.execute("SELECT * from fruit_load_list")
    return my_cur.fetchall()

if streamlit.button("Get Fruit List"):
  my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
  my_data_rows = get_fruit_list()
  streamlit.dataframe(my_data_rows)

def insert_new_fruit(new_fruit):
  with my_cnx.cursor() as my_cur:
    my_cur.execute("insert into fruit_load_list values ('from streamlit')")
    return "Thanks for adding " + new_fruit
  
add_my_fruit = streamlit.text_input("What fruit would you like to add?")
if streamlit.button("Add New Fruit"):
  my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
  back_from_func = insert_new_fruit(add_my_fruit)
  streamlit.text (back_from_func)
