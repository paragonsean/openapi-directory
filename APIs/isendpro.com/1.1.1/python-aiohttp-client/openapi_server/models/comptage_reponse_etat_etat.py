# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class ComptageReponseEtatEtat(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, nb_caractere: str=None, nb_sms: str=None, tel: str=None):
        """ComptageReponseEtatEtat - a model defined in OpenAPI

        :param nb_caractere: The nb_caractere of this ComptageReponseEtatEtat.
        :param nb_sms: The nb_sms of this ComptageReponseEtatEtat.
        :param tel: The tel of this ComptageReponseEtatEtat.
        """
        self.openapi_types = {
            'nb_caractere': str,
            'nb_sms': str,
            'tel': str
        }

        self.attribute_map = {
            'nb_caractere': 'nb_caractere',
            'nb_sms': 'nb_sms',
            'tel': 'tel'
        }

        self._nb_caractere = nb_caractere
        self._nb_sms = nb_sms
        self._tel = tel

    @classmethod
    def from_dict(cls, dikt: dict) -> 'ComptageReponseEtatEtat':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The ComptageReponse_etat_etat of this ComptageReponseEtatEtat.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def nb_caractere(self):
        """Gets the nb_caractere of this ComptageReponseEtatEtat.

        nombre de caractères

        :return: The nb_caractere of this ComptageReponseEtatEtat.
        :rtype: str
        """
        return self._nb_caractere

    @nb_caractere.setter
    def nb_caractere(self, nb_caractere):
        """Sets the nb_caractere of this ComptageReponseEtatEtat.

        nombre de caractères

        :param nb_caractere: The nb_caractere of this ComptageReponseEtatEtat.
        :type nb_caractere: str
        """

        self._nb_caractere = nb_caractere

    @property
    def nb_sms(self):
        """Gets the nb_sms of this ComptageReponseEtatEtat.

        nombre de sms nécessaires

        :return: The nb_sms of this ComptageReponseEtatEtat.
        :rtype: str
        """
        return self._nb_sms

    @nb_sms.setter
    def nb_sms(self, nb_sms):
        """Sets the nb_sms of this ComptageReponseEtatEtat.

        nombre de sms nécessaires

        :param nb_sms: The nb_sms of this ComptageReponseEtatEtat.
        :type nb_sms: str
        """

        self._nb_sms = nb_sms

    @property
    def tel(self):
        """Gets the tel of this ComptageReponseEtatEtat.

        numéro de téléphone

        :return: The tel of this ComptageReponseEtatEtat.
        :rtype: str
        """
        return self._tel

    @tel.setter
    def tel(self, tel):
        """Sets the tel of this ComptageReponseEtatEtat.

        numéro de téléphone

        :param tel: The tel of this ComptageReponseEtatEtat.
        :type tel: str
        """

        self._tel = tel
