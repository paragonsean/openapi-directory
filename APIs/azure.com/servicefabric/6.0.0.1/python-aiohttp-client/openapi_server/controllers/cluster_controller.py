from typing import List, Dict
from aiohttp import web

from openapi_server.models.aad_metadata_object import AadMetadataObject
from openapi_server.models.cluster_configuration import ClusterConfiguration
from openapi_server.models.cluster_configuration_upgrade_description import ClusterConfigurationUpgradeDescription
from openapi_server.models.cluster_configuration_upgrade_status_info import ClusterConfigurationUpgradeStatusInfo
from openapi_server.models.cluster_health import ClusterHealth
from openapi_server.models.cluster_health_chunk import ClusterHealthChunk
from openapi_server.models.cluster_health_chunk_query_description import ClusterHealthChunkQueryDescription
from openapi_server.models.cluster_health_policies import ClusterHealthPolicies
from openapi_server.models.cluster_manifest import ClusterManifest
from openapi_server.models.cluster_upgrade_progress_object import ClusterUpgradeProgressObject
from openapi_server.models.fabric_code_version_info import FabricCodeVersionInfo
from openapi_server.models.fabric_config_version_info import FabricConfigVersionInfo
from openapi_server.models.fabric_error import FabricError
from openapi_server.models.health_information import HealthInformation
from openapi_server.models.provision_fabric_description import ProvisionFabricDescription
from openapi_server.models.resume_cluster_upgrade_description import ResumeClusterUpgradeDescription
from openapi_server.models.start_cluster_upgrade_description import StartClusterUpgradeDescription
from openapi_server.models.unprovision_fabric_description import UnprovisionFabricDescription
from openapi_server.models.update_cluster_upgrade_description import UpdateClusterUpgradeDescription
from openapi_server import util


async def get_aad_metadata(request: web.Request, api_version, timeout=None) -> web.Response:
    """Gets the Azure Active Directory metadata used for secured connection to cluster.

    Gets the Azure Active Directory metadata used for secured connection to cluster. This API is not supposed to be called separately. It provides information needed to set up an Azure Active Directory secured connection with a Service Fabric cluster. 

    :param api_version: The version of the API. This is a required parameter and it&#39;s value must be \&quot;6.0\&quot;.
    :type api_version: str
    :param timeout: The server timeout for performing the operation in seconds. This specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds.
    :type timeout: int

    """
    return web.Response(status=200)


async def get_cluster_configuration(request: web.Request, api_version, configuration_api_version, timeout=None) -> web.Response:
    """Get the Service Fabric standalone cluster configuration.

    Get the Service Fabric standalone cluster configuration. The cluster configuration contains properties of the cluster that include different node types on the cluster, security configurations, fault and upgrade domain topologies etc. 

    :param api_version: The version of the API. This is a required parameter and it&#39;s value must be \&quot;6.0\&quot;.
    :type api_version: str
    :param configuration_api_version: The API version of the Standalone cluster json configuration.
    :type configuration_api_version: str
    :param timeout: The server timeout for performing the operation in seconds. This specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds.
    :type timeout: int

    """
    return web.Response(status=200)


async def get_cluster_configuration_upgrade_status(request: web.Request, api_version, timeout=None) -> web.Response:
    """Get the cluster configuration upgrade status of a Service Fabric standalone cluster.

    Get the cluster configuration upgrade status of a Service Fabric standalone cluster. 

    :param api_version: The version of the API. This is a required parameter and it&#39;s value must be \&quot;6.0\&quot;.
    :type api_version: str
    :param timeout: The server timeout for performing the operation in seconds. This specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds.
    :type timeout: int

    """
    return web.Response(status=200)


