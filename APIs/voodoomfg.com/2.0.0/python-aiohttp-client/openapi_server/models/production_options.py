# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class ProductionOptions(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, orientation: bool=None):
        """ProductionOptions - a model defined in OpenAPI

        :param orientation: The orientation of this ProductionOptions.
        """
        self.openapi_types = {
            'orientation': bool
        }

        self.attribute_map = {
            'orientation': 'orientation'
        }

        self._orientation = orientation

    @classmethod
    def from_dict(cls, dikt: dict) -> 'ProductionOptions':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The ProductionOptions of this ProductionOptions.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def orientation(self):
        """Gets the orientation of this ProductionOptions.

        Indicates whether or not this model needs to be oriented prior to printing. If your model is already oriented for 3D printing, you can omit this flag (or set it to false) and it will not be re-oriented prior to printing. If true, it will be re-oriented prior to printing. If you're not sure if your model is oriented, you should set this flag to true. There is an additional charge for orientation.

        :return: The orientation of this ProductionOptions.
        :rtype: bool
        """
        return self._orientation

    @orientation.setter
    def orientation(self, orientation):
        """Sets the orientation of this ProductionOptions.

        Indicates whether or not this model needs to be oriented prior to printing. If your model is already oriented for 3D printing, you can omit this flag (or set it to false) and it will not be re-oriented prior to printing. If true, it will be re-oriented prior to printing. If you're not sure if your model is oriented, you should set this flag to true. There is an additional charge for orientation.

        :param orientation: The orientation of this ProductionOptions.
        :type orientation: bool
        """

        self._orientation = orientation
