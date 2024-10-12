# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.global_jwt_verifier_algo_settings import GlobalJwtVerifierAlgoSettings
from openapi_server.models.global_jwt_verifier_source import GlobalJwtVerifierSource
from openapi_server.models.global_jwt_verifier_strategy import GlobalJwtVerifierStrategy
from openapi_server.models.local_jwt_verifier import LocalJwtVerifier
from openapi_server.models.ref_jwt_verifier import RefJwtVerifier
from openapi_server import util


class ImportExportServiceDescriptorsInnerJwtVerifier(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, algo_settings: GlobalJwtVerifierAlgoSettings=None, enabled: bool=None, source: GlobalJwtVerifierSource=None, strategy: GlobalJwtVerifierStrategy=None, strict: bool=None, type: str=None, id: str=None):
        """ImportExportServiceDescriptorsInnerJwtVerifier - a model defined in OpenAPI

        :param algo_settings: The algo_settings of this ImportExportServiceDescriptorsInnerJwtVerifier.
        :param enabled: The enabled of this ImportExportServiceDescriptorsInnerJwtVerifier.
        :param source: The source of this ImportExportServiceDescriptorsInnerJwtVerifier.
        :param strategy: The strategy of this ImportExportServiceDescriptorsInnerJwtVerifier.
        :param strict: The strict of this ImportExportServiceDescriptorsInnerJwtVerifier.
        :param type: The type of this ImportExportServiceDescriptorsInnerJwtVerifier.
        :param id: The id of this ImportExportServiceDescriptorsInnerJwtVerifier.
        """
        self.openapi_types = {
            'algo_settings': GlobalJwtVerifierAlgoSettings,
            'enabled': bool,
            'source': GlobalJwtVerifierSource,
            'strategy': GlobalJwtVerifierStrategy,
            'strict': bool,
            'type': str,
            'id': str
        }

        self.attribute_map = {
            'algo_settings': 'algoSettings',
            'enabled': 'enabled',
            'source': 'source',
            'strategy': 'strategy',
            'strict': 'strict',
            'type': 'type',
            'id': 'id'
        }

        self._algo_settings = algo_settings
        self._enabled = enabled
        self._source = source
        self._strategy = strategy
        self._strict = strict
        self._type = type
        self._id = id

    @classmethod
    def from_dict(cls, dikt: dict) -> 'ImportExportServiceDescriptorsInnerJwtVerifier':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The ImportExport_serviceDescriptors_inner_jwtVerifier of this ImportExportServiceDescriptorsInnerJwtVerifier.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def algo_settings(self):
        """Gets the algo_settings of this ImportExportServiceDescriptorsInnerJwtVerifier.


        :return: The algo_settings of this ImportExportServiceDescriptorsInnerJwtVerifier.
        :rtype: GlobalJwtVerifierAlgoSettings
        """
        return self._algo_settings

    @algo_settings.setter
    def algo_settings(self, algo_settings):
        """Sets the algo_settings of this ImportExportServiceDescriptorsInnerJwtVerifier.


        :param algo_settings: The algo_settings of this ImportExportServiceDescriptorsInnerJwtVerifier.
        :type algo_settings: GlobalJwtVerifierAlgoSettings
        """
        if algo_settings is None:
            raise ValueError("Invalid value for `algo_settings`, must not be `None`")

        self._algo_settings = algo_settings

    @property
    def enabled(self):
        """Gets the enabled of this ImportExportServiceDescriptorsInnerJwtVerifier.

        Is it enabled

        :return: The enabled of this ImportExportServiceDescriptorsInnerJwtVerifier.
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this ImportExportServiceDescriptorsInnerJwtVerifier.

        Is it enabled

        :param enabled: The enabled of this ImportExportServiceDescriptorsInnerJwtVerifier.
        :type enabled: bool
        """
        if enabled is None:
            raise ValueError("Invalid value for `enabled`, must not be `None`")

        self._enabled = enabled

    @property
    def source(self):
        """Gets the source of this ImportExportServiceDescriptorsInnerJwtVerifier.


        :return: The source of this ImportExportServiceDescriptorsInnerJwtVerifier.
        :rtype: GlobalJwtVerifierSource
        """
        return self._source

    @source.setter
    def source(self, source):
        """Sets the source of this ImportExportServiceDescriptorsInnerJwtVerifier.


        :param source: The source of this ImportExportServiceDescriptorsInnerJwtVerifier.
        :type source: GlobalJwtVerifierSource
        """
        if source is None:
            raise ValueError("Invalid value for `source`, must not be `None`")

        self._source = source

    @property
    def strategy(self):
        """Gets the strategy of this ImportExportServiceDescriptorsInnerJwtVerifier.


        :return: The strategy of this ImportExportServiceDescriptorsInnerJwtVerifier.
        :rtype: GlobalJwtVerifierStrategy
        """
        return self._strategy

    @strategy.setter
    def strategy(self, strategy):
        """Sets the strategy of this ImportExportServiceDescriptorsInnerJwtVerifier.


        :param strategy: The strategy of this ImportExportServiceDescriptorsInnerJwtVerifier.
        :type strategy: GlobalJwtVerifierStrategy
        """
        if strategy is None:
            raise ValueError("Invalid value for `strategy`, must not be `None`")

        self._strategy = strategy

    @property
    def strict(self):
        """Gets the strict of this ImportExportServiceDescriptorsInnerJwtVerifier.

        Does it fail if JWT not found

        :return: The strict of this ImportExportServiceDescriptorsInnerJwtVerifier.
        :rtype: bool
        """
        return self._strict

    @strict.setter
    def strict(self, strict):
        """Sets the strict of this ImportExportServiceDescriptorsInnerJwtVerifier.

        Does it fail if JWT not found

        :param strict: The strict of this ImportExportServiceDescriptorsInnerJwtVerifier.
        :type strict: bool
        """
        if strict is None:
            raise ValueError("Invalid value for `strict`, must not be `None`")

        self._strict = strict

    @property
    def type(self):
        """Gets the type of this ImportExportServiceDescriptorsInnerJwtVerifier.

        A string with value 'ref'

        :return: The type of this ImportExportServiceDescriptorsInnerJwtVerifier.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ImportExportServiceDescriptorsInnerJwtVerifier.

        A string with value 'ref'

        :param type: The type of this ImportExportServiceDescriptorsInnerJwtVerifier.
        :type type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")

        self._type = type

    @property
    def id(self):
        """Gets the id of this ImportExportServiceDescriptorsInnerJwtVerifier.

        The id of the GlobalJWTVerifier

        :return: The id of this ImportExportServiceDescriptorsInnerJwtVerifier.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ImportExportServiceDescriptorsInnerJwtVerifier.

        The id of the GlobalJWTVerifier

        :param id: The id of this ImportExportServiceDescriptorsInnerJwtVerifier.
        :type id: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")

        self._id = id
