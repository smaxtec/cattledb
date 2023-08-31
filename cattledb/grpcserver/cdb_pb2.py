# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: cdb.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n\tcdb.proto"\\\n\x11TimeSeriesRequest\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x0e\n\x06metric\x18\x02 \x01(\t\x12\x15\n\rfrom_datetime\x18\x03 \x01(\t\x12\x13\n\x0bto_datetime\x18\x04 \x01(\t"b\n\x16MultiTimeSeriesRequest\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x15\n\rfrom_datetime\x18\x03 \x01(\t\x12\x13\n\x0bto_datetime\x18\x04 \x01(\t\x12\x0f\n\x07metrics\x18\x06 \x03(\t"b\n\x11LastValuesRequest\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05\x63ount\x18\x02 \x01(\x05\x12\x10\n\x08max_days\x18\x03 \x01(\x05\x12\x0e\n\x06max_ts\x18\x04 \x01(\t\x12\x0f\n\x07metrics\x18\x06 \x03(\t"V\n\rEventsRequest\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x15\n\rfrom_datetime\x18\x03 \x01(\t\x12\x13\n\x0bto_datetime\x18\x04 \x01(\t"_\n\x11LastEventsRequest\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\r\n\x05\x63ount\x18\x03 \x01(\x05\x12\x10\n\x08max_days\x18\x04 \x01(\x05\x12\x0e\n\x06max_ts\x18\x05 \x01(\t"v\n\x18IncrementActivityRequest\x12\x11\n\treader_id\x18\x01 \x01(\t\x12\x11\n\tdevice_id\x18\x02 \x01(\t\x12\x11\n\ttimestamp\x18\x03 \x01(\t\x12\r\n\x05value\x18\x04 \x01(\x05\x12\x12\n\nparent_ids\x18\x05 \x03(\t",\n\x14TotalActivityRequest\x12\x14\n\x0c\x64\x61y_datetime\x18\x01 \x01(\t"=\n\x12\x41\x63tivityDayRequest\x12\x11\n\tparent_id\x18\x02 \x01(\t\x12\x14\n\x0c\x64\x61y_datetime\x18\x01 \x01(\t"V\n\x15ReaderActivityRequest\x12\x11\n\treader_id\x18\x01 \x01(\t\x12\x15\n\rfrom_datetime\x18\x02 \x01(\t\x12\x13\n\x0bto_datetime\x18\x03 \x01(\t"7\n\x10\x41\x63tivityResponse\x12#\n\nactivities\x18\x01 \x03(\x0b\x32\x0f.ReaderActivity"=\n\x16\x44\x65viceActivityResponse\x12#\n\nactivities\x18\x01 \x03(\x0b\x32\x0f.DeviceActivity"F\n\x0e\x44\x65viceActivity\x12\x10\n\x08\x64\x61y_hour\x18\x01 \x01(\t\x12\x11\n\tdevice_id\x18\x02 \x01(\t\x12\x0f\n\x07\x63ounter\x18\x04 \x01(\x05"I\n\x0eReaderActivity\x12\x10\n\x08\x64\x61y_hour\x18\x01 \x01(\t\x12\x11\n\treader_id\x18\x02 \x01(\t\x12\x12\n\ndevice_ids\x18\x04 \x03(\t"`\n\x0fMetaDataRequest\x12\x13\n\x0bobject_name\x18\x01 \x01(\t\x12\x12\n\nobject_key\x18\x02 \x01(\t\x12\x12\n\nnamespaces\x18\x03 \x03(\t\x12\x10\n\x08internal\x18\x04 \x01(\x08"X\n\x10MetaDataResponse\x12\x13\n\x0bobject_name\x18\x01 \x01(\t\x12\x12\n\nobject_key\x18\x02 \x01(\t\x12\x1b\n\x04\x64\x61ta\x18\x03 \x03(\x0b\x32\r.MetaDataDict"f\n\x0cMetaDataPost\x12\x13\n\x0bobject_name\x18\x01 \x01(\t\x12\x12\n\nobject_key\x18\x02 \x01(\t\x12\x1b\n\x04\x64\x61ta\x18\x03 \x03(\x0b\x32\r.MetaDataDict\x12\x10\n\x08internal\x18\x04 \x01(\x08"7\n\x0cMetaDataDict\x12\x11\n\tnamespace\x18\x01 \x01(\t\x12\x14\n\x05pairs\x18\x02 \x03(\x0b\x32\x05.Pair";\n\tPutResult\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\x0f\n\x07\x63ounter\x18\x02 \x01(\x03\x12\x0f\n\x07message\x18\x03 \x01(\t">\n\x0c\x44\x65leteResult\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\x0f\n\x07\x63ounter\x18\x02 \x01(\x03\x12\x0f\n\x07message\x18\x03 \x01(\t"*\n\tFloatItem\x12\x0e\n\x06offset\x18\x01 \x01(\x11\x12\r\n\x05value\x18\x02 \x01(\x02")\n\x08\x42lobItem\x12\x0e\n\x06offset\x18\x01 \x01(\x11\x12\r\n\x05value\x18\x02 \x01(\x0c""\n\x04Pair\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t""\n\nDictionary\x12\x14\n\x05pairs\x18\x01 \x03(\x0b\x32\x05.Pair"y\n\x0e\x44ictTimeSeries\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x0e\n\x06metric\x18\x02 \x01(\t\x12\x12\n\ntimestamps\x18\x03 \x03(\x03\x12\x1b\n\x06values\x18\x04 \x03(\x0b\x32\x0b.Dictionary\x12\x19\n\x11timestamp_offsets\x18\x05 \x03(\x11"t\n\x0b\x45ventSeries\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x12\n\ntimestamps\x18\x03 \x03(\x03\x12\x1b\n\x06values\x18\x04 \x03(\x0b\x32\x0b.Dictionary\x12\x19\n\x11timestamp_offsets\x18\x05 \x03(\x11"m\n\x0f\x46loatTimeSeries\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x0e\n\x06metric\x18\x02 \x01(\t\x12\x12\n\ntimestamps\x18\x03 \x03(\x03\x12\x0e\n\x06values\x18\x04 \x03(\x02\x12\x19\n\x11timestamp_offsets\x18\x05 \x03(\x11"5\n\x13\x46loatTimeSeriesList\x12\x1e\n\x04\x64\x61ta\x18\x01 \x03(\x0b\x32\x10.FloatTimeSeries2\xbd\x02\n\nTimeSeries\x12-\n\x03get\x12\x12.TimeSeriesRequest\x1a\x10.FloatTimeSeries"\x00\x12;\n\x08getMulti\x12\x17.MultiTimeSeriesRequest\x1a\x14.FloatTimeSeriesList"\x00\x12\x38\n\nlastValues\x12\x12.LastValuesRequest\x1a\x14.FloatTimeSeriesList"\x00\x12%\n\x03put\x12\x10.FloatTimeSeries\x1a\n.PutResult"\x00\x12.\n\x08putMulti\x12\x14.FloatTimeSeriesList\x1a\n.PutResult"\x00\x12\x32\n\x06\x64\x65lete\x12\x17.MultiTimeSeriesRequest\x1a\r.DeleteResult"\x00\x32\xaf\x01\n\x06\x45vents\x12%\n\x03get\x12\x0e.EventsRequest\x1a\x0c.EventSeries"\x00\x12\x30\n\nlastEvents\x12\x12.LastEventsRequest\x1a\x0c.EventSeries"\x00\x12!\n\x03put\x12\x0c.EventSeries\x1a\n.PutResult"\x00\x12)\n\x06\x64\x65lete\x12\x0e.EventsRequest\x1a\r.DeleteResult"\x00\x32\xec\x01\n\x08\x41\x63tivity\x12\x36\n\x08getTotal\x12\x15.TotalActivityRequest\x1a\x11.ActivityResponse"\x00\x12\x32\n\x06getDay\x12\x13.ActivityDayRequest\x1a\x11.ActivityResponse"\x00\x12>\n\tgetReader\x12\x16.ReaderActivityRequest\x1a\x17.DeviceActivityResponse"\x00\x12\x34\n\tincrement\x12\x19.IncrementActivityRequest\x1a\n.PutResult"\x00\x32\\\n\x08MetaData\x12,\n\x03get\x12\x10.MetaDataRequest\x1a\x11.MetaDataResponse"\x00\x12"\n\x03put\x12\r.MetaDataPost\x1a\n.PutResult"\x00\x62\x06proto3'
)


