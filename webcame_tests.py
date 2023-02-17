import cv2
import numpy as np
import webbrowser

cap = cv2.VideoCapture(0) # 0 is the index of the default camera

# Define a "Z" pattern
pattern = np.array([(-0.4, -0.4), (0.4, -0.4), (0.4, 0.0), (-0.4, 0.0), (-0.4, 0.4), (0.4, 0.4)])

# Define a maximum distance from each point on the pattern for a match
max_distance = 30

# Set the contrast level (value between 0 and 100)
contrast_level = 70

# Define a list to track the activated points on the pattern
activated_points = []

# Define colors for the points
inactive_color = (0, 0, 255)  # Red
active_color = (0, 255, 0)  # Green

def activated_a_point(a_point):
    print(f"Activated {a_point}!")

def spell_is_cast():
    print("SPELL CAST")
    url = "https://media3.giphy.com/media/eax0rh3OERAYg/giphy.gif?cid=ecf05e47tncjm1pc7b8f79db5m2bjjl0alowlozizgru3y2f&rid=giphy.gif&ct=g"
    webbrowser.open(url)

while True:
    ret, frame = cap.read()

    if not ret:
        break

    # Flip the frame horizontally
    frame = cv2.flip(frame, 1)

    # Adjust the contrast of the frame
    alpha = (contrast_level + 127) / 127
    adjusted_frame = cv2.convertScaleAbs(frame, alpha=alpha, beta=-contrast_level)

    gray = cv2.cvtColor(adjusted_frame, cv2.COLOR_BGR2GRAY)
    ret, thresh = cv2.threshold(gray, 200, 255, cv2.THRESH_BINARY)
    contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    # Loop through the contours to find the white dot and check for a match with the pattern
    for cnt in contours:
        (x, y), radius = cv2.minEnclosingCircle(cnt)
        center = (int(x), int(y))
        radius = int(radius)

        # Draw the circle around the white dot
        cv2.circle(adjusted_frame, center, radius, (0, 255, 0), 2)

        # Check if the position of the white dot is close enough to the current point on the pattern
        if len(pattern) > 0 and len(activated_points) < len(pattern):
            # Get the next point on the pattern to activate
            next_point = pattern[len(activated_points)]

            # Scale the pattern point to the size of the frame
            height, width, _ = adjusted_frame.shape
            scaled_point = np.round((next_point + 0.5) * np.array([width, height])).astype(int)

            distance = np.sqrt(np.sum((scaled_point - center)**2))

            if distance <= max_distance:
                activated_points.append(next_point)

    # Draw the points on the pattern
    for i, point in enumerate(pattern):
        # Offset the point from the edge of the frame for visibility
        x = int((point[0] + 0.5) * (adjusted_frame.shape[1] - 100) + 50)
        y = int((point[1] + 0.5) * (adjusted_frame.shape[0] - 100) + 50)

        # Change the color of the point based on its activation status
        color = active_color if any(np.array_equal(point, activated_point) for activated_point in activated_points) else inactive_color

        cv2.circle(adjusted_frame, (x, y), 5, color, -1)

    # show video
    cv2.imshow('frame', adjusted_frame)

    # Check if the pattern has been fully activated
    if len(activated_points) == len(pattern):
        spell_cast = spell_is_cast()
        break

    # break with "Q"
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


    # Check if the pattern has been fully activated
    if len(activated_points) == len(pattern):
        spell_cast = spell_is_cast()
    

        # Release the capture and close the window
        cap.release()
        cv2.destroyAllWindows()
