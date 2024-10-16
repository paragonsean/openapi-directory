# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class AppleCertificateNonSecretDetails(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, certificate_validity_end_date: str=None, certificate_validity_start_date: str=None, display_name: str=None):
        """AppleCertificateNonSecretDetails - a model defined in OpenAPI

        :param certificate_validity_end_date: The certificate_validity_end_date of this AppleCertificateNonSecretDetails.
        :param certificate_validity_start_date: The certificate_validity_start_date of this AppleCertificateNonSecretDetails.
        :param display_name: The display_name of this AppleCertificateNonSecretDetails.
        """
        self.openapi_types = {
            'certificate_validity_end_date': str,
            'certificate_validity_start_date': str,
            'display_name': str
        }

        self.attribute_map = {
            'certificate_validity_end_date': 'certificateValidityEndDate',
            'certificate_validity_start_date': 'certificateValidityStartDate',
            'display_name': 'displayName'
        }

        self._certificate_validity_end_date = certificate_validity_end_date
        self._certificate_validity_start_date = certificate_validity_start_date
        self._display_name = display_name

    @classmethod
    def from_dict(cls, dikt: dict) -> 'AppleCertificateNonSecretDetails':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The AppleCertificateNonSecretDetails of this AppleCertificateNonSecretDetails.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def certificate_validity_end_date(self):
        """Gets the certificate_validity_end_date of this AppleCertificateNonSecretDetails.

        The date-time till which the certificate is valid

        :return: The certificate_validity_end_date of this AppleCertificateNonSecretDetails.
        :rtype: str
        """
        return self._certificate_validity_end_date

    @certificate_validity_end_date.setter
    def certificate_validity_end_date(self, certificate_validity_end_date):
        """Sets the certificate_validity_end_date of this AppleCertificateNonSecretDetails.

        The date-time till which the certificate is valid

        :param certificate_validity_end_date: The certificate_validity_end_date of this AppleCertificateNonSecretDetails.
        :type certificate_validity_end_date: str
        """
        if certificate_validity_end_date is None:
            raise ValueError("Invalid value for `certificate_validity_end_date`, must not be `None`")

        self._certificate_validity_end_date = certificate_validity_end_date

    @property
    def certificate_validity_start_date(self):
        """Gets the certificate_validity_start_date of this AppleCertificateNonSecretDetails.

        The date-time from which the certificate is valid

        :return: The certificate_validity_start_date of this AppleCertificateNonSecretDetails.
        :rtype: str
        """
        return self._certificate_validity_start_date

    @certificate_validity_start_date.setter
    def certificate_validity_start_date(self, certificate_validity_start_date):
        """Sets the certificate_validity_start_date of this AppleCertificateNonSecretDetails.

        The date-time from which the certificate is valid

        :param certificate_validity_start_date: The certificate_validity_start_date of this AppleCertificateNonSecretDetails.
        :type certificate_validity_start_date: str
        """
        if certificate_validity_start_date is None:
            raise ValueError("Invalid value for `certificate_validity_start_date`, must not be `None`")

        self._certificate_validity_start_date = certificate_validity_start_date

    @property
    def display_name(self):
        """Gets the display_name of this AppleCertificateNonSecretDetails.

        The display name (CN) of the certificate

        :return: The display_name of this AppleCertificateNonSecretDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this AppleCertificateNonSecretDetails.

        The display name (CN) of the certificate

        :param display_name: The display_name of this AppleCertificateNonSecretDetails.
        :type display_name: str
        """
        if display_name is None:
            raise ValueError("Invalid value for `display_name`, must not be `None`")

        self._display_name = display_name
