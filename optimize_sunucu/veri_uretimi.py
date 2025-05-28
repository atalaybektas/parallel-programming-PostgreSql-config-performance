import psycopg2

DB_CONFIG = {
    'host': 'localhost',
    'port': 5432,
    'dbname': 'postgres',
    'user': 'postgres',
    'password': 'password'
}

create_table_sql = """
CREATE TABLE IF NOT EXISTS kullaniciler (
    id SERIAL PRIMARY KEY,
    name TEXT,
    surname TEXT,
    eposta TEXT,
    dogum_tarihi DATE,
    olusturma_zamani TIMESTAMP
);
"""

insert_sql = """
INSERT INTO kullaniciler (name, surname, eposta, dogum_tarihi, olusturma_zamani)
SELECT
    'Ad_' || floor(random() * 10000000),
    'Soyad_' || floor(random() * 10000000),
    'eposta_' || floor(random() * 10000000) || '@example.com',
    CURRENT_DATE - (floor(random() * 3650) * INTERVAL '1 day'),
    CURRENT_TIMESTAMP - (floor(random() * 1000000) * INTERVAL '1 second')
FROM generate_series(1, 10000000);
"""

conn = psycopg2.connect(**DB_CONFIG)
cur = conn.cursor()

# Tabloyu oluştur
cur.execute(create_table_sql)
conn.commit()

# 10 milyon kaydı ekle
cur.execute(insert_sql)
conn.commit()

cur.close()
conn.close()
print("Tablo oluşturuldu ve 10 milyon kayıt eklendi.")
