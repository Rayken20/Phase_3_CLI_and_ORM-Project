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
        unit TEXT,
        recipe_id INTEGER,
        FOREIGN KEY (recipe_id) REFERENCES recipes(id)
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
categories_data = [
    ('Breakfast', 'Recipes suitable for breakfast'),
    ('Lunch', 'Recipes suitable for lunch'),
    ('Dinner', 'Recipes suitable for dinner')
]

CURSOR.executemany("""
    INSERT INTO categories (name, description) VALUES (?, ?)
""", categories_data)

# Insert sample data into ingredients table
ingredients_data = [
    ('Eggs', 'Protein', 2, 'pieces'),
    ('Bacon', 'Protein', 3, 'slices'),
    ('Tomato', 'Vegetable', 1, 'piece'),
    ('Bread', 'Grain', 2, 'slices'),
    ('Lettuce', 'Vegetable', 1, 'cup'),
    ('Chicken Breast', 'Protein', 1, 'piece'),
    ('Rice', 'Grain', 1, 'cup'),
    ('Broccoli', 'Vegetable', 1, 'cup'),
    ('Salmon Fillet', 'Protein', 1, 'piece')
]

CURSOR.executemany("""
    INSERT INTO ingredients (name, category, quantity, unit) VALUES (?, ?, ?, ?)
""", ingredients_data)

# Insert sample data into recipes table
recipes_data = [
    ('Scrambled Eggs', 'Classic breakfast dish', '1. Beat eggs. 2. Cook bacon. 3. Add tomatoes to the pan. 4. Add eggs and scramble.', 1),
    ('BLT Sandwich', 'Classic lunch option', '1. Toast bread. 2. Add lettuce, tomato, and bacon. 3. Close sandwich and serve.', 2),
    ('Grilled Chicken with Rice', 'Simple dinner recipe', '1. Season chicken and grill. 2. Cook rice. 3. Steam broccoli. 4. Serve together.', 3),
    ('Salmon with Roasted Vegetables', 'Healthy dinner option', '1. Season salmon and bake. 2. Roast vegetables. 3. Serve together.', 4)
]

CURSOR.executemany("""
    INSERT INTO recipes (name, description, instructions, category_id) VALUES (?, ?, ?, ?)
""", recipes_data)

# Update recipe IDs in ingredients table
CURSOR.execute("""
    UPDATE ingredients
    SET recipe_id = (
        SELECT id FROM recipes WHERE recipes.name || ' ' || recipes.description LIKE '%' || ingredients.name || '%'
    )
""")

CONN.commit()

# Close connection
CONN.close()
