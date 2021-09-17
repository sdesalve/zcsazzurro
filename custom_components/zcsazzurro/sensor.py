"""Support for getting collected information from ZCSAzzurro."""
from __future__ import annotations

from datetime import timedelta
import logging

import voluptuous as vol

from homeassistant.components.rest.data import RestData
from homeassistant.components.sensor import (
    DEVICE_CLASS_ENERGY,
    PLATFORM_SCHEMA,
    STATE_CLASS_MEASUREMENT,
    SensorEntity,
)
from homeassistant.const import (
    ATTR_DATE,
    ATTR_TEMPERATURE,
    ATTR_TIME,
    CONF_NAME,
    ENERGY_WATT_HOUR,
)
from homeassistant.core import callback
import homeassistant.helpers.config_validation as cv

import json

_LOGGER = logging.getLogger(__name__)
_ENDPOINT = "https://third.zcsazzurroportal.com:19003"

CONF_THINGKEY = "thingkey"
CONF_AUTHKEY = "authkey"

DEFAULT_NAME = "ZCSAzzurro"
DEFAULT_VERIFY_SSL = False

SCAN_INTERVAL = timedelta(minutes=1)

PLATFORM_SCHEMA = PLATFORM_SCHEMA.extend(
    {
        vol.Required(CONF_THINGKEY): cv.string,
        vol.Required(CONF_AUTHKEY): cv.string,
        vol.Optional(CONF_NAME, default=DEFAULT_NAME): cv.string,
    }
)


async def async_setup_platform(hass, config, async_add_entities, discovery_info=None):
    """Set up the ZCSAzzurro sensor."""
    name = config.get(CONF_NAME)
    auth_key = config.get(CONF_AUTHKEY)
    thing_key = config.get(CONF_THINGKEY)
    method = "POST"
    auth = None
    verify_ssl = DEFAULT_VERIFY_SSL
    timeout = 69

    payload = {
        "lastUpdated":{
            "command":"lastUpdated",
            "params":{
                "thingKey": thing_key,
            }
        },
        "thing.find":{
            "command":"thing.find",
            "params":{
                "thingKey": thing_key,
            }
        },
        "total.energyGenerating":{
            "command":"property.total",
            "params":{
                "thingKey": thing_key,
                "key": "energyGenerating"
            }
        },
        "total.energyCharging":{
            "command":"property.total",
            "params":{
                "thingKey": thing_key,
                "key": "energyCharging"
            }
        },
        "total.energyDischarging":{
            "command":"property.total",
            "params":{
                "thingKey": thing_key,
                "key": "energyDischarging"
            }
        },
        "total.energyExporting":{
            "command":"property.total",
            "params":{
                "thingKey": thing_key,
                "key": "energyExporting"
            }
        },
        "total.energyImporting":{
            "command":"property.total",
            "params":{
                "thingKey": thing_key,
                "key": "energyImporting"
            }
        },
        "total.energyConsuming":{
            "command":"property.total",
            "params":{
                "thingKey": thing_key,
                "key": "energyConsuming"
            }
        },
        "total.energyAutoconsuming":{
            "command":"property.total",
            "params":{
                "thingKey": thing_key,
                "key": "energyAutoconsuming"
            }
        },
        "current.powerGenerating":{
            "command":"property.current",
            "params":{
                "thingKey": thing_key,
                "key": "powerGenerating"
            }
        },
        "current.energyGenerating":{
            "command":"property.current",
            "params":{
                "thingKey": thing_key,
                "key": "energyGenerating"
            }
        },
        "current.batteryCycletime":{
            "command":"property.current",
            "params":{
                "thingKey": thing_key,
                "key": "batteryCycletime"
            }
        },
        "current.batterySoC":{
            "command":"property.current",
            "params":{
                "thingKey": thing_key,
                "key": "batterySoC"
            }
        },
        "current.powerCharging":{
            "command":"property.current",
            "params":{
                "thingKey": thing_key,
                "key": "powerCharging"
            }
        },
        "current.powerDischarging":{
            "command":"property.current",
            "params":{
                "thingKey": thing_key,
                "key": "powerDischarging"
            }
        },
        "current.powerExporting":{
            "command":"property.current",
            "params":{
                "thingKey": thing_key,
                "key": "powerExporting"
            }
        },
        "current.powerImporting":{
            "command":"property.current",
            "params":{
                "thingKey": thing_key,
                "key": "powerImporting"
            }
        },
        "current.powerConsuming":{
            "command":"property.current",
            "params":{
                "thingKey": thing_key,
                "key": "powerConsuming"
            }
        },
        "current.powerAutoconsuming":{
            "command":"property.current",
            "params":{
                "thingKey": thing_key,
                "key": "powerAutoconsuming"
            }
        },
        "current.energyCharging":{
            "command":"property.current",
            "params":{
                "thingKey": thing_key,
                "key": "energyCharging"
            }
        },
        "current.energyDischarging":{
            "command":"property.current",
            "params":{
                "thingKey": thing_key,
                "key": "energyDischarging"
            }
        },
        "current.energyExporting":{
            "command":"property.current",
            "params":{
                "thingKey": thing_key,
                "key": "energyExporting"
            }
        },
        "current.energyImporting":{
            "command":"property.current",
            "params":{
                "thingKey": thing_key,
                "key": "energyImporting"
            }
        },
        "current.energyConsuming":{
            "command":"property.current",
            "params":{
                "thingKey": thing_key,
                "key": "energyConsuming"
            }
        },
        "current.energyAutoconsuming":{
            "command":"property.current",
            "params":{
                "thingKey": thing_key,
                "key": "energyAutoconsuming"
            }
        }
    }
    string_payload = json.dumps(payload)
    
    headers = {
        "Authorization": auth_key
    }

    _LOGGER.debug("method: %s", method)
    _LOGGER.debug("_ENDPOINT: %s", _ENDPOINT)
    _LOGGER.debug("auth: %s", auth)
    _LOGGER.debug("headers: %s", headers)
    _LOGGER.debug("payload: %s", string_payload)
    _LOGGER.debug("verify_ssl: %s", verify_ssl)
    
    rest = RestData(hass, method, _ENDPOINT, auth, headers, None, string_payload, verify_ssl, timeout)
    await rest.async_update()

    if rest.data is None:
        _LOGGER.error("Unable to start fetching data from ZCSAzzurro")
        # return False

    async_add_entities([DSSoutputSensor(rest, name)])

