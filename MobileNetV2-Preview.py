from tensorflow.keras.applications import MobileNetV2

model = MobileNetV2(weights="imagenet")
model.summary