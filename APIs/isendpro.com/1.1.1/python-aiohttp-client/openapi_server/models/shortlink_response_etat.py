# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.shortlink_response_etat_etat_inner import ShortlinkResponseEtatEtatInner
from openapi_server import util


class ShortlinkResponseEtat(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, etat: List[ShortlinkResponseEtatEtatInner]=None):
        """ShortlinkResponseEtat - a model defined in OpenAPI

        :param etat: The etat of this ShortlinkResponseEtat.
        """
        self.openapi_types = {
            'etat': List[ShortlinkResponseEtatEtatInner]
        }

        self.attribute_map = {
            'etat': 'etat'
        }

        self._etat = etat

    @classmethod
    def from_dict(cls, dikt: dict) -> 'ShortlinkResponseEtat':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The ShortlinkResponse_etat of this ShortlinkResponseEtat.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def etat(self):
        """Gets the etat of this ShortlinkResponseEtat.


        :return: The etat of this ShortlinkResponseEtat.
        :rtype: List[ShortlinkResponseEtatEtatInner]
        """
        return self._etat

    @etat.setter
    def etat(self, etat):
        """Sets the etat of this ShortlinkResponseEtat.


        :param etat: The etat of this ShortlinkResponseEtat.
        :type etat: List[ShortlinkResponseEtatEtatInner]
        """

        self._etat = etat
