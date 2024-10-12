# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.background_style import BackgroundStyle
from openapi_server.models.inner_eye_style import InnerEyeStyle
from openapi_server.models.module_style import ModuleStyle
from openapi_server.models.outer_eye_style import OuterEyeStyle
from openapi_server import util


class Style(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, background: BackgroundStyle=None, inner_eye: InnerEyeStyle=None, module: ModuleStyle=None, outer_eye: OuterEyeStyle=None):
        """Style - a model defined in OpenAPI

        :param background: The background of this Style.
        :param inner_eye: The inner_eye of this Style.
        :param module: The module of this Style.
        :param outer_eye: The outer_eye of this Style.
        """
        self.openapi_types = {
            'background': BackgroundStyle,
            'inner_eye': InnerEyeStyle,
            'module': ModuleStyle,
            'outer_eye': OuterEyeStyle
        }

        self.attribute_map = {
            'background': 'background',
            'inner_eye': 'inner_eye',
            'module': 'module',
            'outer_eye': 'outer_eye'
        }

        self._background = background
        self._inner_eye = inner_eye
        self._module = module
        self._outer_eye = outer_eye

    @classmethod
    def from_dict(cls, dikt: dict) -> 'Style':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The Style of this Style.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def background(self):
        """Gets the background of this Style.

        `background` property allows you to select color of the background of the generated QR Code.

        :return: The background of this Style.
        :rtype: BackgroundStyle
        """
        return self._background

    @background.setter
    def background(self, background):
        """Sets the background of this Style.

        `background` property allows you to select color of the background of the generated QR Code.

        :param background: The background of this Style.
        :type background: BackgroundStyle
        """

        self._background = background

    @property
    def inner_eye(self):
        """Gets the inner_eye of this Style.

        `inner_eye` property allows you to select shape and color of the inner eyes of the generated QR Code.

        :return: The inner_eye of this Style.
        :rtype: InnerEyeStyle
        """
        return self._inner_eye

    @inner_eye.setter
    def inner_eye(self, inner_eye):
        """Sets the inner_eye of this Style.

        `inner_eye` property allows you to select shape and color of the inner eyes of the generated QR Code.

        :param inner_eye: The inner_eye of this Style.
        :type inner_eye: InnerEyeStyle
        """

        self._inner_eye = inner_eye

    @property
    def module(self):
        """Gets the module of this Style.

        `module` property allows you to select shape and color of the modules of the generated QR Code.

        :return: The module of this Style.
        :rtype: ModuleStyle
        """
        return self._module

    @module.setter
    def module(self, module):
        """Sets the module of this Style.

        `module` property allows you to select shape and color of the modules of the generated QR Code.

        :param module: The module of this Style.
        :type module: ModuleStyle
        """

        self._module = module

    @property
    def outer_eye(self):
        """Gets the outer_eye of this Style.

        `outer_eye` property allows you to select shape and color of the outer eyes of the generated QR Code.

        :return: The outer_eye of this Style.
        :rtype: OuterEyeStyle
        """
        return self._outer_eye

    @outer_eye.setter
    def outer_eye(self, outer_eye):
        """Sets the outer_eye of this Style.

        `outer_eye` property allows you to select shape and color of the outer eyes of the generated QR Code.

        :param outer_eye: The outer_eye of this Style.
        :type outer_eye: OuterEyeStyle
        """

        self._outer_eye = outer_eye