async def get_cluster_health(request: web.Request, api_version, nodes_health_state_filter=None, applications_health_state_filter=None, events_health_state_filter=None, exclude_health_statistics=None, include_system_application_health_statistics=None, timeout=None) -> web.Response:
    """Gets the health of a Service Fabric cluster.

    Gets the health of a Service Fabric cluster. Use EventsHealthStateFilter to filter the collection of health events reported on the cluster based on the health state. Similarly, use NodesHealthStateFilter and ApplicationsHealthStateFilter to filter the collection of nodes and applications returned based on their aggregated health state. 

    :param api_version: The version of the API. This is a required parameter and it&#39;s value must be \&quot;6.0\&quot;.
    :type api_version: str
    :param nodes_health_state_filter: Allows filtering of the node health state objects returned in the result of cluster health query based on their health state. The possible values for this parameter include integer value of one of the following health states. Only nodes that match the filter are returned. All nodes are used to evaluate the aggregated health state. If not specified, all entries are returned. The state values are flag based enumeration, so the value could be a combination of these values obtained using bitwise &#39;OR&#39; operator. For example, if the provided value is 6 then health state of nodes with HealthState value of OK (2) and Warning (4) are returned.  - Default - Default value. Matches any HealthState. The value is zero. - None - Filter that doesn&#39;t match any HealthState value. Used in order to return no results on a given collection of states. The value is 1. - Ok - Filter that matches input with HealthState value Ok. The value is 2. - Warning - Filter that matches input with HealthState value Warning. The value is 4. - Error - Filter that matches input with HealthState value Error. The value is 8. - All - Filter that matches input with any HealthState value. The value is 65535. 
    :type nodes_health_state_filter: int
    :param applications_health_state_filter: Allows filtering of the application health state objects returned in the result of cluster health query based on their health state. The possible values for this parameter include integer value obtained from members or bitwise operations on members of HealthStateFilter enumeration. Only applications that match the filter are returned. All applications are used to evaluate the aggregated health state. If not specified, all entries are returned. The state values are flag based enumeration, so the value could be a combination of these values obtained using bitwise &#39;OR&#39; operator. For example, if the provided value is 6 then health state of applications with HealthState value of OK (2) and Warning (4) are returned.  - Default - Default value. Matches any HealthState. The value is zero. - None - Filter that doesn&#39;t match any HealthState value. Used in order to return no results on a given collection of states. The value is 1. - Ok - Filter that matches input with HealthState value Ok. The value is 2. - Warning - Filter that matches input with HealthState value Warning. The value is 4. - Error - Filter that matches input with HealthState value Error. The value is 8. - All - Filter that matches input with any HealthState value. The value is 65535. 
    :type applications_health_state_filter: int
    :param events_health_state_filter: Allows filtering the collection of HealthEvent objects returned based on health state. The possible values for this parameter include integer value of one of the following health states. Only events that match the filter are returned. All events are used to evaluate the aggregated health state. If not specified, all entries are returned. The state values are flag based enumeration, so the value could be a combination of these value obtained using bitwise &#39;OR&#39; operator. For example, If the provided value is 6 then all of the events with HealthState value of OK (2) and Warning (4) are returned.  - Default - Default value. Matches any HealthState. The value is zero. - None - Filter that doesn&#39;t match any HealthState value. Used in order to return no results on a given collection of states. The value is 1. - Ok - Filter that matches input with HealthState value Ok. The value is 2. - Warning - Filter that matches input with HealthState value Warning. The value is 4. - Error - Filter that matches input with HealthState value Error. The value is 8. - All - Filter that matches input with any HealthState value. The value is 65535. 
    :type events_health_state_filter: int
    :param exclude_health_statistics: Indicates whether the health statistics should be returned as part of the query result. False by default. The statistics show the number of children entities in health state Ok, Warning, and Error. 
    :type exclude_health_statistics: bool
    :param include_system_application_health_statistics: Indicates whether the health statistics should include the fabric:/System application health statistics. False by default. If IncludeSystemApplicationHealthStatistics is set to true, the health statistics include the entities that belong to the fabric:/System application. Otherwise, the query result includes health statistics only for user applications. The health statistics must be included in the query result for this parameter to be applied. 
    :type include_system_application_health_statistics: bool
    :param timeout: The server timeout for performing the operation in seconds. This specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds.
    :type timeout: int

    """
    return web.Response(status=200)


async def get_cluster_health_chunk(request: web.Request, api_version, timeout=None) -> web.Response:
    """Gets the health of a Service Fabric cluster using health chunks.

    Gets the health of a Service Fabric cluster using health chunks. Includes the aggregated health state of the cluster, but none of the cluster entities. To expand the cluster health and get the health state of all or some of the entities, use the POST URI and specify the cluster health chunk query description. 

    :param api_version: The version of the API. This is a required parameter and it&#39;s value must be \&quot;6.0\&quot;.
    :type api_version: str
    :param timeout: The server timeout for performing the operation in seconds. This specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds.
    :type timeout: int

    """
    return web.Response(status=200)


