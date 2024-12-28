from esphome import pins
from esphome.components import button, fan
import esphome.config_validation as cv
import esphome.codegen as cg
from esphome.cpp_helpers import gpio_pin_expression

from esphome.const import CONF_ID, CONF_NAME, CONF_OUTPUT_ID, CONF_DATA_PIN, CONF_SPEED_COUNT, CONF_DISABLED_BY_DEFAULT, CONF_RESTORE_MODE

MULTI_CONF = True

AUTO_LOAD = [ 'button', 'fan' ]

cc1101_ns = cg.esphome_ns.namespace('cc1101')
CC1101Fan = cc1101_ns.class_('CC1101Fan', cg.PollingComponent, fan.Fan)
CC1101Button = cc1101_ns.class_('CC1101Button', button.Button)
RFHandler = cc1101_ns.class_('RFHandler', cg.Component)

CONF_FAN = "fan"
CONF_BUTTON = "button"
CONF_BUTTONS = "buttons"
CONF_COMMAND = "command"
CONF_RF_HANDLER_ID = "rf_handler_id"
MAP_OFF_TO_ZERO = "map_off_to_zero"

# Define mapping manually
FAN_RESTORE_MODE_OPTIONS = {
    "ALWAYS_ON": fan.FanRestoreMode.ALWAYS_ON,
    "ALWAYS_OFF": fan.FanRestoreMode.ALWAYS_OFF,
}

CONFIG_SCHEMA = cv.COMPONENT_SCHEMA.extend({
  cv.Required(CONF_FAN): fan.FAN_SCHEMA.extend({
    cv.GenerateID(CONF_OUTPUT_ID): cv.declare_id(CC1101Fan),
    cv.GenerateID(CONF_RF_HANDLER_ID): cv.declare_id(RFHandler),
    cv.Required(CONF_DATA_PIN): cv.All(pins.internal_gpio_input_pin_schema),
    cv.Required(MAP_OFF_TO_ZERO): cv.boolean,
    cv.Optional(CONF_NAME, default="Domestic Fan"): str,
    cv.Optional(CONF_SPEED_COUNT, default=3): cv.int_range(min=1, max=100),
    cv.Optional(CONF_DISABLED_BY_DEFAULT, default=False): cv.boolean,
    cv.Optional(CONF_RESTORE_MODE, default="ALWAYS_ON"): cv.enum(FAN_RESTORE_MODE_OPTIONS),
 }),
 cv.Optional(CONF_BUTTONS): cv.ensure_list({
    cv.GenerateID(): cv.declare_id(CC1101Button),
    cv.Required(CONF_NAME): cv.string,
    cv.Required(CONF_COMMAND): cv.int_,
#    cv.Required(CONF_DATA_PIN): cv.All(pins.internal_gpio_input_pin_schema),
 }),
})

async def to_code(config):
    if CONF_FAN not in config:
        raise ValueError("Fan configuration is required.")

    rf_handler = cg.new_Pvariable(config[CONF_FAN][CONF_RF_HANDLER_ID])
    await cg.register_component(rf_handler, config)

    var = cg.new_Pvariable(config[CONF_FAN][CONF_OUTPUT_ID], rf_handler, config[CONF_FAN][CONF_SPEED_COUNT], config[CONF_FAN][MAP_OFF_TO_ZERO])
    await cg.register_component(var, config)
    await fan.register_fan(var, config[CONF_FAN])

    data_pin = await gpio_pin_expression(config[CONF_FAN][CONF_DATA_PIN])
    cg.add(var.set_data_pin(data_pin))

    for conf in config.get(CONF_BUTTONS, []):
      button_component = cg.new_Pvariable(conf[CONF_ID], rf_handler, conf[CONF_COMMAND])
      await cg.register_component(button_component, conf)
      cg.add(button_component)
      await cg.register_component(button_component, conf)

    return var

