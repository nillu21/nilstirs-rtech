# generated from catkin/cmake/template/pkgConfig.cmake.in

# append elements to a list and remove existing duplicates from the list
# copied from catkin/cmake/list_append_deduplicate.cmake to keep pkgConfig
# self contained
macro(_list_append_deduplicate listname)
  if(NOT "${ARGN}" STREQUAL "")
    if(${listname})
      list(REMOVE_ITEM ${listname} ${ARGN})
    endif()
    list(APPEND ${listname} ${ARGN})
  endif()
endmacro()

# append elements to a list if they are not already in the list
# copied from catkin/cmake/list_append_unique.cmake to keep pkgConfig
# self contained
macro(_list_append_unique listname)
  foreach(_item ${ARGN})
    list(FIND ${listname} ${_item} _index)
    if(_index EQUAL -1)
      list(APPEND ${listname} ${_item})
    endif()
  endforeach()
endmacro()

# pack a list of libraries with optional build configuration keywords
# copied from catkin/cmake/catkin_libraries.cmake to keep pkgConfig
# self contained
macro(_pack_libraries_with_build_configuration VAR)
  set(${VAR} "")
  set(_argn ${ARGN})
  list(LENGTH _argn _count)
  set(_index 0)
  while(${_index} LESS ${_count})
    list(GET _argn ${_index} lib)
    if("${lib}" MATCHES "^(debug|optimized|general)$")
      math(EXPR _index "${_index} + 1")
      if(${_index} EQUAL ${_count})
        message(FATAL_ERROR "_pack_libraries_with_build_configuration() the list of libraries '${ARGN}' ends with '${lib}' which is a build configuration keyword and must be followed by a library")
      endif()
      list(GET _argn ${_index} library)
      list(APPEND ${VAR} "${lib}${CATKIN_BUILD_CONFIGURATION_KEYWORD_SEPARATOR}${library}")
    else()
      list(APPEND ${VAR} "${lib}")
    endif()
    math(EXPR _index "${_index} + 1")
  endwhile()
endmacro()

# unpack a list of libraries with optional build configuration keyword prefixes
# copied from catkin/cmake/catkin_libraries.cmake to keep pkgConfig
# self contained
macro(_unpack_libraries_with_build_configuration VAR)
  set(${VAR} "")
  foreach(lib ${ARGN})
    string(REGEX REPLACE "^(debug|optimized|general)${CATKIN_BUILD_CONFIGURATION_KEYWORD_SEPARATOR}(.+)$" "\\1;\\2" lib "${lib}")
    list(APPEND ${VAR} "${lib}")
  endforeach()
endmacro()


if(uwsim_CONFIG_INCLUDED)
  return()
endif()
set(uwsim_CONFIG_INCLUDED TRUE)

# set variables for source/devel/install prefixes
if("FALSE" STREQUAL "TRUE")
  set(uwsim_SOURCE_PREFIX /home/ubuntu/catkin_ws/src/underwater_simulation/uwsim)
  set(uwsim_DEVEL_PREFIX /home/ubuntu/catkin_ws/devel)
  set(uwsim_INSTALL_PREFIX "")
  set(uwsim_PREFIX ${uwsim_DEVEL_PREFIX})
else()
  set(uwsim_SOURCE_PREFIX "")
  set(uwsim_DEVEL_PREFIX "")
  set(uwsim_INSTALL_PREFIX /home/ubuntu/catkin_ws/install)
  set(uwsim_PREFIX ${uwsim_INSTALL_PREFIX})
endif()

# warn when using a deprecated package
if(NOT "" STREQUAL "")
  set(_msg "WARNING: package 'uwsim' is deprecated")
  # append custom deprecation text if available
  if(NOT "" STREQUAL "TRUE")
    set(_msg "${_msg} ()")
  endif()
  message("${_msg}")
endif()

# flag project as catkin-based to distinguish if a find_package()-ed project is a catkin project
set(uwsim_FOUND_CATKIN_PROJECT TRUE)