async def get_cluster_health_chunk_using_policy_and_advanced_filters(request: web.Request, api_version, timeout=None, cluster_health_chunk_query_description=None) -> web.Response:
    """Gets the health of a Service Fabric cluster using health chunks.

    Gets the health of a Service Fabric cluster using health chunks. The health evaluation is done based on the input cluster health chunk query description. The query description allows users to specify health policies for evaluating the cluster and its children. Users can specify very flexible filters to select which cluster entities to return. The selection can be done based on the entities health state and based on the hierarchy. The query can return multi-level children of the entities based on the specified filters. For example, it can return one application with a specified name, and for this application, return only services that are in Error or Warning, and all partitions and replicas for one of these services. 

    :param api_version: The version of the API. This is a required parameter and it&#39;s value must be \&quot;6.0\&quot;.
    :type api_version: str
    :param timeout: The server timeout for performing the operation in seconds. This specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds.
    :type timeout: int
    :param cluster_health_chunk_query_description: Describes the cluster and application health policies used to evaluate the cluster health and the filters to select which cluster entities to be returned. If the cluster health policy is present, it is used to evaluate the cluster events and the cluster nodes. If not present, the health evaluation uses the cluster health policy defined in the cluster manifest or the default cluster health policy. By default, each application is evaluated using its specific application health policy, defined in the application manifest, or the default health policy, if no policy is defined in manifest. If the application health policy map is specified, and it has an entry for an application, the specified application health policy is used to evaluate the application health. Users can specify very flexible filters to select which cluster entities to include in response. The selection can be done based on the entities health state and based on the hierarchy. The query can return multi-level children of the entities based on the specified filters. For example, it can return one application with a specified name, and for this application, return only services that are in Error or Warning, and all partitions and replicas for one of these services. 
    :type cluster_health_chunk_query_description: dict | bytes

    """
    cluster_health_chunk_query_description = ClusterHealthChunkQueryDescription.from_dict(cluster_health_chunk_query_description)
    return web.Response(status=200)


