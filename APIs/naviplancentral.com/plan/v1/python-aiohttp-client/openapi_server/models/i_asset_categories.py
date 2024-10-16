# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.i_net_worth_category import INetWorthCategory
from openapi_server.models.i_value_description_pair_currency import IValueDescriptionPairCurrency
from openapi_server import util


class IAssetCategories(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, all_assets: List[IValueDescriptionPairCurrency]=None, business_assets: INetWorthCategory=None, lifestyle_assets: INetWorthCategory=None, non_qualified_annuities: INetWorthCategory=None, non_qualified_assets: INetWorthCategory=None, private_corporations: INetWorthCategory=None, qualified_annuities: INetWorthCategory=None, qualified_assets: INetWorthCategory=None, real_estate: INetWorthCategory=None, total_assets: INetWorthCategory=None):
        """IAssetCategories - a model defined in OpenAPI

        :param all_assets: The all_assets of this IAssetCategories.
        :param business_assets: The business_assets of this IAssetCategories.
        :param lifestyle_assets: The lifestyle_assets of this IAssetCategories.
        :param non_qualified_annuities: The non_qualified_annuities of this IAssetCategories.
        :param non_qualified_assets: The non_qualified_assets of this IAssetCategories.
        :param private_corporations: The private_corporations of this IAssetCategories.
        :param qualified_annuities: The qualified_annuities of this IAssetCategories.
        :param qualified_assets: The qualified_assets of this IAssetCategories.
        :param real_estate: The real_estate of this IAssetCategories.
        :param total_assets: The total_assets of this IAssetCategories.
        """
        self.openapi_types = {
            'all_assets': List[IValueDescriptionPairCurrency],
            'business_assets': INetWorthCategory,
            'lifestyle_assets': INetWorthCategory,
            'non_qualified_annuities': INetWorthCategory,
            'non_qualified_assets': INetWorthCategory,
            'private_corporations': INetWorthCategory,
            'qualified_annuities': INetWorthCategory,
            'qualified_assets': INetWorthCategory,
            'real_estate': INetWorthCategory,
            'total_assets': INetWorthCategory
        }

        self.attribute_map = {
            'all_assets': 'allAssets',
            'business_assets': 'businessAssets',
            'lifestyle_assets': 'lifestyleAssets',
            'non_qualified_annuities': 'nonQualifiedAnnuities',
            'non_qualified_assets': 'nonQualifiedAssets',
            'private_corporations': 'privateCorporations',
            'qualified_annuities': 'qualifiedAnnuities',
            'qualified_assets': 'qualifiedAssets',
            'real_estate': 'realEstate',
            'total_assets': 'totalAssets'
        }

        self._all_assets = all_assets
        self._business_assets = business_assets
        self._lifestyle_assets = lifestyle_assets
        self._non_qualified_annuities = non_qualified_annuities
        self._non_qualified_assets = non_qualified_assets
        self._private_corporations = private_corporations
        self._qualified_annuities = qualified_annuities
        self._qualified_assets = qualified_assets
        self._real_estate = real_estate
        self._total_assets = total_assets

    @classmethod
    def from_dict(cls, dikt: dict) -> 'IAssetCategories':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The IAssetCategories of this IAssetCategories.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def all_assets(self):
        """Gets the all_assets of this IAssetCategories.


        :return: The all_assets of this IAssetCategories.
        :rtype: List[IValueDescriptionPairCurrency]
        """
        return self._all_assets

    @all_assets.setter
    def all_assets(self, all_assets):
        """Sets the all_assets of this IAssetCategories.


        :param all_assets: The all_assets of this IAssetCategories.
        :type all_assets: List[IValueDescriptionPairCurrency]
        """

        self._all_assets = all_assets

    @property
    def business_assets(self):
        """Gets the business_assets of this IAssetCategories.


        :return: The business_assets of this IAssetCategories.
        :rtype: INetWorthCategory
        """
        return self._business_assets

    @business_assets.setter
    def business_assets(self, business_assets):
        """Sets the business_assets of this IAssetCategories.


        :param business_assets: The business_assets of this IAssetCategories.
        :type business_assets: INetWorthCategory
        """

        self._business_assets = business_assets

    @property
    def lifestyle_assets(self):
        """Gets the lifestyle_assets of this IAssetCategories.


        :return: The lifestyle_assets of this IAssetCategories.
        :rtype: INetWorthCategory
        """
        return self._lifestyle_assets

    @lifestyle_assets.setter
    def lifestyle_assets(self, lifestyle_assets):
        """Sets the lifestyle_assets of this IAssetCategories.


        :param lifestyle_assets: The lifestyle_assets of this IAssetCategories.
        :type lifestyle_assets: INetWorthCategory
        """

        self._lifestyle_assets = lifestyle_assets

    @property
    def non_qualified_annuities(self):
        """Gets the non_qualified_annuities of this IAssetCategories.


        :return: The non_qualified_annuities of this IAssetCategories.
        :rtype: INetWorthCategory
        """
        return self._non_qualified_annuities

    @non_qualified_annuities.setter
    def non_qualified_annuities(self, non_qualified_annuities):
        """Sets the non_qualified_annuities of this IAssetCategories.


        :param non_qualified_annuities: The non_qualified_annuities of this IAssetCategories.
        :type non_qualified_annuities: INetWorthCategory
        """

        self._non_qualified_annuities = non_qualified_annuities

    @property
    def non_qualified_assets(self):
        """Gets the non_qualified_assets of this IAssetCategories.


        :return: The non_qualified_assets of this IAssetCategories.
        :rtype: INetWorthCategory
        """
        return self._non_qualified_assets

    @non_qualified_assets.setter
    def non_qualified_assets(self, non_qualified_assets):
        """Sets the non_qualified_assets of this IAssetCategories.


        :param non_qualified_assets: The non_qualified_assets of this IAssetCategories.
        :type non_qualified_assets: INetWorthCategory
        """

        self._non_qualified_assets = non_qualified_assets

    @property
    def private_corporations(self):
        """Gets the private_corporations of this IAssetCategories.


        :return: The private_corporations of this IAssetCategories.
        :rtype: INetWorthCategory
        """
        return self._private_corporations

    @private_corporations.setter
    def private_corporations(self, private_corporations):
        """Sets the private_corporations of this IAssetCategories.


        :param private_corporations: The private_corporations of this IAssetCategories.
        :type private_corporations: INetWorthCategory
        """

        self._private_corporations = private_corporations

    @property
    def qualified_annuities(self):
        """Gets the qualified_annuities of this IAssetCategories.


        :return: The qualified_annuities of this IAssetCategories.
        :rtype: INetWorthCategory
        """
        return self._qualified_annuities

    @qualified_annuities.setter
    def qualified_annuities(self, qualified_annuities):
        """Sets the qualified_annuities of this IAssetCategories.


        :param qualified_annuities: The qualified_annuities of this IAssetCategories.
        :type qualified_annuities: INetWorthCategory
        """

        self._qualified_annuities = qualified_annuities

    @property
    def qualified_assets(self):
        """Gets the qualified_assets of this IAssetCategories.


        :return: The qualified_assets of this IAssetCategories.
        :rtype: INetWorthCategory
        """
        return self._qualified_assets

    @qualified_assets.setter
    def qualified_assets(self, qualified_assets):
        """Sets the qualified_assets of this IAssetCategories.


        :param qualified_assets: The qualified_assets of this IAssetCategories.
        :type qualified_assets: INetWorthCategory
        """

        self._qualified_assets = qualified_assets

    @property
    def real_estate(self):
        """Gets the real_estate of this IAssetCategories.


        :return: The real_estate of this IAssetCategories.
        :rtype: INetWorthCategory
        """
        return self._real_estate

    @real_estate.setter
    def real_estate(self, real_estate):
        """Sets the real_estate of this IAssetCategories.


        :param real_estate: The real_estate of this IAssetCategories.
        :type real_estate: INetWorthCategory
        """

        self._real_estate = real_estate

    @property
    def total_assets(self):
        """Gets the total_assets of this IAssetCategories.


        :return: The total_assets of this IAssetCategories.
        :rtype: INetWorthCategory
        """
        return self._total_assets

    @total_assets.setter
    def total_assets(self, total_assets):
        """Sets the total_assets of this IAssetCategories.


        :param total_assets: The total_assets of this IAssetCategories.
        :type total_assets: INetWorthCategory
        """

        self._total_assets = total_assets