_TIMESERIESREQUEST = DESCRIPTOR.message_types_by_name["TimeSeriesRequest"]
_MULTITIMESERIESREQUEST = DESCRIPTOR.message_types_by_name["MultiTimeSeriesRequest"]
_LASTVALUESREQUEST = DESCRIPTOR.message_types_by_name["LastValuesRequest"]
_EVENTSREQUEST = DESCRIPTOR.message_types_by_name["EventsRequest"]
_LASTEVENTSREQUEST = DESCRIPTOR.message_types_by_name["LastEventsRequest"]
_INCREMENTACTIVITYREQUEST = DESCRIPTOR.message_types_by_name["IncrementActivityRequest"]
_TOTALACTIVITYREQUEST = DESCRIPTOR.message_types_by_name["TotalActivityRequest"]
_ACTIVITYDAYREQUEST = DESCRIPTOR.message_types_by_name["ActivityDayRequest"]
_READERACTIVITYREQUEST = DESCRIPTOR.message_types_by_name["ReaderActivityRequest"]
_ACTIVITYRESPONSE = DESCRIPTOR.message_types_by_name["ActivityResponse"]
_DEVICEACTIVITYRESPONSE = DESCRIPTOR.message_types_by_name["DeviceActivityResponse"]
_DEVICEACTIVITY = DESCRIPTOR.message_types_by_name["DeviceActivity"]
_READERACTIVITY = DESCRIPTOR.message_types_by_name["ReaderActivity"]
_METADATAREQUEST = DESCRIPTOR.message_types_by_name["MetaDataRequest"]
_METADATARESPONSE = DESCRIPTOR.message_types_by_name["MetaDataResponse"]
_METADATAPOST = DESCRIPTOR.message_types_by_name["MetaDataPost"]
_METADATADICT = DESCRIPTOR.message_types_by_name["MetaDataDict"]
_PUTRESULT = DESCRIPTOR.message_types_by_name["PutResult"]
_DELETERESULT = DESCRIPTOR.message_types_by_name["DeleteResult"]
_FLOATITEM = DESCRIPTOR.message_types_by_name["FloatItem"]
_BLOBITEM = DESCRIPTOR.message_types_by_name["BlobItem"]
_PAIR = DESCRIPTOR.message_types_by_name["Pair"]
_DICTIONARY = DESCRIPTOR.message_types_by_name["Dictionary"]
_DICTTIMESERIES = DESCRIPTOR.message_types_by_name["DictTimeSeries"]
_EVENTSERIES = DESCRIPTOR.message_types_by_name["EventSeries"]
_FLOATTIMESERIES = DESCRIPTOR.message_types_by_name["FloatTimeSeries"]
_FLOATTIMESERIESLIST = DESCRIPTOR.message_types_by_name["FloatTimeSeriesList"]
TimeSeriesRequest = _reflection.GeneratedProtocolMessageType(
    "TimeSeriesRequest",
    (_message.Message,),
    {
        "DESCRIPTOR": _TIMESERIESREQUEST,
        "__module__": "cdb_pb2"
        # @@protoc_insertion_point(class_scope:TimeSeriesRequest)
    },
)
_sym_db.RegisterMessage(TimeSeriesRequest)

