# SDeSalve Home Assistant Integration: ZCSAzzurro

[![Buy me a coffee][buymeacoffee-shield]][buymeacoffee] [![Support my work on Paypal][paypal-shield]][paypal]

This integration allows you to polling your ZCS Azzurro inverter's realtime data from API.

## Usage:
Obtain your Device Serial/ThingKey and your Authorization header value from ZCS Zucchetti.

Add to configuration.yaml:

```
sensor:
  - platform: zcsazzurro
    name: test_zcsazzurro
    thingkey: [YOUR DEVICE SERIAL - THINGKEY]
    authkey: [YOUR AUTHORIZATION HEADER VALUE]
    
```

## Example for extract sensor 
```
template:
  - sensor:

      - name: "Energy Generating ZCS"
        unit_of_measurement: "kWh"
        state: >
          {% set energy = states.sensor.zcsazzurro.attributes.current.energyGenerating | float | default (0) %}
          {{ energy | round(2) }}
        state_class: measurement
        device_class: energy
        icon: mdi:solar-power

      - name: "Power Generating ZCS"
        unit_of_measurement: "W"
        state: >
          {% set power = states.sensor.zcsazzurro.attributes.current.powerGenerating | int | default (0) %}
          {{ power }}
        state_class: measurement
        device_class: power
        icon: mdi:solar-power

      - name: "Energy Exporting ZCS"
        unit_of_measurement: "kWh"
        state: >
          {% set energy = states.sensor.zcsazzurro.attributes.current.energyExporting | float | default (0) %}
          {{ energy | round(2) }}
        state_class: measurement
        device_class: energy
        icon: mdi:solar-power
   
      - name: "Energy Importing ZCS"
        unit_of_measurement: "kWh"
        state: >
          {% set energy = states.sensor.zcsazzurro.attributes.current.energyImporting | float | default (0) %}
          {{ energy | round(2) }}
        state_class: measurement
        device_class: energy
        icon: mdi:solar-power
```

## Example sensor for energy panel
```
utility_meter:
  total_energy_generating_zcs:
    source: sensor.energy_generating_zcs
    cycle: daily

  total_energy_exporting_zcs:
    source: sensor.energy_exporting_zcs
    cycle: daily

  total_energy_importing_zcs:
    source: sensor.energy_importing_zcs
    cycle: daily
```

## Authors & contributors

The original setup of this repository is by [SDeSalve][sdesalve].

## License

Copyright (c) 2021 SDeSalve

See [LICENSE][license]

## Trademark legal notice

This integration is not created, developed, affiliated, supported, maintained or endorsed by **Zucchetti Centro Sistemi S.p.A.**.
All product names, logos, brands, trademarks and registered trademarks are property of their respective owners. All company, product, and service names used are for identification purposes only.
Use of these names, logos, trademarks, and brands does not imply endorsement.


[![hacs_badge](https://img.shields.io/badge/HACS-Custom-orange.svg)](https://github.com/sdesalve/zcsazzurro)

[buymeacoffee-shield]: https://www.buymeacoffee.com/assets/img/guidelines/download-assets-sm-2.svg
[buymeacoffee]: https://www.buymeacoffee.com/sdesalve
[paypal-shield]: https://www.paypalobjects.com/en_US/i/btn/btn_donateCC_LG.gif
[paypal]: https://paypal.me/SDeSalve
[license]: https://github.com/sdesalve/zcsazzurro/LICENSE.md
[sdesalve]: https://github.com/sdesalve
