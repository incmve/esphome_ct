import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.const import CONF_ID

# This links the ithofan to the cc1101 radio component
DEPENDENCIES = ['cc1101']
ithofan_ns = cg.esphome_ns.namespace('ithofan')

CONFIG_SCHEMA = cv.Schema({
    cv.GenerateID(): cv.declare_id(ithofan_ns.IthoFan),
}).extend(cv.COMPONENT_SCHEMA)

def to_code(config):
    var = cg.new_Pvariable(config[CONF_ID])
    yield cg.register_component(var, config)
