import numpy as np

# An image is just this --a grid of numbers
arr = np.array(
	[[1, 2, 3],
	[4, 5, 6],
	[7, 8, 9]]
	)

"""print(arr.shape)
print(arr[1, 2])
print(arr[:, 1])
print(arr * 2)
print(arr.dtype)
print(arr[0:2, 0:2])
"""

image = np.random.randint(0, 256, size=(5,5), dtype=np.uint8)
print("Image:\n", image)
print("Shape:",image.shape)
print("Dtype:",image.dtype)
print("Top left 3x3 crop:\n", image[0:3, 0:3])
print("Max brightness:", np.max(image))
print("Min brightness:", np.min(image))
print("Mean brightness", np.mean(image))
