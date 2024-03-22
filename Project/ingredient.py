import sqlite3

# Database connection
CONN = sqlite3.connect('recipes.db')
CURSOR = CONN.cursor()

class Ingredient:
    def __init__(self, name, category, quantity, unit, recipe_id, id=None):
        self.id = id
        self.name = name
        self.category = category
        self.quantity = quantity
        self.unit = unit
        self.recipe_id = recipe_id

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

    @classmethod
    def create(cls, name, category, quantity, unit, recipe_id):
        ingredient = cls(name, category, quantity, unit, recipe_id)
        ingredient.save()
        return ingredient

    
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

    @classmethod
    def find_by_name(cls, name):
        sql = "SELECT * FROM ingredients WHERE name = ?"
        CURSOR.execute(sql, (name,))
        ingredient_data = CURSOR.fetchone()
        if ingredient_data:
            return cls(*ingredient_data)
        else:
            return None
    @classmethod
    def find_by_id(cls, id_):
        sql = "SELECT * FROM ingredients WHERE id = ?"
        CURSOR.execute(sql, (id_,))
        ingredient_data = CURSOR.fetchone()
        if ingredient_data:
            return cls(*ingredient_data)
        else:
            return None
        
    @classmethod
    def get_all(cls):
        sql = "SELECT * FROM ingredients"
        CURSOR.execute(sql)
        ingredients_data = CURSOR.fetchall()
        return [cls(*ingredient_data) for ingredient_data in ingredients_data]
