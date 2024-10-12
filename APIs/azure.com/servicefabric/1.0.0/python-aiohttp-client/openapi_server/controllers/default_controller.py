from typing import List, Dict
from aiohttp import web

from openapi_server.models.application import Application
from openapi_server.models.application_description import ApplicationDescription
from openapi_server.models.application_health import ApplicationHealth
from openapi_server.models.application_health_report import ApplicationHealthReport
from openapi_server.models.application_list import ApplicationList
from openapi_server.models.application_manifest import ApplicationManifest
from openapi_server.models.application_type import ApplicationType
from openapi_server.models.application_upgrade import ApplicationUpgrade
from openapi_server.models.cluster_health import ClusterHealth
from openapi_server.models.cluster_health_report import ClusterHealthReport
from openapi_server.models.cluster_load_information import ClusterLoadInformation
from openapi_server.models.cluster_upgrade_progress import ClusterUpgradeProgress
from openapi_server.models.create_service_description import CreateServiceDescription
from openapi_server.models.create_service_group_description import CreateServiceGroupDescription
from openapi_server.models.deployed_application import DeployedApplication
from openapi_server.models.deployed_application_health import DeployedApplicationHealth
from openapi_server.models.deployed_application_health_report import DeployedApplicationHealthReport
from openapi_server.models.deployed_code_package import DeployedCodePackage
from openapi_server.models.deployed_replica import DeployedReplica
from openapi_server.models.deployed_replica_detail import DeployedReplicaDetail
from openapi_server.models.deployed_service_health_report import DeployedServiceHealthReport
from openapi_server.models.deployed_service_package import DeployedServicePackage
from openapi_server.models.deployed_service_package_health import DeployedServicePackageHealth
from openapi_server.models.deployed_service_type import DeployedServiceType
from openapi_server.models.disable_node import DisableNode
from openapi_server.models.error_model import ErrorModel
from openapi_server.models.node import Node
from openapi_server.models.node_health import NodeHealth
from openapi_server.models.node_health_report import NodeHealthReport
from openapi_server.models.node_list import NodeList
from openapi_server.models.node_load_information import NodeLoadInformation
from openapi_server.models.partition import Partition
from openapi_server.models.partition_health import PartitionHealth
from openapi_server.models.partition_health_report import PartitionHealthReport
from openapi_server.models.partition_list import PartitionList
from openapi_server.models.partition_load_information import PartitionLoadInformation
from openapi_server.models.register_application_type import RegisterApplicationType
from openapi_server.models.register_cluster_package import RegisterClusterPackage
from openapi_server.models.replica import Replica
from openapi_server.models.replica_health import ReplicaHealth
from openapi_server.models.replica_health_report import ReplicaHealthReport
from openapi_server.models.replica_list import ReplicaList
from openapi_server.models.replica_load_information import ReplicaLoadInformation
from openapi_server.models.resolved_service_partition import ResolvedServicePartition
from openapi_server.models.resume_application_upgrade import ResumeApplicationUpgrade
from openapi_server.models.resume_cluster_upgrade import ResumeClusterUpgrade
from openapi_server.models.service import Service
from openapi_server.models.service_description import ServiceDescription
from openapi_server.models.service_description_template import ServiceDescriptionTemplate
from openapi_server.models.service_group_description import ServiceGroupDescription
from openapi_server.models.service_group_member import ServiceGroupMember
from openapi_server.models.service_health import ServiceHealth
from openapi_server.models.service_health_report import ServiceHealthReport
from openapi_server.models.service_list import ServiceList
from openapi_server.models.service_manifest import ServiceManifest
from openapi_server.models.service_type import ServiceType
from openapi_server.models.start_application_upgrade import StartApplicationUpgrade
from openapi_server.models.start_cluster_upgrade import StartClusterUpgrade
from openapi_server.models.unregister_application_type import UnregisterApplicationType
from openapi_server.models.unregister_cluster_package import UnregisterClusterPackage
from openapi_server.models.update_application_upgrade import UpdateApplicationUpgrade
from openapi_server.models.update_cluster_upgrade import UpdateClusterUpgrade
from openapi_server.models.update_service_description import UpdateServiceDescription
from openapi_server.models.update_service_group_description import UpdateServiceGroupDescription
from openapi_server import util


async def application_healths_get(request: web.Request, application_name, api_version, events_health_state_filter=None, deployed_applications_health_state_filter=None, timeout=None) -> web.Response:
    """application_healths_get

    Get application healths

    :param application_name: The name of the application
    :type application_name: str
    :param api_version: The version of the api
    :type api_version: str
    :param events_health_state_filter: The filter of the events health state
    :type events_health_state_filter: str
    :param deployed_applications_health_state_filter: The filter of the deployed application health state
    :type deployed_applications_health_state_filter: str
    :param timeout: The timeout in seconds
    :type timeout: int

    """
    return web.Response(status=200)


