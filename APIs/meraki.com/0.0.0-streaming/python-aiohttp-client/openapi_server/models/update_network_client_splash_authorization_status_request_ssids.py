# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.update_network_client_splash_authorization_status_request_ssids0 import UpdateNetworkClientSplashAuthorizationStatusRequestSsids0
from openapi_server.models.update_network_client_splash_authorization_status_request_ssids1 import UpdateNetworkClientSplashAuthorizationStatusRequestSsids1
from openapi_server.models.update_network_client_splash_authorization_status_request_ssids10 import UpdateNetworkClientSplashAuthorizationStatusRequestSsids10
from openapi_server.models.update_network_client_splash_authorization_status_request_ssids11 import UpdateNetworkClientSplashAuthorizationStatusRequestSsids11
from openapi_server.models.update_network_client_splash_authorization_status_request_ssids12 import UpdateNetworkClientSplashAuthorizationStatusRequestSsids12
from openapi_server.models.update_network_client_splash_authorization_status_request_ssids13 import UpdateNetworkClientSplashAuthorizationStatusRequestSsids13
from openapi_server.models.update_network_client_splash_authorization_status_request_ssids14 import UpdateNetworkClientSplashAuthorizationStatusRequestSsids14
from openapi_server.models.update_network_client_splash_authorization_status_request_ssids2 import UpdateNetworkClientSplashAuthorizationStatusRequestSsids2
from openapi_server.models.update_network_client_splash_authorization_status_request_ssids3 import UpdateNetworkClientSplashAuthorizationStatusRequestSsids3
from openapi_server.models.update_network_client_splash_authorization_status_request_ssids4 import UpdateNetworkClientSplashAuthorizationStatusRequestSsids4
from openapi_server.models.update_network_client_splash_authorization_status_request_ssids5 import UpdateNetworkClientSplashAuthorizationStatusRequestSsids5
from openapi_server.models.update_network_client_splash_authorization_status_request_ssids6 import UpdateNetworkClientSplashAuthorizationStatusRequestSsids6
from openapi_server.models.update_network_client_splash_authorization_status_request_ssids7 import UpdateNetworkClientSplashAuthorizationStatusRequestSsids7
from openapi_server.models.update_network_client_splash_authorization_status_request_ssids8 import UpdateNetworkClientSplashAuthorizationStatusRequestSsids8
from openapi_server.models.update_network_client_splash_authorization_status_request_ssids9 import UpdateNetworkClientSplashAuthorizationStatusRequestSsids9
from openapi_server import util


