from esphome import pins
from esphome.components import button, fan
import esphome.config_validation as cv
import esphome.codegen as cg
from esphome.cpp_helpers import gpio_pin_expression

from esphome.const import CONF_OUTPUT_ID, CONF_DATA_PIN

cc1101fan_ns = cg.esphome_ns.namespace("cc1101fan")
CC1101Fan = cc1101fan_ns.class_("CC1101Fan", cg.PollingComponent)

MAP_OFF_TO_ZERO = "map_off_to_zero"

# Define mapping manually
FAN_RESTORE_MODE_OPTIONS = {
    "ALWAYS_ON": fan.FanRestoreMode.ALWAYS_ON,
    "ALWAYS_OFF": fan.FanRestoreMode.ALWAYS_OFF,
}

CONFIG_SCHEMA = cv.COMPONENT_SCHEMA.extend({
  cv.Required("fan"): fan.FAN_SCHEMA.extend({
    cv.GenerateID(CONF_OUTPUT_ID): cv.declare_id(CC1101Fan),
    cv.Required(CONF_DATA_PIN): cv.All(pins.internal_gpio_input_pin_schema),
    cv.Required(MAP_OFF_TO_ZERO): cv.boolean,
    cv.Optional(CONF_NAME, default="Domestic Fan"): str,
    cv.Optional(CONF_SPEED_COUNT, default=3): cv.int_range(min=1, max=100),
    cv.Optional(CONF_DISABLED_BY_DEFAULT, default=False): cv.boolean,
    cv.Optional(CONF_RESTORE_MODE, default="ALWAYS_ON"): cv.enum(FAN_RESTORE_MODE_OPTIONS),
 }),
 cv.Optional("buttons"): cv_ensure_list({
    cv.Required(CONF_NAME): cv.string,
    cv.Required("command"): cv.int_,
    cv.Required(CONF_DATA_PIN): cv.All(pins.internal_gpio_input_pin_schema),
 }),
})

async def to_code(config):
    var = cg.new_Pvariable(config["fan"][CONF_OUTPUT_ID])
    await cg.register_component(var, config)

    if "fan" not in config:
        raise Exception

    data_pin = await gpio_pin_expression(config["fan"][CONF_DATA_PIN])
    cg.add(var.set_data_pin(data_pin))

    fan_component = cg.new_Pvariable(config["fan"][CONF_SPEED_COUNT], config["fan"][MAP_OFF_TO_ZERO])
    cg.add(fan_component.set_rf_handler(rf_handler))

    for conf in config.get("buttons", []):
      data_pin = await gpio_pin_expression(config["fan"][CONF_DATA_PIN])
      button_component = cg.new_Pvariable(conf[CONF_NAME], rf_handler, data_pin, conf["command"])
      cg.add(button_component)

    if CONF_PRESET_MODES in config:
        cg.add(var.set_preset_modes(config[CONF_PRESET_MODES]))

    return var

