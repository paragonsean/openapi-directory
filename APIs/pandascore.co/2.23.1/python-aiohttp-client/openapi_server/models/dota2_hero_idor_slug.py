# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class Dota2HeroIDOrSlug(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self):
        """Dota2HeroIDOrSlug - a model defined in OpenAPI

        """
        self.openapi_types = {
        }

        self.attribute_map = {
        }

    @classmethod
    def from_dict(cls, dikt: dict) -> 'Dota2HeroIDOrSlug':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The Dota2HeroIDOrSlug of this Dota2HeroIDOrSlug.
        """
        return util.deserialize_model(dikt, cls)
