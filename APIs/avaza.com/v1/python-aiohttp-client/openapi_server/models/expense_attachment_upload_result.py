# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.file_attachment_details import FileAttachmentDetails
from openapi_server import util


class ExpenseAttachmentUploadResult(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, file_attachments: List[FileAttachmentDetails]=None):
        """ExpenseAttachmentUploadResult - a model defined in OpenAPI

        :param file_attachments: The file_attachments of this ExpenseAttachmentUploadResult.
        """
        self.openapi_types = {
            'file_attachments': List[FileAttachmentDetails]
        }

        self.attribute_map = {
            'file_attachments': 'FileAttachments'
        }

        self._file_attachments = file_attachments

    @classmethod
    def from_dict(cls, dikt: dict) -> 'ExpenseAttachmentUploadResult':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The ExpenseAttachmentUploadResult of this ExpenseAttachmentUploadResult.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def file_attachments(self):
        """Gets the file_attachments of this ExpenseAttachmentUploadResult.


        :return: The file_attachments of this ExpenseAttachmentUploadResult.
        :rtype: List[FileAttachmentDetails]
        """
        return self._file_attachments

    @file_attachments.setter
    def file_attachments(self, file_attachments):
        """Sets the file_attachments of this ExpenseAttachmentUploadResult.


        :param file_attachments: The file_attachments of this ExpenseAttachmentUploadResult.
        :type file_attachments: List[FileAttachmentDetails]
        """

        self._file_attachments = file_attachments
