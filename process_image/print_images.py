import cv2 as cv

def show_image(text, image):
    cv.imshow(text, image)
    cv.waitKey()
    pass


def draw_contours(contours, gray):
    for i in contours:
        M = cv.moments(i)
        if M['m00'] != 0:
            cx = int(M['m10'] / M['m00'])
            cy = int(M['m01'] / M['m00'])
            cv.drawContours(gray, [i], -1, (0, 255, 0), 2)
            cv.circle(gray, (cx, cy), 7, (0, 0, 255), -1)
            cv.putText(gray, "center", (cx - 20, cy - 20),
                        cv.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2)

    cv.imshow("Gray Image with Contours", gray)
    cv.waitKey()


def draw_borders(borders, gray):

    for border in borders:
        start_point = (border[1], border[2])
        end_point = (border[3], border[4])
        cv.rectangle(gray, start_point, end_point, (0, 0, 0), 1)

    cv.imshow("Gray Image with Borders", gray)
    cv.waitKey()