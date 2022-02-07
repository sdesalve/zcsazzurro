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

SCAN_INTERVAL = timedelta(minutes=2)

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
         "realtimeData":  { 
              "command": "realtimeData", 
              "params": { 
                  "thingKey": thing_key,
                  "requiredValues": "*"
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

    async_add_entities([DSSoutputSensor(rest, name, thing_key)])

class DSSoutputSensor(SensorEntity):
    """Representation of a ZCSAzzurro sensor."""

    _attr_state_class = STATE_CLASS_MEASUREMENT
    _attr_device_class = DEVICE_CLASS_ENERGY
    _attr_native_unit_of_measurement = ENERGY_WATT_HOUR

    def __init__(self, rest, name, thing_key):
        """Initialize a ZCSAzzurro sensor."""
        self.rest = rest
        self._attr_name = name
        self._attributes = None
        self.dssoutput = None
        self._state = False
        self._thing_key = thing_key

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
            thing_key = self._thing_key
            _LOGGER.debug("Return the state attributes")
            _LOGGER.debug("thingkey: %s", thing_key)
            
            try: lastUpdated = self.dssoutput["realtimeData"]["params"]["value"][0][thing_key]["lastUpdate"]
            except: lastUpdated = 0
             
            try: energyGeneratingTotal = self.dssoutput["realtimeData"]["params"]["value"][0][thing_key]["energyGeneratingTotal"]
            except: energyGeneratingTotal = 0

            try: energyChargingTotal = self.dssoutput["realtimeData"]["params"]["value"][0][thing_key]["energyChargingTotal"]
            except: energyChargingTotal = 0

            try: energyDischargingTotal = self.dssoutput["realtimeData"]["params"]["value"][0][thing_key]["energyDischargingTotal"]
            except: energyDischargingTotal = 0

            try: energyExportingTotal = self.dssoutput["realtimeData"]["params"]["value"][0][thing_key]["energyExportingTotal"]
            except: energyExportingTotal = 0

            try: energyImportingTotal = self.dssoutput["realtimeData"]["params"]["value"][0][thing_key]["energyImportingTotal"]
            except: energyImportingTotal = 0

            try: energyConsumingTotal = self.dssoutput["realtimeData"]["params"]["value"][0][thing_key]["energyConsumingTotal"]
            except: energyConsumingTotal = 0

            try: energyAutoconsumingTotal = self.dssoutput["realtimeData"]["params"]["value"][0][thing_key]["energyAutoconsumingTotal"]
            except: energyAutoconsumingTotal = 0

            try: energyGenerating = self.dssoutput["realtimeData"]["params"]["value"][0][thing_key]["energyGenerating"]
            except: energyGenerating = 0

            try: powerGenerating = self.dssoutput["realtimeData"]["params"]["value"][0][thing_key]["powerGenerating"]
            except: powerGenerating = 0

            try: batteryCycletime = self.dssoutput["realtimeData"]["params"]["value"][0][thing_key]["batteryCycletime"]
            except: batteryCycletime = 0

            try: batterySoC = self.dssoutput["realtimeData"]["params"]["value"][0][thing_key]["batterySoC"]
            except: batterySoC = 0

            try: powerCharging = self.dssoutput["realtimeData"]["params"]["value"][0][thing_key]["powerCharging"]
            except: powerCharging = 0

            try: powerDischarging = self.dssoutput["realtimeData"]["params"]["value"][0][thing_key]["powerDischarging"]
            except: powerDischarging = 0

            try: powerExporting = self.dssoutput["realtimeData"]["params"]["value"][0][thing_key]["powerExporting"]
            except: powerExporting = 0

            try: powerImporting = self.dssoutput["realtimeData"]["params"]["value"][0][thing_key]["powerImporting"]
            except: powerImporting = 0

            try: powerConsuming = self.dssoutput["realtimeData"]["params"]["value"][0][thing_key]["powerConsuming"]
            except: powerConsuming = 0

            try: powerAutoconsuming = self.dssoutput["realtimeData"]["params"]["value"][0][thing_key]["powerAutoconsuming"]
            except: powerAutoconsuming = 0

            try: energyCharging = self.dssoutput["realtimeData"]["params"]["value"][0][thing_key]["energyCharging"]
            except: energyCharging = 0

            try: energyDischarging = self.dssoutput["realtimeData"]["params"]["value"][0][thing_key]["energyDischarging"]
            except: energyDischarging = 0

            try: energyExporting = self.dssoutput["realtimeData"]["params"]["value"][0][thing_key]["energyExporting"]
            except: energyExporting = 0

            try: energyImporting = self.dssoutput["realtimeData"]["params"]["value"][0][thing_key]["energyImporting"]
            except: energyImporting = 0

            try: energyConsuming = self.dssoutput["realtimeData"]["params"]["value"][0][thing_key]["energyConsuming"]
            except: energyConsuming = 0

            try: energyAutoconsuming = self.dssoutput["realtimeData"]["params"]["value"][0][thing_key]["energyAutoconsuming"]
            except: energyAutoconsuming = 0

            return {
                "lastUpdated": lastUpdated,
                "thing.find": thing_key,
                "total": {
                    "energyGenerating": energyGeneratingTotal,
                    "energyCharging": energyChargingTotal,
                    "energyDischarging": energyDischargingTotal,
                    "energyExporting": energyExportingTotal,
                    "energyImporting": energyImportingTotal,
                    "energyConsuming": energyConsumingTotal,
                    "energyAutoconsuming": energyAutoconsumingTotal,
                },
                "current": {
                    "energyGenerating": energyGenerating,
                    "powerGenerating": powerGenerating,
                    "batteryCycletime": batteryCycletime,
                    "batterySoC": batterySoC,
                    "powerCharging": powerCharging,
                    "powerDischarging": powerDischarging,
                    "powerExporting": powerExporting,
                    "powerImporting": powerImporting,
                    "powerConsuming": powerConsuming,
                    "powerAutoconsuming": powerAutoconsuming,
                    "energyCharging": energyCharging,
                    "energyDischarging": energyDischarging,
                    "energyExporting": energyExporting,
                    "energyImporting": energyImporting,
                    "energyConsuming": energyConsuming,
                    "energyAutoconsuming": energyAutoconsuming,
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
                    self._state = self.dssoutput["realtimeData"]["success"] == True
                except ValueError:
                    _LOGGER.warning("REST result could not be parsed as JSON")
                    _LOGGER.debug("Erroneous JSON: %s", json_dict)
            else:
                _LOGGER.warning("Empty reply found when expecting JSON data")
        except TypeError:
            _LOGGER.error("Unable to fetch data from ZCSAzzurro. Response: %s", self.rest.data)

