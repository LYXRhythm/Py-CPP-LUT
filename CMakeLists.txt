project("CPPLUT")

cmake_minimum_required(VERSION 3.21)

set(EIGEN_DIR "./eigen-3.4.0/")
include_directories(${EIGEN_DIR})

include_directories(./cpp)

set(PyBind11_DIR "./pybind11-master/")
include_directories("./pybind11-master/include")
add_subdirectory(${PyBind11_DIR} build)


pybind11_add_module(ApplyLUT cpp/ApplyLUT.cpp)
find_package(OpenMP)
if(OpenMP_CXX_FOUND)
	target_link_libraries(ApplyLUT PUBLIC OpenMP::OpenMP_CXX)
	target_link_libraries(ApplyLUT )
	message("OpenMP")
	set_property(TARGET ApplyLUT PROPERTY CXX_STANDARD 14)
	if (MSVC)
		  add_custom_command(TARGET example-app
				     POST_BUILD
				     COMMAND ${CMAKE_COMMAND} -E copy_if_different
				     $<TARGET_FILE_DIR:example-app>)
	endif (MSVC)
endif()
