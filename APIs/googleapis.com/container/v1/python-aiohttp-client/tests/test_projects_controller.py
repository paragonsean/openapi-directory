# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.cancel_operation_request import CancelOperationRequest
from openapi_server.models.check_autopilot_compatibility_response import CheckAutopilotCompatibilityResponse
from openapi_server.models.cluster import Cluster
from openapi_server.models.complete_ip_rotation_request import CompleteIPRotationRequest
from openapi_server.models.create_cluster_request import CreateClusterRequest
from openapi_server.models.create_node_pool_request import CreateNodePoolRequest
from openapi_server.models.get_json_web_keys_response import GetJSONWebKeysResponse
from openapi_server.models.get_open_id_config_response import GetOpenIDConfigResponse
from openapi_server.models.list_clusters_response import ListClustersResponse
from openapi_server.models.list_node_pools_response import ListNodePoolsResponse
from openapi_server.models.list_operations_response import ListOperationsResponse
from openapi_server.models.list_usable_subnetworks_response import ListUsableSubnetworksResponse
from openapi_server.models.node_pool import NodePool
from openapi_server.models.operation import Operation
from openapi_server.models.rollback_node_pool_upgrade_request import RollbackNodePoolUpgradeRequest
from openapi_server.models.server_config import ServerConfig
from openapi_server.models.set_addons_config_request import SetAddonsConfigRequest
from openapi_server.models.set_labels_request import SetLabelsRequest
from openapi_server.models.set_legacy_abac_request import SetLegacyAbacRequest
from openapi_server.models.set_locations_request import SetLocationsRequest
from openapi_server.models.set_logging_service_request import SetLoggingServiceRequest
from openapi_server.models.set_maintenance_policy_request import SetMaintenancePolicyRequest
from openapi_server.models.set_master_auth_request import SetMasterAuthRequest
from openapi_server.models.set_monitoring_service_request import SetMonitoringServiceRequest
from openapi_server.models.set_network_policy_request import SetNetworkPolicyRequest
from openapi_server.models.set_node_pool_autoscaling_request import SetNodePoolAutoscalingRequest
from openapi_server.models.set_node_pool_management_request import SetNodePoolManagementRequest
from openapi_server.models.set_node_pool_size_request import SetNodePoolSizeRequest
from openapi_server.models.start_ip_rotation_request import StartIPRotationRequest
from openapi_server.models.update_cluster_request import UpdateClusterRequest
from openapi_server.models.update_master_request import UpdateMasterRequest
from openapi_server.models.update_node_pool_request import UpdateNodePoolRequest


pytestmark = pytest.mark.asyncio

