# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.message_code405_sbs import MessageCode405SBS
from openapi_server import util


class Error405SBSAdditionalErrorsInner(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, code: MessageCode405SBS=None, detail: str=None, title: str=None):
        """Error405SBSAdditionalErrorsInner - a model defined in OpenAPI

        :param code: The code of this Error405SBSAdditionalErrorsInner.
        :param detail: The detail of this Error405SBSAdditionalErrorsInner.
        :param title: The title of this Error405SBSAdditionalErrorsInner.
        """
        self.openapi_types = {
            'code': MessageCode405SBS,
            'detail': str,
            'title': str
        }

        self.attribute_map = {
            'code': 'code',
            'detail': 'detail',
            'title': 'title'
        }

        self._code = code
        self._detail = detail
        self._title = title

    @classmethod
    def from_dict(cls, dikt: dict) -> 'Error405SBSAdditionalErrorsInner':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The Error405_SBS_additionalErrors_inner of this Error405SBSAdditionalErrorsInner.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def code(self):
        """Gets the code of this Error405SBSAdditionalErrorsInner.


        :return: The code of this Error405SBSAdditionalErrorsInner.
        :rtype: MessageCode405SBS
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this Error405SBSAdditionalErrorsInner.


        :param code: The code of this Error405SBSAdditionalErrorsInner.
        :type code: MessageCode405SBS
        """
        if code is None:
            raise ValueError("Invalid value for `code`, must not be `None`")

        self._code = code

    @property
    def detail(self):
        """Gets the detail of this Error405SBSAdditionalErrorsInner.

        Detailed human readable text specific to this instance of the error. XPath might be used to point to the issue generating the error in addition. Remark for Future: In future, a dedicated field might be introduced for the XPath. 

        :return: The detail of this Error405SBSAdditionalErrorsInner.
        :rtype: str
        """
        return self._detail

    @detail.setter
    def detail(self, detail):
        """Sets the detail of this Error405SBSAdditionalErrorsInner.

        Detailed human readable text specific to this instance of the error. XPath might be used to point to the issue generating the error in addition. Remark for Future: In future, a dedicated field might be introduced for the XPath. 

        :param detail: The detail of this Error405SBSAdditionalErrorsInner.
        :type detail: str
        """
        if detail is not None and len(detail) > 500:
            raise ValueError("Invalid value for `detail`, length must be less than or equal to `500`")

        self._detail = detail

    @property
    def title(self):
        """Gets the title of this Error405SBSAdditionalErrorsInner.

        Short human readable description of error type. Could be in local language. To be provided by ASPSPs. 

        :return: The title of this Error405SBSAdditionalErrorsInner.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this Error405SBSAdditionalErrorsInner.

        Short human readable description of error type. Could be in local language. To be provided by ASPSPs. 

        :param title: The title of this Error405SBSAdditionalErrorsInner.
        :type title: str
        """
        if title is not None and len(title) > 70:
            raise ValueError("Invalid value for `title`, length must be less than or equal to `70`")

        self._title = title
