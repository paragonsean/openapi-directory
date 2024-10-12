# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.tax_data_tax_class_interface import TaxDataTaxClassInterface
from openapi_server import util


class TaxTaxClassRepositoryV1SavePostRequest(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, tax_class: TaxDataTaxClassInterface=None):
        """TaxTaxClassRepositoryV1SavePostRequest - a model defined in OpenAPI

        :param tax_class: The tax_class of this TaxTaxClassRepositoryV1SavePostRequest.
        """
        self.openapi_types = {
            'tax_class': TaxDataTaxClassInterface
        }

        self.attribute_map = {
            'tax_class': 'taxClass'
        }

        self._tax_class = tax_class

    @classmethod
    def from_dict(cls, dikt: dict) -> 'TaxTaxClassRepositoryV1SavePostRequest':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The taxTaxClassRepositoryV1SavePost_request of this TaxTaxClassRepositoryV1SavePostRequest.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def tax_class(self):
        """Gets the tax_class of this TaxTaxClassRepositoryV1SavePostRequest.


        :return: The tax_class of this TaxTaxClassRepositoryV1SavePostRequest.
        :rtype: TaxDataTaxClassInterface
        """
        return self._tax_class

    @tax_class.setter
    def tax_class(self, tax_class):
        """Sets the tax_class of this TaxTaxClassRepositoryV1SavePostRequest.


        :param tax_class: The tax_class of this TaxTaxClassRepositoryV1SavePostRequest.
        :type tax_class: TaxDataTaxClassInterface
        """
        if tax_class is None:
            raise ValueError("Invalid value for `tax_class`, must not be `None`")

        self._tax_class = tax_class
