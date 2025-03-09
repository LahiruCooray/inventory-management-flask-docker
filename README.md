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

## **🛠 Installation**
### **1️⃣ Clone the repository**
```bash
git clone https://github.com/LahiruCooray/inventory-management-flask-docker.git
cd inventory-management-flask-docker
```

### **2️⃣ Create and activate a virtual environment (optional but recommended)**
```bash
python3 -m venv venv
source venv/bin/activate   # On macOS/Linux
venv\Scripts\activate      # On Windows
```

### **3️⃣ Install dependencies**
```bash
pip install -r requirements.txt
```

### **4️⃣ Setup environment variables**
Create a `.env` file in the project root and configure necessary environment variables:  
```ini
FLASK_ENV=development
DATABASE_URI=postgresql://your_username:your_password@localhost/your_database

```

### **5️⃣ Initialize the database**
```bash
python db_create.py
```

---

## **🐳 Running with Docker**
### **1️⃣ Build and run the Docker container**
```bash
docker-compose up --build
```

### **2️⃣ Access the app**
Go to: **[http://localhost:5000](http://localhost:5000)**  

---

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
| Endpoint         | Method | Description |
|-----------------|--------|-------------|
| `/`             | GET    | View all inventory items |
| `/add`          | POST   | Add a new product |
| `/edit/<id>`    | POST   | Update or delete a product |
| `/search`       | POST   | Search for a product |

---

## **🚀 Usage**
1️⃣ **Run the app locally**  
```bash
python app.py
```
2️⃣ Open **http://localhost:5000** in your browser  
3️⃣ Manage inventory items with CRUD operations  

---

## **🐜 License**
This project is licensed under the MIT License.  


