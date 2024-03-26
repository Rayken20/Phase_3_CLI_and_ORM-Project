import sqlite3

CONN = sqlite3.connect('recipes.db')
CURSOR = CONN.cursor()

class Category:
    def __init__(self, name, description, id=None):
        self.id = id
        self.name = name
        self.description = description
        self.recipe= []

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

    ## Perfom CRUD Operations
    @classmethod
    def create(cls, name, description):
        existing_category = cls.find_by_name(name)
        if existing_category:
            print(f"Category '{name}' already exists.")
            return existing_category
        else:
            try:
                 category = cls(name, description)
                 category.save()  
                 return category
            except Exception as exc:
                 print("Error creating category: ", exc)



    def update(self):
        """Updates the category's information in the database."""
        try:
            sql = """
                UPDATE categories
                SET name = ?, description = ?
                WHERE id = ?
            """
            CURSOR.execute(sql, (self.name, self.description, self.id))
            CONN.commit()
            print(f"Category with id {self.id} updated successfully.")
            return True
        except Exception as exc:
            print(f"Error updating category with id {self.id}: {exc}")
            return False
        
    @classmethod
    def delete(cls, category_id):
        """Deletes a category with the given ID from the database."""
        try:
            sql_delete_category = "DELETE FROM categories WHERE id = ?"
            CURSOR.execute(sql_delete_category, (category_id,))
            CONN.commit()
            return True 
        except Exception as exc:
            print(f"Error deleting category with id {category_id}: {exc}")
            return False

    ##Find by attributes
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
    
    ##Showcase one-to-many relationships    
    def list_recipes(self):
        """Lists all recipes associated with the category."""        
        sql = "SELECT * FROM recipes WHERE category_id = ?"
        CURSOR.execute(sql, (self.id,))
        recipes_data = CURSOR.fetchall()
        recipes = [Recipe(*recipe_data) for recipe_data in recipes_data] 
        return recipes
    
   

from recipe import Recipe