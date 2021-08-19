# SDeSalve Home Assistant Integration: ZCSAzzurro

[![Buy me a coffee][buymeacoffee-shield]][buymeacoffee] [![Support my work on Paypal][paypal-shield]][paypal]

This integration allows you to polling your ZCS Azzurro inverter's realtime data from API.

## Usage:
Obtain your Device Serial/ThingKey and your Authorization header value from ZCS Zucchetti
Add to configuration.yaml:

```
sensor:
  - platform: zcsazzurro
    name: test_zcsazzurro
    thingkey: [YOUR DEVICE SERIAL - THINGKEY]
    authkey: [YOUR AUTHORIZATION HEADER VALUE]
    
```

## Authors & contributors

The original setup of this repository is by [SDeSalve][sdesalve].

## License

Copyright (c) 2021 SDeSalve

See [LICENSE][license]


[![hacs_badge](https://img.shields.io/badge/HACS-Custom-orange.svg)](https://github.com/sdesalve/zcsazzurro)

[buymeacoffee-shield]: https://www.buymeacoffee.com/assets/img/guidelines/download-assets-sm-2.svg
[buymeacoffee]: https://www.buymeacoffee.com/sdesalve
[paypal-shield]: https://www.paypalobjects.com/en_US/i/btn/btn_donateCC_LG.gif
[paypal]: https://paypal.me/SDeSalve
[license]: https://github.com/sdesalve/zcsazzurro/LICENSE.md
[sdesalve]: https://github.com/sdesalve
