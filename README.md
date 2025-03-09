# **Inventory Management System (Flask + PostgreSQL + Docker)**

A **basic Flask web application** for inventory management with CRUD operations (**Create, Read, Update, Delete**). Uses **PostgreSQL** as the database and **Docker** and **Docker compose** for easy deployment.

---

## **📌 Features**

✔️ Add, edit, delete inventory items  
✔️ View all inventory items  
✔️ Search for items  
✔️ Uses PostgreSQL as the database  
✔️ Environment variable support with `.env`  
✔️ Docker support for easy deployment  

---

## **🚀 Running Options**

You have two options to run this application:

### **Option 1: Fully Local Setup (No Docker)**

1. **Set up PostgreSQL locally**
   - Install PostgreSQL 16.x on your system
   - Create a database named `inventoryDB`
   - Configure a user with appropriate permissions

2. **Set up the Flask application**
   - Clone the repository
   ```bash
   git clone https://github.com/LahiruCooray/inventory-management-flask-docker.git
   cd inventory-management-flask-docker
   ```

   - Create and activate a virtual environment
   ```bash
   python3 -m venv venv
   source venv/bin/activate   # On macOS/Linux
   venv\Scripts\activate      # On Windows
   ```

   - Install dependencies
   ```bash
   pip install -r requirements.txt
   ```

   - Create a `.env` file with local database connection(make sure that your postgresql db is running on port 5432 of your local PC):
   ```
   FLASK_ENV=development
   DATABASE_URI=postgresql://your_username:your_password@localhost:5432/inventoryDB
   ```

   - Initialize the database
   ```bash
   python db_create.py
   ```

   - Run the application
   ```bash
   python app.py
   ```

   - Access at [http://localhost:5000](http://localhost:5000)

### **Option 2: Fully Containerized (Docker for Everything)**

This approach uses Docker Compose to set up both the Flask application and PostgreSQL:

1. **Clone the repository**
   ```bash
   git clone https://github.com/LahiruCooray/inventory-management-flask-docker.git
   cd inventory-management-flask-docker
   ```

2. **Create a `.env` file with Docker network database connection:**
   ```
   FLASK_ENV=development
   DATABASE_URI=postgresql://db_username:db_password@db:5432/inventoryDB
   ```
   
   > **Important**: When using Docker Compose, use `db` as the host (service name) instead of `localhost` since services can reference each other by their service names in the Docker network.

3. **Build and run with Docker Compose**
   ```bash
   docker-compose up --build
   ```

4. **Access the application**
   - Go to [http://localhost:5000](http://localhost:5000)
   
5. **Stopping the containers**
   ```bash
   docker-compose down
   ```

6. **To remove volumes when stopping**
   ```bash
   docker-compose down -v
   ```


## **🛠 Installation Details**

### **Dependencies**

The application requires:
- Python 3.8+
- Flask
- SQLAlchemy
- psycopg2
- python-dotenv
- PostgreSQL 16.x


## **📂 Project Structure**

```
📚 inventory-management-flask-docker
️‍− 📚 app
️‍−    ├── 📚 static             # Static files (CSS file)
️‍−    ├── 📚 templates          # HTML templates
️‍−    ├── app.py                # Main application file
️‍−    ├── db_create.py          # Database initialization script
️‍− Dockerfile                # Docker setup
️‍− docker-compose.yml        # Docker Compose configuration
️‍− .gitignore                # Files to be ignored in Git
️‍− .dockerignore             # Files to be ignored by Docker
️‍− requirements.txt          # Python dependencies
️‍− README.md                 # Project documentation
```

---

## **🛠 API Endpoints**

| Endpoint | Method | Description |
|-----------------|--------|-------------|
| `/` | GET | View all inventory items |
| `/add` | POST | Add a new product |
| `/edit/<id>` | POST | Update or delete a product |
| `/search` | POST | Search for a product |

---

## **🐜 License**

This project is licensed under the MIT License.
