# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.error import Error
from openapi_server.models.patient_identification_response_patient import PatientIdentificationResponsePatient
from openapi_server.models.request_reference import RequestReference
from openapi_server import util


class PatientIdentificationResponse(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, error: Error=None, patient: PatientIdentificationResponsePatient=None, request_id: str=None, resp: RequestReference=None, timestamp: datetime=None):
        """PatientIdentificationResponse - a model defined in OpenAPI

        :param error: The error of this PatientIdentificationResponse.
        :param patient: The patient of this PatientIdentificationResponse.
        :param request_id: The request_id of this PatientIdentificationResponse.
        :param resp: The resp of this PatientIdentificationResponse.
        :param timestamp: The timestamp of this PatientIdentificationResponse.
        """
        self.openapi_types = {
            'error': Error,
            'patient': PatientIdentificationResponsePatient,
            'request_id': str,
            'resp': RequestReference,
            'timestamp': datetime
        }

        self.attribute_map = {
            'error': 'error',
            'patient': 'patient',
            'request_id': 'requestId',
            'resp': 'resp',
            'timestamp': 'timestamp'
        }

        self._error = error
        self._patient = patient
        self._request_id = request_id
        self._resp = resp
        self._timestamp = timestamp

    @classmethod
    def from_dict(cls, dikt: dict) -> 'PatientIdentificationResponse':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The PatientIdentificationResponse of this PatientIdentificationResponse.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def error(self):
        """Gets the error of this PatientIdentificationResponse.


        :return: The error of this PatientIdentificationResponse.
        :rtype: Error
        """
        return self._error

    @error.setter
    def error(self, error):
        """Sets the error of this PatientIdentificationResponse.


        :param error: The error of this PatientIdentificationResponse.
        :type error: Error
        """

        self._error = error

    @property
    def patient(self):
        """Gets the patient of this PatientIdentificationResponse.


        :return: The patient of this PatientIdentificationResponse.
        :rtype: PatientIdentificationResponsePatient
        """
        return self._patient

    @patient.setter
    def patient(self, patient):
        """Sets the patient of this PatientIdentificationResponse.


        :param patient: The patient of this PatientIdentificationResponse.
        :type patient: PatientIdentificationResponsePatient
        """

        self._patient = patient

    @property
    def request_id(self):
        """Gets the request_id of this PatientIdentificationResponse.

        a nonce, unique for each HTTP request

        :return: The request_id of this PatientIdentificationResponse.
        :rtype: str
        """
        return self._request_id

    @request_id.setter
    def request_id(self, request_id):
        """Sets the request_id of this PatientIdentificationResponse.

        a nonce, unique for each HTTP request

        :param request_id: The request_id of this PatientIdentificationResponse.
        :type request_id: str
        """
        if request_id is None:
            raise ValueError("Invalid value for `request_id`, must not be `None`")

        self._request_id = request_id

    @property
    def resp(self):
        """Gets the resp of this PatientIdentificationResponse.


        :return: The resp of this PatientIdentificationResponse.
        :rtype: RequestReference
        """
        return self._resp

    @resp.setter
    def resp(self, resp):
        """Sets the resp of this PatientIdentificationResponse.


        :param resp: The resp of this PatientIdentificationResponse.
        :type resp: RequestReference
        """
        if resp is None:
            raise ValueError("Invalid value for `resp`, must not be `None`")

        self._resp = resp

    @property
    def timestamp(self):
        """Gets the timestamp of this PatientIdentificationResponse.

        Date time format in UTC, includes miliseconds YYYY-MM-DDThh:mm:ss.vZ

        :return: The timestamp of this PatientIdentificationResponse.
        :rtype: datetime
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """Sets the timestamp of this PatientIdentificationResponse.

        Date time format in UTC, includes miliseconds YYYY-MM-DDThh:mm:ss.vZ

        :param timestamp: The timestamp of this PatientIdentificationResponse.
        :type timestamp: datetime
        """
        if timestamp is None:
            raise ValueError("Invalid value for `timestamp`, must not be `None`")

        self._timestamp = timestamp
