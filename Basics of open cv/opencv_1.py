import cv2

# Load the image
im = cv2.imread('chessboard.png', -1)

# Check if the image was successfully loaded
if im is not None:
    # Resize the image
    im = cv2.resize(im, (640, 640))

    # Rotate the image
    im = cv2.rotate(im, cv2.ROTATE_180)

    # Display the image
    cv2.imshow('image', im)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Error: Unable to load the image.")
