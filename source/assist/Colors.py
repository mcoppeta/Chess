# All - None
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Primary
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Secondary
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
PINK = (255, 0, 255)

# Major
ORANGE = (255, 128, 0)
PURPLE = (127, 0, 255)
GRAY = GREY = (128, 128, 128)
BROWN = (102, 51, 0)

# Lists
ALL_COLORS = [BLACK, WHITE, RED, GREEN, BLUE, YELLOW, CYAN, PINK, ORANGE, PURPLE, GRAY, BROWN]
NO_EXTREMES = []
for i in range(2, len(ALL_COLORS)):
    NO_EXTREMES.append(ALL_COLORS[i])
