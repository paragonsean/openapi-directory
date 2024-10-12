# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class Report(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, config_id: str=None, guid: str=None, name: str=None, published: bool=None, report_id: str=None, status: str=None, summary: object=None, type: str=None):
        """Report - a model defined in OpenAPI

        :param config_id: The config_id of this Report.
        :param guid: The guid of this Report.
        :param name: The name of this Report.
        :param published: The published of this Report.
        :param report_id: The report_id of this Report.
        :param status: The status of this Report.
        :param summary: The summary of this Report.
        :param type: The type of this Report.
        """
        self.openapi_types = {
            'config_id': str,
            'guid': str,
            'name': str,
            'published': bool,
            'report_id': str,
            'status': str,
            'summary': object,
            'type': str
        }

        self.attribute_map = {
            'config_id': 'configId',
            'guid': 'guid',
            'name': 'name',
            'published': 'published',
            'report_id': 'reportId',
            'status': 'status',
            'summary': 'summary',
            'type': 'type'
        }

        self._config_id = config_id
        self._guid = guid
        self._name = name
        self._published = published
        self._report_id = report_id
        self._status = status
        self._summary = summary
        self._type = type

    @classmethod
    def from_dict(cls, dikt: dict) -> 'Report':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The Report of this Report.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def config_id(self):
        """Gets the config_id of this Report.


        :return: The config_id of this Report.
        :rtype: str
        """
        return self._config_id

    @config_id.setter
    def config_id(self, config_id):
        """Sets the config_id of this Report.


        :param config_id: The config_id of this Report.
        :type config_id: str
        """

        self._config_id = config_id

    @property
    def guid(self):
        """Gets the guid of this Report.


        :return: The guid of this Report.
        :rtype: str
        """
        return self._guid

    @guid.setter
    def guid(self, guid):
        """Sets the guid of this Report.


        :param guid: The guid of this Report.
        :type guid: str
        """

        self._guid = guid

    @property
    def name(self):
        """Gets the name of this Report.


        :return: The name of this Report.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Report.


        :param name: The name of this Report.
        :type name: str
        """

        self._name = name

    @property
    def published(self):
        """Gets the published of this Report.


        :return: The published of this Report.
        :rtype: bool
        """
        return self._published

    @published.setter
    def published(self, published):
        """Sets the published of this Report.


        :param published: The published of this Report.
        :type published: bool
        """

        self._published = published

    @property
    def report_id(self):
        """Gets the report_id of this Report.


        :return: The report_id of this Report.
        :rtype: str
        """
        return self._report_id

    @report_id.setter
    def report_id(self, report_id):
        """Sets the report_id of this Report.


        :param report_id: The report_id of this Report.
        :type report_id: str
        """

        self._report_id = report_id

    @property
    def status(self):
        """Gets the status of this Report.


        :return: The status of this Report.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this Report.


        :param status: The status of this Report.
        :type status: str
        """

        self._status = status

    @property
    def summary(self):
        """Gets the summary of this Report.


        :return: The summary of this Report.
        :rtype: object
        """
        return self._summary

    @summary.setter
    def summary(self, summary):
        """Sets the summary of this Report.


        :param summary: The summary of this Report.
        :type summary: object
        """

        self._summary = summary

    @property
    def type(self):
        """Gets the type of this Report.


        :return: The type of this Report.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Report.


        :param type: The type of this Report.
        :type type: str
        """

        self._type = type
