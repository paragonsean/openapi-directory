# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.ingredient_object_items_inner_calorie_conversion_factor import IngredientObjectItemsInnerCalorieConversionFactor
from openapi_server.models.ingredient_object_items_inner_components_inner import IngredientObjectItemsInnerComponentsInner
from openapi_server.models.ingredient_object_items_inner_nutrients_inner import IngredientObjectItemsInnerNutrientsInner
from openapi_server.models.ingredient_object_items_inner_portions_inner import IngredientObjectItemsInnerPortionsInner
from openapi_server import util


class IngredientObjectItemsInner(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, calorie_conversion_factor: IngredientObjectItemsInnerCalorieConversionFactor=None, categories: List[str]=None, common_name: str=None, components: List[IngredientObjectItemsInnerComponentsInner]=None, footnote: str=None, name: str=None, nutrients: List[IngredientObjectItemsInnerNutrientsInner]=None, portions: List[IngredientObjectItemsInnerPortionsInner]=None, protein_conversion_factor: float=None, score: str=None, search_term: str=None):
        """IngredientObjectItemsInner - a model defined in OpenAPI

        :param calorie_conversion_factor: The calorie_conversion_factor of this IngredientObjectItemsInner.
        :param categories: The categories of this IngredientObjectItemsInner.
        :param common_name: The common_name of this IngredientObjectItemsInner.
        :param components: The components of this IngredientObjectItemsInner.
        :param footnote: The footnote of this IngredientObjectItemsInner.
        :param name: The name of this IngredientObjectItemsInner.
        :param nutrients: The nutrients of this IngredientObjectItemsInner.
        :param portions: The portions of this IngredientObjectItemsInner.
        :param protein_conversion_factor: The protein_conversion_factor of this IngredientObjectItemsInner.
        :param score: The score of this IngredientObjectItemsInner.
        :param search_term: The search_term of this IngredientObjectItemsInner.
        """
        self.openapi_types = {
            'calorie_conversion_factor': IngredientObjectItemsInnerCalorieConversionFactor,
            'categories': List[str],
            'common_name': str,
            'components': List[IngredientObjectItemsInnerComponentsInner],
            'footnote': str,
            'name': str,
            'nutrients': List[IngredientObjectItemsInnerNutrientsInner],
            'portions': List[IngredientObjectItemsInnerPortionsInner],
            'protein_conversion_factor': float,
            'score': str,
            'search_term': str
        }

        self.attribute_map = {
            'calorie_conversion_factor': 'calorie_conversion_factor',
            'categories': 'categories',
            'common_name': 'common_name',
            'components': 'components',
            'footnote': 'footnote',
            'name': 'name',
            'nutrients': 'nutrients',
            'portions': 'portions',
            'protein_conversion_factor': 'protein_conversion_factor',
            'score': 'score',
            'search_term': 'search_term'
        }

        self._calorie_conversion_factor = calorie_conversion_factor
        self._categories = categories
        self._common_name = common_name
        self._components = components
        self._footnote = footnote
        self._name = name
        self._nutrients = nutrients
        self._portions = portions
        self._protein_conversion_factor = protein_conversion_factor
        self._score = score
        self._search_term = search_term

    @classmethod
    def from_dict(cls, dikt: dict) -> 'IngredientObjectItemsInner':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The IngredientObject_items_inner of this IngredientObjectItemsInner.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def calorie_conversion_factor(self):
        """Gets the calorie_conversion_factor of this IngredientObjectItemsInner.


        :return: The calorie_conversion_factor of this IngredientObjectItemsInner.
        :rtype: IngredientObjectItemsInnerCalorieConversionFactor
        """
        return self._calorie_conversion_factor

    @calorie_conversion_factor.setter
    def calorie_conversion_factor(self, calorie_conversion_factor):
        """Sets the calorie_conversion_factor of this IngredientObjectItemsInner.


        :param calorie_conversion_factor: The calorie_conversion_factor of this IngredientObjectItemsInner.
        :type calorie_conversion_factor: IngredientObjectItemsInnerCalorieConversionFactor
        """

        self._calorie_conversion_factor = calorie_conversion_factor

    @property
    def categories(self):
        """Gets the categories of this IngredientObjectItemsInner.


        :return: The categories of this IngredientObjectItemsInner.
        :rtype: List[str]
        """
        return self._categories

    @categories.setter
    def categories(self, categories):
        """Sets the categories of this IngredientObjectItemsInner.


        :param categories: The categories of this IngredientObjectItemsInner.
        :type categories: List[str]
        """

        self._categories = categories

    @property
    def common_name(self):
        """Gets the common_name of this IngredientObjectItemsInner.

        Common name associated with this item. These generally clarify what the item is (e.g. when the brand name is \"BRAND's Spicy Enchilada\" the common name may be \"Chicken enchilada\")

        :return: The common_name of this IngredientObjectItemsInner.
        :rtype: str
        """
        return self._common_name

    @common_name.setter
    def common_name(self, common_name):
        """Sets the common_name of this IngredientObjectItemsInner.

        Common name associated with this item. These generally clarify what the item is (e.g. when the brand name is \"BRAND's Spicy Enchilada\" the common name may be \"Chicken enchilada\")

        :param common_name: The common_name of this IngredientObjectItemsInner.
        :type common_name: str
        """

        self._common_name = common_name

    @property
    def components(self):
        """Gets the components of this IngredientObjectItemsInner.

        An array of objects containing the constituent parts of a food (e.g. bone is a component of meat)

        :return: The components of this IngredientObjectItemsInner.
        :rtype: List[IngredientObjectItemsInnerComponentsInner]
        """
        return self._components

    @components.setter
    def components(self, components):
        """Sets the components of this IngredientObjectItemsInner.

        An array of objects containing the constituent parts of a food (e.g. bone is a component of meat)

        :param components: The components of this IngredientObjectItemsInner.
        :type components: List[IngredientObjectItemsInnerComponentsInner]
        """

        self._components = components

    @property
    def footnote(self):
        """Gets the footnote of this IngredientObjectItemsInner.

        Comments on any unusual aspects of this item. Examples might include unusual aspects of the food overall

        :return: The footnote of this IngredientObjectItemsInner.
        :rtype: str
        """
        return self._footnote

    @footnote.setter
    def footnote(self, footnote):
        """Sets the footnote of this IngredientObjectItemsInner.

        Comments on any unusual aspects of this item. Examples might include unusual aspects of the food overall

        :param footnote: The footnote of this IngredientObjectItemsInner.
        :type footnote: str
        """

        self._footnote = footnote

    @property
    def name(self):
        """Gets the name of this IngredientObjectItemsInner.

        Item name as provided by brand owner or as shown on packaging

        :return: The name of this IngredientObjectItemsInner.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this IngredientObjectItemsInner.

        Item name as provided by brand owner or as shown on packaging

        :param name: The name of this IngredientObjectItemsInner.
        :type name: str
        """

        self._name = name

    @property
    def nutrients(self):
        """Gets the nutrients of this IngredientObjectItemsInner.

        An array containing nutrient informatio objects for this food item

        :return: The nutrients of this IngredientObjectItemsInner.
        :rtype: List[IngredientObjectItemsInnerNutrientsInner]
        """
        return self._nutrients

    @nutrients.setter
    def nutrients(self, nutrients):
        """Sets the nutrients of this IngredientObjectItemsInner.

        An array containing nutrient informatio objects for this food item

        :param nutrients: The nutrients of this IngredientObjectItemsInner.
        :type nutrients: List[IngredientObjectItemsInnerNutrientsInner]
        """

        self._nutrients = nutrients

    @property
    def portions(self):
        """Gets the portions of this IngredientObjectItemsInner.

        An array of objects containing information on discrete amounts of a food found in this item

        :return: The portions of this IngredientObjectItemsInner.
        :rtype: List[IngredientObjectItemsInnerPortionsInner]
        """
        return self._portions

    @portions.setter
    def portions(self, portions):
        """Sets the portions of this IngredientObjectItemsInner.

        An array of objects containing information on discrete amounts of a food found in this item

        :param portions: The portions of this IngredientObjectItemsInner.
        :type portions: List[IngredientObjectItemsInnerPortionsInner]
        """

        self._portions = portions

    @property
    def protein_conversion_factor(self):
        """Gets the protein_conversion_factor of this IngredientObjectItemsInner.

        The multiplication factor used to calculate protein from nitrogen

        :return: The protein_conversion_factor of this IngredientObjectItemsInner.
        :rtype: float
        """
        return self._protein_conversion_factor

    @protein_conversion_factor.setter
    def protein_conversion_factor(self, protein_conversion_factor):
        """Sets the protein_conversion_factor of this IngredientObjectItemsInner.

        The multiplication factor used to calculate protein from nitrogen

        :param protein_conversion_factor: The protein_conversion_factor of this IngredientObjectItemsInner.
        :type protein_conversion_factor: float
        """

        self._protein_conversion_factor = protein_conversion_factor

    @property
    def score(self):
        """Gets the score of this IngredientObjectItemsInner.

        A value that represents how similar the name of this food item is to the original search term. The lower the value the closer this item's name is to the original search term.

        :return: The score of this IngredientObjectItemsInner.
        :rtype: str
        """
        return self._score

    @score.setter
    def score(self, score):
        """Sets the score of this IngredientObjectItemsInner.

        A value that represents how similar the name of this food item is to the original search term. The lower the value the closer this item's name is to the original search term.

        :param score: The score of this IngredientObjectItemsInner.
        :type score: str
        """

        self._score = score

    @property
    def search_term(self):
        """Gets the search_term of this IngredientObjectItemsInner.

        The original search term that found this food item

        :return: The search_term of this IngredientObjectItemsInner.
        :rtype: str
        """
        return self._search_term

    @search_term.setter
    def search_term(self, search_term):
        """Sets the search_term of this IngredientObjectItemsInner.

        The original search term that found this food item

        :param search_term: The search_term of this IngredientObjectItemsInner.
        :type search_term: str
        """

        self._search_term = search_term
