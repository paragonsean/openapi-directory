# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.meta import Meta
from openapi_server import util


class PatientLinkReferenceResultLink(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, authentication_type: str=None, meta: Meta=None, reference_number: str=None):
        """PatientLinkReferenceResultLink - a model defined in OpenAPI

        :param authentication_type: The authentication_type of this PatientLinkReferenceResultLink.
        :param meta: The meta of this PatientLinkReferenceResultLink.
        :param reference_number: The reference_number of this PatientLinkReferenceResultLink.
        """
        self.openapi_types = {
            'authentication_type': str,
            'meta': Meta,
            'reference_number': str
        }

        self.attribute_map = {
            'authentication_type': 'authenticationType',
            'meta': 'meta',
            'reference_number': 'referenceNumber'
        }

        self._authentication_type = authentication_type
        self._meta = meta
        self._reference_number = reference_number

    @classmethod
    def from_dict(cls, dikt: dict) -> 'PatientLinkReferenceResultLink':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The PatientLinkReferenceResult_link of this PatientLinkReferenceResultLink.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def authentication_type(self):
        """Gets the authentication_type of this PatientLinkReferenceResultLink.


        :return: The authentication_type of this PatientLinkReferenceResultLink.
        :rtype: str
        """
        return self._authentication_type

    @authentication_type.setter
    def authentication_type(self, authentication_type):
        """Sets the authentication_type of this PatientLinkReferenceResultLink.


        :param authentication_type: The authentication_type of this PatientLinkReferenceResultLink.
        :type authentication_type: str
        """
        allowed_values = ["DIRECT", "MEDIATED"]  # noqa: E501
        if authentication_type not in allowed_values:
            raise ValueError(
                "Invalid value for `authentication_type` ({0}), must be one of {1}"
                .format(authentication_type, allowed_values)
            )

        self._authentication_type = authentication_type

    @property
    def meta(self):
        """Gets the meta of this PatientLinkReferenceResultLink.


        :return: The meta of this PatientLinkReferenceResultLink.
        :rtype: Meta
        """
        return self._meta

    @meta.setter
    def meta(self, meta):
        """Sets the meta of this PatientLinkReferenceResultLink.


        :param meta: The meta of this PatientLinkReferenceResultLink.
        :type meta: Meta
        """

        self._meta = meta

    @property
    def reference_number(self):
        """Gets the reference_number of this PatientLinkReferenceResultLink.


        :return: The reference_number of this PatientLinkReferenceResultLink.
        :rtype: str
        """
        return self._reference_number

    @reference_number.setter
    def reference_number(self, reference_number):
        """Sets the reference_number of this PatientLinkReferenceResultLink.


        :param reference_number: The reference_number of this PatientLinkReferenceResultLink.
        :type reference_number: str
        """
        if reference_number is None:
            raise ValueError("Invalid value for `reference_number`, must not be `None`")

        self._reference_number = reference_number
