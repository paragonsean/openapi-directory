# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.comptage_reponse_etat_etat import ComptageReponseEtatEtat
from openapi_server import util


class ComptageReponseEtat(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, etat: List[ComptageReponseEtatEtat]=None):
        """ComptageReponseEtat - a model defined in OpenAPI

        :param etat: The etat of this ComptageReponseEtat.
        """
        self.openapi_types = {
            'etat': List[ComptageReponseEtatEtat]
        }

        self.attribute_map = {
            'etat': 'etat'
        }

        self._etat = etat

    @classmethod
    def from_dict(cls, dikt: dict) -> 'ComptageReponseEtat':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The ComptageReponse_etat of this ComptageReponseEtat.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def etat(self):
        """Gets the etat of this ComptageReponseEtat.


        :return: The etat of this ComptageReponseEtat.
        :rtype: List[ComptageReponseEtatEtat]
        """
        return self._etat

    @etat.setter
    def etat(self, etat):
        """Sets the etat of this ComptageReponseEtat.


        :param etat: The etat of this ComptageReponseEtat.
        :type etat: List[ComptageReponseEtatEtat]
        """

        self._etat = etat
