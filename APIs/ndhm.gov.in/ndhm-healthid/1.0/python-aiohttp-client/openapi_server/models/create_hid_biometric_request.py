# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
import re
from openapi_server import util


class CreateHidBiometricRequest(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, aadhaar: str=None, auto_generated_benefit_id: bool=None, benefit_id: str=None, benefit_name: str=None, bio_type: str=None, consent_health_id: bool=None, mobile_number: str=None, pid: str=None, validity: str=None):
        """CreateHidBiometricRequest - a model defined in OpenAPI

        :param aadhaar: The aadhaar of this CreateHidBiometricRequest.
        :param auto_generated_benefit_id: The auto_generated_benefit_id of this CreateHidBiometricRequest.
        :param benefit_id: The benefit_id of this CreateHidBiometricRequest.
        :param benefit_name: The benefit_name of this CreateHidBiometricRequest.
        :param bio_type: The bio_type of this CreateHidBiometricRequest.
        :param consent_health_id: The consent_health_id of this CreateHidBiometricRequest.
        :param mobile_number: The mobile_number of this CreateHidBiometricRequest.
        :param pid: The pid of this CreateHidBiometricRequest.
        :param validity: The validity of this CreateHidBiometricRequest.
        """
        self.openapi_types = {
            'aadhaar': str,
            'auto_generated_benefit_id': bool,
            'benefit_id': str,
            'benefit_name': str,
            'bio_type': str,
            'consent_health_id': bool,
            'mobile_number': str,
            'pid': str,
            'validity': str
        }

        self.attribute_map = {
            'aadhaar': 'aadhaar',
            'auto_generated_benefit_id': 'autoGeneratedBenefitId',
            'benefit_id': 'benefitId',
            'benefit_name': 'benefitName',
            'bio_type': 'bioType',
            'consent_health_id': 'consentHealthId',
            'mobile_number': 'mobileNumber',
            'pid': 'pid',
            'validity': 'validity'
        }

        self._aadhaar = aadhaar
        self._auto_generated_benefit_id = auto_generated_benefit_id
        self._benefit_id = benefit_id
        self._benefit_name = benefit_name
        self._bio_type = bio_type
        self._consent_health_id = consent_health_id
        self._mobile_number = mobile_number
        self._pid = pid
        self._validity = validity

    @classmethod
    def from_dict(cls, dikt: dict) -> 'CreateHidBiometricRequest':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The CreateHidBiometricRequest of this CreateHidBiometricRequest.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def aadhaar(self):
        """Gets the aadhaar of this CreateHidBiometricRequest.


        :return: The aadhaar of this CreateHidBiometricRequest.
        :rtype: str
        """
        return self._aadhaar

    @aadhaar.setter
    def aadhaar(self, aadhaar):
        """Sets the aadhaar of this CreateHidBiometricRequest.


        :param aadhaar: The aadhaar of this CreateHidBiometricRequest.
        :type aadhaar: str
        """
        if aadhaar is not None and not re.search(r'^(\d{12}|\d{16})*$', aadhaar):
            raise ValueError("Invalid value for `aadhaar`, must be a follow pattern or equal to `/^(\d{12}|\d{16})*$/`")

        self._aadhaar = aadhaar

    @property
    def auto_generated_benefit_id(self):
        """Gets the auto_generated_benefit_id of this CreateHidBiometricRequest.


        :return: The auto_generated_benefit_id of this CreateHidBiometricRequest.
        :rtype: bool
        """
        return self._auto_generated_benefit_id

    @auto_generated_benefit_id.setter
    def auto_generated_benefit_id(self, auto_generated_benefit_id):
        """Sets the auto_generated_benefit_id of this CreateHidBiometricRequest.


        :param auto_generated_benefit_id: The auto_generated_benefit_id of this CreateHidBiometricRequest.
        :type auto_generated_benefit_id: bool
        """

        self._auto_generated_benefit_id = auto_generated_benefit_id

    @property
    def benefit_id(self):
        """Gets the benefit_id of this CreateHidBiometricRequest.


        :return: The benefit_id of this CreateHidBiometricRequest.
        :rtype: str
        """
        return self._benefit_id

    @benefit_id.setter
    def benefit_id(self, benefit_id):
        """Sets the benefit_id of this CreateHidBiometricRequest.


        :param benefit_id: The benefit_id of this CreateHidBiometricRequest.
        :type benefit_id: str
        """

        self._benefit_id = benefit_id

    @property
    def benefit_name(self):
        """Gets the benefit_name of this CreateHidBiometricRequest.


        :return: The benefit_name of this CreateHidBiometricRequest.
        :rtype: str
        """
        return self._benefit_name

    @benefit_name.setter
    def benefit_name(self, benefit_name):
        """Sets the benefit_name of this CreateHidBiometricRequest.


        :param benefit_name: The benefit_name of this CreateHidBiometricRequest.
        :type benefit_name: str
        """

        self._benefit_name = benefit_name

    @property
    def bio_type(self):
        """Gets the bio_type of this CreateHidBiometricRequest.


        :return: The bio_type of this CreateHidBiometricRequest.
        :rtype: str
        """
        return self._bio_type

    @bio_type.setter
    def bio_type(self, bio_type):
        """Sets the bio_type of this CreateHidBiometricRequest.


        :param bio_type: The bio_type of this CreateHidBiometricRequest.
        :type bio_type: str
        """

        self._bio_type = bio_type

    @property
    def consent_health_id(self):
        """Gets the consent_health_id of this CreateHidBiometricRequest.


        :return: The consent_health_id of this CreateHidBiometricRequest.
        :rtype: bool
        """
        return self._consent_health_id

    @consent_health_id.setter
    def consent_health_id(self, consent_health_id):
        """Sets the consent_health_id of this CreateHidBiometricRequest.


        :param consent_health_id: The consent_health_id of this CreateHidBiometricRequest.
        :type consent_health_id: bool
        """

        self._consent_health_id = consent_health_id

    @property
    def mobile_number(self):
        """Gets the mobile_number of this CreateHidBiometricRequest.


        :return: The mobile_number of this CreateHidBiometricRequest.
        :rtype: str
        """
        return self._mobile_number

    @mobile_number.setter
    def mobile_number(self, mobile_number):
        """Sets the mobile_number of this CreateHidBiometricRequest.


        :param mobile_number: The mobile_number of this CreateHidBiometricRequest.
        :type mobile_number: str
        """

        self._mobile_number = mobile_number

    @property
    def pid(self):
        """Gets the pid of this CreateHidBiometricRequest.


        :return: The pid of this CreateHidBiometricRequest.
        :rtype: str
        """
        return self._pid

    @pid.setter
    def pid(self, pid):
        """Sets the pid of this CreateHidBiometricRequest.


        :param pid: The pid of this CreateHidBiometricRequest.
        :type pid: str
        """

        self._pid = pid

    @property
    def validity(self):
        """Gets the validity of this CreateHidBiometricRequest.


        :return: The validity of this CreateHidBiometricRequest.
        :rtype: str
        """
        return self._validity

    @validity.setter
    def validity(self, validity):
        """Sets the validity of this CreateHidBiometricRequest.


        :param validity: The validity of this CreateHidBiometricRequest.
        :type validity: str
        """

        self._validity = validity