async def application_healths_send(request: web.Request, application_name, api_version, application_health_report, timeout=None) -> web.Response:
    """application_healths_send

    Send application health

    :param application_name: The name of the application
    :type application_name: str
    :param api_version: The version of the api
    :type api_version: str
    :param application_health_report: The report of the application health
    :type application_health_report: dict | bytes
    :param timeout: The timeout in seconds
    :type timeout: int

    """
    application_health_report = ApplicationHealthReport.from_dict(application_health_report)
    return web.Response(status=200)


async def application_manifests_get(request: web.Request, application_type_name, application_type_version, api_version, timeout=None) -> web.Response:
    """application_manifests_get

    Get application manifests

    :param application_type_name: The name of the application type
    :type application_type_name: str
    :param application_type_version: The version of the application type
    :type application_type_version: str
    :param api_version: The version of the api
    :type api_version: str
    :param timeout: The timeout in seconds
    :type timeout: int

    """
    return web.Response(status=200)


async def application_types_get(request: web.Request, application_type_name, api_version, timeout=None) -> web.Response:
    """application_types_get

    Get application types

    :param application_type_name: The name of the application type
    :type application_type_name: str
    :param api_version: The version of the api
    :type api_version: str
    :param timeout: The timeout in seconds
    :type timeout: int

    """
    return web.Response(status=200)


async def application_types_list(request: web.Request, api_version, timeout=None) -> web.Response:
    """application_types_list

    List application types

    :param api_version: The version of the api
    :type api_version: str
    :param timeout: The timeout in seconds
    :type timeout: int

    """
    return web.Response(status=200)


async def application_types_register(request: web.Request, api_version, register_application_type, timeout=None) -> web.Response:
    """application_types_register

    Register application types

    :param api_version: The version of the api
    :type api_version: str
    :param register_application_type: The type of the register application
    :type register_application_type: dict | bytes
    :param timeout: The timeout in seconds
    :type timeout: int

    """
    register_application_type = RegisterApplicationType.from_dict(register_application_type)
    return web.Response(status=200)


async def application_types_unregister(request: web.Request, application_type_name, api_version, unregister_application_type, timeout=None) -> web.Response:
    """application_types_unregister

    Unregister application types

    :param application_type_name: The name of the application type
    :type application_type_name: str
    :param api_version: The version of the api
    :type api_version: str
    :param unregister_application_type: The type of the unregister application
    :type unregister_application_type: dict | bytes
    :param timeout: The timeout in seconds
    :type timeout: int

    """
    unregister_application_type = UnregisterApplicationType.from_dict(unregister_application_type)
    return web.Response(status=200)


async def application_upgrade_rollbacks_start(request: web.Request, application_name, api_version, timeout=None) -> web.Response:
    """application_upgrade_rollbacks_start

    Start application upgrade rollbacks

    :param application_name: The name of the application
    :type application_name: str
    :param api_version: The version of the api
    :type api_version: str
    :param timeout: The timeout in seconds
    :type timeout: int

    """
    return web.Response(status=200)


async def application_upgrades_get(request: web.Request, application_name, api_version, timeout=None) -> web.Response:
    """application_upgrades_get

    Get application upgrades

    :param application_name: The name of the application
    :type application_name: str
    :param api_version: The version of the api
    :type api_version: str
    :param timeout: The timeout in seconds
    :type timeout: int

    """
    return web.Response(status=200)


async def application_upgrades_resume(request: web.Request, application_name, api_version, resume_application_upgrade, timeout=None) -> web.Response:
    """application_upgrades_resume

    Resume application upgrades

    :param application_name: The name of the application
    :type application_name: str
    :param api_version: The version of the api
    :type api_version: str
    :param resume_application_upgrade: The upgrade of the resume application
    :type resume_application_upgrade: dict | bytes
    :param timeout: The timeout in seconds
    :type timeout: int

    """
    resume_application_upgrade = ResumeApplicationUpgrade.from_dict(resume_application_upgrade)
    return web.Response(status=200)


async def application_upgrades_start(request: web.Request, application_name, api_version, start_application_upgrade, timeout=None) -> web.Response:
    """application_upgrades_start

    Start application upgrades

    :param application_name: The name of the application
    :type application_name: str
    :param api_version: The version of the api
    :type api_version: str
    :param start_application_upgrade: The description of the start application upgrade
    :type start_application_upgrade: dict | bytes
    :param timeout: The timeout in seconds
    :type timeout: int

    """
    start_application_upgrade = StartApplicationUpgrade.from_dict(start_application_upgrade)
    return web.Response(status=200)


async def application_upgrades_update(request: web.Request, application_name, api_version, update_application_upgrade, timeout=None) -> web.Response:
    """application_upgrades_update

    Update application upgrades

    :param application_name: The name of the application
    :type application_name: str
    :param api_version: The version of the api
    :type api_version: str
    :param update_application_upgrade: The description of the update application upgrade
    :type update_application_upgrade: dict | bytes
    :param timeout: The timeout in seconds
    :type timeout: int

    """
    update_application_upgrade = UpdateApplicationUpgrade.from_dict(update_application_upgrade)
    return web.Response(status=200)


