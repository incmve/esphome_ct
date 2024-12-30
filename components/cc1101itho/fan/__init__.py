from esphome import pins
from esphome.components import fan
import esphome.config_validation as cv
import esphome.codegen as cg
from esphome.cpp_helpers import gpio_pin_expression

from esphome.const import CONF_ID, CONF_NAME, CONF_DATA_PIN, CONF_SPEED_COUNT, CONF_DISABLED_BY_DEFAULT, CONF_RESTORE_MODE, ENTITY_CATEGORY_CONFIG, ICON_CHIP, ICON_SCALE

from .. import cc1101itho_ns, CC1101IthoComponent

MULTI_CONF = True

AUTO_LOAD = [ 'button', 'fan' ]

CONF_COMMAND = "command"
MAP_OFF_TO_ZERO = "map_off_to_zero"

# Define mapping manually
FAN_RESTORE_MODE_OPTIONS = {
    "ALWAYS_ON": fan.FanRestoreMode.ALWAYS_ON,
    "ALWAYS_OFF": fan.FanRestoreMode.ALWAYS_OFF,
}

CONFIG_SCHEMA = {
  cv.GenerateID(CONF_ID): cv.declare_id(CC1101IthoComponent),
  cv.Required(CONF_DATA_PIN): cv.All(pins.internal_gpio_input_pin_schema),
  cv.Required(MAP_OFF_TO_ZERO): cv.boolean,
  cv.Optional(CONF_NAME, default="Domestic Fan"): str,
  cv.Optional(CONF_SPEED_COUNT, default=3): cv.int_range(min=1, max=100),
  cv.Optional(CONF_DISABLED_BY_DEFAULT, default=False): cv.boolean,
  cv.Optional(CONF_RESTORE_MODE, default="ALWAYS_ON"): cv.enum(FAN_RESTORE_MODE_OPTIONS),
}

async def to_code(config):
    var = cg.new_Pvariable(config[CONF_ID], config[CONF_SPEED_COUNT], config[MAP_OFF_TO_ZERO])
    await cg.register_component(var, config)
    await fan.register_fan(var, config)

    data_pin = await gpio_pin_expression(config[CONF_DATA_PIN])
    cg.add(var.set_data_pin(data_pin))

