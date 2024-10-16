# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class ProvisioningProfileFile(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, file_id: str=None, file_name: str=None, target_bundle_identifier: str=None, upload_id: str=None):
        """ProvisioningProfileFile - a model defined in OpenAPI

        :param file_id: The file_id of this ProvisioningProfileFile.
        :param file_name: The file_name of this ProvisioningProfileFile.
        :param target_bundle_identifier: The target_bundle_identifier of this ProvisioningProfileFile.
        :param upload_id: The upload_id of this ProvisioningProfileFile.
        """
        self.openapi_types = {
            'file_id': str,
            'file_name': str,
            'target_bundle_identifier': str,
            'upload_id': str
        }

        self.attribute_map = {
            'file_id': 'fileId',
            'file_name': 'fileName',
            'target_bundle_identifier': 'targetBundleIdentifier',
            'upload_id': 'uploadId'
        }

        self._file_id = file_id
        self._file_name = file_name
        self._target_bundle_identifier = target_bundle_identifier
        self._upload_id = upload_id

    @classmethod
    def from_dict(cls, dikt: dict) -> 'ProvisioningProfileFile':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The ProvisioningProfileFile of this ProvisioningProfileFile.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def file_id(self):
        """Gets the file_id of this ProvisioningProfileFile.

        File id from secure file storage

        :return: The file_id of this ProvisioningProfileFile.
        :rtype: str
        """
        return self._file_id

    @file_id.setter
    def file_id(self, file_id):
        """Sets the file_id of this ProvisioningProfileFile.

        File id from secure file storage

        :param file_id: The file_id of this ProvisioningProfileFile.
        :type file_id: str
        """

        self._file_id = file_id

    @property
    def file_name(self):
        """Gets the file_name of this ProvisioningProfileFile.

        Name of uploaded provisioning profile

        :return: The file_name of this ProvisioningProfileFile.
        :rtype: str
        """
        return self._file_name

    @file_name.setter
    def file_name(self, file_name):
        """Sets the file_name of this ProvisioningProfileFile.

        Name of uploaded provisioning profile

        :param file_name: The file_name of this ProvisioningProfileFile.
        :type file_name: str
        """

        self._file_name = file_name

    @property
    def target_bundle_identifier(self):
        """Gets the target_bundle_identifier of this ProvisioningProfileFile.

        Target the provisioning profile is used to sign

        :return: The target_bundle_identifier of this ProvisioningProfileFile.
        :rtype: str
        """
        return self._target_bundle_identifier

    @target_bundle_identifier.setter
    def target_bundle_identifier(self, target_bundle_identifier):
        """Sets the target_bundle_identifier of this ProvisioningProfileFile.

        Target the provisioning profile is used to sign

        :param target_bundle_identifier: The target_bundle_identifier of this ProvisioningProfileFile.
        :type target_bundle_identifier: str
        """

        self._target_bundle_identifier = target_bundle_identifier

    @property
    def upload_id(self):
        """Gets the upload_id of this ProvisioningProfileFile.

        Upload id to App Center File Upload Store

        :return: The upload_id of this ProvisioningProfileFile.
        :rtype: str
        """
        return self._upload_id

    @upload_id.setter
    def upload_id(self, upload_id):
        """Sets the upload_id of this ProvisioningProfileFile.

        Upload id to App Center File Upload Store

        :param upload_id: The upload_id of this ProvisioningProfileFile.
        :type upload_id: str
        """

        self._upload_id = upload_id
