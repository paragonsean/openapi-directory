# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.add_new_integration_request_any_of_credentials_one_of import AddNewIntegrationRequestAnyOfCredentialsOneOf
from openapi_server.models.add_new_integration_request_any_of_credentials_one_of1 import AddNewIntegrationRequestAnyOfCredentialsOneOf1
from openapi_server.models.add_new_integration_request_any_of_credentials_one_of10 import AddNewIntegrationRequestAnyOfCredentialsOneOf10
from openapi_server.models.add_new_integration_request_any_of_credentials_one_of10_git_hub_cr_credentials import AddNewIntegrationRequestAnyOfCredentialsOneOf10GitHubCrCredentials
from openapi_server.models.add_new_integration_request_any_of_credentials_one_of11 import AddNewIntegrationRequestAnyOfCredentialsOneOf11
from openapi_server.models.add_new_integration_request_any_of_credentials_one_of11_git_hub_enterprise_credentials import AddNewIntegrationRequestAnyOfCredentialsOneOf11GitHubEnterpriseCredentials
from openapi_server.models.add_new_integration_request_any_of_credentials_one_of12 import AddNewIntegrationRequestAnyOfCredentialsOneOf12
from openapi_server.models.add_new_integration_request_any_of_credentials_one_of12_git_lab_credentials import AddNewIntegrationRequestAnyOfCredentialsOneOf12GitLabCredentials
from openapi_server.models.add_new_integration_request_any_of_credentials_one_of13 import AddNewIntegrationRequestAnyOfCredentialsOneOf13
from openapi_server.models.add_new_integration_request_any_of_credentials_one_of13_git_lab_cr_credentials import AddNewIntegrationRequestAnyOfCredentialsOneOf13GitLabCrCredentials
from openapi_server.models.add_new_integration_request_any_of_credentials_one_of14 import AddNewIntegrationRequestAnyOfCredentialsOneOf14
from openapi_server.models.add_new_integration_request_any_of_credentials_one_of14_google_artifact_cr_credentials import AddNewIntegrationRequestAnyOfCredentialsOneOf14GoogleArtifactCrCredentials
from openapi_server.models.add_new_integration_request_any_of_credentials_one_of15 import AddNewIntegrationRequestAnyOfCredentialsOneOf15
from openapi_server.models.add_new_integration_request_any_of_credentials_one_of15_harbor_cr_credentials import AddNewIntegrationRequestAnyOfCredentialsOneOf15HarborCrCredentials
from openapi_server.models.add_new_integration_request_any_of_credentials_one_of16 import AddNewIntegrationRequestAnyOfCredentialsOneOf16
from openapi_server.models.add_new_integration_request_any_of_credentials_one_of16_nexus_cr_credentials import AddNewIntegrationRequestAnyOfCredentialsOneOf16NexusCrCredentials
from openapi_server.models.add_new_integration_request_any_of_credentials_one_of17 import AddNewIntegrationRequestAnyOfCredentialsOneOf17
from openapi_server.models.add_new_integration_request_any_of_credentials_one_of17_quay_cr_credentials import AddNewIntegrationRequestAnyOfCredentialsOneOf17QuayCrCredentials
from openapi_server.models.add_new_integration_request_any_of_credentials_one_of1_artifactory_cr_credentials import AddNewIntegrationRequestAnyOfCredentialsOneOf1ArtifactoryCrCredentials
from openapi_server.models.add_new_integration_request_any_of_credentials_one_of2 import AddNewIntegrationRequestAnyOfCredentialsOneOf2
from openapi_server.models.add_new_integration_request_any_of_credentials_one_of2_azure_repos_credentials import AddNewIntegrationRequestAnyOfCredentialsOneOf2AzureReposCredentials
from openapi_server.models.add_new_integration_request_any_of_credentials_one_of3 import AddNewIntegrationRequestAnyOfCredentialsOneOf3
from openapi_server.models.add_new_integration_request_any_of_credentials_one_of3_bitbucket_cloud_credentials import AddNewIntegrationRequestAnyOfCredentialsOneOf3BitbucketCloudCredentials
from openapi_server.models.add_new_integration_request_any_of_credentials_one_of4 import AddNewIntegrationRequestAnyOfCredentialsOneOf4
from openapi_server.models.add_new_integration_request_any_of_credentials_one_of4_bitbucket_server_credentials import AddNewIntegrationRequestAnyOfCredentialsOneOf4BitbucketServerCredentials
from openapi_server.models.add_new_integration_request_any_of_credentials_one_of5 import AddNewIntegrationRequestAnyOfCredentialsOneOf5
from openapi_server.models.add_new_integration_request_any_of_credentials_one_of5_digital_ocean_cr_credentials import AddNewIntegrationRequestAnyOfCredentialsOneOf5DigitalOceanCrCredentials
from openapi_server.models.add_new_integration_request_any_of_credentials_one_of6 import AddNewIntegrationRequestAnyOfCredentialsOneOf6
from openapi_server.models.add_new_integration_request_any_of_credentials_one_of6_docker_hub_credentials import AddNewIntegrationRequestAnyOfCredentialsOneOf6DockerHubCredentials
from openapi_server.models.add_new_integration_request_any_of_credentials_one_of7 import AddNewIntegrationRequestAnyOfCredentialsOneOf7
from openapi_server.models.add_new_integration_request_any_of_credentials_one_of7_ecr_credentials import AddNewIntegrationRequestAnyOfCredentialsOneOf7EcrCredentials
from openapi_server.models.add_new_integration_request_any_of_credentials_one_of8 import AddNewIntegrationRequestAnyOfCredentialsOneOf8
from openapi_server.models.add_new_integration_request_any_of_credentials_one_of8_gcr_credentials import AddNewIntegrationRequestAnyOfCredentialsOneOf8GcrCredentials
from openapi_server.models.add_new_integration_request_any_of_credentials_one_of9 import AddNewIntegrationRequestAnyOfCredentialsOneOf9
from openapi_server.models.add_new_integration_request_any_of_credentials_one_of9_git_hub_credentials import AddNewIntegrationRequestAnyOfCredentialsOneOf9GitHubCredentials
from openapi_server.models.add_new_integration_request_any_of_credentials_one_of_acr_credentials import AddNewIntegrationRequestAnyOfCredentialsOneOfAcrCredentials
from openapi_server import util