async def applications_create(request: web.Request, api_version, application_description, timeout=None) -> web.Response:
    """applications_create

    Create applications

    :param api_version: The version of the api
    :type api_version: str
    :param application_description: The description of the application
    :type application_description: dict | bytes
    :param timeout: The timeout in seconds
    :type timeout: int

    """
    application_description = ApplicationDescription.from_dict(application_description)
    return web.Response(status=200)


async def applications_get(request: web.Request, application_name, api_version, timeout=None) -> web.Response:
    """applications_get

    Get applications

    :param application_name: The name of the application
    :type application_name: str
    :param api_version: The version of the api
    :type api_version: str
    :param timeout: The timeout in seconds
    :type timeout: int

    """
    return web.Response(status=200)


async def applications_list(request: web.Request, api_version, timeout=None, continuation_token=None) -> web.Response:
    """applications_list

    List applications

    :param api_version: The version of the api
    :type api_version: str
    :param timeout: The timeout in seconds
    :type timeout: int
    :param continuation_token: The token of the continuation
    :type continuation_token: str

    """
    return web.Response(status=200)


async def applications_remove(request: web.Request, application_name, api_version, force_remove=None, timeout=None) -> web.Response:
    """applications_remove

    Remove applications

    :param application_name: The name of the application
    :type application_name: str
    :param api_version: The version of the api
    :type api_version: str
    :param force_remove: The force remove flag to skip services check
    :type force_remove: bool
    :param timeout: The timeout in seconds
    :type timeout: int

    """
    return web.Response(status=200)


async def cluster_healths_get(request: web.Request, api_version, events_health_state_filter=None, nodes_health_state_filter=None, applications_health_state_filter=None, timeout=None) -> web.Response:
    """cluster_healths_get

    Get cluster healths

    :param api_version: The version of the api
    :type api_version: str
    :param events_health_state_filter: The filter of the events health state
    :type events_health_state_filter: str
    :param nodes_health_state_filter: The filter of the nodes health state
    :type nodes_health_state_filter: str
    :param applications_health_state_filter: The filter of the applications health state
    :type applications_health_state_filter: str
    :param timeout: The timeout in seconds
    :type timeout: int

    """
    return web.Response(status=200)


async def cluster_healths_send(request: web.Request, api_version, cluster_health_report, timeout=None) -> web.Response:
    """cluster_healths_send

    Report cluster healths

    :param api_version: The version of the api
    :type api_version: str
    :param cluster_health_report: The report of the cluster health
    :type cluster_health_report: dict | bytes
    :param timeout: The timeout in seconds
    :type timeout: int

    """
    cluster_health_report = ClusterHealthReport.from_dict(cluster_health_report)
    return web.Response(status=200)


async def cluster_load_informations_get(request: web.Request, api_version, timeout=None) -> web.Response:
    """cluster_load_informations_get

    Get cluster load informations

    :param api_version: The version of the api
    :type api_version: str
    :param timeout: The timeout in seconds
    :type timeout: int

    """
    return web.Response(status=200)


async def cluster_manifests_get(request: web.Request, api_version, timeout=None) -> web.Response:
    """cluster_manifests_get

    Get cluster manifests

    :param api_version: The version of the api
    :type api_version: str
    :param timeout: The timeout in seconds
    :type timeout: int

    """
    return web.Response(status=200)


async def cluster_packages_register(request: web.Request, api_version, register_cluster_package, timeout=None) -> web.Response:
    """cluster_packages_register

    Register cluster packages

    :param api_version: The version of the api
    :type api_version: str
    :param register_cluster_package: The package of the register cluster
    :type register_cluster_package: dict | bytes
    :param timeout: The timeout in seconds
    :type timeout: int

    """
    register_cluster_package = RegisterClusterPackage.from_dict(register_cluster_package)
    return web.Response(status=200)


async def cluster_packages_unregister(request: web.Request, api_version, unregister_cluster_package, timeout=None) -> web.Response:
    """cluster_packages_unregister

    Unregister cluster packages

    :param api_version: The version of the api
    :type api_version: str
    :param unregister_cluster_package: The package of the unregister cluster
    :type unregister_cluster_package: dict | bytes
    :param timeout: The timeout in seconds
    :type timeout: int

    """
    unregister_cluster_package = UnregisterClusterPackage.from_dict(unregister_cluster_package)
    return web.Response(status=200)


async def cluster_upgrades_resume(request: web.Request, api_version, resume_cluster_upgrade, timeout=None) -> web.Response:
    """cluster_upgrades_resume

    Resume cluster upgrades

    :param api_version: The version of the api
    :type api_version: str
    :param resume_cluster_upgrade: The upgrade of the cluster
    :type resume_cluster_upgrade: dict | bytes
    :param timeout: The timeout in seconds
    :type timeout: int

    """
    resume_cluster_upgrade = ResumeClusterUpgrade.from_dict(resume_cluster_upgrade)
    return web.Response(status=200)


