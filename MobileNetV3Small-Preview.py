from tensorflow.keras.applications import MobileNetV3Small

model = MobileNetV3Small(weights = 'imagenet')
model.summary()