"""Constants for the Enocean Cust integration."""

import logging

from homeassistant.const import Platform

DOMAIN = "enocean_cust"
DATA_ENOCEAN = "enocean_cust"
ENOCEAN_DONGLE = "dongle"

ERROR_INVALID_DONGLE_PATH = "invalid_dongle_path"

SIGNAL_RECEIVE_MESSAGE = "enocean_cust.receive_message"
SIGNAL_SEND_MESSAGE = "enocean_cust.send_message"

LOGGER = logging.getLogger(__package__)

PLATFORMS = [
    Platform.BINARY_SENSOR,
    Platform.LIGHT,
    Platform.SENSOR,
    Platform.SWITCH,
]
