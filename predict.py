from cog import BasePredictor, Input, Path
from PIL import Image

import moondream as md

class Predictor(BasePredictor):
    def setup(self):
        """Load the model into memory to make running multiple predictions efficient"""
        # Initialize with local model path. Can also read .mf.gz files, but we recommend decompressing
        # up-front to avoid decompression overhead every time the model is initialized.
        self.model = md.vl(model="./model/moondream-0_5b-int8.mf")

    # The arguments and types the model takes as input
    def predict(self,
          image: Path = Input(description="An input image (URL or base64 encoded data string)"),
        #   length: str = Input(description="Caption length either 'short' or 'long'. default is 'long'")
    ) -> str:
        """Run a single prediction on the model"""
        # Load and process image
        image = Image.open(image)
        encoded_image = self.model.encode_image(image)

        return self.model.caption(encoded_image)["caption"]

# # Initialize with local model path. Can also read .mf.gz files, but we recommend decompressing
# # up-front to avoid decompression overhead every time the model is initialized.
# model = md.vl(model="path/to/moondream-2b-int8.mf")

# # Load and process image
# image = Image.open("path/to/image.jpg")
# encoded_image = model.encode_image(image)

# # Generate caption
# caption = model.caption(encoded_image)["caption"]
# print("Caption:", caption)

# # Ask questions
# answer = model.query(encoded_image, "What's in this image?")["answer"]
# print("Answer:", answer)