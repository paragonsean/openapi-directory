# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.error405_piis_additional_errors_inner import Error405PIISAdditionalErrorsInner
from openapi_server.models.links_all import LinksAll
from openapi_server.models.message_code405_piis import MessageCode405PIIS
from openapi_server import util


class Error405PIIS(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, links: LinksAll=None, additional_errors: List[Error405PIISAdditionalErrorsInner]=None, code: MessageCode405PIIS=None, detail: str=None, title: str=None, type: str=None):
        """Error405PIIS - a model defined in OpenAPI

        :param links: The links of this Error405PIIS.
        :param additional_errors: The additional_errors of this Error405PIIS.
        :param code: The code of this Error405PIIS.
        :param detail: The detail of this Error405PIIS.
        :param title: The title of this Error405PIIS.
        :param type: The type of this Error405PIIS.
        """
        self.openapi_types = {
            'links': LinksAll,
            'additional_errors': List[Error405PIISAdditionalErrorsInner],
            'code': MessageCode405PIIS,
            'detail': str,
            'title': str,
            'type': str
        }

        self.attribute_map = {
            'links': '_links',
            'additional_errors': 'additionalErrors',
            'code': 'code',
            'detail': 'detail',
            'title': 'title',
            'type': 'type'
        }

        self._links = links
        self._additional_errors = additional_errors
        self._code = code
        self._detail = detail
        self._title = title
        self._type = type

    @classmethod
    def from_dict(cls, dikt: dict) -> 'Error405PIIS':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The Error405_PIIS of this Error405PIIS.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def links(self):
        """Gets the links of this Error405PIIS.


        :return: The links of this Error405PIIS.
        :rtype: LinksAll
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this Error405PIIS.


        :param links: The links of this Error405PIIS.
        :type links: LinksAll
        """

        self._links = links

    @property
    def additional_errors(self):
        """Gets the additional_errors of this Error405PIIS.

        Array of Error Information Blocks.  Might be used if more than one error is to be communicated 

        :return: The additional_errors of this Error405PIIS.
        :rtype: List[Error405PIISAdditionalErrorsInner]
        """
        return self._additional_errors

    @additional_errors.setter
    def additional_errors(self, additional_errors):
        """Sets the additional_errors of this Error405PIIS.

        Array of Error Information Blocks.  Might be used if more than one error is to be communicated 

        :param additional_errors: The additional_errors of this Error405PIIS.
        :type additional_errors: List[Error405PIISAdditionalErrorsInner]
        """

        self._additional_errors = additional_errors

    @property
    def code(self):
        """Gets the code of this Error405PIIS.


        :return: The code of this Error405PIIS.
        :rtype: MessageCode405PIIS
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this Error405PIIS.


        :param code: The code of this Error405PIIS.
        :type code: MessageCode405PIIS
        """
        if code is None:
            raise ValueError("Invalid value for `code`, must not be `None`")

        self._code = code

    @property
    def detail(self):
        """Gets the detail of this Error405PIIS.

        Detailed human readable text specific to this instance of the error. XPath might be used to point to the issue generating the error in addition. Remark for Future: In future, a dedicated field might be introduced for the XPath. 

        :return: The detail of this Error405PIIS.
        :rtype: str
        """
        return self._detail

    @detail.setter
    def detail(self, detail):
        """Sets the detail of this Error405PIIS.

        Detailed human readable text specific to this instance of the error. XPath might be used to point to the issue generating the error in addition. Remark for Future: In future, a dedicated field might be introduced for the XPath. 

        :param detail: The detail of this Error405PIIS.
        :type detail: str
        """
        if detail is not None and len(detail) > 500:
            raise ValueError("Invalid value for `detail`, length must be less than or equal to `500`")

        self._detail = detail

    @property
    def title(self):
        """Gets the title of this Error405PIIS.

        Short human readable description of error type. Could be in local language. To be provided by ASPSPs. 

        :return: The title of this Error405PIIS.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this Error405PIIS.

        Short human readable description of error type. Could be in local language. To be provided by ASPSPs. 

        :param title: The title of this Error405PIIS.
        :type title: str
        """
        if title is not None and len(title) > 70:
            raise ValueError("Invalid value for `title`, length must be less than or equal to `70`")

        self._title = title

    @property
    def type(self):
        """Gets the type of this Error405PIIS.

        A URI reference [RFC3986] that identifies the problem type. Remark For Future: These URI will be provided by NextGen in future. 

        :return: The type of this Error405PIIS.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Error405PIIS.

        A URI reference [RFC3986] that identifies the problem type. Remark For Future: These URI will be provided by NextGen in future. 

        :param type: The type of this Error405PIIS.
        :type type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")
        if type is not None and len(type) > 70:
            raise ValueError("Invalid value for `type`, length must be less than or equal to `70`")

        self._type = type
