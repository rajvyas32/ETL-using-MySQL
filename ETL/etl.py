import pandas as pd
# import pymysql
from sqlalchemy import create_engine

#Database connection
host='db'
user='root'
password='Admin123'
db='Users'

engine = create_engine(f'mysql://{user}:{password}@{host}/{db}')

# Read in the CSV file
df = pd.read_csv('SRDataEngineerChallenge_DATASET.csv')

# Checking Nulls
print("Null Values Summary: \n",df.isna().sum())

# Checking Duplicates
print("\n Duplicate Values Summary:",df.duplicated().sum())

# Transformations
# Concatenating First and Last Name
df['full_name'] = df['first_name'] + " " + df['last_name']
# Filtering rows whose email doesn't end with .com
df = df[df['email'].str.endswith('.com')]





# Load the data into the database
df.to_sql('users_info', con=engine, if_exists='replace',index=False)

print("Table inserted Successfully")


engine.dispose()
