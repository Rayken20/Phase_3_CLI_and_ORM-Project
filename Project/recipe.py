import sqlite3

# Database connection
CONN = sqlite3.connect('recipes.db')
CURSOR = CONN.cursor()

class Recipe:
    def __init__(self, name, description, ingredients, instructions, category, id=None):
        self.id = id
        self.name = name
        self.description = description
        self.ingredients = ingredients
        self.instructions = instructions
        self.category = category

    def __repr__(self):
        return f"<Recipe {self.id}: {self.name}, {self.description}, {self.category}>"

    def save(self):
        if self.id:
            self.update()
        else:
            sql = """
                INSERT INTO recipes (name, description, ingredients, instructions, category)
                VALUES (?, ?, ?, ?, ?)
            """
            CURSOR.execute(sql, (self.name, self.description, self.ingredients, self.instructions, self.category))
            CONN.commit()
            self.id = CURSOR.lastrowid

    def update(self):
        sql = """
            UPDATE recipes
            SET name = ?, description = ?, ingredients = ?, instructions = ?, category = ?
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.name, self.description, self.ingredients, self.instructions, self.category, self.id))
        CONN.commit()

    def delete(self):
        sql = """
            DELETE FROM recipes
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.id,))
        CONN.commit()
