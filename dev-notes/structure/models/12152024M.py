# users handles user authentication
# Contains the UserProfile model for storing user-specific data

# users/models.py
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    weight = models.DecimalField(max_digits=5, decimal_places=2)
    height = models.DecimalField(max_digits=5, decimal_places=2)
    activity_level = models.CharField(max_length=20, choices=ACTIVITY_CHOICES)
    daily_calorie_needs = models.IntegerField()

# goals manages fitness goals and tracking
# Contains models for different types of goals, and progress

# goals/models.py
class Goal(models.Model):
    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    goal_type = models.CharField(max_length=50, choices=GOAL_CHOICES)
    target_weight = models.DecimalField(max_digits=5, decimal_places=2)
    weekly_goal = models.DecimalField(max_digits=3, decimal_places=1)  # kg/week
    start_date = models.DateField()
    target_date = models.DateField()

# nutrition handles food items and their nutritional information
# Manages the food database and calculations

#nutrition/models.py
class Food(models.Model):
    name = models.CharField(max_length=200)
    brand = models.CharField(max_length=200, blank=True)
    serving_size = models.DecimalField(max_digits=6, decimal_places=2)
    serving_unit = models.CharField(max_length=20)

class NutritionInfo(models.Model):
    food = models.OneToOneField(Food, on_delete=models.CASCADE)
    calories_per_100g = models.DecimalField(max_digits=6, decimal_places=2)
    protein_per_100g = models.DecimalField(max_digits=6, decimal_places=2)
    carbs_per_100g = models.DecimalField(max_digits=6, decimal_places=2)
    fats_per_100g = models.DecimalField(max_digits=6, decimal_places=2)
    fiber_per_100g = models.DecimalField(max_digits=6, decimal_places=2)

# meals handles meal planning and tracking
# Manages daily meal schedules and portions

# meals/models.py
class MealPlan(models.Model):
    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    meals_per_day = models.IntegerField()
    total_calories = models.DecimalField(max_digits=7, decimal_places=2)
    total_protein = models.DecimalField(max_digits=6, decimal_places=2)
    total_carbs = models.DecimalField(max_digits=6, decimal_places=2)
    total_fats = models.DecimalField(max_digits=6, decimal_places=2)

class Meal(models.Model):
    meal_plan = models.ForeignKey(MealPlan, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    meal_time = models.TimeField()
    total_calories = models.DecimalField(max_digits=7, decimal_places=2)

class MealFood(models.Model):
    meal = models.ForeignKey(Meal, on_delete=models.CASCADE)
    food = models.ForeignKey(Food, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=6, decimal_places=2)  # in grams