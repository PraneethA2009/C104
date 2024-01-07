import cv2


img = cv2.imread("solar-system.jpg")


def add_text(img, text, position, font_size, color):
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(img, text, position, font, font_size, color, 2, cv2.LINE_AA)


add_text(img, "Mercury", (50, 50), 1, (255, 255, 255))
add_text(img, "Venus", (150, 150), 1, (255, 255, 255))
add_text(img, "Earth", (250, 250), 1, (255, 255, 255))
add_text(img, "Mars", (350, 350), 1, (255, 255, 255))
add_text(img, "Jupiter", (450, 450), 1, (255, 255, 255))
add_text(img, "Saturn", (550, 550), 1, (255, 255, 255))
add_text(img, "Uranus", (650, 650), 1, (255, 255, 255))
add_text(img, "Neptune", (750, 750), 1, (255, 255, 255))

cv2.imshow("output", img)
cv2.waitKey(0)

cv2.imwrite("Solar_system_with_name.jpg", img)
