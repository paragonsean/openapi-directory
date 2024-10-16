# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.webhook_v2_event_data_resources_inner import WebhookV2EventDataResourcesInner
from openapi_server.models.webhook_v2_event_data_share_inner import WebhookV2EventDataShareInner
from openapi_server import util


class WebhookV2EventData(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, form_details: List[object]=None, resources: List[WebhookV2EventDataResourcesInner]=None, share: List[WebhookV2EventDataShareInner]=None, transfer_status: str=None):
        """WebhookV2EventData - a model defined in OpenAPI

        :param form_details: The form_details of this WebhookV2EventData.
        :param resources: The resources of this WebhookV2EventData.
        :param share: The share of this WebhookV2EventData.
        :param transfer_status: The transfer_status of this WebhookV2EventData.
        """
        self.openapi_types = {
            'form_details': List[object],
            'resources': List[WebhookV2EventDataResourcesInner],
            'share': List[WebhookV2EventDataShareInner],
            'transfer_status': str
        }

        self.attribute_map = {
            'form_details': 'formDetails',
            'resources': 'resources',
            'share': 'share',
            'transfer_status': 'transferStatus'
        }

        self._form_details = form_details
        self._resources = resources
        self._share = share
        self._transfer_status = transfer_status

    @classmethod
    def from_dict(cls, dikt: dict) -> 'WebhookV2EventData':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The WebhookV2EventData of this WebhookV2EventData.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def form_details(self):
        """Gets the form_details of this WebhookV2EventData.


        :return: The form_details of this WebhookV2EventData.
        :rtype: List[object]
        """
        return self._form_details

    @form_details.setter
    def form_details(self, form_details):
        """Sets the form_details of this WebhookV2EventData.


        :param form_details: The form_details of this WebhookV2EventData.
        :type form_details: List[object]
        """

        self._form_details = form_details

    @property
    def resources(self):
        """Gets the resources of this WebhookV2EventData.


        :return: The resources of this WebhookV2EventData.
        :rtype: List[WebhookV2EventDataResourcesInner]
        """
        return self._resources

    @resources.setter
    def resources(self, resources):
        """Sets the resources of this WebhookV2EventData.


        :param resources: The resources of this WebhookV2EventData.
        :type resources: List[WebhookV2EventDataResourcesInner]
        """

        self._resources = resources

    @property
    def share(self):
        """Gets the share of this WebhookV2EventData.


        :return: The share of this WebhookV2EventData.
        :rtype: List[WebhookV2EventDataShareInner]
        """
        return self._share

    @share.setter
    def share(self, share):
        """Sets the share of this WebhookV2EventData.


        :param share: The share of this WebhookV2EventData.
        :type share: List[WebhookV2EventDataShareInner]
        """

        self._share = share

    @property
    def transfer_status(self):
        """Gets the transfer_status of this WebhookV2EventData.

        For uploads, and downloads, whether the file transferred OK. `success` means the transfer did not have errors

        :return: The transfer_status of this WebhookV2EventData.
        :rtype: str
        """
        return self._transfer_status

    @transfer_status.setter
    def transfer_status(self, transfer_status):
        """Sets the transfer_status of this WebhookV2EventData.

        For uploads, and downloads, whether the file transferred OK. `success` means the transfer did not have errors

        :param transfer_status: The transfer_status of this WebhookV2EventData.
        :type transfer_status: str
        """

        self._transfer_status = transfer_status
