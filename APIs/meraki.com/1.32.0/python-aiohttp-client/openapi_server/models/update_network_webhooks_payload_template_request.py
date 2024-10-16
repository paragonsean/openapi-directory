# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.create_network_webhooks_payload_template_request_headers_inner import CreateNetworkWebhooksPayloadTemplateRequestHeadersInner
from openapi_server import util


class UpdateNetworkWebhooksPayloadTemplateRequest(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, body: str=None, body_file: str=None, headers: List[CreateNetworkWebhooksPayloadTemplateRequestHeadersInner]=None, headers_file: str=None, name: str=None):
        """UpdateNetworkWebhooksPayloadTemplateRequest - a model defined in OpenAPI

        :param body: The body of this UpdateNetworkWebhooksPayloadTemplateRequest.
        :param body_file: The body_file of this UpdateNetworkWebhooksPayloadTemplateRequest.
        :param headers: The headers of this UpdateNetworkWebhooksPayloadTemplateRequest.
        :param headers_file: The headers_file of this UpdateNetworkWebhooksPayloadTemplateRequest.
        :param name: The name of this UpdateNetworkWebhooksPayloadTemplateRequest.
        """
        self.openapi_types = {
            'body': str,
            'body_file': str,
            'headers': List[CreateNetworkWebhooksPayloadTemplateRequestHeadersInner],
            'headers_file': str,
            'name': str
        }

        self.attribute_map = {
            'body': 'body',
            'body_file': 'bodyFile',
            'headers': 'headers',
            'headers_file': 'headersFile',
            'name': 'name'
        }

        self._body = body
        self._body_file = body_file
        self._headers = headers
        self._headers_file = headers_file
        self._name = name

    @classmethod
    def from_dict(cls, dikt: dict) -> 'UpdateNetworkWebhooksPayloadTemplateRequest':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The updateNetworkWebhooksPayloadTemplate_request of this UpdateNetworkWebhooksPayloadTemplateRequest.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def body(self):
        """Gets the body of this UpdateNetworkWebhooksPayloadTemplateRequest.

        The liquid template used for the body of the webhook message.

        :return: The body of this UpdateNetworkWebhooksPayloadTemplateRequest.
        :rtype: str
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this UpdateNetworkWebhooksPayloadTemplateRequest.

        The liquid template used for the body of the webhook message.

        :param body: The body of this UpdateNetworkWebhooksPayloadTemplateRequest.
        :type body: str
        """

        self._body = body

    @property
    def body_file(self):
        """Gets the body_file of this UpdateNetworkWebhooksPayloadTemplateRequest.

        A file containing liquid template used for the body of the webhook message.

        :return: The body_file of this UpdateNetworkWebhooksPayloadTemplateRequest.
        :rtype: str
        """
        return self._body_file

    @body_file.setter
    def body_file(self, body_file):
        """Sets the body_file of this UpdateNetworkWebhooksPayloadTemplateRequest.

        A file containing liquid template used for the body of the webhook message.

        :param body_file: The body_file of this UpdateNetworkWebhooksPayloadTemplateRequest.
        :type body_file: str
        """

        self._body_file = body_file

    @property
    def headers(self):
        """Gets the headers of this UpdateNetworkWebhooksPayloadTemplateRequest.

        The liquid template used with the webhook headers.

        :return: The headers of this UpdateNetworkWebhooksPayloadTemplateRequest.
        :rtype: List[CreateNetworkWebhooksPayloadTemplateRequestHeadersInner]
        """
        return self._headers

    @headers.setter
    def headers(self, headers):
        """Sets the headers of this UpdateNetworkWebhooksPayloadTemplateRequest.

        The liquid template used with the webhook headers.

        :param headers: The headers of this UpdateNetworkWebhooksPayloadTemplateRequest.
        :type headers: List[CreateNetworkWebhooksPayloadTemplateRequestHeadersInner]
        """

        self._headers = headers

    @property
    def headers_file(self):
        """Gets the headers_file of this UpdateNetworkWebhooksPayloadTemplateRequest.

        A file containing the liquid template used with the webhook headers.

        :return: The headers_file of this UpdateNetworkWebhooksPayloadTemplateRequest.
        :rtype: str
        """
        return self._headers_file

    @headers_file.setter
    def headers_file(self, headers_file):
        """Sets the headers_file of this UpdateNetworkWebhooksPayloadTemplateRequest.

        A file containing the liquid template used with the webhook headers.

        :param headers_file: The headers_file of this UpdateNetworkWebhooksPayloadTemplateRequest.
        :type headers_file: str
        """

        self._headers_file = headers_file

    @property
    def name(self):
        """Gets the name of this UpdateNetworkWebhooksPayloadTemplateRequest.

        The name of the template

        :return: The name of this UpdateNetworkWebhooksPayloadTemplateRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this UpdateNetworkWebhooksPayloadTemplateRequest.

        The name of the template

        :param name: The name of this UpdateNetworkWebhooksPayloadTemplateRequest.
        :type name: str
        """

        self._name = name
