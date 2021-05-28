import pickle
import cv2
import numpy as np

def file_path_decode(file_path):
    stream = open(file_path.encode('utf-8'), 'rb')
    bytes = bytearray(stream.read())
    numpy_array = np.asarray(bytes, dtype=np.uint8)

    return cv2.imdecode(numpy_array, cv2.IMREAD_UNCHANGED)