async def cluster_upgrades_rollback(request: web.Request, api_version, timeout=None) -> web.Response:
    """cluster_upgrades_rollback

    Rollback cluster upgrades

    :param api_version: The version of the api
    :type api_version: str
    :param timeout: The timeout in seconds
    :type timeout: int

    """
    return web.Response(status=200)


async def cluster_upgrades_start(request: web.Request, api_version, start_cluster_upgrade, timeout=None) -> web.Response:
    """cluster_upgrades_start

    Start cluster upgrades

    :param api_version: The version of the api
    :type api_version: str
    :param start_cluster_upgrade: The description of the start cluster upgrade
    :type start_cluster_upgrade: dict | bytes
    :param timeout: The timeout in seconds
    :type timeout: int

    """
    start_cluster_upgrade = StartClusterUpgrade.from_dict(start_cluster_upgrade)
    return web.Response(status=200)


async def cluster_upgrades_update(request: web.Request, api_version, update_cluster_upgrade, timeout=None) -> web.Response:
    """cluster_upgrades_update

    Update cluster upgrades

    :param api_version: The version of the api
    :type api_version: str
    :param update_cluster_upgrade: The description of the update cluster upgrade
    :type update_cluster_upgrade: dict | bytes
    :param timeout: The timeout in seconds
    :type timeout: int

    """
    update_cluster_upgrade = UpdateClusterUpgrade.from_dict(update_cluster_upgrade)
    return web.Response(status=200)


async def deployed_application_healths_get(request: web.Request, node_name, application_name, api_version, events_health_state_filter=None, deployed_service_packages_health_state_filter=None, timeout=None) -> web.Response:
    """deployed_application_healths_get

    Get deployed application healths

    :param node_name: The name of the node
    :type node_name: str
    :param application_name: The name of the application
    :type application_name: str
    :param api_version: The version of the api
    :type api_version: str
    :param events_health_state_filter: The filter of the events health state
    :type events_health_state_filter: str
    :param deployed_service_packages_health_state_filter: The filter of the deployed service packages health state
    :type deployed_service_packages_health_state_filter: str
    :param timeout: The timeout in seconds
    :type timeout: int

    """
    return web.Response(status=200)


async def deployed_application_healths_send(request: web.Request, node_name, application_name, api_version, deployed_application_health_report, timeout=None) -> web.Response:
    """deployed_application_healths_send

    Send deployed application health

    :param node_name: The name of the node
    :type node_name: str
    :param application_name: The name of the application
    :type application_name: str
    :param api_version: The version of the api
    :type api_version: str
    :param deployed_application_health_report: The report of the deployed application health
    :type deployed_application_health_report: dict | bytes
    :param timeout: The timeout in seconds
    :type timeout: int

    """
    deployed_application_health_report = DeployedApplicationHealthReport.from_dict(deployed_application_health_report)
    return web.Response(status=200)


async def deployed_applications_get(request: web.Request, node_name, application_name, api_version, timeout=None) -> web.Response:
    """deployed_applications_get

    Get deployed applications

    :param node_name: The name of the node
    :type node_name: str
    :param application_name: The name of the application
    :type application_name: str
    :param api_version: The version of the api
    :type api_version: str
    :param timeout: The timeout in seconds
    :type timeout: int

    """
    return web.Response(status=200)


async def deployed_applications_list(request: web.Request, node_name, api_version, timeout=None) -> web.Response:
    """deployed_applications_list

    List deployed applications

    :param node_name: The name of the node
    :type node_name: str
    :param api_version: The version of the api
    :type api_version: str
    :param timeout: The timeout in seconds
    :type timeout: int

    """
    return web.Response(status=200)


async def deployed_code_packages_get(request: web.Request, node_name, application_name, api_version, timeout=None) -> web.Response:
    """deployed_code_packages_get

    Get deployed code packages

    :param node_name: The name of the node
    :type node_name: str
    :param application_name: The name of the application
    :type application_name: str
    :param api_version: The version of the api
    :type api_version: str
    :param timeout: The timeout in seconds
    :type timeout: int

    """
    return web.Response(status=200)


async def deployed_replica_details_get(request: web.Request, node_name, partition_name, replica_id, api_version, timeout=None) -> web.Response:
    """deployed_replica_details_get

    Get deployed replica details

    :param node_name: The name of the node
    :type node_name: str
    :param partition_name: The name of the partition
    :type partition_name: str
    :param replica_id: The id of the replica
    :type replica_id: str
    :param api_version: The version of the api
    :type api_version: str
    :param timeout: The timeout in seconds
    :type timeout: int

    """
    return web.Response(status=200)


async def deployed_replicas_get(request: web.Request, node_name, application_name, api_version, timeout=None) -> web.Response:
    """deployed_replicas_get

    Get deployed replicas

    :param node_name: The name of the node
    :type node_name: str
    :param application_name: The name of the application
    :type application_name: str
    :param api_version: The version of the api
    :type api_version: str
    :param timeout: The timeout in seconds
    :type timeout: int

    """
    return web.Response(status=200)


