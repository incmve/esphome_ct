#pragma once

#include "esphome/components/button/button.h"
#include "../cc1101_itho.h"

namespace esphome {
namespace c1101itho {

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

} // namespace c1101itho
} // namespace esphome 
