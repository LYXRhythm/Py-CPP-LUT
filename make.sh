rm -rf ./build
rm ApplyLUT.cpython-36m-x86_64-linux-gnu.so
mkdir build
cd build
cmake -DCMAKE_PREFIX_PATH=~/LUT/PyApplyLUT-main/libtorch ..
cmake --build . --config Release
cp ApplyLUT.cpython-36m-x86_64-linux-gnu.so ../

