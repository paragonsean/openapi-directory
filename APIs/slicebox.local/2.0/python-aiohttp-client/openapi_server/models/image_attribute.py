# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class ImageAttribute(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, depth: int=None, element: str=None, group: str=None, length: int=None, multiplicity: int=None, name: str=None, path: str=None, value: str=None, vr: str=None):
        """ImageAttribute - a model defined in OpenAPI

        :param depth: The depth of this ImageAttribute.
        :param element: The element of this ImageAttribute.
        :param group: The group of this ImageAttribute.
        :param length: The length of this ImageAttribute.
        :param multiplicity: The multiplicity of this ImageAttribute.
        :param name: The name of this ImageAttribute.
        :param path: The path of this ImageAttribute.
        :param value: The value of this ImageAttribute.
        :param vr: The vr of this ImageAttribute.
        """
        self.openapi_types = {
            'depth': int,
            'element': str,
            'group': str,
            'length': int,
            'multiplicity': int,
            'name': str,
            'path': str,
            'value': str,
            'vr': str
        }

        self.attribute_map = {
            'depth': 'depth',
            'element': 'element',
            'group': 'group',
            'length': 'length',
            'multiplicity': 'multiplicity',
            'name': 'name',
            'path': 'path',
            'value': 'value',
            'vr': 'vr'
        }

        self._depth = depth
        self._element = element
        self._group = group
        self._length = length
        self._multiplicity = multiplicity
        self._name = name
        self._path = path
        self._value = value
        self._vr = vr

    @classmethod
    def from_dict(cls, dikt: dict) -> 'ImageAttribute':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The imageAttribute of this ImageAttribute.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def depth(self):
        """Gets the depth of this ImageAttribute.


        :return: The depth of this ImageAttribute.
        :rtype: int
        """
        return self._depth

    @depth.setter
    def depth(self, depth):
        """Sets the depth of this ImageAttribute.


        :param depth: The depth of this ImageAttribute.
        :type depth: int
        """

        self._depth = depth

    @property
    def element(self):
        """Gets the element of this ImageAttribute.


        :return: The element of this ImageAttribute.
        :rtype: str
        """
        return self._element

    @element.setter
    def element(self, element):
        """Sets the element of this ImageAttribute.


        :param element: The element of this ImageAttribute.
        :type element: str
        """

        self._element = element

    @property
    def group(self):
        """Gets the group of this ImageAttribute.


        :return: The group of this ImageAttribute.
        :rtype: str
        """
        return self._group

    @group.setter
    def group(self, group):
        """Sets the group of this ImageAttribute.


        :param group: The group of this ImageAttribute.
        :type group: str
        """

        self._group = group

    @property
    def length(self):
        """Gets the length of this ImageAttribute.


        :return: The length of this ImageAttribute.
        :rtype: int
        """
        return self._length

    @length.setter
    def length(self, length):
        """Sets the length of this ImageAttribute.


        :param length: The length of this ImageAttribute.
        :type length: int
        """

        self._length = length

    @property
    def multiplicity(self):
        """Gets the multiplicity of this ImageAttribute.


        :return: The multiplicity of this ImageAttribute.
        :rtype: int
        """
        return self._multiplicity

    @multiplicity.setter
    def multiplicity(self, multiplicity):
        """Sets the multiplicity of this ImageAttribute.


        :param multiplicity: The multiplicity of this ImageAttribute.
        :type multiplicity: int
        """

        self._multiplicity = multiplicity

    @property
    def name(self):
        """Gets the name of this ImageAttribute.


        :return: The name of this ImageAttribute.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ImageAttribute.


        :param name: The name of this ImageAttribute.
        :type name: str
        """

        self._name = name

    @property
    def path(self):
        """Gets the path of this ImageAttribute.


        :return: The path of this ImageAttribute.
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """Sets the path of this ImageAttribute.


        :param path: The path of this ImageAttribute.
        :type path: str
        """

        self._path = path

    @property
    def value(self):
        """Gets the value of this ImageAttribute.


        :return: The value of this ImageAttribute.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this ImageAttribute.


        :param value: The value of this ImageAttribute.
        :type value: str
        """

        self._value = value

    @property
    def vr(self):
        """Gets the vr of this ImageAttribute.


        :return: The vr of this ImageAttribute.
        :rtype: str
        """
        return self._vr

    @vr.setter
    def vr(self, vr):
        """Sets the vr of this ImageAttribute.


        :param vr: The vr of this ImageAttribute.
        :type vr: str
        """

        self._vr = vr
