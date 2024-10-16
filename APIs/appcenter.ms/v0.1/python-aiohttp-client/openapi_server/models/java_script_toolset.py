# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.builds_list_toolset_projects200_response_javascript_javascript_solutions_inner import BuildsListToolsetProjects200ResponseJavascriptJavascriptSolutionsInner
from openapi_server import util


class JavaScriptToolset(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, javascript_solutions: List[BuildsListToolsetProjects200ResponseJavascriptJavascriptSolutionsInner]=None, package_json_paths: List[str]=None):
        """JavaScriptToolset - a model defined in OpenAPI

        :param javascript_solutions: The javascript_solutions of this JavaScriptToolset.
        :param package_json_paths: The package_json_paths of this JavaScriptToolset.
        """
        self.openapi_types = {
            'javascript_solutions': List[BuildsListToolsetProjects200ResponseJavascriptJavascriptSolutionsInner],
            'package_json_paths': List[str]
        }

        self.attribute_map = {
            'javascript_solutions': 'javascriptSolutions',
            'package_json_paths': 'packageJsonPaths'
        }

        self._javascript_solutions = javascript_solutions
        self._package_json_paths = package_json_paths

    @classmethod
    def from_dict(cls, dikt: dict) -> 'JavaScriptToolset':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The JavaScriptToolset of this JavaScriptToolset.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def javascript_solutions(self):
        """Gets the javascript_solutions of this JavaScriptToolset.

        The React Native solutions detected

        :return: The javascript_solutions of this JavaScriptToolset.
        :rtype: List[BuildsListToolsetProjects200ResponseJavascriptJavascriptSolutionsInner]
        """
        return self._javascript_solutions

    @javascript_solutions.setter
    def javascript_solutions(self, javascript_solutions):
        """Sets the javascript_solutions of this JavaScriptToolset.

        The React Native solutions detected

        :param javascript_solutions: The javascript_solutions of this JavaScriptToolset.
        :type javascript_solutions: List[BuildsListToolsetProjects200ResponseJavascriptJavascriptSolutionsInner]
        """

        self._javascript_solutions = javascript_solutions

    @property
    def package_json_paths(self):
        """Gets the package_json_paths of this JavaScriptToolset.

        Paths for detected package.json files

        :return: The package_json_paths of this JavaScriptToolset.
        :rtype: List[str]
        """
        return self._package_json_paths

    @package_json_paths.setter
    def package_json_paths(self, package_json_paths):
        """Sets the package_json_paths of this JavaScriptToolset.

        Paths for detected package.json files

        :param package_json_paths: The package_json_paths of this JavaScriptToolset.
        :type package_json_paths: List[str]
        """
        if package_json_paths is None:
            raise ValueError("Invalid value for `package_json_paths`, must not be `None`")

        self._package_json_paths = package_json_paths
