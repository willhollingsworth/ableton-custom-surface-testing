# uncompyle6 version 3.5.0
# Python bytecode 3.7 (3394)
# Decompiled from: Python 2.7.5 (default, Nov 16 2020, 22:23:17)
# [GCC 4.8.5 20150623 (Red Hat 4.8.5-44)]
# Embedded file name: ..\..\..\output\Live\win_64_static\Release\python-bundle\MIDI Remote Scripts\MIDI_Mix\__init__.py
# Size of source mod 2**32: 638 bytes
from __future__ import absolute_import, print_function, unicode_literals
from _Framework.Capabilities import Capabilities as caps
from .MIDI_Mix import MIDI_Mix


def get_capabilities():
    return {caps.CONTROLLER_ID_KEY: caps.controller_id(vendor_id=2536,
                                                       product_ids=[49],
                                                       model_name='MIDI Mix'),

            caps.PORTS_KEY: [
        caps.inport(props=[caps.NOTES_CC, caps.SCRIPT]),
        caps.outport(props=[caps.NOTES_CC, caps.SCRIPT])]}


def create_instance(c_instance):
    return MIDI_Mix(c_instance)