async def deployed_service_package_healths_get(request: web.Request, node_name, application_name, service_package_name, api_version, events_health_state_filter=None, timeout=None) -> web.Response:
    """deployed_service_package_healths_get

    Get deployed service package healths

    :param node_name: The name of the node
    :type node_name: str
    :param application_name: The name of the application
    :type application_name: str
    :param service_package_name: The name of the service package
    :type service_package_name: str
    :param api_version: The version of the api
    :type api_version: str
    :param events_health_state_filter: The filter of the events health state
    :type events_health_state_filter: str
    :param timeout: The timeout in seconds
    :type timeout: int

    """
    return web.Response(status=200)


async def deployed_service_package_healths_send(request: web.Request, node_name, application_name, service_manifest_name, api_version, deployed_service_package_health_report, timeout=None) -> web.Response:
    """deployed_service_package_healths_send

    Send deployed service package health

    :param node_name: The name of the node
    :type node_name: str
    :param application_name: The name of the application
    :type application_name: str
    :param service_manifest_name: The name of the service manifest
    :type service_manifest_name: str
    :param api_version: The version of the api
    :type api_version: str
    :param deployed_service_package_health_report: The report of the deployed service package health
    :type deployed_service_package_health_report: dict | bytes
    :param timeout: The timeout in seconds
    :type timeout: int

    """
    deployed_service_package_health_report = DeployedServiceHealthReport.from_dict(deployed_service_package_health_report)
    return web.Response(status=200)


async def deployed_service_packages_get(request: web.Request, node_name, application_name, api_version, timeout=None) -> web.Response:
    """deployed_service_packages_get

    Get deployed service packages

    :param node_name: The name of the node
    :type node_name: str
    :param application_name: The name of the application
    :type application_name: str
    :param api_version: The version of the api
    :type api_version: str
    :param timeout: The timeout in seconds
    :type timeout: int

    """
    return web.Response(status=200)


async def deployed_service_types_get(request: web.Request, node_name, application_name, api_version, timeout=None) -> web.Response:
    """deployed_service_types_get

    Get deployed service types

    :param node_name: The name of the node
    :type node_name: str
    :param application_name: The name of the application
    :type application_name: str
    :param api_version: The version of the api
    :type api_version: str
    :param timeout: The timeout in seconds
    :type timeout: int

    """
    return web.Response(status=200)


async def node_healths_get(request: web.Request, node_name, api_version, events_health_state_filter=None, timeout=None) -> web.Response:
    """node_healths_get

    Get node healths

    :param node_name: The name of the node
    :type node_name: str
    :param api_version: The version of the api
    :type api_version: str
    :param events_health_state_filter: The filter of the events health state
    :type events_health_state_filter: str
    :param timeout: The timeout in seconds
    :type timeout: int

    """
    return web.Response(status=200)


async def node_healths_send(request: web.Request, node_name, api_version, node_health_report, timeout=None) -> web.Response:
    """node_healths_send

    Send node health

    :param node_name: The name of the node
    :type node_name: str
    :param api_version: The version of the api
    :type api_version: str
    :param node_health_report: The report of the node health
    :type node_health_report: dict | bytes
    :param timeout: The timeout in seconds
    :type timeout: int

    """
    node_health_report = NodeHealthReport.from_dict(node_health_report)
    return web.Response(status=200)


async def node_load_informations_get(request: web.Request, node_name, api_version, timeout=None) -> web.Response:
    """node_load_informations_get

    Get node load informations

    :param node_name: The name of the node
    :type node_name: str
    :param api_version: The version of the api
    :type api_version: str
    :param timeout: The timeout in seconds
    :type timeout: int

    """
    return web.Response(status=200)


async def node_states_remove(request: web.Request, node_name, api_version, timeout=None) -> web.Response:
    """node_states_remove

    Remove node states

    :param node_name: The name of the node
    :type node_name: str
    :param api_version: The version of the api
    :type api_version: str
    :param timeout: The timeout in seconds
    :type timeout: int

    """
    return web.Response(status=200)


async def nodes_disable(request: web.Request, node_name, api_version, disable_node, timeout=None) -> web.Response:
    """nodes_disable

    Disable nodes

    :param node_name: The name of the node
    :type node_name: str
    :param api_version: The version of the api
    :type api_version: str
    :param disable_node: The node
    :type disable_node: dict | bytes
    :param timeout: The timeout in seconds
    :type timeout: int

    """
    disable_node = DisableNode.from_dict(disable_node)
    return web.Response(status=200)


async def nodes_enable(request: web.Request, node_name, api_version, timeout=None) -> web.Response:
    """nodes_enable

    Enable nodes

    :param node_name: The name of the node
    :type node_name: str
    :param api_version: The version of the api
    :type api_version: str
    :param timeout: The timeout in seconds
    :type timeout: int

    """
    return web.Response(status=200)


async def nodes_get(request: web.Request, node_name, api_version, timeout=None) -> web.Response:
    """nodes_get

    Get nodes

    :param node_name: The name of the node
    :type node_name: str
    :param api_version: The version of the api
    :type api_version: str
    :param timeout: The timeout in seconds
    :type timeout: int

    """
    return web.Response(status=200)


