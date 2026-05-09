from scipy.io import loadmat
import numpy as np
import os

input_dir = "data/input"

for fname in os.listdir(input_dir):
    if not fname.endswith(".mat"):
        continue
    path = os.path.join(input_dir, fname)
    data = loadmat(path)
    print(f"\n--- {fname} ---")
    for key, value in data.items():
        if key.startswith("__") or not isinstance(value, np.ndarray):
            continue
        print(f"  key='{key}'  shape={value.shape}  {'<-- 3D CUBE' if len(value.shape)==3 else ''}")
