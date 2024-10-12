# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.error import Error
from openapi_server.models.patient_auth_init_response_auth import PatientAuthInitResponseAuth
from openapi_server.models.request_reference import RequestReference
from openapi_server import util


class PatientAuthInitResponse(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, auth: PatientAuthInitResponseAuth=None, error: Error=None, request_id: str=None, resp: RequestReference=None, timestamp: datetime=None):
        """PatientAuthInitResponse - a model defined in OpenAPI

        :param auth: The auth of this PatientAuthInitResponse.
        :param error: The error of this PatientAuthInitResponse.
        :param request_id: The request_id of this PatientAuthInitResponse.
        :param resp: The resp of this PatientAuthInitResponse.
        :param timestamp: The timestamp of this PatientAuthInitResponse.
        """
        self.openapi_types = {
            'auth': PatientAuthInitResponseAuth,
            'error': Error,
            'request_id': str,
            'resp': RequestReference,
            'timestamp': datetime
        }

        self.attribute_map = {
            'auth': 'auth',
            'error': 'error',
            'request_id': 'requestId',
            'resp': 'resp',
            'timestamp': 'timestamp'
        }

        self._auth = auth
        self._error = error
        self._request_id = request_id
        self._resp = resp
        self._timestamp = timestamp

    @classmethod
    def from_dict(cls, dikt: dict) -> 'PatientAuthInitResponse':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The PatientAuthInitResponse of this PatientAuthInitResponse.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def auth(self):
        """Gets the auth of this PatientAuthInitResponse.


        :return: The auth of this PatientAuthInitResponse.
        :rtype: PatientAuthInitResponseAuth
        """
        return self._auth

    @auth.setter
    def auth(self, auth):
        """Sets the auth of this PatientAuthInitResponse.


        :param auth: The auth of this PatientAuthInitResponse.
        :type auth: PatientAuthInitResponseAuth
        """

        self._auth = auth

    @property
    def error(self):
        """Gets the error of this PatientAuthInitResponse.


        :return: The error of this PatientAuthInitResponse.
        :rtype: Error
        """
        return self._error

    @error.setter
    def error(self, error):
        """Sets the error of this PatientAuthInitResponse.


        :param error: The error of this PatientAuthInitResponse.
        :type error: Error
        """

        self._error = error

    @property
    def request_id(self):
        """Gets the request_id of this PatientAuthInitResponse.

        a nonce, unique for each HTTP request

        :return: The request_id of this PatientAuthInitResponse.
        :rtype: str
        """
        return self._request_id

    @request_id.setter
    def request_id(self, request_id):
        """Sets the request_id of this PatientAuthInitResponse.

        a nonce, unique for each HTTP request

        :param request_id: The request_id of this PatientAuthInitResponse.
        :type request_id: str
        """
        if request_id is None:
            raise ValueError("Invalid value for `request_id`, must not be `None`")

        self._request_id = request_id

    @property
    def resp(self):
        """Gets the resp of this PatientAuthInitResponse.


        :return: The resp of this PatientAuthInitResponse.
        :rtype: RequestReference
        """
        return self._resp

    @resp.setter
    def resp(self, resp):
        """Sets the resp of this PatientAuthInitResponse.


        :param resp: The resp of this PatientAuthInitResponse.
        :type resp: RequestReference
        """
        if resp is None:
            raise ValueError("Invalid value for `resp`, must not be `None`")

        self._resp = resp

    @property
    def timestamp(self):
        """Gets the timestamp of this PatientAuthInitResponse.

        Date time format in UTC, includes miliseconds YYYY-MM-DDThh:mm:ss.vZ

        :return: The timestamp of this PatientAuthInitResponse.
        :rtype: datetime
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """Sets the timestamp of this PatientAuthInitResponse.

        Date time format in UTC, includes miliseconds YYYY-MM-DDThh:mm:ss.vZ

        :param timestamp: The timestamp of this PatientAuthInitResponse.
        :type timestamp: datetime
        """
        if timestamp is None:
            raise ValueError("Invalid value for `timestamp`, must not be `None`")

        self._timestamp = timestamp
