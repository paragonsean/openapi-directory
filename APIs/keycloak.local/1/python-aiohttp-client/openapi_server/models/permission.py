# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class Permission(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, claims: Dict[str, object]=None, rsid: str=None, rsname: str=None, scopes: List[str]=None):
        """Permission - a model defined in OpenAPI

        :param claims: The claims of this Permission.
        :param rsid: The rsid of this Permission.
        :param rsname: The rsname of this Permission.
        :param scopes: The scopes of this Permission.
        """
        self.openapi_types = {
            'claims': Dict[str, object],
            'rsid': str,
            'rsname': str,
            'scopes': List[str]
        }

        self.attribute_map = {
            'claims': 'claims',
            'rsid': 'rsid',
            'rsname': 'rsname',
            'scopes': 'scopes'
        }

        self._claims = claims
        self._rsid = rsid
        self._rsname = rsname
        self._scopes = scopes

    @classmethod
    def from_dict(cls, dikt: dict) -> 'Permission':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The Permission of this Permission.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def claims(self):
        """Gets the claims of this Permission.


        :return: The claims of this Permission.
        :rtype: Dict[str, object]
        """
        return self._claims

    @claims.setter
    def claims(self, claims):
        """Sets the claims of this Permission.


        :param claims: The claims of this Permission.
        :type claims: Dict[str, object]
        """

        self._claims = claims

    @property
    def rsid(self):
        """Gets the rsid of this Permission.


        :return: The rsid of this Permission.
        :rtype: str
        """
        return self._rsid

    @rsid.setter
    def rsid(self, rsid):
        """Sets the rsid of this Permission.


        :param rsid: The rsid of this Permission.
        :type rsid: str
        """

        self._rsid = rsid

    @property
    def rsname(self):
        """Gets the rsname of this Permission.


        :return: The rsname of this Permission.
        :rtype: str
        """
        return self._rsname

    @rsname.setter
    def rsname(self, rsname):
        """Sets the rsname of this Permission.


        :param rsname: The rsname of this Permission.
        :type rsname: str
        """

        self._rsname = rsname

    @property
    def scopes(self):
        """Gets the scopes of this Permission.


        :return: The scopes of this Permission.
        :rtype: List[str]
        """
        return self._scopes

    @scopes.setter
    def scopes(self, scopes):
        """Sets the scopes of this Permission.


        :param scopes: The scopes of this Permission.
        :type scopes: List[str]
        """

        self._scopes = scopes
