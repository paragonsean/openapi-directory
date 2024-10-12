# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.auto_data import AutoData
from openapi_server.models.embedded_image_multipart import EmbeddedImageMultipart
from openapi_server.models.output_file import OutputFile
from openapi_server.models.size_multipart import SizeMultipart
from openapi_server.models.style import Style
from openapi_server import util


class AutoQRCodeMetadata(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, data: AutoData=None, image: EmbeddedImageMultipart=None, output: OutputFile=None, size: SizeMultipart=None, style: Style=None):
        """AutoQRCodeMetadata - a model defined in OpenAPI

        :param data: The data of this AutoQRCodeMetadata.
        :param image: The image of this AutoQRCodeMetadata.
        :param output: The output of this AutoQRCodeMetadata.
        :param size: The size of this AutoQRCodeMetadata.
        :param style: The style of this AutoQRCodeMetadata.
        """
        self.openapi_types = {
            'data': AutoData,
            'image': EmbeddedImageMultipart,
            'output': OutputFile,
            'size': SizeMultipart,
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
    def from_dict(cls, dikt: dict) -> 'AutoQRCodeMetadata':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The AutoQRCodeMetadata of this AutoQRCodeMetadata.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def data(self):
        """Gets the data of this AutoQRCodeMetadata.


        :return: The data of this AutoQRCodeMetadata.
        :rtype: AutoData
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this AutoQRCodeMetadata.


        :param data: The data of this AutoQRCodeMetadata.
        :type data: AutoData
        """
        if data is None:
            raise ValueError("Invalid value for `data`, must not be `None`")

        self._data = data

    @property
    def image(self):
        """Gets the image of this AutoQRCodeMetadata.

        `image` property allows you to set parameters of a custom image (e.g. your company logo, icon etc.) placed in the center of the generated QR Code.

        :return: The image of this AutoQRCodeMetadata.
        :rtype: EmbeddedImageMultipart
        """
        return self._image

    @image.setter
    def image(self, image):
        """Sets the image of this AutoQRCodeMetadata.

        `image` property allows you to set parameters of a custom image (e.g. your company logo, icon etc.) placed in the center of the generated QR Code.

        :param image: The image of this AutoQRCodeMetadata.
        :type image: EmbeddedImageMultipart
        """

        self._image = image

    @property
    def output(self):
        """Gets the output of this AutoQRCodeMetadata.

        `output` property allows you to specify the name and extension (type) of the file returned by the API

        :return: The output of this AutoQRCodeMetadata.
        :rtype: OutputFile
        """
        return self._output

    @output.setter
    def output(self, output):
        """Sets the output of this AutoQRCodeMetadata.

        `output` property allows you to specify the name and extension (type) of the file returned by the API

        :param output: The output of this AutoQRCodeMetadata.
        :type output: OutputFile
        """

        self._output = output

    @property
    def size(self):
        """Gets the size of this AutoQRCodeMetadata.

        `size` property allows you to set the values that define the sizes of the generated QR Code.

        :return: The size of this AutoQRCodeMetadata.
        :rtype: SizeMultipart
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this AutoQRCodeMetadata.

        `size` property allows you to set the values that define the sizes of the generated QR Code.

        :param size: The size of this AutoQRCodeMetadata.
        :type size: SizeMultipart
        """

        self._size = size

    @property
    def style(self):
        """Gets the style of this AutoQRCodeMetadata.

        `style` property allows you to select the appearance parameters of the modules and eyes of the generated QR Code.  All color specifications can be defined via: * CSS3 name: `Black`, `azure`, ... * hex value: `0x000`, `#FFFFFF`, `7fffd4`, ... * RGB/RGBA strings: `rgb(255, 255, 255)`, `rgba(255, 255, 255, 0.5)`, ... * HSL strings: `hsl(270, 60%, 70%)`, `hsl(270, 60%, 70%, .5)`, ...  Color values can be obtained from any online color picker like <a href=\"https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Colors/Color_picker_tool\" rel=\"noopener noreferrer\" target=\"_blank\" >developer.mozilla.org</a>.

        :return: The style of this AutoQRCodeMetadata.
        :rtype: Style
        """
        return self._style

    @style.setter
    def style(self, style):
        """Sets the style of this AutoQRCodeMetadata.

        `style` property allows you to select the appearance parameters of the modules and eyes of the generated QR Code.  All color specifications can be defined via: * CSS3 name: `Black`, `azure`, ... * hex value: `0x000`, `#FFFFFF`, `7fffd4`, ... * RGB/RGBA strings: `rgb(255, 255, 255)`, `rgba(255, 255, 255, 0.5)`, ... * HSL strings: `hsl(270, 60%, 70%)`, `hsl(270, 60%, 70%, .5)`, ...  Color values can be obtained from any online color picker like <a href=\"https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Colors/Color_picker_tool\" rel=\"noopener noreferrer\" target=\"_blank\" >developer.mozilla.org</a>.

        :param style: The style of this AutoQRCodeMetadata.
        :type style: Style
        """

        self._style = style