MultiTimeSeriesRequest = _reflection.GeneratedProtocolMessageType(
    "MultiTimeSeriesRequest",
    (_message.Message,),
    {
        "DESCRIPTOR": _MULTITIMESERIESREQUEST,
        "__module__": "cdb_pb2"
        # @@protoc_insertion_point(class_scope:MultiTimeSeriesRequest)
    },
)
_sym_db.RegisterMessage(MultiTimeSeriesRequest)

LastValuesRequest = _reflection.GeneratedProtocolMessageType(
    "LastValuesRequest",
    (_message.Message,),
    {
        "DESCRIPTOR": _LASTVALUESREQUEST,
        "__module__": "cdb_pb2"
        # @@protoc_insertion_point(class_scope:LastValuesRequest)
    },
)
_sym_db.RegisterMessage(LastValuesRequest)

EventsRequest = _reflection.GeneratedProtocolMessageType(
    "EventsRequest",
    (_message.Message,),
    {
        "DESCRIPTOR": _EVENTSREQUEST,
        "__module__": "cdb_pb2"
        # @@protoc_insertion_point(class_scope:EventsRequest)
    },
)
_sym_db.RegisterMessage(EventsRequest)

LastEventsRequest = _reflection.GeneratedProtocolMessageType(
    "LastEventsRequest",
    (_message.Message,),
    {
        "DESCRIPTOR": _LASTEVENTSREQUEST,
        "__module__": "cdb_pb2"
        # @@protoc_insertion_point(class_scope:LastEventsRequest)
    },
)
_sym_db.RegisterMessage(LastEventsRequest)

