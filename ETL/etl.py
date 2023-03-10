import pandas as pd
# import pymysql
from sqlalchemy import create_engine


try:
    #Database connection
    host='db'
    user='root'
    password='Admin123'
    db='Users'
    engine = create_engine(f'mysql://{user}:{password}@{host}/{db}')
    print("Connected to Users database successfully")

    try:
        # Read in the CSV file
        df = pd.read_csv('DATASET.csv')
        print("\nRead CSV operation succesfull \n")

        # Checking Nulls
        print("Null Values Summary: \n",df.isna().sum())

        # Checking Duplicates
        print("\nDuplicate Values Summary:",df.duplicated().sum())

        # Transformations
        # Concatenating First and Last Name
        df['full_name'] = df['first_name'] + " " + df['last_name']
        # Filtering rows whose email doesn't end with .com
        df = df[df['email'].str.endswith('.com')]
    except Exception as e:
        print("\nError in reading CSV or perfoming transformation")



    # Load the data into the database
    try:
        df.to_sql('users_info', con=engine, if_exists='replace',index=False)
        print("\nTable users_info inserted Successfully")
        engine.dispose()
    except Exception as e:
        print("\nUnable to load users_info table in Users database")


except Exception as e:
    print("The connection to Users database was not successfull")




