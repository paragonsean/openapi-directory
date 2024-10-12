# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class Rabatt(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, betrag_brutto: int=None, betrag_netto: int=None, bezeichnung: str=None, satz: str=None):
        """Rabatt - a model defined in OpenAPI

        :param betrag_brutto: The betrag_brutto of this Rabatt.
        :param betrag_netto: The betrag_netto of this Rabatt.
        :param bezeichnung: The bezeichnung of this Rabatt.
        :param satz: The satz of this Rabatt.
        """
        self.openapi_types = {
            'betrag_brutto': int,
            'betrag_netto': int,
            'bezeichnung': str,
            'satz': str
        }

        self.attribute_map = {
            'betrag_brutto': 'Betrag-Brutto',
            'betrag_netto': 'Betrag-Netto',
            'bezeichnung': 'Bezeichnung',
            'satz': 'Satz'
        }

        self._betrag_brutto = betrag_brutto
        self._betrag_netto = betrag_netto
        self._bezeichnung = bezeichnung
        self._satz = satz

    @classmethod
    def from_dict(cls, dikt: dict) -> 'Rabatt':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The Rabatt of this Rabatt.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def betrag_brutto(self):
        """Gets the betrag_brutto of this Rabatt.

        The amount in cents

        :return: The betrag_brutto of this Rabatt.
        :rtype: int
        """
        return self._betrag_brutto

    @betrag_brutto.setter
    def betrag_brutto(self, betrag_brutto):
        """Sets the betrag_brutto of this Rabatt.

        The amount in cents

        :param betrag_brutto: The betrag_brutto of this Rabatt.
        :type betrag_brutto: int
        """
        if betrag_brutto is None:
            raise ValueError("Invalid value for `betrag_brutto`, must not be `None`")

        self._betrag_brutto = betrag_brutto

    @property
    def betrag_netto(self):
        """Gets the betrag_netto of this Rabatt.

        The amount in cents

        :return: The betrag_netto of this Rabatt.
        :rtype: int
        """
        return self._betrag_netto

    @betrag_netto.setter
    def betrag_netto(self, betrag_netto):
        """Sets the betrag_netto of this Rabatt.

        The amount in cents

        :param betrag_netto: The betrag_netto of this Rabatt.
        :type betrag_netto: int
        """
        if betrag_netto is None:
            raise ValueError("Invalid value for `betrag_netto`, must not be `None`")

        self._betrag_netto = betrag_netto

    @property
    def bezeichnung(self):
        """Gets the bezeichnung of this Rabatt.


        :return: The bezeichnung of this Rabatt.
        :rtype: str
        """
        return self._bezeichnung

    @bezeichnung.setter
    def bezeichnung(self, bezeichnung):
        """Sets the bezeichnung of this Rabatt.


        :param bezeichnung: The bezeichnung of this Rabatt.
        :type bezeichnung: str
        """
        if bezeichnung is None:
            raise ValueError("Invalid value for `bezeichnung`, must not be `None`")

        self._bezeichnung = bezeichnung

    @property
    def satz(self):
        """Gets the satz of this Rabatt.


        :return: The satz of this Rabatt.
        :rtype: str
        """
        return self._satz

    @satz.setter
    def satz(self, satz):
        """Sets the satz of this Rabatt.


        :param satz: The satz of this Rabatt.
        :type satz: str
        """
        allowed_values = ["NORMAL", "ERMAESSIGT1", "ERMAESSIGT2", "BESONDERS", "NULL"]  # noqa: E501
        if satz not in allowed_values:
            raise ValueError(
                "Invalid value for `satz` ({0}), must be one of {1}"
                .format(satz, allowed_values)
            )

        self._satz = satz