IncrementActivityRequest = _reflection.GeneratedProtocolMessageType(
    "IncrementActivityRequest",
    (_message.Message,),
    {
        "DESCRIPTOR": _INCREMENTACTIVITYREQUEST,
        "__module__": "cdb_pb2"
        # @@protoc_insertion_point(class_scope:IncrementActivityRequest)
    },
)
_sym_db.RegisterMessage(IncrementActivityRequest)

TotalActivityRequest = _reflection.GeneratedProtocolMessageType(
    "TotalActivityRequest",
    (_message.Message,),
    {
        "DESCRIPTOR": _TOTALACTIVITYREQUEST,
        "__module__": "cdb_pb2"
        # @@protoc_insertion_point(class_scope:TotalActivityRequest)
    },
)
_sym_db.RegisterMessage(TotalActivityRequest)

ActivityDayRequest = _reflection.GeneratedProtocolMessageType(
    "ActivityDayRequest",
    (_message.Message,),
    {
        "DESCRIPTOR": _ACTIVITYDAYREQUEST,
        "__module__": "cdb_pb2"
        # @@protoc_insertion_point(class_scope:ActivityDayRequest)
    },
)
_sym_db.RegisterMessage(ActivityDayRequest)

ReaderActivityRequest = _reflection.GeneratedProtocolMessageType(
    "ReaderActivityRequest",
    (_message.Message,),
    {
        "DESCRIPTOR": _READERACTIVITYREQUEST,
        "__module__": "cdb_pb2"
        # @@protoc_insertion_point(class_scope:ReaderActivityRequest)
    },
)
_sym_db.RegisterMessage(ReaderActivityRequest)

ActivityResponse = _reflection.GeneratedProtocolMessageType(
    "ActivityResponse",
    (_message.Message,),
    {
        "DESCRIPTOR": _ACTIVITYRESPONSE,
        "__module__": "cdb_pb2"
        # @@protoc_insertion_point(class_scope:ActivityResponse)
    },
)
_sym_db.RegisterMessage(ActivityResponse)

DeviceActivityResponse = _reflection.GeneratedProtocolMessageType(
    "DeviceActivityResponse",
    (_message.Message,),
    {
        "DESCRIPTOR": _DEVICEACTIVITYRESPONSE,
        "__module__": "cdb_pb2"
        # @@protoc_insertion_point(class_scope:DeviceActivityResponse)
    },
)
_sym_db.RegisterMessage(DeviceActivityResponse)

DeviceActivity = _reflection.GeneratedProtocolMessageType(
    "DeviceActivity",
    (_message.Message,),
    {
        "DESCRIPTOR": _DEVICEACTIVITY,
        "__module__": "cdb_pb2"
        # @@protoc_insertion_point(class_scope:DeviceActivity)
    },
)
_sym_db.RegisterMessage(DeviceActivity)

ReaderActivity = _reflection.GeneratedProtocolMessageType(
    "ReaderActivity",
    (_message.Message,),
    {
        "DESCRIPTOR": _READERACTIVITY,
        "__module__": "cdb_pb2"
        # @@protoc_insertion_point(class_scope:ReaderActivity)
    },
)
_sym_db.RegisterMessage(ReaderActivity)

MetaDataRequest = _reflection.GeneratedProtocolMessageType(
    "MetaDataRequest",
    (_message.Message,),
    {
        "DESCRIPTOR": _METADATAREQUEST,
        "__module__": "cdb_pb2"
        # @@protoc_insertion_point(class_scope:MetaDataRequest)
    },
)
_sym_db.RegisterMessage(MetaDataRequest)

