# Py-CPP-LUT

## Build and Install

### requirements(in the "../3d-Party"):
- pybind11
- eigen
- the C++ compiler support C++14 and openmp

### install: 

```
mkdir build
cmake ..
add the generated .so file to the path where python can find it.

or

./make.sh
```

## How to use
```python
python ./test/py_lut_inference_test.py
```

The origin image: ![origin_image](./test/1.jpg)

The applyed lut image
![lut_image](./test/new_img_1.jpg)
