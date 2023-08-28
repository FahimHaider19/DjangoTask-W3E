# E-commerce Product Catalog

This project is an E-commerce product catalog that allows users to browse and search for products. It also includes an admin dashboard for managing products and a product details page where users can add reviews.

## Features

1. **Admin Dashboard:** Using Superuser.

2. **Product Listing Page:** Users can view a list of available products.

3. **Product Search:** Users can search for products by their names.

4. **Product Details Page:** Users can view detailed information about a specific product.

5. **Product Reviews:** Users can add reviews to products on the details page.


## Prerequisites
  - Docker
  - Python
  - Django
  - PostgreSQL / PGAdmin


## Installation and Setup

1. Clone the repository:

   ```
   git clone https://github.com/FahimHaider19/DjangoTask-W3E
   cd DjangoTask-W3E
   ```

2. Create a virtual environment and activate it:

   ```
   python -m venv venv
   source venv/bin/activate
   ```

3. Install the required packages:

   ```
   pip install -r requirements.txt
   ```

4. Create `.env` update the environment variables:

   ```
   DBNAME=DjangoTaskW3E
   DBUSER=user-name
   DBPASSWORD=strong-password
   DBHOST=localhost
   DBPORT=5432
   ```

5. Change Directory and Navigate to Project

   ```
   cd DjangoTaskW3E
   ```

5. Run migrations:

   ```
   python manage.py migrate
   ```

6. Start the development server:

   ```
   python manage.py runserver
   ```

7. Open your browser and navigate to `http://127.0.0.1:8000` to access the application.

## Create Superuser
1. **Activate Virtual Environment(if needed):**
   If you're using a virtual environment, make sure it's activated. Navigate to your project's root directory and run:

   ```
   source venv/bin/activate
   ```

2. **Run the Management Command:**
   In your terminal, navigate to your project's directory and run the following command:

   ```
   python manage.py createsuperuser
   ```

3. **Enter Superuser Details:**
   You'll be prompted to enter the following details for the superuser:

   - Username: Enter a username for the superuser.
   - Email address: Enter the email address associated with the superuser.
   - Password: Set a strong password for the superuser.

4. **Confirm Password:**
   You'll be asked to confirm the password by entering it again.

5. **Superuser Created:**
   Once you've completed these steps, the superuser will be created, and you'll receive a confirmation message.


## Requirements

See the `requirements.txt` file for a list of Python packages required for this project. You can install them using the following command:

```
pip install -r requirements.txt
```



## PostgreSQL Setup

- Create a new file named `docker-compose-postgres.yml`.

- Copy and paste the following content into the `docker-compose-postgres.yml` file:

   ```yaml
   version: "3.8"
   services:
     db:
       image: postgres
       container_name: postgres
       restart: always
       ports:
         - "5432:5432"
       environment:
         POSTGRES_USER: user-name
         POSTGRES_PASSWORD: strong-password
       volumes:
         - local_pgdata:/var/lib/postgresql/data
     pgadmin:
       image: dpage/pgadmin4
       container_name: pgadmin4_container
       restart: always
       ports:
         - "8888:80"
       environment:
         PGADMIN_DEFAULT_EMAIL: user-name@domain-name.com
         PGADMIN_DEFAULT_PASSWORD: strong-password
       volumes:
         - pgadmin-data:/var/lib/pgadmin

   volumes:
     local_pgdata:
     pgadmin-data:
   ```

- Open a terminal window and navigate to the folder where you placed the `docker-compose-postgres.yml` file.

- Run the following command to start the PostgreSQL and pgAdmin containers:
```
docker-compose -f docker-compose-postgres.yml up -d
```
- PostgreSQL will be available on port `5432`, and pgAdmin will be available on port `8888`.


- Make sure you have Docker and Docker Compose installed before running the above commands. These instructions assume that you are in the same directory as the Docker Compose files when running the commands. Once the containers are up and running, you can proceed with setting up your Flask app to interact with the PostgreSQL and Elasticsearch databases.


## Contribute

Contributions are welcome! If you find any issues or want to add new features, feel free to open a pull request.

## License

This project is licensed under the [MIT License](LICENSE).
