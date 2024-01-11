from deepeye.srgan_wrapper import BSRGan, RealESRGan

from deepeye.models.payload import Payload, ModelType

import numpy as np

data = np.random.rand(3, 256, 256)

payload = Payload(
    data=data.tolist(),
    type=ModelType.BSRGan,
    model='bsrgan.pth',
    max_value=255,
    up_scale=4
)
