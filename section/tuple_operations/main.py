# Initial items on shelf #1 (provided as a tuple)
shelf1 = ("celery", "spinach", "cucumbers")

# Items being added to the shelf #1 (provided as a list)
shelf1_update = ["tomatoes", "celery", "cilantro"]

# 1. Convert list to tuple
shelf1_update_tuple = tuple(shelf1_update)

# 2. Concatenate tuples
shelf1_concat = shelf1 + shelf1_update_tuple

# 3. Count occurrences of "celery"
celery_count = shelf1_concat.count("celery")

# 4. Find index of first "celery"
celery_index = shelf1_concat.index("celery")

# Output
print("Updated Shelf #1:", shelf1_concat)
print("Number of Celery:", celery_count)
print("Celery Index:", celery_index)