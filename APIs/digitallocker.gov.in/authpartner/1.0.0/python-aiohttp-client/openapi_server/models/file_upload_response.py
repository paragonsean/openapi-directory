# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.file_upload_response_details import FileUploadResponseDetails
from openapi_server import util


class FileUploadResponse(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, details: FileUploadResponseDetails=None):
        """FileUploadResponse - a model defined in OpenAPI

        :param details: The details of this FileUploadResponse.
        """
        self.openapi_types = {
            'details': FileUploadResponseDetails
        }

        self.attribute_map = {
            'details': 'details'
        }

        self._details = details

    @classmethod
    def from_dict(cls, dikt: dict) -> 'FileUploadResponse':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The FileUploadResponse of this FileUploadResponse.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def details(self):
        """Gets the details of this FileUploadResponse.


        :return: The details of this FileUploadResponse.
        :rtype: FileUploadResponseDetails
        """
        return self._details

    @details.setter
    def details(self, details):
        """Sets the details of this FileUploadResponse.


        :param details: The details of this FileUploadResponse.
        :type details: FileUploadResponseDetails
        """

        self._details = details
