# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class PVService(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    """
    allowed enum values
    """
    NICONICODOUGA = 'NicoNicoDouga'
    YOUTUBE = 'Youtube'
    SOUNDCLOUD = 'SoundCloud'
    VIMEO = 'Vimeo'
    PIAPRO = 'Piapro'
    BILIBILI = 'Bilibili'
    FILE = 'File'
    LOCALFILE = 'LocalFile'
    CREOFUGA = 'Creofuga'
    BANDCAMP = 'Bandcamp'

    def __init__(self):
        """PVService - a model defined in OpenAPI

        """
        self.openapi_types = {
        }

        self.attribute_map = {
        }

    @classmethod
    def from_dict(cls, dikt: dict) -> 'PVService':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The PVService of this PVService.
        """
        return util.deserialize_model(dikt, cls)
