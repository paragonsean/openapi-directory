# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
import re
from openapi_server import util


class CreateHidNotifyBenefitRequest(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, aadhar_number_or_uid_token: str=None, auto_generated_benefit_id: bool=None, benefit_id: str=None, benefit_name: str=None, consent_health_id: bool=None, date_of_birth: str=None, gender: str=None, mobile_number: str=None, name: str=None, state_code: str=None, validity: str=None):
        """CreateHidNotifyBenefitRequest - a model defined in OpenAPI

        :param aadhar_number_or_uid_token: The aadhar_number_or_uid_token of this CreateHidNotifyBenefitRequest.
        :param auto_generated_benefit_id: The auto_generated_benefit_id of this CreateHidNotifyBenefitRequest.
        :param benefit_id: The benefit_id of this CreateHidNotifyBenefitRequest.
        :param benefit_name: The benefit_name of this CreateHidNotifyBenefitRequest.
        :param consent_health_id: The consent_health_id of this CreateHidNotifyBenefitRequest.
        :param date_of_birth: The date_of_birth of this CreateHidNotifyBenefitRequest.
        :param gender: The gender of this CreateHidNotifyBenefitRequest.
        :param mobile_number: The mobile_number of this CreateHidNotifyBenefitRequest.
        :param name: The name of this CreateHidNotifyBenefitRequest.
        :param state_code: The state_code of this CreateHidNotifyBenefitRequest.
        :param validity: The validity of this CreateHidNotifyBenefitRequest.
        """
        self.openapi_types = {
            'aadhar_number_or_uid_token': str,
            'auto_generated_benefit_id': bool,
            'benefit_id': str,
            'benefit_name': str,
            'consent_health_id': bool,
            'date_of_birth': str,
            'gender': str,
            'mobile_number': str,
            'name': str,
            'state_code': str,
            'validity': str
        }

        self.attribute_map = {
            'aadhar_number_or_uid_token': 'aadharNumberOrUidToken',
            'auto_generated_benefit_id': 'autoGeneratedBenefitId',
            'benefit_id': 'benefitId',
            'benefit_name': 'benefitName',
            'consent_health_id': 'consentHealthId',
            'date_of_birth': 'dateOfBirth',
            'gender': 'gender',
            'mobile_number': 'mobileNumber',
            'name': 'name',
            'state_code': 'stateCode',
            'validity': 'validity'
        }

        self._aadhar_number_or_uid_token = aadhar_number_or_uid_token
        self._auto_generated_benefit_id = auto_generated_benefit_id
        self._benefit_id = benefit_id
        self._benefit_name = benefit_name
        self._consent_health_id = consent_health_id
        self._date_of_birth = date_of_birth
        self._gender = gender
        self._mobile_number = mobile_number
        self._name = name
        self._state_code = state_code
        self._validity = validity

    @classmethod
    def from_dict(cls, dikt: dict) -> 'CreateHidNotifyBenefitRequest':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The CreateHidNotifyBenefitRequest of this CreateHidNotifyBenefitRequest.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def aadhar_number_or_uid_token(self):
        """Gets the aadhar_number_or_uid_token of this CreateHidNotifyBenefitRequest.


        :return: The aadhar_number_or_uid_token of this CreateHidNotifyBenefitRequest.
        :rtype: str
        """
        return self._aadhar_number_or_uid_token

    @aadhar_number_or_uid_token.setter
    def aadhar_number_or_uid_token(self, aadhar_number_or_uid_token):
        """Sets the aadhar_number_or_uid_token of this CreateHidNotifyBenefitRequest.


        :param aadhar_number_or_uid_token: The aadhar_number_or_uid_token of this CreateHidNotifyBenefitRequest.
        :type aadhar_number_or_uid_token: str
        """

        self._aadhar_number_or_uid_token = aadhar_number_or_uid_token

    @property
    def auto_generated_benefit_id(self):
        """Gets the auto_generated_benefit_id of this CreateHidNotifyBenefitRequest.


        :return: The auto_generated_benefit_id of this CreateHidNotifyBenefitRequest.
        :rtype: bool
        """
        return self._auto_generated_benefit_id

    @auto_generated_benefit_id.setter
    def auto_generated_benefit_id(self, auto_generated_benefit_id):
        """Sets the auto_generated_benefit_id of this CreateHidNotifyBenefitRequest.


        :param auto_generated_benefit_id: The auto_generated_benefit_id of this CreateHidNotifyBenefitRequest.
        :type auto_generated_benefit_id: bool
        """

        self._auto_generated_benefit_id = auto_generated_benefit_id

    @property
    def benefit_id(self):
        """Gets the benefit_id of this CreateHidNotifyBenefitRequest.


        :return: The benefit_id of this CreateHidNotifyBenefitRequest.
        :rtype: str
        """
        return self._benefit_id

    @benefit_id.setter
    def benefit_id(self, benefit_id):
        """Sets the benefit_id of this CreateHidNotifyBenefitRequest.


        :param benefit_id: The benefit_id of this CreateHidNotifyBenefitRequest.
        :type benefit_id: str
        """

        self._benefit_id = benefit_id

    @property
    def benefit_name(self):
        """Gets the benefit_name of this CreateHidNotifyBenefitRequest.


        :return: The benefit_name of this CreateHidNotifyBenefitRequest.
        :rtype: str
        """
        return self._benefit_name

    @benefit_name.setter
    def benefit_name(self, benefit_name):
        """Sets the benefit_name of this CreateHidNotifyBenefitRequest.


        :param benefit_name: The benefit_name of this CreateHidNotifyBenefitRequest.
        :type benefit_name: str
        """

        self._benefit_name = benefit_name

    @property
    def consent_health_id(self):
        """Gets the consent_health_id of this CreateHidNotifyBenefitRequest.


        :return: The consent_health_id of this CreateHidNotifyBenefitRequest.
        :rtype: bool
        """
        return self._consent_health_id

    @consent_health_id.setter
    def consent_health_id(self, consent_health_id):
        """Sets the consent_health_id of this CreateHidNotifyBenefitRequest.


        :param consent_health_id: The consent_health_id of this CreateHidNotifyBenefitRequest.
        :type consent_health_id: bool
        """

        self._consent_health_id = consent_health_id

    @property
    def date_of_birth(self):
        """Gets the date_of_birth of this CreateHidNotifyBenefitRequest.


        :return: The date_of_birth of this CreateHidNotifyBenefitRequest.
        :rtype: str
        """
        return self._date_of_birth

    @date_of_birth.setter
    def date_of_birth(self, date_of_birth):
        """Sets the date_of_birth of this CreateHidNotifyBenefitRequest.


        :param date_of_birth: The date_of_birth of this CreateHidNotifyBenefitRequest.
        :type date_of_birth: str
        """

        self._date_of_birth = date_of_birth

    @property
    def gender(self):
        """Gets the gender of this CreateHidNotifyBenefitRequest.


        :return: The gender of this CreateHidNotifyBenefitRequest.
        :rtype: str
        """
        return self._gender

    @gender.setter
    def gender(self, gender):
        """Sets the gender of this CreateHidNotifyBenefitRequest.


        :param gender: The gender of this CreateHidNotifyBenefitRequest.
        :type gender: str
        """
        if gender is not None and not re.search(r'^(M|F|T)$', gender):
            raise ValueError("Invalid value for `gender`, must be a follow pattern or equal to `/^(M|F|T)$/`")

        self._gender = gender

    @property
    def mobile_number(self):
        """Gets the mobile_number of this CreateHidNotifyBenefitRequest.


        :return: The mobile_number of this CreateHidNotifyBenefitRequest.
        :rtype: str
        """
        return self._mobile_number

    @mobile_number.setter
    def mobile_number(self, mobile_number):
        """Sets the mobile_number of this CreateHidNotifyBenefitRequest.


        :param mobile_number: The mobile_number of this CreateHidNotifyBenefitRequest.
        :type mobile_number: str
        """

        self._mobile_number = mobile_number

    @property
    def name(self):
        """Gets the name of this CreateHidNotifyBenefitRequest.


        :return: The name of this CreateHidNotifyBenefitRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CreateHidNotifyBenefitRequest.


        :param name: The name of this CreateHidNotifyBenefitRequest.
        :type name: str
        """

        self._name = name

    @property
    def state_code(self):
        """Gets the state_code of this CreateHidNotifyBenefitRequest.


        :return: The state_code of this CreateHidNotifyBenefitRequest.
        :rtype: str
        """
        return self._state_code

    @state_code.setter
    def state_code(self, state_code):
        """Sets the state_code of this CreateHidNotifyBenefitRequest.


        :param state_code: The state_code of this CreateHidNotifyBenefitRequest.
        :type state_code: str
        """

        self._state_code = state_code

    @property
    def validity(self):
        """Gets the validity of this CreateHidNotifyBenefitRequest.


        :return: The validity of this CreateHidNotifyBenefitRequest.
        :rtype: str
        """
        return self._validity

    @validity.setter
    def validity(self, validity):
        """Sets the validity of this CreateHidNotifyBenefitRequest.


        :param validity: The validity of this CreateHidNotifyBenefitRequest.
        :type validity: str
        """

        self._validity = validity
