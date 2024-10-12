# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.bare_metal_admin_cluster import BareMetalAdminCluster
from openapi_server.models.bare_metal_cluster import BareMetalCluster
from openapi_server.models.bare_metal_node_pool import BareMetalNodePool
from openapi_server.models.enroll_bare_metal_admin_cluster_request import EnrollBareMetalAdminClusterRequest
from openapi_server.models.enroll_bare_metal_cluster_request import EnrollBareMetalClusterRequest
from openapi_server.models.enroll_bare_metal_node_pool_request import EnrollBareMetalNodePoolRequest
from openapi_server.models.enroll_vmware_admin_cluster_request import EnrollVmwareAdminClusterRequest
from openapi_server.models.enroll_vmware_cluster_request import EnrollVmwareClusterRequest
from openapi_server.models.enroll_vmware_node_pool_request import EnrollVmwareNodePoolRequest
from openapi_server.models.list_bare_metal_admin_clusters_response import ListBareMetalAdminClustersResponse
from openapi_server.models.list_bare_metal_clusters_response import ListBareMetalClustersResponse
from openapi_server.models.list_bare_metal_node_pools_response import ListBareMetalNodePoolsResponse
from openapi_server.models.list_locations_response import ListLocationsResponse
from openapi_server.models.list_operations_response import ListOperationsResponse
from openapi_server.models.list_vmware_admin_clusters_response import ListVmwareAdminClustersResponse
from openapi_server.models.list_vmware_clusters_response import ListVmwareClustersResponse
from openapi_server.models.list_vmware_node_pools_response import ListVmwareNodePoolsResponse
from openapi_server.models.operation import Operation
from openapi_server.models.policy import Policy
from openapi_server.models.query_bare_metal_admin_version_config_response import QueryBareMetalAdminVersionConfigResponse
from openapi_server.models.query_bare_metal_version_config_response import QueryBareMetalVersionConfigResponse
from openapi_server.models.query_vmware_version_config_response import QueryVmwareVersionConfigResponse
from openapi_server.models.set_iam_policy_request import SetIamPolicyRequest
from openapi_server.models.test_iam_permissions_request import TestIamPermissionsRequest
from openapi_server.models.test_iam_permissions_response import TestIamPermissionsResponse
from openapi_server.models.vmware_cluster import VmwareCluster
from openapi_server.models.vmware_node_pool import VmwareNodePool


pytestmark = pytest.mark.asyncio

