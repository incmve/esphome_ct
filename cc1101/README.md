## Howto

### ESPhome configuration

#### Top part

external_components:
  - source: github://esphome/esphome@dev
    components: [ cc1101 ]

#### FAN part

```yaml
fan:
  - platform: "c1101"
    speed_count: 3
    name: "Mechanical Fan"
    data_pin: D1
    map_off_to_zero: True
```


## Known limitations

No option for the timer button (e.g. single, double, triple=click)

Just low/medium/high ... set speed_count to 4 if you need full

PIN is not configurable (it looks like it, but it's not)
