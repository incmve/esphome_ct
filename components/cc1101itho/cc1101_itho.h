#pragma once

#include "esphome/components/button/button.h"
#include "esphome/components/fan/fan.h"
#include "esphome/core/component.h"
#include "esphome/core/gpio.h"

namespace esphome {
namespace c1101itho {

#ifndef ITHOPACKET_H_
#define ITHOPACKET_H_
/*
 * Author: Klusjesman, modified bij supersjimmie for Arduino/ESP8266
 */

enum IthoMessageType {
    ithomsg_unknown = 0,
    ithomsg_control = 1,
    ithomsg_join = 2,
     ithomsg_leave = 3
};
 
 //do not change enum because they are used in calculations!
enum IthoCommand {
    IthoUnknown = 0,

    IthoJoin = 4,
    IthoLeave = 8,

    IthoStandby = 34,
    IthoLow = 35,	
    IthoMedium = 36,	
    IthoHigh = 37,
    IthoFull = 38,

    IthoTimer1 = 41,
    IthoTimer2 = 51,
    IthoTimer3 = 61,

    //duco c system remote
    DucoStandby = 251,
    DucoLow = 252,
    DucoMedium = 253,
    DucoHigh = 254
};


class IthoPacket {
    public:
    uint8_t deviceId1[6];
    uint8_t deviceId2[8];
    IthoMessageType messageType;
    IthoCommand command;
    IthoCommand previous;

    uint8_t counter;		//0-255, counter is increased on every remote button press
};

#endif /* ITHOPACKET_H_ */

class CC1101IthoComponent : public PollingComponent {
 public:
  void setup() override;
  void set_data_pin(InternalGPIOPin *data_pin) { data_pin_ = data_pin; }
  void publish_state();

  static void ITHOinterrupt();
  static void ITHOcheck();

 protected:
  InternalGPIOPin *data_pin_;
};

class CC1101IthoTimer10Button : public button::Button, public Parented<CC1101IthoComponent> {
 public:
  CC1101IthoTimer10Button() = default;

 protected:
  void press_action() override;
};

class CC1101IthoTimer20Button : public button::Button, public Parented<CC1101IthoComponent> {
 public:
  CC1101IthoTimer20Button() = default;

 protected:
  void press_action() override;
};

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