class AddNewIntegrationRequestAnyOfCredentials(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, acr_credentials: AddNewIntegrationRequestAnyOfCredentialsOneOfAcrCredentials=None, artifactory_cr_credentials: AddNewIntegrationRequestAnyOfCredentialsOneOf1ArtifactoryCrCredentials=None, azure_repos_credentials: AddNewIntegrationRequestAnyOfCredentialsOneOf2AzureReposCredentials=None, bitbucket_cloud_credentials: AddNewIntegrationRequestAnyOfCredentialsOneOf3BitbucketCloudCredentials=None, bitbucket_server_credentials: AddNewIntegrationRequestAnyOfCredentialsOneOf4BitbucketServerCredentials=None, digital_ocean_cr_credentials: AddNewIntegrationRequestAnyOfCredentialsOneOf5DigitalOceanCrCredentials=None, docker_hub_credentials: AddNewIntegrationRequestAnyOfCredentialsOneOf6DockerHubCredentials=None, ecr_credentials: AddNewIntegrationRequestAnyOfCredentialsOneOf7EcrCredentials=None, gcr_credentials: AddNewIntegrationRequestAnyOfCredentialsOneOf8GcrCredentials=None, git_hub_credentials: AddNewIntegrationRequestAnyOfCredentialsOneOf9GitHubCredentials=None, git_hub_cr_credentials: AddNewIntegrationRequestAnyOfCredentialsOneOf10GitHubCrCredentials=None, git_hub_enterprise_credentials: AddNewIntegrationRequestAnyOfCredentialsOneOf11GitHubEnterpriseCredentials=None, git_lab_credentials: AddNewIntegrationRequestAnyOfCredentialsOneOf12GitLabCredentials=None, git_lab_cr_credentials: AddNewIntegrationRequestAnyOfCredentialsOneOf13GitLabCrCredentials=None, google_artifact_cr_credentials: AddNewIntegrationRequestAnyOfCredentialsOneOf14GoogleArtifactCrCredentials=None, harbor_cr_credentials: AddNewIntegrationRequestAnyOfCredentialsOneOf15HarborCrCredentials=None, nexus_cr_credentials: AddNewIntegrationRequestAnyOfCredentialsOneOf16NexusCrCredentials=None, quay_cr_credentials: AddNewIntegrationRequestAnyOfCredentialsOneOf17QuayCrCredentials=None):
        """AddNewIntegrationRequestAnyOfCredentials - a model defined in OpenAPI

        :param acr_credentials: The acr_credentials of this AddNewIntegrationRequestAnyOfCredentials.
        :param artifactory_cr_credentials: The artifactory_cr_credentials of this AddNewIntegrationRequestAnyOfCredentials.
        :param azure_repos_credentials: The azure_repos_credentials of this AddNewIntegrationRequestAnyOfCredentials.
        :param bitbucket_cloud_credentials: The bitbucket_cloud_credentials of this AddNewIntegrationRequestAnyOfCredentials.
        :param bitbucket_server_credentials: The bitbucket_server_credentials of this AddNewIntegrationRequestAnyOfCredentials.
        :param digital_ocean_cr_credentials: The digital_ocean_cr_credentials of this AddNewIntegrationRequestAnyOfCredentials.
        :param docker_hub_credentials: The docker_hub_credentials of this AddNewIntegrationRequestAnyOfCredentials.
        :param ecr_credentials: The ecr_credentials of this AddNewIntegrationRequestAnyOfCredentials.
        :param gcr_credentials: The gcr_credentials of this AddNewIntegrationRequestAnyOfCredentials.
        :param git_hub_credentials: The git_hub_credentials of this AddNewIntegrationRequestAnyOfCredentials.
        :param git_hub_cr_credentials: The git_hub_cr_credentials of this AddNewIntegrationRequestAnyOfCredentials.
        :param git_hub_enterprise_credentials: The git_hub_enterprise_credentials of this AddNewIntegrationRequestAnyOfCredentials.
        :param git_lab_credentials: The git_lab_credentials of this AddNewIntegrationRequestAnyOfCredentials.
        :param git_lab_cr_credentials: The git_lab_cr_credentials of this AddNewIntegrationRequestAnyOfCredentials.
        :param google_artifact_cr_credentials: The google_artifact_cr_credentials of this AddNewIntegrationRequestAnyOfCredentials.
        :param harbor_cr_credentials: The harbor_cr_credentials of this AddNewIntegrationRequestAnyOfCredentials.
        :param nexus_cr_credentials: The nexus_cr_credentials of this AddNewIntegrationRequestAnyOfCredentials.
        :param quay_cr_credentials: The quay_cr_credentials of this AddNewIntegrationRequestAnyOfCredentials.
        """
        self.openapi_types = {
            'acr_credentials': AddNewIntegrationRequestAnyOfCredentialsOneOfAcrCredentials,
            'artifactory_cr_credentials': AddNewIntegrationRequestAnyOfCredentialsOneOf1ArtifactoryCrCredentials,
            'azure_repos_credentials': AddNewIntegrationRequestAnyOfCredentialsOneOf2AzureReposCredentials,
            'bitbucket_cloud_credentials': AddNewIntegrationRequestAnyOfCredentialsOneOf3BitbucketCloudCredentials,
            'bitbucket_server_credentials': AddNewIntegrationRequestAnyOfCredentialsOneOf4BitbucketServerCredentials,
            'digital_ocean_cr_credentials': AddNewIntegrationRequestAnyOfCredentialsOneOf5DigitalOceanCrCredentials,
            'docker_hub_credentials': AddNewIntegrationRequestAnyOfCredentialsOneOf6DockerHubCredentials,
            'ecr_credentials': AddNewIntegrationRequestAnyOfCredentialsOneOf7EcrCredentials,
            'gcr_credentials': AddNewIntegrationRequestAnyOfCredentialsOneOf8GcrCredentials,
            'git_hub_credentials': AddNewIntegrationRequestAnyOfCredentialsOneOf9GitHubCredentials,
            'git_hub_cr_credentials': AddNewIntegrationRequestAnyOfCredentialsOneOf10GitHubCrCredentials,
            'git_hub_enterprise_credentials': AddNewIntegrationRequestAnyOfCredentialsOneOf11GitHubEnterpriseCredentials,
            'git_lab_credentials': AddNewIntegrationRequestAnyOfCredentialsOneOf12GitLabCredentials,
            'git_lab_cr_credentials': AddNewIntegrationRequestAnyOfCredentialsOneOf13GitLabCrCredentials,
            'google_artifact_cr_credentials': AddNewIntegrationRequestAnyOfCredentialsOneOf14GoogleArtifactCrCredentials,
            'harbor_cr_credentials': AddNewIntegrationRequestAnyOfCredentialsOneOf15HarborCrCredentials,
            'nexus_cr_credentials': AddNewIntegrationRequestAnyOfCredentialsOneOf16NexusCrCredentials,
            'quay_cr_credentials': AddNewIntegrationRequestAnyOfCredentialsOneOf17QuayCrCredentials
        }

        self.attribute_map = {
            'acr_credentials': 'AcrCredentials',
            'artifactory_cr_credentials': 'ArtifactoryCrCredentials',
            'azure_repos_credentials': 'AzureReposCredentials',
            'bitbucket_cloud_credentials': 'BitbucketCloudCredentials',
            'bitbucket_server_credentials': 'BitbucketServerCredentials',
            'digital_ocean_cr_credentials': 'DigitalOceanCrCredentials',
            'docker_hub_credentials': 'DockerHubCredentials',
            'ecr_credentials': 'EcrCredentials',
            'gcr_credentials': 'GcrCredentials',
            'git_hub_credentials': 'GitHubCredentials',
            'git_hub_cr_credentials': 'GitHubCrCredentials',
            'git_hub_enterprise_credentials': 'GitHubEnterpriseCredentials',
            'git_lab_credentials': 'GitLabCredentials',
            'git_lab_cr_credentials': 'GitLabCrCredentials',
            'google_artifact_cr_credentials': 'GoogleArtifactCrCredentials',
            'harbor_cr_credentials': 'HarborCrCredentials',
            'nexus_cr_credentials': 'NexusCrCredentials',
            'quay_cr_credentials': 'QuayCrCredentials'
        }

        self._acr_credentials = acr_credentials
        self._artifactory_cr_credentials = artifactory_cr_credentials
        self._azure_repos_credentials = azure_repos_credentials
        self._bitbucket_cloud_credentials = bitbucket_cloud_credentials
        self._bitbucket_server_credentials = bitbucket_server_credentials
        self._digital_ocean_cr_credentials = digital_ocean_cr_credentials
        self._docker_hub_credentials = docker_hub_credentials
        self._ecr_credentials = ecr_credentials
        self._gcr_credentials = gcr_credentials
        self._git_hub_credentials = git_hub_credentials
        self._git_hub_cr_credentials = git_hub_cr_credentials
        self._git_hub_enterprise_credentials = git_hub_enterprise_credentials
        self._git_lab_credentials = git_lab_credentials
        self._git_lab_cr_credentials = git_lab_cr_credentials
        self._google_artifact_cr_credentials = google_artifact_cr_credentials
        self._harbor_cr_credentials = harbor_cr_credentials
        self._nexus_cr_credentials = nexus_cr_credentials
        self._quay_cr_credentials = quay_cr_credentials

    @classmethod
    def from_dict(cls, dikt: dict) -> 'AddNewIntegrationRequestAnyOfCredentials':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The Add_new_integration_request_anyOf_credentials of this AddNewIntegrationRequestAnyOfCredentials.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def acr_credentials(self):
        """Gets the acr_credentials of this AddNewIntegrationRequestAnyOfCredentials.


        :return: The acr_credentials of this AddNewIntegrationRequestAnyOfCredentials.
        :rtype: AddNewIntegrationRequestAnyOfCredentialsOneOfAcrCredentials
        """
        return self._acr_credentials

    @acr_credentials.setter
    def acr_credentials(self, acr_credentials):
        """Sets the acr_credentials of this AddNewIntegrationRequestAnyOfCredentials.


        :param acr_credentials: The acr_credentials of this AddNewIntegrationRequestAnyOfCredentials.
        :type acr_credentials: AddNewIntegrationRequestAnyOfCredentialsOneOfAcrCredentials
        """

        self._acr_credentials = acr_credentials

    @property
    def artifactory_cr_credentials(self):
        """Gets the artifactory_cr_credentials of this AddNewIntegrationRequestAnyOfCredentials.


        :return: The artifactory_cr_credentials of this AddNewIntegrationRequestAnyOfCredentials.
        :rtype: AddNewIntegrationRequestAnyOfCredentialsOneOf1ArtifactoryCrCredentials
        """
        return self._artifactory_cr_credentials

    @artifactory_cr_credentials.setter
    def artifactory_cr_credentials(self, artifactory_cr_credentials):
        """Sets the artifactory_cr_credentials of this AddNewIntegrationRequestAnyOfCredentials.


        :param artifactory_cr_credentials: The artifactory_cr_credentials of this AddNewIntegrationRequestAnyOfCredentials.
        :type artifactory_cr_credentials: AddNewIntegrationRequestAnyOfCredentialsOneOf1ArtifactoryCrCredentials
        """

        self._artifactory_cr_credentials = artifactory_cr_credentials

    @property
    def azure_repos_credentials(self):
        """Gets the azure_repos_credentials of this AddNewIntegrationRequestAnyOfCredentials.


        :return: The azure_repos_credentials of this AddNewIntegrationRequestAnyOfCredentials.
        :rtype: AddNewIntegrationRequestAnyOfCredentialsOneOf2AzureReposCredentials
        """
        return self._azure_repos_credentials

    @azure_repos_credentials.setter
    def azure_repos_credentials(self, azure_repos_credentials):
        """Sets the azure_repos_credentials of this AddNewIntegrationRequestAnyOfCredentials.


        :param azure_repos_credentials: The azure_repos_credentials of this AddNewIntegrationRequestAnyOfCredentials.
        :type azure_repos_credentials: AddNewIntegrationRequestAnyOfCredentialsOneOf2AzureReposCredentials
        """

        self._azure_repos_credentials = azure_repos_credentials

    @property
    def bitbucket_cloud_credentials(self):
        """Gets the bitbucket_cloud_credentials of this AddNewIntegrationRequestAnyOfCredentials.


        :return: The bitbucket_cloud_credentials of this AddNewIntegrationRequestAnyOfCredentials.
        :rtype: AddNewIntegrationRequestAnyOfCredentialsOneOf3BitbucketCloudCredentials
        """
        return self._bitbucket_cloud_credentials

    @bitbucket_cloud_credentials.setter
    def bitbucket_cloud_credentials(self, bitbucket_cloud_credentials):
        """Sets the bitbucket_cloud_credentials of this AddNewIntegrationRequestAnyOfCredentials.


        :param bitbucket_cloud_credentials: The bitbucket_cloud_credentials of this AddNewIntegrationRequestAnyOfCredentials.
        :type bitbucket_cloud_credentials: AddNewIntegrationRequestAnyOfCredentialsOneOf3BitbucketCloudCredentials
        """

        self._bitbucket_cloud_credentials = bitbucket_cloud_credentials

    @property
    def bitbucket_server_credentials(self):
        """Gets the bitbucket_server_credentials of this AddNewIntegrationRequestAnyOfCredentials.


        :return: The bitbucket_server_credentials of this AddNewIntegrationRequestAnyOfCredentials.
        :rtype: AddNewIntegrationRequestAnyOfCredentialsOneOf4BitbucketServerCredentials
        """
        return self._bitbucket_server_credentials

    @bitbucket_server_credentials.setter
    def bitbucket_server_credentials(self, bitbucket_server_credentials):
        """Sets the bitbucket_server_credentials of this AddNewIntegrationRequestAnyOfCredentials.


        :param bitbucket_server_credentials: The bitbucket_server_credentials of this AddNewIntegrationRequestAnyOfCredentials.
        :type bitbucket_server_credentials: AddNewIntegrationRequestAnyOfCredentialsOneOf4BitbucketServerCredentials
        """

        self._bitbucket_server_credentials = bitbucket_server_credentials

    @property
    def digital_ocean_cr_credentials(self):
        """Gets the digital_ocean_cr_credentials of this AddNewIntegrationRequestAnyOfCredentials.


        :return: The digital_ocean_cr_credentials of this AddNewIntegrationRequestAnyOfCredentials.
        :rtype: AddNewIntegrationRequestAnyOfCredentialsOneOf5DigitalOceanCrCredentials
        """
        return self._digital_ocean_cr_credentials

    @digital_ocean_cr_credentials.setter
    def digital_ocean_cr_credentials(self, digital_ocean_cr_credentials):
        """Sets the digital_ocean_cr_credentials of this AddNewIntegrationRequestAnyOfCredentials.


        :param digital_ocean_cr_credentials: The digital_ocean_cr_credentials of this AddNewIntegrationRequestAnyOfCredentials.
        :type digital_ocean_cr_credentials: AddNewIntegrationRequestAnyOfCredentialsOneOf5DigitalOceanCrCredentials
        """

        self._digital_ocean_cr_credentials = digital_ocean_cr_credentials

    @property
    def docker_hub_credentials(self):
        """Gets the docker_hub_credentials of this AddNewIntegrationRequestAnyOfCredentials.


        :return: The docker_hub_credentials of this AddNewIntegrationRequestAnyOfCredentials.
        :rtype: AddNewIntegrationRequestAnyOfCredentialsOneOf6DockerHubCredentials
        """
        return self._docker_hub_credentials

    @docker_hub_credentials.setter
    def docker_hub_credentials(self, docker_hub_credentials):
        """Sets the docker_hub_credentials of this AddNewIntegrationRequestAnyOfCredentials.


        :param docker_hub_credentials: The docker_hub_credentials of this AddNewIntegrationRequestAnyOfCredentials.
        :type docker_hub_credentials: AddNewIntegrationRequestAnyOfCredentialsOneOf6DockerHubCredentials
        """

        self._docker_hub_credentials = docker_hub_credentials

    @property
    def ecr_credentials(self):
        """Gets the ecr_credentials of this AddNewIntegrationRequestAnyOfCredentials.


        :return: The ecr_credentials of this AddNewIntegrationRequestAnyOfCredentials.
        :rtype: AddNewIntegrationRequestAnyOfCredentialsOneOf7EcrCredentials
        """
        return self._ecr_credentials

    @ecr_credentials.setter
    def ecr_credentials(self, ecr_credentials):
        """Sets the ecr_credentials of this AddNewIntegrationRequestAnyOfCredentials.


        :param ecr_credentials: The ecr_credentials of this AddNewIntegrationRequestAnyOfCredentials.
        :type ecr_credentials: AddNewIntegrationRequestAnyOfCredentialsOneOf7EcrCredentials
        """

        self._ecr_credentials = ecr_credentials

    @property
    def gcr_credentials(self):
        """Gets the gcr_credentials of this AddNewIntegrationRequestAnyOfCredentials.


        :return: The gcr_credentials of this AddNewIntegrationRequestAnyOfCredentials.
        :rtype: AddNewIntegrationRequestAnyOfCredentialsOneOf8GcrCredentials
        """
        return self._gcr_credentials

    @gcr_credentials.setter
    def gcr_credentials(self, gcr_credentials):
        """Sets the gcr_credentials of this AddNewIntegrationRequestAnyOfCredentials.


        :param gcr_credentials: The gcr_credentials of this AddNewIntegrationRequestAnyOfCredentials.
        :type gcr_credentials: AddNewIntegrationRequestAnyOfCredentialsOneOf8GcrCredentials
        """

        self._gcr_credentials = gcr_credentials

    @property
    def git_hub_credentials(self):
        """Gets the git_hub_credentials of this AddNewIntegrationRequestAnyOfCredentials.


        :return: The git_hub_credentials of this AddNewIntegrationRequestAnyOfCredentials.
        :rtype: AddNewIntegrationRequestAnyOfCredentialsOneOf9GitHubCredentials
        """
        return self._git_hub_credentials

    @git_hub_credentials.setter
    def git_hub_credentials(self, git_hub_credentials):
        """Sets the git_hub_credentials of this AddNewIntegrationRequestAnyOfCredentials.


        :param git_hub_credentials: The git_hub_credentials of this AddNewIntegrationRequestAnyOfCredentials.
        :type git_hub_credentials: AddNewIntegrationRequestAnyOfCredentialsOneOf9GitHubCredentials
        """

        self._git_hub_credentials = git_hub_credentials

    @property
    def git_hub_cr_credentials(self):
        """Gets the git_hub_cr_credentials of this AddNewIntegrationRequestAnyOfCredentials.


        :return: The git_hub_cr_credentials of this AddNewIntegrationRequestAnyOfCredentials.
        :rtype: AddNewIntegrationRequestAnyOfCredentialsOneOf10GitHubCrCredentials
        """
        return self._git_hub_cr_credentials

    @git_hub_cr_credentials.setter
    def git_hub_cr_credentials(self, git_hub_cr_credentials):
        """Sets the git_hub_cr_credentials of this AddNewIntegrationRequestAnyOfCredentials.


        :param git_hub_cr_credentials: The git_hub_cr_credentials of this AddNewIntegrationRequestAnyOfCredentials.
        :type git_hub_cr_credentials: AddNewIntegrationRequestAnyOfCredentialsOneOf10GitHubCrCredentials
        """

        self._git_hub_cr_credentials = git_hub_cr_credentials

    @property
    def git_hub_enterprise_credentials(self):
        """Gets the git_hub_enterprise_credentials of this AddNewIntegrationRequestAnyOfCredentials.


        :return: The git_hub_enterprise_credentials of this AddNewIntegrationRequestAnyOfCredentials.
        :rtype: AddNewIntegrationRequestAnyOfCredentialsOneOf11GitHubEnterpriseCredentials
        """
        return self._git_hub_enterprise_credentials

    @git_hub_enterprise_credentials.setter
    def git_hub_enterprise_credentials(self, git_hub_enterprise_credentials):
        """Sets the git_hub_enterprise_credentials of this AddNewIntegrationRequestAnyOfCredentials.


        :param git_hub_enterprise_credentials: The git_hub_enterprise_credentials of this AddNewIntegrationRequestAnyOfCredentials.
        :type git_hub_enterprise_credentials: AddNewIntegrationRequestAnyOfCredentialsOneOf11GitHubEnterpriseCredentials
        """

        self._git_hub_enterprise_credentials = git_hub_enterprise_credentials

    @property
    def git_lab_credentials(self):
        """Gets the git_lab_credentials of this AddNewIntegrationRequestAnyOfCredentials.


        :return: The git_lab_credentials of this AddNewIntegrationRequestAnyOfCredentials.
        :rtype: AddNewIntegrationRequestAnyOfCredentialsOneOf12GitLabCredentials
        """
        return self._git_lab_credentials

    @git_lab_credentials.setter
    def git_lab_credentials(self, git_lab_credentials):
        """Sets the git_lab_credentials of this AddNewIntegrationRequestAnyOfCredentials.


        :param git_lab_credentials: The git_lab_credentials of this AddNewIntegrationRequestAnyOfCredentials.
        :type git_lab_credentials: AddNewIntegrationRequestAnyOfCredentialsOneOf12GitLabCredentials
        """

        self._git_lab_credentials = git_lab_credentials

    @property
    def git_lab_cr_credentials(self):
        """Gets the git_lab_cr_credentials of this AddNewIntegrationRequestAnyOfCredentials.


        :return: The git_lab_cr_credentials of this AddNewIntegrationRequestAnyOfCredentials.
        :rtype: AddNewIntegrationRequestAnyOfCredentialsOneOf13GitLabCrCredentials
        """
        return self._git_lab_cr_credentials

    @git_lab_cr_credentials.setter
    def git_lab_cr_credentials(self, git_lab_cr_credentials):
        """Sets the git_lab_cr_credentials of this AddNewIntegrationRequestAnyOfCredentials.


        :param git_lab_cr_credentials: The git_lab_cr_credentials of this AddNewIntegrationRequestAnyOfCredentials.
        :type git_lab_cr_credentials: AddNewIntegrationRequestAnyOfCredentialsOneOf13GitLabCrCredentials
        """

        self._git_lab_cr_credentials = git_lab_cr_credentials

    @property
    def google_artifact_cr_credentials(self):
        """Gets the google_artifact_cr_credentials of this AddNewIntegrationRequestAnyOfCredentials.


        :return: The google_artifact_cr_credentials of this AddNewIntegrationRequestAnyOfCredentials.
        :rtype: AddNewIntegrationRequestAnyOfCredentialsOneOf14GoogleArtifactCrCredentials
        """
        return self._google_artifact_cr_credentials

    @google_artifact_cr_credentials.setter
    def google_artifact_cr_credentials(self, google_artifact_cr_credentials):
        """Sets the google_artifact_cr_credentials of this AddNewIntegrationRequestAnyOfCredentials.


        :param google_artifact_cr_credentials: The google_artifact_cr_credentials of this AddNewIntegrationRequestAnyOfCredentials.
        :type google_artifact_cr_credentials: AddNewIntegrationRequestAnyOfCredentialsOneOf14GoogleArtifactCrCredentials
        """

        self._google_artifact_cr_credentials = google_artifact_cr_credentials

    @property
    def harbor_cr_credentials(self):
        """Gets the harbor_cr_credentials of this AddNewIntegrationRequestAnyOfCredentials.


        :return: The harbor_cr_credentials of this AddNewIntegrationRequestAnyOfCredentials.
        :rtype: AddNewIntegrationRequestAnyOfCredentialsOneOf15HarborCrCredentials
        """
        return self._harbor_cr_credentials

    @harbor_cr_credentials.setter
    def harbor_cr_credentials(self, harbor_cr_credentials):
        """Sets the harbor_cr_credentials of this AddNewIntegrationRequestAnyOfCredentials.


        :param harbor_cr_credentials: The harbor_cr_credentials of this AddNewIntegrationRequestAnyOfCredentials.
        :type harbor_cr_credentials: AddNewIntegrationRequestAnyOfCredentialsOneOf15HarborCrCredentials
        """

        self._harbor_cr_credentials = harbor_cr_credentials

    @property
    def nexus_cr_credentials(self):
        """Gets the nexus_cr_credentials of this AddNewIntegrationRequestAnyOfCredentials.


        :return: The nexus_cr_credentials of this AddNewIntegrationRequestAnyOfCredentials.
        :rtype: AddNewIntegrationRequestAnyOfCredentialsOneOf16NexusCrCredentials
        """
        return self._nexus_cr_credentials

    @nexus_cr_credentials.setter
    def nexus_cr_credentials(self, nexus_cr_credentials):
        """Sets the nexus_cr_credentials of this AddNewIntegrationRequestAnyOfCredentials.


        :param nexus_cr_credentials: The nexus_cr_credentials of this AddNewIntegrationRequestAnyOfCredentials.
        :type nexus_cr_credentials: AddNewIntegrationRequestAnyOfCredentialsOneOf16NexusCrCredentials
        """

        self._nexus_cr_credentials = nexus_cr_credentials

    @property
    def quay_cr_credentials(self):
        """Gets the quay_cr_credentials of this AddNewIntegrationRequestAnyOfCredentials.


        :return: The quay_cr_credentials of this AddNewIntegrationRequestAnyOfCredentials.
        :rtype: AddNewIntegrationRequestAnyOfCredentialsOneOf17QuayCrCredentials
        """
        return self._quay_cr_credentials

    @quay_cr_credentials.setter
    def quay_cr_credentials(self, quay_cr_credentials):
        """Sets the quay_cr_credentials of this AddNewIntegrationRequestAnyOfCredentials.


        :param quay_cr_credentials: The quay_cr_credentials of this AddNewIntegrationRequestAnyOfCredentials.
        :type quay_cr_credentials: AddNewIntegrationRequestAnyOfCredentialsOneOf17QuayCrCredentials
        """

        self._quay_cr_credentials = quay_cr_credentials
