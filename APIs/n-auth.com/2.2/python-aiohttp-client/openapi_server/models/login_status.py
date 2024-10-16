# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class LoginStatus(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, accountid: int=None, canprovoke: bool=None, hsid: str=None, loggedin: bool=None, loginqrdata: str=None, pk: str=None, userid: str=None):
        """LoginStatus - a model defined in OpenAPI

        :param accountid: The accountid of this LoginStatus.
        :param canprovoke: The canprovoke of this LoginStatus.
        :param hsid: The hsid of this LoginStatus.
        :param loggedin: The loggedin of this LoginStatus.
        :param loginqrdata: The loginqrdata of this LoginStatus.
        :param pk: The pk of this LoginStatus.
        :param userid: The userid of this LoginStatus.
        """
        self.openapi_types = {
            'accountid': int,
            'canprovoke': bool,
            'hsid': str,
            'loggedin': bool,
            'loginqrdata': str,
            'pk': str,
            'userid': str
        }

        self.attribute_map = {
            'accountid': 'accountid',
            'canprovoke': 'canprovoke',
            'hsid': 'hsid',
            'loggedin': 'loggedin',
            'loginqrdata': 'loginqrdata',
            'pk': 'pk',
            'userid': 'userid'
        }

        self._accountid = accountid
        self._canprovoke = canprovoke
        self._hsid = hsid
        self._loggedin = loggedin
        self._loginqrdata = loginqrdata
        self._pk = pk
        self._userid = userid

    @classmethod
    def from_dict(cls, dikt: dict) -> 'LoginStatus':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The LoginStatus of this LoginStatus.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def accountid(self):
        """Gets the accountid of this LoginStatus.

        Account id

        :return: The accountid of this LoginStatus.
        :rtype: int
        """
        return self._accountid

    @accountid.setter
    def accountid(self, accountid):
        """Sets the accountid of this LoginStatus.

        Account id

        :param accountid: The accountid of this LoginStatus.
        :type accountid: int
        """

        self._accountid = accountid

    @property
    def canprovoke(self):
        """Gets the canprovoke of this LoginStatus.

        True if a login can be pushed from the server, false otherwise

        :return: The canprovoke of this LoginStatus.
        :rtype: bool
        """
        return self._canprovoke

    @canprovoke.setter
    def canprovoke(self, canprovoke):
        """Sets the canprovoke of this LoginStatus.

        True if a login can be pushed from the server, false otherwise

        :param canprovoke: The canprovoke of this LoginStatus.
        :type canprovoke: bool
        """

        self._canprovoke = canprovoke

    @property
    def hsid(self):
        """Gets the hsid of this LoginStatus.

        Converted session id, used by the websockets

        :return: The hsid of this LoginStatus.
        :rtype: str
        """
        return self._hsid

    @hsid.setter
    def hsid(self, hsid):
        """Sets the hsid of this LoginStatus.

        Converted session id, used by the websockets

        :param hsid: The hsid of this LoginStatus.
        :type hsid: str
        """

        self._hsid = hsid

    @property
    def loggedin(self):
        """Gets the loggedin of this LoginStatus.

        True if the user is loggedin, false otherwise

        :return: The loggedin of this LoginStatus.
        :rtype: bool
        """
        return self._loggedin

    @loggedin.setter
    def loggedin(self, loggedin):
        """Sets the loggedin of this LoginStatus.

        True if the user is loggedin, false otherwise

        :param loggedin: The loggedin of this LoginStatus.
        :type loggedin: bool
        """

        self._loggedin = loggedin

    @property
    def loginqrdata(self):
        """Gets the loginqrdata of this LoginStatus.

        Base64 encoded data that is represented in the login qr code

        :return: The loginqrdata of this LoginStatus.
        :rtype: str
        """
        return self._loginqrdata

    @loginqrdata.setter
    def loginqrdata(self, loginqrdata):
        """Sets the loginqrdata of this LoginStatus.

        Base64 encoded data that is represented in the login qr code

        :param loginqrdata: The loginqrdata of this LoginStatus.
        :type loginqrdata: str
        """

        self._loginqrdata = loginqrdata

    @property
    def pk(self):
        """Gets the pk of this LoginStatus.

        Base64 encoded public key of the nextAuth app. This uniquely identifies the account on the nextAuth app, regardless of the username

        :return: The pk of this LoginStatus.
        :rtype: str
        """
        return self._pk

    @pk.setter
    def pk(self, pk):
        """Sets the pk of this LoginStatus.

        Base64 encoded public key of the nextAuth app. This uniquely identifies the account on the nextAuth app, regardless of the username

        :param pk: The pk of this LoginStatus.
        :type pk: str
        """

        self._pk = pk

    @property
    def userid(self):
        """Gets the userid of this LoginStatus.

        User name

        :return: The userid of this LoginStatus.
        :rtype: str
        """
        return self._userid

    @userid.setter
    def userid(self, userid):
        """Sets the userid of this LoginStatus.

        User name

        :param userid: The userid of this LoginStatus.
        :type userid: str
        """

        self._userid = userid
