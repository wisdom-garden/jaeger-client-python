#
# Autogenerated by Thrift Compiler (0.9.3)
#
# DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
#
#  options string: py:new_style,tornado
#

from thrift.Thrift import TType, TMessageType, TException, TApplicationException
import logging
from .ttypes import *
from thrift.Thrift import TProcessor
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol, TProtocol
try:
  from thrift.protocol import fastbinary
except:
  fastbinary = None

from tornado import gen
from tornado import concurrent
from thrift.transport import TTransport

class Iface(object):
  def startTrace(self, request):
    """
    Parameters:
     - request
    """
    pass

  def joinTrace(self, request):
    """
    Parameters:
     - request
    """
    pass


class Client(Iface):
  def __init__(self, transport, iprot_factory, oprot_factory=None):
    self._transport = transport
    self._iprot_factory = iprot_factory
    self._oprot_factory = (oprot_factory if oprot_factory is not None
                           else iprot_factory)
    self._seqid = 0
    self._reqs = {}
    self._transport.io_loop.spawn_callback(self._start_receiving)

  @gen.engine
  def _start_receiving(self):
    while True:
      try:
        frame = yield self._transport.readFrame()
      except TTransport.TTransportException as e:
        for future in self._reqs.itervalues():
          future.set_exception(e)
        self._reqs = {}
        return
      tr = TTransport.TMemoryBuffer(frame)
      iprot = self._iprot_factory.getProtocol(tr)
      (fname, mtype, rseqid) = iprot.readMessageBegin()
      future = self._reqs.pop(rseqid, None)
      if not future:
        # future has already been discarded
        continue
      method = getattr(self, 'recv_' + fname)
      try:
        result = method(iprot, mtype, rseqid)
      except Exception as e:
        future.set_exception(e)
      else:
        future.set_result(result)

  def startTrace(self, request):
    """
    Parameters:
     - request
    """
    self._seqid += 1
    future = self._reqs[self._seqid] = concurrent.Future()
    self.send_startTrace(request)
    return future

  def send_startTrace(self, request):
    oprot = self._oprot_factory.getProtocol(self._transport)
    oprot.writeMessageBegin('startTrace', TMessageType.CALL, self._seqid)
    args = startTrace_args()
    args.request = request
    args.write(oprot)
    oprot.writeMessageEnd()
    oprot.trans.flush()

  def recv_startTrace(self, iprot, mtype, rseqid):
    if mtype == TMessageType.EXCEPTION:
      x = TApplicationException()
      x.read(iprot)
      iprot.readMessageEnd()
      raise x
    result = startTrace_result()
    result.read(iprot)
    iprot.readMessageEnd()
    if result.success is not None:
      return result.success
    raise TApplicationException(TApplicationException.MISSING_RESULT, "startTrace failed: unknown result")

  def joinTrace(self, request):
    """
    Parameters:
     - request
    """
    self._seqid += 1
    future = self._reqs[self._seqid] = concurrent.Future()
    self.send_joinTrace(request)
    return future

  def send_joinTrace(self, request):
    oprot = self._oprot_factory.getProtocol(self._transport)
    oprot.writeMessageBegin('joinTrace', TMessageType.CALL, self._seqid)
    args = joinTrace_args()
    args.request = request
    args.write(oprot)
    oprot.writeMessageEnd()
    oprot.trans.flush()

  def recv_joinTrace(self, iprot, mtype, rseqid):
    if mtype == TMessageType.EXCEPTION:
      x = TApplicationException()
      x.read(iprot)
      iprot.readMessageEnd()
      raise x
    result = joinTrace_result()
    result.read(iprot)
    iprot.readMessageEnd()
    if result.success is not None:
      return result.success
    raise TApplicationException(TApplicationException.MISSING_RESULT, "joinTrace failed: unknown result")


