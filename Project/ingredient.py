import sqlite3

# Database connection
CONN = sqlite3.connect('recipes.db')
CURSOR = CONN.cursor()

class Ingredient:
    def __init__(self, name, category, quantity, unit, id=None):
        self.id = id
        self.name = name
        self.category = category
        self.quantity = quantity
        self.unit = unit

    def __repr__(self):
        return f"<Ingredient {self.id}: {self.name}, {self.category}, {self.quantity}, {self.unit}>"

    def save(self):
        if self.id:
            self.update()
        else:
            sql = """
                INSERT INTO ingredients (name, category, quantity, unit)
                VALUES (?, ?, ?, ?)
            """
            CURSOR.execute(sql, (self.name, self.category, self.quantity, self.unit))
            CONN.commit()
            self.id = CURSOR.lastrowid

    def update(self):
        sql = """
            UPDATE ingredients
            SET name = ?, category = ?, quantity = ?, unit = ?
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.name, self.category, self.quantity, self.unit, self.id))
        CONN.commit()

    def delete(self):
        sql = """
            DELETE FROM ingredients
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.id,))
        CONN.commit()
