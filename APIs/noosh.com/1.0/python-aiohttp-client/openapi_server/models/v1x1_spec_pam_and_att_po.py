# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class V1x1SpecPamAndAttPO(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, attribute_id: int=None, attribute_value: object=None, label: str=None, param_id: int=None, param_name: str=None):
        """V1x1SpecPamAndAttPO - a model defined in OpenAPI

        :param attribute_id: The attribute_id of this V1x1SpecPamAndAttPO.
        :param attribute_value: The attribute_value of this V1x1SpecPamAndAttPO.
        :param label: The label of this V1x1SpecPamAndAttPO.
        :param param_id: The param_id of this V1x1SpecPamAndAttPO.
        :param param_name: The param_name of this V1x1SpecPamAndAttPO.
        """
        self.openapi_types = {
            'attribute_id': int,
            'attribute_value': object,
            'label': str,
            'param_id': int,
            'param_name': str
        }

        self.attribute_map = {
            'attribute_id': 'attribute_id',
            'attribute_value': 'attribute_value',
            'label': 'label',
            'param_id': 'param_id',
            'param_name': 'param_name'
        }

        self._attribute_id = attribute_id
        self._attribute_value = attribute_value
        self._label = label
        self._param_id = param_id
        self._param_name = param_name

    @classmethod
    def from_dict(cls, dikt: dict) -> 'V1x1SpecPamAndAttPO':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The V1x1SpecPamAndAttPO of this V1x1SpecPamAndAttPO.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def attribute_id(self):
        """Gets the attribute_id of this V1x1SpecPamAndAttPO.

        

        :return: The attribute_id of this V1x1SpecPamAndAttPO.
        :rtype: int
        """
        return self._attribute_id

    @attribute_id.setter
    def attribute_id(self, attribute_id):
        """Sets the attribute_id of this V1x1SpecPamAndAttPO.

        

        :param attribute_id: The attribute_id of this V1x1SpecPamAndAttPO.
        :type attribute_id: int
        """

        self._attribute_id = attribute_id

    @property
    def attribute_value(self):
        """Gets the attribute_value of this V1x1SpecPamAndAttPO.

        Java type: java.lang.Object

        :return: The attribute_value of this V1x1SpecPamAndAttPO.
        :rtype: object
        """
        return self._attribute_value

    @attribute_value.setter
    def attribute_value(self, attribute_value):
        """Sets the attribute_value of this V1x1SpecPamAndAttPO.

        Java type: java.lang.Object

        :param attribute_value: The attribute_value of this V1x1SpecPamAndAttPO.
        :type attribute_value: object
        """

        self._attribute_value = attribute_value

    @property
    def label(self):
        """Gets the label of this V1x1SpecPamAndAttPO.

        

        :return: The label of this V1x1SpecPamAndAttPO.
        :rtype: str
        """
        return self._label

    @label.setter
    def label(self, label):
        """Sets the label of this V1x1SpecPamAndAttPO.

        

        :param label: The label of this V1x1SpecPamAndAttPO.
        :type label: str
        """

        self._label = label

    @property
    def param_id(self):
        """Gets the param_id of this V1x1SpecPamAndAttPO.

        

        :return: The param_id of this V1x1SpecPamAndAttPO.
        :rtype: int
        """
        return self._param_id

    @param_id.setter
    def param_id(self, param_id):
        """Sets the param_id of this V1x1SpecPamAndAttPO.

        

        :param param_id: The param_id of this V1x1SpecPamAndAttPO.
        :type param_id: int
        """

        self._param_id = param_id

    @property
    def param_name(self):
        """Gets the param_name of this V1x1SpecPamAndAttPO.

        

        :return: The param_name of this V1x1SpecPamAndAttPO.
        :rtype: str
        """
        return self._param_name

    @param_name.setter
    def param_name(self, param_name):
        """Sets the param_name of this V1x1SpecPamAndAttPO.

        

        :param param_name: The param_name of this V1x1SpecPamAndAttPO.
        :type param_name: str
        """

        self._param_name = param_name
