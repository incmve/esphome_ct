from esphome import pins
from esphome.components import button, fan
import esphome.config_validation as cv
import esphome.codegen as cg
from esphome.cpp_helpers import gpio_pin_expression

from esphome.const import CONF_ID, CONF_NAME, CONF_DATA_PIN, CONF_SPEED_COUNT, CONF_DISABLED_BY_DEFAULT, CONF_RESTORE_MODE, ENTITY_CATEGORY_CONFIG, ICON_CHIP, ICON_SCALE

MULTI_CONF = True

AUTO_LOAD = [ 'button', 'fan' ]

cc1101itho_ns = cg.esphome_ns.namespace('cc1101itho')
CC1101Itho = cc1101itho_ns.class_('CC1101IthoComponent', cg.PollingComponent)

CONF_FAN = "fan"
CONF_BUTTON = "button"
CONF_TIMER10_BUTTON = "timer_10_minutes"
CONF_TIMER20_BUTTON = "timer_20_minutes"
CONF_COMMAND = "command"
MAP_OFF_TO_ZERO = "map_off_to_zero"

# Define mapping manually
FAN_RESTORE_MODE_OPTIONS = {
    "ALWAYS_ON": fan.FanRestoreMode.ALWAYS_ON,
    "ALWAYS_OFF": fan.FanRestoreMode.ALWAYS_OFF,
}

CC1101IthoTimer10Button = cc1101itho_ns.class_(
    "CC1101IthoTimer10Button",
    button.Button,
)
CC1101IthoTimer20Button = cc1101itho_ns.class_(
    "CC1101IthoTimer20Button",
    button.Button,
)

CONFIG_SCHEMA = cv.COMPONENT_SCHEMA.extend({
  cv.Required(CONF_FAN): fan.FAN_SCHEMA.extend({
    cv.GenerateID(CONF_ID): cv.declare_id(CC1101Itho),
    cv.Required(CONF_DATA_PIN): cv.All(pins.internal_gpio_input_pin_schema),
    cv.Required(MAP_OFF_TO_ZERO): cv.boolean,
    cv.Optional(CONF_NAME, default="Domestic Fan"): str,
    cv.Optional(CONF_SPEED_COUNT, default=3): cv.int_range(min=1, max=100),
    cv.Optional(CONF_DISABLED_BY_DEFAULT, default=False): cv.boolean,
    cv.Optional(CONF_RESTORE_MODE, default="ALWAYS_ON"): cv.enum(FAN_RESTORE_MODE_OPTIONS),
 }),
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
})

async def to_code(config):
    if CONF_FAN not in config:
        raise ValueError("Fan configuration is required.")

    var = cg.new_Pvariable(config[CONF_FAN][CONF_ID], config[CONF_FAN][CONF_SPEED_COUNT], config[CONF_FAN][MAP_OFF_TO_ZERO])
    await cg.register_component(var, config)
    await fan.register_fan(var, config[CONF_FAN])

    data_pin = await gpio_pin_expression(config[CONF_FAN][CONF_DATA_PIN])
    cg.add(var.set_data_pin(data_pin))

    parent = await cg.get_variable(config[CONF_FAN][CONF_ID])
    if timer10 := config.get(CONF_TIMER10_BUTTON):
        b = await button.new_button(timer10)
        await cg.register_parented(b, parent)
    if timer20 := config.get(CONF_TIMER20_BUTTON):
        b = await button.new_button(timer20)
        await cg.register_parented(b, parent)

    return var