class DSSoutputSensor(SensorEntity):
    """Representation of a ZCSAzzurro sensor."""

    _attr_state_class = STATE_CLASS_MEASUREMENT
    _attr_device_class = DEVICE_CLASS_ENERGY
    _attr_native_unit_of_measurement = ENERGY_WATT_HOUR

    def __init__(self, rest, name):
        """Initialize a ZCSAzzurro sensor."""
        self.rest = rest
        self._attr_name = name
        self._attributes = None
        self.dssoutput = None
        self._state = False


    @property
    def state(self):
        """Return the state of the device."""
        value = self._state
        _LOGGER.debug("Return the state: %s", value)
        return value


    @property
    def extra_state_attributes(self):
        """Return the state attributes of the monitored installation."""
        if self.dssoutput is not None:
            try:
                _LOGGER.debug("Return the state attributes")
                return {
                    "lastUpdated": self.dssoutput["lastUpdated"]["params"]["value"],
                    "thing.find": self.dssoutput["thing.find"]["params"]["value"],
                    "total": {
                        "energyGenerating": self.dssoutput["total.energyGenerating"]["params"]["value"],
                        "energyCharging": self.dssoutput["total.energyCharging"]["params"]["value"],
                        "energyDischarging": self.dssoutput["total.energyDischarging"]["params"]["value"],
                        "energyExporting": self.dssoutput["total.energyExporting"]["params"]["value"],
                        "energyImporting": self.dssoutput["total.energyImporting"]["params"]["value"],
                        "energyConsuming": self.dssoutput["total.energyConsuming"]["params"]["value"],
                        "energyAutoconsuming": self.dssoutput["total.energyAutoconsuming"]["params"]["value"]
                    },
                    "current": {
                        "energyGenerating": self.dssoutput["current.energyGenerating"]["params"]["value"],
                        "powerGenerating": self.dssoutput["current.powerGenerating"]["params"]["value"],
                        "batteryCycletime": self.dssoutput["current.batteryCycletime"]["params"]["value"],
                        "batterySoC": self.dssoutput["current.batterySoC"]["params"]["value"],
                        "powerCharging": self.dssoutput["current.powerCharging"]["params"]["value"],
                        "powerDischarging": self.dssoutput["current.powerDischarging"]["params"]["value"],
                        "powerExporting": self.dssoutput["current.powerExporting"]["params"]["value"],
                        "powerImporting": self.dssoutput["current.powerImporting"]["params"]["value"],
                        "powerConsuming": self.dssoutput["current.powerConsuming"]["params"]["value"],
                        "powerAutoconsuming": self.dssoutput["current.powerAutoconsuming"]["params"]["value"],
                        "energyCharging": self.dssoutput["current.energyCharging"]["params"]["value"],
                        "energyDischarging": self.dssoutput["current.energyDischarging"]["params"]["value"],
                        "energyExporting": self.dssoutput["current.energyExporting"]["params"]["value"],
                        "energyImporting": self.dssoutput["current.energyImporting"]["params"]["value"],
                        "energyConsuming": self.dssoutput["current.energyConsuming"]["params"]["value"],
                        "energyAutoconsuming": self.dssoutput["current.energyAutoconsuming"]["params"]["value"],
                    },
                }
            except TypeError:
                _LOGGER.error("Error cannot find all required keys: %s", self.dssoutput)
                return {
                    "lastUpdated": False,
                    "thing.find": False,
                    "total": {
                        "energyGenerating": 0,
                        "energyCharging": 0,
                        "energyDischarging": 0,
                        "energyExporting": 0,
                        "energyImporting": 0,
                        "energyConsuming": 0,
                        "energyAutoconsuming": 0
                    },
                    "current": {
                        "energyGenerating": 0,
                        "powerGenerating": 0,
                        "batteryCycletime": 0,
                        "batterySoC": 0,
                        "powerCharging": 0,
                        "powerDischarging": 0,
                        "powerExporting": 0,
                        "powerImporting": 0,
                        "powerConsuming": 0,
                        "powerAutoconsuming": 0,
                        "energyCharging": 0,
                        "energyDischarging": 0,
                        "energyExporting": 0,
                        "energyImporting": 0,
                        "energyConsuming": 0,
                        "energyAutoconsuming": 0,
                    },
                }
        else:
            return {
                "lastUpdated": False,
                "thing.find": False,
                "total": {
                    "energyGenerating": 0,
                    "energyCharging": 0,
                    "energyDischarging": 0,
                    "energyExporting": 0,
                    "energyImporting": 0,
                    "energyConsuming": 0,
                    "energyAutoconsuming": 0
                },
                "current": {
                    "energyGenerating": 0,
                    "powerGenerating": 0,
                    "batteryCycletime": 0,
                    "batterySoC": 0,
                    "powerCharging": 0,
                    "powerDischarging": 0,
                    "powerExporting": 0,
                    "powerImporting": 0,
                    "powerConsuming": 0,
                    "powerAutoconsuming": 0,
                    "energyCharging": 0,
                    "energyDischarging": 0,
                    "energyExporting": 0,
                    "energyImporting": 0,
                    "energyConsuming": 0,
                    "energyAutoconsuming": 0,
                },
            }

    async def async_update(self):
        """Get the latest data from the ZCSAzzurro API and updates the state."""
        await self.rest.async_update()
        self._async_update_from_rest_data()

    async def async_added_to_hass(self):
        """Ensure the data from the initial update is reflected in the state."""
        self._async_update_from_rest_data()

    @callback
    def _async_update_from_rest_data(self):
        """Update state from the rest data."""
        try:
            json_dict = self.rest.data
            if json_dict is not None:
                try:
                    _LOGGER.debug("Data fetched from resource: %s", json_dict)
                    json_dict = json.loads(json_dict)
                    self.dssoutput = json_dict
                    self._state = self.dssoutput["thing.find"]["params"]["value"] == True
                except ValueError:
                    _LOGGER.warning("REST result could not be parsed as JSON")
                    _LOGGER.debug("Erroneous JSON: %s", json_dict)
            else:
                _LOGGER.warning("Empty reply found when expecting JSON data")
                self.dssoutput = None
                self._state = False            
        except TypeError:
            self.dssoutput = None
            self._state = False
            _LOGGER.error("Unable to fetch data from ZCSAzzurro. Response: %s", self.rest.data)

