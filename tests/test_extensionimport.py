#!/usr/bin/python
# coding: utf-8


def test_import_timeseries_extension():
    # Make sure to compile cattledb extension cdb_ext_ts first
    # Otherwise tests that also import cdb_ext_ts will fail with TypeErrors
    from cdb_ext_ts import timeseries
