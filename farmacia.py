import sqlite3

conexion = sqlite3.connect('farmacia.db')
cursor = conexion.cursor()


cursor.execute('''
    CREATE TABLE IF NOT EXISTS clientes (
        id_cliente INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        telefono TEXT
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS productos (
        id_producto INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        precio REAL NOT NULL,
        stock INTEGER NOT NULL
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS ventas (
        id_venta INTEGER PRIMARY KEY AUTOINCREMENT,
        id_cliente INTEGER,
        id_producto INTEGER,
        cantidad INTEGER NOT NULL,
        fecha TEXT NOT NULL,
        FOREIGN KEY (id_cliente) REFERENCES clientes (id_cliente),
        FOREIGN KEY (id_producto) REFERENCES productos (id_producto)
    )
''')

cursor.execute("INSERT INTO clientes (nombre, telefono) VALUES ('Carlos Gómez', '12213265')")
cursor.execute("INSERT INTO clientes (nombre, telefono) VALUES ('María López', '95836411')")

cursor.execute("INSERT INTO productos (nombre, precio, stock) VALUES ('Paracetamol 500mg', 1.50, 100)")
cursor.execute("INSERT INTO productos (nombre, precio, stock) VALUES ('Ibuprofeno 400mg', 2.00, 50)")
