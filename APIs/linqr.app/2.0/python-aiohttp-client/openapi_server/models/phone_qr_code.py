# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.embedded_image import EmbeddedImage
from openapi_server.models.output_file import OutputFile
from openapi_server.models.phone_data import PhoneData
from openapi_server.models.size import Size
from openapi_server.models.style import Style
from openapi_server import util


class PhoneQRCode(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, data: PhoneData=None, image: EmbeddedImage=None, output: OutputFile=None, size: Size=None, style: Style=None):
        """PhoneQRCode - a model defined in OpenAPI

        :param data: The data of this PhoneQRCode.
        :param image: The image of this PhoneQRCode.
        :param output: The output of this PhoneQRCode.
        :param size: The size of this PhoneQRCode.
        :param style: The style of this PhoneQRCode.
        """
        self.openapi_types = {
            'data': PhoneData,
            'image': EmbeddedImage,
            'output': OutputFile,
            'size': Size,
            'style': Style
        }

        self.attribute_map = {
            'data': 'data',
            'image': 'image',
            'output': 'output',
            'size': 'size',
            'style': 'style'
        }

        self._data = data
        self._image = image
        self._output = output
        self._size = size
        self._style = style

    @classmethod
    def from_dict(cls, dikt: dict) -> 'PhoneQRCode':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The PhoneQRCode of this PhoneQRCode.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def data(self):
        """Gets the data of this PhoneQRCode.

        `data` property allows you to specify telephone number called.

        :return: The data of this PhoneQRCode.
        :rtype: PhoneData
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this PhoneQRCode.

        `data` property allows you to specify telephone number called.

        :param data: The data of this PhoneQRCode.
        :type data: PhoneData
        """
        if data is None:
            raise ValueError("Invalid value for `data`, must not be `None`")

        self._data = data

    @property
    def image(self):
        """Gets the image of this PhoneQRCode.

        `image` property allows you to set parameters of a custom image (e.g. your company logo, icon etc.) placed in the center of the generated QR Code.

        :return: The image of this PhoneQRCode.
        :rtype: EmbeddedImage
        """
        return self._image

    @image.setter
    def image(self, image):
        """Sets the image of this PhoneQRCode.

        `image` property allows you to set parameters of a custom image (e.g. your company logo, icon etc.) placed in the center of the generated QR Code.

        :param image: The image of this PhoneQRCode.
        :type image: EmbeddedImage
        """

        self._image = image

    @property
    def output(self):
        """Gets the output of this PhoneQRCode.

        `output` property allows you to specify the name and extension (type) of the file returned by the API

        :return: The output of this PhoneQRCode.
        :rtype: OutputFile
        """
        return self._output

    @output.setter
    def output(self, output):
        """Sets the output of this PhoneQRCode.

        `output` property allows you to specify the name and extension (type) of the file returned by the API

        :param output: The output of this PhoneQRCode.
        :type output: OutputFile
        """

        self._output = output

    @property
    def size(self):
        """Gets the size of this PhoneQRCode.

        `size` property allows you to set the values that define the sizes of the generated QR Code.

        :return: The size of this PhoneQRCode.
        :rtype: Size
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this PhoneQRCode.

        `size` property allows you to set the values that define the sizes of the generated QR Code.

        :param size: The size of this PhoneQRCode.
        :type size: Size
        """

        self._size = size

    @property
    def style(self):
        """Gets the style of this PhoneQRCode.

        `style` property allows you to select the appearance parameters of the modules and eyes of the generated QR Code.  All color specifications can be defined via: * CSS3 name: `Black`, `azure`, ... * hex value: `0x000`, `#FFFFFF`, `7fffd4`, ... * RGB/RGBA strings: `rgb(255, 255, 255)`, `rgba(255, 255, 255, 0.5)`, ... * HSL strings: `hsl(270, 60%, 70%)`, `hsl(270, 60%, 70%, .5)`, ...  Color values can be obtained from any online color picker like <a href=\"https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Colors/Color_picker_tool\" rel=\"noopener noreferrer\" target=\"_blank\" >developer.mozilla.org</a>.

        :return: The style of this PhoneQRCode.
        :rtype: Style
        """
        return self._style

    @style.setter
    def style(self, style):
        """Sets the style of this PhoneQRCode.

        `style` property allows you to select the appearance parameters of the modules and eyes of the generated QR Code.  All color specifications can be defined via: * CSS3 name: `Black`, `azure`, ... * hex value: `0x000`, `#FFFFFF`, `7fffd4`, ... * RGB/RGBA strings: `rgb(255, 255, 255)`, `rgba(255, 255, 255, 0.5)`, ... * HSL strings: `hsl(270, 60%, 70%)`, `hsl(270, 60%, 70%, .5)`, ...  Color values can be obtained from any online color picker like <a href=\"https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Colors/Color_picker_tool\" rel=\"noopener noreferrer\" target=\"_blank\" >developer.mozilla.org</a>.

        :param style: The style of this PhoneQRCode.
        :type style: Style
        """

        self._style = style
