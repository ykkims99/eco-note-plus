# video_enhancer.py
# Eco-Note+ video enhancement script using ONNX Runtime

import onnxruntime as ort
import numpy as np
import cv2

def enhance_video(frame_path, model_path='models/onnx/esrgan_lite.onnx'):
    sess = ort.InferenceSession(model_path)
    frame = cv2.imread(frame_path)
    frame = cv2.resize(frame, (128, 128))
    input_image = np.transpose(frame, (2, 0, 1)).astype(np.float32) / 255.0
    input_image = input_image[np.newaxis, :]
    result = sess.run(None, {sess.get_inputs()[0].name: input_image})[0]
    output = np.clip(result[0].transpose(1, 2, 0) * 255, 0, 255).astype(np.uint8)
    cv2.imwrite("enhanced_output.jpg", output)
    print("Enhanced frame saved as 'enhanced_output.jpg'")

if __name__ == "__main__":
    enhance_video("test_image.jpg")
