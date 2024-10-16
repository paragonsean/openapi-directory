# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class PatchReleaseRequest(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, dest_publish_id: str=None, error_context_id: str=None, error_details: str=None, is_wrapper_request: bool=None, status: str=None, wrap_package_url: str=None):
        """PatchReleaseRequest - a model defined in OpenAPI

        :param dest_publish_id: The dest_publish_id of this PatchReleaseRequest.
        :param error_context_id: The error_context_id of this PatchReleaseRequest.
        :param error_details: The error_details of this PatchReleaseRequest.
        :param is_wrapper_request: The is_wrapper_request of this PatchReleaseRequest.
        :param status: The status of this PatchReleaseRequest.
        :param wrap_package_url: The wrap_package_url of this PatchReleaseRequest.
        """
        self.openapi_types = {
            'dest_publish_id': str,
            'error_context_id': str,
            'error_details': str,
            'is_wrapper_request': bool,
            'status': str,
            'wrap_package_url': str
        }

        self.attribute_map = {
            'dest_publish_id': 'dest_publish_id',
            'error_context_id': 'error_contextId',
            'error_details': 'error_details',
            'is_wrapper_request': 'is_wrapper_request',
            'status': 'status',
            'wrap_package_url': 'wrap_package_url'
        }

        self._dest_publish_id = dest_publish_id
        self._error_context_id = error_context_id
        self._error_details = error_details
        self._is_wrapper_request = is_wrapper_request
        self._status = status
        self._wrap_package_url = wrap_package_url

    @classmethod
    def from_dict(cls, dikt: dict) -> 'PatchReleaseRequest':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The PatchReleaseRequest of this PatchReleaseRequest.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def dest_publish_id(self):
        """Gets the dest_publish_id of this PatchReleaseRequest.

        Destination Publish Id

        :return: The dest_publish_id of this PatchReleaseRequest.
        :rtype: str
        """
        return self._dest_publish_id

    @dest_publish_id.setter
    def dest_publish_id(self, dest_publish_id):
        """Sets the dest_publish_id of this PatchReleaseRequest.

        Destination Publish Id

        :param dest_publish_id: The dest_publish_id of this PatchReleaseRequest.
        :type dest_publish_id: str
        """

        self._dest_publish_id = dest_publish_id

    @property
    def error_context_id(self):
        """Gets the error_context_id of this PatchReleaseRequest.

        contextId for failed error message

        :return: The error_context_id of this PatchReleaseRequest.
        :rtype: str
        """
        return self._error_context_id

    @error_context_id.setter
    def error_context_id(self, error_context_id):
        """Sets the error_context_id of this PatchReleaseRequest.

        contextId for failed error message

        :param error_context_id: The error_context_id of this PatchReleaseRequest.
        :type error_context_id: str
        """

        self._error_context_id = error_context_id

    @property
    def error_details(self):
        """Gets the error_details of this PatchReleaseRequest.

        failure error details from store

        :return: The error_details of this PatchReleaseRequest.
        :rtype: str
        """
        return self._error_details

    @error_details.setter
    def error_details(self, error_details):
        """Sets the error_details of this PatchReleaseRequest.

        failure error details from store

        :param error_details: The error_details of this PatchReleaseRequest.
        :type error_details: str
        """

        self._error_details = error_details

    @property
    def is_wrapper_request(self):
        """Gets the is_wrapper_request of this PatchReleaseRequest.

        request is for wrapping or not

        :return: The is_wrapper_request of this PatchReleaseRequest.
        :rtype: bool
        """
        return self._is_wrapper_request

    @is_wrapper_request.setter
    def is_wrapper_request(self, is_wrapper_request):
        """Sets the is_wrapper_request of this PatchReleaseRequest.

        request is for wrapping or not

        :param is_wrapper_request: The is_wrapper_request of this PatchReleaseRequest.
        :type is_wrapper_request: bool
        """

        self._is_wrapper_request = is_wrapper_request

    @property
    def status(self):
        """Gets the status of this PatchReleaseRequest.

        updated status of release

        :return: The status of this PatchReleaseRequest.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this PatchReleaseRequest.

        updated status of release

        :param status: The status of this PatchReleaseRequest.
        :type status: str
        """

        self._status = status

    @property
    def wrap_package_url(self):
        """Gets the wrap_package_url of this PatchReleaseRequest.

        package url for wrapping request

        :return: The wrap_package_url of this PatchReleaseRequest.
        :rtype: str
        """
        return self._wrap_package_url

    @wrap_package_url.setter
    def wrap_package_url(self, wrap_package_url):
        """Sets the wrap_package_url of this PatchReleaseRequest.

        package url for wrapping request

        :param wrap_package_url: The wrap_package_url of this PatchReleaseRequest.
        :type wrap_package_url: str
        """

        self._wrap_package_url = wrap_package_url
