# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.ssl_certificate_request_validation import SslCertificateRequestValidation
from openapi_server.models.ssl_certificate_type import SslCertificateType
from openapi_server.models.ssl_certificate_validation_level import SslCertificateValidationLevel
from openapi_server.models.ssl_certificate_vendor import SslCertificateVendor
from openapi_server.models.ssl_subject_alt_name import SslSubjectAltName
from openapi_server import util


class SslCertificateRequestDetail(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, certificate_type: SslCertificateType=None, common_name: str=None, id: int=None, order_code: str=None, subject_alt_names: List[SslSubjectAltName]=None, validation_level: SslCertificateValidationLevel=None, validations: List[SslCertificateRequestValidation]=None, vendor: SslCertificateVendor=None):
        """SslCertificateRequestDetail - a model defined in OpenAPI

        :param certificate_type: The certificate_type of this SslCertificateRequestDetail.
        :param common_name: The common_name of this SslCertificateRequestDetail.
        :param id: The id of this SslCertificateRequestDetail.
        :param order_code: The order_code of this SslCertificateRequestDetail.
        :param subject_alt_names: The subject_alt_names of this SslCertificateRequestDetail.
        :param validation_level: The validation_level of this SslCertificateRequestDetail.
        :param validations: The validations of this SslCertificateRequestDetail.
        :param vendor: The vendor of this SslCertificateRequestDetail.
        """
        self.openapi_types = {
            'certificate_type': SslCertificateType,
            'common_name': str,
            'id': int,
            'order_code': str,
            'subject_alt_names': List[SslSubjectAltName],
            'validation_level': SslCertificateValidationLevel,
            'validations': List[SslCertificateRequestValidation],
            'vendor': SslCertificateVendor
        }

        self.attribute_map = {
            'certificate_type': 'certificate_type',
            'common_name': 'common_name',
            'id': 'id',
            'order_code': 'order_code',
            'subject_alt_names': 'subject_alt_names',
            'validation_level': 'validation_level',
            'validations': 'validations',
            'vendor': 'vendor'
        }

        self._certificate_type = certificate_type
        self._common_name = common_name
        self._id = id
        self._order_code = order_code
        self._subject_alt_names = subject_alt_names
        self._validation_level = validation_level
        self._validations = validations
        self._vendor = vendor

    @classmethod
    def from_dict(cls, dikt: dict) -> 'SslCertificateRequestDetail':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The SslCertificateRequestDetail of this SslCertificateRequestDetail.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def certificate_type(self):
        """Gets the certificate_type of this SslCertificateRequestDetail.


        :return: The certificate_type of this SslCertificateRequestDetail.
        :rtype: SslCertificateType
        """
        return self._certificate_type

    @certificate_type.setter
    def certificate_type(self, certificate_type):
        """Sets the certificate_type of this SslCertificateRequestDetail.


        :param certificate_type: The certificate_type of this SslCertificateRequestDetail.
        :type certificate_type: SslCertificateType
        """

        self._certificate_type = certificate_type

    @property
    def common_name(self):
        """Gets the common_name of this SslCertificateRequestDetail.

        The common name of the certificate request.

        :return: The common_name of this SslCertificateRequestDetail.
        :rtype: str
        """
        return self._common_name

    @common_name.setter
    def common_name(self, common_name):
        """Sets the common_name of this SslCertificateRequestDetail.

        The common name of the certificate request.

        :param common_name: The common_name of this SslCertificateRequestDetail.
        :type common_name: str
        """

        self._common_name = common_name

    @property
    def id(self):
        """Gets the id of this SslCertificateRequestDetail.

        The id of the certificate request.

        :return: The id of this SslCertificateRequestDetail.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this SslCertificateRequestDetail.

        The id of the certificate request.

        :param id: The id of this SslCertificateRequestDetail.
        :type id: int
        """

        self._id = id

    @property
    def order_code(self):
        """Gets the order_code of this SslCertificateRequestDetail.

        The order code of the certificate request.

        :return: The order_code of this SslCertificateRequestDetail.
        :rtype: str
        """
        return self._order_code

    @order_code.setter
    def order_code(self, order_code):
        """Sets the order_code of this SslCertificateRequestDetail.

        The order code of the certificate request.

        :param order_code: The order_code of this SslCertificateRequestDetail.
        :type order_code: str
        """

        self._order_code = order_code

    @property
    def subject_alt_names(self):
        """Gets the subject_alt_names of this SslCertificateRequestDetail.

        The list of all supported domains in the certificate.

        :return: The subject_alt_names of this SslCertificateRequestDetail.
        :rtype: List[SslSubjectAltName]
        """
        return self._subject_alt_names

    @subject_alt_names.setter
    def subject_alt_names(self, subject_alt_names):
        """Sets the subject_alt_names of this SslCertificateRequestDetail.

        The list of all supported domains in the certificate.

        :param subject_alt_names: The subject_alt_names of this SslCertificateRequestDetail.
        :type subject_alt_names: List[SslSubjectAltName]
        """

        self._subject_alt_names = subject_alt_names

    @property
    def validation_level(self):
        """Gets the validation_level of this SslCertificateRequestDetail.


        :return: The validation_level of this SslCertificateRequestDetail.
        :rtype: SslCertificateValidationLevel
        """
        return self._validation_level

    @validation_level.setter
    def validation_level(self, validation_level):
        """Sets the validation_level of this SslCertificateRequestDetail.


        :param validation_level: The validation_level of this SslCertificateRequestDetail.
        :type validation_level: SslCertificateValidationLevel
        """

        self._validation_level = validation_level

    @property
    def validations(self):
        """Gets the validations of this SslCertificateRequestDetail.

        The list of dns names to be validated with the information related to domain verification.

        :return: The validations of this SslCertificateRequestDetail.
        :rtype: List[SslCertificateRequestValidation]
        """
        return self._validations

    @validations.setter
    def validations(self, validations):
        """Sets the validations of this SslCertificateRequestDetail.

        The list of dns names to be validated with the information related to domain verification.

        :param validations: The validations of this SslCertificateRequestDetail.
        :type validations: List[SslCertificateRequestValidation]
        """

        self._validations = validations

    @property
    def vendor(self):
        """Gets the vendor of this SslCertificateRequestDetail.


        :return: The vendor of this SslCertificateRequestDetail.
        :rtype: SslCertificateVendor
        """
        return self._vendor

    @vendor.setter
    def vendor(self, vendor):
        """Sets the vendor of this SslCertificateRequestDetail.


        :param vendor: The vendor of this SslCertificateRequestDetail.
        :type vendor: SslCertificateVendor
        """

        self._vendor = vendor
