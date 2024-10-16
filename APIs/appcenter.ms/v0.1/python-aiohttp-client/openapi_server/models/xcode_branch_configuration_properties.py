# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.branch_configurations_get200_response_all_of_toolsets_xcode_app_extension_provisioning_profile_files_inner import BranchConfigurationsGet200ResponseAllOfToolsetsXcodeAppExtensionProvisioningProfileFilesInner
from openapi_server import util


class XcodeBranchConfigurationProperties(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, app_extension_provisioning_profile_files: List[BranchConfigurationsGet200ResponseAllOfToolsetsXcodeAppExtensionProvisioningProfileFilesInner]=None, archive_configuration: str=None, automatic_signing: bool=None, cartfile_path: str=None, certificate_encoded: str=None, certificate_file_id: str=None, certificate_filename: str=None, certificate_password: str=None, certificate_upload_id: str=None, force_legacy_build_system: bool=None, podfile_path: str=None, project_or_workspace_path: str=None, provisioning_profile_encoded: str=None, provisioning_profile_file_id: str=None, provisioning_profile_filename: str=None, provisioning_profile_upload_id: str=None, scheme: str=None, target_to_archive: str=None, team_id: str=None, xcode_project_sha: str=None, xcode_version: str=None):
        """XcodeBranchConfigurationProperties - a model defined in OpenAPI

        :param app_extension_provisioning_profile_files: The app_extension_provisioning_profile_files of this XcodeBranchConfigurationProperties.
        :param archive_configuration: The archive_configuration of this XcodeBranchConfigurationProperties.
        :param automatic_signing: The automatic_signing of this XcodeBranchConfigurationProperties.
        :param cartfile_path: The cartfile_path of this XcodeBranchConfigurationProperties.
        :param certificate_encoded: The certificate_encoded of this XcodeBranchConfigurationProperties.
        :param certificate_file_id: The certificate_file_id of this XcodeBranchConfigurationProperties.
        :param certificate_filename: The certificate_filename of this XcodeBranchConfigurationProperties.
        :param certificate_password: The certificate_password of this XcodeBranchConfigurationProperties.
        :param certificate_upload_id: The certificate_upload_id of this XcodeBranchConfigurationProperties.
        :param force_legacy_build_system: The force_legacy_build_system of this XcodeBranchConfigurationProperties.
        :param podfile_path: The podfile_path of this XcodeBranchConfigurationProperties.
        :param project_or_workspace_path: The project_or_workspace_path of this XcodeBranchConfigurationProperties.
        :param provisioning_profile_encoded: The provisioning_profile_encoded of this XcodeBranchConfigurationProperties.
        :param provisioning_profile_file_id: The provisioning_profile_file_id of this XcodeBranchConfigurationProperties.
        :param provisioning_profile_filename: The provisioning_profile_filename of this XcodeBranchConfigurationProperties.
        :param provisioning_profile_upload_id: The provisioning_profile_upload_id of this XcodeBranchConfigurationProperties.
        :param scheme: The scheme of this XcodeBranchConfigurationProperties.
        :param target_to_archive: The target_to_archive of this XcodeBranchConfigurationProperties.
        :param team_id: The team_id of this XcodeBranchConfigurationProperties.
        :param xcode_project_sha: The xcode_project_sha of this XcodeBranchConfigurationProperties.
        :param xcode_version: The xcode_version of this XcodeBranchConfigurationProperties.
        """
        self.openapi_types = {
            'app_extension_provisioning_profile_files': List[BranchConfigurationsGet200ResponseAllOfToolsetsXcodeAppExtensionProvisioningProfileFilesInner],
            'archive_configuration': str,
            'automatic_signing': bool,
            'cartfile_path': str,
            'certificate_encoded': str,
            'certificate_file_id': str,
            'certificate_filename': str,
            'certificate_password': str,
            'certificate_upload_id': str,
            'force_legacy_build_system': bool,
            'podfile_path': str,
            'project_or_workspace_path': str,
            'provisioning_profile_encoded': str,
            'provisioning_profile_file_id': str,
            'provisioning_profile_filename': str,
            'provisioning_profile_upload_id': str,
            'scheme': str,
            'target_to_archive': str,
            'team_id': str,
            'xcode_project_sha': str,
            'xcode_version': str
        }

        self.attribute_map = {
            'app_extension_provisioning_profile_files': 'appExtensionProvisioningProfileFiles',
            'archive_configuration': 'archiveConfiguration',
            'automatic_signing': 'automaticSigning',
            'cartfile_path': 'cartfilePath',
            'certificate_encoded': 'certificateEncoded',
            'certificate_file_id': 'certificateFileId',
            'certificate_filename': 'certificateFilename',
            'certificate_password': 'certificatePassword',
            'certificate_upload_id': 'certificateUploadId',
            'force_legacy_build_system': 'forceLegacyBuildSystem',
            'podfile_path': 'podfilePath',
            'project_or_workspace_path': 'projectOrWorkspacePath',
            'provisioning_profile_encoded': 'provisioningProfileEncoded',
            'provisioning_profile_file_id': 'provisioningProfileFileId',
            'provisioning_profile_filename': 'provisioningProfileFilename',
            'provisioning_profile_upload_id': 'provisioningProfileUploadId',
            'scheme': 'scheme',
            'target_to_archive': 'targetToArchive',
            'team_id': 'teamId',
            'xcode_project_sha': 'xcodeProjectSha',
            'xcode_version': 'xcodeVersion'
        }

        self._app_extension_provisioning_profile_files = app_extension_provisioning_profile_files
        self._archive_configuration = archive_configuration
        self._automatic_signing = automatic_signing
        self._cartfile_path = cartfile_path
        self._certificate_encoded = certificate_encoded
        self._certificate_file_id = certificate_file_id
        self._certificate_filename = certificate_filename
        self._certificate_password = certificate_password
        self._certificate_upload_id = certificate_upload_id
        self._force_legacy_build_system = force_legacy_build_system
        self._podfile_path = podfile_path
        self._project_or_workspace_path = project_or_workspace_path
        self._provisioning_profile_encoded = provisioning_profile_encoded
        self._provisioning_profile_file_id = provisioning_profile_file_id
        self._provisioning_profile_filename = provisioning_profile_filename
        self._provisioning_profile_upload_id = provisioning_profile_upload_id
        self._scheme = scheme
        self._target_to_archive = target_to_archive
        self._team_id = team_id
        self._xcode_project_sha = xcode_project_sha
        self._xcode_version = xcode_version

    @classmethod
    def from_dict(cls, dikt: dict) -> 'XcodeBranchConfigurationProperties':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The XcodeBranchConfigurationProperties of this XcodeBranchConfigurationProperties.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def app_extension_provisioning_profile_files(self):
        """Gets the app_extension_provisioning_profile_files of this XcodeBranchConfigurationProperties.


        :return: The app_extension_provisioning_profile_files of this XcodeBranchConfigurationProperties.
        :rtype: List[BranchConfigurationsGet200ResponseAllOfToolsetsXcodeAppExtensionProvisioningProfileFilesInner]
        """
        return self._app_extension_provisioning_profile_files

    @app_extension_provisioning_profile_files.setter
    def app_extension_provisioning_profile_files(self, app_extension_provisioning_profile_files):
        """Sets the app_extension_provisioning_profile_files of this XcodeBranchConfigurationProperties.


        :param app_extension_provisioning_profile_files: The app_extension_provisioning_profile_files of this XcodeBranchConfigurationProperties.
        :type app_extension_provisioning_profile_files: List[BranchConfigurationsGet200ResponseAllOfToolsetsXcodeAppExtensionProvisioningProfileFilesInner]
        """

        self._app_extension_provisioning_profile_files = app_extension_provisioning_profile_files

    @property
    def archive_configuration(self):
        """Gets the archive_configuration of this XcodeBranchConfigurationProperties.

        The build configuration of the target to archive

        :return: The archive_configuration of this XcodeBranchConfigurationProperties.
        :rtype: str
        """
        return self._archive_configuration

    @archive_configuration.setter
    def archive_configuration(self, archive_configuration):
        """Sets the archive_configuration of this XcodeBranchConfigurationProperties.

        The build configuration of the target to archive

        :param archive_configuration: The archive_configuration of this XcodeBranchConfigurationProperties.
        :type archive_configuration: str
        """

        self._archive_configuration = archive_configuration

    @property
    def automatic_signing(self):
        """Gets the automatic_signing of this XcodeBranchConfigurationProperties.


        :return: The automatic_signing of this XcodeBranchConfigurationProperties.
        :rtype: bool
        """
        return self._automatic_signing

    @automatic_signing.setter
    def automatic_signing(self, automatic_signing):
        """Sets the automatic_signing of this XcodeBranchConfigurationProperties.


        :param automatic_signing: The automatic_signing of this XcodeBranchConfigurationProperties.
        :type automatic_signing: bool
        """

        self._automatic_signing = automatic_signing

    @property
    def cartfile_path(self):
        """Gets the cartfile_path of this XcodeBranchConfigurationProperties.

        Path to Carthage file, if present

        :return: The cartfile_path of this XcodeBranchConfigurationProperties.
        :rtype: str
        """
        return self._cartfile_path

    @cartfile_path.setter
    def cartfile_path(self, cartfile_path):
        """Sets the cartfile_path of this XcodeBranchConfigurationProperties.

        Path to Carthage file, if present

        :param cartfile_path: The cartfile_path of this XcodeBranchConfigurationProperties.
        :type cartfile_path: str
        """

        self._cartfile_path = cartfile_path

    @property
    def certificate_encoded(self):
        """Gets the certificate_encoded of this XcodeBranchConfigurationProperties.


        :return: The certificate_encoded of this XcodeBranchConfigurationProperties.
        :rtype: str
        """
        return self._certificate_encoded

    @certificate_encoded.setter
    def certificate_encoded(self, certificate_encoded):
        """Sets the certificate_encoded of this XcodeBranchConfigurationProperties.


        :param certificate_encoded: The certificate_encoded of this XcodeBranchConfigurationProperties.
        :type certificate_encoded: str
        """

        self._certificate_encoded = certificate_encoded

    @property
    def certificate_file_id(self):
        """Gets the certificate_file_id of this XcodeBranchConfigurationProperties.


        :return: The certificate_file_id of this XcodeBranchConfigurationProperties.
        :rtype: str
        """
        return self._certificate_file_id

    @certificate_file_id.setter
    def certificate_file_id(self, certificate_file_id):
        """Sets the certificate_file_id of this XcodeBranchConfigurationProperties.


        :param certificate_file_id: The certificate_file_id of this XcodeBranchConfigurationProperties.
        :type certificate_file_id: str
        """

        self._certificate_file_id = certificate_file_id

    @property
    def certificate_filename(self):
        """Gets the certificate_filename of this XcodeBranchConfigurationProperties.


        :return: The certificate_filename of this XcodeBranchConfigurationProperties.
        :rtype: str
        """
        return self._certificate_filename

    @certificate_filename.setter
    def certificate_filename(self, certificate_filename):
        """Sets the certificate_filename of this XcodeBranchConfigurationProperties.


        :param certificate_filename: The certificate_filename of this XcodeBranchConfigurationProperties.
        :type certificate_filename: str
        """

        self._certificate_filename = certificate_filename

    @property
    def certificate_password(self):
        """Gets the certificate_password of this XcodeBranchConfigurationProperties.


        :return: The certificate_password of this XcodeBranchConfigurationProperties.
        :rtype: str
        """
        return self._certificate_password

    @certificate_password.setter
    def certificate_password(self, certificate_password):
        """Sets the certificate_password of this XcodeBranchConfigurationProperties.


        :param certificate_password: The certificate_password of this XcodeBranchConfigurationProperties.
        :type certificate_password: str
        """

        self._certificate_password = certificate_password

    @property
    def certificate_upload_id(self):
        """Gets the certificate_upload_id of this XcodeBranchConfigurationProperties.


        :return: The certificate_upload_id of this XcodeBranchConfigurationProperties.
        :rtype: str
        """
        return self._certificate_upload_id

    @certificate_upload_id.setter
    def certificate_upload_id(self, certificate_upload_id):
        """Sets the certificate_upload_id of this XcodeBranchConfigurationProperties.


        :param certificate_upload_id: The certificate_upload_id of this XcodeBranchConfigurationProperties.
        :type certificate_upload_id: str
        """

        self._certificate_upload_id = certificate_upload_id

    @property
    def force_legacy_build_system(self):
        """Gets the force_legacy_build_system of this XcodeBranchConfigurationProperties.

        Setting this to true forces the build to use Xcode legacy build system. Otherwise, the setting from workspace settings is used. By default new build system is used if workspace setting is not committed to the repository. Only used for iOS React Native app, with Xcode 10. 

        :return: The force_legacy_build_system of this XcodeBranchConfigurationProperties.
        :rtype: bool
        """
        return self._force_legacy_build_system

    @force_legacy_build_system.setter
    def force_legacy_build_system(self, force_legacy_build_system):
        """Sets the force_legacy_build_system of this XcodeBranchConfigurationProperties.

        Setting this to true forces the build to use Xcode legacy build system. Otherwise, the setting from workspace settings is used. By default new build system is used if workspace setting is not committed to the repository. Only used for iOS React Native app, with Xcode 10. 

        :param force_legacy_build_system: The force_legacy_build_system of this XcodeBranchConfigurationProperties.
        :type force_legacy_build_system: bool
        """

        self._force_legacy_build_system = force_legacy_build_system

    @property
    def podfile_path(self):
        """Gets the podfile_path of this XcodeBranchConfigurationProperties.

        Path to CococaPods file, if present

        :return: The podfile_path of this XcodeBranchConfigurationProperties.
        :rtype: str
        """
        return self._podfile_path

    @podfile_path.setter
    def podfile_path(self, podfile_path):
        """Sets the podfile_path of this XcodeBranchConfigurationProperties.

        Path to CococaPods file, if present

        :param podfile_path: The podfile_path of this XcodeBranchConfigurationProperties.
        :type podfile_path: str
        """

        self._podfile_path = podfile_path

    @property
    def project_or_workspace_path(self):
        """Gets the project_or_workspace_path of this XcodeBranchConfigurationProperties.

        Xcode project/workspace path

        :return: The project_or_workspace_path of this XcodeBranchConfigurationProperties.
        :rtype: str
        """
        return self._project_or_workspace_path

    @project_or_workspace_path.setter
    def project_or_workspace_path(self, project_or_workspace_path):
        """Sets the project_or_workspace_path of this XcodeBranchConfigurationProperties.

        Xcode project/workspace path

        :param project_or_workspace_path: The project_or_workspace_path of this XcodeBranchConfigurationProperties.
        :type project_or_workspace_path: str
        """

        self._project_or_workspace_path = project_or_workspace_path

    @property
    def provisioning_profile_encoded(self):
        """Gets the provisioning_profile_encoded of this XcodeBranchConfigurationProperties.


        :return: The provisioning_profile_encoded of this XcodeBranchConfigurationProperties.
        :rtype: str
        """
        return self._provisioning_profile_encoded

    @provisioning_profile_encoded.setter
    def provisioning_profile_encoded(self, provisioning_profile_encoded):
        """Sets the provisioning_profile_encoded of this XcodeBranchConfigurationProperties.


        :param provisioning_profile_encoded: The provisioning_profile_encoded of this XcodeBranchConfigurationProperties.
        :type provisioning_profile_encoded: str
        """

        self._provisioning_profile_encoded = provisioning_profile_encoded

    @property
    def provisioning_profile_file_id(self):
        """Gets the provisioning_profile_file_id of this XcodeBranchConfigurationProperties.


        :return: The provisioning_profile_file_id of this XcodeBranchConfigurationProperties.
        :rtype: str
        """
        return self._provisioning_profile_file_id

    @provisioning_profile_file_id.setter
    def provisioning_profile_file_id(self, provisioning_profile_file_id):
        """Sets the provisioning_profile_file_id of this XcodeBranchConfigurationProperties.


        :param provisioning_profile_file_id: The provisioning_profile_file_id of this XcodeBranchConfigurationProperties.
        :type provisioning_profile_file_id: str
        """

        self._provisioning_profile_file_id = provisioning_profile_file_id

    @property
    def provisioning_profile_filename(self):
        """Gets the provisioning_profile_filename of this XcodeBranchConfigurationProperties.


        :return: The provisioning_profile_filename of this XcodeBranchConfigurationProperties.
        :rtype: str
        """
        return self._provisioning_profile_filename

    @provisioning_profile_filename.setter
    def provisioning_profile_filename(self, provisioning_profile_filename):
        """Sets the provisioning_profile_filename of this XcodeBranchConfigurationProperties.


        :param provisioning_profile_filename: The provisioning_profile_filename of this XcodeBranchConfigurationProperties.
        :type provisioning_profile_filename: str
        """

        self._provisioning_profile_filename = provisioning_profile_filename

    @property
    def provisioning_profile_upload_id(self):
        """Gets the provisioning_profile_upload_id of this XcodeBranchConfigurationProperties.


        :return: The provisioning_profile_upload_id of this XcodeBranchConfigurationProperties.
        :rtype: str
        """
        return self._provisioning_profile_upload_id

    @provisioning_profile_upload_id.setter
    def provisioning_profile_upload_id(self, provisioning_profile_upload_id):
        """Sets the provisioning_profile_upload_id of this XcodeBranchConfigurationProperties.


        :param provisioning_profile_upload_id: The provisioning_profile_upload_id of this XcodeBranchConfigurationProperties.
        :type provisioning_profile_upload_id: str
        """

        self._provisioning_profile_upload_id = provisioning_profile_upload_id

    @property
    def scheme(self):
        """Gets the scheme of this XcodeBranchConfigurationProperties.


        :return: The scheme of this XcodeBranchConfigurationProperties.
        :rtype: str
        """
        return self._scheme

    @scheme.setter
    def scheme(self, scheme):
        """Sets the scheme of this XcodeBranchConfigurationProperties.


        :param scheme: The scheme of this XcodeBranchConfigurationProperties.
        :type scheme: str
        """

        self._scheme = scheme

    @property
    def target_to_archive(self):
        """Gets the target_to_archive of this XcodeBranchConfigurationProperties.

        The target id of the selected scheme to archive

        :return: The target_to_archive of this XcodeBranchConfigurationProperties.
        :rtype: str
        """
        return self._target_to_archive

    @target_to_archive.setter
    def target_to_archive(self, target_to_archive):
        """Sets the target_to_archive of this XcodeBranchConfigurationProperties.

        The target id of the selected scheme to archive

        :param target_to_archive: The target_to_archive of this XcodeBranchConfigurationProperties.
        :type target_to_archive: str
        """

        self._target_to_archive = target_to_archive

    @property
    def team_id(self):
        """Gets the team_id of this XcodeBranchConfigurationProperties.


        :return: The team_id of this XcodeBranchConfigurationProperties.
        :rtype: str
        """
        return self._team_id

    @team_id.setter
    def team_id(self, team_id):
        """Sets the team_id of this XcodeBranchConfigurationProperties.


        :param team_id: The team_id of this XcodeBranchConfigurationProperties.
        :type team_id: str
        """

        self._team_id = team_id

    @property
    def xcode_project_sha(self):
        """Gets the xcode_project_sha of this XcodeBranchConfigurationProperties.

        The selected pbxproject hash to the repositroy

        :return: The xcode_project_sha of this XcodeBranchConfigurationProperties.
        :rtype: str
        """
        return self._xcode_project_sha

    @xcode_project_sha.setter
    def xcode_project_sha(self, xcode_project_sha):
        """Sets the xcode_project_sha of this XcodeBranchConfigurationProperties.

        The selected pbxproject hash to the repositroy

        :param xcode_project_sha: The xcode_project_sha of this XcodeBranchConfigurationProperties.
        :type xcode_project_sha: str
        """

        self._xcode_project_sha = xcode_project_sha

    @property
    def xcode_version(self):
        """Gets the xcode_version of this XcodeBranchConfigurationProperties.

        Xcode version used to build. Available versions can be found in \"/xcode_versions\" API. Default is latest stable version, at the time when the configuration is set.

        :return: The xcode_version of this XcodeBranchConfigurationProperties.
        :rtype: str
        """
        return self._xcode_version

    @xcode_version.setter
    def xcode_version(self, xcode_version):
        """Sets the xcode_version of this XcodeBranchConfigurationProperties.

        Xcode version used to build. Available versions can be found in \"/xcode_versions\" API. Default is latest stable version, at the time when the configuration is set.

        :param xcode_version: The xcode_version of this XcodeBranchConfigurationProperties.
        :type xcode_version: str
        """

        self._xcode_version = xcode_version
