This project analyzes the impact of PostgreSQL configuration settings on system performance by comparing well-configured and misconfigured environments under identical hardware conditions. Additionally, it explores the effects of parallel query execution on performance using Python.

📁 Project Structure
Two virtual machines are set up using Oracle VirtualBox.

PostgreSQL 17 is installed on both machines.

One machine is configured with optimal settings (based on hardware).

The other machine is deliberately misconfigured to simulate performance issues.

🖥️ System Specifications
Each virtual machine is provisioned with:

8 GB RAM

4 CPU cores

100 GB SSD

Ubuntu 22.04 LTS

PostgreSQL 17

⚙️ Configuration Details
Proper Configuration (Server A)
Key parameters were optimized using PGTune, including:

plaintext
Copy
Edit
shared_buffers = 2GB
work_mem = 64MB
effective_cache_size = 6GB
max_connections = 100
wal_buffers = 16MB
checkpoint_completion_target = 0.9
Improper Configuration (Server B)
Deliberately inefficient settings were applied:

plaintext
Copy
Edit
shared_buffers = 16MB
work_mem = 1MB
effective_cache_size = 512MB
max_connections = 1000
wal_buffers = 256kB
checkpoint_completion_target = 0.1
🧪 Test Dataset
A synthetic user table with 10 million rows was generated using PostgreSQL’s generate_series() function:

sql
Copy
Edit
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    name TEXT,
    surname TEXT,
    email TEXT,
    birth_date DATE,
    created_at TIMESTAMP
);
🧾 Query Types
The following types of queries were executed:

Search by ID

Search by email

Filter by birth date range

Group and order by surname

⚡ Parallel Query Execution
Using Python’s concurrent.futures.ThreadPoolExecutor, both sequential and parallel executions of user ID queries were performed. Two test scripts were developed:

test_sequential.py: Executes queries one by one.

test_parallel.py: Executes queries in parallel using 10 threads.

🧰 Tools Used
PostgreSQL 17

Python 3

psycopg2 for PostgreSQL connections

concurrent.futures for parallelism

top and htop for resource monitoring
