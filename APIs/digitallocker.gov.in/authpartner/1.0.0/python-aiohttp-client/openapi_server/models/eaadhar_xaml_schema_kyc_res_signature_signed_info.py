# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.eaadhar_xaml_schema_kyc_res_signature_signed_info_canonicalization_method import EaadharXamlSchemaKycResSignatureSignedInfoCanonicalizationMethod
from openapi_server.models.eaadhar_xaml_schema_kyc_res_signature_signed_info_reference import EaadharXamlSchemaKycResSignatureSignedInfoReference
from openapi_server import util


class EaadharXamlSchemaKycResSignatureSignedInfo(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, canonicalization_method: EaadharXamlSchemaKycResSignatureSignedInfoCanonicalizationMethod=None, reference: EaadharXamlSchemaKycResSignatureSignedInfoReference=None, signature_method: EaadharXamlSchemaKycResSignatureSignedInfoCanonicalizationMethod=None):
        """EaadharXamlSchemaKycResSignatureSignedInfo - a model defined in OpenAPI

        :param canonicalization_method: The canonicalization_method of this EaadharXamlSchemaKycResSignatureSignedInfo.
        :param reference: The reference of this EaadharXamlSchemaKycResSignatureSignedInfo.
        :param signature_method: The signature_method of this EaadharXamlSchemaKycResSignatureSignedInfo.
        """
        self.openapi_types = {
            'canonicalization_method': EaadharXamlSchemaKycResSignatureSignedInfoCanonicalizationMethod,
            'reference': EaadharXamlSchemaKycResSignatureSignedInfoReference,
            'signature_method': EaadharXamlSchemaKycResSignatureSignedInfoCanonicalizationMethod
        }

        self.attribute_map = {
            'canonicalization_method': 'CanonicalizationMethod',
            'reference': 'Reference',
            'signature_method': 'SignatureMethod'
        }

        self._canonicalization_method = canonicalization_method
        self._reference = reference
        self._signature_method = signature_method

    @classmethod
    def from_dict(cls, dikt: dict) -> 'EaadharXamlSchemaKycResSignatureSignedInfo':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The EaadharXamlSchema_KycRes_Signature_SignedInfo of this EaadharXamlSchemaKycResSignatureSignedInfo.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def canonicalization_method(self):
        """Gets the canonicalization_method of this EaadharXamlSchemaKycResSignatureSignedInfo.


        :return: The canonicalization_method of this EaadharXamlSchemaKycResSignatureSignedInfo.
        :rtype: EaadharXamlSchemaKycResSignatureSignedInfoCanonicalizationMethod
        """
        return self._canonicalization_method

    @canonicalization_method.setter
    def canonicalization_method(self, canonicalization_method):
        """Sets the canonicalization_method of this EaadharXamlSchemaKycResSignatureSignedInfo.


        :param canonicalization_method: The canonicalization_method of this EaadharXamlSchemaKycResSignatureSignedInfo.
        :type canonicalization_method: EaadharXamlSchemaKycResSignatureSignedInfoCanonicalizationMethod
        """
        if canonicalization_method is None:
            raise ValueError("Invalid value for `canonicalization_method`, must not be `None`")

        self._canonicalization_method = canonicalization_method

    @property
    def reference(self):
        """Gets the reference of this EaadharXamlSchemaKycResSignatureSignedInfo.


        :return: The reference of this EaadharXamlSchemaKycResSignatureSignedInfo.
        :rtype: EaadharXamlSchemaKycResSignatureSignedInfoReference
        """
        return self._reference

    @reference.setter
    def reference(self, reference):
        """Sets the reference of this EaadharXamlSchemaKycResSignatureSignedInfo.


        :param reference: The reference of this EaadharXamlSchemaKycResSignatureSignedInfo.
        :type reference: EaadharXamlSchemaKycResSignatureSignedInfoReference
        """
        if reference is None:
            raise ValueError("Invalid value for `reference`, must not be `None`")

        self._reference = reference

    @property
    def signature_method(self):
        """Gets the signature_method of this EaadharXamlSchemaKycResSignatureSignedInfo.


        :return: The signature_method of this EaadharXamlSchemaKycResSignatureSignedInfo.
        :rtype: EaadharXamlSchemaKycResSignatureSignedInfoCanonicalizationMethod
        """
        return self._signature_method

    @signature_method.setter
    def signature_method(self, signature_method):
        """Sets the signature_method of this EaadharXamlSchemaKycResSignatureSignedInfo.


        :param signature_method: The signature_method of this EaadharXamlSchemaKycResSignatureSignedInfo.
        :type signature_method: EaadharXamlSchemaKycResSignatureSignedInfoCanonicalizationMethod
        """
        if signature_method is None:
            raise ValueError("Invalid value for `signature_method`, must not be `None`")

        self._signature_method = signature_method
