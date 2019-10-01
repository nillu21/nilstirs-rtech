# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from underwater_sensor_msgs/SpawnMarkerRequest.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import genpy
import geometry_msgs.msg
import visualization_msgs.msg
import std_msgs.msg

class SpawnMarkerRequest(genpy.Message):
  _md5sum = "382477d5cd41e53aa19e79a2e0ea5925"
  _type = "underwater_sensor_msgs/SpawnMarkerRequest"
  _has_header = False #flag to mark the presence of a Header object
  _full_text = """visualization_msgs/Marker marker

================================================================================
MSG: visualization_msgs/Marker
# See http://www.ros.org/wiki/rviz/DisplayTypes/Marker and http://www.ros.org/wiki/rviz/Tutorials/Markers%3A%20Basic%20Shapes for more information on using this message with rviz

uint8 ARROW=0
uint8 CUBE=1
uint8 SPHERE=2
uint8 CYLINDER=3
uint8 LINE_STRIP=4
uint8 LINE_LIST=5
uint8 CUBE_LIST=6
uint8 SPHERE_LIST=7
uint8 POINTS=8
uint8 TEXT_VIEW_FACING=9
uint8 MESH_RESOURCE=10
uint8 TRIANGLE_LIST=11

uint8 ADD=0
uint8 MODIFY=0
uint8 DELETE=2
uint8 DELETEALL=3

Header header                        # header for time/frame information
string ns                            # Namespace to place this object in... used in conjunction with id to create a unique name for the object
int32 id 		                         # object ID useful in conjunction with the namespace for manipulating and deleting the object later
int32 type 		                       # Type of object
int32 action 	                       # 0 add/modify an object, 1 (deprecated), 2 deletes an object, 3 deletes all objects
geometry_msgs/Pose pose                 # Pose of the object
geometry_msgs/Vector3 scale             # Scale of the object 1,1,1 means default (usually 1 meter square)
std_msgs/ColorRGBA color             # Color [0.0-1.0]
duration lifetime                    # How long the object should last before being automatically deleted.  0 means forever
bool frame_locked                    # If this marker should be frame-locked, i.e. retransformed into its frame every timestep

#Only used if the type specified has some use for them (eg. POINTS, LINE_STRIP, ...)
geometry_msgs/Point[] points
#Only used if the type specified has some use for them (eg. POINTS, LINE_STRIP, ...)
#number of colors must either be 0 or equal to the number of points
#NOTE: alpha is not yet used
std_msgs/ColorRGBA[] colors

# NOTE: only used for text markers
string text

# NOTE: only used for MESH_RESOURCE markers
string mesh_resource
bool mesh_use_embedded_materials

================================================================================
MSG: std_msgs/Header
# Standard metadata for higher-level stamped data types.
# This is generally used to communicate timestamped data 
# in a particular coordinate frame.
# 
# sequence ID: consecutively increasing ID 
uint32 seq
#Two-integer timestamp that is expressed as:
# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')
# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')
# time-handling sugar is provided by the client library
time stamp
#Frame this data is associated with
# 0: no frame
# 1: global frame
string frame_id

================================================================================
MSG: geometry_msgs/Pose
# A representation of pose in free space, composed of position and orientation. 
Point position
Quaternion orientation

================================================================================
MSG: geometry_msgs/Point
# This contains the position of a point in free space
float64 x
float64 y
float64 z

================================================================================
MSG: geometry_msgs/Quaternion
# This represents an orientation in free space in quaternion form.

float64 x
float64 y
float64 z
float64 w

================================================================================
MSG: geometry_msgs/Vector3
# This represents a vector in free space. 
# It is only meant to represent a direction. Therefore, it does not
# make sense to apply a translation to it (e.g., when applying a 
# generic rigid transformation to a Vector3, tf2 will only apply the
# rotation). If you want your data to be translatable too, use the
# geometry_msgs/Point message instead.

float64 x
float64 y
float64 z
================================================================================
MSG: std_msgs/ColorRGBA
float32 r
float32 g
float32 b
float32 a
"""
  __slots__ = ['marker']
  _slot_types = ['visualization_msgs/Marker']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       marker

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(SpawnMarkerRequest, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.marker is None:
        self.marker = visualization_msgs.msg.Marker()
    else:
      self.marker = visualization_msgs.msg.Marker()

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      _x = self
      buff.write(_get_struct_3I().pack(_x.marker.header.seq, _x.marker.header.stamp.secs, _x.marker.header.stamp.nsecs))
      _x = self.marker.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self.marker.ns
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_get_struct_3i10d4f2iB().pack(_x.marker.id, _x.marker.type, _x.marker.action, _x.marker.pose.position.x, _x.marker.pose.position.y, _x.marker.pose.position.z, _x.marker.pose.orientation.x, _x.marker.pose.orientation.y, _x.marker.pose.orientation.z, _x.marker.pose.orientation.w, _x.marker.scale.x, _x.marker.scale.y, _x.marker.scale.z, _x.marker.color.r, _x.marker.color.g, _x.marker.color.b, _x.marker.color.a, _x.marker.lifetime.secs, _x.marker.lifetime.nsecs, _x.marker.frame_locked))
      length = len(self.marker.points)
      buff.write(_struct_I.pack(length))
      for val1 in self.marker.points:
        _x = val1
        buff.write(_get_struct_3d().pack(_x.x, _x.y, _x.z))
      length = len(self.marker.colors)
      buff.write(_struct_I.pack(length))
      for val1 in self.marker.colors:
        _x = val1
        buff.write(_get_struct_4f().pack(_x.r, _x.g, _x.b, _x.a))
      _x = self.marker.text
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self.marker.mesh_resource
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      buff.write(_get_struct_B().pack(self.marker.mesh_use_embedded_materials))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    try:
      if self.marker is None:
        self.marker = visualization_msgs.msg.Marker()
      end = 0
      _x = self
      start = end
      end += 12
      (_x.marker.header.seq, _x.marker.header.stamp.secs, _x.marker.header.stamp.nsecs,) = _get_struct_3I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.marker.header.frame_id = str[start:end].decode('utf-8')
      else:
        self.marker.header.frame_id = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.marker.ns = str[start:end].decode('utf-8')
      else:
        self.marker.ns = str[start:end]
      _x = self
      start = end
      end += 117
      (_x.marker.id, _x.marker.type, _x.marker.action, _x.marker.pose.position.x, _x.marker.pose.position.y, _x.marker.pose.position.z, _x.marker.pose.orientation.x, _x.marker.pose.orientation.y, _x.marker.pose.orientation.z, _x.marker.pose.orientation.w, _x.marker.scale.x, _x.marker.scale.y, _x.marker.scale.z, _x.marker.color.r, _x.marker.color.g, _x.marker.color.b, _x.marker.color.a, _x.marker.lifetime.secs, _x.marker.lifetime.nsecs, _x.marker.frame_locked,) = _get_struct_3i10d4f2iB().unpack(str[start:end])
      self.marker.frame_locked = bool(self.marker.frame_locked)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.marker.points = []
      for i in range(0, length):
        val1 = geometry_msgs.msg.Point()
        _x = val1
        start = end
        end += 24
        (_x.x, _x.y, _x.z,) = _get_struct_3d().unpack(str[start:end])
        self.marker.points.append(val1)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.marker.colors = []
      for i in range(0, length):
        val1 = std_msgs.msg.ColorRGBA()
        _x = val1
        start = end
        end += 16
        (_x.r, _x.g, _x.b, _x.a,) = _get_struct_4f().unpack(str[start:end])
        self.marker.colors.append(val1)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.marker.text = str[start:end].decode('utf-8')
      else:
        self.marker.text = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.marker.mesh_resource = str[start:end].decode('utf-8')
      else:
        self.marker.mesh_resource = str[start:end]
      start = end
      end += 1
      (self.marker.mesh_use_embedded_materials,) = _get_struct_B().unpack(str[start:end])
      self.marker.mesh_use_embedded_materials = bool(self.marker.mesh_use_embedded_materials)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      _x = self
      buff.write(_get_struct_3I().pack(_x.marker.header.seq, _x.marker.header.stamp.secs, _x.marker.header.stamp.nsecs))
      _x = self.marker.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self.marker.ns
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_get_struct_3i10d4f2iB().pack(_x.marker.id, _x.marker.type, _x.marker.action, _x.marker.pose.position.x, _x.marker.pose.position.y, _x.marker.pose.position.z, _x.marker.pose.orientation.x, _x.marker.pose.orientation.y, _x.marker.pose.orientation.z, _x.marker.pose.orientation.w, _x.marker.scale.x, _x.marker.scale.y, _x.marker.scale.z, _x.marker.color.r, _x.marker.color.g, _x.marker.color.b, _x.marker.color.a, _x.marker.lifetime.secs, _x.marker.lifetime.nsecs, _x.marker.frame_locked))
      length = len(self.marker.points)
      buff.write(_struct_I.pack(length))
      for val1 in self.marker.points:
        _x = val1
        buff.write(_get_struct_3d().pack(_x.x, _x.y, _x.z))
      length = len(self.marker.colors)
      buff.write(_struct_I.pack(length))
      for val1 in self.marker.colors:
        _x = val1
        buff.write(_get_struct_4f().pack(_x.r, _x.g, _x.b, _x.a))
      _x = self.marker.text
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self.marker.mesh_resource
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      buff.write(_get_struct_B().pack(self.marker.mesh_use_embedded_materials))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    try:
      if self.marker is None:
        self.marker = visualization_msgs.msg.Marker()
      end = 0
      _x = self
      start = end
      end += 12
      (_x.marker.header.seq, _x.marker.header.stamp.secs, _x.marker.header.stamp.nsecs,) = _get_struct_3I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.marker.header.frame_id = str[start:end].decode('utf-8')
      else:
        self.marker.header.frame_id = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.marker.ns = str[start:end].decode('utf-8')
      else:
        self.marker.ns = str[start:end]
      _x = self
      start = end
      end += 117
      (_x.marker.id, _x.marker.type, _x.marker.action, _x.marker.pose.position.x, _x.marker.pose.position.y, _x.marker.pose.position.z, _x.marker.pose.orientation.x, _x.marker.pose.orientation.y, _x.marker.pose.orientation.z, _x.marker.pose.orientation.w, _x.marker.scale.x, _x.marker.scale.y, _x.marker.scale.z, _x.marker.color.r, _x.marker.color.g, _x.marker.color.b, _x.marker.color.a, _x.marker.lifetime.secs, _x.marker.lifetime.nsecs, _x.marker.frame_locked,) = _get_struct_3i10d4f2iB().unpack(str[start:end])
      self.marker.frame_locked = bool(self.marker.frame_locked)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.marker.points = []
      for i in range(0, length):
        val1 = geometry_msgs.msg.Point()
        _x = val1
        start = end
        end += 24
        (_x.x, _x.y, _x.z,) = _get_struct_3d().unpack(str[start:end])
        self.marker.points.append(val1)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.marker.colors = []
      for i in range(0, length):
        val1 = std_msgs.msg.ColorRGBA()
        _x = val1
        start = end
        end += 16
        (_x.r, _x.g, _x.b, _x.a,) = _get_struct_4f().unpack(str[start:end])
        self.marker.colors.append(val1)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.marker.text = str[start:end].decode('utf-8')
      else:
        self.marker.text = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.marker.mesh_resource = str[start:end].decode('utf-8')
      else:
        self.marker.mesh_resource = str[start:end]
      start = end
      end += 1
      (self.marker.mesh_use_embedded_materials,) = _get_struct_B().unpack(str[start:end])
      self.marker.mesh_use_embedded_materials = bool(self.marker.mesh_use_embedded_materials)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_4f = None