async def nodes_list(request: web.Request, api_version, timeout=None, continuation_token=None) -> web.Response:
    """nodes_list

    List nodes

    :param api_version: The version of the api
    :type api_version: str
    :param timeout: The timeout in seconds
    :type timeout: int
    :param continuation_token: The token of the continuation
    :type continuation_token: str

    """
    return web.Response(status=200)


async def partition_healths_get(request: web.Request, partition_id, api_version, events_health_state_filter=None, replicas_health_state_filter=None, timeout=None) -> web.Response:
    """partition_healths_get

    Get partition healths

    :param partition_id: The id of the partition
    :type partition_id: str
    :param api_version: The version of the api
    :type api_version: str
    :param events_health_state_filter: The filter of the events health state
    :type events_health_state_filter: str
    :param replicas_health_state_filter: The filter of the replicas health state
    :type replicas_health_state_filter: str
    :param timeout: The timeout in seconds
    :type timeout: int

    """
    return web.Response(status=200)


async def partition_healths_send(request: web.Request, partition_id, api_version, partition_health_report, timeout=None) -> web.Response:
    """partition_healths_send

    Send partition health

    :param partition_id: The id of the partition
    :type partition_id: str
    :param api_version: The version of the api
    :type api_version: str
    :param partition_health_report: The report of the partition health
    :type partition_health_report: dict | bytes
    :param timeout: The timeout in seconds
    :type timeout: int

    """
    partition_health_report = PartitionHealthReport.from_dict(partition_health_report)
    return web.Response(status=200)


async def partition_lists_repair(request: web.Request, service_name, api_version, timeout=None) -> web.Response:
    """partition_lists_repair

    Repair partition lists

    :param service_name: The name of the service
    :type service_name: str
    :param api_version: The version of the api
    :type api_version: str
    :param timeout: The timeout in seconds
    :type timeout: int

    """
    return web.Response(status=200)


async def partition_load_informations_get(request: web.Request, partition_id, api_version, timeout=None) -> web.Response:
    """partition_load_informations_get

    Get partition load informations

    :param partition_id: The id of the partition
    :type partition_id: str
    :param api_version: The version of the api
    :type api_version: str
    :param timeout: The timeout in seconds
    :type timeout: int

    """
    return web.Response(status=200)


async def partition_loads_reset(request: web.Request, partition_id, api_version, timeout=None) -> web.Response:
    """partition_loads_reset

    Reset partition loads

    :param partition_id: The id of the partition
    :type partition_id: str
    :param api_version: The version of the api
    :type api_version: str
    :param timeout: The timeout in seconds
    :type timeout: int

    """
    return web.Response(status=200)


async def partitions_get(request: web.Request, service_name, partition_id, api_version, timeout=None) -> web.Response:
    """partitions_get

    Get partitions

    :param service_name: The name of the service
    :type service_name: str
    :param partition_id: The id of the partition
    :type partition_id: str
    :param api_version: The version of the api
    :type api_version: str
    :param timeout: The timeout in seconds
    :type timeout: int

    """
    return web.Response(status=200)


async def partitions_list(request: web.Request, service_name, api_version, timeout=None) -> web.Response:
    """partitions_list

    List partitions

    :param service_name: The name of the service
    :type service_name: str
    :param api_version: The version of the api
    :type api_version: str
    :param timeout: The timeout in seconds
    :type timeout: int

    """
    return web.Response(status=200)


async def partitions_repair(request: web.Request, partition_id, api_version, timeout=None) -> web.Response:
    """partitions_repair

    Repair partitions

    :param partition_id: The id of the partition
    :type partition_id: str
    :param api_version: The version of the api
    :type api_version: str
    :param timeout: The timeout in seconds
    :type timeout: int

    """
    return web.Response(status=200)


async def replica_healths_get(request: web.Request, partition_id, replica_id, api_version, events_health_state_filter=None, timeout=None) -> web.Response:
    """replica_healths_get

    Get replica healths

    :param partition_id: The id of the partition
    :type partition_id: str
    :param replica_id: The id of the replica
    :type replica_id: str
    :param api_version: The version of the api
    :type api_version: str
    :param events_health_state_filter: The filter of the events health state
    :type events_health_state_filter: str
    :param timeout: The timeout in seconds
    :type timeout: int

    """
    return web.Response(status=200)


async def replica_healths_send(request: web.Request, partition_id, replica_id, api_version, replica_health_report, timeout=None) -> web.Response:
    """replica_healths_send

    Send replica healths

    :param partition_id: The id of the partition
    :type partition_id: str
    :param replica_id: The id of the replica
    :type replica_id: str
    :param api_version: The version of the api
    :type api_version: str
    :param replica_health_report: The report of the replica health
    :type replica_health_report: dict | bytes
    :param timeout: The timeout in seconds
    :type timeout: int

    """
    replica_health_report = ReplicaHealthReport.from_dict(replica_health_report)
    return web.Response(status=200)


