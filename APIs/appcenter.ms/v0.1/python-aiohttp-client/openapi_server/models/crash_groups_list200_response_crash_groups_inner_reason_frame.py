# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class CrashGroupsList200ResponseCrashGroupsInnerReasonFrame(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, app_code: bool=None, class_method: bool=None, class_name: str=None, code_formatted: str=None, code_raw: str=None, exception_type: str=None, file: str=None, framework_name: str=None, language: str=None, line: int=None, method: str=None, method_params: str=None, os_exception_type: str=None):
        """CrashGroupsList200ResponseCrashGroupsInnerReasonFrame - a model defined in OpenAPI

        :param app_code: The app_code of this CrashGroupsList200ResponseCrashGroupsInnerReasonFrame.
        :param class_method: The class_method of this CrashGroupsList200ResponseCrashGroupsInnerReasonFrame.
        :param class_name: The class_name of this CrashGroupsList200ResponseCrashGroupsInnerReasonFrame.
        :param code_formatted: The code_formatted of this CrashGroupsList200ResponseCrashGroupsInnerReasonFrame.
        :param code_raw: The code_raw of this CrashGroupsList200ResponseCrashGroupsInnerReasonFrame.
        :param exception_type: The exception_type of this CrashGroupsList200ResponseCrashGroupsInnerReasonFrame.
        :param file: The file of this CrashGroupsList200ResponseCrashGroupsInnerReasonFrame.
        :param framework_name: The framework_name of this CrashGroupsList200ResponseCrashGroupsInnerReasonFrame.
        :param language: The language of this CrashGroupsList200ResponseCrashGroupsInnerReasonFrame.
        :param line: The line of this CrashGroupsList200ResponseCrashGroupsInnerReasonFrame.
        :param method: The method of this CrashGroupsList200ResponseCrashGroupsInnerReasonFrame.
        :param method_params: The method_params of this CrashGroupsList200ResponseCrashGroupsInnerReasonFrame.
        :param os_exception_type: The os_exception_type of this CrashGroupsList200ResponseCrashGroupsInnerReasonFrame.
        """
        self.openapi_types = {
            'app_code': bool,
            'class_method': bool,
            'class_name': str,
            'code_formatted': str,
            'code_raw': str,
            'exception_type': str,
            'file': str,
            'framework_name': str,
            'language': str,
            'line': int,
            'method': str,
            'method_params': str,
            'os_exception_type': str
        }

        self.attribute_map = {
            'app_code': 'app_code',
            'class_method': 'class_method',
            'class_name': 'class_name',
            'code_formatted': 'code_formatted',
            'code_raw': 'code_raw',
            'exception_type': 'exception_type',
            'file': 'file',
            'framework_name': 'framework_name',
            'language': 'language',
            'line': 'line',
            'method': 'method',
            'method_params': 'method_params',
            'os_exception_type': 'os_exception_type'
        }

        self._app_code = app_code
        self._class_method = class_method
        self._class_name = class_name
        self._code_formatted = code_formatted
        self._code_raw = code_raw
        self._exception_type = exception_type
        self._file = file
        self._framework_name = framework_name
        self._language = language
        self._line = line
        self._method = method
        self._method_params = method_params
        self._os_exception_type = os_exception_type

    @classmethod
    def from_dict(cls, dikt: dict) -> 'CrashGroupsList200ResponseCrashGroupsInnerReasonFrame':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The crashGroups_list_200_response_crash_groups_inner_reason_frame of this CrashGroupsList200ResponseCrashGroupsInnerReasonFrame.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def app_code(self):
        """Gets the app_code of this CrashGroupsList200ResponseCrashGroupsInnerReasonFrame.

        this line isn't from any framework

        :return: The app_code of this CrashGroupsList200ResponseCrashGroupsInnerReasonFrame.
        :rtype: bool
        """
        return self._app_code

    @app_code.setter
    def app_code(self, app_code):
        """Sets the app_code of this CrashGroupsList200ResponseCrashGroupsInnerReasonFrame.

        this line isn't from any framework

        :param app_code: The app_code of this CrashGroupsList200ResponseCrashGroupsInnerReasonFrame.
        :type app_code: bool
        """

        self._app_code = app_code

    @property
    def class_method(self):
        """Gets the class_method of this CrashGroupsList200ResponseCrashGroupsInnerReasonFrame.

        is a class method

        :return: The class_method of this CrashGroupsList200ResponseCrashGroupsInnerReasonFrame.
        :rtype: bool
        """
        return self._class_method

    @class_method.setter
    def class_method(self, class_method):
        """Sets the class_method of this CrashGroupsList200ResponseCrashGroupsInnerReasonFrame.

        is a class method

        :param class_method: The class_method of this CrashGroupsList200ResponseCrashGroupsInnerReasonFrame.
        :type class_method: bool
        """

        self._class_method = class_method

    @property
    def class_name(self):
        """Gets the class_name of this CrashGroupsList200ResponseCrashGroupsInnerReasonFrame.

        name of the class

        :return: The class_name of this CrashGroupsList200ResponseCrashGroupsInnerReasonFrame.
        :rtype: str
        """
        return self._class_name

    @class_name.setter
    def class_name(self, class_name):
        """Sets the class_name of this CrashGroupsList200ResponseCrashGroupsInnerReasonFrame.

        name of the class

        :param class_name: The class_name of this CrashGroupsList200ResponseCrashGroupsInnerReasonFrame.
        :type class_name: str
        """

        self._class_name = class_name

    @property
    def code_formatted(self):
        """Gets the code_formatted of this CrashGroupsList200ResponseCrashGroupsInnerReasonFrame.

        Formatted frame string

        :return: The code_formatted of this CrashGroupsList200ResponseCrashGroupsInnerReasonFrame.
        :rtype: str
        """
        return self._code_formatted

    @code_formatted.setter
    def code_formatted(self, code_formatted):
        """Sets the code_formatted of this CrashGroupsList200ResponseCrashGroupsInnerReasonFrame.

        Formatted frame string

        :param code_formatted: The code_formatted of this CrashGroupsList200ResponseCrashGroupsInnerReasonFrame.
        :type code_formatted: str
        """

        self._code_formatted = code_formatted

    @property
    def code_raw(self):
        """Gets the code_raw of this CrashGroupsList200ResponseCrashGroupsInnerReasonFrame.

        Unformatted Frame string

        :return: The code_raw of this CrashGroupsList200ResponseCrashGroupsInnerReasonFrame.
        :rtype: str
        """
        return self._code_raw

    @code_raw.setter
    def code_raw(self, code_raw):
        """Sets the code_raw of this CrashGroupsList200ResponseCrashGroupsInnerReasonFrame.

        Unformatted Frame string

        :param code_raw: The code_raw of this CrashGroupsList200ResponseCrashGroupsInnerReasonFrame.
        :type code_raw: str
        """

        self._code_raw = code_raw

    @property
    def exception_type(self):
        """Gets the exception_type of this CrashGroupsList200ResponseCrashGroupsInnerReasonFrame.

        Exception type.

        :return: The exception_type of this CrashGroupsList200ResponseCrashGroupsInnerReasonFrame.
        :rtype: str
        """
        return self._exception_type

    @exception_type.setter
    def exception_type(self, exception_type):
        """Sets the exception_type of this CrashGroupsList200ResponseCrashGroupsInnerReasonFrame.

        Exception type.

        :param exception_type: The exception_type of this CrashGroupsList200ResponseCrashGroupsInnerReasonFrame.
        :type exception_type: str
        """

        self._exception_type = exception_type

    @property
    def file(self):
        """Gets the file of this CrashGroupsList200ResponseCrashGroupsInnerReasonFrame.

        name of the file

        :return: The file of this CrashGroupsList200ResponseCrashGroupsInnerReasonFrame.
        :rtype: str
        """
        return self._file

    @file.setter
    def file(self, file):
        """Sets the file of this CrashGroupsList200ResponseCrashGroupsInnerReasonFrame.

        name of the file

        :param file: The file of this CrashGroupsList200ResponseCrashGroupsInnerReasonFrame.
        :type file: str
        """

        self._file = file

    @property
    def framework_name(self):
        """Gets the framework_name of this CrashGroupsList200ResponseCrashGroupsInnerReasonFrame.

        Name of the framework

        :return: The framework_name of this CrashGroupsList200ResponseCrashGroupsInnerReasonFrame.
        :rtype: str
        """
        return self._framework_name

    @framework_name.setter
    def framework_name(self, framework_name):
        """Sets the framework_name of this CrashGroupsList200ResponseCrashGroupsInnerReasonFrame.

        Name of the framework

        :param framework_name: The framework_name of this CrashGroupsList200ResponseCrashGroupsInnerReasonFrame.
        :type framework_name: str
        """

        self._framework_name = framework_name

    @property
    def language(self):
        """Gets the language of this CrashGroupsList200ResponseCrashGroupsInnerReasonFrame.

        programming language of the frame

        :return: The language of this CrashGroupsList200ResponseCrashGroupsInnerReasonFrame.
        :rtype: str
        """
        return self._language

    @language.setter
    def language(self, language):
        """Sets the language of this CrashGroupsList200ResponseCrashGroupsInnerReasonFrame.

        programming language of the frame

        :param language: The language of this CrashGroupsList200ResponseCrashGroupsInnerReasonFrame.
        :type language: str
        """
        allowed_values = ["JavaScript", "CSharp", "Objective-C", "Objective-Cpp", "Cpp", "C", "Swift", "Java", "Unknown"]  # noqa: E501
        if language not in allowed_values:
            raise ValueError(
                "Invalid value for `language` ({0}), must be one of {1}"
                .format(language, allowed_values)
            )

        self._language = language

    @property
    def line(self):
        """Gets the line of this CrashGroupsList200ResponseCrashGroupsInnerReasonFrame.

        line number

        :return: The line of this CrashGroupsList200ResponseCrashGroupsInnerReasonFrame.
        :rtype: int
        """
        return self._line

    @line.setter
    def line(self, line):
        """Sets the line of this CrashGroupsList200ResponseCrashGroupsInnerReasonFrame.

        line number

        :param line: The line of this CrashGroupsList200ResponseCrashGroupsInnerReasonFrame.
        :type line: int
        """

        self._line = line

    @property
    def method(self):
        """Gets the method of this CrashGroupsList200ResponseCrashGroupsInnerReasonFrame.

        name of the method

        :return: The method of this CrashGroupsList200ResponseCrashGroupsInnerReasonFrame.
        :rtype: str
        """
        return self._method

    @method.setter
    def method(self, method):
        """Sets the method of this CrashGroupsList200ResponseCrashGroupsInnerReasonFrame.

        name of the method

        :param method: The method of this CrashGroupsList200ResponseCrashGroupsInnerReasonFrame.
        :type method: str
        """

        self._method = method

    @property
    def method_params(self):
        """Gets the method_params of this CrashGroupsList200ResponseCrashGroupsInnerReasonFrame.

        parameters of the frames method

        :return: The method_params of this CrashGroupsList200ResponseCrashGroupsInnerReasonFrame.
        :rtype: str
        """
        return self._method_params

    @method_params.setter
    def method_params(self, method_params):
        """Sets the method_params of this CrashGroupsList200ResponseCrashGroupsInnerReasonFrame.

        parameters of the frames method

        :param method_params: The method_params of this CrashGroupsList200ResponseCrashGroupsInnerReasonFrame.
        :type method_params: str
        """

        self._method_params = method_params

    @property
    def os_exception_type(self):
        """Gets the os_exception_type of this CrashGroupsList200ResponseCrashGroupsInnerReasonFrame.

        OS exception type. (aka. SIGNAL)

        :return: The os_exception_type of this CrashGroupsList200ResponseCrashGroupsInnerReasonFrame.
        :rtype: str
        """
        return self._os_exception_type

    @os_exception_type.setter
    def os_exception_type(self, os_exception_type):
        """Sets the os_exception_type of this CrashGroupsList200ResponseCrashGroupsInnerReasonFrame.

        OS exception type. (aka. SIGNAL)

        :param os_exception_type: The os_exception_type of this CrashGroupsList200ResponseCrashGroupsInnerReasonFrame.
        :type os_exception_type: str
        """

        self._os_exception_type = os_exception_type
