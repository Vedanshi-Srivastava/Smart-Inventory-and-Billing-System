import psycopg2

def connection():
    con = psycopg2.connect(
        host = "localhost",
        database = "ecommerce",
        user = "postgres",
        password = "Gungun@31",
        port = "5432",
    )

    if con : 
        print(">>>>> Connection Established!")
    else:
        print(">>>>> Connection Failed!")
    return con

conn = connection()
    