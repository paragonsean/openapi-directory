# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class ArticleDOI(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, doi: str=None):
        """ArticleDOI - a model defined in OpenAPI

        :param doi: The doi of this ArticleDOI.
        """
        self.openapi_types = {
            'doi': str
        }

        self.attribute_map = {
            'doi': 'doi'
        }

        self._doi = doi

    @classmethod
    def from_dict(cls, dikt: dict) -> 'ArticleDOI':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The ArticleDOI of this ArticleDOI.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def doi(self):
        """Gets the doi of this ArticleDOI.

        Reserved DOI

        :return: The doi of this ArticleDOI.
        :rtype: str
        """
        return self._doi

    @doi.setter
    def doi(self, doi):
        """Sets the doi of this ArticleDOI.

        Reserved DOI

        :param doi: The doi of this ArticleDOI.
        :type doi: str
        """
        if doi is None:
            raise ValueError("Invalid value for `doi`, must not be `None`")

        self._doi = doi
