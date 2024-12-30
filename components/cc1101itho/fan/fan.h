#pragma once

#include "esphome/components/fan/fan.h"
#include "../cc1101_itho.h"

namespace esphome {
namespace c1101itho {

class CC1101IthoFan : public fan::Fan, public Parented<CC1101IthoComponent> {
 public:
  CC1101IthoFan(int speed_count, bool map_off_to_zero) : speed_count_(speed_count), map_off_to_zero_(map_off_to_zero) {}
  fan::FanTraits get_traits() override;

  void set_fan_speed(int speed);

 protected:
  void control(const fan::FanCall &call) override;

  int speed_count_{};
  bool map_off_to_zero_{};

  int Speed = -1;
  int LastSpeed = -1;
};

} // namespace c1101itho
} // namespace esphome 
