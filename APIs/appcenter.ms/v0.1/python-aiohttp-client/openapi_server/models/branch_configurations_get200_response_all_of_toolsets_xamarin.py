# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class BranchConfigurationsGet200ResponseAllOfToolsetsXamarin(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, args: str=None, configuration: str=None, is_sim_build: bool=None, mono_version: str=None, p12_file: str=None, p12_pwd: str=None, prov_profile: str=None, sdk_bundle: str=None, sln_path: str=None, symlink: str=None):
        """BranchConfigurationsGet200ResponseAllOfToolsetsXamarin - a model defined in OpenAPI

        :param args: The args of this BranchConfigurationsGet200ResponseAllOfToolsetsXamarin.
        :param configuration: The configuration of this BranchConfigurationsGet200ResponseAllOfToolsetsXamarin.
        :param is_sim_build: The is_sim_build of this BranchConfigurationsGet200ResponseAllOfToolsetsXamarin.
        :param mono_version: The mono_version of this BranchConfigurationsGet200ResponseAllOfToolsetsXamarin.
        :param p12_file: The p12_file of this BranchConfigurationsGet200ResponseAllOfToolsetsXamarin.
        :param p12_pwd: The p12_pwd of this BranchConfigurationsGet200ResponseAllOfToolsetsXamarin.
        :param prov_profile: The prov_profile of this BranchConfigurationsGet200ResponseAllOfToolsetsXamarin.
        :param sdk_bundle: The sdk_bundle of this BranchConfigurationsGet200ResponseAllOfToolsetsXamarin.
        :param sln_path: The sln_path of this BranchConfigurationsGet200ResponseAllOfToolsetsXamarin.
        :param symlink: The symlink of this BranchConfigurationsGet200ResponseAllOfToolsetsXamarin.
        """
        self.openapi_types = {
            'args': str,
            'configuration': str,
            'is_sim_build': bool,
            'mono_version': str,
            'p12_file': str,
            'p12_pwd': str,
            'prov_profile': str,
            'sdk_bundle': str,
            'sln_path': str,
            'symlink': str
        }

        self.attribute_map = {
            'args': 'args',
            'configuration': 'configuration',
            'is_sim_build': 'isSimBuild',
            'mono_version': 'monoVersion',
            'p12_file': 'p12File',
            'p12_pwd': 'p12Pwd',
            'prov_profile': 'provProfile',
            'sdk_bundle': 'sdkBundle',
            'sln_path': 'slnPath',
            'symlink': 'symlink'
        }

        self._args = args
        self._configuration = configuration
        self._is_sim_build = is_sim_build
        self._mono_version = mono_version
        self._p12_file = p12_file
        self._p12_pwd = p12_pwd
        self._prov_profile = prov_profile
        self._sdk_bundle = sdk_bundle
        self._sln_path = sln_path
        self._symlink = symlink

    @classmethod
    def from_dict(cls, dikt: dict) -> 'BranchConfigurationsGet200ResponseAllOfToolsetsXamarin':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The branchConfigurations_get_200_response_allOf_toolsets_xamarin of this BranchConfigurationsGet200ResponseAllOfToolsetsXamarin.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def args(self):
        """Gets the args of this BranchConfigurationsGet200ResponseAllOfToolsetsXamarin.


        :return: The args of this BranchConfigurationsGet200ResponseAllOfToolsetsXamarin.
        :rtype: str
        """
        return self._args

    @args.setter
    def args(self, args):
        """Sets the args of this BranchConfigurationsGet200ResponseAllOfToolsetsXamarin.


        :param args: The args of this BranchConfigurationsGet200ResponseAllOfToolsetsXamarin.
        :type args: str
        """

        self._args = args

    @property
    def configuration(self):
        """Gets the configuration of this BranchConfigurationsGet200ResponseAllOfToolsetsXamarin.


        :return: The configuration of this BranchConfigurationsGet200ResponseAllOfToolsetsXamarin.
        :rtype: str
        """
        return self._configuration

    @configuration.setter
    def configuration(self, configuration):
        """Sets the configuration of this BranchConfigurationsGet200ResponseAllOfToolsetsXamarin.


        :param configuration: The configuration of this BranchConfigurationsGet200ResponseAllOfToolsetsXamarin.
        :type configuration: str
        """

        self._configuration = configuration

    @property
    def is_sim_build(self):
        """Gets the is_sim_build of this BranchConfigurationsGet200ResponseAllOfToolsetsXamarin.


        :return: The is_sim_build of this BranchConfigurationsGet200ResponseAllOfToolsetsXamarin.
        :rtype: bool
        """
        return self._is_sim_build

    @is_sim_build.setter
    def is_sim_build(self, is_sim_build):
        """Sets the is_sim_build of this BranchConfigurationsGet200ResponseAllOfToolsetsXamarin.


        :param is_sim_build: The is_sim_build of this BranchConfigurationsGet200ResponseAllOfToolsetsXamarin.
        :type is_sim_build: bool
        """

        self._is_sim_build = is_sim_build

    @property
    def mono_version(self):
        """Gets the mono_version of this BranchConfigurationsGet200ResponseAllOfToolsetsXamarin.


        :return: The mono_version of this BranchConfigurationsGet200ResponseAllOfToolsetsXamarin.
        :rtype: str
        """
        return self._mono_version

    @mono_version.setter
    def mono_version(self, mono_version):
        """Sets the mono_version of this BranchConfigurationsGet200ResponseAllOfToolsetsXamarin.


        :param mono_version: The mono_version of this BranchConfigurationsGet200ResponseAllOfToolsetsXamarin.
        :type mono_version: str
        """

        self._mono_version = mono_version

    @property
    def p12_file(self):
        """Gets the p12_file of this BranchConfigurationsGet200ResponseAllOfToolsetsXamarin.


        :return: The p12_file of this BranchConfigurationsGet200ResponseAllOfToolsetsXamarin.
        :rtype: str
        """
        return self._p12_file

    @p12_file.setter
    def p12_file(self, p12_file):
        """Sets the p12_file of this BranchConfigurationsGet200ResponseAllOfToolsetsXamarin.


        :param p12_file: The p12_file of this BranchConfigurationsGet200ResponseAllOfToolsetsXamarin.
        :type p12_file: str
        """

        self._p12_file = p12_file

    @property
    def p12_pwd(self):
        """Gets the p12_pwd of this BranchConfigurationsGet200ResponseAllOfToolsetsXamarin.


        :return: The p12_pwd of this BranchConfigurationsGet200ResponseAllOfToolsetsXamarin.
        :rtype: str
        """
        return self._p12_pwd

    @p12_pwd.setter
    def p12_pwd(self, p12_pwd):
        """Sets the p12_pwd of this BranchConfigurationsGet200ResponseAllOfToolsetsXamarin.


        :param p12_pwd: The p12_pwd of this BranchConfigurationsGet200ResponseAllOfToolsetsXamarin.
        :type p12_pwd: str
        """

        self._p12_pwd = p12_pwd

    @property
    def prov_profile(self):
        """Gets the prov_profile of this BranchConfigurationsGet200ResponseAllOfToolsetsXamarin.


        :return: The prov_profile of this BranchConfigurationsGet200ResponseAllOfToolsetsXamarin.
        :rtype: str
        """
        return self._prov_profile

    @prov_profile.setter
    def prov_profile(self, prov_profile):
        """Sets the prov_profile of this BranchConfigurationsGet200ResponseAllOfToolsetsXamarin.


        :param prov_profile: The prov_profile of this BranchConfigurationsGet200ResponseAllOfToolsetsXamarin.
        :type prov_profile: str
        """

        self._prov_profile = prov_profile

    @property
    def sdk_bundle(self):
        """Gets the sdk_bundle of this BranchConfigurationsGet200ResponseAllOfToolsetsXamarin.


        :return: The sdk_bundle of this BranchConfigurationsGet200ResponseAllOfToolsetsXamarin.
        :rtype: str
        """
        return self._sdk_bundle

    @sdk_bundle.setter
    def sdk_bundle(self, sdk_bundle):
        """Sets the sdk_bundle of this BranchConfigurationsGet200ResponseAllOfToolsetsXamarin.


        :param sdk_bundle: The sdk_bundle of this BranchConfigurationsGet200ResponseAllOfToolsetsXamarin.
        :type sdk_bundle: str
        """

        self._sdk_bundle = sdk_bundle

    @property
    def sln_path(self):
        """Gets the sln_path of this BranchConfigurationsGet200ResponseAllOfToolsetsXamarin.


        :return: The sln_path of this BranchConfigurationsGet200ResponseAllOfToolsetsXamarin.
        :rtype: str
        """
        return self._sln_path

    @sln_path.setter
    def sln_path(self, sln_path):
        """Sets the sln_path of this BranchConfigurationsGet200ResponseAllOfToolsetsXamarin.


        :param sln_path: The sln_path of this BranchConfigurationsGet200ResponseAllOfToolsetsXamarin.
        :type sln_path: str
        """

        self._sln_path = sln_path

    @property
    def symlink(self):
        """Gets the symlink of this BranchConfigurationsGet200ResponseAllOfToolsetsXamarin.

        Symlink of the SDK Bundle and Mono installation. The build will use the associated Mono bundled with related Xamarin SDK. If both symlink and monoVersion or sdkBundle are passed, the symlink is taking precedence. If non-existing symlink is passed, the current stable Mono version will be configured for building. 

        :return: The symlink of this BranchConfigurationsGet200ResponseAllOfToolsetsXamarin.
        :rtype: str
        """
        return self._symlink

    @symlink.setter
    def symlink(self, symlink):
        """Sets the symlink of this BranchConfigurationsGet200ResponseAllOfToolsetsXamarin.

        Symlink of the SDK Bundle and Mono installation. The build will use the associated Mono bundled with related Xamarin SDK. If both symlink and monoVersion or sdkBundle are passed, the symlink is taking precedence. If non-existing symlink is passed, the current stable Mono version will be configured for building. 

        :param symlink: The symlink of this BranchConfigurationsGet200ResponseAllOfToolsetsXamarin.
        :type symlink: str
        """

        self._symlink = symlink
