#include "esphome/core/log.h"
#include "button.h"

namespace esphome {
namespace cc1101fan {

static const char *const BUTTON_TAG = "cc1101ithofan.button";

void CC1101IthoTimer10Button::press_action() {
  ESP_LOGI(BUTTON_TAG, "Starting 10 minute timer on Itho Fan");
  // this->parent_->run_offset_calibrations();
}

void CC1101IthoTimer20Button::press_action() {
  ESP_LOGI(BUTTON_TAG, "Starting 20 minute timer on Itho Fan");
  // this->parent_->run_offset_calibrations();
}

} // namespace cc1101fan
} // namespace esphome
