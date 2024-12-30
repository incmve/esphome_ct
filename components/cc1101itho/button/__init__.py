from esphome import pins
from esphome.components import button, fan
import esphome.config_validation as cv
import esphome.codegen as cg
from esphome.cpp_helpers import gpio_pin_expression

from esphome.const import CONF_ID, CONF_NAME, CONF_DATA_PIN, CONF_SPEED_COUNT, CONF_DISABLED_BY_DEFAULT, CONF_RESTORE_MODE, ENTITY_CATEGORY_CONFIG, ICON_CHIP, ICON_SCALE

from .. import cc1101itho_ns, CC1101IthoComponent

MULTI_CONF = True

AUTO_LOAD = [ 'button', 'fan' ]

CONF_FAN = "fan"
CONF_BUTTON = "button"
CONF_TIMER10_BUTTON = "timer_10_minutes"
CONF_TIMER20_BUTTON = "timer_20_minutes"

CC1101IthoTimer10Button = cc1101itho_ns.class_(
    "CC1101IthoTimer10Button",
    button.Button,
)
CC1101IthoTimer20Button = cc1101itho_ns.class_(
    "CC1101IthoTimer20Button",
    button.Button,
)

CONFIG_SCHEMA = {
  cv.GenerateID(CONF_ID): cv.declare_id(CC1101IthoComponent),
  cv.Optional(CONF_TIMER10_BUTTON): button.button_schema(
    CC1101IthoTimer10Button,
    entity_category=ENTITY_CATEGORY_CONFIG,
    icon=ICON_SCALE,
  ),
  cv.Optional(CONF_TIMER20_BUTTON): button.button_schema(
    CC1101IthoTimer20Button,
    entity_category=ENTITY_CATEGORY_CONFIG,
    icon=ICON_CHIP,
  ),
}

async def to_code(config):
    if timer10 := config.get(CONF_TIMER10_BUTTON):
        b = await button.new_button(timer10)
        await cg.register_parented(b, parent)
    if timer20 := config.get(CONF_TIMER20_BUTTON):
        b = await button.new_button(timer20)
        await cg.register_parented(b, parent)

    return var

