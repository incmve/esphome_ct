import esphome.codegen as cg
from esphome.components import button
import esphome.config_validation as cv
from esphome.const import CONF_OUTPUT_ID, CONF_DATA_PIN, DEVICE_CLASS_IDENTIFY, ICON_PULSE, DEVICE_CLASS_TIMESTAMP, ICON_TIMER

from .. import CONF_LD2410_ID, LD2410Component, ld2410_ns

CONF_BUTTON_JOIN= "button_join"
JoinButton = ld2410_ns.class_("C1101JoinButton", button.Button)

CONF_BUTTON_TIMER_1= "button_timer_1"
Timer1Button = ld2410_ns.class_("C1101Timer1Button", button.Button)
CONF_BUTTON_TIMER_2= "button_timer_2"
Timer2Button = ld2410_ns.class_("C1101Timer3Button", button.Button)
CONF_BUTTON_TIMER_3= "button_timer_3"
Timer3Button = ld2410_ns.class_("C1101Timer4Button", button.Button)


CONFIG_SCHEMA = {
  cv.GenerateID(CONF_OUTPUT_ID): cv.declare_id(CC1101Fan),
  cv.Required(CONF_DATA_PIN): cv.All(pins.internal_gpio_input_pin_schema),
  cv.Optional(CONF_BUTTON_JOIN): button.button_schema(
        JoinButton,
        device_class=DEVICE_CLASS_IDENTIFY,
        entity_category=ENTITY_CATEGORY_CONFIG,
        icon=ICON_PULSE,
  ),
  cv.Optional(CONF_BUTTON_TIMER_1): button.button_schema(
        Timer1Button,
        device_class=DEVICE_CLASS_TIMESTAMP,
        entity_category=ENTITY_CATEGORY_CONFIG,
        icon=ICON_TIMER,
  ),
  cv.Optional(CONF_BUTTON_TIMER_2): button.button_schema(
        Timer2Button,
        device_class=DEVICE_CLASS_TIMESTAMP,
        entity_category=ENTITY_CATEGORY_CONFIG,
        icon=ICON_TIMER,
  ),
  cv.Optional(CONF_BUTTON_TIMER_3): button.button_schema(
        Timer3Button,
        device_class=DEVICE_CLASS_TIMESTAMP,
        entity_category=ENTITY_CATEGORY_CONFIG,
        icon=ICON_TIMER,
  ),
}).extend(cv.COMPONENT_SCHEMA)

async def to_code(config):
    var = cg.new_Pvariable(config[CONF_OUTPUT_ID])
    await cg.register_component(var, config)

    if button := config.get(CONF_BUTTON_JOIN):
        b = await button.new_button(button)
        await cg.register_parented(b, config[CONF_OUTPUT_ID])
    if button := config.get(CONF_BUTTON_TIMER_1):
        b = await button.new_button(button)
        await cg.register_parented(b, config[CONF_OUTPUT_ID])
    if button := config.get(CONF_BUTTON_TIMER_2):
        b = await button.new_button(button)
        await cg.register_parented(b, config[CONF_OUTPUT_ID])
    if button := config.get(CONF_BUTTON_TIMER_3):
        b = await button.new_button(button)
        await cg.register_parented(b, config[CONF_OUTPUT_ID])



CONF_QUERY_PARAMS = "query_params"

CONFIG_SCHEMA = {
    cv.GenerateID(CONF_LD2410_ID): cv.use_id(LD2410Component),
    cv.Optional(CONF_RESTART): button.button_schema(
        RestartButton,
        device_class=DEVICE_CLASS_RESTART,
        entity_category=ENTITY_CATEGORY_DIAGNOSTIC,
        icon=ICON_RESTART,
    ),
    cv.Optional(CONF_QUERY_PARAMS): button.button_schema(
        QueryButton,
        entity_category=ENTITY_CATEGORY_DIAGNOSTIC,
        icon=ICON_DATABASE,
    ),
}


async def to_code(config):
    ld2410_component = await cg.get_variable(config[CONF_LD2410_ID])
    if factory_reset_config := config.get(CONF_FACTORY_RESET):
        b = await button.new_button(factory_reset_config)
        await cg.register_parented(b, config[CONF_LD2410_ID])
        cg.add(ld2410_component.set_reset_button(b))
    if restart_config := config.get(CONF_RESTART):
        b = await button.new_button(restart_config)
        await cg.register_parented(b, config[CONF_LD2410_ID])
        cg.add(ld2410_component.set_restart_button(b))
    if query_params_config := config.get(CONF_QUERY_PARAMS):
        b = await button.new_button(query_params_config)
        await cg.register_parented(b, config[CONF_LD2410_ID])
        cg.add(ld2410_component.set_query_button(b))