async def replica_load_informations_get(request: web.Request, partition_id, replica_id, api_version, timeout=None) -> web.Response:
    """replica_load_informations_get

    Get replica load informations

    :param partition_id: The id of the partition
    :type partition_id: str
    :param replica_id: The id of the replica
    :type replica_id: str
    :param api_version: The version of the api
    :type api_version: str
    :param timeout: The timeout in seconds
    :type timeout: int

    """
    return web.Response(status=200)


async def replicas_get(request: web.Request, partition_id, replica_id, api_version, timeout=None) -> web.Response:
    """replicas_get

    Get replicas

    :param partition_id: The id of the partition
    :type partition_id: str
    :param replica_id: The id of the replica
    :type replica_id: str
    :param api_version: The version of the api
    :type api_version: str
    :param timeout: The timeout in seconds
    :type timeout: int

    """
    return web.Response(status=200)


async def replicas_list(request: web.Request, partition_id, api_version, timeout=None) -> web.Response:
    """replicas_list

    List replicas

    :param partition_id: The id of the partition
    :type partition_id: str
    :param api_version: The version of the api
    :type api_version: str
    :param timeout: The timeout in seconds
    :type timeout: int

    """
    return web.Response(status=200)


async def service_descriptions_get(request: web.Request, service_name, api_version, timeout=None) -> web.Response:
    """service_descriptions_get

    Get service descriptions

    :param service_name: The name of the service
    :type service_name: str
    :param api_version: The version of the api
    :type api_version: str
    :param timeout: The timeout in seconds
    :type timeout: int

    """
    return web.Response(status=200)


async def service_from_templates_create(request: web.Request, application_name, api_version, service_description_template, timeout=None) -> web.Response:
    """service_from_templates_create

    Create service from templates

    :param application_name: The name of the application
    :type application_name: str
    :param api_version: The version of the api
    :type api_version: str
    :param service_description_template: The template of the service description
    :type service_description_template: dict | bytes
    :param timeout: The timeout in seconds
    :type timeout: int

    """
    service_description_template = ServiceDescriptionTemplate.from_dict(service_description_template)
    return web.Response(status=200)


async def service_group_descriptions_get(request: web.Request, application_name, service_name, api_version, timeout=None) -> web.Response:
    """service_group_descriptions_get

    Get service group descriptions

    :param application_name: The name of the application
    :type application_name: str
    :param service_name: The name of the service
    :type service_name: str
    :param api_version: The version of the api
    :type api_version: str
    :param timeout: The timeout in seconds
    :type timeout: int

    """
    return web.Response(status=200)


async def service_group_from_templates_create(request: web.Request, application_name, api_version, service_description_template, timeout=None) -> web.Response:
    """service_group_from_templates_create

    Create service group from templates

    :param application_name: The name of the application
    :type application_name: str
    :param api_version: The version of the api
    :type api_version: str
    :param service_description_template: The template of the service description
    :type service_description_template: dict | bytes
    :param timeout: The timeout in seconds
    :type timeout: int

    """
    service_description_template = ServiceDescriptionTemplate.from_dict(service_description_template)
    return web.Response(status=200)


async def service_group_members_get(request: web.Request, application_name, service_name, api_version, timeout=None) -> web.Response:
    """service_group_members_get

    Get service group members

    :param application_name: The name of the application
    :type application_name: str
    :param service_name: The name of the service
    :type service_name: str
    :param api_version: The version of the api
    :type api_version: str
    :param timeout: The timeout in seconds
    :type timeout: int

    """
    return web.Response(status=200)


async def service_groups_create(request: web.Request, application_name, api_version, create_service_group_description, timeout=None) -> web.Response:
    """service_groups_create

    Create service groups

    :param application_name: The name of the service group
    :type application_name: str
    :param api_version: The version of the api
    :type api_version: str
    :param create_service_group_description: The description of the service group
    :type create_service_group_description: dict | bytes
    :param timeout: The timeout in seconds
    :type timeout: int

    """
    create_service_group_description = CreateServiceGroupDescription.from_dict(create_service_group_description)
    return web.Response(status=200)


async def service_groups_remove(request: web.Request, application_name, service_name, api_version, timeout=None) -> web.Response:
    """service_groups_remove

    Remove service groups

    :param application_name: The name of the application
    :type application_name: str
    :param service_name: The name of the service
    :type service_name: str
    :param api_version: The version of the api
    :type api_version: str
    :param timeout: The timeout in seconds
    :type timeout: int

    """
    return web.Response(status=200)


async def service_groups_update(request: web.Request, application_name, service_name, api_version, update_service_group_description, timeout=None) -> web.Response:
    """service_groups_update

    Update service groups

    :param application_name: The name of the application
    :type application_name: str
    :param service_name: The name of the service
    :type service_name: str
    :param api_version: The version of the api
    :type api_version: str
    :param update_service_group_description: The description of the service group update
    :type update_service_group_description: dict | bytes
    :param timeout: The timeout in seconds
    :type timeout: int

    """
    update_service_group_description = UpdateServiceGroupDescription.from_dict(update_service_group_description)
    return web.Response(status=200)