class UpdateNetworkClientSplashAuthorizationStatusRequestSsids(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, _0: UpdateNetworkClientSplashAuthorizationStatusRequestSsids0=None, _1: UpdateNetworkClientSplashAuthorizationStatusRequestSsids1=None, _2: UpdateNetworkClientSplashAuthorizationStatusRequestSsids2=None, _3: UpdateNetworkClientSplashAuthorizationStatusRequestSsids3=None, _4: UpdateNetworkClientSplashAuthorizationStatusRequestSsids4=None, _5: UpdateNetworkClientSplashAuthorizationStatusRequestSsids5=None, _6: UpdateNetworkClientSplashAuthorizationStatusRequestSsids6=None, _7: UpdateNetworkClientSplashAuthorizationStatusRequestSsids7=None, _8: UpdateNetworkClientSplashAuthorizationStatusRequestSsids8=None, _9: UpdateNetworkClientSplashAuthorizationStatusRequestSsids9=None, _10: UpdateNetworkClientSplashAuthorizationStatusRequestSsids10=None, _11: UpdateNetworkClientSplashAuthorizationStatusRequestSsids11=None, _12: UpdateNetworkClientSplashAuthorizationStatusRequestSsids12=None, _13: UpdateNetworkClientSplashAuthorizationStatusRequestSsids13=None, _14: UpdateNetworkClientSplashAuthorizationStatusRequestSsids14=None):
        """UpdateNetworkClientSplashAuthorizationStatusRequestSsids - a model defined in OpenAPI

        :param _0: The _0 of this UpdateNetworkClientSplashAuthorizationStatusRequestSsids.
        :param _1: The _1 of this UpdateNetworkClientSplashAuthorizationStatusRequestSsids.
        :param _2: The _2 of this UpdateNetworkClientSplashAuthorizationStatusRequestSsids.
        :param _3: The _3 of this UpdateNetworkClientSplashAuthorizationStatusRequestSsids.
        :param _4: The _4 of this UpdateNetworkClientSplashAuthorizationStatusRequestSsids.
        :param _5: The _5 of this UpdateNetworkClientSplashAuthorizationStatusRequestSsids.
        :param _6: The _6 of this UpdateNetworkClientSplashAuthorizationStatusRequestSsids.
        :param _7: The _7 of this UpdateNetworkClientSplashAuthorizationStatusRequestSsids.
        :param _8: The _8 of this UpdateNetworkClientSplashAuthorizationStatusRequestSsids.
        :param _9: The _9 of this UpdateNetworkClientSplashAuthorizationStatusRequestSsids.
        :param _10: The _10 of this UpdateNetworkClientSplashAuthorizationStatusRequestSsids.
        :param _11: The _11 of this UpdateNetworkClientSplashAuthorizationStatusRequestSsids.
        :param _12: The _12 of this UpdateNetworkClientSplashAuthorizationStatusRequestSsids.
        :param _13: The _13 of this UpdateNetworkClientSplashAuthorizationStatusRequestSsids.
        :param _14: The _14 of this UpdateNetworkClientSplashAuthorizationStatusRequestSsids.
        """
        self.openapi_types = {
            '_0': UpdateNetworkClientSplashAuthorizationStatusRequestSsids0,
            '_1': UpdateNetworkClientSplashAuthorizationStatusRequestSsids1,
            '_2': UpdateNetworkClientSplashAuthorizationStatusRequestSsids2,
            '_3': UpdateNetworkClientSplashAuthorizationStatusRequestSsids3,
            '_4': UpdateNetworkClientSplashAuthorizationStatusRequestSsids4,
            '_5': UpdateNetworkClientSplashAuthorizationStatusRequestSsids5,
            '_6': UpdateNetworkClientSplashAuthorizationStatusRequestSsids6,
            '_7': UpdateNetworkClientSplashAuthorizationStatusRequestSsids7,
            '_8': UpdateNetworkClientSplashAuthorizationStatusRequestSsids8,
            '_9': UpdateNetworkClientSplashAuthorizationStatusRequestSsids9,
            '_10': UpdateNetworkClientSplashAuthorizationStatusRequestSsids10,
            '_11': UpdateNetworkClientSplashAuthorizationStatusRequestSsids11,
            '_12': UpdateNetworkClientSplashAuthorizationStatusRequestSsids12,
            '_13': UpdateNetworkClientSplashAuthorizationStatusRequestSsids13,
            '_14': UpdateNetworkClientSplashAuthorizationStatusRequestSsids14
        }

        self.attribute_map = {
            '_0': '0',
            '_1': '1',
            '_2': '2',
            '_3': '3',
            '_4': '4',
            '_5': '5',
            '_6': '6',
            '_7': '7',
            '_8': '8',
            '_9': '9',
            '_10': '10',
            '_11': '11',
            '_12': '12',
            '_13': '13',
            '_14': '14'
        }

        self.__0 = _0
        self.__1 = _1
        self.__2 = _2
        self.__3 = _3
        self.__4 = _4
        self.__5 = _5
        self.__6 = _6
        self.__7 = _7
        self.__8 = _8
        self.__9 = _9
        self.__10 = _10
        self.__11 = _11
        self.__12 = _12
        self.__13 = _13
        self.__14 = _14

    @classmethod
    def from_dict(cls, dikt: dict) -> 'UpdateNetworkClientSplashAuthorizationStatusRequestSsids':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The updateNetworkClientSplashAuthorizationStatus_request_ssids of this UpdateNetworkClientSplashAuthorizationStatusRequestSsids.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def _0(self):
        """Gets the _0 of this UpdateNetworkClientSplashAuthorizationStatusRequestSsids.


        :return: The _0 of this UpdateNetworkClientSplashAuthorizationStatusRequestSsids.
        :rtype: UpdateNetworkClientSplashAuthorizationStatusRequestSsids0
        """
        return self.__0

    @_0.setter
    def _0(self, _0):
        """Sets the _0 of this UpdateNetworkClientSplashAuthorizationStatusRequestSsids.


        :param _0: The _0 of this UpdateNetworkClientSplashAuthorizationStatusRequestSsids.
        :type _0: UpdateNetworkClientSplashAuthorizationStatusRequestSsids0
        """

        self.__0 = _0

    @property
    def _1(self):
        """Gets the _1 of this UpdateNetworkClientSplashAuthorizationStatusRequestSsids.


        :return: The _1 of this UpdateNetworkClientSplashAuthorizationStatusRequestSsids.
        :rtype: UpdateNetworkClientSplashAuthorizationStatusRequestSsids1
        """
        return self.__1

    @_1.setter
    def _1(self, _1):
        """Sets the _1 of this UpdateNetworkClientSplashAuthorizationStatusRequestSsids.


        :param _1: The _1 of this UpdateNetworkClientSplashAuthorizationStatusRequestSsids.
        :type _1: UpdateNetworkClientSplashAuthorizationStatusRequestSsids1
        """

        self.__1 = _1

    @property
    def _2(self):
        """Gets the _2 of this UpdateNetworkClientSplashAuthorizationStatusRequestSsids.


        :return: The _2 of this UpdateNetworkClientSplashAuthorizationStatusRequestSsids.
        :rtype: UpdateNetworkClientSplashAuthorizationStatusRequestSsids2
        """
        return self.__2

    @_2.setter
    def _2(self, _2):
        """Sets the _2 of this UpdateNetworkClientSplashAuthorizationStatusRequestSsids.


        :param _2: The _2 of this UpdateNetworkClientSplashAuthorizationStatusRequestSsids.
        :type _2: UpdateNetworkClientSplashAuthorizationStatusRequestSsids2
        """

        self.__2 = _2

    @property
    def _3(self):
        """Gets the _3 of this UpdateNetworkClientSplashAuthorizationStatusRequestSsids.


        :return: The _3 of this UpdateNetworkClientSplashAuthorizationStatusRequestSsids.
        :rtype: UpdateNetworkClientSplashAuthorizationStatusRequestSsids3
        """
        return self.__3

    @_3.setter
    def _3(self, _3):
        """Sets the _3 of this UpdateNetworkClientSplashAuthorizationStatusRequestSsids.


        :param _3: The _3 of this UpdateNetworkClientSplashAuthorizationStatusRequestSsids.
        :type _3: UpdateNetworkClientSplashAuthorizationStatusRequestSsids3
        """

        self.__3 = _3

    @property
    def _4(self):
        """Gets the _4 of this UpdateNetworkClientSplashAuthorizationStatusRequestSsids.


        :return: The _4 of this UpdateNetworkClientSplashAuthorizationStatusRequestSsids.
        :rtype: UpdateNetworkClientSplashAuthorizationStatusRequestSsids4
        """
        return self.__4

    @_4.setter
    def _4(self, _4):
        """Sets the _4 of this UpdateNetworkClientSplashAuthorizationStatusRequestSsids.


        :param _4: The _4 of this UpdateNetworkClientSplashAuthorizationStatusRequestSsids.
        :type _4: UpdateNetworkClientSplashAuthorizationStatusRequestSsids4
        """

        self.__4 = _4

    @property
    def _5(self):
        """Gets the _5 of this UpdateNetworkClientSplashAuthorizationStatusRequestSsids.


        :return: The _5 of this UpdateNetworkClientSplashAuthorizationStatusRequestSsids.
        :rtype: UpdateNetworkClientSplashAuthorizationStatusRequestSsids5
        """
        return self.__5

    @_5.setter
    def _5(self, _5):
        """Sets the _5 of this UpdateNetworkClientSplashAuthorizationStatusRequestSsids.


        :param _5: The _5 of this UpdateNetworkClientSplashAuthorizationStatusRequestSsids.
        :type _5: UpdateNetworkClientSplashAuthorizationStatusRequestSsids5
        """

        self.__5 = _5

    @property
    def _6(self):
        """Gets the _6 of this UpdateNetworkClientSplashAuthorizationStatusRequestSsids.


        :return: The _6 of this UpdateNetworkClientSplashAuthorizationStatusRequestSsids.
        :rtype: UpdateNetworkClientSplashAuthorizationStatusRequestSsids6
        """
        return self.__6

    @_6.setter
    def _6(self, _6):
        """Sets the _6 of this UpdateNetworkClientSplashAuthorizationStatusRequestSsids.


        :param _6: The _6 of this UpdateNetworkClientSplashAuthorizationStatusRequestSsids.
        :type _6: UpdateNetworkClientSplashAuthorizationStatusRequestSsids6
        """

        self.__6 = _6

    @property
    def _7(self):
        """Gets the _7 of this UpdateNetworkClientSplashAuthorizationStatusRequestSsids.


        :return: The _7 of this UpdateNetworkClientSplashAuthorizationStatusRequestSsids.
        :rtype: UpdateNetworkClientSplashAuthorizationStatusRequestSsids7
        """
        return self.__7

    @_7.setter
    def _7(self, _7):
        """Sets the _7 of this UpdateNetworkClientSplashAuthorizationStatusRequestSsids.


        :param _7: The _7 of this UpdateNetworkClientSplashAuthorizationStatusRequestSsids.
        :type _7: UpdateNetworkClientSplashAuthorizationStatusRequestSsids7
        """

        self.__7 = _7

    @property
    def _8(self):
        """Gets the _8 of this UpdateNetworkClientSplashAuthorizationStatusRequestSsids.


        :return: The _8 of this UpdateNetworkClientSplashAuthorizationStatusRequestSsids.
        :rtype: UpdateNetworkClientSplashAuthorizationStatusRequestSsids8
        """
        return self.__8

    @_8.setter
    def _8(self, _8):
        """Sets the _8 of this UpdateNetworkClientSplashAuthorizationStatusRequestSsids.


        :param _8: The _8 of this UpdateNetworkClientSplashAuthorizationStatusRequestSsids.
        :type _8: UpdateNetworkClientSplashAuthorizationStatusRequestSsids8
        """

        self.__8 = _8

    @property
    def _9(self):
        """Gets the _9 of this UpdateNetworkClientSplashAuthorizationStatusRequestSsids.


        :return: The _9 of this UpdateNetworkClientSplashAuthorizationStatusRequestSsids.
        :rtype: UpdateNetworkClientSplashAuthorizationStatusRequestSsids9
        """
        return self.__9

    @_9.setter
    def _9(self, _9):
        """Sets the _9 of this UpdateNetworkClientSplashAuthorizationStatusRequestSsids.


        :param _9: The _9 of this UpdateNetworkClientSplashAuthorizationStatusRequestSsids.
        :type _9: UpdateNetworkClientSplashAuthorizationStatusRequestSsids9
        """

        self.__9 = _9

    @property
    def _10(self):
        """Gets the _10 of this UpdateNetworkClientSplashAuthorizationStatusRequestSsids.


        :return: The _10 of this UpdateNetworkClientSplashAuthorizationStatusRequestSsids.
        :rtype: UpdateNetworkClientSplashAuthorizationStatusRequestSsids10
        """
        return self.__10

    @_10.setter
    def _10(self, _10):
        """Sets the _10 of this UpdateNetworkClientSplashAuthorizationStatusRequestSsids.


        :param _10: The _10 of this UpdateNetworkClientSplashAuthorizationStatusRequestSsids.
        :type _10: UpdateNetworkClientSplashAuthorizationStatusRequestSsids10
        """

        self.__10 = _10

    @property
    def _11(self):
        """Gets the _11 of this UpdateNetworkClientSplashAuthorizationStatusRequestSsids.


        :return: The _11 of this UpdateNetworkClientSplashAuthorizationStatusRequestSsids.
        :rtype: UpdateNetworkClientSplashAuthorizationStatusRequestSsids11
        """
        return self.__11

    @_11.setter
    def _11(self, _11):
        """Sets the _11 of this UpdateNetworkClientSplashAuthorizationStatusRequestSsids.


        :param _11: The _11 of this UpdateNetworkClientSplashAuthorizationStatusRequestSsids.
        :type _11: UpdateNetworkClientSplashAuthorizationStatusRequestSsids11
        """

        self.__11 = _11

    @property
    def _12(self):
        """Gets the _12 of this UpdateNetworkClientSplashAuthorizationStatusRequestSsids.


        :return: The _12 of this UpdateNetworkClientSplashAuthorizationStatusRequestSsids.
        :rtype: UpdateNetworkClientSplashAuthorizationStatusRequestSsids12
        """
        return self.__12

    @_12.setter
    def _12(self, _12):
        """Sets the _12 of this UpdateNetworkClientSplashAuthorizationStatusRequestSsids.


        :param _12: The _12 of this UpdateNetworkClientSplashAuthorizationStatusRequestSsids.
        :type _12: UpdateNetworkClientSplashAuthorizationStatusRequestSsids12
        """

        self.__12 = _12

    @property
    def _13(self):
        """Gets the _13 of this UpdateNetworkClientSplashAuthorizationStatusRequestSsids.


        :return: The _13 of this UpdateNetworkClientSplashAuthorizationStatusRequestSsids.
        :rtype: UpdateNetworkClientSplashAuthorizationStatusRequestSsids13
        """
        return self.__13

    @_13.setter
    def _13(self, _13):
        """Sets the _13 of this UpdateNetworkClientSplashAuthorizationStatusRequestSsids.


        :param _13: The _13 of this UpdateNetworkClientSplashAuthorizationStatusRequestSsids.
        :type _13: UpdateNetworkClientSplashAuthorizationStatusRequestSsids13
        """

        self.__13 = _13

    @property
    def _14(self):
        """Gets the _14 of this UpdateNetworkClientSplashAuthorizationStatusRequestSsids.


        :return: The _14 of this UpdateNetworkClientSplashAuthorizationStatusRequestSsids.
        :rtype: UpdateNetworkClientSplashAuthorizationStatusRequestSsids14
        """
        return self.__14

    @_14.setter
    def _14(self, _14):
        """Sets the _14 of this UpdateNetworkClientSplashAuthorizationStatusRequestSsids.


        :param _14: The _14 of this UpdateNetworkClientSplashAuthorizationStatusRequestSsids.
        :type _14: UpdateNetworkClientSplashAuthorizationStatusRequestSsids14
        """

        self.__14 = _14
