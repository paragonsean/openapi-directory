# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class CrashesListAttachments200ResponseInner(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, app_id: str=None, attachment_id: str=None, blob_location: str=None, content_type: str=None, crash_id: str=None, created_time: datetime=None, file_name: str=None, size: float=None):
        """CrashesListAttachments200ResponseInner - a model defined in OpenAPI

        :param app_id: The app_id of this CrashesListAttachments200ResponseInner.
        :param attachment_id: The attachment_id of this CrashesListAttachments200ResponseInner.
        :param blob_location: The blob_location of this CrashesListAttachments200ResponseInner.
        :param content_type: The content_type of this CrashesListAttachments200ResponseInner.
        :param crash_id: The crash_id of this CrashesListAttachments200ResponseInner.
        :param created_time: The created_time of this CrashesListAttachments200ResponseInner.
        :param file_name: The file_name of this CrashesListAttachments200ResponseInner.
        :param size: The size of this CrashesListAttachments200ResponseInner.
        """
        self.openapi_types = {
            'app_id': str,
            'attachment_id': str,
            'blob_location': str,
            'content_type': str,
            'crash_id': str,
            'created_time': datetime,
            'file_name': str,
            'size': float
        }

        self.attribute_map = {
            'app_id': 'app_id',
            'attachment_id': 'attachment_id',
            'blob_location': 'blob_location',
            'content_type': 'content_type',
            'crash_id': 'crash_id',
            'created_time': 'created_time',
            'file_name': 'file_name',
            'size': 'size'
        }

        self._app_id = app_id
        self._attachment_id = attachment_id
        self._blob_location = blob_location
        self._content_type = content_type
        self._crash_id = crash_id
        self._created_time = created_time
        self._file_name = file_name
        self._size = size

    @classmethod
    def from_dict(cls, dikt: dict) -> 'CrashesListAttachments200ResponseInner':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The crashes_listAttachments_200_response_inner of this CrashesListAttachments200ResponseInner.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def app_id(self):
        """Gets the app_id of this CrashesListAttachments200ResponseInner.


        :return: The app_id of this CrashesListAttachments200ResponseInner.
        :rtype: str
        """
        return self._app_id

    @app_id.setter
    def app_id(self, app_id):
        """Sets the app_id of this CrashesListAttachments200ResponseInner.


        :param app_id: The app_id of this CrashesListAttachments200ResponseInner.
        :type app_id: str
        """
        if app_id is None:
            raise ValueError("Invalid value for `app_id`, must not be `None`")

        self._app_id = app_id

    @property
    def attachment_id(self):
        """Gets the attachment_id of this CrashesListAttachments200ResponseInner.


        :return: The attachment_id of this CrashesListAttachments200ResponseInner.
        :rtype: str
        """
        return self._attachment_id

    @attachment_id.setter
    def attachment_id(self, attachment_id):
        """Sets the attachment_id of this CrashesListAttachments200ResponseInner.


        :param attachment_id: The attachment_id of this CrashesListAttachments200ResponseInner.
        :type attachment_id: str
        """
        if attachment_id is None:
            raise ValueError("Invalid value for `attachment_id`, must not be `None`")

        self._attachment_id = attachment_id

    @property
    def blob_location(self):
        """Gets the blob_location of this CrashesListAttachments200ResponseInner.


        :return: The blob_location of this CrashesListAttachments200ResponseInner.
        :rtype: str
        """
        return self._blob_location

    @blob_location.setter
    def blob_location(self, blob_location):
        """Sets the blob_location of this CrashesListAttachments200ResponseInner.


        :param blob_location: The blob_location of this CrashesListAttachments200ResponseInner.
        :type blob_location: str
        """
        if blob_location is None:
            raise ValueError("Invalid value for `blob_location`, must not be `None`")

        self._blob_location = blob_location

    @property
    def content_type(self):
        """Gets the content_type of this CrashesListAttachments200ResponseInner.


        :return: The content_type of this CrashesListAttachments200ResponseInner.
        :rtype: str
        """
        return self._content_type

    @content_type.setter
    def content_type(self, content_type):
        """Sets the content_type of this CrashesListAttachments200ResponseInner.


        :param content_type: The content_type of this CrashesListAttachments200ResponseInner.
        :type content_type: str
        """
        if content_type is None:
            raise ValueError("Invalid value for `content_type`, must not be `None`")

        self._content_type = content_type

    @property
    def crash_id(self):
        """Gets the crash_id of this CrashesListAttachments200ResponseInner.


        :return: The crash_id of this CrashesListAttachments200ResponseInner.
        :rtype: str
        """
        return self._crash_id

    @crash_id.setter
    def crash_id(self, crash_id):
        """Sets the crash_id of this CrashesListAttachments200ResponseInner.


        :param crash_id: The crash_id of this CrashesListAttachments200ResponseInner.
        :type crash_id: str
        """
        if crash_id is None:
            raise ValueError("Invalid value for `crash_id`, must not be `None`")

        self._crash_id = crash_id

    @property
    def created_time(self):
        """Gets the created_time of this CrashesListAttachments200ResponseInner.


        :return: The created_time of this CrashesListAttachments200ResponseInner.
        :rtype: datetime
        """
        return self._created_time

    @created_time.setter
    def created_time(self, created_time):
        """Sets the created_time of this CrashesListAttachments200ResponseInner.


        :param created_time: The created_time of this CrashesListAttachments200ResponseInner.
        :type created_time: datetime
        """
        if created_time is None:
            raise ValueError("Invalid value for `created_time`, must not be `None`")

        self._created_time = created_time

    @property
    def file_name(self):
        """Gets the file_name of this CrashesListAttachments200ResponseInner.


        :return: The file_name of this CrashesListAttachments200ResponseInner.
        :rtype: str
        """
        return self._file_name

    @file_name.setter
    def file_name(self, file_name):
        """Sets the file_name of this CrashesListAttachments200ResponseInner.


        :param file_name: The file_name of this CrashesListAttachments200ResponseInner.
        :type file_name: str
        """
        if file_name is None:
            raise ValueError("Invalid value for `file_name`, must not be `None`")

        self._file_name = file_name

    @property
    def size(self):
        """Gets the size of this CrashesListAttachments200ResponseInner.


        :return: The size of this CrashesListAttachments200ResponseInner.
        :rtype: float
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this CrashesListAttachments200ResponseInner.


        :param size: The size of this CrashesListAttachments200ResponseInner.
        :type size: float
        """
        if size is None:
            raise ValueError("Invalid value for `size`, must not be `None`")

        self._size = size
