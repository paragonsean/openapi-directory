# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
import re
from openapi_server import util


class GlobalResourcesSharedModelsTranslationSetAttribute(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, id: int=None, name: str=None, translation_set_id: int=None, value: str=None):
        """GlobalResourcesSharedModelsTranslationSetAttribute - a model defined in OpenAPI

        :param id: The id of this GlobalResourcesSharedModelsTranslationSetAttribute.
        :param name: The name of this GlobalResourcesSharedModelsTranslationSetAttribute.
        :param translation_set_id: The translation_set_id of this GlobalResourcesSharedModelsTranslationSetAttribute.
        :param value: The value of this GlobalResourcesSharedModelsTranslationSetAttribute.
        """
        self.openapi_types = {
            'id': int,
            'name': str,
            'translation_set_id': int,
            'value': str
        }

        self.attribute_map = {
            'id': 'ID',
            'name': 'Name',
            'translation_set_id': 'TranslationSetID',
            'value': 'Value'
        }

        self._id = id
        self._name = name
        self._translation_set_id = translation_set_id
        self._value = value

    @classmethod
    def from_dict(cls, dikt: dict) -> 'GlobalResourcesSharedModelsTranslationSetAttribute':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The GlobalResources.Shared.Models.TranslationSetAttribute of this GlobalResourcesSharedModelsTranslationSetAttribute.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self):
        """Gets the id of this GlobalResourcesSharedModelsTranslationSetAttribute.

        The ID of this attribute.

        :return: The id of this GlobalResourcesSharedModelsTranslationSetAttribute.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this GlobalResourcesSharedModelsTranslationSetAttribute.

        The ID of this attribute.

        :param id: The id of this GlobalResourcesSharedModelsTranslationSetAttribute.
        :type id: int
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this GlobalResourcesSharedModelsTranslationSetAttribute.

        The name of this Attribute.

        :return: The name of this GlobalResourcesSharedModelsTranslationSetAttribute.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this GlobalResourcesSharedModelsTranslationSetAttribute.

        The name of this Attribute.

        :param name: The name of this GlobalResourcesSharedModelsTranslationSetAttribute.
        :type name: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")
        if name is not None and not re.search(r'[a-zA-Z0-9]+', name):
            raise ValueError("Invalid value for `name`, must be a follow pattern or equal to `/[a-zA-Z0-9]+/`")

        self._name = name

    @property
    def translation_set_id(self):
        """Gets the translation_set_id of this GlobalResourcesSharedModelsTranslationSetAttribute.

        The ID of the translation set to which this attribute belongs.

        :return: The translation_set_id of this GlobalResourcesSharedModelsTranslationSetAttribute.
        :rtype: int
        """
        return self._translation_set_id

    @translation_set_id.setter
    def translation_set_id(self, translation_set_id):
        """Sets the translation_set_id of this GlobalResourcesSharedModelsTranslationSetAttribute.

        The ID of the translation set to which this attribute belongs.

        :param translation_set_id: The translation_set_id of this GlobalResourcesSharedModelsTranslationSetAttribute.
        :type translation_set_id: int
        """

        self._translation_set_id = translation_set_id

    @property
    def value(self):
        """Gets the value of this GlobalResourcesSharedModelsTranslationSetAttribute.

        The value of this Attribute

        :return: The value of this GlobalResourcesSharedModelsTranslationSetAttribute.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this GlobalResourcesSharedModelsTranslationSetAttribute.

        The value of this Attribute

        :param value: The value of this GlobalResourcesSharedModelsTranslationSetAttribute.
        :type value: str
        """

        self._value = value