MetaDataResponse = _reflection.GeneratedProtocolMessageType(
    "MetaDataResponse",
    (_message.Message,),
    {
        "DESCRIPTOR": _METADATARESPONSE,
        "__module__": "cdb_pb2"
        # @@protoc_insertion_point(class_scope:MetaDataResponse)
    },
)
_sym_db.RegisterMessage(MetaDataResponse)

MetaDataPost = _reflection.GeneratedProtocolMessageType(
    "MetaDataPost",
    (_message.Message,),
    {
        "DESCRIPTOR": _METADATAPOST,
        "__module__": "cdb_pb2"
        # @@protoc_insertion_point(class_scope:MetaDataPost)
    },
)
_sym_db.RegisterMessage(MetaDataPost)

MetaDataDict = _reflection.GeneratedProtocolMessageType(
    "MetaDataDict",
    (_message.Message,),
    {
        "DESCRIPTOR": _METADATADICT,
        "__module__": "cdb_pb2"
        # @@protoc_insertion_point(class_scope:MetaDataDict)
    },
)
_sym_db.RegisterMessage(MetaDataDict)

PutResult = _reflection.GeneratedProtocolMessageType(
    "PutResult",
    (_message.Message,),
    {
        "DESCRIPTOR": _PUTRESULT,
        "__module__": "cdb_pb2"
        # @@protoc_insertion_point(class_scope:PutResult)
    },
)
_sym_db.RegisterMessage(PutResult)

DeleteResult = _reflection.GeneratedProtocolMessageType(
    "DeleteResult",
    (_message.Message,),
    {
        "DESCRIPTOR": _DELETERESULT,
        "__module__": "cdb_pb2"
        # @@protoc_insertion_point(class_scope:DeleteResult)
    },
)
_sym_db.RegisterMessage(DeleteResult)

FloatItem = _reflection.GeneratedProtocolMessageType(
    "FloatItem",
    (_message.Message,),
    {
        "DESCRIPTOR": _FLOATITEM,
        "__module__": "cdb_pb2"
        # @@protoc_insertion_point(class_scope:FloatItem)
    },
)
_sym_db.RegisterMessage(FloatItem)

BlobItem = _reflection.GeneratedProtocolMessageType(
    "BlobItem",
    (_message.Message,),
    {
        "DESCRIPTOR": _BLOBITEM,
        "__module__": "cdb_pb2"
        # @@protoc_insertion_point(class_scope:BlobItem)
    },
)
_sym_db.RegisterMessage(BlobItem)

Pair = _reflection.GeneratedProtocolMessageType(
    "Pair",
    (_message.Message,),
    {
        "DESCRIPTOR": _PAIR,
        "__module__": "cdb_pb2"
        # @@protoc_insertion_point(class_scope:Pair)
    },
)
_sym_db.RegisterMessage(Pair)

Dictionary = _reflection.GeneratedProtocolMessageType(
    "Dictionary",
    (_message.Message,),
    {
        "DESCRIPTOR": _DICTIONARY,
        "__module__": "cdb_pb2"
        # @@protoc_insertion_point(class_scope:Dictionary)
    },
)
_sym_db.RegisterMessage(Dictionary)

DictTimeSeries = _reflection.GeneratedProtocolMessageType(
    "DictTimeSeries",
    (_message.Message,),
    {
        "DESCRIPTOR": _DICTTIMESERIES,
        "__module__": "cdb_pb2"
        # @@protoc_insertion_point(class_scope:DictTimeSeries)
    },
)
_sym_db.RegisterMessage(DictTimeSeries)

EventSeries = _reflection.GeneratedProtocolMessageType(
    "EventSeries",
    (_message.Message,),
    {
        "DESCRIPTOR": _EVENTSERIES,
        "__module__": "cdb_pb2"
        # @@protoc_insertion_point(class_scope:EventSeries)
    },
)
_sym_db.RegisterMessage(EventSeries)

FloatTimeSeries = _reflection.GeneratedProtocolMessageType(
    "FloatTimeSeries",
    (_message.Message,),
    {
        "DESCRIPTOR": _FLOATTIMESERIES,
        "__module__": "cdb_pb2"
        # @@protoc_insertion_point(class_scope:FloatTimeSeries)
    },
)
_sym_db.RegisterMessage(FloatTimeSeries)