async def get_cluster_health_using_policy(request: web.Request, api_version, nodes_health_state_filter=None, applications_health_state_filter=None, events_health_state_filter=None, exclude_health_statistics=None, include_system_application_health_statistics=None, timeout=None, cluster_health_policies=None) -> web.Response:
    """Gets the health of a Service Fabric cluster using the specified policy.

    Gets the health of a Service Fabric cluster. Use EventsHealthStateFilter to filter the collection of health events reported on the cluster based on the health state. Similarly, use NodesHealthStateFilter and ApplicationsHealthStateFilter to filter the collection of nodes and applications returned based on their aggregated health state. Use ClusterHealthPolicies to override the health policies used to evaluate the health. 

    :param api_version: The version of the API. This is a required parameter and it&#39;s value must be \&quot;6.0\&quot;.
    :type api_version: str
    :param nodes_health_state_filter: Allows filtering of the node health state objects returned in the result of cluster health query based on their health state. The possible values for this parameter include integer value of one of the following health states. Only nodes that match the filter are returned. All nodes are used to evaluate the aggregated health state. If not specified, all entries are returned. The state values are flag based enumeration, so the value could be a combination of these values obtained using bitwise &#39;OR&#39; operator. For example, if the provided value is 6 then health state of nodes with HealthState value of OK (2) and Warning (4) are returned.  - Default - Default value. Matches any HealthState. The value is zero. - None - Filter that doesn&#39;t match any HealthState value. Used in order to return no results on a given collection of states. The value is 1. - Ok - Filter that matches input with HealthState value Ok. The value is 2. - Warning - Filter that matches input with HealthState value Warning. The value is 4. - Error - Filter that matches input with HealthState value Error. The value is 8. - All - Filter that matches input with any HealthState value. The value is 65535. 
    :type nodes_health_state_filter: int
    :param applications_health_state_filter: Allows filtering of the application health state objects returned in the result of cluster health query based on their health state. The possible values for this parameter include integer value obtained from members or bitwise operations on members of HealthStateFilter enumeration. Only applications that match the filter are returned. All applications are used to evaluate the aggregated health state. If not specified, all entries are returned. The state values are flag based enumeration, so the value could be a combination of these values obtained using bitwise &#39;OR&#39; operator. For example, if the provided value is 6 then health state of applications with HealthState value of OK (2) and Warning (4) are returned.  - Default - Default value. Matches any HealthState. The value is zero. - None - Filter that doesn&#39;t match any HealthState value. Used in order to return no results on a given collection of states. The value is 1. - Ok - Filter that matches input with HealthState value Ok. The value is 2. - Warning - Filter that matches input with HealthState value Warning. The value is 4. - Error - Filter that matches input with HealthState value Error. The value is 8. - All - Filter that matches input with any HealthState value. The value is 65535. 
    :type applications_health_state_filter: int
    :param events_health_state_filter: Allows filtering the collection of HealthEvent objects returned based on health state. The possible values for this parameter include integer value of one of the following health states. Only events that match the filter are returned. All events are used to evaluate the aggregated health state. If not specified, all entries are returned. The state values are flag based enumeration, so the value could be a combination of these value obtained using bitwise &#39;OR&#39; operator. For example, If the provided value is 6 then all of the events with HealthState value of OK (2) and Warning (4) are returned.  - Default - Default value. Matches any HealthState. The value is zero. - None - Filter that doesn&#39;t match any HealthState value. Used in order to return no results on a given collection of states. The value is 1. - Ok - Filter that matches input with HealthState value Ok. The value is 2. - Warning - Filter that matches input with HealthState value Warning. The value is 4. - Error - Filter that matches input with HealthState value Error. The value is 8. - All - Filter that matches input with any HealthState value. The value is 65535. 
    :type events_health_state_filter: int
    :param exclude_health_statistics: Indicates whether the health statistics should be returned as part of the query result. False by default. The statistics show the number of children entities in health state Ok, Warning, and Error. 
    :type exclude_health_statistics: bool
    :param include_system_application_health_statistics: Indicates whether the health statistics should include the fabric:/System application health statistics. False by default. If IncludeSystemApplicationHealthStatistics is set to true, the health statistics include the entities that belong to the fabric:/System application. Otherwise, the query result includes health statistics only for user applications. The health statistics must be included in the query result for this parameter to be applied. 
    :type include_system_application_health_statistics: bool
    :param timeout: The server timeout for performing the operation in seconds. This specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds.
    :type timeout: int
    :param cluster_health_policies: Describes the health policies used to evaluate the cluster health. If not present, the health evaluation uses the cluster health policy defined in the cluster manifest or the default cluster health policy. By default, each application is evaluated using its specific application health policy, defined in the application manifest, or the default health policy, if no policy is defined in manifest. If the application health policy map is specified, and it has an entry for an application, the specified application health policy is used to evaluate the application health. 
    :type cluster_health_policies: dict | bytes

    """
    cluster_health_policies = ClusterHealthPolicies.from_dict(cluster_health_policies)
    return web.Response(status=200)


async def get_cluster_manifest(request: web.Request, api_version, timeout=None) -> web.Response:
    """Get the Service Fabric cluster manifest.

    Get the Service Fabric cluster manifest. The cluster manifest contains properties of the cluster that include different node types on the cluster, security configurations, fault and upgrade domain topologies etc.  These properties are specified as part of the ClusterConfig.JSON file while deploying a stand alone cluster. However, most of the information in the cluster manifest is generated internally by service fabric during cluster deployment in other deployment scenarios (for e.g when using azuer portal).  The contents of the cluster manifest are for informational purposes only and users are not expected to take a dependency on the format of the file contents or its interpretation. 

    :param api_version: The version of the API. This is a required parameter and it&#39;s value must be \&quot;6.0\&quot;.
    :type api_version: str
    :param timeout: The server timeout for performing the operation in seconds. This specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds.
    :type timeout: int

    """
    return web.Response(status=200)


async def get_cluster_upgrade_progress(request: web.Request, api_version, timeout=None) -> web.Response:
    """Gets the progress of the current cluster upgrade.

    Gets the current progress of the ongoing cluster upgrade. If no upgrade is currently in progress, gets the last state of the previous cluster upgrade.

    :param api_version: The version of the API. This is a required parameter and it&#39;s value must be \&quot;6.0\&quot;.
    :type api_version: str
    :param timeout: The server timeout for performing the operation in seconds. This specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds.
    :type timeout: int

    """
    return web.Response(status=200)


