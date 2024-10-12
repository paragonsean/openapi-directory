# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class AsymmetricEncryptedSecret(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, encryption_algorithm: str=None, encryption_cert_thumbprint: str=None, value: str=None):
        """AsymmetricEncryptedSecret - a model defined in OpenAPI

        :param encryption_algorithm: The encryption_algorithm of this AsymmetricEncryptedSecret.
        :param encryption_cert_thumbprint: The encryption_cert_thumbprint of this AsymmetricEncryptedSecret.
        :param value: The value of this AsymmetricEncryptedSecret.
        """
        self.openapi_types = {
            'encryption_algorithm': str,
            'encryption_cert_thumbprint': str,
            'value': str
        }

        self.attribute_map = {
            'encryption_algorithm': 'encryptionAlgorithm',
            'encryption_cert_thumbprint': 'encryptionCertThumbprint',
            'value': 'value'
        }

        self._encryption_algorithm = encryption_algorithm
        self._encryption_cert_thumbprint = encryption_cert_thumbprint
        self._value = value

    @classmethod
    def from_dict(cls, dikt: dict) -> 'AsymmetricEncryptedSecret':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The AsymmetricEncryptedSecret of this AsymmetricEncryptedSecret.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def encryption_algorithm(self):
        """Gets the encryption_algorithm of this AsymmetricEncryptedSecret.

        The algorithm used to encrypt \"Value\".

        :return: The encryption_algorithm of this AsymmetricEncryptedSecret.
        :rtype: str
        """
        return self._encryption_algorithm

    @encryption_algorithm.setter
    def encryption_algorithm(self, encryption_algorithm):
        """Sets the encryption_algorithm of this AsymmetricEncryptedSecret.

        The algorithm used to encrypt \"Value\".

        :param encryption_algorithm: The encryption_algorithm of this AsymmetricEncryptedSecret.
        :type encryption_algorithm: str
        """
        allowed_values = ["None", "AES256", "RSAES_PKCS1_v_1_5"]  # noqa: E501
        if encryption_algorithm not in allowed_values:
            raise ValueError(
                "Invalid value for `encryption_algorithm` ({0}), must be one of {1}"
                .format(encryption_algorithm, allowed_values)
            )

        self._encryption_algorithm = encryption_algorithm

    @property
    def encryption_cert_thumbprint(self):
        """Gets the encryption_cert_thumbprint of this AsymmetricEncryptedSecret.

        Thumbprint certificate that was used to encrypt \"Value\". If the value in unencrypted, it will be null.

        :return: The encryption_cert_thumbprint of this AsymmetricEncryptedSecret.
        :rtype: str
        """
        return self._encryption_cert_thumbprint

    @encryption_cert_thumbprint.setter
    def encryption_cert_thumbprint(self, encryption_cert_thumbprint):
        """Sets the encryption_cert_thumbprint of this AsymmetricEncryptedSecret.

        Thumbprint certificate that was used to encrypt \"Value\". If the value in unencrypted, it will be null.

        :param encryption_cert_thumbprint: The encryption_cert_thumbprint of this AsymmetricEncryptedSecret.
        :type encryption_cert_thumbprint: str
        """

        self._encryption_cert_thumbprint = encryption_cert_thumbprint

    @property
    def value(self):
        """Gets the value of this AsymmetricEncryptedSecret.

        The value of the secret.

        :return: The value of this AsymmetricEncryptedSecret.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this AsymmetricEncryptedSecret.

        The value of the secret.

        :param value: The value of this AsymmetricEncryptedSecret.
        :type value: str
        """
        if value is None:
            raise ValueError("Invalid value for `value`, must not be `None`")

        self._value = value
