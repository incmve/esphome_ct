## Howto

### ESPhome configuration

#### Top part

```yaml
external_components:
  - source: 
      type: git
      url: https://github.com/CoMPaTech/esphome_ct
    # refresh: 3600s # only set this briefly otherwise it just refreshes daily, see https://esphome.io/components/external_components#external-components-refresh for setting refresh too low
```

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