async def get_provisioned_fabric_code_version_info_list(request: web.Request, api_version, code_version=None, timeout=None) -> web.Response:
    """Gets a list of fabric code versions that are provisioned in a Service Fabric cluster.

    Gets a list of information about fabric code versions that are provisioned in the cluster. The parameter CodeVersion can be used to optionally filter the output to only that particular version.

    :param api_version: The version of the API. This is a required parameter and it&#39;s value must be \&quot;6.0\&quot;.
    :type api_version: str
    :param code_version: The product version of Service Fabric.
    :type code_version: str
    :param timeout: The server timeout for performing the operation in seconds. This specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds.
    :type timeout: int

    """
    return web.Response(status=200)


async def get_provisioned_fabric_config_version_info_list(request: web.Request, api_version, config_version=None, timeout=None) -> web.Response:
    """Gets a list of fabric config versions that are provisioned in a Service Fabric cluster.

    Gets a list of information about fabric config versions that are provisioned in the cluster. The parameter ConfigVersion can be used to optionally filter the output to only that particular version.

    :param api_version: The version of the API. This is a required parameter and it&#39;s value must be \&quot;6.0\&quot;.
    :type api_version: str
    :param config_version: The config version of Service Fabric.
    :type config_version: str
    :param timeout: The server timeout for performing the operation in seconds. This specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds.
    :type timeout: int

    """
    return web.Response(status=200)


async def provision_cluster(request: web.Request, api_version, provision_fabric_description, timeout=None) -> web.Response:
    """Provision the code or configuration packages of a Service Fabric cluster.

    Validate and provision the code or configuration packages of a Service Fabric cluster.

    :param api_version: The version of the API. This is a required parameter and it&#39;s value must be \&quot;6.0\&quot;.
    :type api_version: str
    :param provision_fabric_description: Describes the parameters for provisioning a cluster.
    :type provision_fabric_description: dict | bytes
    :param timeout: The server timeout for performing the operation in seconds. This specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds.
    :type timeout: int

    """
    provision_fabric_description = ProvisionFabricDescription.from_dict(provision_fabric_description)
    return web.Response(status=200)


async def report_cluster_health(request: web.Request, api_version, health_information, immediate=None, timeout=None) -> web.Response:
    """Sends a health report on the Service Fabric cluster.

    Sends a health report on a Service Fabric cluster. The report must contain the information about the source of the health report and property on which it is reported. The report is sent to a Service Fabric gateway node, which forwards to the health store. The report may be accepted by the gateway, but rejected by the health store after extra validation. For example, the health store may reject the report because of an invalid parameter, like a stale sequence number. To see whether the report was applied in the health store, run GetClusterHealth and check that the report appears in the HealthEvents section. 

    :param api_version: The version of the API. This is a required parameter and it&#39;s value must be \&quot;6.0\&quot;.
    :type api_version: str
    :param health_information: Describes the health information for the health report. This information needs to be present in all of the health reports sent to the health manager.
    :type health_information: dict | bytes
    :param immediate: A flag which indicates whether the report should be sent immediately. A health report is sent to a Service Fabric gateway Application, which forwards to the health store. If Immediate is set to true, the report is sent immediately from Http Gateway to the health store, regardless of the fabric client settings that the Http Gateway Application is using. This is useful for critical reports that should be sent as soon as possible. Depending on timing and other conditions, sending the report may still fail, for example if the Http Gateway is closed or the message doesn&#39;t reach the Gateway. If Immediate is set to false, the report is sent based on the health client settings from the Http Gateway. Therefore, it will be batched according to the HealthReportSendInterval configuration. This is the recommended setting because it allows the health client to optimize health reporting messages to health store as well as health report processing. By default, reports are not sent immediately. 
    :type immediate: bool
    :param timeout: The server timeout for performing the operation in seconds. This specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds.
    :type timeout: int

    """
    health_information = HealthInformation.from_dict(health_information)
    return web.Response(status=200)


