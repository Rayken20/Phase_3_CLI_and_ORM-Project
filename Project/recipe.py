import sqlite3

# Database connection
CONN = sqlite3.connect('recipes.db')
CURSOR = CONN.cursor()

class Recipe:
    def __init__(self, name, description, ingredients, instructions, category_id, id=None):
        self.id = id
        self.name = name
        self.description = description
        self.ingredients = ingredients
        self.instructions = instructions
        self.category_id = category_id

    def __repr__(self):
        return f"<Recipe {self.id}: {self.name}, {self.description}, {self.category_id}>"

    def save(self):
        if self.id:
            self.update()
        else:
            sql = """
                INSERT INTO recipes (name, description, ingredients, instructions, category_id)
                VALUES (?, ?, ?, ?, ?)
            """
            CURSOR.execute(sql, (self.name, self.description, self.ingredients, self.instructions, self.category_id))
            CONN.commit()
            self.id = CURSOR.lastrowid

    def update(self):
        sql = """
            UPDATE recipes
            SET name = ?, description = ?, ingredients = ?, instructions = ?, category_id = ?
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.name, self.description, self.ingredients, self.instructions, self.category_id, self.id))
        CONN.commit()

    def delete(self):
        sql = """
            DELETE FROM recipes
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.id,))
        CONN.commit()

    @classmethod
    def list_all(cls):
        sql = "SELECT * FROM recipes"
        CURSOR.execute(sql)
        recipes_data = CURSOR.fetchall()
        return [cls(*recipe_data) for recipe_data in recipes_data]

    @classmethod
    def find_by_name(cls, name):
        sql = "SELECT * FROM recipes WHERE name = ?"
        CURSOR.execute(sql, (name,))
        recipe_data = CURSOR.fetchone()
        if recipe_data:
            return cls(*recipe_data)
        else:
            return None

    @classmethod
    def find_by_id(cls, id_):
        sql = "SELECT * FROM recipes WHERE id = ?"
        CURSOR.execute(sql, (id_,))
        recipe_data = CURSOR.fetchone()
        if recipe_data:
            return cls(*recipe_data)
        else:
            return None

    @classmethod
    def create(cls, name, description, ingredients, instructions, category_id):
        recipe = cls(name, description, ingredients, instructions, category_id)
        recipe.save()
        return recipe

    @classmethod
    def list_by_category(cls, category_id):
        sql = "SELECT * FROM recipes WHERE category_id = ?"
        CURSOR.execute(sql, (category_id,))
        recipes_data = CURSOR.fetchall()
        return [cls(*recipe_data) for recipe_data in recipes_data]