async def test_container_projects_aggregated_usable_subnetworks_list(client):
    """Test case for container_projects_aggregated_usable_subnetworks_list

    
    """
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example'),
                    ('filter', 'filter_example'),
                    ('pageSize', 56),
                    ('pageToken', 'page_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/{parent}/aggregated/usableSubnetworks'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_container_projects_locations_clusters_check_autopilot_compatibility(client):
    """Test case for container_projects_locations_clusters_check_autopilot_compatibility

    
    """
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/{namecheck_autopilot_compatibilit}'.format(name='name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_container_projects_locations_clusters_complete_ip_rotation(client):
    """Test case for container_projects_locations_clusters_complete_ip_rotation

    
    """
    body = {"zone":"zone","name":"name","clusterId":"clusterId","projectId":"projectId"}
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/{namecomplete_ip_rotatio}'.format(name='name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_container_projects_locations_clusters_create(client):
    """Test case for container_projects_locations_clusters_create

    
    """
    body = {"cluster":{"addonsConfig":{"kubernetesDashboard":{"disabled":True},"configConnectorConfig":{"enabled":True},"statefulHaConfig":{"enabled":True},"gkeBackupAgentConfig":{"enabled":True},"gcePersistentDiskCsiDriverConfig":{"enabled":True},"httpLoadBalancing":{"disabled":True},"cloudRunConfig":{"loadBalancerType":"LOAD_BALANCER_TYPE_UNSPECIFIED","disabled":True},"networkPolicyConfig":{"disabled":True},"horizontalPodAutoscaling":{"disabled":True},"dnsCacheConfig":{"enabled":True},"gcsFuseCsiDriverConfig":{"enabled":True},"gcpFilestoreCsiDriverConfig":{"enabled":True}},"fleet":{"preRegistered":True,"project":"project","membership":"membership"},"parentProductConfig":{"productName":"productName","labels":{"key":"labels"}},"resourceUsageExportConfig":{"consumptionMeteringConfig":{"enabled":True},"bigqueryDestination":{"datasetId":"datasetId"},"enableNetworkEgressMetering":True},"autopilot":{"workloadPolicyConfig":{"allowNetAdmin":True},"enabled":True},"masterAuthorizedNetworksConfig":{"gcpPublicCidrsAccessEnabled":True,"cidrBlocks":[{"displayName":"displayName","cidrBlock":"cidrBlock"},{"displayName":"displayName","cidrBlock":"cidrBlock"}],"enabled":True},"databaseEncryption":{"keyName":"keyName","state":"UNKNOWN"},"currentMasterVersion":"currentMasterVersion","monitoringConfig":{"advancedDatapathObservabilityConfig":{"relayMode":"RELAY_MODE_UNSPECIFIED","enableMetrics":True,"enableRelay":True},"componentConfig":{"enableComponents":["COMPONENT_UNSPECIFIED","COMPONENT_UNSPECIFIED"]},"managedPrometheusConfig":{"enabled":True}},"meshCertificates":{"enableCertificates":True},"zone":"zone","enterpriseConfig":{"clusterTier":"CLUSTER_TIER_UNSPECIFIED"},"securityPostureConfig":{"mode":"MODE_UNSPECIFIED","vulnerabilityMode":"VULNERABILITY_MODE_UNSPECIFIED"},"enableKubernetesAlpha":True,"id":"id","nodePools":[{"updateInfo":{"blueGreenInfo":{"phase":"PHASE_UNSPECIFIED","blueInstanceGroupUrls":["blueInstanceGroupUrls","blueInstanceGroupUrls"],"greenInstanceGroupUrls":["greenInstanceGroupUrls","greenInstanceGroupUrls"],"bluePoolDeletionStartTime":"bluePoolDeletionStartTime","greenPoolVersion":"greenPoolVersion"}},"podIpv4CidrSize":9,"bestEffortProvisioning":{"minProvisionNodes":4,"enabled":True},"maxPodsConstraint":{"maxPodsPerNode":"maxPodsPerNode"},"networkConfig":{"podCidrOverprovisionConfig":{"disable":True},"enablePrivateNodes":True,"additionalNodeNetworkConfigs":[{"subnetwork":"subnetwork","network":"network"},{"subnetwork":"subnetwork","network":"network"}],"podRange":"podRange","podIpv4RangeUtilization":9.965781217890562,"networkPerformanceConfig":{"totalEgressBandwidthTier":"TIER_UNSPECIFIED"},"additionalPodNetworkConfigs":[{"secondaryPodRange":"secondaryPodRange","subnetwork":"subnetwork","maxPodsPerNode":{"maxPodsPerNode":"maxPodsPerNode"}},{"secondaryPodRange":"secondaryPodRange","subnetwork":"subnetwork","maxPodsPerNode":{"maxPodsPerNode":"maxPodsPerNode"}}],"podIpv4CidrBlock":"podIpv4CidrBlock","createPodRange":True},"upgradeSettings":{"maxSurge":5,"maxUnavailable":5,"blueGreenSettings":{"standardRolloutPolicy":{"batchSoakDuration":"batchSoakDuration","batchPercentage":1.4658129,"batchNodeCount":6},"nodePoolSoakDuration":"nodePoolSoakDuration"},"strategy":"NODE_POOL_UPDATE_STRATEGY_UNSPECIFIED"},"queuedProvisioning":{"enabled":True},"version":"version","statusMessage":"statusMessage","selfLink":"selfLink","initialNodeCount":5,"instanceGroupUrls":["instanceGroupUrls","instanceGroupUrls"],"management":{"autoUpgrade":True,"upgradeOptions":{"autoUpgradeStartTime":"autoUpgradeStartTime","description":"description"},"autoRepair":True},"name":"name","placementPolicy":{"policyName":"policyName","tpuTopology":"tpuTopology","type":"TYPE_UNSPECIFIED"},"etag":"etag","locations":["locations","locations"],"autoscaling":{"locationPolicy":"LOCATION_POLICY_UNSPECIFIED","autoprovisioned":True,"minNodeCount":6,"totalMinNodeCount":1,"maxNodeCount":1,"totalMaxNodeCount":7,"enabled":True},"conditions":[{"code":"UNKNOWN","message":"message","canonicalCode":"OK"},{"code":"UNKNOWN","message":"message","canonicalCode":"OK"}],"config":{"metadata":{"key":"metadata"},"gcfsConfig":{"enabled":True},"reservationAffinity":{"consumeReservationType":"UNSPECIFIED","values":["values","values"],"key":"key"},"oauthScopes":["oauthScopes","oauthScopes"],"linuxNodeConfig":{"cgroupMode":"CGROUP_MODE_UNSPECIFIED","sysctls":{"key":"sysctls"}},"minCpuPlatform":"minCpuPlatform","kubeletConfig":{"podPidsLimit":"podPidsLimit","insecureKubeletReadonlyPortEnabled":True,"cpuManagerPolicy":"cpuManagerPolicy","cpuCfsQuotaPeriod":"cpuCfsQuotaPeriod","cpuCfsQuota":True},"windowsNodeConfig":{"osVersion":"OS_VERSION_UNSPECIFIED"},"bootDiskKmsKey":"bootDiskKmsKey","enableConfidentialStorage":True,"diskType":"diskType","gvnic":{"enabled":True},"imageType":"imageType","localSsdCount":1,"machineType":"machineType","advancedMachineFeatures":{"threadsPerCore":"threadsPerCore"},"shieldedInstanceConfig":{"enableIntegrityMonitoring":True,"enableSecureBoot":True},"soleTenantConfig":{"nodeAffinities":[{"values":["values","values"],"key":"key","operator":"OPERATOR_UNSPECIFIED"},{"values":["values","values"],"key":"key","operator":"OPERATOR_UNSPECIFIED"}]},"serviceAccount":"serviceAccount","taints":[{"effect":"EFFECT_UNSPECIFIED","value":"value","key":"key"},{"effect":"EFFECT_UNSPECIFIED","value":"value","key":"key"}],"sandboxConfig":{"type":"UNSPECIFIED"},"nodeGroup":"nodeGroup","confidentialNodes":{"enabled":True},"labels":{"key":"labels"},"tags":["tags","tags"],"workloadMetadataConfig":{"mode":"MODE_UNSPECIFIED"},"resourceManagerTags":{"tags":{"key":"tags"}},"preemptible":True,"fastSocket":{"enabled":True},"loggingConfig":{"variantConfig":{"variant":"VARIANT_UNSPECIFIED"}},"spot":True,"resourceLabels":{"key":"resourceLabels"},"accelerators":[{"acceleratorType":"acceleratorType","gpuSharingConfig":{"gpuSharingStrategy":"GPU_SHARING_STRATEGY_UNSPECIFIED","maxSharedClientsPerGpu":"maxSharedClientsPerGpu"},"acceleratorCount":"acceleratorCount","gpuDriverInstallationConfig":{"gpuDriverVersion":"GPU_DRIVER_VERSION_UNSPECIFIED"},"gpuPartitionSize":"gpuPartitionSize"},{"acceleratorType":"acceleratorType","gpuSharingConfig":{"gpuSharingStrategy":"GPU_SHARING_STRATEGY_UNSPECIFIED","maxSharedClientsPerGpu":"maxSharedClientsPerGpu"},"acceleratorCount":"acceleratorCount","gpuDriverInstallationConfig":{"gpuDriverVersion":"GPU_DRIVER_VERSION_UNSPECIFIED"},"gpuPartitionSize":"gpuPartitionSize"}],"ephemeralStorageLocalSsdConfig":{"localSsdCount":4},"localNvmeSsdBlockConfig":{"localSsdCount":7},"secondaryBootDisks":[{"mode":"MODE_UNSPECIFIED","diskImage":"diskImage"},{"mode":"MODE_UNSPECIFIED","diskImage":"diskImage"}],"diskSizeGb":2},"status":"STATUS_UNSPECIFIED"},{"updateInfo":{"blueGreenInfo":{"phase":"PHASE_UNSPECIFIED","blueInstanceGroupUrls":["blueInstanceGroupUrls","blueInstanceGroupUrls"],"greenInstanceGroupUrls":["greenInstanceGroupUrls","greenInstanceGroupUrls"],"bluePoolDeletionStartTime":"bluePoolDeletionStartTime","greenPoolVersion":"greenPoolVersion"}},"podIpv4CidrSize":9,"bestEffortProvisioning":{"minProvisionNodes":4,"enabled":True},"maxPodsConstraint":{"maxPodsPerNode":"maxPodsPerNode"},"networkConfig":{"podCidrOverprovisionConfig":{"disable":True},"enablePrivateNodes":True,"additionalNodeNetworkConfigs":[{"subnetwork":"subnetwork","network":"network"},{"subnetwork":"subnetwork","network":"network"}],"podRange":"podRange","podIpv4RangeUtilization":9.965781217890562,"networkPerformanceConfig":{"totalEgressBandwidthTier":"TIER_UNSPECIFIED"},"additionalPodNetworkConfigs":[{"secondaryPodRange":"secondaryPodRange","subnetwork":"subnetwork","maxPodsPerNode":{"maxPodsPerNode":"maxPodsPerNode"}},{"secondaryPodRange":"secondaryPodRange","subnetwork":"subnetwork","maxPodsPerNode":{"maxPodsPerNode":"maxPodsPerNode"}}],"podIpv4CidrBlock":"podIpv4CidrBlock","createPodRange":True},"upgradeSettings":{"maxSurge":5,"maxUnavailable":5,"blueGreenSettings":{"standardRolloutPolicy":{"batchSoakDuration":"batchSoakDuration","batchPercentage":1.4658129,"batchNodeCount":6},"nodePoolSoakDuration":"nodePoolSoakDuration"},"strategy":"NODE_POOL_UPDATE_STRATEGY_UNSPECIFIED"},"queuedProvisioning":{"enabled":True},"version":"version","statusMessage":"statusMessage","selfLink":"selfLink","initialNodeCount":5,"instanceGroupUrls":["instanceGroupUrls","instanceGroupUrls"],"management":{"autoUpgrade":True,"upgradeOptions":{"autoUpgradeStartTime":"autoUpgradeStartTime","description":"description"},"autoRepair":True},"name":"name","placementPolicy":{"policyName":"policyName","tpuTopology":"tpuTopology","type":"TYPE_UNSPECIFIED"},"etag":"etag","locations":["locations","locations"],"autoscaling":{"locationPolicy":"LOCATION_POLICY_UNSPECIFIED","autoprovisioned":True,"minNodeCount":6,"totalMinNodeCount":1,"maxNodeCount":1,"totalMaxNodeCount":7,"enabled":True},"conditions":[{"code":"UNKNOWN","message":"message","canonicalCode":"OK"},{"code":"UNKNOWN","message":"message","canonicalCode":"OK"}],"config":{"metadata":{"key":"metadata"},"gcfsConfig":{"enabled":True},"reservationAffinity":{"consumeReservationType":"UNSPECIFIED","values":["values","values"],"key":"key"},"oauthScopes":["oauthScopes","oauthScopes"],"linuxNodeConfig":{"cgroupMode":"CGROUP_MODE_UNSPECIFIED","sysctls":{"key":"sysctls"}},"minCpuPlatform":"minCpuPlatform","kubeletConfig":{"podPidsLimit":"podPidsLimit","insecureKubeletReadonlyPortEnabled":True,"cpuManagerPolicy":"cpuManagerPolicy","cpuCfsQuotaPeriod":"cpuCfsQuotaPeriod","cpuCfsQuota":True},"windowsNodeConfig":{"osVersion":"OS_VERSION_UNSPECIFIED"},"bootDiskKmsKey":"bootDiskKmsKey","enableConfidentialStorage":True,"diskType":"diskType","gvnic":{"enabled":True},"imageType":"imageType","localSsdCount":1,"machineType":"machineType","advancedMachineFeatures":{"threadsPerCore":"threadsPerCore"},"shieldedInstanceConfig":{"enableIntegrityMonitoring":True,"enableSecureBoot":True},"soleTenantConfig":{"nodeAffinities":[{"values":["values","values"],"key":"key","operator":"OPERATOR_UNSPECIFIED"},{"values":["values","values"],"key":"key","operator":"OPERATOR_UNSPECIFIED"}]},"serviceAccount":"serviceAccount","taints":[{"effect":"EFFECT_UNSPECIFIED","value":"value","key":"key"},{"effect":"EFFECT_UNSPECIFIED","value":"value","key":"key"}],"sandboxConfig":{"type":"UNSPECIFIED"},"nodeGroup":"nodeGroup","confidentialNodes":{"enabled":True},"labels":{"key":"labels"},"tags":["tags","tags"],"workloadMetadataConfig":{"mode":"MODE_UNSPECIFIED"},"resourceManagerTags":{"tags":{"key":"tags"}},"preemptible":True,"fastSocket":{"enabled":True},"loggingConfig":{"variantConfig":{"variant":"VARIANT_UNSPECIFIED"}},"spot":True,"resourceLabels":{"key":"resourceLabels"},"accelerators":[{"acceleratorType":"acceleratorType","gpuSharingConfig":{"gpuSharingStrategy":"GPU_SHARING_STRATEGY_UNSPECIFIED","maxSharedClientsPerGpu":"maxSharedClientsPerGpu"},"acceleratorCount":"acceleratorCount","gpuDriverInstallationConfig":{"gpuDriverVersion":"GPU_DRIVER_VERSION_UNSPECIFIED"},"gpuPartitionSize":"gpuPartitionSize"},{"acceleratorType":"acceleratorType","gpuSharingConfig":{"gpuSharingStrategy":"GPU_SHARING_STRATEGY_UNSPECIFIED","maxSharedClientsPerGpu":"maxSharedClientsPerGpu"},"acceleratorCount":"acceleratorCount","gpuDriverInstallationConfig":{"gpuDriverVersion":"GPU_DRIVER_VERSION_UNSPECIFIED"},"gpuPartitionSize":"gpuPartitionSize"}],"ephemeralStorageLocalSsdConfig":{"localSsdCount":4},"localNvmeSsdBlockConfig":{"localSsdCount":7},"secondaryBootDisks":[{"mode":"MODE_UNSPECIFIED","diskImage":"diskImage"},{"mode":"MODE_UNSPECIFIED","diskImage":"diskImage"}],"diskSizeGb":2},"status":"STATUS_UNSPECIFIED"}],"binaryAuthorization":{"evaluationMode":"EVALUATION_MODE_UNSPECIFIED","enabled":True},"enableK8sBetaApis":{"enabledApis":["enabledApis","enabledApis"]},"networkPolicy":{"provider":"PROVIDER_UNSPECIFIED","enabled":True},"currentNodeCount":2,"loggingService":"loggingService","enableTpu":True,"maintenancePolicy":{"resourceVersion":"resourceVersion","window":{"dailyMaintenanceWindow":{"duration":"duration","startTime":"startTime"},"maintenanceExclusions":{"key":{"maintenanceExclusionOptions":{"scope":"NO_UPGRADES"},"startTime":"startTime","endTime":"endTime"}},"recurringWindow":{"recurrence":"recurrence","window":{"maintenanceExclusionOptions":{"scope":"NO_UPGRADES"},"startTime":"startTime","endTime":"endTime"}}}},"instanceGroupUrls":["instanceGroupUrls","instanceGroupUrls"],"releaseChannel":{"channel":"UNSPECIFIED"},"expireTime":"expireTime","nodeIpv4CidrSize":1,"subnetwork":"subnetwork","name":"name","resourceLabels":{"key":"resourceLabels"},"authenticatorGroupsConfig":{"securityGroup":"securityGroup","enabled":True},"etag":"etag","autoscaling":{"autoprovisioningLocations":["autoprovisioningLocations","autoprovisioningLocations"],"autoscalingProfile":"PROFILE_UNSPECIFIED","resourceLimits":[{"maximum":"maximum","minimum":"minimum","resourceType":"resourceType"},{"maximum":"maximum","minimum":"minimum","resourceType":"resourceType"}],"autoprovisioningNodePoolDefaults":{"shieldedInstanceConfig":{"enableIntegrityMonitoring":True,"enableSecureBoot":True},"management":{"autoUpgrade":True,"upgradeOptions":{"autoUpgradeStartTime":"autoUpgradeStartTime","description":"description"},"autoRepair":True},"minCpuPlatform":"minCpuPlatform","insecureKubeletReadonlyPortEnabled":True,"bootDiskKmsKey":"bootDiskKmsKey","upgradeSettings":{"maxSurge":5,"maxUnavailable":5,"blueGreenSettings":{"standardRolloutPolicy":{"batchSoakDuration":"batchSoakDuration","batchPercentage":1.4658129,"batchNodeCount":6},"nodePoolSoakDuration":"nodePoolSoakDuration"},"strategy":"NODE_POOL_UPDATE_STRATEGY_UNSPECIFIED"},"serviceAccount":"serviceAccount","diskType":"diskType","oauthScopes":["oauthScopes","oauthScopes"],"imageType":"imageType","diskSizeGb":0},"enableNodeAutoprovisioning":True},"conditions":[{"code":"UNKNOWN","message":"message","canonicalCode":"OK"},{"code":"UNKNOWN","message":"message","canonicalCode":"OK"}],"status":"STATUS_UNSPECIFIED","nodePoolAutoConfig":{"resourceManagerTags":{"tags":{"key":"tags"}},"networkTags":{"tags":["tags","tags"]}},"defaultMaxPodsConstraint":{"maxPodsPerNode":"maxPodsPerNode"},"masterAuth":{"clientCertificateConfig":{"issueClientCertificate":True},"clientCertificate":"clientCertificate","password":"password","clientKey":"clientKey","clusterCaCertificate":"clusterCaCertificate","username":"username"},"verticalPodAutoscaling":{"enabled":True},"description":"description","costManagementConfig":{"enabled":True},"labelFingerprint":"labelFingerprint","ipAllocationPolicy":{"clusterIpv4CidrBlock":"clusterIpv4CidrBlock","createSubnetwork":True,"clusterIpv4Cidr":"clusterIpv4Cidr","servicesIpv4CidrBlock":"servicesIpv4CidrBlock","servicesSecondaryRangeName":"servicesSecondaryRangeName","nodeIpv4Cidr":"nodeIpv4Cidr","ipv6AccessType":"IPV6_ACCESS_TYPE_UNSPECIFIED","subnetworkName":"subnetworkName","podCidrOverprovisionConfig":{"disable":True},"useRoutes":True,"useIpAliases":True,"tpuIpv4CidrBlock":"tpuIpv4CidrBlock","additionalPodRangesConfig":{"podRangeInfo":[{"rangeName":"rangeName","utilization":9.301444243932576},{"rangeName":"rangeName","utilization":9.301444243932576}],"podRangeNames":["podRangeNames","podRangeNames"]},"servicesIpv6CidrBlock":"servicesIpv6CidrBlock","servicesIpv4Cidr":"servicesIpv4Cidr","clusterSecondaryRangeName":"clusterSecondaryRangeName","defaultPodIpv4RangeUtilization":3.616076749251911,"nodeIpv4CidrBlock":"nodeIpv4CidrBlock","stackType":"STACK_TYPE_UNSPECIFIED","subnetIpv6CidrBlock":"subnetIpv6CidrBlock"},"nodeConfig":{"metadata":{"key":"metadata"},"gcfsConfig":{"enabled":True},"reservationAffinity":{"consumeReservationType":"UNSPECIFIED","values":["values","values"],"key":"key"},"oauthScopes":["oauthScopes","oauthScopes"],"linuxNodeConfig":{"cgroupMode":"CGROUP_MODE_UNSPECIFIED","sysctls":{"key":"sysctls"}},"minCpuPlatform":"minCpuPlatform","kubeletConfig":{"podPidsLimit":"podPidsLimit","insecureKubeletReadonlyPortEnabled":True,"cpuManagerPolicy":"cpuManagerPolicy","cpuCfsQuotaPeriod":"cpuCfsQuotaPeriod","cpuCfsQuota":True},"windowsNodeConfig":{"osVersion":"OS_VERSION_UNSPECIFIED"},"bootDiskKmsKey":"bootDiskKmsKey","enableConfidentialStorage":True,"diskType":"diskType","gvnic":{"enabled":True},"imageType":"imageType","localSsdCount":1,"machineType":"machineType","advancedMachineFeatures":{"threadsPerCore":"threadsPerCore"},"shieldedInstanceConfig":{"enableIntegrityMonitoring":True,"enableSecureBoot":True},"soleTenantConfig":{"nodeAffinities":[{"values":["values","values"],"key":"key","operator":"OPERATOR_UNSPECIFIED"},{"values":["values","values"],"key":"key","operator":"OPERATOR_UNSPECIFIED"}]},"serviceAccount":"serviceAccount","taints":[{"effect":"EFFECT_UNSPECIFIED","value":"value","key":"key"},{"effect":"EFFECT_UNSPECIFIED","value":"value","key":"key"}],"sandboxConfig":{"type":"UNSPECIFIED"},"nodeGroup":"nodeGroup","confidentialNodes":{"enabled":True},"labels":{"key":"labels"},"tags":["tags","tags"],"workloadMetadataConfig":{"mode":"MODE_UNSPECIFIED"},"resourceManagerTags":{"tags":{"key":"tags"}},"preemptible":True,"fastSocket":{"enabled":True},"loggingConfig":{"variantConfig":{"variant":"VARIANT_UNSPECIFIED"}},"spot":True,"resourceLabels":{"key":"resourceLabels"},"accelerators":[{"acceleratorType":"acceleratorType","gpuSharingConfig":{"gpuSharingStrategy":"GPU_SHARING_STRATEGY_UNSPECIFIED","maxSharedClientsPerGpu":"maxSharedClientsPerGpu"},"acceleratorCount":"acceleratorCount","gpuDriverInstallationConfig":{"gpuDriverVersion":"GPU_DRIVER_VERSION_UNSPECIFIED"},"gpuPartitionSize":"gpuPartitionSize"},{"acceleratorType":"acceleratorType","gpuSharingConfig":{"gpuSharingStrategy":"GPU_SHARING_STRATEGY_UNSPECIFIED","maxSharedClientsPerGpu":"maxSharedClientsPerGpu"},"acceleratorCount":"acceleratorCount","gpuDriverInstallationConfig":{"gpuDriverVersion":"GPU_DRIVER_VERSION_UNSPECIFIED"},"gpuPartitionSize":"gpuPartitionSize"}],"ephemeralStorageLocalSsdConfig":{"localSsdCount":4},"localNvmeSsdBlockConfig":{"localSsdCount":7},"secondaryBootDisks":[{"mode":"MODE_UNSPECIFIED","diskImage":"diskImage"},{"mode":"MODE_UNSPECIFIED","diskImage":"diskImage"}],"diskSizeGb":2},"network":"network","endpoint":"endpoint","initialNodeCount":7,"shieldedNodes":{"enabled":True},"initialClusterVersion":"initialClusterVersion","privateClusterConfig":{"enablePrivateEndpoint":True,"publicEndpoint":"publicEndpoint","masterGlobalAccessConfig":{"enabled":True},"enablePrivateNodes":True,"privateEndpointSubnetwork":"privateEndpointSubnetwork","peeringName":"peeringName","privateEndpoint":"privateEndpoint","masterIpv4CidrBlock":"masterIpv4CidrBlock"},"legacyAbac":{"enabled":True},"clusterIpv4Cidr":"clusterIpv4Cidr","monitoringService":"monitoringService","workloadIdentityConfig":{"workloadPool":"workloadPool"},"networkConfig":{"defaultSnatStatus":{"disabled":True},"dnsConfig":{"clusterDnsDomain":"clusterDnsDomain","clusterDnsScope":"DNS_SCOPE_UNSPECIFIED","clusterDns":"PROVIDER_UNSPECIFIED"},"enableMultiNetworking":True,"serviceExternalIpsConfig":{"enabled":True},"network":"network","privateIpv6GoogleAccess":"PRIVATE_IPV6_GOOGLE_ACCESS_UNSPECIFIED","enableL4ilbSubsetting":True,"datapathProvider":"DATAPATH_PROVIDER_UNSPECIFIED","gatewayApiConfig":{"channel":"CHANNEL_UNSPECIFIED"},"enableFqdnNetworkPolicy":True,"subnetwork":"subnetwork","enableIntraNodeVisibility":True,"networkPerformanceConfig":{"totalEgressBandwidthTier":"TIER_UNSPECIFIED"},"inTransitEncryptionConfig":"IN_TRANSIT_ENCRYPTION_CONFIG_UNSPECIFIED"},"statusMessage":"statusMessage","confidentialNodes":{"enabled":True},"selfLink":"selfLink","identityServiceConfig":{"enabled":True},"currentNodeVersion":"currentNodeVersion","tpuIpv4CidrBlock":"tpuIpv4CidrBlock","createTime":"createTime","loggingConfig":{"componentConfig":{"enableComponents":["COMPONENT_UNSPECIFIED","COMPONENT_UNSPECIFIED"]}},"servicesIpv4Cidr":"servicesIpv4Cidr","location":"location","locations":["locations","locations"],"nodePoolDefaults":{"nodeConfigDefaults":{"gcfsConfig":{"enabled":True},"loggingConfig":{"variantConfig":{"variant":"VARIANT_UNSPECIFIED"}}}},"notificationConfig":{"pubsub":{"filter":{"eventType":["EVENT_TYPE_UNSPECIFIED","EVENT_TYPE_UNSPECIFIED"]},"topic":"topic","enabled":True}}},"parent":"parent","zone":"zone","projectId":"projectId"}
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/{parent}/clusters'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_container_projects_locations_clusters_get_jwks(client):
    """Test case for container_projects_locations_clusters_get_jwks

    
    """
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v1/{parent}/jwks'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_container_projects_locations_clusters_list(client):
    """Test case for container_projects_locations_clusters_list

    
    """
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example'),
                    ('projectId', 'project_id_example'),
                    ('zone', 'zone_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/{parent}/clusters'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_container_projects_locations_clusters_node_pools_complete_upgrade(client):
    """Test case for container_projects_locations_clusters_node_pools_complete_upgrade

    
    """
    body = None
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/{namecomplete_upgrad}'.format(name='name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_container_projects_locations_clusters_node_pools_create(client):
    """Test case for container_projects_locations_clusters_node_pools_create

    
    """
    body = {"nodePool":{"updateInfo":{"blueGreenInfo":{"phase":"PHASE_UNSPECIFIED","blueInstanceGroupUrls":["blueInstanceGroupUrls","blueInstanceGroupUrls"],"greenInstanceGroupUrls":["greenInstanceGroupUrls","greenInstanceGroupUrls"],"bluePoolDeletionStartTime":"bluePoolDeletionStartTime","greenPoolVersion":"greenPoolVersion"}},"podIpv4CidrSize":9,"bestEffortProvisioning":{"minProvisionNodes":4,"enabled":True},"maxPodsConstraint":{"maxPodsPerNode":"maxPodsPerNode"},"networkConfig":{"podCidrOverprovisionConfig":{"disable":True},"enablePrivateNodes":True,"additionalNodeNetworkConfigs":[{"subnetwork":"subnetwork","network":"network"},{"subnetwork":"subnetwork","network":"network"}],"podRange":"podRange","podIpv4RangeUtilization":9.965781217890562,"networkPerformanceConfig":{"totalEgressBandwidthTier":"TIER_UNSPECIFIED"},"additionalPodNetworkConfigs":[{"secondaryPodRange":"secondaryPodRange","subnetwork":"subnetwork","maxPodsPerNode":{"maxPodsPerNode":"maxPodsPerNode"}},{"secondaryPodRange":"secondaryPodRange","subnetwork":"subnetwork","maxPodsPerNode":{"maxPodsPerNode":"maxPodsPerNode"}}],"podIpv4CidrBlock":"podIpv4CidrBlock","createPodRange":True},"upgradeSettings":{"maxSurge":5,"maxUnavailable":5,"blueGreenSettings":{"standardRolloutPolicy":{"batchSoakDuration":"batchSoakDuration","batchPercentage":1.4658129,"batchNodeCount":6},"nodePoolSoakDuration":"nodePoolSoakDuration"},"strategy":"NODE_POOL_UPDATE_STRATEGY_UNSPECIFIED"},"queuedProvisioning":{"enabled":True},"version":"version","statusMessage":"statusMessage","selfLink":"selfLink","initialNodeCount":5,"instanceGroupUrls":["instanceGroupUrls","instanceGroupUrls"],"management":{"autoUpgrade":True,"upgradeOptions":{"autoUpgradeStartTime":"autoUpgradeStartTime","description":"description"},"autoRepair":True},"name":"name","placementPolicy":{"policyName":"policyName","tpuTopology":"tpuTopology","type":"TYPE_UNSPECIFIED"},"etag":"etag","locations":["locations","locations"],"autoscaling":{"locationPolicy":"LOCATION_POLICY_UNSPECIFIED","autoprovisioned":True,"minNodeCount":6,"totalMinNodeCount":1,"maxNodeCount":1,"totalMaxNodeCount":7,"enabled":True},"conditions":[{"code":"UNKNOWN","message":"message","canonicalCode":"OK"},{"code":"UNKNOWN","message":"message","canonicalCode":"OK"}],"config":{"metadata":{"key":"metadata"},"gcfsConfig":{"enabled":True},"reservationAffinity":{"consumeReservationType":"UNSPECIFIED","values":["values","values"],"key":"key"},"oauthScopes":["oauthScopes","oauthScopes"],"linuxNodeConfig":{"cgroupMode":"CGROUP_MODE_UNSPECIFIED","sysctls":{"key":"sysctls"}},"minCpuPlatform":"minCpuPlatform","kubeletConfig":{"podPidsLimit":"podPidsLimit","insecureKubeletReadonlyPortEnabled":True,"cpuManagerPolicy":"cpuManagerPolicy","cpuCfsQuotaPeriod":"cpuCfsQuotaPeriod","cpuCfsQuota":True},"windowsNodeConfig":{"osVersion":"OS_VERSION_UNSPECIFIED"},"bootDiskKmsKey":"bootDiskKmsKey","enableConfidentialStorage":True,"diskType":"diskType","gvnic":{"enabled":True},"imageType":"imageType","localSsdCount":1,"machineType":"machineType","advancedMachineFeatures":{"threadsPerCore":"threadsPerCore"},"shieldedInstanceConfig":{"enableIntegrityMonitoring":True,"enableSecureBoot":True},"soleTenantConfig":{"nodeAffinities":[{"values":["values","values"],"key":"key","operator":"OPERATOR_UNSPECIFIED"},{"values":["values","values"],"key":"key","operator":"OPERATOR_UNSPECIFIED"}]},"serviceAccount":"serviceAccount","taints":[{"effect":"EFFECT_UNSPECIFIED","value":"value","key":"key"},{"effect":"EFFECT_UNSPECIFIED","value":"value","key":"key"}],"sandboxConfig":{"type":"UNSPECIFIED"},"nodeGroup":"nodeGroup","confidentialNodes":{"enabled":True},"labels":{"key":"labels"},"tags":["tags","tags"],"workloadMetadataConfig":{"mode":"MODE_UNSPECIFIED"},"resourceManagerTags":{"tags":{"key":"tags"}},"preemptible":True,"fastSocket":{"enabled":True},"loggingConfig":{"variantConfig":{"variant":"VARIANT_UNSPECIFIED"}},"spot":True,"resourceLabels":{"key":"resourceLabels"},"accelerators":[{"acceleratorType":"acceleratorType","gpuSharingConfig":{"gpuSharingStrategy":"GPU_SHARING_STRATEGY_UNSPECIFIED","maxSharedClientsPerGpu":"maxSharedClientsPerGpu"},"acceleratorCount":"acceleratorCount","gpuDriverInstallationConfig":{"gpuDriverVersion":"GPU_DRIVER_VERSION_UNSPECIFIED"},"gpuPartitionSize":"gpuPartitionSize"},{"acceleratorType":"acceleratorType","gpuSharingConfig":{"gpuSharingStrategy":"GPU_SHARING_STRATEGY_UNSPECIFIED","maxSharedClientsPerGpu":"maxSharedClientsPerGpu"},"acceleratorCount":"acceleratorCount","gpuDriverInstallationConfig":{"gpuDriverVersion":"GPU_DRIVER_VERSION_UNSPECIFIED"},"gpuPartitionSize":"gpuPartitionSize"}],"ephemeralStorageLocalSsdConfig":{"localSsdCount":4},"localNvmeSsdBlockConfig":{"localSsdCount":7},"secondaryBootDisks":[{"mode":"MODE_UNSPECIFIED","diskImage":"diskImage"},{"mode":"MODE_UNSPECIFIED","diskImage":"diskImage"}],"diskSizeGb":2},"status":"STATUS_UNSPECIFIED"},"parent":"parent","zone":"zone","clusterId":"clusterId","projectId":"projectId"}
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/{parent}/nodePools'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_container_projects_locations_clusters_node_pools_delete(client):
    """Test case for container_projects_locations_clusters_node_pools_delete

    
    """
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example'),
                    ('clusterId', 'cluster_id_example'),
                    ('nodePoolId', 'node_pool_id_example'),
                    ('projectId', 'project_id_example'),
                    ('zone', 'zone_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/v1/{name}'.format(name='name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_container_projects_locations_clusters_node_pools_list(client):
    """Test case for container_projects_locations_clusters_node_pools_list

    
    """
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example'),
                    ('clusterId', 'cluster_id_example'),
                    ('projectId', 'project_id_example'),
                    ('zone', 'zone_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/{parent}/nodePools'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_container_projects_locations_clusters_node_pools_rollback(client):
    """Test case for container_projects_locations_clusters_node_pools_rollback

    
    """
    body = {"nodePoolId":"nodePoolId","zone":"zone","name":"name","clusterId":"clusterId","projectId":"projectId","respectPdb":True}
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/{namerollbac}'.format(name='name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_container_projects_locations_clusters_node_pools_set_autoscaling(client):
    """Test case for container_projects_locations_clusters_node_pools_set_autoscaling

    
    """
    body = {"nodePoolId":"nodePoolId","zone":"zone","name":"name","autoscaling":{"locationPolicy":"LOCATION_POLICY_UNSPECIFIED","autoprovisioned":True,"minNodeCount":6,"totalMinNodeCount":1,"maxNodeCount":1,"totalMaxNodeCount":7,"enabled":True},"clusterId":"clusterId","projectId":"projectId"}
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/{nameset_autoscalin}'.format(name='name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_container_projects_locations_clusters_node_pools_set_management(client):
    """Test case for container_projects_locations_clusters_node_pools_set_management

    
    """
    body = {"nodePoolId":"nodePoolId","management":{"autoUpgrade":True,"upgradeOptions":{"autoUpgradeStartTime":"autoUpgradeStartTime","description":"description"},"autoRepair":True},"zone":"zone","name":"name","clusterId":"clusterId","projectId":"projectId"}
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/{nameset_managemen}'.format(name='name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_container_projects_locations_clusters_node_pools_set_size(client):
    """Test case for container_projects_locations_clusters_node_pools_set_size

    
    """
    body = {"nodePoolId":"nodePoolId","zone":"zone","name":"name","nodeCount":0,"clusterId":"clusterId","projectId":"projectId"}
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/{nameset_siz}'.format(name='name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_container_projects_locations_clusters_node_pools_update(client):
    """Test case for container_projects_locations_clusters_node_pools_update

    
    """
    body = {"gcfsConfig":{"enabled":True},"upgradeSettings":{"maxSurge":5,"maxUnavailable":5,"blueGreenSettings":{"standardRolloutPolicy":{"batchSoakDuration":"batchSoakDuration","batchPercentage":1.4658129,"batchNodeCount":6},"nodePoolSoakDuration":"nodePoolSoakDuration"},"strategy":"NODE_POOL_UPDATE_STRATEGY_UNSPECIFIED"},"clusterId":"clusterId","linuxNodeConfig":{"cgroupMode":"CGROUP_MODE_UNSPECIFIED","sysctls":{"key":"sysctls"}},"queuedProvisioning":{"enabled":True},"zone":"zone","kubeletConfig":{"podPidsLimit":"podPidsLimit","insecureKubeletReadonlyPortEnabled":True,"cpuManagerPolicy":"cpuManagerPolicy","cpuCfsQuotaPeriod":"cpuCfsQuotaPeriod","cpuCfsQuota":True},"windowsNodeConfig":{"osVersion":"OS_VERSION_UNSPECIFIED"},"diskType":"diskType","gvnic":{"enabled":True},"imageType":"imageType","machineType":"machineType","nodePoolId":"nodePoolId","nodeNetworkConfig":{"podCidrOverprovisionConfig":{"disable":True},"enablePrivateNodes":True,"additionalNodeNetworkConfigs":[{"subnetwork":"subnetwork","network":"network"},{"subnetwork":"subnetwork","network":"network"}],"podRange":"podRange","podIpv4RangeUtilization":9.965781217890562,"networkPerformanceConfig":{"totalEgressBandwidthTier":"TIER_UNSPECIFIED"},"additionalPodNetworkConfigs":[{"secondaryPodRange":"secondaryPodRange","subnetwork":"subnetwork","maxPodsPerNode":{"maxPodsPerNode":"maxPodsPerNode"}},{"secondaryPodRange":"secondaryPodRange","subnetwork":"subnetwork","maxPodsPerNode":{"maxPodsPerNode":"maxPodsPerNode"}}],"podIpv4CidrBlock":"podIpv4CidrBlock","createPodRange":True},"nodeVersion":"nodeVersion","taints":{"taints":[{"effect":"EFFECT_UNSPECIFIED","value":"value","key":"key"},{"effect":"EFFECT_UNSPECIFIED","value":"value","key":"key"}]},"confidentialNodes":{"enabled":True},"labels":{"labels":{"key":"labels"}},"tags":{"tags":["tags","tags"]},"workloadMetadataConfig":{"mode":"MODE_UNSPECIFIED"},"resourceManagerTags":{"tags":{"key":"tags"}},"fastSocket":{"enabled":True},"loggingConfig":{"variantConfig":{"variant":"VARIANT_UNSPECIFIED"}},"name":"name","resourceLabels":{"labels":{"key":"labels"}},"etag":"etag","locations":["locations","locations"],"projectId":"projectId","diskSizeGb":"diskSizeGb"}
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/v1/{name}'.format(name='name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_container_projects_locations_clusters_set_addons(client):
    """Test case for container_projects_locations_clusters_set_addons

    
    """
    body = {"addonsConfig":{"kubernetesDashboard":{"disabled":True},"configConnectorConfig":{"enabled":True},"statefulHaConfig":{"enabled":True},"gkeBackupAgentConfig":{"enabled":True},"gcePersistentDiskCsiDriverConfig":{"enabled":True},"httpLoadBalancing":{"disabled":True},"cloudRunConfig":{"loadBalancerType":"LOAD_BALANCER_TYPE_UNSPECIFIED","disabled":True},"networkPolicyConfig":{"disabled":True},"horizontalPodAutoscaling":{"disabled":True},"dnsCacheConfig":{"enabled":True},"gcsFuseCsiDriverConfig":{"enabled":True},"gcpFilestoreCsiDriverConfig":{"enabled":True}},"zone":"zone","name":"name","clusterId":"clusterId","projectId":"projectId"}
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/{nameset_addon}'.format(name='name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_container_projects_locations_clusters_set_legacy_abac(client):
    """Test case for container_projects_locations_clusters_set_legacy_abac

    
    """
    body = {"zone":"zone","name":"name","clusterId":"clusterId","projectId":"projectId","enabled":True}
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/{nameset_legacy_aba}'.format(name='name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_container_projects_locations_clusters_set_locations(client):
    """Test case for container_projects_locations_clusters_set_locations

    
    """
    body = {"zone":"zone","name":"name","locations":["locations","locations"],"clusterId":"clusterId","projectId":"projectId"}
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/{nameset_location}'.format(name='name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_container_projects_locations_clusters_set_logging(client):
    """Test case for container_projects_locations_clusters_set_logging

    
    """
    body = {"zone":"zone","name":"name","clusterId":"clusterId","loggingService":"loggingService","projectId":"projectId"}
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/{nameset_loggin}'.format(name='name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_container_projects_locations_clusters_set_maintenance_policy(client):
    """Test case for container_projects_locations_clusters_set_maintenance_policy

    
    """
    body = {"maintenancePolicy":{"resourceVersion":"resourceVersion","window":{"dailyMaintenanceWindow":{"duration":"duration","startTime":"startTime"},"maintenanceExclusions":{"key":{"maintenanceExclusionOptions":{"scope":"NO_UPGRADES"},"startTime":"startTime","endTime":"endTime"}},"recurringWindow":{"recurrence":"recurrence","window":{"maintenanceExclusionOptions":{"scope":"NO_UPGRADES"},"startTime":"startTime","endTime":"endTime"}}}},"zone":"zone","name":"name","clusterId":"clusterId","projectId":"projectId"}
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/{nameset_maintenance_polic}'.format(name='name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_container_projects_locations_clusters_set_master_auth(client):
    """Test case for container_projects_locations_clusters_set_master_auth

    
    """
    body = {"zone":"zone","name":"name","action":"UNKNOWN","update":{"clientCertificateConfig":{"issueClientCertificate":True},"clientCertificate":"clientCertificate","password":"password","clientKey":"clientKey","clusterCaCertificate":"clusterCaCertificate","username":"username"},"clusterId":"clusterId","projectId":"projectId"}
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/{nameset_master_aut}'.format(name='name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_container_projects_locations_clusters_set_monitoring(client):
    """Test case for container_projects_locations_clusters_set_monitoring

    
    """
    body = {"zone":"zone","monitoringService":"monitoringService","name":"name","clusterId":"clusterId","projectId":"projectId"}
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/{nameset_monitorin}'.format(name='name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_container_projects_locations_clusters_set_network_policy(client):
    """Test case for container_projects_locations_clusters_set_network_policy

    
    """
    body = {"zone":"zone","networkPolicy":{"provider":"PROVIDER_UNSPECIFIED","enabled":True},"name":"name","clusterId":"clusterId","projectId":"projectId"}
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/{nameset_network_polic}'.format(name='name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_container_projects_locations_clusters_set_resource_labels(client):
    """Test case for container_projects_locations_clusters_set_resource_labels

    
    """
    body = {"zone":"zone","name":"name","resourceLabels":{"key":"resourceLabels"},"clusterId":"clusterId","labelFingerprint":"labelFingerprint","projectId":"projectId"}
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/{nameset_resource_label}'.format(name='name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_container_projects_locations_clusters_start_ip_rotation(client):
    """Test case for container_projects_locations_clusters_start_ip_rotation

    
    """
    body = {"rotateCredentials":True,"zone":"zone","name":"name","clusterId":"clusterId","projectId":"projectId"}
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/{namestart_ip_rotatio}'.format(name='name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_container_projects_locations_clusters_update_master(client):
    """Test case for container_projects_locations_clusters_update_master

    
    """
    body = {"zone":"zone","masterVersion":"masterVersion","name":"name","clusterId":"clusterId","projectId":"projectId"}
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/{nameupdate_maste}'.format(name='name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_container_projects_locations_clusters_well_known_get_openid_configuration(client):
    """Test case for container_projects_locations_clusters_well_known_get_openid_configuration

    
    """
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v1/{parent}/.well-known/openid-configuration'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_container_projects_locations_get_server_config(client):
    """Test case for container_projects_locations_get_server_config

    
    """
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example'),
                    ('projectId', 'project_id_example'),
                    ('zone', 'zone_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/{name}/serverConfig'.format(name='name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_container_projects_locations_operations_cancel(client):
    """Test case for container_projects_locations_operations_cancel

    
    """
    body = {"zone":"zone","name":"name","operationId":"operationId","projectId":"projectId"}
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/{namecance}'.format(name='name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_container_projects_locations_operations_get(client):
    """Test case for container_projects_locations_operations_get

    
    """
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example'),
                    ('operationId', 'operation_id_example'),
                    ('projectId', 'project_id_example'),
                    ('zone', 'zone_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/{name}'.format(name='name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_container_projects_locations_operations_list(client):
    """Test case for container_projects_locations_operations_list

    
    """
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example'),
                    ('projectId', 'project_id_example'),
                    ('zone', 'zone_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/{parent}/operations'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_container_projects_zones_clusters_addons(client):
    """Test case for container_projects_zones_clusters_addons

    
    """
    body = {"addonsConfig":{"kubernetesDashboard":{"disabled":True},"configConnectorConfig":{"enabled":True},"statefulHaConfig":{"enabled":True},"gkeBackupAgentConfig":{"enabled":True},"gcePersistentDiskCsiDriverConfig":{"enabled":True},"httpLoadBalancing":{"disabled":True},"cloudRunConfig":{"loadBalancerType":"LOAD_BALANCER_TYPE_UNSPECIFIED","disabled":True},"networkPolicyConfig":{"disabled":True},"horizontalPodAutoscaling":{"disabled":True},"dnsCacheConfig":{"enabled":True},"gcsFuseCsiDriverConfig":{"enabled":True},"gcpFilestoreCsiDriverConfig":{"enabled":True}},"zone":"zone","name":"name","clusterId":"clusterId","projectId":"projectId"}
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/projects/{project_id}/zones/{zone}/clusters/{cluster_id}/addons'.format(project_id='project_id_example', zone='zone_example', cluster_id='cluster_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_container_projects_zones_clusters_complete_ip_rotation(client):
    """Test case for container_projects_zones_clusters_complete_ip_rotation

    
    """
    body = {"zone":"zone","name":"name","clusterId":"clusterId","projectId":"projectId"}
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/projects/{project_id}/zones/{zone}/clusters/{cluster_idcomplete_ip_rotatio}'.format(project_id='project_id_example', zone='zone_example', cluster_id='cluster_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_container_projects_zones_clusters_create(client):
    """Test case for container_projects_zones_clusters_create

    
    """
    body = {"cluster":{"addonsConfig":{"kubernetesDashboard":{"disabled":True},"configConnectorConfig":{"enabled":True},"statefulHaConfig":{"enabled":True},"gkeBackupAgentConfig":{"enabled":True},"gcePersistentDiskCsiDriverConfig":{"enabled":True},"httpLoadBalancing":{"disabled":True},"cloudRunConfig":{"loadBalancerType":"LOAD_BALANCER_TYPE_UNSPECIFIED","disabled":True},"networkPolicyConfig":{"disabled":True},"horizontalPodAutoscaling":{"disabled":True},"dnsCacheConfig":{"enabled":True},"gcsFuseCsiDriverConfig":{"enabled":True},"gcpFilestoreCsiDriverConfig":{"enabled":True}},"fleet":{"preRegistered":True,"project":"project","membership":"membership"},"parentProductConfig":{"productName":"productName","labels":{"key":"labels"}},"resourceUsageExportConfig":{"consumptionMeteringConfig":{"enabled":True},"bigqueryDestination":{"datasetId":"datasetId"},"enableNetworkEgressMetering":True},"autopilot":{"workloadPolicyConfig":{"allowNetAdmin":True},"enabled":True},"masterAuthorizedNetworksConfig":{"gcpPublicCidrsAccessEnabled":True,"cidrBlocks":[{"displayName":"displayName","cidrBlock":"cidrBlock"},{"displayName":"displayName","cidrBlock":"cidrBlock"}],"enabled":True},"databaseEncryption":{"keyName":"keyName","state":"UNKNOWN"},"currentMasterVersion":"currentMasterVersion","monitoringConfig":{"advancedDatapathObservabilityConfig":{"relayMode":"RELAY_MODE_UNSPECIFIED","enableMetrics":True,"enableRelay":True},"componentConfig":{"enableComponents":["COMPONENT_UNSPECIFIED","COMPONENT_UNSPECIFIED"]},"managedPrometheusConfig":{"enabled":True}},"meshCertificates":{"enableCertificates":True},"zone":"zone","enterpriseConfig":{"clusterTier":"CLUSTER_TIER_UNSPECIFIED"},"securityPostureConfig":{"mode":"MODE_UNSPECIFIED","vulnerabilityMode":"VULNERABILITY_MODE_UNSPECIFIED"},"enableKubernetesAlpha":True,"id":"id","nodePools":[{"updateInfo":{"blueGreenInfo":{"phase":"PHASE_UNSPECIFIED","blueInstanceGroupUrls":["blueInstanceGroupUrls","blueInstanceGroupUrls"],"greenInstanceGroupUrls":["greenInstanceGroupUrls","greenInstanceGroupUrls"],"bluePoolDeletionStartTime":"bluePoolDeletionStartTime","greenPoolVersion":"greenPoolVersion"}},"podIpv4CidrSize":9,"bestEffortProvisioning":{"minProvisionNodes":4,"enabled":True},"maxPodsConstraint":{"maxPodsPerNode":"maxPodsPerNode"},"networkConfig":{"podCidrOverprovisionConfig":{"disable":True},"enablePrivateNodes":True,"additionalNodeNetworkConfigs":[{"subnetwork":"subnetwork","network":"network"},{"subnetwork":"subnetwork","network":"network"}],"podRange":"podRange","podIpv4RangeUtilization":9.965781217890562,"networkPerformanceConfig":{"totalEgressBandwidthTier":"TIER_UNSPECIFIED"},"additionalPodNetworkConfigs":[{"secondaryPodRange":"secondaryPodRange","subnetwork":"subnetwork","maxPodsPerNode":{"maxPodsPerNode":"maxPodsPerNode"}},{"secondaryPodRange":"secondaryPodRange","subnetwork":"subnetwork","maxPodsPerNode":{"maxPodsPerNode":"maxPodsPerNode"}}],"podIpv4CidrBlock":"podIpv4CidrBlock","createPodRange":True},"upgradeSettings":{"maxSurge":5,"maxUnavailable":5,"blueGreenSettings":{"standardRolloutPolicy":{"batchSoakDuration":"batchSoakDuration","batchPercentage":1.4658129,"batchNodeCount":6},"nodePoolSoakDuration":"nodePoolSoakDuration"},"strategy":"NODE_POOL_UPDATE_STRATEGY_UNSPECIFIED"},"queuedProvisioning":{"enabled":True},"version":"version","statusMessage":"statusMessage","selfLink":"selfLink","initialNodeCount":5,"instanceGroupUrls":["instanceGroupUrls","instanceGroupUrls"],"management":{"autoUpgrade":True,"upgradeOptions":{"autoUpgradeStartTime":"autoUpgradeStartTime","description":"description"},"autoRepair":True},"name":"name","placementPolicy":{"policyName":"policyName","tpuTopology":"tpuTopology","type":"TYPE_UNSPECIFIED"},"etag":"etag","locations":["locations","locations"],"autoscaling":{"locationPolicy":"LOCATION_POLICY_UNSPECIFIED","autoprovisioned":True,"minNodeCount":6,"totalMinNodeCount":1,"maxNodeCount":1,"totalMaxNodeCount":7,"enabled":True},"conditions":[{"code":"UNKNOWN","message":"message","canonicalCode":"OK"},{"code":"UNKNOWN","message":"message","canonicalCode":"OK"}],"config":{"metadata":{"key":"metadata"},"gcfsConfig":{"enabled":True},"reservationAffinity":{"consumeReservationType":"UNSPECIFIED","values":["values","values"],"key":"key"},"oauthScopes":["oauthScopes","oauthScopes"],"linuxNodeConfig":{"cgroupMode":"CGROUP_MODE_UNSPECIFIED","sysctls":{"key":"sysctls"}},"minCpuPlatform":"minCpuPlatform","kubeletConfig":{"podPidsLimit":"podPidsLimit","insecureKubeletReadonlyPortEnabled":True,"cpuManagerPolicy":"cpuManagerPolicy","cpuCfsQuotaPeriod":"cpuCfsQuotaPeriod","cpuCfsQuota":True},"windowsNodeConfig":{"osVersion":"OS_VERSION_UNSPECIFIED"},"bootDiskKmsKey":"bootDiskKmsKey","enableConfidentialStorage":True,"diskType":"diskType","gvnic":{"enabled":True},"imageType":"imageType","localSsdCount":1,"machineType":"machineType","advancedMachineFeatures":{"threadsPerCore":"threadsPerCore"},"shieldedInstanceConfig":{"enableIntegrityMonitoring":True,"enableSecureBoot":True},"soleTenantConfig":{"nodeAffinities":[{"values":["values","values"],"key":"key","operator":"OPERATOR_UNSPECIFIED"},{"values":["values","values"],"key":"key","operator":"OPERATOR_UNSPECIFIED"}]},"serviceAccount":"serviceAccount","taints":[{"effect":"EFFECT_UNSPECIFIED","value":"value","key":"key"},{"effect":"EFFECT_UNSPECIFIED","value":"value","key":"key"}],"sandboxConfig":{"type":"UNSPECIFIED"},"nodeGroup":"nodeGroup","confidentialNodes":{"enabled":True},"labels":{"key":"labels"},"tags":["tags","tags"],"workloadMetadataConfig":{"mode":"MODE_UNSPECIFIED"},"resourceManagerTags":{"tags":{"key":"tags"}},"preemptible":True,"fastSocket":{"enabled":True},"loggingConfig":{"variantConfig":{"variant":"VARIANT_UNSPECIFIED"}},"spot":True,"resourceLabels":{"key":"resourceLabels"},"accelerators":[{"acceleratorType":"acceleratorType","gpuSharingConfig":{"gpuSharingStrategy":"GPU_SHARING_STRATEGY_UNSPECIFIED","maxSharedClientsPerGpu":"maxSharedClientsPerGpu"},"acceleratorCount":"acceleratorCount","gpuDriverInstallationConfig":{"gpuDriverVersion":"GPU_DRIVER_VERSION_UNSPECIFIED"},"gpuPartitionSize":"gpuPartitionSize"},{"acceleratorType":"acceleratorType","gpuSharingConfig":{"gpuSharingStrategy":"GPU_SHARING_STRATEGY_UNSPECIFIED","maxSharedClientsPerGpu":"maxSharedClientsPerGpu"},"acceleratorCount":"acceleratorCount","gpuDriverInstallationConfig":{"gpuDriverVersion":"GPU_DRIVER_VERSION_UNSPECIFIED"},"gpuPartitionSize":"gpuPartitionSize"}],"ephemeralStorageLocalSsdConfig":{"localSsdCount":4},"localNvmeSsdBlockConfig":{"localSsdCount":7},"secondaryBootDisks":[{"mode":"MODE_UNSPECIFIED","diskImage":"diskImage"},{"mode":"MODE_UNSPECIFIED","diskImage":"diskImage"}],"diskSizeGb":2},"status":"STATUS_UNSPECIFIED"},{"updateInfo":{"blueGreenInfo":{"phase":"PHASE_UNSPECIFIED","blueInstanceGroupUrls":["blueInstanceGroupUrls","blueInstanceGroupUrls"],"greenInstanceGroupUrls":["greenInstanceGroupUrls","greenInstanceGroupUrls"],"bluePoolDeletionStartTime":"bluePoolDeletionStartTime","greenPoolVersion":"greenPoolVersion"}},"podIpv4CidrSize":9,"bestEffortProvisioning":{"minProvisionNodes":4,"enabled":True},"maxPodsConstraint":{"maxPodsPerNode":"maxPodsPerNode"},"networkConfig":{"podCidrOverprovisionConfig":{"disable":True},"enablePrivateNodes":True,"additionalNodeNetworkConfigs":[{"subnetwork":"subnetwork","network":"network"},{"subnetwork":"subnetwork","network":"network"}],"podRange":"podRange","podIpv4RangeUtilization":9.965781217890562,"networkPerformanceConfig":{"totalEgressBandwidthTier":"TIER_UNSPECIFIED"},"additionalPodNetworkConfigs":[{"secondaryPodRange":"secondaryPodRange","subnetwork":"subnetwork","maxPodsPerNode":{"maxPodsPerNode":"maxPodsPerNode"}},{"secondaryPodRange":"secondaryPodRange","subnetwork":"subnetwork","maxPodsPerNode":{"maxPodsPerNode":"maxPodsPerNode"}}],"podIpv4CidrBlock":"podIpv4CidrBlock","createPodRange":True},"upgradeSettings":{"maxSurge":5,"maxUnavailable":5,"blueGreenSettings":{"standardRolloutPolicy":{"batchSoakDuration":"batchSoakDuration","batchPercentage":1.4658129,"batchNodeCount":6},"nodePoolSoakDuration":"nodePoolSoakDuration"},"strategy":"NODE_POOL_UPDATE_STRATEGY_UNSPECIFIED"},"queuedProvisioning":{"enabled":True},"version":"version","statusMessage":"statusMessage","selfLink":"selfLink","initialNodeCount":5,"instanceGroupUrls":["instanceGroupUrls","instanceGroupUrls"],"management":{"autoUpgrade":True,"upgradeOptions":{"autoUpgradeStartTime":"autoUpgradeStartTime","description":"description"},"autoRepair":True},"name":"name","placementPolicy":{"policyName":"policyName","tpuTopology":"tpuTopology","type":"TYPE_UNSPECIFIED"},"etag":"etag","locations":["locations","locations"],"autoscaling":{"locationPolicy":"LOCATION_POLICY_UNSPECIFIED","autoprovisioned":True,"minNodeCount":6,"totalMinNodeCount":1,"maxNodeCount":1,"totalMaxNodeCount":7,"enabled":True},"conditions":[{"code":"UNKNOWN","message":"message","canonicalCode":"OK"},{"code":"UNKNOWN","message":"message","canonicalCode":"OK"}],"config":{"metadata":{"key":"metadata"},"gcfsConfig":{"enabled":True},"reservationAffinity":{"consumeReservationType":"UNSPECIFIED","values":["values","values"],"key":"key"},"oauthScopes":["oauthScopes","oauthScopes"],"linuxNodeConfig":{"cgroupMode":"CGROUP_MODE_UNSPECIFIED","sysctls":{"key":"sysctls"}},"minCpuPlatform":"minCpuPlatform","kubeletConfig":{"podPidsLimit":"podPidsLimit","insecureKubeletReadonlyPortEnabled":True,"cpuManagerPolicy":"cpuManagerPolicy","cpuCfsQuotaPeriod":"cpuCfsQuotaPeriod","cpuCfsQuota":True},"windowsNodeConfig":{"osVersion":"OS_VERSION_UNSPECIFIED"},"bootDiskKmsKey":"bootDiskKmsKey","enableConfidentialStorage":True,"diskType":"diskType","gvnic":{"enabled":True},"imageType":"imageType","localSsdCount":1,"machineType":"machineType","advancedMachineFeatures":{"threadsPerCore":"threadsPerCore"},"shieldedInstanceConfig":{"enableIntegrityMonitoring":True,"enableSecureBoot":True},"soleTenantConfig":{"nodeAffinities":[{"values":["values","values"],"key":"key","operator":"OPERATOR_UNSPECIFIED"},{"values":["values","values"],"key":"key","operator":"OPERATOR_UNSPECIFIED"}]},"serviceAccount":"serviceAccount","taints":[{"effect":"EFFECT_UNSPECIFIED","value":"value","key":"key"},{"effect":"EFFECT_UNSPECIFIED","value":"value","key":"key"}],"sandboxConfig":{"type":"UNSPECIFIED"},"nodeGroup":"nodeGroup","confidentialNodes":{"enabled":True},"labels":{"key":"labels"},"tags":["tags","tags"],"workloadMetadataConfig":{"mode":"MODE_UNSPECIFIED"},"resourceManagerTags":{"tags":{"key":"tags"}},"preemptible":True,"fastSocket":{"enabled":True},"loggingConfig":{"variantConfig":{"variant":"VARIANT_UNSPECIFIED"}},"spot":True,"resourceLabels":{"key":"resourceLabels"},"accelerators":[{"acceleratorType":"acceleratorType","gpuSharingConfig":{"gpuSharingStrategy":"GPU_SHARING_STRATEGY_UNSPECIFIED","maxSharedClientsPerGpu":"maxSharedClientsPerGpu"},"acceleratorCount":"acceleratorCount","gpuDriverInstallationConfig":{"gpuDriverVersion":"GPU_DRIVER_VERSION_UNSPECIFIED"},"gpuPartitionSize":"gpuPartitionSize"},{"acceleratorType":"acceleratorType","gpuSharingConfig":{"gpuSharingStrategy":"GPU_SHARING_STRATEGY_UNSPECIFIED","maxSharedClientsPerGpu":"maxSharedClientsPerGpu"},"acceleratorCount":"acceleratorCount","gpuDriverInstallationConfig":{"gpuDriverVersion":"GPU_DRIVER_VERSION_UNSPECIFIED"},"gpuPartitionSize":"gpuPartitionSize"}],"ephemeralStorageLocalSsdConfig":{"localSsdCount":4},"localNvmeSsdBlockConfig":{"localSsdCount":7},"secondaryBootDisks":[{"mode":"MODE_UNSPECIFIED","diskImage":"diskImage"},{"mode":"MODE_UNSPECIFIED","diskImage":"diskImage"}],"diskSizeGb":2},"status":"STATUS_UNSPECIFIED"}],"binaryAuthorization":{"evaluationMode":"EVALUATION_MODE_UNSPECIFIED","enabled":True},"enableK8sBetaApis":{"enabledApis":["enabledApis","enabledApis"]},"networkPolicy":{"provider":"PROVIDER_UNSPECIFIED","enabled":True},"currentNodeCount":2,"loggingService":"loggingService","enableTpu":True,"maintenancePolicy":{"resourceVersion":"resourceVersion","window":{"dailyMaintenanceWindow":{"duration":"duration","startTime":"startTime"},"maintenanceExclusions":{"key":{"maintenanceExclusionOptions":{"scope":"NO_UPGRADES"},"startTime":"startTime","endTime":"endTime"}},"recurringWindow":{"recurrence":"recurrence","window":{"maintenanceExclusionOptions":{"scope":"NO_UPGRADES"},"startTime":"startTime","endTime":"endTime"}}}},"instanceGroupUrls":["instanceGroupUrls","instanceGroupUrls"],"releaseChannel":{"channel":"UNSPECIFIED"},"expireTime":"expireTime","nodeIpv4CidrSize":1,"subnetwork":"subnetwork","name":"name","resourceLabels":{"key":"resourceLabels"},"authenticatorGroupsConfig":{"securityGroup":"securityGroup","enabled":True},"etag":"etag","autoscaling":{"autoprovisioningLocations":["autoprovisioningLocations","autoprovisioningLocations"],"autoscalingProfile":"PROFILE_UNSPECIFIED","resourceLimits":[{"maximum":"maximum","minimum":"minimum","resourceType":"resourceType"},{"maximum":"maximum","minimum":"minimum","resourceType":"resourceType"}],"autoprovisioningNodePoolDefaults":{"shieldedInstanceConfig":{"enableIntegrityMonitoring":True,"enableSecureBoot":True},"management":{"autoUpgrade":True,"upgradeOptions":{"autoUpgradeStartTime":"autoUpgradeStartTime","description":"description"},"autoRepair":True},"minCpuPlatform":"minCpuPlatform","insecureKubeletReadonlyPortEnabled":True,"bootDiskKmsKey":"bootDiskKmsKey","upgradeSettings":{"maxSurge":5,"maxUnavailable":5,"blueGreenSettings":{"standardRolloutPolicy":{"batchSoakDuration":"batchSoakDuration","batchPercentage":1.4658129,"batchNodeCount":6},"nodePoolSoakDuration":"nodePoolSoakDuration"},"strategy":"NODE_POOL_UPDATE_STRATEGY_UNSPECIFIED"},"serviceAccount":"serviceAccount","diskType":"diskType","oauthScopes":["oauthScopes","oauthScopes"],"imageType":"imageType","diskSizeGb":0},"enableNodeAutoprovisioning":True},"conditions":[{"code":"UNKNOWN","message":"message","canonicalCode":"OK"},{"code":"UNKNOWN","message":"message","canonicalCode":"OK"}],"status":"STATUS_UNSPECIFIED","nodePoolAutoConfig":{"resourceManagerTags":{"tags":{"key":"tags"}},"networkTags":{"tags":["tags","tags"]}},"defaultMaxPodsConstraint":{"maxPodsPerNode":"maxPodsPerNode"},"masterAuth":{"clientCertificateConfig":{"issueClientCertificate":True},"clientCertificate":"clientCertificate","password":"password","clientKey":"clientKey","clusterCaCertificate":"clusterCaCertificate","username":"username"},"verticalPodAutoscaling":{"enabled":True},"description":"description","costManagementConfig":{"enabled":True},"labelFingerprint":"labelFingerprint","ipAllocationPolicy":{"clusterIpv4CidrBlock":"clusterIpv4CidrBlock","createSubnetwork":True,"clusterIpv4Cidr":"clusterIpv4Cidr","servicesIpv4CidrBlock":"servicesIpv4CidrBlock","servicesSecondaryRangeName":"servicesSecondaryRangeName","nodeIpv4Cidr":"nodeIpv4Cidr","ipv6AccessType":"IPV6_ACCESS_TYPE_UNSPECIFIED","subnetworkName":"subnetworkName","podCidrOverprovisionConfig":{"disable":True},"useRoutes":True,"useIpAliases":True,"tpuIpv4CidrBlock":"tpuIpv4CidrBlock","additionalPodRangesConfig":{"podRangeInfo":[{"rangeName":"rangeName","utilization":9.301444243932576},{"rangeName":"rangeName","utilization":9.301444243932576}],"podRangeNames":["podRangeNames","podRangeNames"]},"servicesIpv6CidrBlock":"servicesIpv6CidrBlock","servicesIpv4Cidr":"servicesIpv4Cidr","clusterSecondaryRangeName":"clusterSecondaryRangeName","defaultPodIpv4RangeUtilization":3.616076749251911,"nodeIpv4CidrBlock":"nodeIpv4CidrBlock","stackType":"STACK_TYPE_UNSPECIFIED","subnetIpv6CidrBlock":"subnetIpv6CidrBlock"},"nodeConfig":{"metadata":{"key":"metadata"},"gcfsConfig":{"enabled":True},"reservationAffinity":{"consumeReservationType":"UNSPECIFIED","values":["values","values"],"key":"key"},"oauthScopes":["oauthScopes","oauthScopes"],"linuxNodeConfig":{"cgroupMode":"CGROUP_MODE_UNSPECIFIED","sysctls":{"key":"sysctls"}},"minCpuPlatform":"minCpuPlatform","kubeletConfig":{"podPidsLimit":"podPidsLimit","insecureKubeletReadonlyPortEnabled":True,"cpuManagerPolicy":"cpuManagerPolicy","cpuCfsQuotaPeriod":"cpuCfsQuotaPeriod","cpuCfsQuota":True},"windowsNodeConfig":{"osVersion":"OS_VERSION_UNSPECIFIED"},"bootDiskKmsKey":"bootDiskKmsKey","enableConfidentialStorage":True,"diskType":"diskType","gvnic":{"enabled":True},"imageType":"imageType","localSsdCount":1,"machineType":"machineType","advancedMachineFeatures":{"threadsPerCore":"threadsPerCore"},"shieldedInstanceConfig":{"enableIntegrityMonitoring":True,"enableSecureBoot":True},"soleTenantConfig":{"nodeAffinities":[{"values":["values","values"],"key":"key","operator":"OPERATOR_UNSPECIFIED"},{"values":["values","values"],"key":"key","operator":"OPERATOR_UNSPECIFIED"}]},"serviceAccount":"serviceAccount","taints":[{"effect":"EFFECT_UNSPECIFIED","value":"value","key":"key"},{"effect":"EFFECT_UNSPECIFIED","value":"value","key":"key"}],"sandboxConfig":{"type":"UNSPECIFIED"},"nodeGroup":"nodeGroup","confidentialNodes":{"enabled":True},"labels":{"key":"labels"},"tags":["tags","tags"],"workloadMetadataConfig":{"mode":"MODE_UNSPECIFIED"},"resourceManagerTags":{"tags":{"key":"tags"}},"preemptible":True,"fastSocket":{"enabled":True},"loggingConfig":{"variantConfig":{"variant":"VARIANT_UNSPECIFIED"}},"spot":True,"resourceLabels":{"key":"resourceLabels"},"accelerators":[{"acceleratorType":"acceleratorType","gpuSharingConfig":{"gpuSharingStrategy":"GPU_SHARING_STRATEGY_UNSPECIFIED","maxSharedClientsPerGpu":"maxSharedClientsPerGpu"},"acceleratorCount":"acceleratorCount","gpuDriverInstallationConfig":{"gpuDriverVersion":"GPU_DRIVER_VERSION_UNSPECIFIED"},"gpuPartitionSize":"gpuPartitionSize"},{"acceleratorType":"acceleratorType","gpuSharingConfig":{"gpuSharingStrategy":"GPU_SHARING_STRATEGY_UNSPECIFIED","maxSharedClientsPerGpu":"maxSharedClientsPerGpu"},"acceleratorCount":"acceleratorCount","gpuDriverInstallationConfig":{"gpuDriverVersion":"GPU_DRIVER_VERSION_UNSPECIFIED"},"gpuPartitionSize":"gpuPartitionSize"}],"ephemeralStorageLocalSsdConfig":{"localSsdCount":4},"localNvmeSsdBlockConfig":{"localSsdCount":7},"secondaryBootDisks":[{"mode":"MODE_UNSPECIFIED","diskImage":"diskImage"},{"mode":"MODE_UNSPECIFIED","diskImage":"diskImage"}],"diskSizeGb":2},"network":"network","endpoint":"endpoint","initialNodeCount":7,"shieldedNodes":{"enabled":True},"initialClusterVersion":"initialClusterVersion","privateClusterConfig":{"enablePrivateEndpoint":True,"publicEndpoint":"publicEndpoint","masterGlobalAccessConfig":{"enabled":True},"enablePrivateNodes":True,"privateEndpointSubnetwork":"privateEndpointSubnetwork","peeringName":"peeringName","privateEndpoint":"privateEndpoint","masterIpv4CidrBlock":"masterIpv4CidrBlock"},"legacyAbac":{"enabled":True},"clusterIpv4Cidr":"clusterIpv4Cidr","monitoringService":"monitoringService","workloadIdentityConfig":{"workloadPool":"workloadPool"},"networkConfig":{"defaultSnatStatus":{"disabled":True},"dnsConfig":{"clusterDnsDomain":"clusterDnsDomain","clusterDnsScope":"DNS_SCOPE_UNSPECIFIED","clusterDns":"PROVIDER_UNSPECIFIED"},"enableMultiNetworking":True,"serviceExternalIpsConfig":{"enabled":True},"network":"network","privateIpv6GoogleAccess":"PRIVATE_IPV6_GOOGLE_ACCESS_UNSPECIFIED","enableL4ilbSubsetting":True,"datapathProvider":"DATAPATH_PROVIDER_UNSPECIFIED","gatewayApiConfig":{"channel":"CHANNEL_UNSPECIFIED"},"enableFqdnNetworkPolicy":True,"subnetwork":"subnetwork","enableIntraNodeVisibility":True,"networkPerformanceConfig":{"totalEgressBandwidthTier":"TIER_UNSPECIFIED"},"inTransitEncryptionConfig":"IN_TRANSIT_ENCRYPTION_CONFIG_UNSPECIFIED"},"statusMessage":"statusMessage","confidentialNodes":{"enabled":True},"selfLink":"selfLink","identityServiceConfig":{"enabled":True},"currentNodeVersion":"currentNodeVersion","tpuIpv4CidrBlock":"tpuIpv4CidrBlock","createTime":"createTime","loggingConfig":{"componentConfig":{"enableComponents":["COMPONENT_UNSPECIFIED","COMPONENT_UNSPECIFIED"]}},"servicesIpv4Cidr":"servicesIpv4Cidr","location":"location","locations":["locations","locations"],"nodePoolDefaults":{"nodeConfigDefaults":{"gcfsConfig":{"enabled":True},"loggingConfig":{"variantConfig":{"variant":"VARIANT_UNSPECIFIED"}}}},"notificationConfig":{"pubsub":{"filter":{"eventType":["EVENT_TYPE_UNSPECIFIED","EVENT_TYPE_UNSPECIFIED"]},"topic":"topic","enabled":True}}},"parent":"parent","zone":"zone","projectId":"projectId"}
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/projects/{project_id}/zones/{zone}/clusters'.format(project_id='project_id_example', zone='zone_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_container_projects_zones_clusters_delete(client):
    """Test case for container_projects_zones_clusters_delete

    
    """
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example'),
                    ('name', 'name_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/v1/projects/{project_id}/zones/{zone}/clusters/{cluster_id}'.format(project_id='project_id_example', zone='zone_example', cluster_id='cluster_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_container_projects_zones_clusters_get(client):
    """Test case for container_projects_zones_clusters_get

    
    """
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example'),
                    ('name', 'name_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/projects/{project_id}/zones/{zone}/clusters/{cluster_id}'.format(project_id='project_id_example', zone='zone_example', cluster_id='cluster_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_container_projects_zones_clusters_legacy_abac(client):
    """Test case for container_projects_zones_clusters_legacy_abac

    
    """
    body = {"zone":"zone","name":"name","clusterId":"clusterId","projectId":"projectId","enabled":True}
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/projects/{project_id}/zones/{zone}/clusters/{cluster_id}/legacyAbac'.format(project_id='project_id_example', zone='zone_example', cluster_id='cluster_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_container_projects_zones_clusters_list(client):
    """Test case for container_projects_zones_clusters_list

    
    """
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example'),
                    ('parent', 'parent_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/projects/{project_id}/zones/{zone}/clusters'.format(project_id='project_id_example', zone='zone_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_container_projects_zones_clusters_locations(client):
    """Test case for container_projects_zones_clusters_locations

    
    """
    body = {"zone":"zone","name":"name","locations":["locations","locations"],"clusterId":"clusterId","projectId":"projectId"}
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/projects/{project_id}/zones/{zone}/clusters/{cluster_id}/locations'.format(project_id='project_id_example', zone='zone_example', cluster_id='cluster_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_container_projects_zones_clusters_logging(client):
    """Test case for container_projects_zones_clusters_logging

    
    """
    body = {"zone":"zone","name":"name","clusterId":"clusterId","loggingService":"loggingService","projectId":"projectId"}
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/projects/{project_id}/zones/{zone}/clusters/{cluster_id}/logging'.format(project_id='project_id_example', zone='zone_example', cluster_id='cluster_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_container_projects_zones_clusters_master(client):
    """Test case for container_projects_zones_clusters_master

    
    """
    body = {"zone":"zone","masterVersion":"masterVersion","name":"name","clusterId":"clusterId","projectId":"projectId"}
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/projects/{project_id}/zones/{zone}/clusters/{cluster_id}/master'.format(project_id='project_id_example', zone='zone_example', cluster_id='cluster_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_container_projects_zones_clusters_monitoring(client):
    """Test case for container_projects_zones_clusters_monitoring

    
    """
    body = {"zone":"zone","monitoringService":"monitoringService","name":"name","clusterId":"clusterId","projectId":"projectId"}
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/projects/{project_id}/zones/{zone}/clusters/{cluster_id}/monitoring'.format(project_id='project_id_example', zone='zone_example', cluster_id='cluster_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_container_projects_zones_clusters_node_pools_autoscaling(client):
    """Test case for container_projects_zones_clusters_node_pools_autoscaling

    
    """
    body = {"nodePoolId":"nodePoolId","zone":"zone","name":"name","autoscaling":{"locationPolicy":"LOCATION_POLICY_UNSPECIFIED","autoprovisioned":True,"minNodeCount":6,"totalMinNodeCount":1,"maxNodeCount":1,"totalMaxNodeCount":7,"enabled":True},"clusterId":"clusterId","projectId":"projectId"}
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/projects/{project_id}/zones/{zone}/clusters/{cluster_id}/nodePools/{node_pool_id}/autoscaling'.format(project_id='project_id_example', zone='zone_example', cluster_id='cluster_id_example', node_pool_id='node_pool_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_container_projects_zones_clusters_node_pools_create(client):
    """Test case for container_projects_zones_clusters_node_pools_create

    
    """
    body = {"nodePool":{"updateInfo":{"blueGreenInfo":{"phase":"PHASE_UNSPECIFIED","blueInstanceGroupUrls":["blueInstanceGroupUrls","blueInstanceGroupUrls"],"greenInstanceGroupUrls":["greenInstanceGroupUrls","greenInstanceGroupUrls"],"bluePoolDeletionStartTime":"bluePoolDeletionStartTime","greenPoolVersion":"greenPoolVersion"}},"podIpv4CidrSize":9,"bestEffortProvisioning":{"minProvisionNodes":4,"enabled":True},"maxPodsConstraint":{"maxPodsPerNode":"maxPodsPerNode"},"networkConfig":{"podCidrOverprovisionConfig":{"disable":True},"enablePrivateNodes":True,"additionalNodeNetworkConfigs":[{"subnetwork":"subnetwork","network":"network"},{"subnetwork":"subnetwork","network":"network"}],"podRange":"podRange","podIpv4RangeUtilization":9.965781217890562,"networkPerformanceConfig":{"totalEgressBandwidthTier":"TIER_UNSPECIFIED"},"additionalPodNetworkConfigs":[{"secondaryPodRange":"secondaryPodRange","subnetwork":"subnetwork","maxPodsPerNode":{"maxPodsPerNode":"maxPodsPerNode"}},{"secondaryPodRange":"secondaryPodRange","subnetwork":"subnetwork","maxPodsPerNode":{"maxPodsPerNode":"maxPodsPerNode"}}],"podIpv4CidrBlock":"podIpv4CidrBlock","createPodRange":True},"upgradeSettings":{"maxSurge":5,"maxUnavailable":5,"blueGreenSettings":{"standardRolloutPolicy":{"batchSoakDuration":"batchSoakDuration","batchPercentage":1.4658129,"batchNodeCount":6},"nodePoolSoakDuration":"nodePoolSoakDuration"},"strategy":"NODE_POOL_UPDATE_STRATEGY_UNSPECIFIED"},"queuedProvisioning":{"enabled":True},"version":"version","statusMessage":"statusMessage","selfLink":"selfLink","initialNodeCount":5,"instanceGroupUrls":["instanceGroupUrls","instanceGroupUrls"],"management":{"autoUpgrade":True,"upgradeOptions":{"autoUpgradeStartTime":"autoUpgradeStartTime","description":"description"},"autoRepair":True},"name":"name","placementPolicy":{"policyName":"policyName","tpuTopology":"tpuTopology","type":"TYPE_UNSPECIFIED"},"etag":"etag","locations":["locations","locations"],"autoscaling":{"locationPolicy":"LOCATION_POLICY_UNSPECIFIED","autoprovisioned":True,"minNodeCount":6,"totalMinNodeCount":1,"maxNodeCount":1,"totalMaxNodeCount":7,"enabled":True},"conditions":[{"code":"UNKNOWN","message":"message","canonicalCode":"OK"},{"code":"UNKNOWN","message":"message","canonicalCode":"OK"}],"config":{"metadata":{"key":"metadata"},"gcfsConfig":{"enabled":True},"reservationAffinity":{"consumeReservationType":"UNSPECIFIED","values":["values","values"],"key":"key"},"oauthScopes":["oauthScopes","oauthScopes"],"linuxNodeConfig":{"cgroupMode":"CGROUP_MODE_UNSPECIFIED","sysctls":{"key":"sysctls"}},"minCpuPlatform":"minCpuPlatform","kubeletConfig":{"podPidsLimit":"podPidsLimit","insecureKubeletReadonlyPortEnabled":True,"cpuManagerPolicy":"cpuManagerPolicy","cpuCfsQuotaPeriod":"cpuCfsQuotaPeriod","cpuCfsQuota":True},"windowsNodeConfig":{"osVersion":"OS_VERSION_UNSPECIFIED"},"bootDiskKmsKey":"bootDiskKmsKey","enableConfidentialStorage":True,"diskType":"diskType","gvnic":{"enabled":True},"imageType":"imageType","localSsdCount":1,"machineType":"machineType","advancedMachineFeatures":{"threadsPerCore":"threadsPerCore"},"shieldedInstanceConfig":{"enableIntegrityMonitoring":True,"enableSecureBoot":True},"soleTenantConfig":{"nodeAffinities":[{"values":["values","values"],"key":"key","operator":"OPERATOR_UNSPECIFIED"},{"values":["values","values"],"key":"key","operator":"OPERATOR_UNSPECIFIED"}]},"serviceAccount":"serviceAccount","taints":[{"effect":"EFFECT_UNSPECIFIED","value":"value","key":"key"},{"effect":"EFFECT_UNSPECIFIED","value":"value","key":"key"}],"sandboxConfig":{"type":"UNSPECIFIED"},"nodeGroup":"nodeGroup","confidentialNodes":{"enabled":True},"labels":{"key":"labels"},"tags":["tags","tags"],"workloadMetadataConfig":{"mode":"MODE_UNSPECIFIED"},"resourceManagerTags":{"tags":{"key":"tags"}},"preemptible":True,"fastSocket":{"enabled":True},"loggingConfig":{"variantConfig":{"variant":"VARIANT_UNSPECIFIED"}},"spot":True,"resourceLabels":{"key":"resourceLabels"},"accelerators":[{"acceleratorType":"acceleratorType","gpuSharingConfig":{"gpuSharingStrategy":"GPU_SHARING_STRATEGY_UNSPECIFIED","maxSharedClientsPerGpu":"maxSharedClientsPerGpu"},"acceleratorCount":"acceleratorCount","gpuDriverInstallationConfig":{"gpuDriverVersion":"GPU_DRIVER_VERSION_UNSPECIFIED"},"gpuPartitionSize":"gpuPartitionSize"},{"acceleratorType":"acceleratorType","gpuSharingConfig":{"gpuSharingStrategy":"GPU_SHARING_STRATEGY_UNSPECIFIED","maxSharedClientsPerGpu":"maxSharedClientsPerGpu"},"acceleratorCount":"acceleratorCount","gpuDriverInstallationConfig":{"gpuDriverVersion":"GPU_DRIVER_VERSION_UNSPECIFIED"},"gpuPartitionSize":"gpuPartitionSize"}],"ephemeralStorageLocalSsdConfig":{"localSsdCount":4},"localNvmeSsdBlockConfig":{"localSsdCount":7},"secondaryBootDisks":[{"mode":"MODE_UNSPECIFIED","diskImage":"diskImage"},{"mode":"MODE_UNSPECIFIED","diskImage":"diskImage"}],"diskSizeGb":2},"status":"STATUS_UNSPECIFIED"},"parent":"parent","zone":"zone","clusterId":"clusterId","projectId":"projectId"}
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/projects/{project_id}/zones/{zone}/clusters/{cluster_id}/nodePools'.format(project_id='project_id_example', zone='zone_example', cluster_id='cluster_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_container_projects_zones_clusters_node_pools_delete(client):
    """Test case for container_projects_zones_clusters_node_pools_delete

    
    """
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example'),
                    ('name', 'name_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/v1/projects/{project_id}/zones/{zone}/clusters/{cluster_id}/nodePools/{node_pool_id}'.format(project_id='project_id_example', zone='zone_example', cluster_id='cluster_id_example', node_pool_id='node_pool_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_container_projects_zones_clusters_node_pools_get(client):
    """Test case for container_projects_zones_clusters_node_pools_get

    
    """
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example'),
                    ('name', 'name_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/projects/{project_id}/zones/{zone}/clusters/{cluster_id}/nodePools/{node_pool_id}'.format(project_id='project_id_example', zone='zone_example', cluster_id='cluster_id_example', node_pool_id='node_pool_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_container_projects_zones_clusters_node_pools_list(client):
    """Test case for container_projects_zones_clusters_node_pools_list

    
    """
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example'),
                    ('parent', 'parent_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/projects/{project_id}/zones/{zone}/clusters/{cluster_id}/nodePools'.format(project_id='project_id_example', zone='zone_example', cluster_id='cluster_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_container_projects_zones_clusters_node_pools_rollback(client):
    """Test case for container_projects_zones_clusters_node_pools_rollback

    
    """
    body = {"nodePoolId":"nodePoolId","zone":"zone","name":"name","clusterId":"clusterId","projectId":"projectId","respectPdb":True}
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/projects/{project_id}/zones/{zone}/clusters/{cluster_id}/nodePools/{node_pool_idrollbac}'.format(project_id='project_id_example', zone='zone_example', cluster_id='cluster_id_example', node_pool_id='node_pool_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_container_projects_zones_clusters_node_pools_set_management(client):
    """Test case for container_projects_zones_clusters_node_pools_set_management

    
    """
    body = {"nodePoolId":"nodePoolId","management":{"autoUpgrade":True,"upgradeOptions":{"autoUpgradeStartTime":"autoUpgradeStartTime","description":"description"},"autoRepair":True},"zone":"zone","name":"name","clusterId":"clusterId","projectId":"projectId"}
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/projects/{project_id}/zones/{zone}/clusters/{cluster_id}/nodePools/{node_pool_id}/setManagement'.format(project_id='project_id_example', zone='zone_example', cluster_id='cluster_id_example', node_pool_id='node_pool_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_container_projects_zones_clusters_node_pools_set_size(client):
    """Test case for container_projects_zones_clusters_node_pools_set_size

    
    """
    body = {"nodePoolId":"nodePoolId","zone":"zone","name":"name","nodeCount":0,"clusterId":"clusterId","projectId":"projectId"}
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/projects/{project_id}/zones/{zone}/clusters/{cluster_id}/nodePools/{node_pool_id}/setSize'.format(project_id='project_id_example', zone='zone_example', cluster_id='cluster_id_example', node_pool_id='node_pool_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_container_projects_zones_clusters_node_pools_update(client):
    """Test case for container_projects_zones_clusters_node_pools_update

    
    """
    body = {"gcfsConfig":{"enabled":True},"upgradeSettings":{"maxSurge":5,"maxUnavailable":5,"blueGreenSettings":{"standardRolloutPolicy":{"batchSoakDuration":"batchSoakDuration","batchPercentage":1.4658129,"batchNodeCount":6},"nodePoolSoakDuration":"nodePoolSoakDuration"},"strategy":"NODE_POOL_UPDATE_STRATEGY_UNSPECIFIED"},"clusterId":"clusterId","linuxNodeConfig":{"cgroupMode":"CGROUP_MODE_UNSPECIFIED","sysctls":{"key":"sysctls"}},"queuedProvisioning":{"enabled":True},"zone":"zone","kubeletConfig":{"podPidsLimit":"podPidsLimit","insecureKubeletReadonlyPortEnabled":True,"cpuManagerPolicy":"cpuManagerPolicy","cpuCfsQuotaPeriod":"cpuCfsQuotaPeriod","cpuCfsQuota":True},"windowsNodeConfig":{"osVersion":"OS_VERSION_UNSPECIFIED"},"diskType":"diskType","gvnic":{"enabled":True},"imageType":"imageType","machineType":"machineType","nodePoolId":"nodePoolId","nodeNetworkConfig":{"podCidrOverprovisionConfig":{"disable":True},"enablePrivateNodes":True,"additionalNodeNetworkConfigs":[{"subnetwork":"subnetwork","network":"network"},{"subnetwork":"subnetwork","network":"network"}],"podRange":"podRange","podIpv4RangeUtilization":9.965781217890562,"networkPerformanceConfig":{"totalEgressBandwidthTier":"TIER_UNSPECIFIED"},"additionalPodNetworkConfigs":[{"secondaryPodRange":"secondaryPodRange","subnetwork":"subnetwork","maxPodsPerNode":{"maxPodsPerNode":"maxPodsPerNode"}},{"secondaryPodRange":"secondaryPodRange","subnetwork":"subnetwork","maxPodsPerNode":{"maxPodsPerNode":"maxPodsPerNode"}}],"podIpv4CidrBlock":"podIpv4CidrBlock","createPodRange":True},"nodeVersion":"nodeVersion","taints":{"taints":[{"effect":"EFFECT_UNSPECIFIED","value":"value","key":"key"},{"effect":"EFFECT_UNSPECIFIED","value":"value","key":"key"}]},"confidentialNodes":{"enabled":True},"labels":{"labels":{"key":"labels"}},"tags":{"tags":["tags","tags"]},"workloadMetadataConfig":{"mode":"MODE_UNSPECIFIED"},"resourceManagerTags":{"tags":{"key":"tags"}},"fastSocket":{"enabled":True},"loggingConfig":{"variantConfig":{"variant":"VARIANT_UNSPECIFIED"}},"name":"name","resourceLabels":{"labels":{"key":"labels"}},"etag":"etag","locations":["locations","locations"],"projectId":"projectId","diskSizeGb":"diskSizeGb"}
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/projects/{project_id}/zones/{zone}/clusters/{cluster_id}/nodePools/{node_pool_id}/update'.format(project_id='project_id_example', zone='zone_example', cluster_id='cluster_id_example', node_pool_id='node_pool_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_container_projects_zones_clusters_resource_labels(client):
    """Test case for container_projects_zones_clusters_resource_labels

    
    """
    body = {"zone":"zone","name":"name","resourceLabels":{"key":"resourceLabels"},"clusterId":"clusterId","labelFingerprint":"labelFingerprint","projectId":"projectId"}
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/projects/{project_id}/zones/{zone}/clusters/{cluster_id}/resourceLabels'.format(project_id='project_id_example', zone='zone_example', cluster_id='cluster_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_container_projects_zones_clusters_set_maintenance_policy(client):
    """Test case for container_projects_zones_clusters_set_maintenance_policy

    
    """
    body = {"maintenancePolicy":{"resourceVersion":"resourceVersion","window":{"dailyMaintenanceWindow":{"duration":"duration","startTime":"startTime"},"maintenanceExclusions":{"key":{"maintenanceExclusionOptions":{"scope":"NO_UPGRADES"},"startTime":"startTime","endTime":"endTime"}},"recurringWindow":{"recurrence":"recurrence","window":{"maintenanceExclusionOptions":{"scope":"NO_UPGRADES"},"startTime":"startTime","endTime":"endTime"}}}},"zone":"zone","name":"name","clusterId":"clusterId","projectId":"projectId"}
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/projects/{project_id}/zones/{zone}/clusters/{cluster_idset_maintenance_polic}'.format(project_id='project_id_example', zone='zone_example', cluster_id='cluster_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_container_projects_zones_clusters_set_master_auth(client):
    """Test case for container_projects_zones_clusters_set_master_auth

    
    """
    body = {"zone":"zone","name":"name","action":"UNKNOWN","update":{"clientCertificateConfig":{"issueClientCertificate":True},"clientCertificate":"clientCertificate","password":"password","clientKey":"clientKey","clusterCaCertificate":"clusterCaCertificate","username":"username"},"clusterId":"clusterId","projectId":"projectId"}
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/projects/{project_id}/zones/{zone}/clusters/{cluster_idset_master_aut}'.format(project_id='project_id_example', zone='zone_example', cluster_id='cluster_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_container_projects_zones_clusters_set_network_policy(client):
    """Test case for container_projects_zones_clusters_set_network_policy

    
    """
    body = {"zone":"zone","networkPolicy":{"provider":"PROVIDER_UNSPECIFIED","enabled":True},"name":"name","clusterId":"clusterId","projectId":"projectId"}
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/projects/{project_id}/zones/{zone}/clusters/{cluster_idset_network_polic}'.format(project_id='project_id_example', zone='zone_example', cluster_id='cluster_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_container_projects_zones_clusters_start_ip_rotation(client):
    """Test case for container_projects_zones_clusters_start_ip_rotation

    
    """
    body = {"rotateCredentials":True,"zone":"zone","name":"name","clusterId":"clusterId","projectId":"projectId"}
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/projects/{project_id}/zones/{zone}/clusters/{cluster_idstart_ip_rotatio}'.format(project_id='project_id_example', zone='zone_example', cluster_id='cluster_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_container_projects_zones_clusters_update(client):
    """Test case for container_projects_zones_clusters_update

    
    """
    body = {"zone":"zone","name":"name","update":{"desiredIdentityServiceConfig":{"enabled":True},"desiredStackType":"STACK_TYPE_UNSPECIFIED","desiredNotificationConfig":{"pubsub":{"filter":{"eventType":["EVENT_TYPE_UNSPECIFIED","EVENT_TYPE_UNSPECIFIED"]},"topic":"topic","enabled":True}},"desiredVerticalPodAutoscaling":{"enabled":True},"removedAdditionalPodRangesConfig":{"podRangeInfo":[{"rangeName":"rangeName","utilization":9.301444243932576},{"rangeName":"rangeName","utilization":9.301444243932576}],"podRangeNames":["podRangeNames","podRangeNames"]},"desiredSecurityPostureConfig":{"mode":"MODE_UNSPECIFIED","vulnerabilityMode":"VULNERABILITY_MODE_UNSPECIFIED"},"enableK8sBetaApis":{"enabledApis":["enabledApis","enabledApis"]},"desiredDatabaseEncryption":{"keyName":"keyName","state":"UNKNOWN"},"desiredDnsConfig":{"clusterDnsDomain":"clusterDnsDomain","clusterDnsScope":"DNS_SCOPE_UNSPECIFIED","clusterDns":"PROVIDER_UNSPECIFIED"},"desiredMeshCertificates":{"enableCertificates":True},"desiredMasterAuthorizedNetworksConfig":{"gcpPublicCidrsAccessEnabled":True,"cidrBlocks":[{"displayName":"displayName","cidrBlock":"cidrBlock"},{"displayName":"displayName","cidrBlock":"cidrBlock"}],"enabled":True},"desiredWorkloadIdentityConfig":{"workloadPool":"workloadPool"},"desiredAuthenticatorGroupsConfig":{"securityGroup":"securityGroup","enabled":True},"desiredFleet":{"preRegistered":True,"project":"project","membership":"membership"},"desiredImageType":"desiredImageType","desiredResourceUsageExportConfig":{"consumptionMeteringConfig":{"enabled":True},"bigqueryDestination":{"datasetId":"datasetId"},"enableNetworkEgressMetering":True},"desiredLoggingService":"desiredLoggingService","desiredPrivateClusterConfig":{"enablePrivateEndpoint":True,"publicEndpoint":"publicEndpoint","masterGlobalAccessConfig":{"enabled":True},"enablePrivateNodes":True,"privateEndpointSubnetwork":"privateEndpointSubnetwork","peeringName":"peeringName","privateEndpoint":"privateEndpoint","masterIpv4CidrBlock":"masterIpv4CidrBlock"},"additionalPodRangesConfig":{"podRangeInfo":[{"rangeName":"rangeName","utilization":9.301444243932576},{"rangeName":"rangeName","utilization":9.301444243932576}],"podRangeNames":["podRangeNames","podRangeNames"]},"desiredCostManagementConfig":{"enabled":True},"desiredNodePoolAutoscaling":{"locationPolicy":"LOCATION_POLICY_UNSPECIFIED","autoprovisioned":True,"minNodeCount":6,"totalMinNodeCount":1,"maxNodeCount":1,"totalMaxNodeCount":7,"enabled":True},"desiredAutopilotWorkloadPolicyConfig":{"allowNetAdmin":True},"etag":"etag","desiredNodePoolAutoConfigResourceManagerTags":{"tags":{"key":"tags"}},"desiredEnablePrivateEndpoint":True,"desiredReleaseChannel":{"channel":"UNSPECIFIED"},"desiredShieldedNodes":{"enabled":True},"desiredIntraNodeVisibilityConfig":{"enabled":True},"desiredAddonsConfig":{"kubernetesDashboard":{"disabled":True},"configConnectorConfig":{"enabled":True},"statefulHaConfig":{"enabled":True},"gkeBackupAgentConfig":{"enabled":True},"gcePersistentDiskCsiDriverConfig":{"enabled":True},"httpLoadBalancing":{"disabled":True},"cloudRunConfig":{"loadBalancerType":"LOAD_BALANCER_TYPE_UNSPECIFIED","disabled":True},"networkPolicyConfig":{"disabled":True},"horizontalPodAutoscaling":{"disabled":True},"dnsCacheConfig":{"enabled":True},"gcsFuseCsiDriverConfig":{"enabled":True},"gcpFilestoreCsiDriverConfig":{"enabled":True}},"desiredBinaryAuthorization":{"evaluationMode":"EVALUATION_MODE_UNSPECIFIED","enabled":True},"desiredNetworkPerformanceConfig":{"totalEgressBandwidthTier":"TIER_UNSPECIFIED"},"desiredK8sBetaApis":{"enabledApis":["enabledApis","enabledApis"]},"desiredL4ilbSubsettingConfig":{"enabled":True},"desiredNodePoolId":"desiredNodePoolId","desiredGcfsConfig":{"enabled":True},"desiredInTransitEncryptionConfig":"IN_TRANSIT_ENCRYPTION_CONFIG_UNSPECIFIED","desiredNodeVersion":"desiredNodeVersion","desiredNodePoolAutoConfigNetworkTags":{"tags":["tags","tags"]},"desiredServiceExternalIpsConfig":{"enabled":True},"desiredParentProductConfig":{"productName":"productName","labels":{"key":"labels"}},"desiredMonitoringService":"desiredMonitoringService","desiredGatewayApiConfig":{"channel":"CHANNEL_UNSPECIFIED"},"desiredMasterVersion":"desiredMasterVersion","desiredMonitoringConfig":{"advancedDatapathObservabilityConfig":{"relayMode":"RELAY_MODE_UNSPECIFIED","enableMetrics":True,"enableRelay":True},"componentConfig":{"enableComponents":["COMPONENT_UNSPECIFIED","COMPONENT_UNSPECIFIED"]},"managedPrometheusConfig":{"enabled":True}},"desiredLocations":["desiredLocations","desiredLocations"],"desiredLoggingConfig":{"componentConfig":{"enableComponents":["COMPONENT_UNSPECIFIED","COMPONENT_UNSPECIFIED"]}},"desiredDatapathProvider":"DATAPATH_PROVIDER_UNSPECIFIED","desiredPrivateIpv6GoogleAccess":"PRIVATE_IPV6_GOOGLE_ACCESS_UNSPECIFIED","desiredDefaultSnatStatus":{"disabled":True},"desiredEnableFqdnNetworkPolicy":True,"desiredClusterAutoscaling":{"autoprovisioningLocations":["autoprovisioningLocations","autoprovisioningLocations"],"autoscalingProfile":"PROFILE_UNSPECIFIED","resourceLimits":[{"maximum":"maximum","minimum":"minimum","resourceType":"resourceType"},{"maximum":"maximum","minimum":"minimum","resourceType":"resourceType"}],"autoprovisioningNodePoolDefaults":{"shieldedInstanceConfig":{"enableIntegrityMonitoring":True,"enableSecureBoot":True},"management":{"autoUpgrade":True,"upgradeOptions":{"autoUpgradeStartTime":"autoUpgradeStartTime","description":"description"},"autoRepair":True},"minCpuPlatform":"minCpuPlatform","insecureKubeletReadonlyPortEnabled":True,"bootDiskKmsKey":"bootDiskKmsKey","upgradeSettings":{"maxSurge":5,"maxUnavailable":5,"blueGreenSettings":{"standardRolloutPolicy":{"batchSoakDuration":"batchSoakDuration","batchPercentage":1.4658129,"batchNodeCount":6},"nodePoolSoakDuration":"nodePoolSoakDuration"},"strategy":"NODE_POOL_UPDATE_STRATEGY_UNSPECIFIED"},"serviceAccount":"serviceAccount","diskType":"diskType","oauthScopes":["oauthScopes","oauthScopes"],"imageType":"imageType","diskSizeGb":0},"enableNodeAutoprovisioning":True},"desiredNodePoolLoggingConfig":{"variantConfig":{"variant":"VARIANT_UNSPECIFIED"}}},"clusterId":"clusterId","projectId":"projectId"}
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/v1/projects/{project_id}/zones/{zone}/clusters/{cluster_id}'.format(project_id='project_id_example', zone='zone_example', cluster_id='cluster_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_container_projects_zones_get_serverconfig(client):
    """Test case for container_projects_zones_get_serverconfig

    
    """
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example'),
                    ('name', 'name_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/projects/{project_id}/zones/{zone}/serverconfig'.format(project_id='project_id_example', zone='zone_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_container_projects_zones_operations_cancel(client):
    """Test case for container_projects_zones_operations_cancel

    
    """
    body = {"zone":"zone","name":"name","operationId":"operationId","projectId":"projectId"}
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/projects/{project_id}/zones/{zone}/operations/{operation_idcance}'.format(project_id='project_id_example', zone='zone_example', operation_id='operation_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_container_projects_zones_operations_get(client):
    """Test case for container_projects_zones_operations_get

    
    """
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example'),
                    ('name', 'name_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/projects/{project_id}/zones/{zone}/operations/{operation_id}'.format(project_id='project_id_example', zone='zone_example', operation_id='operation_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_container_projects_zones_operations_list(client):
    """Test case for container_projects_zones_operations_list

    
    """
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example'),
                    ('parent', 'parent_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/projects/{project_id}/zones/{zone}/operations'.format(project_id='project_id_example', zone='zone_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

