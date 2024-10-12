# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class ApiVersionSetUpdateParametersProperties(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, display_name: str=None, versioning_scheme: str=None, description: str=None, version_header_name: str=None, version_query_name: str=None):
        """ApiVersionSetUpdateParametersProperties - a model defined in OpenAPI

        :param display_name: The display_name of this ApiVersionSetUpdateParametersProperties.
        :param versioning_scheme: The versioning_scheme of this ApiVersionSetUpdateParametersProperties.
        :param description: The description of this ApiVersionSetUpdateParametersProperties.
        :param version_header_name: The version_header_name of this ApiVersionSetUpdateParametersProperties.
        :param version_query_name: The version_query_name of this ApiVersionSetUpdateParametersProperties.
        """
        self.openapi_types = {
            'display_name': str,
            'versioning_scheme': str,
            'description': str,
            'version_header_name': str,
            'version_query_name': str
        }

        self.attribute_map = {
            'display_name': 'displayName',
            'versioning_scheme': 'versioningScheme',
            'description': 'description',
            'version_header_name': 'versionHeaderName',
            'version_query_name': 'versionQueryName'
        }

        self._display_name = display_name
        self._versioning_scheme = versioning_scheme
        self._description = description
        self._version_header_name = version_header_name
        self._version_query_name = version_query_name

    @classmethod
    def from_dict(cls, dikt: dict) -> 'ApiVersionSetUpdateParametersProperties':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The ApiVersionSetUpdateParametersProperties of this ApiVersionSetUpdateParametersProperties.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def display_name(self):
        """Gets the display_name of this ApiVersionSetUpdateParametersProperties.

        Name of API Version Set

        :return: The display_name of this ApiVersionSetUpdateParametersProperties.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this ApiVersionSetUpdateParametersProperties.

        Name of API Version Set

        :param display_name: The display_name of this ApiVersionSetUpdateParametersProperties.
        :type display_name: str
        """
        if display_name is not None and len(display_name) > 100:
            raise ValueError("Invalid value for `display_name`, length must be less than or equal to `100`")
        if display_name is not None and len(display_name) < 1:
            raise ValueError("Invalid value for `display_name`, length must be greater than or equal to `1`")

        self._display_name = display_name

    @property
    def versioning_scheme(self):
        """Gets the versioning_scheme of this ApiVersionSetUpdateParametersProperties.

        An value that determines where the API Version identifer will be located in a HTTP request.

        :return: The versioning_scheme of this ApiVersionSetUpdateParametersProperties.
        :rtype: str
        """
        return self._versioning_scheme

    @versioning_scheme.setter
    def versioning_scheme(self, versioning_scheme):
        """Sets the versioning_scheme of this ApiVersionSetUpdateParametersProperties.

        An value that determines where the API Version identifer will be located in a HTTP request.

        :param versioning_scheme: The versioning_scheme of this ApiVersionSetUpdateParametersProperties.
        :type versioning_scheme: str
        """
        allowed_values = ["Segment", "Query", "Header"]  # noqa: E501
        if versioning_scheme not in allowed_values:
            raise ValueError(
                "Invalid value for `versioning_scheme` ({0}), must be one of {1}"
                .format(versioning_scheme, allowed_values)
            )

        self._versioning_scheme = versioning_scheme

    @property
    def description(self):
        """Gets the description of this ApiVersionSetUpdateParametersProperties.

        Description of API Version Set.

        :return: The description of this ApiVersionSetUpdateParametersProperties.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ApiVersionSetUpdateParametersProperties.

        Description of API Version Set.

        :param description: The description of this ApiVersionSetUpdateParametersProperties.
        :type description: str
        """

        self._description = description

    @property
    def version_header_name(self):
        """Gets the version_header_name of this ApiVersionSetUpdateParametersProperties.

        Name of HTTP header parameter that indicates the API Version if versioningScheme is set to `header`.

        :return: The version_header_name of this ApiVersionSetUpdateParametersProperties.
        :rtype: str
        """
        return self._version_header_name

    @version_header_name.setter
    def version_header_name(self, version_header_name):
        """Sets the version_header_name of this ApiVersionSetUpdateParametersProperties.

        Name of HTTP header parameter that indicates the API Version if versioningScheme is set to `header`.

        :param version_header_name: The version_header_name of this ApiVersionSetUpdateParametersProperties.
        :type version_header_name: str
        """
        if version_header_name is not None and len(version_header_name) > 100:
            raise ValueError("Invalid value for `version_header_name`, length must be less than or equal to `100`")
        if version_header_name is not None and len(version_header_name) < 1:
            raise ValueError("Invalid value for `version_header_name`, length must be greater than or equal to `1`")

        self._version_header_name = version_header_name

    @property
    def version_query_name(self):
        """Gets the version_query_name of this ApiVersionSetUpdateParametersProperties.

        Name of query parameter that indicates the API Version if versioningScheme is set to `query`.

        :return: The version_query_name of this ApiVersionSetUpdateParametersProperties.
        :rtype: str
        """
        return self._version_query_name

    @version_query_name.setter
    def version_query_name(self, version_query_name):
        """Sets the version_query_name of this ApiVersionSetUpdateParametersProperties.

        Name of query parameter that indicates the API Version if versioningScheme is set to `query`.

        :param version_query_name: The version_query_name of this ApiVersionSetUpdateParametersProperties.
        :type version_query_name: str
        """
        if version_query_name is not None and len(version_query_name) > 100:
            raise ValueError("Invalid value for `version_query_name`, length must be less than or equal to `100`")
        if version_query_name is not None and len(version_query_name) < 1:
            raise ValueError("Invalid value for `version_query_name`, length must be greater than or equal to `1`")

        self._version_query_name = version_query_name
