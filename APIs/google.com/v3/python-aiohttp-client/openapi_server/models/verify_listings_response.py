# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.parsed_listing import ParsedListing
from openapi_server import util


class VerifyListingsResponse(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, parsed_listing: ParsedListing=None):
        """VerifyListingsResponse - a model defined in OpenAPI

        :param parsed_listing: The parsed_listing of this VerifyListingsResponse.
        """
        self.openapi_types = {
            'parsed_listing': ParsedListing
        }

        self.attribute_map = {
            'parsed_listing': 'parsedListing'
        }

        self._parsed_listing = parsed_listing

    @classmethod
    def from_dict(cls, dikt: dict) -> 'VerifyListingsResponse':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The VerifyListingsResponse of this VerifyListingsResponse.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def parsed_listing(self):
        """Gets the parsed_listing of this VerifyListingsResponse.


        :return: The parsed_listing of this VerifyListingsResponse.
        :rtype: ParsedListing
        """
        return self._parsed_listing

    @parsed_listing.setter
    def parsed_listing(self, parsed_listing):
        """Sets the parsed_listing of this VerifyListingsResponse.


        :param parsed_listing: The parsed_listing of this VerifyListingsResponse.
        :type parsed_listing: ParsedListing
        """

        self._parsed_listing = parsed_listing