FloatTimeSeriesList = _reflection.GeneratedProtocolMessageType(
    "FloatTimeSeriesList",
    (_message.Message,),
    {
        "DESCRIPTOR": _FLOATTIMESERIESLIST,
        "__module__": "cdb_pb2"
        # @@protoc_insertion_point(class_scope:FloatTimeSeriesList)
    },
)
_sym_db.RegisterMessage(FloatTimeSeriesList)

_TIMESERIES = DESCRIPTOR.services_by_name["TimeSeries"]
_EVENTS = DESCRIPTOR.services_by_name["Events"]
_ACTIVITY = DESCRIPTOR.services_by_name["Activity"]
_METADATA = DESCRIPTOR.services_by_name["MetaData"]
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    _TIMESERIESREQUEST._serialized_start = 13
    _TIMESERIESREQUEST._serialized_end = 105
    _MULTITIMESERIESREQUEST._serialized_start = 107
    _MULTITIMESERIESREQUEST._serialized_end = 205
    _LASTVALUESREQUEST._serialized_start = 207
    _LASTVALUESREQUEST._serialized_end = 305
    _EVENTSREQUEST._serialized_start = 307
    _EVENTSREQUEST._serialized_end = 393
    _LASTEVENTSREQUEST._serialized_start = 395
    _LASTEVENTSREQUEST._serialized_end = 490
    _INCREMENTACTIVITYREQUEST._serialized_start = 492
    _INCREMENTACTIVITYREQUEST._serialized_end = 610
    _TOTALACTIVITYREQUEST._serialized_start = 612
    _TOTALACTIVITYREQUEST._serialized_end = 656
    _ACTIVITYDAYREQUEST._serialized_start = 658
    _ACTIVITYDAYREQUEST._serialized_end = 719
    _READERACTIVITYREQUEST._serialized_start = 721
    _READERACTIVITYREQUEST._serialized_end = 807
    _ACTIVITYRESPONSE._serialized_start = 809
    _ACTIVITYRESPONSE._serialized_end = 864
    _DEVICEACTIVITYRESPONSE._serialized_start = 866
    _DEVICEACTIVITYRESPONSE._serialized_end = 927
    _DEVICEACTIVITY._serialized_start = 929
    _DEVICEACTIVITY._serialized_end = 999
    _READERACTIVITY._serialized_start = 1001
    _READERACTIVITY._serialized_end = 1074
    _METADATAREQUEST._serialized_start = 1076
    _METADATAREQUEST._serialized_end = 1172
    _METADATARESPONSE._serialized_start = 1174
    _METADATARESPONSE._serialized_end = 1262
    _METADATAPOST._serialized_start = 1264
    _METADATAPOST._serialized_end = 1366
    _METADATADICT._serialized_start = 1368
    _METADATADICT._serialized_end = 1423
    _PUTRESULT._serialized_start = 1425
    _PUTRESULT._serialized_end = 1484
    _DELETERESULT._serialized_start = 1486
    _DELETERESULT._serialized_end = 1548
    _FLOATITEM._serialized_start = 1550
    _FLOATITEM._serialized_end = 1592
    _BLOBITEM._serialized_start = 1594
    _BLOBITEM._serialized_end = 1635
    _PAIR._serialized_start = 1637
    _PAIR._serialized_end = 1671
    _DICTIONARY._serialized_start = 1673
    _DICTIONARY._serialized_end = 1707
    _DICTTIMESERIES._serialized_start = 1709
    _DICTTIMESERIES._serialized_end = 1830
    _EVENTSERIES._serialized_start = 1832
    _EVENTSERIES._serialized_end = 1948
    _FLOATTIMESERIES._serialized_start = 1950
    _FLOATTIMESERIES._serialized_end = 2059
    _FLOATTIMESERIESLIST._serialized_start = 2061
    _FLOATTIMESERIESLIST._serialized_end = 2114
    _TIMESERIES._serialized_start = 2117
    _TIMESERIES._serialized_end = 2434
    _EVENTS._serialized_start = 2437
    _EVENTS._serialized_end = 2612
    _ACTIVITY._serialized_start = 2615
    _ACTIVITY._serialized_end = 2851
    _METADATA._serialized_start = 2853
    _METADATA._serialized_end = 2945
# @@protoc_insertion_point(module_scope)
