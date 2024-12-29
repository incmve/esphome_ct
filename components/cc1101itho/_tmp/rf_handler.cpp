#include "rf_handler.h"

class CC1101Fan : public PollingComponent, public fan::Fan {
 public:
  CC1101Fan(RFHandler *rf_handler, InternalGPIOPin *data_pin)
      : rf_handler_(rf_handler), data_pin_(data_pin) {}

  void setup() override {
    // Set up the data pin
    this->rf_handler_->setup_pin(this->data_pin_);
  }

 protected:
  RFHandler *rf_handler_;
  InternalGPIOPin *data_pin_;
};
