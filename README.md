# Variant Search API 🧬✨

A fast, efficient, and scalable API built with FastAPI and PostgreSQL to search through genetic variant data.

## Features 🚀

- **Fast Searches:** Utilizes PostgreSQL's advanced indexing for rapid querying.
- **Scalable:** Designed with scalability in mind to handle millions of rows.
- **Interactive Docs:** FastAPI provides automatic interactive API documentation.

## Getting Started 🛠

### Prerequisites

- Python 3.8 or newer
- PostgreSQL
- Pip

### Installation

1. **Clone the Repository**

```bash
git clone https://github.com/your_username/variant-search-api.git
cd variant-search-api
```

2. **Set Up a Virtual Environment**

```bash
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```

3. **Install Dependencies**

```bash
pip install -r requirements.txt
```

4. **Environment Variables**

Rename `.env.example` to `.env` and update the variables:

```
DATABASE_URL=postgresql+asyncpg://username:password@localhost/your_database_name
```

5. **Initialize the Database**

Ensure PostgreSQL is running and then:

```bash
alembic upgrade head
```

6. **Run the API**

```bash
uvicorn main:app --reload
```

Visit `http://localhost:8000` in your browser to see the API in action!

## Importing CSV Data into Dockerized Database

To import a CSV file into a Dockerized database, follow the provided steps:

```bash
# Step 1: Copy the CSV file into the Docker container.
docker cp /path/on/host/myfile.csv container_name:/path/in/container/myfile.csv

# Step 2: Connect to your database inside the Docker container.
docker exec -it container_name psql -U username -d databasename

# Inside the psql prompt, use the following SQL command to import the CSV:
COPY tablename FROM '/path/in/container/myfile.csv' DELIMITER ',' CSV HEADER;

# Exit the psql prompt.
\q
```
