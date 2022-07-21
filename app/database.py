import os
import sys
from sqlalchemy import create_engine, text

URL_DB = os.getenv('URL_DB')

def query_db(depth, gradient):
    engine = create_engine(URL_DB)

    query = text("""
    SELECT latitude, longitude, depth, gradient
    FROM wells
    WHERE depth > :foobar AND gradient > :gradient;
    """)

    with engine.connect() as conn:
        results = conn.execute(query, foobar=depth, gradient=gradient).fetchall()

    return results

if __name__ == '__main__':
    depth = sys.argv[1]
    gradient = sys.argv[2]
    print(query_db(depth, gradient))
