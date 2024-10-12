# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class IngredientObjectItemsInnerCalorieConversionFactor(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, carbohydrate_value: float=None, fat_value: float=None, protein_value: float=None):
        """IngredientObjectItemsInnerCalorieConversionFactor - a model defined in OpenAPI

        :param carbohydrate_value: The carbohydrate_value of this IngredientObjectItemsInnerCalorieConversionFactor.
        :param fat_value: The fat_value of this IngredientObjectItemsInnerCalorieConversionFactor.
        :param protein_value: The protein_value of this IngredientObjectItemsInnerCalorieConversionFactor.
        """
        self.openapi_types = {
            'carbohydrate_value': float,
            'fat_value': float,
            'protein_value': float
        }

        self.attribute_map = {
            'carbohydrate_value': 'carbohydrate_value',
            'fat_value': 'fat_value',
            'protein_value': 'protein_value'
        }

        self._carbohydrate_value = carbohydrate_value
        self._fat_value = fat_value
        self._protein_value = protein_value

    @classmethod
    def from_dict(cls, dikt: dict) -> 'IngredientObjectItemsInnerCalorieConversionFactor':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The IngredientObject_items_inner_calorie_conversion_factor of this IngredientObjectItemsInnerCalorieConversionFactor.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def carbohydrate_value(self):
        """Gets the carbohydrate_value of this IngredientObjectItemsInnerCalorieConversionFactor.

        The multiplication factor for carbohydrates

        :return: The carbohydrate_value of this IngredientObjectItemsInnerCalorieConversionFactor.
        :rtype: float
        """
        return self._carbohydrate_value

    @carbohydrate_value.setter
    def carbohydrate_value(self, carbohydrate_value):
        """Sets the carbohydrate_value of this IngredientObjectItemsInnerCalorieConversionFactor.

        The multiplication factor for carbohydrates

        :param carbohydrate_value: The carbohydrate_value of this IngredientObjectItemsInnerCalorieConversionFactor.
        :type carbohydrate_value: float
        """

        self._carbohydrate_value = carbohydrate_value

    @property
    def fat_value(self):
        """Gets the fat_value of this IngredientObjectItemsInnerCalorieConversionFactor.

        The multiplication factor for fat

        :return: The fat_value of this IngredientObjectItemsInnerCalorieConversionFactor.
        :rtype: float
        """
        return self._fat_value

    @fat_value.setter
    def fat_value(self, fat_value):
        """Sets the fat_value of this IngredientObjectItemsInnerCalorieConversionFactor.

        The multiplication factor for fat

        :param fat_value: The fat_value of this IngredientObjectItemsInnerCalorieConversionFactor.
        :type fat_value: float
        """

        self._fat_value = fat_value

    @property
    def protein_value(self):
        """Gets the protein_value of this IngredientObjectItemsInnerCalorieConversionFactor.

        The multiplication factor for protein

        :return: The protein_value of this IngredientObjectItemsInnerCalorieConversionFactor.
        :rtype: float
        """
        return self._protein_value

    @protein_value.setter
    def protein_value(self, protein_value):
        """Sets the protein_value of this IngredientObjectItemsInnerCalorieConversionFactor.

        The multiplication factor for protein

        :param protein_value: The protein_value of this IngredientObjectItemsInnerCalorieConversionFactor.
        :type protein_value: float
        """

        self._protein_value = protein_value
