# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.eft_bank_dto import EFTBankDto
from openapi_server import util


class SupplierQueryDto(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, account_name: str=None, account_number: str=None, additional_emails: List[str]=None, address: List[str]=None, auth_code: str=None, bank: EFTBankDto=None, business_identifier_code: str=None, code: str=None, contact: str=None, e_ft_reference: str=None, email: str=None, fax: str=None, id: int=None, international_bank_account_number: str=None, mobile: str=None, name: str=None, our_code: str=None, owner_type_id: int=None, phone: str=None, postponed_accounting: bool=None, timestamp: str=None, vat_analysis_type_id: int=None, vat_reg: str=None, vat_type: int=None):
        """SupplierQueryDto - a model defined in OpenAPI

        :param account_name: The account_name of this SupplierQueryDto.
        :param account_number: The account_number of this SupplierQueryDto.
        :param additional_emails: The additional_emails of this SupplierQueryDto.
        :param address: The address of this SupplierQueryDto.
        :param auth_code: The auth_code of this SupplierQueryDto.
        :param bank: The bank of this SupplierQueryDto.
        :param business_identifier_code: The business_identifier_code of this SupplierQueryDto.
        :param code: The code of this SupplierQueryDto.
        :param contact: The contact of this SupplierQueryDto.
        :param e_ft_reference: The e_ft_reference of this SupplierQueryDto.
        :param email: The email of this SupplierQueryDto.
        :param fax: The fax of this SupplierQueryDto.
        :param id: The id of this SupplierQueryDto.
        :param international_bank_account_number: The international_bank_account_number of this SupplierQueryDto.
        :param mobile: The mobile of this SupplierQueryDto.
        :param name: The name of this SupplierQueryDto.
        :param our_code: The our_code of this SupplierQueryDto.
        :param owner_type_id: The owner_type_id of this SupplierQueryDto.
        :param phone: The phone of this SupplierQueryDto.
        :param postponed_accounting: The postponed_accounting of this SupplierQueryDto.
        :param timestamp: The timestamp of this SupplierQueryDto.
        :param vat_analysis_type_id: The vat_analysis_type_id of this SupplierQueryDto.
        :param vat_reg: The vat_reg of this SupplierQueryDto.
        :param vat_type: The vat_type of this SupplierQueryDto.
        """
        self.openapi_types = {
            'account_name': str,
            'account_number': str,
            'additional_emails': List[str],
            'address': List[str],
            'auth_code': str,
            'bank': EFTBankDto,
            'business_identifier_code': str,
            'code': str,
            'contact': str,
            'e_ft_reference': str,
            'email': str,
            'fax': str,
            'id': int,
            'international_bank_account_number': str,
            'mobile': str,
            'name': str,
            'our_code': str,
            'owner_type_id': int,
            'phone': str,
            'postponed_accounting': bool,
            'timestamp': str,
            'vat_analysis_type_id': int,
            'vat_reg': str,
            'vat_type': int
        }

        self.attribute_map = {
            'account_name': 'accountName',
            'account_number': 'accountNumber',
            'additional_emails': 'additionalEmails',
            'address': 'address',
            'auth_code': 'authCode',
            'bank': 'bank',
            'business_identifier_code': 'businessIdentifierCode',
            'code': 'code',
            'contact': 'contact',
            'e_ft_reference': 'eFTReference',
            'email': 'email',
            'fax': 'fax',
            'id': 'id',
            'international_bank_account_number': 'internationalBankAccountNumber',
            'mobile': 'mobile',
            'name': 'name',
            'our_code': 'ourCode',
            'owner_type_id': 'ownerTypeId',
            'phone': 'phone',
            'postponed_accounting': 'postponedAccounting',
            'timestamp': 'timestamp',
            'vat_analysis_type_id': 'vatAnalysisTypeId',
            'vat_reg': 'vatReg',
            'vat_type': 'vatType'
        }

        self._account_name = account_name
        self._account_number = account_number
        self._additional_emails = additional_emails
        self._address = address
        self._auth_code = auth_code
        self._bank = bank
        self._business_identifier_code = business_identifier_code
        self._code = code
        self._contact = contact
        self._e_ft_reference = e_ft_reference
        self._email = email
        self._fax = fax
        self._id = id
        self._international_bank_account_number = international_bank_account_number
        self._mobile = mobile
        self._name = name
        self._our_code = our_code
        self._owner_type_id = owner_type_id
        self._phone = phone
        self._postponed_accounting = postponed_accounting
        self._timestamp = timestamp
        self._vat_analysis_type_id = vat_analysis_type_id
        self._vat_reg = vat_reg
        self._vat_type = vat_type

    @classmethod
    def from_dict(cls, dikt: dict) -> 'SupplierQueryDto':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The SupplierQueryDto of this SupplierQueryDto.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def account_name(self):
        """Gets the account_name of this SupplierQueryDto.


        :return: The account_name of this SupplierQueryDto.
        :rtype: str
        """
        return self._account_name

    @account_name.setter
    def account_name(self, account_name):
        """Sets the account_name of this SupplierQueryDto.


        :param account_name: The account_name of this SupplierQueryDto.
        :type account_name: str
        """

        self._account_name = account_name

    @property
    def account_number(self):
        """Gets the account_number of this SupplierQueryDto.


        :return: The account_number of this SupplierQueryDto.
        :rtype: str
        """
        return self._account_number

    @account_number.setter
    def account_number(self, account_number):
        """Sets the account_number of this SupplierQueryDto.


        :param account_number: The account_number of this SupplierQueryDto.
        :type account_number: str
        """

        self._account_number = account_number

    @property
    def additional_emails(self):
        """Gets the additional_emails of this SupplierQueryDto.


        :return: The additional_emails of this SupplierQueryDto.
        :rtype: List[str]
        """
        return self._additional_emails

    @additional_emails.setter
    def additional_emails(self, additional_emails):
        """Sets the additional_emails of this SupplierQueryDto.


        :param additional_emails: The additional_emails of this SupplierQueryDto.
        :type additional_emails: List[str]
        """

        self._additional_emails = additional_emails

    @property
    def address(self):
        """Gets the address of this SupplierQueryDto.


        :return: The address of this SupplierQueryDto.
        :rtype: List[str]
        """
        return self._address

    @address.setter
    def address(self, address):
        """Sets the address of this SupplierQueryDto.


        :param address: The address of this SupplierQueryDto.
        :type address: List[str]
        """

        self._address = address

    @property
    def auth_code(self):
        """Gets the auth_code of this SupplierQueryDto.


        :return: The auth_code of this SupplierQueryDto.
        :rtype: str
        """
        return self._auth_code

    @auth_code.setter
    def auth_code(self, auth_code):
        """Sets the auth_code of this SupplierQueryDto.


        :param auth_code: The auth_code of this SupplierQueryDto.
        :type auth_code: str
        """

        self._auth_code = auth_code

    @property
    def bank(self):
        """Gets the bank of this SupplierQueryDto.


        :return: The bank of this SupplierQueryDto.
        :rtype: EFTBankDto
        """
        return self._bank

    @bank.setter
    def bank(self, bank):
        """Sets the bank of this SupplierQueryDto.


        :param bank: The bank of this SupplierQueryDto.
        :type bank: EFTBankDto
        """

        self._bank = bank

    @property
    def business_identifier_code(self):
        """Gets the business_identifier_code of this SupplierQueryDto.


        :return: The business_identifier_code of this SupplierQueryDto.
        :rtype: str
        """
        return self._business_identifier_code

    @business_identifier_code.setter
    def business_identifier_code(self, business_identifier_code):
        """Sets the business_identifier_code of this SupplierQueryDto.


        :param business_identifier_code: The business_identifier_code of this SupplierQueryDto.
        :type business_identifier_code: str
        """

        self._business_identifier_code = business_identifier_code

    @property
    def code(self):
        """Gets the code of this SupplierQueryDto.


        :return: The code of this SupplierQueryDto.
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this SupplierQueryDto.


        :param code: The code of this SupplierQueryDto.
        :type code: str
        """

        self._code = code

    @property
    def contact(self):
        """Gets the contact of this SupplierQueryDto.


        :return: The contact of this SupplierQueryDto.
        :rtype: str
        """
        return self._contact

    @contact.setter
    def contact(self, contact):
        """Sets the contact of this SupplierQueryDto.


        :param contact: The contact of this SupplierQueryDto.
        :type contact: str
        """

        self._contact = contact

    @property
    def e_ft_reference(self):
        """Gets the e_ft_reference of this SupplierQueryDto.


        :return: The e_ft_reference of this SupplierQueryDto.
        :rtype: str
        """
        return self._e_ft_reference

    @e_ft_reference.setter
    def e_ft_reference(self, e_ft_reference):
        """Sets the e_ft_reference of this SupplierQueryDto.


        :param e_ft_reference: The e_ft_reference of this SupplierQueryDto.
        :type e_ft_reference: str
        """

        self._e_ft_reference = e_ft_reference

    @property
    def email(self):
        """Gets the email of this SupplierQueryDto.


        :return: The email of this SupplierQueryDto.
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this SupplierQueryDto.


        :param email: The email of this SupplierQueryDto.
        :type email: str
        """

        self._email = email

    @property
    def fax(self):
        """Gets the fax of this SupplierQueryDto.


        :return: The fax of this SupplierQueryDto.
        :rtype: str
        """
        return self._fax

    @fax.setter
    def fax(self, fax):
        """Sets the fax of this SupplierQueryDto.


        :param fax: The fax of this SupplierQueryDto.
        :type fax: str
        """

        self._fax = fax

    @property
    def id(self):
        """Gets the id of this SupplierQueryDto.


        :return: The id of this SupplierQueryDto.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this SupplierQueryDto.


        :param id: The id of this SupplierQueryDto.
        :type id: int
        """

        self._id = id

    @property
    def international_bank_account_number(self):
        """Gets the international_bank_account_number of this SupplierQueryDto.


        :return: The international_bank_account_number of this SupplierQueryDto.
        :rtype: str
        """
        return self._international_bank_account_number

    @international_bank_account_number.setter
    def international_bank_account_number(self, international_bank_account_number):
        """Sets the international_bank_account_number of this SupplierQueryDto.


        :param international_bank_account_number: The international_bank_account_number of this SupplierQueryDto.
        :type international_bank_account_number: str
        """

        self._international_bank_account_number = international_bank_account_number

    @property
    def mobile(self):
        """Gets the mobile of this SupplierQueryDto.


        :return: The mobile of this SupplierQueryDto.
        :rtype: str
        """
        return self._mobile

    @mobile.setter
    def mobile(self, mobile):
        """Sets the mobile of this SupplierQueryDto.


        :param mobile: The mobile of this SupplierQueryDto.
        :type mobile: str
        """

        self._mobile = mobile

    @property
    def name(self):
        """Gets the name of this SupplierQueryDto.


        :return: The name of this SupplierQueryDto.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this SupplierQueryDto.


        :param name: The name of this SupplierQueryDto.
        :type name: str
        """

        self._name = name

    @property
    def our_code(self):
        """Gets the our_code of this SupplierQueryDto.


        :return: The our_code of this SupplierQueryDto.
        :rtype: str
        """
        return self._our_code

    @our_code.setter
    def our_code(self, our_code):
        """Sets the our_code of this SupplierQueryDto.


        :param our_code: The our_code of this SupplierQueryDto.
        :type our_code: str
        """

        self._our_code = our_code

    @property
    def owner_type_id(self):
        """Gets the owner_type_id of this SupplierQueryDto.


        :return: The owner_type_id of this SupplierQueryDto.
        :rtype: int
        """
        return self._owner_type_id

    @owner_type_id.setter
    def owner_type_id(self, owner_type_id):
        """Sets the owner_type_id of this SupplierQueryDto.


        :param owner_type_id: The owner_type_id of this SupplierQueryDto.
        :type owner_type_id: int
        """

        self._owner_type_id = owner_type_id

    @property
    def phone(self):
        """Gets the phone of this SupplierQueryDto.


        :return: The phone of this SupplierQueryDto.
        :rtype: str
        """
        return self._phone

    @phone.setter
    def phone(self, phone):
        """Sets the phone of this SupplierQueryDto.


        :param phone: The phone of this SupplierQueryDto.
        :type phone: str
        """

        self._phone = phone

    @property
    def postponed_accounting(self):
        """Gets the postponed_accounting of this SupplierQueryDto.


        :return: The postponed_accounting of this SupplierQueryDto.
        :rtype: bool
        """
        return self._postponed_accounting

    @postponed_accounting.setter
    def postponed_accounting(self, postponed_accounting):
        """Sets the postponed_accounting of this SupplierQueryDto.


        :param postponed_accounting: The postponed_accounting of this SupplierQueryDto.
        :type postponed_accounting: bool
        """

        self._postponed_accounting = postponed_accounting

    @property
    def timestamp(self):
        """Gets the timestamp of this SupplierQueryDto.


        :return: The timestamp of this SupplierQueryDto.
        :rtype: str
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """Sets the timestamp of this SupplierQueryDto.


        :param timestamp: The timestamp of this SupplierQueryDto.
        :type timestamp: str
        """

        self._timestamp = timestamp

    @property
    def vat_analysis_type_id(self):
        """Gets the vat_analysis_type_id of this SupplierQueryDto.


        :return: The vat_analysis_type_id of this SupplierQueryDto.
        :rtype: int
        """
        return self._vat_analysis_type_id

    @vat_analysis_type_id.setter
    def vat_analysis_type_id(self, vat_analysis_type_id):
        """Sets the vat_analysis_type_id of this SupplierQueryDto.


        :param vat_analysis_type_id: The vat_analysis_type_id of this SupplierQueryDto.
        :type vat_analysis_type_id: int
        """

        self._vat_analysis_type_id = vat_analysis_type_id

    @property
    def vat_reg(self):
        """Gets the vat_reg of this SupplierQueryDto.


        :return: The vat_reg of this SupplierQueryDto.
        :rtype: str
        """
        return self._vat_reg

    @vat_reg.setter
    def vat_reg(self, vat_reg):
        """Sets the vat_reg of this SupplierQueryDto.


        :param vat_reg: The vat_reg of this SupplierQueryDto.
        :type vat_reg: str
        """

        self._vat_reg = vat_reg

    @property
    def vat_type(self):
        """Gets the vat_type of this SupplierQueryDto.


        :return: The vat_type of this SupplierQueryDto.
        :rtype: int
        """
        return self._vat_type

    @vat_type.setter
    def vat_type(self, vat_type):
        """Sets the vat_type of this SupplierQueryDto.


        :param vat_type: The vat_type of this SupplierQueryDto.
        :type vat_type: int
        """

        self._vat_type = vat_type
