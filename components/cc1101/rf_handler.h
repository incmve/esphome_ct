#pragma once

#include "esphome/core/component.h"
#include "esphome/core/gpio.h"

class RFHandler {
 public:
  void setup_pin(InternalGPIOPin *data_pin) { 
    data
    this->data_pin_->setup();
    this->data_pin_->pin_mode(gpio::FLAG_INPUT);
  }

  void sendCommand(int command) {
    // Your RF sending logic here
    rf.sendCommand(command);
  }
 protected:
    InternalGPIOPin *data_pin_;
};
