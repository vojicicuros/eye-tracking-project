import cv2

# Try different camera indexes (0, 1, 2) if needed
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)  # Use CAP_DSHOW for Windows, remove it for Linux/macOS

if not cap.isOpened():
    print("❌ Error: Camera not detected.")
    exit()

# Set resolution (Optional, adjust based on your C920 settings)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

print("✅ Camera initialized. Press 'Q' to exit.")

while True:
    ret, frame = cap.read()

    if not ret:
        print("❌ Failed to grab frame.")
        break

    cv2.imshow("Live Camera Feed - Logitech C920", frame)

    # Press 'q' to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        print("🔴 Exiting...")
        break

# Release resources
cap.release()
cv2.destroyAllWindows()
