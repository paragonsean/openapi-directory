# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.branded_food_object_items_inner_diet_labels_gluten_free import BrandedFoodObjectItemsInnerDietLabelsGlutenFree
from openapi_server.models.branded_food_object_items_inner_diet_labels_vegan import BrandedFoodObjectItemsInnerDietLabelsVegan
from openapi_server.models.branded_food_object_items_inner_diet_labels_vegetarian import BrandedFoodObjectItemsInnerDietLabelsVegetarian
from openapi_server import util


class BrandedFoodObjectItemsInnerDietLabels(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, gluten_free: BrandedFoodObjectItemsInnerDietLabelsGlutenFree=None, vegan: BrandedFoodObjectItemsInnerDietLabelsVegan=None, vegetarian: BrandedFoodObjectItemsInnerDietLabelsVegetarian=None):
        """BrandedFoodObjectItemsInnerDietLabels - a model defined in OpenAPI

        :param gluten_free: The gluten_free of this BrandedFoodObjectItemsInnerDietLabels.
        :param vegan: The vegan of this BrandedFoodObjectItemsInnerDietLabels.
        :param vegetarian: The vegetarian of this BrandedFoodObjectItemsInnerDietLabels.
        """
        self.openapi_types = {
            'gluten_free': BrandedFoodObjectItemsInnerDietLabelsGlutenFree,
            'vegan': BrandedFoodObjectItemsInnerDietLabelsVegan,
            'vegetarian': BrandedFoodObjectItemsInnerDietLabelsVegetarian
        }

        self.attribute_map = {
            'gluten_free': 'gluten_free',
            'vegan': 'vegan',
            'vegetarian': 'vegetarian'
        }

        self._gluten_free = gluten_free
        self._vegan = vegan
        self._vegetarian = vegetarian

    @classmethod
    def from_dict(cls, dikt: dict) -> 'BrandedFoodObjectItemsInnerDietLabels':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The BrandedFoodObject_items_inner_diet_labels of this BrandedFoodObjectItemsInnerDietLabels.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def gluten_free(self):
        """Gets the gluten_free of this BrandedFoodObjectItemsInnerDietLabels.


        :return: The gluten_free of this BrandedFoodObjectItemsInnerDietLabels.
        :rtype: BrandedFoodObjectItemsInnerDietLabelsGlutenFree
        """
        return self._gluten_free

    @gluten_free.setter
    def gluten_free(self, gluten_free):
        """Sets the gluten_free of this BrandedFoodObjectItemsInnerDietLabels.


        :param gluten_free: The gluten_free of this BrandedFoodObjectItemsInnerDietLabels.
        :type gluten_free: BrandedFoodObjectItemsInnerDietLabelsGlutenFree
        """

        self._gluten_free = gluten_free

    @property
    def vegan(self):
        """Gets the vegan of this BrandedFoodObjectItemsInnerDietLabels.


        :return: The vegan of this BrandedFoodObjectItemsInnerDietLabels.
        :rtype: BrandedFoodObjectItemsInnerDietLabelsVegan
        """
        return self._vegan

    @vegan.setter
    def vegan(self, vegan):
        """Sets the vegan of this BrandedFoodObjectItemsInnerDietLabels.


        :param vegan: The vegan of this BrandedFoodObjectItemsInnerDietLabels.
        :type vegan: BrandedFoodObjectItemsInnerDietLabelsVegan
        """

        self._vegan = vegan

    @property
    def vegetarian(self):
        """Gets the vegetarian of this BrandedFoodObjectItemsInnerDietLabels.


        :return: The vegetarian of this BrandedFoodObjectItemsInnerDietLabels.
        :rtype: BrandedFoodObjectItemsInnerDietLabelsVegetarian
        """
        return self._vegetarian

    @vegetarian.setter
    def vegetarian(self, vegetarian):
        """Sets the vegetarian of this BrandedFoodObjectItemsInnerDietLabels.


        :param vegetarian: The vegetarian of this BrandedFoodObjectItemsInnerDietLabels.
        :type vegetarian: BrandedFoodObjectItemsInnerDietLabelsVegetarian
        """

        self._vegetarian = vegetarian
