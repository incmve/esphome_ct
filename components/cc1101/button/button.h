#include "esphome/components/button/button.h"
#include "../rf_handler.h"

class CC1101Button : public button::Button, public Component {
 public:
  CC1101Button(RFHandler *rf_handler, InternalGPIOPin *data_pin, int command)
      : rf_handler_(rf_handler), data_pin_(data_pin), command_(command) {}

  void setup() override {
    // Set up the button pin
    this->rf_handler_->setup_pin(this->data_pin_);
  }

  void press_action() override {
    this->rf_handler_->sendCommand(this->command_);
  }

 protected:
  RFHandler *rf_handler_;
  InternalGPIOPin *data_pin_;
  int command_;
};
