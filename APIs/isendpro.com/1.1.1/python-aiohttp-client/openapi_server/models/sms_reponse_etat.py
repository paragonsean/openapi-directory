# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.sms_reponse_etat_etat import SMSReponseEtatEtat
from openapi_server import util


class SMSReponseEtat(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, etat: List[SMSReponseEtatEtat]=None):
        """SMSReponseEtat - a model defined in OpenAPI

        :param etat: The etat of this SMSReponseEtat.
        """
        self.openapi_types = {
            'etat': List[SMSReponseEtatEtat]
        }

        self.attribute_map = {
            'etat': 'etat'
        }

        self._etat = etat

    @classmethod
    def from_dict(cls, dikt: dict) -> 'SMSReponseEtat':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The SMSReponse_etat of this SMSReponseEtat.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def etat(self):
        """Gets the etat of this SMSReponseEtat.


        :return: The etat of this SMSReponseEtat.
        :rtype: List[SMSReponseEtatEtat]
        """
        return self._etat

    @etat.setter
    def etat(self, etat):
        """Sets the etat of this SMSReponseEtat.


        :param etat: The etat of this SMSReponseEtat.
        :type etat: List[SMSReponseEtatEtat]
        """

        self._etat = etat
