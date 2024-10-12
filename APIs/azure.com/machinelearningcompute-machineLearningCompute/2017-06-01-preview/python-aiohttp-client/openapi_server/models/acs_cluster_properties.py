# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.kubernetes_cluster_properties import KubernetesClusterProperties
from openapi_server.models.system_services import SystemServices
from openapi_server import util


class AcsClusterProperties(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, agent_count: int=None, agent_vm_size: str='D2_v2', cluster_fqdn: str=None, orchestrator_properties: KubernetesClusterProperties=None, orchestrator_type: str=None, system_services: List[SystemServices]=None):
        """AcsClusterProperties - a model defined in OpenAPI

        :param agent_count: The agent_count of this AcsClusterProperties.
        :param agent_vm_size: The agent_vm_size of this AcsClusterProperties.
        :param cluster_fqdn: The cluster_fqdn of this AcsClusterProperties.
        :param orchestrator_properties: The orchestrator_properties of this AcsClusterProperties.
        :param orchestrator_type: The orchestrator_type of this AcsClusterProperties.
        :param system_services: The system_services of this AcsClusterProperties.
        """
        self.openapi_types = {
            'agent_count': int,
            'agent_vm_size': str,
            'cluster_fqdn': str,
            'orchestrator_properties': KubernetesClusterProperties,
            'orchestrator_type': str,
            'system_services': List[SystemServices]
        }

        self.attribute_map = {
            'agent_count': 'agentCount',
            'agent_vm_size': 'agentVmSize',
            'cluster_fqdn': 'clusterFqdn',
            'orchestrator_properties': 'orchestratorProperties',
            'orchestrator_type': 'orchestratorType',
            'system_services': 'systemServices'
        }

        self._agent_count = agent_count
        self._agent_vm_size = agent_vm_size
        self._cluster_fqdn = cluster_fqdn
        self._orchestrator_properties = orchestrator_properties
        self._orchestrator_type = orchestrator_type
        self._system_services = system_services

    @classmethod
    def from_dict(cls, dikt: dict) -> 'AcsClusterProperties':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The AcsClusterProperties of this AcsClusterProperties.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def agent_count(self):
        """Gets the agent_count of this AcsClusterProperties.

        The number of agent nodes in the Container Service. This can be changed to scale the cluster.

        :return: The agent_count of this AcsClusterProperties.
        :rtype: int
        """
        return self._agent_count

    @agent_count.setter
    def agent_count(self, agent_count):
        """Sets the agent_count of this AcsClusterProperties.

        The number of agent nodes in the Container Service. This can be changed to scale the cluster.

        :param agent_count: The agent_count of this AcsClusterProperties.
        :type agent_count: int
        """
        if agent_count is not None and agent_count > 100:
            raise ValueError("Invalid value for `agent_count`, must be a value less than or equal to `100`")
        if agent_count is not None and agent_count < 1:
            raise ValueError("Invalid value for `agent_count`, must be a value greater than or equal to `1`")

        self._agent_count = agent_count

    @property
    def agent_vm_size(self):
        """Gets the agent_vm_size of this AcsClusterProperties.

        The Azure VM size of the agent VM nodes. This cannot be changed once the cluster is created.

        :return: The agent_vm_size of this AcsClusterProperties.
        :rtype: str
        """
        return self._agent_vm_size

    @agent_vm_size.setter
    def agent_vm_size(self, agent_vm_size):
        """Sets the agent_vm_size of this AcsClusterProperties.

        The Azure VM size of the agent VM nodes. This cannot be changed once the cluster is created.

        :param agent_vm_size: The agent_vm_size of this AcsClusterProperties.
        :type agent_vm_size: str
        """
        allowed_values = ["Standard_A0", "Standard_A1", "Standard_A2", "Standard_A3", "Standard_A4", "Standard_A5", "Standard_A6", "Standard_A7", "Standard_A8", "Standard_A9", "Standard_A10", "Standard_A11", "Standard_D1", "Standard_D2", "Standard_D3", "Standard_D4", "Standard_D11", "Standard_D12", "Standard_D13", "Standard_D14", "Standard_D1_v2", "Standard_D2_v2", "Standard_D3_v2", "Standard_D4_v2", "Standard_D5_v2", "Standard_D11_v2", "Standard_D12_v2", "Standard_D13_v2", "Standard_D14_v2", "Standard_G1", "Standard_G2", "Standard_G3", "Standard_G4", "Standard_G5", "Standard_DS1", "Standard_DS2", "Standard_DS3", "Standard_DS4", "Standard_DS11", "Standard_DS12", "Standard_DS13", "Standard_DS14", "Standard_GS1", "Standard_GS2", "Standard_GS3", "Standard_GS4", "Standard_GS5"]  # noqa: E501
        if agent_vm_size not in allowed_values:
            raise ValueError(
                "Invalid value for `agent_vm_size` ({0}), must be one of {1}"
                .format(agent_vm_size, allowed_values)
            )

        self._agent_vm_size = agent_vm_size

    @property
    def cluster_fqdn(self):
        """Gets the cluster_fqdn of this AcsClusterProperties.

        The FQDN of the cluster. 

        :return: The cluster_fqdn of this AcsClusterProperties.
        :rtype: str
        """
        return self._cluster_fqdn

    @cluster_fqdn.setter
    def cluster_fqdn(self, cluster_fqdn):
        """Sets the cluster_fqdn of this AcsClusterProperties.

        The FQDN of the cluster. 

        :param cluster_fqdn: The cluster_fqdn of this AcsClusterProperties.
        :type cluster_fqdn: str
        """

        self._cluster_fqdn = cluster_fqdn

    @property
    def orchestrator_properties(self):
        """Gets the orchestrator_properties of this AcsClusterProperties.


        :return: The orchestrator_properties of this AcsClusterProperties.
        :rtype: KubernetesClusterProperties
        """
        return self._orchestrator_properties

    @orchestrator_properties.setter
    def orchestrator_properties(self, orchestrator_properties):
        """Sets the orchestrator_properties of this AcsClusterProperties.


        :param orchestrator_properties: The orchestrator_properties of this AcsClusterProperties.
        :type orchestrator_properties: KubernetesClusterProperties
        """
        if orchestrator_properties is None:
            raise ValueError("Invalid value for `orchestrator_properties`, must not be `None`")

        self._orchestrator_properties = orchestrator_properties

    @property
    def orchestrator_type(self):
        """Gets the orchestrator_type of this AcsClusterProperties.

        Type of orchestrator. It cannot be changed once the cluster is created.

        :return: The orchestrator_type of this AcsClusterProperties.
        :rtype: str
        """
        return self._orchestrator_type

    @orchestrator_type.setter
    def orchestrator_type(self, orchestrator_type):
        """Sets the orchestrator_type of this AcsClusterProperties.

        Type of orchestrator. It cannot be changed once the cluster is created.

        :param orchestrator_type: The orchestrator_type of this AcsClusterProperties.
        :type orchestrator_type: str
        """
        allowed_values = ["Kubernetes"]  # noqa: E501
        if orchestrator_type not in allowed_values:
            raise ValueError(
                "Invalid value for `orchestrator_type` ({0}), must be one of {1}"
                .format(orchestrator_type, allowed_values)
            )

        self._orchestrator_type = orchestrator_type

    @property
    def system_services(self):
        """Gets the system_services of this AcsClusterProperties.

        The system services deployed to the cluster

        :return: The system_services of this AcsClusterProperties.
        :rtype: List[SystemServices]
        """
        return self._system_services

    @system_services.setter
    def system_services(self, system_services):
        """Sets the system_services of this AcsClusterProperties.

        The system services deployed to the cluster

        :param system_services: The system_services of this AcsClusterProperties.
        :type system_services: List[SystemServices]
        """

        self._system_services = system_services
