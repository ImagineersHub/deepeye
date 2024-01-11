from deepeye.models.payload import Payload, ModelType


def test_payload_model_name():

    assert ModelType.BSRGan.name == 'BSRGan'

    assert ModelType.RealESRGan.name == 'RealESRGan'