async def service_healths_get(request: web.Request, service_name, api_version, timeout=None) -> web.Response:
    """service_healths_get

    Get service healths

    :param service_name: The name of the service
    :type service_name: str
    :param api_version: The version of the api
    :type api_version: str
    :param timeout: The timeout in seconds
    :type timeout: int

    """
    return web.Response(status=200)


async def service_healths_send(request: web.Request, service_name, api_version, service_health_report, timeout=None) -> web.Response:
    """service_healths_send

    Send service healths

    :param service_name: The name of the service
    :type service_name: str
    :param api_version: The version of the api
    :type api_version: str
    :param service_health_report: The report of the service health
    :type service_health_report: dict | bytes
    :param timeout: The timeout in seconds
    :type timeout: int

    """
    service_health_report = ServiceHealthReport.from_dict(service_health_report)
    return web.Response(status=200)


async def service_manifests_get(request: web.Request, application_type_name, application_type_version, service_manifest_name, api_version, timeout=None) -> web.Response:
    """service_manifests_get

    Get service manifests

    :param application_type_name: The name of the application type
    :type application_type_name: str
    :param application_type_version: The version of the application type
    :type application_type_version: str
    :param service_manifest_name: The name of the service manifest
    :type service_manifest_name: str
    :param api_version: The version of the api
    :type api_version: str
    :param timeout: The timeout in seconds
    :type timeout: int

    """
    return web.Response(status=200)


async def service_types_get(request: web.Request, application_type_name, application_type_version, api_version, timeout=None) -> web.Response:
    """service_types_get

    Get service types

    :param application_type_name: The name of the application type
    :type application_type_name: str
    :param application_type_version: The version of the application type
    :type application_type_version: str
    :param api_version: The version of the api
    :type api_version: str
    :param timeout: The timeout in seconds
    :type timeout: int

    """
    return web.Response(status=200)


async def services_create(request: web.Request, application_name, api_version, create_service_description, timeout=None) -> web.Response:
    """services_create

    Create services

    :param application_name: The name of the application
    :type application_name: str
    :param api_version: The version of the api
    :type api_version: str
    :param create_service_description: The description of the service
    :type create_service_description: dict | bytes
    :param timeout: The timeout in seconds
    :type timeout: int

    """
    create_service_description = CreateServiceDescription.from_dict(create_service_description)
    return web.Response(status=200)


async def services_get(request: web.Request, application_name, service_name, api_version, timeout=None) -> web.Response:
    """services_get

    Get services

    :param application_name: The name of the application
    :type application_name: str
    :param service_name: The name of the service
    :type service_name: str
    :param api_version: The version of the api
    :type api_version: str
    :param timeout: The timeout in seconds
    :type timeout: int

    """
    return web.Response(status=200)


async def services_list(request: web.Request, application_name, api_version, timeout=None) -> web.Response:
    """services_list

    List services

    :param application_name: The name of the application
    :type application_name: str
    :param api_version: The version of the api
    :type api_version: str
    :param timeout: The timeout in seconds
    :type timeout: int

    """
    return web.Response(status=200)


async def services_remove(request: web.Request, service_name, api_version, timeout=None) -> web.Response:
    """services_remove

    Remove services

    :param service_name: The name of the service
    :type service_name: str
    :param api_version: The version of the api
    :type api_version: str
    :param timeout: The timeout in seconds
    :type timeout: int

    """
    return web.Response(status=200)


async def services_resolve(request: web.Request, service_name, api_version, partition_key_type=None, partition_key_value=None, previous_rsp_version=None, timeout=None) -> web.Response:
    """services_resolve

    Resolve services

    :param service_name: The name of the service
    :type service_name: str
    :param api_version: The version of the api
    :type api_version: str
    :param partition_key_type: The type of the partition key
    :type partition_key_type: int
    :param partition_key_value: The value of the partition key
    :type partition_key_value: str
    :param previous_rsp_version: The version of the previous rsp
    :type previous_rsp_version: str
    :param timeout: The timeout in seconds
    :type timeout: int

    """
    return web.Response(status=200)


async def services_update(request: web.Request, service_name, api_version, update_service_description, timeout=None) -> web.Response:
    """services_update

    Update services

    :param service_name: The name of the service
    :type service_name: str
    :param api_version: The version of the api
    :type api_version: str
    :param update_service_description: The description of the service update
    :type update_service_description: dict | bytes
    :param timeout: The timeout in seconds
    :type timeout: int

    """
    update_service_description = UpdateServiceDescription.from_dict(update_service_description)
    return web.Response(status=200)


async def upgrade_progresses_get(request: web.Request, api_version, timeout=None) -> web.Response:
    """upgrade_progresses_get

    Get upgrade progresses

    :param api_version: The version of the api
    :type api_version: str
    :param timeout: The timeout in seconds
    :type timeout: int

    """
    return web.Response(status=200)
