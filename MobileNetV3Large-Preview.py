from tensorflow.keras.applications import MobileNetV3Large

model = MobileNetV3Large(weights = 'imagenet')
model.summary()