async def resume_cluster_upgrade(request: web.Request, api_version, resume_cluster_upgrade_description, timeout=None) -> web.Response:
    """Make the cluster upgrade move on to the next upgrade domain.

    Make the cluster upgrade move on to the next upgrade domain.

    :param api_version: The version of the API. This is a required parameter and it&#39;s value must be \&quot;6.0\&quot;.
    :type api_version: str
    :param resume_cluster_upgrade_description: Describes the parameters for resuming a cluster upgrade.
    :type resume_cluster_upgrade_description: dict | bytes
    :param timeout: The server timeout for performing the operation in seconds. This specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds.
    :type timeout: int

    """
    resume_cluster_upgrade_description = ResumeClusterUpgradeDescription.from_dict(resume_cluster_upgrade_description)
    return web.Response(status=200)


async def rollback_cluster_upgrade(request: web.Request, api_version, timeout=None) -> web.Response:
    """Rollback the upgrade of a Service Fabric cluster.

    Rollback the upgrade of a Service Fabric cluster.

    :param api_version: The version of the API. This is a required parameter and it&#39;s value must be \&quot;6.0\&quot;.
    :type api_version: str
    :param timeout: The server timeout for performing the operation in seconds. This specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds.
    :type timeout: int

    """
    return web.Response(status=200)


async def start_cluster_configuration_upgrade(request: web.Request, api_version, cluster_configuration_upgrade_description, timeout=None) -> web.Response:
    """Start upgrading the configuration of a Service Fabric standalone cluster.

    Validate the supplied configuration upgrade parameters and start upgrading the cluster configuration if the parameters are valid.

    :param api_version: The version of the API. This is a required parameter and it&#39;s value must be \&quot;6.0\&quot;.
    :type api_version: str
    :param cluster_configuration_upgrade_description: Parameters for a standalone cluster configuration upgrade.
    :type cluster_configuration_upgrade_description: dict | bytes
    :param timeout: The server timeout for performing the operation in seconds. This specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds.
    :type timeout: int

    """
    cluster_configuration_upgrade_description = ClusterConfigurationUpgradeDescription.from_dict(cluster_configuration_upgrade_description)
    return web.Response(status=200)


async def start_cluster_upgrade(request: web.Request, api_version, start_cluster_upgrade_description, timeout=None) -> web.Response:
    """Start upgrading the code or configuration version of a Service Fabric cluster.

    Validate the supplied upgrade parameters and start upgrading the code or configuration version of a Service Fabric cluster if the parameters are valid.

    :param api_version: The version of the API. This is a required parameter and it&#39;s value must be \&quot;6.0\&quot;.
    :type api_version: str
    :param start_cluster_upgrade_description: Describes the parameters for starting a cluster upgrade.
    :type start_cluster_upgrade_description: dict | bytes
    :param timeout: The server timeout for performing the operation in seconds. This specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds.
    :type timeout: int

    """
    start_cluster_upgrade_description = StartClusterUpgradeDescription.from_dict(start_cluster_upgrade_description)
    return web.Response(status=200)


async def unprovision_cluster(request: web.Request, api_version, unprovision_fabric_description, timeout=None) -> web.Response:
    """Unprovision the code or configuration packages of a Service Fabric cluster.

    Unprovision the code or configuration packages of a Service Fabric cluster.

    :param api_version: The version of the API. This is a required parameter and it&#39;s value must be \&quot;6.0\&quot;.
    :type api_version: str
    :param unprovision_fabric_description: Describes the parameters for unprovisioning a cluster.
    :type unprovision_fabric_description: dict | bytes
    :param timeout: The server timeout for performing the operation in seconds. This specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds.
    :type timeout: int

    """
    unprovision_fabric_description = UnprovisionFabricDescription.from_dict(unprovision_fabric_description)
    return web.Response(status=200)


async def update_cluster_upgrade(request: web.Request, api_version, update_cluster_upgrade_description, timeout=None) -> web.Response:
    """Update the upgrade parameters of a Service Fabric cluster upgrade.

    Update the upgrade parameters of a Service Fabric cluster upgrade.

    :param api_version: The version of the API. This is a required parameter and it&#39;s value must be \&quot;6.0\&quot;.
    :type api_version: str
    :param update_cluster_upgrade_description: Parameters for updating a cluster upgrade.
    :type update_cluster_upgrade_description: dict | bytes
    :param timeout: The server timeout for performing the operation in seconds. This specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds.
    :type timeout: int

    """
    update_cluster_upgrade_description = UpdateClusterUpgradeDescription.from_dict(update_cluster_upgrade_description)
    return web.Response(status=200)