async def test_gkeonprem_projects_locations_bare_metal_admin_clusters_create(client):
    """Test case for gkeonprem_projects_locations_bare_metal_admin_clusters_create

    
    """
    body = {"fleet":{"membership":"membership"},"clusterOperations":{"enableApplicationLogs":True},"annotations":{"key":"annotations"},"description":"description","reconciling":True,"storage":{"lvpShareConfig":{"sharedPathPvCount":5,"lvpConfig":{"path":"path","storageClass":"storageClass"}},"lvpNodeMountsConfig":{"path":"path","storageClass":"storageClass"}},"nodeConfig":{"maxPodsPerNode":"maxPodsPerNode"},"validationCheck":{"scenario":"SCENARIO_UNSPECIFIED","option":"OPTIONS_UNSPECIFIED","status":{"result":[{"reason":"reason","description":"description","details":"details","state":"STATE_UNKNOWN","category":"category"},{"reason":"reason","description":"description","details":"details","state":"STATE_UNKNOWN","category":"category"}]}},"maintenanceStatus":{"machineDrainStatus":{"drainedMachines":[{"nodeIp":"nodeIp"},{"nodeIp":"nodeIp"}],"drainingMachines":[{"nodeIp":"nodeIp","podCount":5},{"nodeIp":"nodeIp","podCount":5}]}},"uid":"uid","endpoint":"endpoint","maintenanceConfig":{"maintenanceAddressCidrBlocks":["maintenanceAddressCidrBlocks","maintenanceAddressCidrBlocks"]},"controlPlane":{"apiServerArgs":[{"argument":"argument","value":"value"},{"argument":"argument","value":"value"}],"controlPlaneNodePoolConfig":{"nodePoolConfig":{"kubeletConfig":{"registryBurst":0,"registryPullQps":6,"serializeImagePullsDisabled":True},"nodeConfigs":[{"nodeIp":"nodeIp","labels":{"key":"labels"}},{"nodeIp":"nodeIp","labels":{"key":"labels"}}],"taints":[{"effect":"EFFECT_UNSPECIFIED","value":"value","key":"key"},{"effect":"EFFECT_UNSPECIFIED","value":"value","key":"key"}],"operatingSystem":"OPERATING_SYSTEM_UNSPECIFIED","labels":{"key":"labels"}}}},"loadBalancer":{"portConfig":{"controlPlaneLoadBalancerPort":1},"vipConfig":{"controlPlaneVip":"controlPlaneVip"},"manualLbConfig":{"enabled":True}},"bareMetalVersion":"bareMetalVersion","state":"STATE_UNSPECIFIED","binaryAuthorization":{"evaluationMode":"EVALUATION_MODE_UNSPECIFIED"},"nodeAccessConfig":{"loginUser":"loginUser"},"networkConfig":{"islandModeCidr":{"serviceAddressCidrBlocks":["serviceAddressCidrBlocks","serviceAddressCidrBlocks"],"podAddressCidrBlocks":["podAddressCidrBlocks","podAddressCidrBlocks"]}},"osEnvironmentConfig":{"packageRepoExcluded":True},"updateTime":"updateTime","localName":"localName","proxy":{"noProxy":["noProxy","noProxy"],"uri":"uri"},"securityConfig":{"authorization":{"adminUsers":[{"username":"username"},{"username":"username"}]}},"createTime":"createTime","deleteTime":"deleteTime","name":"name","etag":"etag","status":{"errorMessage":"errorMessage","conditions":[{"reason":"reason","state":"STATE_UNSPECIFIED","lastTransitionTime":"lastTransitionTime","message":"message","type":"type"},{"reason":"reason","state":"STATE_UNSPECIFIED","lastTransitionTime":"lastTransitionTime","message":"message","type":"type"}]}}
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
                    ('bareMetalAdminClusterId', 'bare_metal_admin_cluster_id_example'),
                    ('validateOnly', True)]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/{parent}/bareMetalAdminClusters'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_gkeonprem_projects_locations_bare_metal_admin_clusters_enroll(client):
    """Test case for gkeonprem_projects_locations_bare_metal_admin_clusters_enroll

    
    """
    body = {"bareMetalAdminClusterId":"bareMetalAdminClusterId","membership":"membership"}
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
        path='/v1/{parent}/bareMetalAdminClusters:enroll'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_gkeonprem_projects_locations_bare_metal_admin_clusters_list(client):
    """Test case for gkeonprem_projects_locations_bare_metal_admin_clusters_list

    
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
                    ('pageSize', 56),
                    ('pageToken', 'page_token_example'),
                    ('view', 'view_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/{parent}/bareMetalAdminClusters'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_gkeonprem_projects_locations_bare_metal_admin_clusters_query_version_config(client):
    """Test case for gkeonprem_projects_locations_bare_metal_admin_clusters_query_version_config

    
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
                    ('upgradeConfig.clusterName', 'upgrade_config_cluster_name_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/{parent}/bareMetalAdminClusters:queryVersionConfig'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_gkeonprem_projects_locations_bare_metal_clusters_bare_metal_node_pools_create(client):
    """Test case for gkeonprem_projects_locations_bare_metal_clusters_bare_metal_node_pools_create

    
    """
    body = {"nodePoolConfig":{"kubeletConfig":{"registryBurst":0,"registryPullQps":6,"serializeImagePullsDisabled":True},"nodeConfigs":[{"nodeIp":"nodeIp","labels":{"key":"labels"}},{"nodeIp":"nodeIp","labels":{"key":"labels"}}],"taints":[{"effect":"EFFECT_UNSPECIFIED","value":"value","key":"key"},{"effect":"EFFECT_UNSPECIFIED","value":"value","key":"key"}],"operatingSystem":"OPERATING_SYSTEM_UNSPECIFIED","labels":{"key":"labels"}},"displayName":"displayName","annotations":{"key":"annotations"},"reconciling":True,"updateTime":"updateTime","upgradePolicy":{"parallelUpgradeConfig":{"minimumAvailableNodes":6,"concurrentNodes":0}},"uid":"uid","createTime":"createTime","deleteTime":"deleteTime","name":"name","etag":"etag","state":"STATE_UNSPECIFIED","status":{"errorMessage":"errorMessage","conditions":[{"reason":"reason","state":"STATE_UNSPECIFIED","lastTransitionTime":"lastTransitionTime","message":"message","type":"type"},{"reason":"reason","state":"STATE_UNSPECIFIED","lastTransitionTime":"lastTransitionTime","message":"message","type":"type"}]}}
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
                    ('bareMetalNodePoolId', 'bare_metal_node_pool_id_example'),
                    ('validateOnly', True)]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/{parent}/bareMetalNodePools'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_gkeonprem_projects_locations_bare_metal_clusters_bare_metal_node_pools_enroll(client):
    """Test case for gkeonprem_projects_locations_bare_metal_clusters_bare_metal_node_pools_enroll

    
    """
    body = {"validateOnly":True,"bareMetalNodePoolId":"bareMetalNodePoolId"}
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
        path='/v1/{parent}/bareMetalNodePools:enroll'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_gkeonprem_projects_locations_bare_metal_clusters_bare_metal_node_pools_list(client):
    """Test case for gkeonprem_projects_locations_bare_metal_clusters_bare_metal_node_pools_list

    
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
                    ('pageSize', 56),
                    ('pageToken', 'page_token_example'),
                    ('view', 'view_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/{parent}/bareMetalNodePools'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_gkeonprem_projects_locations_bare_metal_clusters_create(client):
    """Test case for gkeonprem_projects_locations_bare_metal_clusters_create

    
    """
    body = {"fleet":{"membership":"membership"},"clusterOperations":{"enableApplicationLogs":True},"annotations":{"key":"annotations"},"description":"description","reconciling":True,"storage":{"lvpShareConfig":{"sharedPathPvCount":5,"lvpConfig":{"path":"path","storageClass":"storageClass"}},"lvpNodeMountsConfig":{"path":"path","storageClass":"storageClass"}},"adminClusterName":"adminClusterName","nodeConfig":{"containerRuntime":"CONTAINER_RUNTIME_UNSPECIFIED","maxPodsPerNode":"maxPodsPerNode"},"validationCheck":{"scenario":"SCENARIO_UNSPECIFIED","option":"OPTIONS_UNSPECIFIED","status":{"result":[{"reason":"reason","description":"description","details":"details","state":"STATE_UNKNOWN","category":"category"},{"reason":"reason","description":"description","details":"details","state":"STATE_UNKNOWN","category":"category"}]}},"maintenanceStatus":{"machineDrainStatus":{"drainedMachines":[{"nodeIp":"nodeIp"},{"nodeIp":"nodeIp"}],"drainingMachines":[{"nodeIp":"nodeIp","podCount":6},{"nodeIp":"nodeIp","podCount":6}]}},"uid":"uid","endpoint":"endpoint","maintenanceConfig":{"maintenanceAddressCidrBlocks":["maintenanceAddressCidrBlocks","maintenanceAddressCidrBlocks"]},"controlPlane":{"apiServerArgs":[{"argument":"argument","value":"value"},{"argument":"argument","value":"value"}],"controlPlaneNodePoolConfig":{"nodePoolConfig":{"kubeletConfig":{"registryBurst":0,"registryPullQps":6,"serializeImagePullsDisabled":True},"nodeConfigs":[{"nodeIp":"nodeIp","labels":{"key":"labels"}},{"nodeIp":"nodeIp","labels":{"key":"labels"}}],"taints":[{"effect":"EFFECT_UNSPECIFIED","value":"value","key":"key"},{"effect":"EFFECT_UNSPECIFIED","value":"value","key":"key"}],"operatingSystem":"OPERATING_SYSTEM_UNSPECIFIED","labels":{"key":"labels"}}}},"loadBalancer":{"portConfig":{"controlPlaneLoadBalancerPort":0},"bgpLbConfig":{"bgpPeerConfigs":[{"ipAddress":"ipAddress","asn":"asn","controlPlaneNodes":["controlPlaneNodes","controlPlaneNodes"]},{"ipAddress":"ipAddress","asn":"asn","controlPlaneNodes":["controlPlaneNodes","controlPlaneNodes"]}],"addressPools":[{"addresses":["addresses","addresses"],"avoidBuggyIps":True,"pool":"pool","manualAssign":True},{"addresses":["addresses","addresses"],"avoidBuggyIps":True,"pool":"pool","manualAssign":True}],"loadBalancerNodePoolConfig":{"nodePoolConfig":{"kubeletConfig":{"registryBurst":0,"registryPullQps":6,"serializeImagePullsDisabled":True},"nodeConfigs":[{"nodeIp":"nodeIp","labels":{"key":"labels"}},{"nodeIp":"nodeIp","labels":{"key":"labels"}}],"taints":[{"effect":"EFFECT_UNSPECIFIED","value":"value","key":"key"},{"effect":"EFFECT_UNSPECIFIED","value":"value","key":"key"}],"operatingSystem":"OPERATING_SYSTEM_UNSPECIFIED","labels":{"key":"labels"}}},"asn":"asn"},"metalLbConfig":{"addressPools":[{"addresses":["addresses","addresses"],"avoidBuggyIps":True,"pool":"pool","manualAssign":True},{"addresses":["addresses","addresses"],"avoidBuggyIps":True,"pool":"pool","manualAssign":True}],"loadBalancerNodePoolConfig":{"nodePoolConfig":{"kubeletConfig":{"registryBurst":0,"registryPullQps":6,"serializeImagePullsDisabled":True},"nodeConfigs":[{"nodeIp":"nodeIp","labels":{"key":"labels"}},{"nodeIp":"nodeIp","labels":{"key":"labels"}}],"taints":[{"effect":"EFFECT_UNSPECIFIED","value":"value","key":"key"},{"effect":"EFFECT_UNSPECIFIED","value":"value","key":"key"}],"operatingSystem":"OPERATING_SYSTEM_UNSPECIFIED","labels":{"key":"labels"}}}},"vipConfig":{"ingressVip":"ingressVip","controlPlaneVip":"controlPlaneVip"},"manualLbConfig":{"enabled":True}},"bareMetalVersion":"bareMetalVersion","state":"STATE_UNSPECIFIED","binaryAuthorization":{"evaluationMode":"EVALUATION_MODE_UNSPECIFIED"},"nodeAccessConfig":{"loginUser":"loginUser"},"adminClusterMembership":"adminClusterMembership","networkConfig":{"advancedNetworking":True,"islandModeCidr":{"serviceAddressCidrBlocks":["serviceAddressCidrBlocks","serviceAddressCidrBlocks"],"podAddressCidrBlocks":["podAddressCidrBlocks","podAddressCidrBlocks"]},"multipleNetworkInterfacesConfig":{"enabled":True},"srIovConfig":{"enabled":True}},"osEnvironmentConfig":{"packageRepoExcluded":True},"updateTime":"updateTime","upgradePolicy":{"policy":"NODE_POOL_POLICY_UNSPECIFIED"},"localName":"localName","proxy":{"noProxy":["noProxy","noProxy"],"uri":"uri"},"securityConfig":{"authorization":{"adminUsers":[{"username":"username"},{"username":"username"}]}},"createTime":"createTime","deleteTime":"deleteTime","name":"name","etag":"etag","status":{"errorMessage":"errorMessage","conditions":[{"reason":"reason","state":"STATE_UNSPECIFIED","lastTransitionTime":"lastTransitionTime","message":"message","type":"type"},{"reason":"reason","state":"STATE_UNSPECIFIED","lastTransitionTime":"lastTransitionTime","message":"message","type":"type"}]}}
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
                    ('bareMetalClusterId', 'bare_metal_cluster_id_example'),
                    ('validateOnly', True)]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/{parent}/bareMetalClusters'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_gkeonprem_projects_locations_bare_metal_clusters_enroll(client):
    """Test case for gkeonprem_projects_locations_bare_metal_clusters_enroll

    
    """
    body = {"localName":"localName","bareMetalClusterId":"bareMetalClusterId","adminClusterMembership":"adminClusterMembership"}
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
        path='/v1/{parent}/bareMetalClusters:enroll'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_gkeonprem_projects_locations_bare_metal_clusters_list(client):
    """Test case for gkeonprem_projects_locations_bare_metal_clusters_list

    
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
                    ('pageToken', 'page_token_example'),
                    ('view', 'view_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/{parent}/bareMetalClusters'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_gkeonprem_projects_locations_bare_metal_clusters_query_version_config(client):
    """Test case for gkeonprem_projects_locations_bare_metal_clusters_query_version_config

    
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
                    ('createConfig.adminClusterMembership', 'create_config_admin_cluster_membership_example'),
                    ('createConfig.adminClusterName', 'create_config_admin_cluster_name_example'),
                    ('upgradeConfig.clusterName', 'upgrade_config_cluster_name_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/{parent}/bareMetalClusters:queryVersionConfig'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_gkeonprem_projects_locations_list(client):
    """Test case for gkeonprem_projects_locations_list

    
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
        path='/v1/{name}/locations'.format(name='name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_gkeonprem_projects_locations_operations_cancel(client):
    """Test case for gkeonprem_projects_locations_operations_cancel

    
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
        path='/v1/{namecance}'.format(name='name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_gkeonprem_projects_locations_vmware_admin_clusters_enroll(client):
    """Test case for gkeonprem_projects_locations_vmware_admin_clusters_enroll

    
    """
    body = {"membership":"membership","vmwareAdminClusterId":"vmwareAdminClusterId"}
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
        path='/v1/{parent}/vmwareAdminClusters:enroll'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_gkeonprem_projects_locations_vmware_admin_clusters_list(client):
    """Test case for gkeonprem_projects_locations_vmware_admin_clusters_list

    
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
                    ('pageSize', 56),
                    ('pageToken', 'page_token_example'),
                    ('view', 'view_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/{parent}/vmwareAdminClusters'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_gkeonprem_projects_locations_vmware_clusters_create(client):
    """Test case for gkeonprem_projects_locations_vmware_clusters_create

    
    """
    body = {"disableBundledIngress":True,"fleet":{"membership":"membership"},"dataplaneV2":{"dataplaneV2Enabled":True,"advancedNetworking":True,"windowsDataplaneV2Enabled":True,"forwardMode":"forwardMode"},"annotations":{"key":"annotations"},"description":"description","reconciling":True,"storage":{"vsphereCsiDisabled":True},"antiAffinityGroups":{"aagConfigDisabled":True},"adminClusterName":"adminClusterName","validationCheck":{"scenario":"SCENARIO_UNSPECIFIED","option":"OPTIONS_UNSPECIFIED","status":{"result":[{"reason":"reason","description":"description","details":"details","state":"STATE_UNKNOWN","category":"category"},{"reason":"reason","description":"description","details":"details","state":"STATE_UNKNOWN","category":"category"}]}},"enableControlPlaneV2":True,"authorization":{"adminUsers":[{"username":"username"},{"username":"username"}]},"uid":"uid","endpoint":"endpoint","vmTrackingEnabled":True,"loadBalancer":{"seesawConfig":{"stackdriverName":"stackdriverName","masterIp":"masterIp","ipBlocks":[{"netmask":"netmask","ips":[{"hostname":"hostname","ip":"ip"},{"hostname":"hostname","ip":"ip"}],"gateway":"gateway"},{"netmask":"netmask","ips":[{"hostname":"hostname","ip":"ip"},{"hostname":"hostname","ip":"ip"}],"gateway":"gateway"}],"enableHa":True,"vms":["vms","vms"],"group":"group"},"f5Config":{"address":"address","partition":"partition","snatPool":"snatPool"},"metalLbConfig":{"addressPools":[{"addresses":["addresses","addresses"],"avoidBuggyIps":True,"pool":"pool","manualAssign":True},{"addresses":["addresses","addresses"],"avoidBuggyIps":True,"pool":"pool","manualAssign":True}]},"vipConfig":{"ingressVip":"ingressVip","controlPlaneVip":"controlPlaneVip"},"manualLbConfig":{"konnectivityServerNodePort":5,"ingressHttpNodePort":6,"ingressHttpsNodePort":1,"controlPlaneNodePort":0}},"vcenter":{"cluster":"cluster","address":"address","folder":"folder","datastore":"datastore","caCertData":"caCertData","datacenter":"datacenter","storagePolicyName":"storagePolicyName","resourcePool":"resourcePool"},"state":"STATE_UNSPECIFIED","binaryAuthorization":{"evaluationMode":"EVALUATION_MODE_UNSPECIFIED"},"controlPlaneNode":{"autoResizeConfig":{"enabled":True},"memory":"memory","vsphereConfig":{"datastore":"datastore","storagePolicyName":"storagePolicyName"},"cpus":"cpus","replicas":"replicas"},"adminClusterMembership":"adminClusterMembership","networkConfig":{"dhcpIpConfig":{"enabled":True},"hostConfig":{"ntpServers":["ntpServers","ntpServers"],"dnsServers":["dnsServers","dnsServers"],"dnsSearchDomains":["dnsSearchDomains","dnsSearchDomains"]},"serviceAddressCidrBlocks":["serviceAddressCidrBlocks","serviceAddressCidrBlocks"],"vcenterNetwork":"vcenterNetwork","controlPlaneV2Config":{"controlPlaneIpBlock":{"netmask":"netmask","ips":[{"hostname":"hostname","ip":"ip"},{"hostname":"hostname","ip":"ip"}],"gateway":"gateway"}},"staticIpConfig":{"ipBlocks":[{"netmask":"netmask","ips":[{"hostname":"hostname","ip":"ip"},{"hostname":"hostname","ip":"ip"}],"gateway":"gateway"},{"netmask":"netmask","ips":[{"hostname":"hostname","ip":"ip"},{"hostname":"hostname","ip":"ip"}],"gateway":"gateway"}]},"podAddressCidrBlocks":["podAddressCidrBlocks","podAddressCidrBlocks"]},"updateTime":"updateTime","autoRepairConfig":{"enabled":True},"upgradePolicy":{"controlPlaneOnly":True},"localName":"localName","onPremVersion":"onPremVersion","createTime":"createTime","deleteTime":"deleteTime","name":"name","etag":"etag","status":{"errorMessage":"errorMessage","conditions":[{"reason":"reason","state":"STATE_UNSPECIFIED","lastTransitionTime":"lastTransitionTime","message":"message","type":"type"},{"reason":"reason","state":"STATE_UNSPECIFIED","lastTransitionTime":"lastTransitionTime","message":"message","type":"type"}]}}
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
                    ('validateOnly', True),
                    ('vmwareClusterId', 'vmware_cluster_id_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/{parent}/vmwareClusters'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_gkeonprem_projects_locations_vmware_clusters_enroll(client):
    """Test case for gkeonprem_projects_locations_vmware_clusters_enroll

    
    """
    body = {"localName":"localName","validateOnly":True,"adminClusterMembership":"adminClusterMembership","vmwareClusterId":"vmwareClusterId"}
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
        path='/v1/{parent}/vmwareClusters:enroll'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_gkeonprem_projects_locations_vmware_clusters_list(client):
    """Test case for gkeonprem_projects_locations_vmware_clusters_list

    
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
                    ('pageToken', 'page_token_example'),
                    ('view', 'view_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/{parent}/vmwareClusters'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_gkeonprem_projects_locations_vmware_clusters_query_version_config(client):
    """Test case for gkeonprem_projects_locations_vmware_clusters_query_version_config

    
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
                    ('createConfig.adminClusterMembership', 'create_config_admin_cluster_membership_example'),
                    ('createConfig.adminClusterName', 'create_config_admin_cluster_name_example'),
                    ('upgradeConfig.clusterName', 'upgrade_config_cluster_name_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/{parent}/vmwareClusters:queryVersionConfig'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_gkeonprem_projects_locations_vmware_clusters_vmware_node_pools_create(client):
    """Test case for gkeonprem_projects_locations_vmware_clusters_vmware_node_pools_create

    
    """
    body = {"displayName":"displayName","annotations":{"key":"annotations"},"reconciling":True,"updateTime":"updateTime","onPremVersion":"onPremVersion","uid":"uid","nodePoolAutoscaling":{"maxReplicas":0,"minReplicas":6},"createTime":"createTime","deleteTime":"deleteTime","name":"name","etag":"etag","state":"STATE_UNSPECIFIED","config":{"image":"image","memoryMb":"memoryMb","vsphereConfig":{"hostGroups":["hostGroups","hostGroups"],"datastore":"datastore","tags":[{"tag":"tag","category":"category"},{"tag":"tag","category":"category"}]},"cpus":"cpus","replicas":"replicas","enableLoadBalancer":True,"taints":[{"effect":"EFFECT_UNSPECIFIED","value":"value","key":"key"},{"effect":"EFFECT_UNSPECIFIED","value":"value","key":"key"}],"bootDiskSizeGb":"bootDiskSizeGb","imageType":"imageType","labels":{"key":"labels"}},"status":{"errorMessage":"errorMessage","conditions":[{"reason":"reason","state":"STATE_UNSPECIFIED","lastTransitionTime":"lastTransitionTime","message":"message","type":"type"},{"reason":"reason","state":"STATE_UNSPECIFIED","lastTransitionTime":"lastTransitionTime","message":"message","type":"type"}]}}
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
                    ('validateOnly', True),
                    ('vmwareNodePoolId', 'vmware_node_pool_id_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/{parent}/vmwareNodePools'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_gkeonprem_projects_locations_vmware_clusters_vmware_node_pools_delete(client):
    """Test case for gkeonprem_projects_locations_vmware_clusters_vmware_node_pools_delete

    
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
                    ('allowMissing', True),
                    ('etag', 'etag_example'),
                    ('ignoreErrors', True),
                    ('validateOnly', True)]
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

async def test_gkeonprem_projects_locations_vmware_clusters_vmware_node_pools_enroll(client):
    """Test case for gkeonprem_projects_locations_vmware_clusters_vmware_node_pools_enroll

    
    """
    body = {"vmwareNodePoolId":"vmwareNodePoolId"}
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
        path='/v1/{parent}/vmwareNodePools:enroll'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_gkeonprem_projects_locations_vmware_clusters_vmware_node_pools_get_iam_policy(client):
    """Test case for gkeonprem_projects_locations_vmware_clusters_vmware_node_pools_get_iam_policy

    
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
                    ('options.requestedPolicyVersion', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/{resourceget_iam_polic}'.format(resource='resource_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_gkeonprem_projects_locations_vmware_clusters_vmware_node_pools_list(client):
    """Test case for gkeonprem_projects_locations_vmware_clusters_vmware_node_pools_list

    
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
                    ('pageSize', 56),
                    ('pageToken', 'page_token_example'),
                    ('view', 'view_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/{parent}/vmwareNodePools'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_gkeonprem_projects_locations_vmware_clusters_vmware_node_pools_operations_get(client):
    """Test case for gkeonprem_projects_locations_vmware_clusters_vmware_node_pools_operations_get

    
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
                    ('view', 'view_example')]
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

async def test_gkeonprem_projects_locations_vmware_clusters_vmware_node_pools_operations_list(client):
    """Test case for gkeonprem_projects_locations_vmware_clusters_vmware_node_pools_operations_list

    
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
        path='/v1/{name}/operations'.format(name='name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_gkeonprem_projects_locations_vmware_clusters_vmware_node_pools_patch(client):
    """Test case for gkeonprem_projects_locations_vmware_clusters_vmware_node_pools_patch

    
    """
    body = {"displayName":"displayName","annotations":{"key":"annotations"},"reconciling":True,"updateTime":"updateTime","onPremVersion":"onPremVersion","uid":"uid","nodePoolAutoscaling":{"maxReplicas":0,"minReplicas":6},"createTime":"createTime","deleteTime":"deleteTime","name":"name","etag":"etag","state":"STATE_UNSPECIFIED","config":{"image":"image","memoryMb":"memoryMb","vsphereConfig":{"hostGroups":["hostGroups","hostGroups"],"datastore":"datastore","tags":[{"tag":"tag","category":"category"},{"tag":"tag","category":"category"}]},"cpus":"cpus","replicas":"replicas","enableLoadBalancer":True,"taints":[{"effect":"EFFECT_UNSPECIFIED","value":"value","key":"key"},{"effect":"EFFECT_UNSPECIFIED","value":"value","key":"key"}],"bootDiskSizeGb":"bootDiskSizeGb","imageType":"imageType","labels":{"key":"labels"}},"status":{"errorMessage":"errorMessage","conditions":[{"reason":"reason","state":"STATE_UNSPECIFIED","lastTransitionTime":"lastTransitionTime","message":"message","type":"type"},{"reason":"reason","state":"STATE_UNSPECIFIED","lastTransitionTime":"lastTransitionTime","message":"message","type":"type"}]}}
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
                    ('updateMask', 'update_mask_example'),
                    ('validateOnly', True)]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/v1/{name}'.format(name='name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_gkeonprem_projects_locations_vmware_clusters_vmware_node_pools_set_iam_policy(client):
    """Test case for gkeonprem_projects_locations_vmware_clusters_vmware_node_pools_set_iam_policy

    
    """
    body = {"policy":{"bindings":[{"condition":{"expression":"expression","description":"description","location":"location","title":"title"},"role":"role","members":["members","members"]},{"condition":{"expression":"expression","description":"description","location":"location","title":"title"},"role":"role","members":["members","members"]}],"etag":"etag","version":0}}
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
        path='/v1/{resourceset_iam_polic}'.format(resource='resource_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_gkeonprem_projects_locations_vmware_clusters_vmware_node_pools_test_iam_permissions(client):
    """Test case for gkeonprem_projects_locations_vmware_clusters_vmware_node_pools_test_iam_permissions

    
    """
    body = {"permissions":["permissions","permissions"]}
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
        path='/v1/{resourcetest_iam_permission}'.format(resource='resource_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_gkeonprem_projects_locations_vmware_clusters_vmware_node_pools_unenroll(client):
    """Test case for gkeonprem_projects_locations_vmware_clusters_vmware_node_pools_unenroll

    
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
                    ('allowMissing', True),
                    ('etag', 'etag_example'),
                    ('validateOnly', True)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/v1/{nameunenrol}'.format(name='name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

