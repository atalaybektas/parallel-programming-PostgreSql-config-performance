import psycopg2
import time
from concurrent.futures import ThreadPoolExecutor


ids = list(range(1000000, 1000011)


def fetch_user(id):
    
    conn = psycopg2.connect(
        dbname="postgres",
        user="postgres",
        password="password",
        host="localhost",
        port="5432"
    )
    cur = conn.cursor()

    
    cur.execute("SELECT * FROM kullanicilar WHERE id = %s", (id,))
    cur.fetchone() 

    
    cur.close()
    conn.close()

# Start time measurement
start = time.time()

# Use ThreadPoolExecutor to run queries in parallel (10 threads)
with ThreadPoolExecutor(max_workers=10) as executor:
    executor.map(fetch_user, ids)

# End time measurement
end = time.time()
print(f"Total time spent for parallel test: {end - start:.2f} seconds")