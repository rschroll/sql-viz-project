import sys
from sqlalchemy import create_engine

def query_db(depth, gradient, conn_str):
    engine = create_engine(conn_str)

    query = f"""
    SELECT latitude, longitude, depth, gradient
    FROM wells
    WHERE depth > {depth} AND gradient > {gradient};
    """

    with engine.connect() as conn:
        results = conn.execute(query).fetchall()

    return results

if __name__ == '__main__':
    depth = sys.argv[1]
    gradient = sys.argv[2]
    conn_str = sys.argv[3]
    print(query_db(depth, gradient, conn_str))
