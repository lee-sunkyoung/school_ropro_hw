cmake_minimum_required(VERSION 3.0.2)
project(ropro_node1)

find_package(catkin REQUIRED COMPONENTS
  geometry_msgs
  roscpp
  sensor_msgs
  std_msgs
)

generate_messages(DEPENDENCIES std_msgs)

catkin_package(
  INCLUDE_DIRS include
  LIBRARIES joystick_mani
  CATKIN_DEPENDS geometry_msgs roscpp sensor_msgs std_msgs
)

include_directories(
  include
  ${catkin_INCLUDE_DIRS}
)

add_executable(ropro_node1 src/ropro_node1.cpp)
target_link_libraries(ropro_node1 ${catkin_LIBRARIES})
add_dependencies(ropro_node1 ${${ropro_node1}_EXPORTED_TARGETS} ${catkin_EXPORTED_TARGETS})