if(NOT "include;/usr/include;/opt/ros/kinetic/include/uwsim_bullet;/usr/include/libxml++-2.6;/usr/lib/x86_64-linux-gnu/libxml++-2.6/include;/usr/include/libxml2;/usr/include/glibmm-2.4;/usr/lib/x86_64-linux-gnu/glibmm-2.4/include;/usr/include/glib-2.0;/usr/lib/x86_64-linux-gnu/glib-2.0/include;/usr/include/sigc++-2.0;/usr/lib/x86_64-linux-gnu/sigc++-2.0/include;/opt/ros/kinetic/include/osg_interactive_markers;/opt/ros/kinetic/include/osg_markers;/opt/ros/kinetic/include/uwsim_osgocean;/opt/ros/kinetic/include/osg_utils " STREQUAL " ")
  set(uwsim_INCLUDE_DIRS "")
  set(_include_dirs "include;/usr/include;/opt/ros/kinetic/include/uwsim_bullet;/usr/include/libxml++-2.6;/usr/lib/x86_64-linux-gnu/libxml++-2.6/include;/usr/include/libxml2;/usr/include/glibmm-2.4;/usr/lib/x86_64-linux-gnu/glibmm-2.4/include;/usr/include/glib-2.0;/usr/lib/x86_64-linux-gnu/glib-2.0/include;/usr/include/sigc++-2.0;/usr/lib/x86_64-linux-gnu/sigc++-2.0/include;/opt/ros/kinetic/include/osg_interactive_markers;/opt/ros/kinetic/include/osg_markers;/opt/ros/kinetic/include/uwsim_osgocean;/opt/ros/kinetic/include/osg_utils")
  if(NOT " " STREQUAL " ")
    set(_report "Check the issue tracker '' and consider creating a ticket if the problem has not been reported yet.")
  elseif(NOT "http://www.irs.uji.es/uwsim/ " STREQUAL " ")
    set(_report "Check the website 'http://www.irs.uji.es/uwsim/' for information and consider reporting the problem.")
  else()
    set(_report "Report the problem to the maintainer 'Mario Prats <marioprats@gmail.com>, Javier Perez <perezsolerj@gmail.com>' and request to fix the problem.")
  endif()
  foreach(idir ${_include_dirs})
    if(IS_ABSOLUTE ${idir} AND IS_DIRECTORY ${idir})
      set(include ${idir})
    elseif("${idir} " STREQUAL "include ")
      get_filename_component(include "${uwsim_DIR}/../../../include" ABSOLUTE)
      if(NOT IS_DIRECTORY ${include})
        message(FATAL_ERROR "Project 'uwsim' specifies '${idir}' as an include dir, which is not found.  It does not exist in '${include}'.  ${_report}")
      endif()
    else()
      message(FATAL_ERROR "Project 'uwsim' specifies '${idir}' as an include dir, which is not found.  It does neither exist as an absolute directory nor in '/home/ubuntu/catkin_ws/install/${idir}'.  ${_report}")
    endif()
    _list_append_unique(uwsim_INCLUDE_DIRS ${include})
  endforeach()
endif()