class Processor(Iface, TProcessor):
  def __init__(self, handler):
    self._handler = handler
    self._processMap = {}
    self._processMap["startTrace"] = Processor.process_startTrace
    self._processMap["joinTrace"] = Processor.process_joinTrace

  def process(self, iprot, oprot):
    (name, type, seqid) = iprot.readMessageBegin()
    if name not in self._processMap:
      iprot.skip(TType.STRUCT)
      iprot.readMessageEnd()
      x = TApplicationException(TApplicationException.UNKNOWN_METHOD, 'Unknown function %s' % (name))
      oprot.writeMessageBegin(name, TMessageType.EXCEPTION, seqid)
      x.write(oprot)
      oprot.writeMessageEnd()
      oprot.trans.flush()
      return
    else:
      return self._processMap[name](self, seqid, iprot, oprot)

  @gen.coroutine
  def process_startTrace(self, seqid, iprot, oprot):
    args = startTrace_args()
    args.read(iprot)
    iprot.readMessageEnd()
    result = startTrace_result()
    result.success = yield gen.maybe_future(self._handler.startTrace(args.request))
    oprot.writeMessageBegin("startTrace", TMessageType.REPLY, seqid)
    result.write(oprot)
    oprot.writeMessageEnd()
    oprot.trans.flush()

  @gen.coroutine
  def process_joinTrace(self, seqid, iprot, oprot):
    args = joinTrace_args()
    args.read(iprot)
    iprot.readMessageEnd()
    result = joinTrace_result()
    result.success = yield gen.maybe_future(self._handler.joinTrace(args.request))
    oprot.writeMessageBegin("joinTrace", TMessageType.REPLY, seqid)
    result.write(oprot)
    oprot.writeMessageEnd()
    oprot.trans.flush()


# HELPER FUNCTIONS AND STRUCTURES

class startTrace_args(object):
  """
  Attributes:
   - request
  """

  thrift_spec = (
    None, # 0
    (1, TType.STRUCT, 'request', (StartTraceRequest, StartTraceRequest.thrift_spec), None, ), # 1
  )

  def __init__(self, request=None,):
    self.request = request

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
          self.request = StartTraceRequest()
          self.request.read(iprot)
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
    oprot.writeStructBegin('startTrace_args')
    if self.request is not None:
      oprot.writeFieldBegin('request', TType.STRUCT, 1)
      self.request.write(oprot)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __hash__(self):
    value = 17
    value = (value * 31) ^ hash(self.request)
    return value

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.items()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class startTrace_result(object):
  """
  Attributes:
   - success
  """

  thrift_spec = (
    (0, TType.STRUCT, 'success', (TraceResponse, TraceResponse.thrift_spec), None, ), # 0
  )

  def __init__(self, success=None,):
    self.success = success

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 0:
        if ftype == TType.STRUCT:
          self.success = TraceResponse()
          self.success.read(iprot)
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
    oprot.writeStructBegin('startTrace_result')
    if self.success is not None:
      oprot.writeFieldBegin('success', TType.STRUCT, 0)
      self.success.write(oprot)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __hash__(self):
    value = 17
    value = (value * 31) ^ hash(self.success)
    return value

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.items()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class joinTrace_args(object):
  """
  Attributes:
   - request
  """

  thrift_spec = (
    None, # 0
    (1, TType.STRUCT, 'request', (JoinTraceRequest, JoinTraceRequest.thrift_spec), None, ), # 1
  )

  def __init__(self, request=None,):
    self.request = request

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
          self.request = JoinTraceRequest()
          self.request.read(iprot)
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
    oprot.writeStructBegin('joinTrace_args')
    if self.request is not None:
      oprot.writeFieldBegin('request', TType.STRUCT, 1)
      self.request.write(oprot)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __hash__(self):
    value = 17
    value = (value * 31) ^ hash(self.request)
    return value

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.items()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class joinTrace_result(object):
  """
  Attributes:
   - success
  """

  thrift_spec = (
    (0, TType.STRUCT, 'success', (TraceResponse, TraceResponse.thrift_spec), None, ), # 0
  )

  def __init__(self, success=None,):
    self.success = success

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 0:
        if ftype == TType.STRUCT:
          self.success = TraceResponse()
          self.success.read(iprot)
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
    oprot.writeStructBegin('joinTrace_result')
    if self.success is not None:
      oprot.writeFieldBegin('success', TType.STRUCT, 0)
      self.success.write(oprot)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __hash__(self):
    value = 17
    value = (value * 31) ^ hash(self.success)
    return value

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.items()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)
