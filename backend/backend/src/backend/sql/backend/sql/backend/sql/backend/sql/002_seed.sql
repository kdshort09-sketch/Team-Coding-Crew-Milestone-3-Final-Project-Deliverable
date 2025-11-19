INSERT INTO users (email, password_hash, display_name)
VALUES
('demo@mealmaster.app', 'hashedpassword', 'Demo User');

INSERT INTO ingredients (name)
VALUES ('egg'), ('milk'), ('flour'), ('sugar'), ('salt'), ('butter');

INSERT INTO recipes (user_id, title, description, steps)
VALUES 
(1, 'Pancakes', 'Simple pancake recipe.', 'Mix ingredients and cook on griddle');

INSERT INTO recipe_ingredients (recipe_id, ingredient_id, quantity)
VALUES
(1, 1, '2'),
(1, 2, '1 cup'),
(1, 3, '1 cup'),
(1, 6, '2 tbsp');
