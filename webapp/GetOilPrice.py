from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import pandas as pd
from sqlalchemy import create_engine
import datetime
import ast,logging

# Connecting database
def conn_db():
    try:
        logging.info('Connecting database to table...')
        conn_string = 'postgresql://postgres:postgres@postgres:5432/warehouse'
        db = create_engine(conn_string)
        conn = db.connect()
        return conn
    except Exception as e:
        logging.error('Error connecting to database at %s', exc_info=e)

# Create table
def create_table(conn, sql):
    try:
        conn.execute(sql)
    except Exception as e:
        logging.error('Error create table at %s', exc_info=e)

# Scraping data from web application
def extract_data():
    try:
        # Scraping data from source
        url = 'https://www.pttor.com/th'
        option = webdriver.ChromeOptions()
        option.add_argument('headless')
        driver = webdriver.Remote(
            command_executor='http://selenium-hub:4444/wd/hub',
            desired_capabilities=DesiredCapabilities.CHROME
        )
        driver.get(url)
        logging.info('Scraping data from %s', url)

        # Get data from element html
        results = []
        for element in driver.find_elements_by_class_name('home-oil-price__table-price'):
            price = element.text
            if price != '' :
                results.append(price)

        driver.quit()
        # Create dataframe
        column = [
            'DieselB20',
            'Diesel',
            'DieselB7',
            'PetrolE85',
            'PetrolE20',
            'Gasohol91',
            'Gasohol95',
            'Petrol',
            'SupperPower_DieselB7',
            'SupperPower_Gasohol95'
        ]
        results = pd.DataFrame([results], columns=column)
        return results
    except Exception as e:
        logging.error('Error extract data source at %s', exc_info=e)

# Transform data
def transform_data(df):
    try:
        # Add datetime column
        logging.info('Transform data...')
        df['Created_at'] = datetime.datetime.now()
        return df
    except Exception as e:
        logging.error('Error transform dataframe at %s', exc_info=e)

# Write dataframe to database
def load_data(df, table, conn):
    try:
        logging.info('Write data to table %s...', table)
        df.to_sql(table, con=conn, if_exists='append',index=False,index_label='id')
    except Exception as e:
        logging.error('Error write dataframe at %s', exc_info=e)

# Main app
if __name__ == "__main__":
    # Workflow 
    # 1. Scraping data from url source 
    # 2. Transform data 
    # 3. Load dataframe to database

    table = 'oil_price'
    conn = conn_db()
    oil_price = extract_data()
    oil_price_df = transform_data(oil_price)
    load_data(oil_price_df, table, conn)