set(libraries "uwsim;/usr/lib/x86_64-linux-gnu/libboost_thread.so;/usr/lib/x86_64-linux-gnu/libboost_program_options.so;/usr/lib/x86_64-linux-gnu/libboost_system.so;/usr/lib/x86_64-linux-gnu/libboost_filesystem.so;/usr/lib/x86_64-linux-gnu/libboost_chrono.so;/usr/lib/x86_64-linux-gnu/libboost_date_time.so;/usr/lib/x86_64-linux-gnu/libboost_atomic.so;/usr/lib/x86_64-linux-gnu/libpthread.so;/opt/ros/kinetic/lib/uwsim_bullet/libBulletCollision.a;/opt/ros/kinetic/lib/uwsim_bullet/libBulletDynamics.a;/opt/ros/kinetic/lib/uwsim_bullet/libBulletSoftBody.a;/opt/ros/kinetic/lib/uwsim_bullet/libLinearMath.a;xml++-2.6;xml2;glibmm-2.4;gobject-2.0;glib-2.0;sigc-2.0;/usr/lib/x86_64-linux-gnu/libosgSim.so;/usr/lib/x86_64-linux-gnu/libosgUtil.so;/usr/lib/x86_64-linux-gnu/libosgDB.so;/usr/lib/x86_64-linux-gnu/libosgFX.so;/usr/lib/x86_64-linux-gnu/libosgGA.so;/usr/lib/x86_64-linux-gnu/libosgTerrain.so;/usr/lib/x86_64-linux-gnu/libosgViewer.so;/usr/lib/x86_64-linux-gnu/libosgText.so;/usr/lib/x86_64-linux-gnu/libosgWidget.so;/usr/lib/x86_64-linux-gnu/libosg.so;/usr/lib/x86_64-linux-gnu/libosgParticle.so;/usr/lib/x86_64-linux-gnu/libosgManipulator.so;/usr/lib/x86_64-linux-gnu/libOpenThreads.so;/opt/ros/kinetic/lib/libosgbCollision.so;/opt/ros/kinetic/lib/libosgbDynamics.so;/opt/ros/kinetic/lib/libosgbInteraction.so;/opt/ros/kinetic/lib/libosg_interactive_markers.so;/opt/ros/kinetic/lib/libosg_markers.so;/opt/ros/kinetic/lib/libosgOcean.so;/opt/ros/kinetic/lib/libosg_utils.so;/opt/ros/kinetic/lib/libosgwTools.so;/opt/ros/kinetic/lib/libosgwQuery.so;/opt/ros/kinetic/lib/libosgwMx.so")
foreach(library ${libraries})
  # keep build configuration keywords, target names and absolute libraries as-is
  if("${library}" MATCHES "^(debug|optimized|general)$")
    list(APPEND uwsim_LIBRARIES ${library})
  elseif(TARGET ${library})
    list(APPEND uwsim_LIBRARIES ${library})
  elseif(IS_ABSOLUTE ${library})
    list(APPEND uwsim_LIBRARIES ${library})
  else()
    set(lib_path "")
    set(lib "${library}-NOTFOUND")
    # since the path where the library is found is returned we have to iterate over the paths manually
    foreach(path /home/ubuntu/catkin_ws/install/lib;/home/ubuntu/catkin_ws/devel/lib;/opt/ros/kinetic/lib)
      find_library(lib ${library}
        PATHS ${path}
        NO_DEFAULT_PATH NO_CMAKE_FIND_ROOT_PATH)
      if(lib)
        set(lib_path ${path})
        break()
      endif()
    endforeach()
    if(lib)
      _list_append_unique(uwsim_LIBRARY_DIRS ${lib_path})
      list(APPEND uwsim_LIBRARIES ${lib})
    else()
      # as a fall back for non-catkin libraries try to search globally
      find_library(lib ${library})
      if(NOT lib)
        message(FATAL_ERROR "Project '${PROJECT_NAME}' tried to find library '${library}'.  The library is neither a target nor built/installed properly.  Did you compile project 'uwsim'?  Did you find_package() it before the subdirectory containing its code is included?")
      endif()
      list(APPEND uwsim_LIBRARIES ${lib})
    endif()
  endif()
endforeach()

set(uwsim_EXPORTED_TARGETS "")
# create dummy targets for exported code generation targets to make life of users easier
foreach(t ${uwsim_EXPORTED_TARGETS})
  if(NOT TARGET ${t})
    add_custom_target(${t})
  endif()
endforeach()

set(depends "geometry_msgs;image_transport;interactive_markers;kdl_parser;nav_msgs;pcl_ros;pluginlib;resource_retriever;robot_state_publisher;roscpp;sensor_msgs;tf;underwater_sensor_msgs;urdf")
foreach(depend ${depends})
  string(REPLACE " " ";" depend_list ${depend})
  # the package name of the dependency must be kept in a unique variable so that it is not overwritten in recursive calls
  list(GET depend_list 0 uwsim_dep)
  list(LENGTH depend_list count)
  if(${count} EQUAL 1)
    # simple dependencies must only be find_package()-ed once
    if(NOT ${uwsim_dep}_FOUND)
      find_package(${uwsim_dep} REQUIRED NO_MODULE)
    endif()
  else()
    # dependencies with components must be find_package()-ed again
    list(REMOVE_AT depend_list 0)
    find_package(${uwsim_dep} REQUIRED NO_MODULE ${depend_list})
  endif()
  _list_append_unique(uwsim_INCLUDE_DIRS ${${uwsim_dep}_INCLUDE_DIRS})

  # merge build configuration keywords with library names to correctly deduplicate
  _pack_libraries_with_build_configuration(uwsim_LIBRARIES ${uwsim_LIBRARIES})
  _pack_libraries_with_build_configuration(_libraries ${${uwsim_dep}_LIBRARIES})
  _list_append_deduplicate(uwsim_LIBRARIES ${_libraries})
  # undo build configuration keyword merging after deduplication
  _unpack_libraries_with_build_configuration(uwsim_LIBRARIES ${uwsim_LIBRARIES})

  _list_append_unique(uwsim_LIBRARY_DIRS ${${uwsim_dep}_LIBRARY_DIRS})
  list(APPEND uwsim_EXPORTED_TARGETS ${${uwsim_dep}_EXPORTED_TARGETS})
endforeach()

set(pkg_cfg_extras "")
foreach(extra ${pkg_cfg_extras})
  if(NOT IS_ABSOLUTE ${extra})
    set(extra ${uwsim_DIR}/${extra})
  endif()
  include(${extra})
endforeach()
