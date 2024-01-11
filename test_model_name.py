from deepeye.models.payload import Payload, ModelType
from deepeye.srgan_wrapper import BSRGan, RealESRGan


def test_payload_model_name():

    assert ModelType.BSRGan.name == 'BSRGan'

    assert ModelType.RealESRGan.name == 'RealESRGan'