def _get_struct_4f():
    global _struct_4f
    if _struct_4f is None:
        _struct_4f = struct.Struct("<4f")
    return _struct_4f
_struct_3I = None
def _get_struct_3I():
    global _struct_3I
    if _struct_3I is None:
        _struct_3I = struct.Struct("<3I")
    return _struct_3I
_struct_B = None
def _get_struct_B():
    global _struct_B
    if _struct_B is None:
        _struct_B = struct.Struct("<B")
    return _struct_B
_struct_3i10d4f2iB = None
def _get_struct_3i10d4f2iB():
    global _struct_3i10d4f2iB
    if _struct_3i10d4f2iB is None:
        _struct_3i10d4f2iB = struct.Struct("<3i10d4f2iB")
    return _struct_3i10d4f2iB
_struct_3d = None
def _get_struct_3d():
    global _struct_3d
    if _struct_3d is None:
        _struct_3d = struct.Struct("<3d")
    return _struct_3d
# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from underwater_sensor_msgs/SpawnMarkerResponse.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct


class SpawnMarkerResponse(genpy.Message):
  _md5sum = "2ec6f3eff0161f4257b808b12bc830c2"
  _type = "underwater_sensor_msgs/SpawnMarkerResponse"
  _has_header = False #flag to mark the presence of a Header object
  _full_text = """bool success
string status_message

"""
  __slots__ = ['success','status_message']
  _slot_types = ['bool','string']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       success,status_message

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(SpawnMarkerResponse, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.success is None:
        self.success = False
      if self.status_message is None:
        self.status_message = ''
    else:
      self.success = False
      self.status_message = ''

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      buff.write(_get_struct_B().pack(self.success))
      _x = self.status_message
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    try:
      end = 0
      start = end
      end += 1
      (self.success,) = _get_struct_B().unpack(str[start:end])
      self.success = bool(self.success)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.status_message = str[start:end].decode('utf-8')
      else:
        self.status_message = str[start:end]
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      buff.write(_get_struct_B().pack(self.success))
      _x = self.status_message
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    try:
      end = 0
      start = end
      end += 1
      (self.success,) = _get_struct_B().unpack(str[start:end])
      self.success = bool(self.success)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.status_message = str[start:end].decode('utf-8')
      else:
        self.status_message = str[start:end]
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_B = None
def _get_struct_B():
    global _struct_B
    if _struct_B is None:
        _struct_B = struct.Struct("<B")
    return _struct_B
class SpawnMarker(object):
  _type          = 'underwater_sensor_msgs/SpawnMarker'
  _md5sum = 'a7395a01b635e68c485c6bc7fed0b5a1'
  _request_class  = SpawnMarkerRequest
  _response_class = SpawnMarkerResponse
