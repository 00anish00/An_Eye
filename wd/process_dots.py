import time

def dots():
    column = 12
    row = 1
    # Create the visual representation
    for row in range(row):
        for col in range(column):
            time.sleep(0.001)
            print("('.')......", end="")
