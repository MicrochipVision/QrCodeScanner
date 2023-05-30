import cv2
from pyzbar.pyzbar import decode

# Load the video capture
cap = cv2.VideoCapture(0)

while True:
    # Read a frame from the video capture
    ret, frame = cap.read()
    
    # Flip the frame horizontally
    frame = cv2.flip(frame, 1)

    # Decode any QR codes or barcodes in the frame
    decoded_objs = decode(frame)

    # Loop through each decoded object
    for obj in decoded_objs:
        # Print the barcode or QR code data
        print('Type:', obj.type)
        print('Data:', obj.data)

        # Get the location of the barcode or QR code
        rect = obj.rect
        x, y, w, h = rect.left, rect.top, rect.width, rect.height

        # Draw a rectangle around the barcode or QR code
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 3)

    # Display the image with barcodes and QR codes highlighted
    cv2.imshow('Barcode and QR code scannerusing PyZbar', frame)
    
    # Check if the 'q' key was pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture and close all windows
cap.release()
cv2.destroyAllWindows()
