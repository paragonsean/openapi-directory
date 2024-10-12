# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.tax_data_tax_rate_interface import TaxDataTaxRateInterface
from openapi_server import util


class TaxTaxRateRepositoryV1SavePutRequest(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, tax_rate: TaxDataTaxRateInterface=None):
        """TaxTaxRateRepositoryV1SavePutRequest - a model defined in OpenAPI

        :param tax_rate: The tax_rate of this TaxTaxRateRepositoryV1SavePutRequest.
        """
        self.openapi_types = {
            'tax_rate': TaxDataTaxRateInterface
        }

        self.attribute_map = {
            'tax_rate': 'taxRate'
        }

        self._tax_rate = tax_rate

    @classmethod
    def from_dict(cls, dikt: dict) -> 'TaxTaxRateRepositoryV1SavePutRequest':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The taxTaxRateRepositoryV1SavePut_request of this TaxTaxRateRepositoryV1SavePutRequest.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def tax_rate(self):
        """Gets the tax_rate of this TaxTaxRateRepositoryV1SavePutRequest.


        :return: The tax_rate of this TaxTaxRateRepositoryV1SavePutRequest.
        :rtype: TaxDataTaxRateInterface
        """
        return self._tax_rate

    @tax_rate.setter
    def tax_rate(self, tax_rate):
        """Sets the tax_rate of this TaxTaxRateRepositoryV1SavePutRequest.


        :param tax_rate: The tax_rate of this TaxTaxRateRepositoryV1SavePutRequest.
        :type tax_rate: TaxDataTaxRateInterface
        """
        if tax_rate is None:
            raise ValueError("Invalid value for `tax_rate`, must not be `None`")

        self._tax_rate = tax_rate
