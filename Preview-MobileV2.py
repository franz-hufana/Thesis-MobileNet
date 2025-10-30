import os
import numpy as np
from keras.applications.mobilenet_v2 import MobileNetV2

model = MobileNetV2(weights = 'imagenet')

model.summary()