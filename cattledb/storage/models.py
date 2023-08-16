#!/usr/bin/python
# coding: utf-8

from enum import Enum

from ..core.models import (DeviceActivityItem, EventList, FastDictTimeseries,
                           FastFloatTimeseries, MetaDataItem,
                           ReaderActivityItem, RowUpsert, SerializableDict,
                           SerializableNamespaceDict, TimeSeries)


class EventSeriesType(Enum):
    DAILY = 1
    MONTHLY = 2
