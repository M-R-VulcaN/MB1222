cmake_minimum_required(VERSION 3.0.2)
project(mb1222)

find_package(catkin REQUIRED COMPONENTS
    rospy
    std_msgs
)

catkin_package(
#  INCLUDE_DIRS include
#  LIBRARIES MB1222
#  CATKIN_DEPENDS other_catkin_pkg
#  DEPENDS system_lib
)

include_directories(
# include
    ${catkin_INCLUDE_DIRS}
)

catkin_install_python(PROGRAMS
  scripts/avg_ultra_sonic.py
  scripts/change_address.py
  scripts/ultra_sonic.py
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)