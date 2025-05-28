import psycopg2
import time

# Generate a list of 10 different user IDs to query
ids = list(range(1000000, 1000011)

# Establish a single connection to the PostgreSQL database
conn = psycopg2.connect(
    dbname="postgres",
    user="postgres",
    password="password",
    host="localhost",
    port="5432"
)
cur = conn.cursor()

# Start time measurement
start = time.time()

# Perform queries sequentially (one after another)
for id in ids:
    cur.execute("SELECT * FROM kullanicilar WHERE id = %s", (id,))
    cur.fetchone()  # Fetch the result (not stored or printed)

# End time measurement
end = time.time()

print(f"Total time spent for sequential test: {end - start:.2f} seconds")

# Close the cursor and the database connection
cur.close()
conn.close()