from ultralytics import YOLO

# Use raw string or double backslashes for the file path
model = YOLO(r'models\best.pt')  # Option 1: Raw string
# model = YOLO('models\\best.pt')  # Option 2: Double backslashes

results = model.predict('input_videos/08fd33_4.mp4', save=True)
print(results[0])
print('--------------------------------------------------------------------------------')
for box in results[0].boxes:
    print(box)
