import esphome.codegen as cg
import esphome.config_validation as cv

from esphome.cpp_helpers import gpio_pin_expression

from esphome.const import CONF_ID, CONF_NAME, CONF_DATA_PIN, CONF_SPEED_COUNT, CONF_DISABLED_BY_DEFAULT, CONF_RESTORE_MODE, ENTITY_CATEGORY_CONFIG, ICON_CHIP, ICON_SCALE

MULTI_CONF = True
AUTO_LOAD = [ 'button', 'fan' ]
CONF_FAN = "fan"
CODEOWNERS = ["@compatech"]

cc1101itho_ns = cg.esphome_ns.namespace('cc1101itho')

CONF_CC1101ITHO_ID = "cc1101itho_id"

CC1101IthoComponent = cc1101itho_ns.class_('CC1101IthoComponent', cg.PollingComponent)

async def to_code(config):
    if CONF_FAN not in config:
        raise ValueError("Fan configuration is required.")

    data_pin = await gpio_pin_expression(config[CONF_FAN][CONF_DATA_PIN])
    cg.add(var.set_data_pin(data_pin))
