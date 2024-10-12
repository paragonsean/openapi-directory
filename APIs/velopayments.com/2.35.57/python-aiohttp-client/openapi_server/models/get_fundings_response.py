# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.funding_audit import FundingAudit
from openapi_server.models.get_fundings_response_links import GetFundingsResponseLinks
from openapi_server.models.paged_user_response_page import PagedUserResponsePage
from openapi_server import util


class GetFundingsResponse(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, content: List[FundingAudit]=None, links: List[GetFundingsResponseLinks]=None, page: PagedUserResponsePage=None):
        """GetFundingsResponse - a model defined in OpenAPI

        :param content: The content of this GetFundingsResponse.
        :param links: The links of this GetFundingsResponse.
        :param page: The page of this GetFundingsResponse.
        """
        self.openapi_types = {
            'content': List[FundingAudit],
            'links': List[GetFundingsResponseLinks],
            'page': PagedUserResponsePage
        }

        self.attribute_map = {
            'content': 'content',
            'links': 'links',
            'page': 'page'
        }

        self._content = content
        self._links = links
        self._page = page

    @classmethod
    def from_dict(cls, dikt: dict) -> 'GetFundingsResponse':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The GetFundingsResponse of this GetFundingsResponse.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def content(self):
        """Gets the content of this GetFundingsResponse.


        :return: The content of this GetFundingsResponse.
        :rtype: List[FundingAudit]
        """
        return self._content

    @content.setter
    def content(self, content):
        """Sets the content of this GetFundingsResponse.


        :param content: The content of this GetFundingsResponse.
        :type content: List[FundingAudit]
        """

        self._content = content

    @property
    def links(self):
        """Gets the links of this GetFundingsResponse.


        :return: The links of this GetFundingsResponse.
        :rtype: List[GetFundingsResponseLinks]
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this GetFundingsResponse.


        :param links: The links of this GetFundingsResponse.
        :type links: List[GetFundingsResponseLinks]
        """

        self._links = links

    @property
    def page(self):
        """Gets the page of this GetFundingsResponse.


        :return: The page of this GetFundingsResponse.
        :rtype: PagedUserResponsePage
        """
        return self._page

    @page.setter
    def page(self, page):
        """Sets the page of this GetFundingsResponse.


        :param page: The page of this GetFundingsResponse.
        :type page: PagedUserResponsePage
        """

        self._page = page
