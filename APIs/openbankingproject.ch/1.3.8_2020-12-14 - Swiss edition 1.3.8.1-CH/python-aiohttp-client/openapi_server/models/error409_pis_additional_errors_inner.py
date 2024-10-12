# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.message_code409_pis import MessageCode409PIS
from openapi_server import util


class Error409PISAdditionalErrorsInner(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, code: MessageCode409PIS=None, detail: str=None, title: str=None):
        """Error409PISAdditionalErrorsInner - a model defined in OpenAPI

        :param code: The code of this Error409PISAdditionalErrorsInner.
        :param detail: The detail of this Error409PISAdditionalErrorsInner.
        :param title: The title of this Error409PISAdditionalErrorsInner.
        """
        self.openapi_types = {
            'code': MessageCode409PIS,
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
    def from_dict(cls, dikt: dict) -> 'Error409PISAdditionalErrorsInner':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The Error409_PIS_additionalErrors_inner of this Error409PISAdditionalErrorsInner.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def code(self):
        """Gets the code of this Error409PISAdditionalErrorsInner.


        :return: The code of this Error409PISAdditionalErrorsInner.
        :rtype: MessageCode409PIS
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this Error409PISAdditionalErrorsInner.


        :param code: The code of this Error409PISAdditionalErrorsInner.
        :type code: MessageCode409PIS
        """
        if code is None:
            raise ValueError("Invalid value for `code`, must not be `None`")

        self._code = code

    @property
    def detail(self):
        """Gets the detail of this Error409PISAdditionalErrorsInner.

        Detailed human readable text specific to this instance of the error. XPath might be used to point to the issue generating the error in addition. Remark for Future: In future, a dedicated field might be introduced for the XPath. 

        :return: The detail of this Error409PISAdditionalErrorsInner.
        :rtype: str
        """
        return self._detail

    @detail.setter
    def detail(self, detail):
        """Sets the detail of this Error409PISAdditionalErrorsInner.

        Detailed human readable text specific to this instance of the error. XPath might be used to point to the issue generating the error in addition. Remark for Future: In future, a dedicated field might be introduced for the XPath. 

        :param detail: The detail of this Error409PISAdditionalErrorsInner.
        :type detail: str
        """
        if detail is not None and len(detail) > 500:
            raise ValueError("Invalid value for `detail`, length must be less than or equal to `500`")

        self._detail = detail

    @property
    def title(self):
        """Gets the title of this Error409PISAdditionalErrorsInner.

        Short human readable description of error type. Could be in local language. To be provided by ASPSPs. 

        :return: The title of this Error409PISAdditionalErrorsInner.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this Error409PISAdditionalErrorsInner.

        Short human readable description of error type. Could be in local language. To be provided by ASPSPs. 

        :param title: The title of this Error409PISAdditionalErrorsInner.
        :type title: str
        """
        if title is not None and len(title) > 70:
            raise ValueError("Invalid value for `title`, length must be less than or equal to `70`")

        self._title = title
