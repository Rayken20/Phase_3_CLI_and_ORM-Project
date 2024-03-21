import sqlite3

# Database connection
CONN = sqlite3.connect('recipes.db')
CURSOR = CONN.cursor()

# Create tables
CURSOR.execute("""
    CREATE TABLE IF NOT EXISTS recipes (
        id INTEGER PRIMARY KEY,
        name TEXT,
        description TEXT,
        ingredients TEXT,
        instructions TEXT,
        category_id INTEGER,
        FOREIGN KEY (category_id) REFERENCES categories(id)
    )
""")

CURSOR.execute("""
    CREATE TABLE IF NOT EXISTS ingredients (
        id INTEGER PRIMARY KEY,
        name TEXT,
        category TEXT,
        quantity REAL,
        unit TEXT
    )
""")

CURSOR.execute("""
    CREATE TABLE IF NOT EXISTS categories (
        id INTEGER PRIMARY KEY,
        name TEXT,
        description TEXT
    )
""")

# Insert sample data into categories table
CURSOR.execute("""
    INSERT INTO categories (name, description) VALUES
    ('Breakfast', 'Recipes suitable for breakfast'),
    ('Lunch', 'Recipes suitable for lunch'),
    ('Dinner', 'Recipes suitable for dinner')
""")

# Insert sample data into ingredients table
CURSOR.executemany("""
    INSERT INTO ingredients (name, category, quantity, unit) VALUES (?, ?, ?, ?)
""", [
    ('Eggs', 'Protein', 2, 'pieces'),
    ('Bacon', 'Protein', 3, 'slices'),
    ('Tomato', 'Vegetable', 1, 'piece'),
    ('Bread', 'Grain', 2, 'slices'),
    ('Lettuce', 'Vegetable', 1, 'cup'),
    ('Chicken Breast', 'Protein', 1, 'piece'),
    ('Rice', 'Grain', 1, 'cup'),
    ('Broccoli', 'Vegetable', 1, 'cup'),
    ('Salmon Fillet', 'Protein', 1, 'piece')
])

# Insert sample data into recipes table
CURSOR.executemany("""
    INSERT INTO recipes (name, description, ingredients, instructions, category_id) VALUES (?, ?, ?, ?, ?)
""", [
    ('Scrambled Eggs', 'Classic breakfast dish', 'Eggs, Bacon, Tomato', '1. Beat eggs. 2. Cook bacon. 3. Add tomatoes to the pan. 4. Add eggs and scramble.', 1),
    ('BLT Sandwich', 'Classic lunch option', 'Bacon, Lettuce, Tomato, Bread', '1. Toast bread. 2. Add lettuce, tomato, and bacon. 3. Close sandwich and serve.', 2),
    ('Grilled Chicken with Rice', 'Simple dinner recipe', 'Chicken Breast, Rice, Broccoli', '1. Season chicken and grill. 2. Cook rice. 3. Steam broccoli. 4. Serve together.', 3),
    ('Salmon with Roasted Vegetables', 'Healthy dinner option', 'Salmon Fillet, Broccoli, Tomato', '1. Season salmon and bake. 2. Roast vegetables. 3. Serve together.', 3)
])

CONN.commit()

# Close connection
CONN.close()