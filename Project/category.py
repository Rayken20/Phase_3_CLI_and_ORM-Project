import sqlite3

CONN = sqlite3.connect('recipes.db')
CURSOR = CONN.cursor()

class Category:
    def __init__(self, name, description, id=None):
        self.id = id
        self.name = name
        self.description = description

    def __repr__(self):
        return f"<Category {self.id}: {self.name}, {self.description}>"

    def save(self):
        if self.id:
            self.update()
        else:
            sql = """
                INSERT INTO categories (name, description)
                VALUES (?, ?)
            """
            CURSOR.execute(sql, (self.name, self.description))
            CONN.commit()
            self.id = CURSOR.lastrowid

    def update(self):
        sql = """
            UPDATE categories
            SET name = ?, description = ?
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.name, self.description, self.id))
        CONN.commit()

    def delete(self):
        # Delete associated recipes first
        sql_delete_recipes = "DELETE FROM recipes WHERE category_id = ?"
        CURSOR.execute(sql_delete_recipes, (self.id,))
        # Delete the category itself
        sql_delete_category = "DELETE FROM categories WHERE id = ?"
        CURSOR.execute(sql_delete_category, (self.id,))
        CONN.commit()

    @classmethod
    def find_by_name(cls, name):
        sql = "SELECT * FROM categories WHERE name = ?"
        CURSOR.execute(sql, (name,))
        category_data = CURSOR.fetchone()
        if category_data:
            return cls(*category_data)
        else:
            return None

    @classmethod
    def find_by_id(cls, id_):
        sql = "SELECT * FROM categories WHERE id = ?"
        CURSOR.execute(sql, (id_,))
        category_data = CURSOR.fetchone()
        if category_data:
            return cls(*category_data)
        else:
            return None

    @classmethod
    def get_all(cls):
        sql = "SELECT * FROM categories"
        CURSOR.execute(sql)
        categories_data = CURSOR.fetchall()
        return [cls(*category_data) for category_data in categories_data]

    @classmethod
    def create(cls, name, description):
        category = cls(name, description)
        category.save()  # Use save method to insert into database
        return category
