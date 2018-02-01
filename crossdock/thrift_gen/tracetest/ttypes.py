#
# Autogenerated by Thrift Compiler (0.9.3)
#
# DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
#
#  options string: py:new_style,tornado
#

from thrift.Thrift import TType, TMessageType, TException, TApplicationException

from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol, TProtocol
try:
  from thrift.protocol import fastbinary
except:
  fastbinary = None


class Transport(object):
  HTTP = 0
  TCHANNEL = 1

  _VALUES_TO_NAMES = {
    0: "HTTP",
    1: "TCHANNEL",
  }

  _NAMES_TO_VALUES = {
    "HTTP": 0,
    "TCHANNEL": 1,
  }


class Downstream(object):
  """
  Attributes:
   - serviceName
   - serverRole
   - host
   - port
   - transport
   - downstream
  """

  #thrift_spec = (
    #None, # 0
    #(1, TType.STRING, 'serviceName', None, None, ), # 1
    #(2, TType.STRING, 'serverRole', None, None, ), # 2
    #(3, TType.STRING, 'host', None, None, ), # 3
    #(4, TType.STRING, 'port', None, None, ), # 4
    #(5, TType.I32, 'transport', None, None, ), # 5
    #(6, TType.STRUCT, 'downstream', (Downstream, Downstream.thrift_spec), None, ), # 6
  #)

  def __init__(self, serviceName=None, serverRole=None, host=None, port=None, transport=None, downstream=None,):
    self.serviceName = serviceName
    self.serverRole = serverRole
    self.host = host
    self.port = port
    self.transport = transport
    self.downstream = downstream

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.STRING:
          self.serviceName = iprot.readString()
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.STRING:
          self.serverRole = iprot.readString()
        else:
          iprot.skip(ftype)
      elif fid == 3:
        if ftype == TType.STRING:
          self.host = iprot.readString()
        else:
          iprot.skip(ftype)
      elif fid == 4:
        if ftype == TType.STRING:
          self.port = iprot.readString()
        else:
          iprot.skip(ftype)
      elif fid == 5:
        if ftype == TType.I32:
          self.transport = iprot.readI32()
        else:
          iprot.skip(ftype)
      elif fid == 6:
        if ftype == TType.STRUCT:
          self.downstream = Downstream()
          self.downstream.read(iprot)
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('Downstream')
    if self.serviceName is not None:
      oprot.writeFieldBegin('serviceName', TType.STRING, 1)
      oprot.writeString(self.serviceName)
      oprot.writeFieldEnd()
    if self.serverRole is not None:
      oprot.writeFieldBegin('serverRole', TType.STRING, 2)
      oprot.writeString(self.serverRole)
      oprot.writeFieldEnd()
    if self.host is not None:
      oprot.writeFieldBegin('host', TType.STRING, 3)
      oprot.writeString(self.host)
      oprot.writeFieldEnd()
    if self.port is not None:
      oprot.writeFieldBegin('port', TType.STRING, 4)
      oprot.writeString(self.port)
      oprot.writeFieldEnd()
    if self.transport is not None:
      oprot.writeFieldBegin('transport', TType.I32, 5)
      oprot.writeI32(self.transport)
      oprot.writeFieldEnd()
    if self.downstream is not None:
      oprot.writeFieldBegin('downstream', TType.STRUCT, 6)
      self.downstream.write(oprot)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    if self.serviceName is None:
      raise TProtocol.TProtocolException(message='Required field serviceName is unset!')
    if self.serverRole is None:
      raise TProtocol.TProtocolException(message='Required field serverRole is unset!')
    if self.host is None:
      raise TProtocol.TProtocolException(message='Required field host is unset!')
    if self.port is None:
      raise TProtocol.TProtocolException(message='Required field port is unset!')
    if self.transport is None:
      raise TProtocol.TProtocolException(message='Required field transport is unset!')
    return


  def __hash__(self):
    value = 17
    value = (value * 31) ^ hash(self.serviceName)
    value = (value * 31) ^ hash(self.serverRole)
    value = (value * 31) ^ hash(self.host)
    value = (value * 31) ^ hash(self.port)
    value = (value * 31) ^ hash(self.transport)
    value = (value * 31) ^ hash(self.downstream)
    return value

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.items()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class StartTraceRequest(object):
  """
  Attributes:
   - serverRole
   - sampled
   - baggage
   - downstream
  """

  #thrift_spec = (
    #None, # 0
    #(1, TType.STRING, 'serverRole', None, None, ), # 1
    #(2, TType.BOOL, 'sampled', None, None, ), # 2
    #(3, TType.STRING, 'baggage', None, None, ), # 3
    #(4, TType.STRUCT, 'downstream', (Downstream, Downstream.thrift_spec), None, ), # 4
  #)

  def __init__(self, serverRole=None, sampled=None, baggage=None, downstream=None,):
    self.serverRole = serverRole
    self.sampled = sampled
    self.baggage = baggage
    self.downstream = downstream

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.STRING:
          self.serverRole = iprot.readString()
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.BOOL:
          self.sampled = iprot.readBool()
        else:
          iprot.skip(ftype)
      elif fid == 3:
        if ftype == TType.STRING:
          self.baggage = iprot.readString()
        else:
          iprot.skip(ftype)
      elif fid == 4:
        if ftype == TType.STRUCT:
          self.downstream = Downstream()
          self.downstream.read(iprot)
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('StartTraceRequest')
    if self.serverRole is not None:
      oprot.writeFieldBegin('serverRole', TType.STRING, 1)
      oprot.writeString(self.serverRole)
      oprot.writeFieldEnd()
    if self.sampled is not None:
      oprot.writeFieldBegin('sampled', TType.BOOL, 2)
      oprot.writeBool(self.sampled)
      oprot.writeFieldEnd()
    if self.baggage is not None:
      oprot.writeFieldBegin('baggage', TType.STRING, 3)
      oprot.writeString(self.baggage)
      oprot.writeFieldEnd()
    if self.downstream is not None:
      oprot.writeFieldBegin('downstream', TType.STRUCT, 4)
      self.downstream.write(oprot)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    if self.serverRole is None:
      raise TProtocol.TProtocolException(message='Required field serverRole is unset!')
    if self.sampled is None:
      raise TProtocol.TProtocolException(message='Required field sampled is unset!')
    if self.baggage is None:
      raise TProtocol.TProtocolException(message='Required field baggage is unset!')
    if self.downstream is None:
      raise TProtocol.TProtocolException(message='Required field downstream is unset!')
    return


  def __hash__(self):
    value = 17
    value = (value * 31) ^ hash(self.serverRole)
    value = (value * 31) ^ hash(self.sampled)
    value = (value * 31) ^ hash(self.baggage)
    value = (value * 31) ^ hash(self.downstream)
    return value

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.items()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class JoinTraceRequest(object):
  """
  Attributes:
   - serverRole
   - downstream
  """

  #thrift_spec = (
    #None, # 0
    #(1, TType.STRING, 'serverRole', None, None, ), # 1
    #(2, TType.STRUCT, 'downstream', (Downstream, Downstream.thrift_spec), None, ), # 2
  #)

  def __init__(self, serverRole=None, downstream=None,):
    self.serverRole = serverRole
    self.downstream = downstream

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.STRING:
          self.serverRole = iprot.readString()
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.STRUCT:
          self.downstream = Downstream()
          self.downstream.read(iprot)
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('JoinTraceRequest')
    if self.serverRole is not None:
      oprot.writeFieldBegin('serverRole', TType.STRING, 1)
      oprot.writeString(self.serverRole)
      oprot.writeFieldEnd()
    if self.downstream is not None:
      oprot.writeFieldBegin('downstream', TType.STRUCT, 2)
      self.downstream.write(oprot)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    if self.serverRole is None:
      raise TProtocol.TProtocolException(message='Required field serverRole is unset!')
    return


  def __hash__(self):
    value = 17
    value = (value * 31) ^ hash(self.serverRole)
    value = (value * 31) ^ hash(self.downstream)
    return value

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.items()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class ObservedSpan(object):
  """
  Attributes:
   - traceId
   - sampled
   - baggage
  """

  #thrift_spec = (
    #None, # 0
    #(1, TType.STRING, 'traceId', None, None, ), # 1
    #(2, TType.BOOL, 'sampled', None, None, ), # 2
    #(3, TType.STRING, 'baggage', None, None, ), # 3
  #)

  def __init__(self, traceId=None, sampled=None, baggage=None,):
    self.traceId = traceId
    self.sampled = sampled
    self.baggage = baggage

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.STRING:
          self.traceId = iprot.readString()
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.BOOL:
          self.sampled = iprot.readBool()
        else:
          iprot.skip(ftype)
      elif fid == 3:
        if ftype == TType.STRING:
          self.baggage = iprot.readString()
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('ObservedSpan')
    if self.traceId is not None:
      oprot.writeFieldBegin('traceId', TType.STRING, 1)
      oprot.writeString(self.traceId)
      oprot.writeFieldEnd()
    if self.sampled is not None:
      oprot.writeFieldBegin('sampled', TType.BOOL, 2)
      oprot.writeBool(self.sampled)
      oprot.writeFieldEnd()
    if self.baggage is not None:
      oprot.writeFieldBegin('baggage', TType.STRING, 3)
      oprot.writeString(self.baggage)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    if self.traceId is None:
      raise TProtocol.TProtocolException(message='Required field traceId is unset!')
    if self.sampled is None:
      raise TProtocol.TProtocolException(message='Required field sampled is unset!')
    if self.baggage is None:
      raise TProtocol.TProtocolException(message='Required field baggage is unset!')
    return


  def __hash__(self):
    value = 17
    value = (value * 31) ^ hash(self.traceId)
    value = (value * 31) ^ hash(self.sampled)
    value = (value * 31) ^ hash(self.baggage)
    return value

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.items()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class TraceResponse(object):
  """
  Each server must include the information about the span it observed.
  It can only be omitted from the response if notImplementedError field is not empty.
  If the server was instructed to make a downstream call, it must embed the
  downstream response in its own response.

  Attributes:
   - span
   - downstream
   - notImplementedError
  """

  #thrift_spec = (
    #None, # 0
    #(1, TType.STRUCT, 'span', (ObservedSpan, ObservedSpan.thrift_spec), None, ), # 1
    #(2, TType.STRUCT, 'downstream', (TraceResponse, TraceResponse.thrift_spec), None, ), # 2
    #(3, TType.STRING, 'notImplementedError', None, None, ), # 3
  #)

  def __init__(self, span=None, downstream=None, notImplementedError=None,):
    self.span = span
    self.downstream = downstream
    self.notImplementedError = notImplementedError

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.STRUCT:
          self.span = ObservedSpan()
          self.span.read(iprot)
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.STRUCT:
          self.downstream = TraceResponse()
          self.downstream.read(iprot)
        else:
          iprot.skip(ftype)
      elif fid == 3:
        if ftype == TType.STRING:
          self.notImplementedError = iprot.readString()
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('TraceResponse')
    if self.span is not None:
      oprot.writeFieldBegin('span', TType.STRUCT, 1)
      self.span.write(oprot)
      oprot.writeFieldEnd()
    if self.downstream is not None:
      oprot.writeFieldBegin('downstream', TType.STRUCT, 2)
      self.downstream.write(oprot)
      oprot.writeFieldEnd()
    if self.notImplementedError is not None:
      oprot.writeFieldBegin('notImplementedError', TType.STRING, 3)
      oprot.writeString(self.notImplementedError)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    if self.notImplementedError is None:
      raise TProtocol.TProtocolException(message='Required field notImplementedError is unset!')
    return


  def __hash__(self):
    value = 17
    value = (value * 31) ^ hash(self.span)
    value = (value * 31) ^ hash(self.downstream)
    value = (value * 31) ^ hash(self.notImplementedError)
    return value

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.items()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)
