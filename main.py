from Library import Ring
import random

something = Ring("ring", "png", "arrow.png")
something.create_files(1)
N = something.create_pro_video(random.randint(0, 360), 45, [[60, 5], [60, 4], [60, 3], [60, 2], [60, 1], [20, 0]])
print("Result of ring:", N)
