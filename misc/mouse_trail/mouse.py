import matplotlib.pyplot as plt

# Read the coordinates
with open('mouse_movements.txt', 'r') as f:
    coordinates = []
    for line in f:
        if ',' in line:
            x, y = map(int, line.strip().split(','))
            coordinates.append((x, y))

# Plot the coordinates
x_coords = [coord[0] for coord in coordinates]
y_coords = [coord[1] for coord in coordinates]

plt.figure(figsize=(15, 8))
plt.scatter(x_coords, y_coords, s=1, alpha=0.6)
plt.gca().invert_yaxis()  # Invert y-axis to match screen coordinates
plt.title('Mouse Movement Pattern')
plt.xlabel('X Coordinate')
plt.ylabel('Y Coordinate')
plt.show()

# Also try connecting the points in sequence
plt.figure(figsize=(15, 8))
plt.plot(x_coords, y_coords, linewidth=0.5, alpha=0.7)
plt.gca().invert_yaxis()
plt.title('Mouse Movement Path')
plt.xlabel('X Coordinate')
plt.ylabel('Y Coordinate')
plt.show()