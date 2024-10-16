# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class PrimaryInsurance(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, insurance_claim_office_number: str=None, insurance_company: str=None, insurance_group_name: str=None, insurance_group_number: str=None, insurance_id_number: str=None, insurance_payer_id: str=None, insurance_plan_name: str=None, insurance_plan_type: str=None, is_subscriber_the_patient: bool=None, patient_relationship_to_subscriber: str=None, photo_back: str=None, photo_front: str=None, subscriber_address: str=None, subscriber_city: str=None, subscriber_country: str=None, subscriber_date_of_birth: str=None, subscriber_first_name: str=None, subscriber_gender: str=None, subscriber_last_name: str=None, subscriber_middle_name: str=None, subscriber_social_security: str=None, subscriber_state: str=None, subscriber_suffix: str=None, subscriber_zip_code: str=None):
        """PrimaryInsurance - a model defined in OpenAPI

        :param insurance_claim_office_number: The insurance_claim_office_number of this PrimaryInsurance.
        :param insurance_company: The insurance_company of this PrimaryInsurance.
        :param insurance_group_name: The insurance_group_name of this PrimaryInsurance.
        :param insurance_group_number: The insurance_group_number of this PrimaryInsurance.
        :param insurance_id_number: The insurance_id_number of this PrimaryInsurance.
        :param insurance_payer_id: The insurance_payer_id of this PrimaryInsurance.
        :param insurance_plan_name: The insurance_plan_name of this PrimaryInsurance.
        :param insurance_plan_type: The insurance_plan_type of this PrimaryInsurance.
        :param is_subscriber_the_patient: The is_subscriber_the_patient of this PrimaryInsurance.
        :param patient_relationship_to_subscriber: The patient_relationship_to_subscriber of this PrimaryInsurance.
        :param photo_back: The photo_back of this PrimaryInsurance.
        :param photo_front: The photo_front of this PrimaryInsurance.
        :param subscriber_address: The subscriber_address of this PrimaryInsurance.
        :param subscriber_city: The subscriber_city of this PrimaryInsurance.
        :param subscriber_country: The subscriber_country of this PrimaryInsurance.
        :param subscriber_date_of_birth: The subscriber_date_of_birth of this PrimaryInsurance.
        :param subscriber_first_name: The subscriber_first_name of this PrimaryInsurance.
        :param subscriber_gender: The subscriber_gender of this PrimaryInsurance.
        :param subscriber_last_name: The subscriber_last_name of this PrimaryInsurance.
        :param subscriber_middle_name: The subscriber_middle_name of this PrimaryInsurance.
        :param subscriber_social_security: The subscriber_social_security of this PrimaryInsurance.
        :param subscriber_state: The subscriber_state of this PrimaryInsurance.
        :param subscriber_suffix: The subscriber_suffix of this PrimaryInsurance.
        :param subscriber_zip_code: The subscriber_zip_code of this PrimaryInsurance.
        """
        self.openapi_types = {
            'insurance_claim_office_number': str,
            'insurance_company': str,
            'insurance_group_name': str,
            'insurance_group_number': str,
            'insurance_id_number': str,
            'insurance_payer_id': str,
            'insurance_plan_name': str,
            'insurance_plan_type': str,
            'is_subscriber_the_patient': bool,
            'patient_relationship_to_subscriber': str,
            'photo_back': str,
            'photo_front': str,
            'subscriber_address': str,
            'subscriber_city': str,
            'subscriber_country': str,
            'subscriber_date_of_birth': str,
            'subscriber_first_name': str,
            'subscriber_gender': str,
            'subscriber_last_name': str,
            'subscriber_middle_name': str,
            'subscriber_social_security': str,
            'subscriber_state': str,
            'subscriber_suffix': str,
            'subscriber_zip_code': str
        }

        self.attribute_map = {
            'insurance_claim_office_number': 'insurance_claim_office_number',
            'insurance_company': 'insurance_company',
            'insurance_group_name': 'insurance_group_name',
            'insurance_group_number': 'insurance_group_number',
            'insurance_id_number': 'insurance_id_number',
            'insurance_payer_id': 'insurance_payer_id',
            'insurance_plan_name': 'insurance_plan_name',
            'insurance_plan_type': 'insurance_plan_type',
            'is_subscriber_the_patient': 'is_subscriber_the_patient',
            'patient_relationship_to_subscriber': 'patient_relationship_to_subscriber',
            'photo_back': 'photo_back',
            'photo_front': 'photo_front',
            'subscriber_address': 'subscriber_address',
            'subscriber_city': 'subscriber_city',
            'subscriber_country': 'subscriber_country',
            'subscriber_date_of_birth': 'subscriber_date_of_birth',
            'subscriber_first_name': 'subscriber_first_name',
            'subscriber_gender': 'subscriber_gender',
            'subscriber_last_name': 'subscriber_last_name',
            'subscriber_middle_name': 'subscriber_middle_name',
            'subscriber_social_security': 'subscriber_social_security',
            'subscriber_state': 'subscriber_state',
            'subscriber_suffix': 'subscriber_suffix',
            'subscriber_zip_code': 'subscriber_zip_code'
        }

        self._insurance_claim_office_number = insurance_claim_office_number
        self._insurance_company = insurance_company
        self._insurance_group_name = insurance_group_name
        self._insurance_group_number = insurance_group_number
        self._insurance_id_number = insurance_id_number
        self._insurance_payer_id = insurance_payer_id
        self._insurance_plan_name = insurance_plan_name
        self._insurance_plan_type = insurance_plan_type
        self._is_subscriber_the_patient = is_subscriber_the_patient
        self._patient_relationship_to_subscriber = patient_relationship_to_subscriber
        self._photo_back = photo_back
        self._photo_front = photo_front
        self._subscriber_address = subscriber_address
        self._subscriber_city = subscriber_city
        self._subscriber_country = subscriber_country
        self._subscriber_date_of_birth = subscriber_date_of_birth
        self._subscriber_first_name = subscriber_first_name
        self._subscriber_gender = subscriber_gender
        self._subscriber_last_name = subscriber_last_name
        self._subscriber_middle_name = subscriber_middle_name
        self._subscriber_social_security = subscriber_social_security
        self._subscriber_state = subscriber_state
        self._subscriber_suffix = subscriber_suffix
        self._subscriber_zip_code = subscriber_zip_code

    @classmethod
    def from_dict(cls, dikt: dict) -> 'PrimaryInsurance':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The PrimaryInsurance of this PrimaryInsurance.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def insurance_claim_office_number(self):
        """Gets the insurance_claim_office_number of this PrimaryInsurance.

        Insurance office phone number

        :return: The insurance_claim_office_number of this PrimaryInsurance.
        :rtype: str
        """
        return self._insurance_claim_office_number

    @insurance_claim_office_number.setter
    def insurance_claim_office_number(self, insurance_claim_office_number):
        """Sets the insurance_claim_office_number of this PrimaryInsurance.

        Insurance office phone number

        :param insurance_claim_office_number: The insurance_claim_office_number of this PrimaryInsurance.
        :type insurance_claim_office_number: str
        """

        self._insurance_claim_office_number = insurance_claim_office_number

    @property
    def insurance_company(self):
        """Gets the insurance_company of this PrimaryInsurance.

        

        :return: The insurance_company of this PrimaryInsurance.
        :rtype: str
        """
        return self._insurance_company

    @insurance_company.setter
    def insurance_company(self, insurance_company):
        """Sets the insurance_company of this PrimaryInsurance.

        

        :param insurance_company: The insurance_company of this PrimaryInsurance.
        :type insurance_company: str
        """

        self._insurance_company = insurance_company

    @property
    def insurance_group_name(self):
        """Gets the insurance_group_name of this PrimaryInsurance.

        

        :return: The insurance_group_name of this PrimaryInsurance.
        :rtype: str
        """
        return self._insurance_group_name

    @insurance_group_name.setter
    def insurance_group_name(self, insurance_group_name):
        """Sets the insurance_group_name of this PrimaryInsurance.

        

        :param insurance_group_name: The insurance_group_name of this PrimaryInsurance.
        :type insurance_group_name: str
        """

        self._insurance_group_name = insurance_group_name

    @property
    def insurance_group_number(self):
        """Gets the insurance_group_number of this PrimaryInsurance.

        

        :return: The insurance_group_number of this PrimaryInsurance.
        :rtype: str
        """
        return self._insurance_group_number

    @insurance_group_number.setter
    def insurance_group_number(self, insurance_group_number):
        """Sets the insurance_group_number of this PrimaryInsurance.

        

        :param insurance_group_number: The insurance_group_number of this PrimaryInsurance.
        :type insurance_group_number: str
        """

        self._insurance_group_number = insurance_group_number

    @property
    def insurance_id_number(self):
        """Gets the insurance_id_number of this PrimaryInsurance.

        

        :return: The insurance_id_number of this PrimaryInsurance.
        :rtype: str
        """
        return self._insurance_id_number

    @insurance_id_number.setter
    def insurance_id_number(self, insurance_id_number):
        """Sets the insurance_id_number of this PrimaryInsurance.

        

        :param insurance_id_number: The insurance_id_number of this PrimaryInsurance.
        :type insurance_id_number: str
        """

        self._insurance_id_number = insurance_id_number

    @property
    def insurance_payer_id(self):
        """Gets the insurance_payer_id of this PrimaryInsurance.

        

        :return: The insurance_payer_id of this PrimaryInsurance.
        :rtype: str
        """
        return self._insurance_payer_id

    @insurance_payer_id.setter
    def insurance_payer_id(self, insurance_payer_id):
        """Sets the insurance_payer_id of this PrimaryInsurance.

        

        :param insurance_payer_id: The insurance_payer_id of this PrimaryInsurance.
        :type insurance_payer_id: str
        """

        self._insurance_payer_id = insurance_payer_id

    @property
    def insurance_plan_name(self):
        """Gets the insurance_plan_name of this PrimaryInsurance.

        Name of insurance plan.

        :return: The insurance_plan_name of this PrimaryInsurance.
        :rtype: str
        """
        return self._insurance_plan_name

    @insurance_plan_name.setter
    def insurance_plan_name(self, insurance_plan_name):
        """Sets the insurance_plan_name of this PrimaryInsurance.

        Name of insurance plan.

        :param insurance_plan_name: The insurance_plan_name of this PrimaryInsurance.
        :type insurance_plan_name: str
        """

        self._insurance_plan_name = insurance_plan_name

    @property
    def insurance_plan_type(self):
        """Gets the insurance_plan_type of this PrimaryInsurance.

        

        :return: The insurance_plan_type of this PrimaryInsurance.
        :rtype: str
        """
        return self._insurance_plan_type

    @insurance_plan_type.setter
    def insurance_plan_type(self, insurance_plan_type):
        """Sets the insurance_plan_type of this PrimaryInsurance.

        

        :param insurance_plan_type: The insurance_plan_type of this PrimaryInsurance.
        :type insurance_plan_type: str
        """
        allowed_values = ["", "AM", "BL", "CH", "CI", "17", "DS", "14", "FI", "HM", "16", "15", "LM", "MC", "MA", "MB", "ZZ", "OF", "11", "13", "12", "TV", "VA", "WC"]  # noqa: E501
        if insurance_plan_type not in allowed_values:
            raise ValueError(
                "Invalid value for `insurance_plan_type` ({0}), must be one of {1}"
                .format(insurance_plan_type, allowed_values)
            )

        self._insurance_plan_type = insurance_plan_type

    @property
    def is_subscriber_the_patient(self):
        """Gets the is_subscriber_the_patient of this PrimaryInsurance.

        True if the insurance policy is under patient's own name. Defaults to true

        :return: The is_subscriber_the_patient of this PrimaryInsurance.
        :rtype: bool
        """
        return self._is_subscriber_the_patient

    @is_subscriber_the_patient.setter
    def is_subscriber_the_patient(self, is_subscriber_the_patient):
        """Sets the is_subscriber_the_patient of this PrimaryInsurance.

        True if the insurance policy is under patient's own name. Defaults to true

        :param is_subscriber_the_patient: The is_subscriber_the_patient of this PrimaryInsurance.
        :type is_subscriber_the_patient: bool
        """

        self._is_subscriber_the_patient = is_subscriber_the_patient

    @property
    def patient_relationship_to_subscriber(self):
        """Gets the patient_relationship_to_subscriber of this PrimaryInsurance.

        HCFA/1500 individual relationship code

        :return: The patient_relationship_to_subscriber of this PrimaryInsurance.
        :rtype: str
        """
        return self._patient_relationship_to_subscriber

    @patient_relationship_to_subscriber.setter
    def patient_relationship_to_subscriber(self, patient_relationship_to_subscriber):
        """Sets the patient_relationship_to_subscriber of this PrimaryInsurance.

        HCFA/1500 individual relationship code

        :param patient_relationship_to_subscriber: The patient_relationship_to_subscriber of this PrimaryInsurance.
        :type patient_relationship_to_subscriber: str
        """
        allowed_values = ["", "01", "04", "05", "07", "10", "15", "17", "19", "20", "21", "22", "23", "24", "29", "32", "33", "36", "39", "40", "41", "43", "53", "76", "G8"]  # noqa: E501
        if patient_relationship_to_subscriber not in allowed_values:
            raise ValueError(
                "Invalid value for `patient_relationship_to_subscriber` ({0}), must be one of {1}"
                .format(patient_relationship_to_subscriber, allowed_values)
            )

        self._patient_relationship_to_subscriber = patient_relationship_to_subscriber

    @property
    def photo_back(self):
        """Gets the photo_back of this PrimaryInsurance.

        Photo of back of insurance card

        :return: The photo_back of this PrimaryInsurance.
        :rtype: str
        """
        return self._photo_back

    @photo_back.setter
    def photo_back(self, photo_back):
        """Sets the photo_back of this PrimaryInsurance.

        Photo of back of insurance card

        :param photo_back: The photo_back of this PrimaryInsurance.
        :type photo_back: str
        """

        self._photo_back = photo_back

    @property
    def photo_front(self):
        """Gets the photo_front of this PrimaryInsurance.

        Photo of front of insurance card

        :return: The photo_front of this PrimaryInsurance.
        :rtype: str
        """
        return self._photo_front

    @photo_front.setter
    def photo_front(self, photo_front):
        """Sets the photo_front of this PrimaryInsurance.

        Photo of front of insurance card

        :param photo_front: The photo_front of this PrimaryInsurance.
        :type photo_front: str
        """

        self._photo_front = photo_front

    @property
    def subscriber_address(self):
        """Gets the subscriber_address of this PrimaryInsurance.

        

        :return: The subscriber_address of this PrimaryInsurance.
        :rtype: str
        """
        return self._subscriber_address

    @subscriber_address.setter
    def subscriber_address(self, subscriber_address):
        """Sets the subscriber_address of this PrimaryInsurance.

        

        :param subscriber_address: The subscriber_address of this PrimaryInsurance.
        :type subscriber_address: str
        """

        self._subscriber_address = subscriber_address

    @property
    def subscriber_city(self):
        """Gets the subscriber_city of this PrimaryInsurance.

        

        :return: The subscriber_city of this PrimaryInsurance.
        :rtype: str
        """
        return self._subscriber_city

    @subscriber_city.setter
    def subscriber_city(self, subscriber_city):
        """Sets the subscriber_city of this PrimaryInsurance.

        

        :param subscriber_city: The subscriber_city of this PrimaryInsurance.
        :type subscriber_city: str
        """

        self._subscriber_city = subscriber_city

    @property
    def subscriber_country(self):
        """Gets the subscriber_country of this PrimaryInsurance.

        Two-letter country code

        :return: The subscriber_country of this PrimaryInsurance.
        :rtype: str
        """
        return self._subscriber_country

    @subscriber_country.setter
    def subscriber_country(self, subscriber_country):
        """Sets the subscriber_country of this PrimaryInsurance.

        Two-letter country code

        :param subscriber_country: The subscriber_country of this PrimaryInsurance.
        :type subscriber_country: str
        """
        allowed_values = ["", "AF", "AX", "AL", "DZ", "AS", "AD", "AO", "AI", "AQ", "AG", "AR", "AM", "AW", "AU", "AT", "AZ", "BS", "BH", "BD", "BB", "BY", "BE", "BZ", "BJ", "BM", "BT", "BO", "BQ", "BA", "BW", "BV", "BR", "IO", "BN", "BG", "BF", "BI", "KH", "CM", "CA", "CV", "KY", "CF", "TD", "CL", "CN", "CX", "CC", "CO", "KM", "CG", "CD", "CK", "CR", "CI", "HR", "CU", "CW", "CY", "CZ", "CYM", "DK", "DJ", "DM", "DO", "EC", "EG", "SV", "GQ", "ER", "EE", "ET", "FK", "FO", "FJ", "FI", "FR", "GF", "PF", "TF", "GA", "GM", "GE", "DE", "GH", "GI", "GR", "GL", "GD", "GP", "GU", "GT", "GG", "GN", "GW", "GY", "HT", "HM", "VA", "HN", "HK", "HU", "IS", "IN", "ID", "IR", "IQ", "IE", "IM", "IL", "IT", "JM", "JP", "JE", "JO", "KZ", "KE", "KI", "KP", "KR", "XK", "KW", "KG", "LA", "LV", "LB", "LS", "LR", "LY", "LI", "LT", "LU", "MO", "MK", "MG", "MW", "MY", "MV", "ML", "MT", "MH", "MQ", "MR", "MU", "YT", "MX", "FM", "MD", "MC", "MN", "ME", "MS", "MA", "MZ", "MM", "NA", "NR", "NP", "NL", "NC", "NZ", "NI", "NE", "NG", "NU", "NF", "MP", "false", "OM", "PK", "PW", "PS", "PA", "PG", "PY", "PE", "PH", "PN", "PL", "PT", "PR", "QA", "RE", "RO", "RU", "RW", "BL", "SH", "KN", "LC", "MF", "PM", "VC", "WS", "SM", "ST", "SA", "SN", "RS", "SC", "SL", "SG", "SX", "SK", "SI", "SB", "SO", "ZA", "GS", "SS", "ES", "LK", "SD", "SR", "SJ", "SZ", "SE", "CH", "SY", "TW", "TJ", "TZ", "TH", "TL", "TG", "TK", "TO", "TT", "TN", "TR", "TM", "TC", "TV", "UG", "UA", "AE", "GB", "US", "UM", "UY", "UZ", "VU", "VE", "VN", "VG", "VI", "WF", "EH", "YE", "ZM", "ZW"]  # noqa: E501
        if subscriber_country not in allowed_values:
            raise ValueError(
                "Invalid value for `subscriber_country` ({0}), must be one of {1}"
                .format(subscriber_country, allowed_values)
            )

        self._subscriber_country = subscriber_country

    @property
    def subscriber_date_of_birth(self):
        """Gets the subscriber_date_of_birth of this PrimaryInsurance.

        

        :return: The subscriber_date_of_birth of this PrimaryInsurance.
        :rtype: str
        """
        return self._subscriber_date_of_birth

    @subscriber_date_of_birth.setter
    def subscriber_date_of_birth(self, subscriber_date_of_birth):
        """Sets the subscriber_date_of_birth of this PrimaryInsurance.

        

        :param subscriber_date_of_birth: The subscriber_date_of_birth of this PrimaryInsurance.
        :type subscriber_date_of_birth: str
        """

        self._subscriber_date_of_birth = subscriber_date_of_birth

    @property
    def subscriber_first_name(self):
        """Gets the subscriber_first_name of this PrimaryInsurance.

        

        :return: The subscriber_first_name of this PrimaryInsurance.
        :rtype: str
        """
        return self._subscriber_first_name

    @subscriber_first_name.setter
    def subscriber_first_name(self, subscriber_first_name):
        """Sets the subscriber_first_name of this PrimaryInsurance.

        

        :param subscriber_first_name: The subscriber_first_name of this PrimaryInsurance.
        :type subscriber_first_name: str
        """

        self._subscriber_first_name = subscriber_first_name

    @property
    def subscriber_gender(self):
        """Gets the subscriber_gender of this PrimaryInsurance.

        One of `\"Male\"` or `\"Female\"`

        :return: The subscriber_gender of this PrimaryInsurance.
        :rtype: str
        """
        return self._subscriber_gender

    @subscriber_gender.setter
    def subscriber_gender(self, subscriber_gender):
        """Sets the subscriber_gender of this PrimaryInsurance.

        One of `\"Male\"` or `\"Female\"`

        :param subscriber_gender: The subscriber_gender of this PrimaryInsurance.
        :type subscriber_gender: str
        """
        allowed_values = ["", "Male", "Female", "Other", "UNK", "ASKU"]  # noqa: E501
        if subscriber_gender not in allowed_values:
            raise ValueError(
                "Invalid value for `subscriber_gender` ({0}), must be one of {1}"
                .format(subscriber_gender, allowed_values)
            )

        self._subscriber_gender = subscriber_gender

    @property
    def subscriber_last_name(self):
        """Gets the subscriber_last_name of this PrimaryInsurance.

        

        :return: The subscriber_last_name of this PrimaryInsurance.
        :rtype: str
        """
        return self._subscriber_last_name

    @subscriber_last_name.setter
    def subscriber_last_name(self, subscriber_last_name):
        """Sets the subscriber_last_name of this PrimaryInsurance.

        

        :param subscriber_last_name: The subscriber_last_name of this PrimaryInsurance.
        :type subscriber_last_name: str
        """

        self._subscriber_last_name = subscriber_last_name

    @property
    def subscriber_middle_name(self):
        """Gets the subscriber_middle_name of this PrimaryInsurance.

        

        :return: The subscriber_middle_name of this PrimaryInsurance.
        :rtype: str
        """
        return self._subscriber_middle_name

    @subscriber_middle_name.setter
    def subscriber_middle_name(self, subscriber_middle_name):
        """Sets the subscriber_middle_name of this PrimaryInsurance.

        

        :param subscriber_middle_name: The subscriber_middle_name of this PrimaryInsurance.
        :type subscriber_middle_name: str
        """

        self._subscriber_middle_name = subscriber_middle_name

    @property
    def subscriber_social_security(self):
        """Gets the subscriber_social_security of this PrimaryInsurance.

        

        :return: The subscriber_social_security of this PrimaryInsurance.
        :rtype: str
        """
        return self._subscriber_social_security

    @subscriber_social_security.setter
    def subscriber_social_security(self, subscriber_social_security):
        """Sets the subscriber_social_security of this PrimaryInsurance.

        

        :param subscriber_social_security: The subscriber_social_security of this PrimaryInsurance.
        :type subscriber_social_security: str
        """

        self._subscriber_social_security = subscriber_social_security

    @property
    def subscriber_state(self):
        """Gets the subscriber_state of this PrimaryInsurance.

        Two-letter state code

        :return: The subscriber_state of this PrimaryInsurance.
        :rtype: str
        """
        return self._subscriber_state

    @subscriber_state.setter
    def subscriber_state(self, subscriber_state):
        """Sets the subscriber_state of this PrimaryInsurance.

        Two-letter state code

        :param subscriber_state: The subscriber_state of this PrimaryInsurance.
        :type subscriber_state: str
        """
        allowed_values = ["AL", "AK", "AS", "AZ", "AR", "AA", "AE", "AP", "CA", "CO", "CT", "DE", "DC", "FL", "GA", "GU", "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD", "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ", "NM", "NY", "NC", "ND", "MP", "OH", "OK", "OR", "PA", "PR", "RI", "SC", "SD", "TN", "TX", "UT", "VT", "VI", "VA", "WA", "WV", "WI", "WY"]  # noqa: E501
        if subscriber_state not in allowed_values:
            raise ValueError(
                "Invalid value for `subscriber_state` ({0}), must be one of {1}"
                .format(subscriber_state, allowed_values)
            )

        self._subscriber_state = subscriber_state

    @property
    def subscriber_suffix(self):
        """Gets the subscriber_suffix of this PrimaryInsurance.

        E.g. `\"II\"` or `\"III\"`

        :return: The subscriber_suffix of this PrimaryInsurance.
        :rtype: str
        """
        return self._subscriber_suffix

    @subscriber_suffix.setter
    def subscriber_suffix(self, subscriber_suffix):
        """Sets the subscriber_suffix of this PrimaryInsurance.

        E.g. `\"II\"` or `\"III\"`

        :param subscriber_suffix: The subscriber_suffix of this PrimaryInsurance.
        :type subscriber_suffix: str
        """

        self._subscriber_suffix = subscriber_suffix

    @property
    def subscriber_zip_code(self):
        """Gets the subscriber_zip_code of this PrimaryInsurance.

        

        :return: The subscriber_zip_code of this PrimaryInsurance.
        :rtype: str
        """
        return self._subscriber_zip_code

    @subscriber_zip_code.setter
    def subscriber_zip_code(self, subscriber_zip_code):
        """Sets the subscriber_zip_code of this PrimaryInsurance.

        

        :param subscriber_zip_code: The subscriber_zip_code of this PrimaryInsurance.
        :type subscriber_zip_code: str
        """

        self._subscriber_zip_code = subscriber_zip_code
