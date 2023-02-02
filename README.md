# ETL Project using Python, MySQL, and Docker
This project demonstrates how to perform an ETL process using Python, MySQL, and Docker. The project extracts data from a CSV source, transforms it into a desired format, and loads it into a MySQL database.

## Prerequisites
- Python 3
- Docker
- Docker Compose
- MySQL

## Project Structure
The project has the following structure:<br>
|-- `etl.py` <br>
|-- `SRDataEngineerChallenge_DATASET.csv` <br>
|-- `docker-compose.yml` <br>
|-- `Dockerfile` <br>

- etl.py contains the ETL logic which reads the CSV file (i.e Packaged in the docker folder) and loads it in to the MySQL server running on docker.
- SRDataEngineerChallenge_DATASET.csv contains the dummy information and data about the users.
- docker-compose.yml and Dockerfile are used to create a Docker container for the project.

## Steps to run the project
1. Clone the project repository.
```
$ git clone https://github.com/rajvyas32/ETL-using-MySQL.git
```
2. Change into the project directory.
```
$ cd ETL-using-MySQL/ETL
```
3. Start the Docker containers using Docker Compose.
```
$ docker-compose up
```
### Docker Compose Explanation:

This is docker-compose file sets up two services, "db" and "app", and a named volume "mysql-data".

- The "db" service runs a MySQL 8.0 database using the official MySQL Docker image. It sets the root password to "Admin123" and creates a database named "Users". The database's port 3306 is mapped to the host's port 3306, and the database data is stored in the named volume "mysql-data".

- The "app" service builds an image using a Dockerfile in the current directory and runs a Python script "etl.py" in the "/app" directory. The current directory is mounted as a volume at "/app" and the "app" service depends on the "db" service.

- The "app" service runs "etl.py" (with python as a base image) connects to MySQL server of "db" service, loads up the CSV file performs a set of transformation, creates a table named "users_info" and loads the data in "Users" database.

### Python file etl.py Explanation:

The python file is divided into three logical try-catch blocks.

The first block is database connection block and prints:
- "Connected to Users database successfully" when succefully connected and "The connection to Users database was not successfull" in case of failure.

The second block is trasfomation block and prints following:
- "Read CSV operation succesfull" if it was able to read CSV succesfully.
- "Null Values Summary" and "Duplicate Values Summary"
- "Error in reading CSV or perfoming transformation" in case of error from above operations

Second block does following transformation to dataframe:
- 1. Creates a new column "full_name" by appending "first_name" & "last_name"
- 2. Filters all the row which doesn't contain '.com' as domain name

The third block is data loading block and prints:
- "Table users_info inserted Successfully" when the tranformed dataframe is loaded into Users database.
- "Unable to load users_info table in Users database" in case of failure.


Once, the execution of python file is completed you will see following output:

![image](https://user-images.githubusercontent.com/124141023/216142750-63c7fc7d-524a-4743-8edd-02ea4bb69f7b.png)


### MySQL Data Validation

To check whether the data inserted by the python script is loaded succesfully we perform following operations:

1. Goto the termical and execute mysqlcontainer in interactive mode:
```
docker exec -it mysqlcontainer bash
```


2. In the interactive mode run mysql command with user as root once prompted put password as "Admin123":
```
mysql -u root -p
```

3. Once in mysql databse run the select query to retrive users_info data:
```
select * from Users.users_info;
```


Hurray!! The data was loaded succesfully?





