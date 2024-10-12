# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.global_config import GlobalConfig
from openapi_server.models.import_export_admins_inner import ImportExportAdminsInner
from openapi_server.models.import_export_api_keys_inner import ImportExportApiKeysInner
from openapi_server.models.import_export_error_templates_inner import ImportExportErrorTemplatesInner
from openapi_server.models.import_export_service_descriptors_inner import ImportExportServiceDescriptorsInner
from openapi_server.models.import_export_service_groups_inner import ImportExportServiceGroupsInner
from openapi_server.models.import_export_simple_admins_inner import ImportExportSimpleAdminsInner
from openapi_server.models.import_export_stats import ImportExportStats
from openapi_server import util


class ImportExport(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, admins: List[ImportExportAdminsInner]=None, api_keys: List[ImportExportApiKeysInner]=None, app_config: Dict[str, str]=None, config: GlobalConfig=None, _date: datetime=None, date_raw: int=None, error_templates: List[ImportExportErrorTemplatesInner]=None, label: str=None, service_descriptors: List[ImportExportServiceDescriptorsInner]=None, service_groups: List[ImportExportServiceGroupsInner]=None, simple_admins: List[ImportExportSimpleAdminsInner]=None, stats: ImportExportStats=None):
        """ImportExport - a model defined in OpenAPI

        :param admins: The admins of this ImportExport.
        :param api_keys: The api_keys of this ImportExport.
        :param app_config: The app_config of this ImportExport.
        :param config: The config of this ImportExport.
        :param _date: The _date of this ImportExport.
        :param date_raw: The date_raw of this ImportExport.
        :param error_templates: The error_templates of this ImportExport.
        :param label: The label of this ImportExport.
        :param service_descriptors: The service_descriptors of this ImportExport.
        :param service_groups: The service_groups of this ImportExport.
        :param simple_admins: The simple_admins of this ImportExport.
        :param stats: The stats of this ImportExport.
        """
        self.openapi_types = {
            'admins': List[ImportExportAdminsInner],
            'api_keys': List[ImportExportApiKeysInner],
            'app_config': Dict[str, str],
            'config': GlobalConfig,
            '_date': datetime,
            'date_raw': int,
            'error_templates': List[ImportExportErrorTemplatesInner],
            'label': str,
            'service_descriptors': List[ImportExportServiceDescriptorsInner],
            'service_groups': List[ImportExportServiceGroupsInner],
            'simple_admins': List[ImportExportSimpleAdminsInner],
            'stats': ImportExportStats
        }

        self.attribute_map = {
            'admins': 'admins',
            'api_keys': 'apiKeys',
            'app_config': 'appConfig',
            'config': 'config',
            '_date': 'date',
            'date_raw': 'dateRaw',
            'error_templates': 'errorTemplates',
            'label': 'label',
            'service_descriptors': 'serviceDescriptors',
            'service_groups': 'serviceGroups',
            'simple_admins': 'simpleAdmins',
            'stats': 'stats'
        }

        self._admins = admins
        self._api_keys = api_keys
        self._app_config = app_config
        self._config = config
        self.__date = _date
        self._date_raw = date_raw
        self._error_templates = error_templates
        self._label = label
        self._service_descriptors = service_descriptors
        self._service_groups = service_groups
        self._simple_admins = simple_admins
        self._stats = stats

    @classmethod
    def from_dict(cls, dikt: dict) -> 'ImportExport':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The ImportExport of this ImportExport.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def admins(self):
        """Gets the admins of this ImportExport.

        Current U2F admin at the time of export

        :return: The admins of this ImportExport.
        :rtype: List[ImportExportAdminsInner]
        """
        return self._admins

    @admins.setter
    def admins(self, admins):
        """Sets the admins of this ImportExport.

        Current U2F admin at the time of export

        :param admins: The admins of this ImportExport.
        :type admins: List[ImportExportAdminsInner]
        """
        if admins is None:
            raise ValueError("Invalid value for `admins`, must not be `None`")

        self._admins = admins

    @property
    def api_keys(self):
        """Gets the api_keys of this ImportExport.

        Current apik keys at the time of export

        :return: The api_keys of this ImportExport.
        :rtype: List[ImportExportApiKeysInner]
        """
        return self._api_keys

    @api_keys.setter
    def api_keys(self, api_keys):
        """Sets the api_keys of this ImportExport.

        Current apik keys at the time of export

        :param api_keys: The api_keys of this ImportExport.
        :type api_keys: List[ImportExportApiKeysInner]
        """
        if api_keys is None:
            raise ValueError("Invalid value for `api_keys`, must not be `None`")

        self._api_keys = api_keys

    @property
    def app_config(self):
        """Gets the app_config of this ImportExport.

        Current env variables at the time of export

        :return: The app_config of this ImportExport.
        :rtype: Dict[str, str]
        """
        return self._app_config

    @app_config.setter
    def app_config(self, app_config):
        """Sets the app_config of this ImportExport.

        Current env variables at the time of export

        :param app_config: The app_config of this ImportExport.
        :type app_config: Dict[str, str]
        """

        self._app_config = app_config

    @property
    def config(self):
        """Gets the config of this ImportExport.


        :return: The config of this ImportExport.
        :rtype: GlobalConfig
        """
        return self._config

    @config.setter
    def config(self, config):
        """Sets the config of this ImportExport.


        :param config: The config of this ImportExport.
        :type config: GlobalConfig
        """
        if config is None:
            raise ValueError("Invalid value for `config`, must not be `None`")

        self._config = config

    @property
    def _date(self):
        """Gets the _date of this ImportExport.


        :return: The _date of this ImportExport.
        :rtype: datetime
        """
        return self.__date

    @_date.setter
    def _date(self, _date):
        """Sets the _date of this ImportExport.


        :param _date: The _date of this ImportExport.
        :type _date: datetime
        """
        if _date is None:
            raise ValueError("Invalid value for `_date`, must not be `None`")

        self.__date = _date

    @property
    def date_raw(self):
        """Gets the date_raw of this ImportExport.


        :return: The date_raw of this ImportExport.
        :rtype: int
        """
        return self._date_raw

    @date_raw.setter
    def date_raw(self, date_raw):
        """Sets the date_raw of this ImportExport.


        :param date_raw: The date_raw of this ImportExport.
        :type date_raw: int
        """
        if date_raw is None:
            raise ValueError("Invalid value for `date_raw`, must not be `None`")

        self._date_raw = date_raw

    @property
    def error_templates(self):
        """Gets the error_templates of this ImportExport.

        Current error templates at the time of export

        :return: The error_templates of this ImportExport.
        :rtype: List[ImportExportErrorTemplatesInner]
        """
        return self._error_templates

    @error_templates.setter
    def error_templates(self, error_templates):
        """Sets the error_templates of this ImportExport.

        Current error templates at the time of export

        :param error_templates: The error_templates of this ImportExport.
        :type error_templates: List[ImportExportErrorTemplatesInner]
        """
        if error_templates is None:
            raise ValueError("Invalid value for `error_templates`, must not be `None`")

        self._error_templates = error_templates

    @property
    def label(self):
        """Gets the label of this ImportExport.


        :return: The label of this ImportExport.
        :rtype: str
        """
        return self._label

    @label.setter
    def label(self, label):
        """Sets the label of this ImportExport.


        :param label: The label of this ImportExport.
        :type label: str
        """
        if label is None:
            raise ValueError("Invalid value for `label`, must not be `None`")

        self._label = label

    @property
    def service_descriptors(self):
        """Gets the service_descriptors of this ImportExport.

        Current service descriptors at the time of export

        :return: The service_descriptors of this ImportExport.
        :rtype: List[ImportExportServiceDescriptorsInner]
        """
        return self._service_descriptors

    @service_descriptors.setter
    def service_descriptors(self, service_descriptors):
        """Sets the service_descriptors of this ImportExport.

        Current service descriptors at the time of export

        :param service_descriptors: The service_descriptors of this ImportExport.
        :type service_descriptors: List[ImportExportServiceDescriptorsInner]
        """
        if service_descriptors is None:
            raise ValueError("Invalid value for `service_descriptors`, must not be `None`")

        self._service_descriptors = service_descriptors

    @property
    def service_groups(self):
        """Gets the service_groups of this ImportExport.

        Current service groups at the time of export

        :return: The service_groups of this ImportExport.
        :rtype: List[ImportExportServiceGroupsInner]
        """
        return self._service_groups

    @service_groups.setter
    def service_groups(self, service_groups):
        """Sets the service_groups of this ImportExport.

        Current service groups at the time of export

        :param service_groups: The service_groups of this ImportExport.
        :type service_groups: List[ImportExportServiceGroupsInner]
        """
        if service_groups is None:
            raise ValueError("Invalid value for `service_groups`, must not be `None`")

        self._service_groups = service_groups

    @property
    def simple_admins(self):
        """Gets the simple_admins of this ImportExport.

        Current simple admins at the time of export

        :return: The simple_admins of this ImportExport.
        :rtype: List[ImportExportSimpleAdminsInner]
        """
        return self._simple_admins

    @simple_admins.setter
    def simple_admins(self, simple_admins):
        """Sets the simple_admins of this ImportExport.

        Current simple admins at the time of export

        :param simple_admins: The simple_admins of this ImportExport.
        :type simple_admins: List[ImportExportSimpleAdminsInner]
        """
        if simple_admins is None:
            raise ValueError("Invalid value for `simple_admins`, must not be `None`")

        self._simple_admins = simple_admins

    @property
    def stats(self):
        """Gets the stats of this ImportExport.


        :return: The stats of this ImportExport.
        :rtype: ImportExportStats
        """
        return self._stats

    @stats.setter
    def stats(self, stats):
        """Sets the stats of this ImportExport.


        :param stats: The stats of this ImportExport.
        :type stats: ImportExportStats
        """
        if stats is None:
            raise ValueError("Invalid value for `stats`, must not be `None`")

        self._stats = stats
