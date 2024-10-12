# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.autoscaling_policy import AutoscalingPolicy
from openapi_server.models.batch import Batch
from openapi_server.models.cluster import Cluster
from openapi_server.models.diagnose_cluster_request import DiagnoseClusterRequest
from openapi_server.models.get_iam_policy_request import GetIamPolicyRequest
from openapi_server.models.inject_credentials_request import InjectCredentialsRequest
from openapi_server.models.instantiate_workflow_template_request import InstantiateWorkflowTemplateRequest
from openapi_server.models.job import Job
from openapi_server.models.list_autoscaling_policies_response import ListAutoscalingPoliciesResponse
from openapi_server.models.list_batches_response import ListBatchesResponse
from openapi_server.models.list_clusters_response import ListClustersResponse
from openapi_server.models.list_jobs_response import ListJobsResponse
from openapi_server.models.list_session_templates_response import ListSessionTemplatesResponse
from openapi_server.models.list_sessions_response import ListSessionsResponse
from openapi_server.models.list_workflow_templates_response import ListWorkflowTemplatesResponse
from openapi_server.models.node_group import NodeGroup
from openapi_server.models.operation import Operation
from openapi_server.models.policy import Policy
from openapi_server.models.repair_cluster_request import RepairClusterRequest
from openapi_server.models.repair_node_group_request import RepairNodeGroupRequest
from openapi_server.models.resize_node_group_request import ResizeNodeGroupRequest
from openapi_server.models.session import Session
from openapi_server.models.session_template import SessionTemplate
from openapi_server.models.set_iam_policy_request import SetIamPolicyRequest
from openapi_server.models.start_cluster_request import StartClusterRequest
from openapi_server.models.stop_cluster_request import StopClusterRequest
from openapi_server.models.submit_job_request import SubmitJobRequest
from openapi_server.models.terminate_session_request import TerminateSessionRequest
from openapi_server.models.test_iam_permissions_request import TestIamPermissionsRequest
from openapi_server.models.test_iam_permissions_response import TestIamPermissionsResponse
from openapi_server.models.workflow_template import WorkflowTemplate


pytestmark = pytest.mark.asyncio

async def test_dataproc_projects_locations_batches_create(client):
    """Test case for dataproc_projects_locations_batches_create

    
    """
    body = {"creator":"creator","stateMessage":"stateMessage","sparkRBatch":{"args":["args","args"],"mainRFileUri":"mainRFileUri","archiveUris":["archiveUris","archiveUris"],"fileUris":["fileUris","fileUris"]},"uuid":"uuid","sparkSqlBatch":{"queryFileUri":"queryFileUri","jarFileUris":["jarFileUris","jarFileUris"],"queryVariables":{"key":"queryVariables"}},"labels":{"key":"labels"},"sparkBatch":{"args":["args","args"],"mainClass":"mainClass","archiveUris":["archiveUris","archiveUris"],"mainJarFileUri":"mainJarFileUri","fileUris":["fileUris","fileUris"],"jarFileUris":["jarFileUris","jarFileUris"]},"stateHistory":[{"stateMessage":"stateMessage","state":"STATE_UNSPECIFIED","stateStartTime":"stateStartTime"},{"stateMessage":"stateMessage","state":"STATE_UNSPECIFIED","stateStartTime":"stateStartTime"}],"createTime":"createTime","stateTime":"stateTime","name":"name","pysparkBatch":{"args":["args","args"],"archiveUris":["archiveUris","archiveUris"],"mainPythonFileUri":"mainPythonFileUri","fileUris":["fileUris","fileUris"],"jarFileUris":["jarFileUris","jarFileUris"],"pythonFileUris":["pythonFileUris","pythonFileUris"]},"runtimeConfig":{"repositoryConfig":{"pypiRepositoryConfig":{"pypiRepository":"pypiRepository"}},"containerImage":"containerImage","version":"version","properties":{"key":"properties"}},"environmentConfig":{"executionConfig":{"networkUri":"networkUri","networkTags":["networkTags","networkTags"],"kmsKey":"kmsKey","stagingBucket":"stagingBucket","subnetworkUri":"subnetworkUri","serviceAccount":"serviceAccount","idleTtl":"idleTtl","ttl":"ttl"},"peripheralsConfig":{"sparkHistoryServerConfig":{"dataprocCluster":"dataprocCluster"},"metastoreService":"metastoreService"}},"state":"STATE_UNSPECIFIED","operation":"operation","runtimeInfo":{"endpoints":{"key":"endpoints"},"outputUri":"outputUri","diagnosticOutputUri":"diagnosticOutputUri","currentUsage":{"acceleratorType":"acceleratorType","milliDcu":"milliDcu","milliDcuPremium":"milliDcuPremium","shuffleStorageGb":"shuffleStorageGb","snapshotTime":"snapshotTime","milliAccelerator":"milliAccelerator","shuffleStorageGbPremium":"shuffleStorageGbPremium"},"approximateUsage":{"acceleratorType":"acceleratorType","milliAcceleratorSeconds":"milliAcceleratorSeconds","milliDcuSeconds":"milliDcuSeconds","shuffleStorageGbSeconds":"shuffleStorageGbSeconds"}}}
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
                    ('batchId', 'batch_id_example'),
                    ('requestId', 'request_id_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/{parent}/batches'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dataproc_projects_locations_batches_list(client):
    """Test case for dataproc_projects_locations_batches_list

    
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
                    ('orderBy', 'order_by_example'),
                    ('pageSize', 56),
                    ('pageToken', 'page_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/{parent}/batches'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dataproc_projects_locations_session_templates_create(client):
    """Test case for dataproc_projects_locations_session_templates_create

    
    """
    body = {"creator":"creator","createTime":"createTime","jupyterSession":{"displayName":"displayName","kernel":"KERNEL_UNSPECIFIED"},"name":"name","description":"description","runtimeConfig":{"repositoryConfig":{"pypiRepositoryConfig":{"pypiRepository":"pypiRepository"}},"containerImage":"containerImage","version":"version","properties":{"key":"properties"}},"updateTime":"updateTime","environmentConfig":{"executionConfig":{"networkUri":"networkUri","networkTags":["networkTags","networkTags"],"kmsKey":"kmsKey","stagingBucket":"stagingBucket","subnetworkUri":"subnetworkUri","serviceAccount":"serviceAccount","idleTtl":"idleTtl","ttl":"ttl"},"peripheralsConfig":{"sparkHistoryServerConfig":{"dataprocCluster":"dataprocCluster"},"metastoreService":"metastoreService"}},"uuid":"uuid","labels":{"key":"labels"}}
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
        path='/v1/{parent}/sessionTemplates'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dataproc_projects_locations_session_templates_list(client):
    """Test case for dataproc_projects_locations_session_templates_list

    
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
        path='/v1/{parent}/sessionTemplates'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dataproc_projects_locations_session_templates_patch(client):
    """Test case for dataproc_projects_locations_session_templates_patch

    
    """
    body = {"creator":"creator","createTime":"createTime","jupyterSession":{"displayName":"displayName","kernel":"KERNEL_UNSPECIFIED"},"name":"name","description":"description","runtimeConfig":{"repositoryConfig":{"pypiRepositoryConfig":{"pypiRepository":"pypiRepository"}},"containerImage":"containerImage","version":"version","properties":{"key":"properties"}},"updateTime":"updateTime","environmentConfig":{"executionConfig":{"networkUri":"networkUri","networkTags":["networkTags","networkTags"],"kmsKey":"kmsKey","stagingBucket":"stagingBucket","subnetworkUri":"subnetworkUri","serviceAccount":"serviceAccount","idleTtl":"idleTtl","ttl":"ttl"},"peripheralsConfig":{"sparkHistoryServerConfig":{"dataprocCluster":"dataprocCluster"},"metastoreService":"metastoreService"}},"uuid":"uuid","labels":{"key":"labels"}}
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
        method='PATCH',
        path='/v1/{name}'.format(name='name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dataproc_projects_locations_sessions_create(client):
    """Test case for dataproc_projects_locations_sessions_create

    
    """
    body = {"creator":"creator","stateMessage":"stateMessage","sessionTemplate":"sessionTemplate","uuid":"uuid","labels":{"key":"labels"},"stateHistory":[{"stateMessage":"stateMessage","state":"STATE_UNSPECIFIED","stateStartTime":"stateStartTime"},{"stateMessage":"stateMessage","state":"STATE_UNSPECIFIED","stateStartTime":"stateStartTime"}],"createTime":"createTime","stateTime":"stateTime","jupyterSession":{"displayName":"displayName","kernel":"KERNEL_UNSPECIFIED"},"name":"name","runtimeConfig":{"repositoryConfig":{"pypiRepositoryConfig":{"pypiRepository":"pypiRepository"}},"containerImage":"containerImage","version":"version","properties":{"key":"properties"}},"environmentConfig":{"executionConfig":{"networkUri":"networkUri","networkTags":["networkTags","networkTags"],"kmsKey":"kmsKey","stagingBucket":"stagingBucket","subnetworkUri":"subnetworkUri","serviceAccount":"serviceAccount","idleTtl":"idleTtl","ttl":"ttl"},"peripheralsConfig":{"sparkHistoryServerConfig":{"dataprocCluster":"dataprocCluster"},"metastoreService":"metastoreService"}},"state":"STATE_UNSPECIFIED","user":"user","runtimeInfo":{"endpoints":{"key":"endpoints"},"outputUri":"outputUri","diagnosticOutputUri":"diagnosticOutputUri","currentUsage":{"acceleratorType":"acceleratorType","milliDcu":"milliDcu","milliDcuPremium":"milliDcuPremium","shuffleStorageGb":"shuffleStorageGb","snapshotTime":"snapshotTime","milliAccelerator":"milliAccelerator","shuffleStorageGbPremium":"shuffleStorageGbPremium"},"approximateUsage":{"acceleratorType":"acceleratorType","milliAcceleratorSeconds":"milliAcceleratorSeconds","milliDcuSeconds":"milliDcuSeconds","shuffleStorageGbSeconds":"shuffleStorageGbSeconds"}}}
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
                    ('requestId', 'request_id_example'),
                    ('sessionId', 'session_id_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/{parent}/sessions'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dataproc_projects_locations_sessions_list(client):
    """Test case for dataproc_projects_locations_sessions_list

    
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
        path='/v1/{parent}/sessions'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dataproc_projects_locations_sessions_terminate(client):
    """Test case for dataproc_projects_locations_sessions_terminate

    
    """
    body = {"requestId":"requestId"}
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
        path='/v1/{nameterminat}'.format(name='name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dataproc_projects_regions_autoscaling_policies_create(client):
    """Test case for dataproc_projects_regions_autoscaling_policies_create

    
    """
    body = {"basicAlgorithm":{"sparkStandaloneConfig":{"scaleDownMinWorkerFraction":6.027456183070403,"scaleUpMinWorkerFraction":5.962133916683182,"gracefulDecommissionTimeout":"gracefulDecommissionTimeout","removeOnlyIdleWorkers":True,"scaleDownFactor":0.8008281904610115,"scaleUpFactor":1.4658129805029452},"cooldownPeriod":"cooldownPeriod","yarnConfig":{"scaleDownMinWorkerFraction":2.3021358869347655,"scaleUpMinWorkerFraction":9.301444243932576,"gracefulDecommissionTimeout":"gracefulDecommissionTimeout","scaleDownFactor":5.637376656633329,"scaleUpFactor":7.061401241503109}},"name":"name","id":"id","workerConfig":{"minInstances":2,"weight":4,"maxInstances":3},"secondaryWorkerConfig":{"minInstances":2,"weight":4,"maxInstances":3},"labels":{"key":"labels"}}
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
        path='/v1/{parent}/autoscalingPolicies'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dataproc_projects_regions_autoscaling_policies_list(client):
    """Test case for dataproc_projects_regions_autoscaling_policies_list

    
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
                    ('pageToken', 'page_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/{parent}/autoscalingPolicies'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dataproc_projects_regions_clusters_create(client):
    """Test case for dataproc_projects_regions_clusters_create

    
    """
    body = {"clusterUuid":"clusterUuid","statusHistory":[{"substate":"UNSPECIFIED","detail":"detail","state":"UNKNOWN","stateStartTime":"stateStartTime"},{"substate":"UNSPECIFIED","detail":"detail","state":"UNKNOWN","stateStartTime":"stateStartTime"}],"clusterName":"clusterName","metrics":{"yarnMetrics":{"key":"yarnMetrics"},"hdfsMetrics":{"key":"hdfsMetrics"}},"config":{"encryptionConfig":{"kmsKey":"kmsKey","gcePdKmsKeyName":"gcePdKmsKeyName"},"softwareConfig":{"imageVersion":"imageVersion","optionalComponents":["COMPONENT_UNSPECIFIED","COMPONENT_UNSPECIFIED"],"properties":{"key":"properties"}},"lifecycleConfig":{"autoDeleteTime":"autoDeleteTime","idleStartTime":"idleStartTime","idleDeleteTtl":"idleDeleteTtl","autoDeleteTtl":"autoDeleteTtl"},"configBucket":"configBucket","masterConfig":{"instanceFlexibilityPolicy":{"instanceSelectionResults":[{"vmCount":5,"machineType":"machineType"},{"vmCount":5,"machineType":"machineType"}],"instanceSelectionList":[{"rank":5,"machineTypes":["machineTypes","machineTypes"]},{"rank":5,"machineTypes":["machineTypes","machineTypes"]}]},"minNumInstances":2,"machineTypeUri":"machineTypeUri","isPreemptible":True,"preemptibility":"PREEMPTIBILITY_UNSPECIFIED","managedGroupConfig":{"instanceGroupManagerUri":"instanceGroupManagerUri","instanceGroupManagerName":"instanceGroupManagerName","instanceTemplateName":"instanceTemplateName"},"imageUri":"imageUri","instanceNames":["instanceNames","instanceNames"],"instanceReferences":[{"instanceId":"instanceId","instanceName":"instanceName","publicEciesKey":"publicEciesKey","publicKey":"publicKey"},{"instanceId":"instanceId","instanceName":"instanceName","publicEciesKey":"publicEciesKey","publicKey":"publicKey"}],"minCpuPlatform":"minCpuPlatform","numInstances":7,"diskConfig":{"bootDiskType":"bootDiskType","bootDiskSizeGb":6,"localSsdInterface":"localSsdInterface","numLocalSsds":1},"accelerators":[{"acceleratorTypeUri":"acceleratorTypeUri","acceleratorCount":0},{"acceleratorTypeUri":"acceleratorTypeUri","acceleratorCount":0}],"startupConfig":{"requiredRegistrationFraction":9.301444243932576}},"workerConfig":{"instanceFlexibilityPolicy":{"instanceSelectionResults":[{"vmCount":5,"machineType":"machineType"},{"vmCount":5,"machineType":"machineType"}],"instanceSelectionList":[{"rank":5,"machineTypes":["machineTypes","machineTypes"]},{"rank":5,"machineTypes":["machineTypes","machineTypes"]}]},"minNumInstances":2,"machineTypeUri":"machineTypeUri","isPreemptible":True,"preemptibility":"PREEMPTIBILITY_UNSPECIFIED","managedGroupConfig":{"instanceGroupManagerUri":"instanceGroupManagerUri","instanceGroupManagerName":"instanceGroupManagerName","instanceTemplateName":"instanceTemplateName"},"imageUri":"imageUri","instanceNames":["instanceNames","instanceNames"],"instanceReferences":[{"instanceId":"instanceId","instanceName":"instanceName","publicEciesKey":"publicEciesKey","publicKey":"publicKey"},{"instanceId":"instanceId","instanceName":"instanceName","publicEciesKey":"publicEciesKey","publicKey":"publicKey"}],"minCpuPlatform":"minCpuPlatform","numInstances":7,"diskConfig":{"bootDiskType":"bootDiskType","bootDiskSizeGb":6,"localSsdInterface":"localSsdInterface","numLocalSsds":1},"accelerators":[{"acceleratorTypeUri":"acceleratorTypeUri","acceleratorCount":0},{"acceleratorTypeUri":"acceleratorTypeUri","acceleratorCount":0}],"startupConfig":{"requiredRegistrationFraction":9.301444243932576}},"secondaryWorkerConfig":{"instanceFlexibilityPolicy":{"instanceSelectionResults":[{"vmCount":5,"machineType":"machineType"},{"vmCount":5,"machineType":"machineType"}],"instanceSelectionList":[{"rank":5,"machineTypes":["machineTypes","machineTypes"]},{"rank":5,"machineTypes":["machineTypes","machineTypes"]}]},"minNumInstances":2,"machineTypeUri":"machineTypeUri","isPreemptible":True,"preemptibility":"PREEMPTIBILITY_UNSPECIFIED","managedGroupConfig":{"instanceGroupManagerUri":"instanceGroupManagerUri","instanceGroupManagerName":"instanceGroupManagerName","instanceTemplateName":"instanceTemplateName"},"imageUri":"imageUri","instanceNames":["instanceNames","instanceNames"],"instanceReferences":[{"instanceId":"instanceId","instanceName":"instanceName","publicEciesKey":"publicEciesKey","publicKey":"publicKey"},{"instanceId":"instanceId","instanceName":"instanceName","publicEciesKey":"publicEciesKey","publicKey":"publicKey"}],"minCpuPlatform":"minCpuPlatform","numInstances":7,"diskConfig":{"bootDiskType":"bootDiskType","bootDiskSizeGb":6,"localSsdInterface":"localSsdInterface","numLocalSsds":1},"accelerators":[{"acceleratorTypeUri":"acceleratorTypeUri","acceleratorCount":0},{"acceleratorTypeUri":"acceleratorTypeUri","acceleratorCount":0}],"startupConfig":{"requiredRegistrationFraction":9.301444243932576}},"gkeClusterConfig":{"gkeClusterTarget":"gkeClusterTarget","namespacedGkeDeploymentTarget":{"clusterNamespace":"clusterNamespace","targetGkeCluster":"targetGkeCluster"},"nodePoolTarget":[{"nodePool":"nodePool","nodePoolConfig":{"locations":["locations","locations"],"autoscaling":{"minNodeCount":2,"maxNodeCount":3},"config":{"preemptible":True,"minCpuPlatform":"minCpuPlatform","spot":True,"bootDiskKmsKey":"bootDiskKmsKey","accelerators":[{"acceleratorType":"acceleratorType","acceleratorCount":"acceleratorCount","gpuPartitionSize":"gpuPartitionSize"},{"acceleratorType":"acceleratorType","acceleratorCount":"acceleratorCount","gpuPartitionSize":"gpuPartitionSize"}],"localSsdCount":4,"machineType":"machineType"}},"roles":["ROLE_UNSPECIFIED","ROLE_UNSPECIFIED"]},{"nodePool":"nodePool","nodePoolConfig":{"locations":["locations","locations"],"autoscaling":{"minNodeCount":2,"maxNodeCount":3},"config":{"preemptible":True,"minCpuPlatform":"minCpuPlatform","spot":True,"bootDiskKmsKey":"bootDiskKmsKey","accelerators":[{"acceleratorType":"acceleratorType","acceleratorCount":"acceleratorCount","gpuPartitionSize":"gpuPartitionSize"},{"acceleratorType":"acceleratorType","acceleratorCount":"acceleratorCount","gpuPartitionSize":"gpuPartitionSize"}],"localSsdCount":4,"machineType":"machineType"}},"roles":["ROLE_UNSPECIFIED","ROLE_UNSPECIFIED"]}]},"securityConfig":{"identityConfig":{"userServiceAccountMapping":{"key":"userServiceAccountMapping"}},"kerberosConfig":{"tgtLifetimeHours":7,"keyPasswordUri":"keyPasswordUri","rootPrincipalPasswordUri":"rootPrincipalPasswordUri","kdcDbKeyUri":"kdcDbKeyUri","crossRealmTrustSharedPasswordUri":"crossRealmTrustSharedPasswordUri","keystoreUri":"keystoreUri","truststorePasswordUri":"truststorePasswordUri","crossRealmTrustKdc":"crossRealmTrustKdc","enableKerberos":True,"crossRealmTrustAdminServer":"crossRealmTrustAdminServer","kmsKeyUri":"kmsKeyUri","truststoreUri":"truststoreUri","realm":"realm","crossRealmTrustRealm":"crossRealmTrustRealm","keystorePasswordUri":"keystorePasswordUri"}},"autoscalingConfig":{"policyUri":"policyUri"},"metastoreConfig":{"dataprocMetastoreService":"dataprocMetastoreService"},"endpointConfig":{"httpPorts":{"key":"httpPorts"},"enableHttpPortAccess":True},"auxiliaryNodeGroups":[{"nodeGroupId":"nodeGroupId","nodeGroup":{"nodeGroupConfig":{"instanceFlexibilityPolicy":{"instanceSelectionResults":[{"vmCount":5,"machineType":"machineType"},{"vmCount":5,"machineType":"machineType"}],"instanceSelectionList":[{"rank":5,"machineTypes":["machineTypes","machineTypes"]},{"rank":5,"machineTypes":["machineTypes","machineTypes"]}]},"minNumInstances":2,"machineTypeUri":"machineTypeUri","isPreemptible":True,"preemptibility":"PREEMPTIBILITY_UNSPECIFIED","managedGroupConfig":{"instanceGroupManagerUri":"instanceGroupManagerUri","instanceGroupManagerName":"instanceGroupManagerName","instanceTemplateName":"instanceTemplateName"},"imageUri":"imageUri","instanceNames":["instanceNames","instanceNames"],"instanceReferences":[{"instanceId":"instanceId","instanceName":"instanceName","publicEciesKey":"publicEciesKey","publicKey":"publicKey"},{"instanceId":"instanceId","instanceName":"instanceName","publicEciesKey":"publicEciesKey","publicKey":"publicKey"}],"minCpuPlatform":"minCpuPlatform","numInstances":7,"diskConfig":{"bootDiskType":"bootDiskType","bootDiskSizeGb":6,"localSsdInterface":"localSsdInterface","numLocalSsds":1},"accelerators":[{"acceleratorTypeUri":"acceleratorTypeUri","acceleratorCount":0},{"acceleratorTypeUri":"acceleratorTypeUri","acceleratorCount":0}],"startupConfig":{"requiredRegistrationFraction":9.301444243932576}},"roles":["ROLE_UNSPECIFIED","ROLE_UNSPECIFIED"],"name":"name","labels":{"key":"labels"}}},{"nodeGroupId":"nodeGroupId","nodeGroup":{"nodeGroupConfig":{"instanceFlexibilityPolicy":{"instanceSelectionResults":[{"vmCount":5,"machineType":"machineType"},{"vmCount":5,"machineType":"machineType"}],"instanceSelectionList":[{"rank":5,"machineTypes":["machineTypes","machineTypes"]},{"rank":5,"machineTypes":["machineTypes","machineTypes"]}]},"minNumInstances":2,"machineTypeUri":"machineTypeUri","isPreemptible":True,"preemptibility":"PREEMPTIBILITY_UNSPECIFIED","managedGroupConfig":{"instanceGroupManagerUri":"instanceGroupManagerUri","instanceGroupManagerName":"instanceGroupManagerName","instanceTemplateName":"instanceTemplateName"},"imageUri":"imageUri","instanceNames":["instanceNames","instanceNames"],"instanceReferences":[{"instanceId":"instanceId","instanceName":"instanceName","publicEciesKey":"publicEciesKey","publicKey":"publicKey"},{"instanceId":"instanceId","instanceName":"instanceName","publicEciesKey":"publicEciesKey","publicKey":"publicKey"}],"minCpuPlatform":"minCpuPlatform","numInstances":7,"diskConfig":{"bootDiskType":"bootDiskType","bootDiskSizeGb":6,"localSsdInterface":"localSsdInterface","numLocalSsds":1},"accelerators":[{"acceleratorTypeUri":"acceleratorTypeUri","acceleratorCount":0},{"acceleratorTypeUri":"acceleratorTypeUri","acceleratorCount":0}],"startupConfig":{"requiredRegistrationFraction":9.301444243932576}},"roles":["ROLE_UNSPECIFIED","ROLE_UNSPECIFIED"],"name":"name","labels":{"key":"labels"}}}],"initializationActions":[{"executableFile":"executableFile","executionTimeout":"executionTimeout"},{"executableFile":"executableFile","executionTimeout":"executionTimeout"}],"gceClusterConfig":{"networkUri":"networkUri","metadata":{"key":"metadata"},"nodeGroupAffinity":{"nodeGroupUri":"nodeGroupUri"},"shieldedInstanceConfig":{"enableVtpm":True,"enableIntegrityMonitoring":True,"enableSecureBoot":True},"reservationAffinity":{"consumeReservationType":"TYPE_UNSPECIFIED","values":["values","values"],"key":"key"},"subnetworkUri":"subnetworkUri","serviceAccount":"serviceAccount","confidentialInstanceConfig":{"enableConfidentialCompute":True},"privateIpv6GoogleAccess":"PRIVATE_IPV6_GOOGLE_ACCESS_UNSPECIFIED","tags":["tags","tags"],"serviceAccountScopes":["serviceAccountScopes","serviceAccountScopes"],"internalIpOnly":True,"zoneUri":"zoneUri"},"tempBucket":"tempBucket","dataprocMetricConfig":{"metrics":[{"metricSource":"METRIC_SOURCE_UNSPECIFIED","metricOverrides":["metricOverrides","metricOverrides"]},{"metricSource":"METRIC_SOURCE_UNSPECIFIED","metricOverrides":["metricOverrides","metricOverrides"]}]}},"projectId":"projectId","virtualClusterConfig":{"kubernetesClusterConfig":{"gkeClusterConfig":{"gkeClusterTarget":"gkeClusterTarget","namespacedGkeDeploymentTarget":{"clusterNamespace":"clusterNamespace","targetGkeCluster":"targetGkeCluster"},"nodePoolTarget":[{"nodePool":"nodePool","nodePoolConfig":{"locations":["locations","locations"],"autoscaling":{"minNodeCount":2,"maxNodeCount":3},"config":{"preemptible":True,"minCpuPlatform":"minCpuPlatform","spot":True,"bootDiskKmsKey":"bootDiskKmsKey","accelerators":[{"acceleratorType":"acceleratorType","acceleratorCount":"acceleratorCount","gpuPartitionSize":"gpuPartitionSize"},{"acceleratorType":"acceleratorType","acceleratorCount":"acceleratorCount","gpuPartitionSize":"gpuPartitionSize"}],"localSsdCount":4,"machineType":"machineType"}},"roles":["ROLE_UNSPECIFIED","ROLE_UNSPECIFIED"]},{"nodePool":"nodePool","nodePoolConfig":{"locations":["locations","locations"],"autoscaling":{"minNodeCount":2,"maxNodeCount":3},"config":{"preemptible":True,"minCpuPlatform":"minCpuPlatform","spot":True,"bootDiskKmsKey":"bootDiskKmsKey","accelerators":[{"acceleratorType":"acceleratorType","acceleratorCount":"acceleratorCount","gpuPartitionSize":"gpuPartitionSize"},{"acceleratorType":"acceleratorType","acceleratorCount":"acceleratorCount","gpuPartitionSize":"gpuPartitionSize"}],"localSsdCount":4,"machineType":"machineType"}},"roles":["ROLE_UNSPECIFIED","ROLE_UNSPECIFIED"]}]},"kubernetesNamespace":"kubernetesNamespace","kubernetesSoftwareConfig":{"componentVersion":{"key":"componentVersion"},"properties":{"key":"properties"}}},"stagingBucket":"stagingBucket","auxiliaryServicesConfig":{"metastoreConfig":{"dataprocMetastoreService":"dataprocMetastoreService"},"sparkHistoryServerConfig":{"dataprocCluster":"dataprocCluster"}}},"labels":{"key":"labels"},"status":{"substate":"UNSPECIFIED","detail":"detail","state":"UNKNOWN","stateStartTime":"stateStartTime"}}
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
                    ('actionOnFailedPrimaryWorkers', 'action_on_failed_primary_workers_example'),
                    ('requestId', 'request_id_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/projects/{project_id}/regions/{region}/clusters'.format(project_id='project_id_example', region='region_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dataproc_projects_regions_clusters_delete(client):
    """Test case for dataproc_projects_regions_clusters_delete

    
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
                    ('clusterUuid', 'cluster_uuid_example'),
                    ('gracefulTerminationTimeout', 'graceful_termination_timeout_example'),
                    ('requestId', 'request_id_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/v1/projects/{project_id}/regions/{region}/clusters/{cluster_name}'.format(project_id='project_id_example', region='region_example', cluster_name='cluster_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dataproc_projects_regions_clusters_diagnose(client):
    """Test case for dataproc_projects_regions_clusters_diagnose

    
    """
    body = {"diagnosisInterval":{"startTime":"startTime","endTime":"endTime"},"tarballAccess":"TARBALL_ACCESS_UNSPECIFIED","jobs":["jobs","jobs"],"yarnApplicationIds":["yarnApplicationIds","yarnApplicationIds"],"tarballGcsDir":"tarballGcsDir","job":"job","yarnApplicationId":"yarnApplicationId"}
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
        path='/v1/projects/{project_id}/regions/{region}/clusters/{cluster_namediagnos}'.format(project_id='project_id_example', region='region_example', cluster_name='cluster_name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dataproc_projects_regions_clusters_get(client):
    """Test case for dataproc_projects_regions_clusters_get

    
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
        path='/v1/projects/{project_id}/regions/{region}/clusters/{cluster_name}'.format(project_id='project_id_example', region='region_example', cluster_name='cluster_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dataproc_projects_regions_clusters_inject_credentials(client):
    """Test case for dataproc_projects_regions_clusters_inject_credentials

    
    """
    body = {"clusterUuid":"clusterUuid","credentialsCiphertext":"credentialsCiphertext"}
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
        path='/v1/{project}/{region}/{clusterinject_credential}'.format(project='project_example', region='region_example', cluster='cluster_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dataproc_projects_regions_clusters_list(client):
    """Test case for dataproc_projects_regions_clusters_list

    
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
        path='/v1/projects/{project_id}/regions/{region}/clusters'.format(project_id='project_id_example', region='region_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dataproc_projects_regions_clusters_node_groups_create(client):
    """Test case for dataproc_projects_regions_clusters_node_groups_create

    
    """
    body = {"nodeGroupConfig":{"instanceFlexibilityPolicy":{"instanceSelectionResults":[{"vmCount":5,"machineType":"machineType"},{"vmCount":5,"machineType":"machineType"}],"instanceSelectionList":[{"rank":5,"machineTypes":["machineTypes","machineTypes"]},{"rank":5,"machineTypes":["machineTypes","machineTypes"]}]},"minNumInstances":2,"machineTypeUri":"machineTypeUri","isPreemptible":True,"preemptibility":"PREEMPTIBILITY_UNSPECIFIED","managedGroupConfig":{"instanceGroupManagerUri":"instanceGroupManagerUri","instanceGroupManagerName":"instanceGroupManagerName","instanceTemplateName":"instanceTemplateName"},"imageUri":"imageUri","instanceNames":["instanceNames","instanceNames"],"instanceReferences":[{"instanceId":"instanceId","instanceName":"instanceName","publicEciesKey":"publicEciesKey","publicKey":"publicKey"},{"instanceId":"instanceId","instanceName":"instanceName","publicEciesKey":"publicEciesKey","publicKey":"publicKey"}],"minCpuPlatform":"minCpuPlatform","numInstances":7,"diskConfig":{"bootDiskType":"bootDiskType","bootDiskSizeGb":6,"localSsdInterface":"localSsdInterface","numLocalSsds":1},"accelerators":[{"acceleratorTypeUri":"acceleratorTypeUri","acceleratorCount":0},{"acceleratorTypeUri":"acceleratorTypeUri","acceleratorCount":0}],"startupConfig":{"requiredRegistrationFraction":9.301444243932576}},"roles":["ROLE_UNSPECIFIED","ROLE_UNSPECIFIED"],"name":"name","labels":{"key":"labels"}}
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
                    ('nodeGroupId', 'node_group_id_example'),
                    ('parentOperationId', 'parent_operation_id_example'),
                    ('requestId', 'request_id_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/{parent}/nodeGroups'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dataproc_projects_regions_clusters_node_groups_repair(client):
    """Test case for dataproc_projects_regions_clusters_node_groups_repair

    
    """
    body = {"instanceNames":["instanceNames","instanceNames"],"requestId":"requestId","repairAction":"REPAIR_ACTION_UNSPECIFIED"}
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
        path='/v1/{namerepai}'.format(name='name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dataproc_projects_regions_clusters_node_groups_resize(client):
    """Test case for dataproc_projects_regions_clusters_node_groups_resize

    
    """
    body = {"parentOperationId":"parentOperationId","size":0,"requestId":"requestId","gracefulDecommissionTimeout":"gracefulDecommissionTimeout"}
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
        path='/v1/{nameresiz}'.format(name='name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dataproc_projects_regions_clusters_patch(client):
    """Test case for dataproc_projects_regions_clusters_patch

    
    """
    body = {"clusterUuid":"clusterUuid","statusHistory":[{"substate":"UNSPECIFIED","detail":"detail","state":"UNKNOWN","stateStartTime":"stateStartTime"},{"substate":"UNSPECIFIED","detail":"detail","state":"UNKNOWN","stateStartTime":"stateStartTime"}],"clusterName":"clusterName","metrics":{"yarnMetrics":{"key":"yarnMetrics"},"hdfsMetrics":{"key":"hdfsMetrics"}},"config":{"encryptionConfig":{"kmsKey":"kmsKey","gcePdKmsKeyName":"gcePdKmsKeyName"},"softwareConfig":{"imageVersion":"imageVersion","optionalComponents":["COMPONENT_UNSPECIFIED","COMPONENT_UNSPECIFIED"],"properties":{"key":"properties"}},"lifecycleConfig":{"autoDeleteTime":"autoDeleteTime","idleStartTime":"idleStartTime","idleDeleteTtl":"idleDeleteTtl","autoDeleteTtl":"autoDeleteTtl"},"configBucket":"configBucket","masterConfig":{"instanceFlexibilityPolicy":{"instanceSelectionResults":[{"vmCount":5,"machineType":"machineType"},{"vmCount":5,"machineType":"machineType"}],"instanceSelectionList":[{"rank":5,"machineTypes":["machineTypes","machineTypes"]},{"rank":5,"machineTypes":["machineTypes","machineTypes"]}]},"minNumInstances":2,"machineTypeUri":"machineTypeUri","isPreemptible":True,"preemptibility":"PREEMPTIBILITY_UNSPECIFIED","managedGroupConfig":{"instanceGroupManagerUri":"instanceGroupManagerUri","instanceGroupManagerName":"instanceGroupManagerName","instanceTemplateName":"instanceTemplateName"},"imageUri":"imageUri","instanceNames":["instanceNames","instanceNames"],"instanceReferences":[{"instanceId":"instanceId","instanceName":"instanceName","publicEciesKey":"publicEciesKey","publicKey":"publicKey"},{"instanceId":"instanceId","instanceName":"instanceName","publicEciesKey":"publicEciesKey","publicKey":"publicKey"}],"minCpuPlatform":"minCpuPlatform","numInstances":7,"diskConfig":{"bootDiskType":"bootDiskType","bootDiskSizeGb":6,"localSsdInterface":"localSsdInterface","numLocalSsds":1},"accelerators":[{"acceleratorTypeUri":"acceleratorTypeUri","acceleratorCount":0},{"acceleratorTypeUri":"acceleratorTypeUri","acceleratorCount":0}],"startupConfig":{"requiredRegistrationFraction":9.301444243932576}},"workerConfig":{"instanceFlexibilityPolicy":{"instanceSelectionResults":[{"vmCount":5,"machineType":"machineType"},{"vmCount":5,"machineType":"machineType"}],"instanceSelectionList":[{"rank":5,"machineTypes":["machineTypes","machineTypes"]},{"rank":5,"machineTypes":["machineTypes","machineTypes"]}]},"minNumInstances":2,"machineTypeUri":"machineTypeUri","isPreemptible":True,"preemptibility":"PREEMPTIBILITY_UNSPECIFIED","managedGroupConfig":{"instanceGroupManagerUri":"instanceGroupManagerUri","instanceGroupManagerName":"instanceGroupManagerName","instanceTemplateName":"instanceTemplateName"},"imageUri":"imageUri","instanceNames":["instanceNames","instanceNames"],"instanceReferences":[{"instanceId":"instanceId","instanceName":"instanceName","publicEciesKey":"publicEciesKey","publicKey":"publicKey"},{"instanceId":"instanceId","instanceName":"instanceName","publicEciesKey":"publicEciesKey","publicKey":"publicKey"}],"minCpuPlatform":"minCpuPlatform","numInstances":7,"diskConfig":{"bootDiskType":"bootDiskType","bootDiskSizeGb":6,"localSsdInterface":"localSsdInterface","numLocalSsds":1},"accelerators":[{"acceleratorTypeUri":"acceleratorTypeUri","acceleratorCount":0},{"acceleratorTypeUri":"acceleratorTypeUri","acceleratorCount":0}],"startupConfig":{"requiredRegistrationFraction":9.301444243932576}},"secondaryWorkerConfig":{"instanceFlexibilityPolicy":{"instanceSelectionResults":[{"vmCount":5,"machineType":"machineType"},{"vmCount":5,"machineType":"machineType"}],"instanceSelectionList":[{"rank":5,"machineTypes":["machineTypes","machineTypes"]},{"rank":5,"machineTypes":["machineTypes","machineTypes"]}]},"minNumInstances":2,"machineTypeUri":"machineTypeUri","isPreemptible":True,"preemptibility":"PREEMPTIBILITY_UNSPECIFIED","managedGroupConfig":{"instanceGroupManagerUri":"instanceGroupManagerUri","instanceGroupManagerName":"instanceGroupManagerName","instanceTemplateName":"instanceTemplateName"},"imageUri":"imageUri","instanceNames":["instanceNames","instanceNames"],"instanceReferences":[{"instanceId":"instanceId","instanceName":"instanceName","publicEciesKey":"publicEciesKey","publicKey":"publicKey"},{"instanceId":"instanceId","instanceName":"instanceName","publicEciesKey":"publicEciesKey","publicKey":"publicKey"}],"minCpuPlatform":"minCpuPlatform","numInstances":7,"diskConfig":{"bootDiskType":"bootDiskType","bootDiskSizeGb":6,"localSsdInterface":"localSsdInterface","numLocalSsds":1},"accelerators":[{"acceleratorTypeUri":"acceleratorTypeUri","acceleratorCount":0},{"acceleratorTypeUri":"acceleratorTypeUri","acceleratorCount":0}],"startupConfig":{"requiredRegistrationFraction":9.301444243932576}},"gkeClusterConfig":{"gkeClusterTarget":"gkeClusterTarget","namespacedGkeDeploymentTarget":{"clusterNamespace":"clusterNamespace","targetGkeCluster":"targetGkeCluster"},"nodePoolTarget":[{"nodePool":"nodePool","nodePoolConfig":{"locations":["locations","locations"],"autoscaling":{"minNodeCount":2,"maxNodeCount":3},"config":{"preemptible":True,"minCpuPlatform":"minCpuPlatform","spot":True,"bootDiskKmsKey":"bootDiskKmsKey","accelerators":[{"acceleratorType":"acceleratorType","acceleratorCount":"acceleratorCount","gpuPartitionSize":"gpuPartitionSize"},{"acceleratorType":"acceleratorType","acceleratorCount":"acceleratorCount","gpuPartitionSize":"gpuPartitionSize"}],"localSsdCount":4,"machineType":"machineType"}},"roles":["ROLE_UNSPECIFIED","ROLE_UNSPECIFIED"]},{"nodePool":"nodePool","nodePoolConfig":{"locations":["locations","locations"],"autoscaling":{"minNodeCount":2,"maxNodeCount":3},"config":{"preemptible":True,"minCpuPlatform":"minCpuPlatform","spot":True,"bootDiskKmsKey":"bootDiskKmsKey","accelerators":[{"acceleratorType":"acceleratorType","acceleratorCount":"acceleratorCount","gpuPartitionSize":"gpuPartitionSize"},{"acceleratorType":"acceleratorType","acceleratorCount":"acceleratorCount","gpuPartitionSize":"gpuPartitionSize"}],"localSsdCount":4,"machineType":"machineType"}},"roles":["ROLE_UNSPECIFIED","ROLE_UNSPECIFIED"]}]},"securityConfig":{"identityConfig":{"userServiceAccountMapping":{"key":"userServiceAccountMapping"}},"kerberosConfig":{"tgtLifetimeHours":7,"keyPasswordUri":"keyPasswordUri","rootPrincipalPasswordUri":"rootPrincipalPasswordUri","kdcDbKeyUri":"kdcDbKeyUri","crossRealmTrustSharedPasswordUri":"crossRealmTrustSharedPasswordUri","keystoreUri":"keystoreUri","truststorePasswordUri":"truststorePasswordUri","crossRealmTrustKdc":"crossRealmTrustKdc","enableKerberos":True,"crossRealmTrustAdminServer":"crossRealmTrustAdminServer","kmsKeyUri":"kmsKeyUri","truststoreUri":"truststoreUri","realm":"realm","crossRealmTrustRealm":"crossRealmTrustRealm","keystorePasswordUri":"keystorePasswordUri"}},"autoscalingConfig":{"policyUri":"policyUri"},"metastoreConfig":{"dataprocMetastoreService":"dataprocMetastoreService"},"endpointConfig":{"httpPorts":{"key":"httpPorts"},"enableHttpPortAccess":True},"auxiliaryNodeGroups":[{"nodeGroupId":"nodeGroupId","nodeGroup":{"nodeGroupConfig":{"instanceFlexibilityPolicy":{"instanceSelectionResults":[{"vmCount":5,"machineType":"machineType"},{"vmCount":5,"machineType":"machineType"}],"instanceSelectionList":[{"rank":5,"machineTypes":["machineTypes","machineTypes"]},{"rank":5,"machineTypes":["machineTypes","machineTypes"]}]},"minNumInstances":2,"machineTypeUri":"machineTypeUri","isPreemptible":True,"preemptibility":"PREEMPTIBILITY_UNSPECIFIED","managedGroupConfig":{"instanceGroupManagerUri":"instanceGroupManagerUri","instanceGroupManagerName":"instanceGroupManagerName","instanceTemplateName":"instanceTemplateName"},"imageUri":"imageUri","instanceNames":["instanceNames","instanceNames"],"instanceReferences":[{"instanceId":"instanceId","instanceName":"instanceName","publicEciesKey":"publicEciesKey","publicKey":"publicKey"},{"instanceId":"instanceId","instanceName":"instanceName","publicEciesKey":"publicEciesKey","publicKey":"publicKey"}],"minCpuPlatform":"minCpuPlatform","numInstances":7,"diskConfig":{"bootDiskType":"bootDiskType","bootDiskSizeGb":6,"localSsdInterface":"localSsdInterface","numLocalSsds":1},"accelerators":[{"acceleratorTypeUri":"acceleratorTypeUri","acceleratorCount":0},{"acceleratorTypeUri":"acceleratorTypeUri","acceleratorCount":0}],"startupConfig":{"requiredRegistrationFraction":9.301444243932576}},"roles":["ROLE_UNSPECIFIED","ROLE_UNSPECIFIED"],"name":"name","labels":{"key":"labels"}}},{"nodeGroupId":"nodeGroupId","nodeGroup":{"nodeGroupConfig":{"instanceFlexibilityPolicy":{"instanceSelectionResults":[{"vmCount":5,"machineType":"machineType"},{"vmCount":5,"machineType":"machineType"}],"instanceSelectionList":[{"rank":5,"machineTypes":["machineTypes","machineTypes"]},{"rank":5,"machineTypes":["machineTypes","machineTypes"]}]},"minNumInstances":2,"machineTypeUri":"machineTypeUri","isPreemptible":True,"preemptibility":"PREEMPTIBILITY_UNSPECIFIED","managedGroupConfig":{"instanceGroupManagerUri":"instanceGroupManagerUri","instanceGroupManagerName":"instanceGroupManagerName","instanceTemplateName":"instanceTemplateName"},"imageUri":"imageUri","instanceNames":["instanceNames","instanceNames"],"instanceReferences":[{"instanceId":"instanceId","instanceName":"instanceName","publicEciesKey":"publicEciesKey","publicKey":"publicKey"},{"instanceId":"instanceId","instanceName":"instanceName","publicEciesKey":"publicEciesKey","publicKey":"publicKey"}],"minCpuPlatform":"minCpuPlatform","numInstances":7,"diskConfig":{"bootDiskType":"bootDiskType","bootDiskSizeGb":6,"localSsdInterface":"localSsdInterface","numLocalSsds":1},"accelerators":[{"acceleratorTypeUri":"acceleratorTypeUri","acceleratorCount":0},{"acceleratorTypeUri":"acceleratorTypeUri","acceleratorCount":0}],"startupConfig":{"requiredRegistrationFraction":9.301444243932576}},"roles":["ROLE_UNSPECIFIED","ROLE_UNSPECIFIED"],"name":"name","labels":{"key":"labels"}}}],"initializationActions":[{"executableFile":"executableFile","executionTimeout":"executionTimeout"},{"executableFile":"executableFile","executionTimeout":"executionTimeout"}],"gceClusterConfig":{"networkUri":"networkUri","metadata":{"key":"metadata"},"nodeGroupAffinity":{"nodeGroupUri":"nodeGroupUri"},"shieldedInstanceConfig":{"enableVtpm":True,"enableIntegrityMonitoring":True,"enableSecureBoot":True},"reservationAffinity":{"consumeReservationType":"TYPE_UNSPECIFIED","values":["values","values"],"key":"key"},"subnetworkUri":"subnetworkUri","serviceAccount":"serviceAccount","confidentialInstanceConfig":{"enableConfidentialCompute":True},"privateIpv6GoogleAccess":"PRIVATE_IPV6_GOOGLE_ACCESS_UNSPECIFIED","tags":["tags","tags"],"serviceAccountScopes":["serviceAccountScopes","serviceAccountScopes"],"internalIpOnly":True,"zoneUri":"zoneUri"},"tempBucket":"tempBucket","dataprocMetricConfig":{"metrics":[{"metricSource":"METRIC_SOURCE_UNSPECIFIED","metricOverrides":["metricOverrides","metricOverrides"]},{"metricSource":"METRIC_SOURCE_UNSPECIFIED","metricOverrides":["metricOverrides","metricOverrides"]}]}},"projectId":"projectId","virtualClusterConfig":{"kubernetesClusterConfig":{"gkeClusterConfig":{"gkeClusterTarget":"gkeClusterTarget","namespacedGkeDeploymentTarget":{"clusterNamespace":"clusterNamespace","targetGkeCluster":"targetGkeCluster"},"nodePoolTarget":[{"nodePool":"nodePool","nodePoolConfig":{"locations":["locations","locations"],"autoscaling":{"minNodeCount":2,"maxNodeCount":3},"config":{"preemptible":True,"minCpuPlatform":"minCpuPlatform","spot":True,"bootDiskKmsKey":"bootDiskKmsKey","accelerators":[{"acceleratorType":"acceleratorType","acceleratorCount":"acceleratorCount","gpuPartitionSize":"gpuPartitionSize"},{"acceleratorType":"acceleratorType","acceleratorCount":"acceleratorCount","gpuPartitionSize":"gpuPartitionSize"}],"localSsdCount":4,"machineType":"machineType"}},"roles":["ROLE_UNSPECIFIED","ROLE_UNSPECIFIED"]},{"nodePool":"nodePool","nodePoolConfig":{"locations":["locations","locations"],"autoscaling":{"minNodeCount":2,"maxNodeCount":3},"config":{"preemptible":True,"minCpuPlatform":"minCpuPlatform","spot":True,"bootDiskKmsKey":"bootDiskKmsKey","accelerators":[{"acceleratorType":"acceleratorType","acceleratorCount":"acceleratorCount","gpuPartitionSize":"gpuPartitionSize"},{"acceleratorType":"acceleratorType","acceleratorCount":"acceleratorCount","gpuPartitionSize":"gpuPartitionSize"}],"localSsdCount":4,"machineType":"machineType"}},"roles":["ROLE_UNSPECIFIED","ROLE_UNSPECIFIED"]}]},"kubernetesNamespace":"kubernetesNamespace","kubernetesSoftwareConfig":{"componentVersion":{"key":"componentVersion"},"properties":{"key":"properties"}}},"stagingBucket":"stagingBucket","auxiliaryServicesConfig":{"metastoreConfig":{"dataprocMetastoreService":"dataprocMetastoreService"},"sparkHistoryServerConfig":{"dataprocCluster":"dataprocCluster"}}},"labels":{"key":"labels"},"status":{"substate":"UNSPECIFIED","detail":"detail","state":"UNKNOWN","stateStartTime":"stateStartTime"}}
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
                    ('gracefulDecommissionTimeout', 'graceful_decommission_timeout_example'),
                    ('requestId', 'request_id_example'),
                    ('updateMask', 'update_mask_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/v1/projects/{project_id}/regions/{region}/clusters/{cluster_name}'.format(project_id='project_id_example', region='region_example', cluster_name='cluster_name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dataproc_projects_regions_clusters_repair(client):
    """Test case for dataproc_projects_regions_clusters_repair

    
    """
    body = {"clusterUuid":"clusterUuid","parentOperationId":"parentOperationId","requestId":"requestId","gracefulDecommissionTimeout":"gracefulDecommissionTimeout","nodePools":[{"instanceNames":["instanceNames","instanceNames"],"repairAction":"REPAIR_ACTION_UNSPECIFIED","id":"id"},{"instanceNames":["instanceNames","instanceNames"],"repairAction":"REPAIR_ACTION_UNSPECIFIED","id":"id"}]}
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
        path='/v1/projects/{project_id}/regions/{region}/clusters/{cluster_namerepai}'.format(project_id='project_id_example', region='region_example', cluster_name='cluster_name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dataproc_projects_regions_clusters_start(client):
    """Test case for dataproc_projects_regions_clusters_start

    
    """
    body = {"clusterUuid":"clusterUuid","requestId":"requestId"}
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
        path='/v1/projects/{project_id}/regions/{region}/clusters/{cluster_namestar}'.format(project_id='project_id_example', region='region_example', cluster_name='cluster_name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dataproc_projects_regions_clusters_stop(client):
    """Test case for dataproc_projects_regions_clusters_stop

    
    """
    body = {"clusterUuid":"clusterUuid","requestId":"requestId"}
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
        path='/v1/projects/{project_id}/regions/{region}/clusters/{cluster_namesto}'.format(project_id='project_id_example', region='region_example', cluster_name='cluster_name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dataproc_projects_regions_jobs_cancel(client):
    """Test case for dataproc_projects_regions_jobs_cancel

    
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
        path='/v1/projects/{project_id}/regions/{region}/jobs/{job_idcance}'.format(project_id='project_id_example', region='region_example', job_id='job_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dataproc_projects_regions_jobs_delete(client):
    """Test case for dataproc_projects_regions_jobs_delete

    
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
        method='DELETE',
        path='/v1/projects/{project_id}/regions/{region}/jobs/{job_id}'.format(project_id='project_id_example', region='region_example', job_id='job_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dataproc_projects_regions_jobs_get(client):
    """Test case for dataproc_projects_regions_jobs_get

    
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
        path='/v1/projects/{project_id}/regions/{region}/jobs/{job_id}'.format(project_id='project_id_example', region='region_example', job_id='job_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dataproc_projects_regions_jobs_list(client):
    """Test case for dataproc_projects_regions_jobs_list

    
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
                    ('clusterName', 'cluster_name_example'),
                    ('filter', 'filter_example'),
                    ('jobStateMatcher', 'job_state_matcher_example'),
                    ('pageSize', 56),
                    ('pageToken', 'page_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/projects/{project_id}/regions/{region}/jobs'.format(project_id='project_id_example', region='region_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dataproc_projects_regions_jobs_patch(client):
    """Test case for dataproc_projects_regions_jobs_patch

    
    """
    body = {"driverControlFilesUri":"driverControlFilesUri","yarnApplications":[{"trackingUrl":"trackingUrl","name":"name","progress":5.637377,"state":"STATE_UNSPECIFIED"},{"trackingUrl":"trackingUrl","name":"name","progress":5.637377,"state":"STATE_UNSPECIFIED"}],"trinoJob":{"clientTags":["clientTags","clientTags"],"loggingConfig":{"driverLogLevels":{"key":"LEVEL_UNSPECIFIED"}},"continueOnFailure":True,"queryFileUri":"queryFileUri","outputFormat":"outputFormat","properties":{"key":"properties"},"queryList":{"queries":["queries","queries"]}},"done":True,"prestoJob":{"clientTags":["clientTags","clientTags"],"loggingConfig":{"driverLogLevels":{"key":"LEVEL_UNSPECIFIED"}},"continueOnFailure":True,"queryFileUri":"queryFileUri","outputFormat":"outputFormat","properties":{"key":"properties"},"queryList":{"queries":["queries","queries"]}},"driverOutputResourceUri":"driverOutputResourceUri","hiveJob":{"scriptVariables":{"key":"scriptVariables"},"continueOnFailure":True,"queryFileUri":"queryFileUri","jarFileUris":["jarFileUris","jarFileUris"],"properties":{"key":"properties"},"queryList":{"queries":["queries","queries"]}},"labels":{"key":"labels"},"hadoopJob":{"args":["args","args"],"mainClass":"mainClass","archiveUris":["archiveUris","archiveUris"],"loggingConfig":{"driverLogLevels":{"key":"LEVEL_UNSPECIFIED"}},"mainJarFileUri":"mainJarFileUri","fileUris":["fileUris","fileUris"],"jarFileUris":["jarFileUris","jarFileUris"],"properties":{"key":"properties"}},"pysparkJob":{"args":["args","args"],"archiveUris":["archiveUris","archiveUris"],"loggingConfig":{"driverLogLevels":{"key":"LEVEL_UNSPECIFIED"}},"mainPythonFileUri":"mainPythonFileUri","fileUris":["fileUris","fileUris"],"jarFileUris":["jarFileUris","jarFileUris"],"properties":{"key":"properties"},"pythonFileUris":["pythonFileUris","pythonFileUris"]},"reference":{"jobId":"jobId","projectId":"projectId"},"statusHistory":[{"substate":"UNSPECIFIED","details":"details","state":"STATE_UNSPECIFIED","stateStartTime":"stateStartTime"},{"substate":"UNSPECIFIED","details":"details","state":"STATE_UNSPECIFIED","stateStartTime":"stateStartTime"}],"jobUuid":"jobUuid","sparkSqlJob":{"scriptVariables":{"key":"scriptVariables"},"loggingConfig":{"driverLogLevels":{"key":"LEVEL_UNSPECIFIED"}},"queryFileUri":"queryFileUri","jarFileUris":["jarFileUris","jarFileUris"],"properties":{"key":"properties"},"queryList":{"queries":["queries","queries"]}},"driverSchedulingConfig":{"memoryMb":0,"vcores":6},"flinkJob":{"args":["args","args"],"mainClass":"mainClass","loggingConfig":{"driverLogLevels":{"key":"LEVEL_UNSPECIFIED"}},"mainJarFileUri":"mainJarFileUri","jarFileUris":["jarFileUris","jarFileUris"],"properties":{"key":"properties"},"savepointUri":"savepointUri"},"scheduling":{"maxFailuresTotal":5,"maxFailuresPerHour":1},"sparkRJob":{"args":["args","args"],"mainRFileUri":"mainRFileUri","archiveUris":["archiveUris","archiveUris"],"loggingConfig":{"driverLogLevels":{"key":"LEVEL_UNSPECIFIED"}},"fileUris":["fileUris","fileUris"],"properties":{"key":"properties"}},"pigJob":{"scriptVariables":{"key":"scriptVariables"},"loggingConfig":{"driverLogLevels":{"key":"LEVEL_UNSPECIFIED"}},"continueOnFailure":True,"queryFileUri":"queryFileUri","jarFileUris":["jarFileUris","jarFileUris"],"properties":{"key":"properties"},"queryList":{"queries":["queries","queries"]}},"placement":{"clusterUuid":"clusterUuid","clusterName":"clusterName","clusterLabels":{"key":"clusterLabels"}},"sparkJob":{"args":["args","args"],"mainClass":"mainClass","archiveUris":["archiveUris","archiveUris"],"loggingConfig":{"driverLogLevels":{"key":"LEVEL_UNSPECIFIED"}},"mainJarFileUri":"mainJarFileUri","fileUris":["fileUris","fileUris"],"jarFileUris":["jarFileUris","jarFileUris"],"properties":{"key":"properties"}},"status":{"substate":"UNSPECIFIED","details":"details","state":"STATE_UNSPECIFIED","stateStartTime":"stateStartTime"}}
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
                    ('updateMask', 'update_mask_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/v1/projects/{project_id}/regions/{region}/jobs/{job_id}'.format(project_id='project_id_example', region='region_example', job_id='job_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dataproc_projects_regions_jobs_submit(client):
    """Test case for dataproc_projects_regions_jobs_submit

    
    """
    body = {"requestId":"requestId","job":{"driverControlFilesUri":"driverControlFilesUri","yarnApplications":[{"trackingUrl":"trackingUrl","name":"name","progress":5.637377,"state":"STATE_UNSPECIFIED"},{"trackingUrl":"trackingUrl","name":"name","progress":5.637377,"state":"STATE_UNSPECIFIED"}],"trinoJob":{"clientTags":["clientTags","clientTags"],"loggingConfig":{"driverLogLevels":{"key":"LEVEL_UNSPECIFIED"}},"continueOnFailure":True,"queryFileUri":"queryFileUri","outputFormat":"outputFormat","properties":{"key":"properties"},"queryList":{"queries":["queries","queries"]}},"done":True,"prestoJob":{"clientTags":["clientTags","clientTags"],"loggingConfig":{"driverLogLevels":{"key":"LEVEL_UNSPECIFIED"}},"continueOnFailure":True,"queryFileUri":"queryFileUri","outputFormat":"outputFormat","properties":{"key":"properties"},"queryList":{"queries":["queries","queries"]}},"driverOutputResourceUri":"driverOutputResourceUri","hiveJob":{"scriptVariables":{"key":"scriptVariables"},"continueOnFailure":True,"queryFileUri":"queryFileUri","jarFileUris":["jarFileUris","jarFileUris"],"properties":{"key":"properties"},"queryList":{"queries":["queries","queries"]}},"labels":{"key":"labels"},"hadoopJob":{"args":["args","args"],"mainClass":"mainClass","archiveUris":["archiveUris","archiveUris"],"loggingConfig":{"driverLogLevels":{"key":"LEVEL_UNSPECIFIED"}},"mainJarFileUri":"mainJarFileUri","fileUris":["fileUris","fileUris"],"jarFileUris":["jarFileUris","jarFileUris"],"properties":{"key":"properties"}},"pysparkJob":{"args":["args","args"],"archiveUris":["archiveUris","archiveUris"],"loggingConfig":{"driverLogLevels":{"key":"LEVEL_UNSPECIFIED"}},"mainPythonFileUri":"mainPythonFileUri","fileUris":["fileUris","fileUris"],"jarFileUris":["jarFileUris","jarFileUris"],"properties":{"key":"properties"},"pythonFileUris":["pythonFileUris","pythonFileUris"]},"reference":{"jobId":"jobId","projectId":"projectId"},"statusHistory":[{"substate":"UNSPECIFIED","details":"details","state":"STATE_UNSPECIFIED","stateStartTime":"stateStartTime"},{"substate":"UNSPECIFIED","details":"details","state":"STATE_UNSPECIFIED","stateStartTime":"stateStartTime"}],"jobUuid":"jobUuid","sparkSqlJob":{"scriptVariables":{"key":"scriptVariables"},"loggingConfig":{"driverLogLevels":{"key":"LEVEL_UNSPECIFIED"}},"queryFileUri":"queryFileUri","jarFileUris":["jarFileUris","jarFileUris"],"properties":{"key":"properties"},"queryList":{"queries":["queries","queries"]}},"driverSchedulingConfig":{"memoryMb":0,"vcores":6},"flinkJob":{"args":["args","args"],"mainClass":"mainClass","loggingConfig":{"driverLogLevels":{"key":"LEVEL_UNSPECIFIED"}},"mainJarFileUri":"mainJarFileUri","jarFileUris":["jarFileUris","jarFileUris"],"properties":{"key":"properties"},"savepointUri":"savepointUri"},"scheduling":{"maxFailuresTotal":5,"maxFailuresPerHour":1},"sparkRJob":{"args":["args","args"],"mainRFileUri":"mainRFileUri","archiveUris":["archiveUris","archiveUris"],"loggingConfig":{"driverLogLevels":{"key":"LEVEL_UNSPECIFIED"}},"fileUris":["fileUris","fileUris"],"properties":{"key":"properties"}},"pigJob":{"scriptVariables":{"key":"scriptVariables"},"loggingConfig":{"driverLogLevels":{"key":"LEVEL_UNSPECIFIED"}},"continueOnFailure":True,"queryFileUri":"queryFileUri","jarFileUris":["jarFileUris","jarFileUris"],"properties":{"key":"properties"},"queryList":{"queries":["queries","queries"]}},"placement":{"clusterUuid":"clusterUuid","clusterName":"clusterName","clusterLabels":{"key":"clusterLabels"}},"sparkJob":{"args":["args","args"],"mainClass":"mainClass","archiveUris":["archiveUris","archiveUris"],"loggingConfig":{"driverLogLevels":{"key":"LEVEL_UNSPECIFIED"}},"mainJarFileUri":"mainJarFileUri","fileUris":["fileUris","fileUris"],"jarFileUris":["jarFileUris","jarFileUris"],"properties":{"key":"properties"}},"status":{"substate":"UNSPECIFIED","details":"details","state":"STATE_UNSPECIFIED","stateStartTime":"stateStartTime"}}}
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
        path='/v1/projects/{project_id}/regions/{region}/jobs:submit'.format(project_id='project_id_example', region='region_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dataproc_projects_regions_jobs_submit_as_operation(client):
    """Test case for dataproc_projects_regions_jobs_submit_as_operation

    
    """
    body = {"requestId":"requestId","job":{"driverControlFilesUri":"driverControlFilesUri","yarnApplications":[{"trackingUrl":"trackingUrl","name":"name","progress":5.637377,"state":"STATE_UNSPECIFIED"},{"trackingUrl":"trackingUrl","name":"name","progress":5.637377,"state":"STATE_UNSPECIFIED"}],"trinoJob":{"clientTags":["clientTags","clientTags"],"loggingConfig":{"driverLogLevels":{"key":"LEVEL_UNSPECIFIED"}},"continueOnFailure":True,"queryFileUri":"queryFileUri","outputFormat":"outputFormat","properties":{"key":"properties"},"queryList":{"queries":["queries","queries"]}},"done":True,"prestoJob":{"clientTags":["clientTags","clientTags"],"loggingConfig":{"driverLogLevels":{"key":"LEVEL_UNSPECIFIED"}},"continueOnFailure":True,"queryFileUri":"queryFileUri","outputFormat":"outputFormat","properties":{"key":"properties"},"queryList":{"queries":["queries","queries"]}},"driverOutputResourceUri":"driverOutputResourceUri","hiveJob":{"scriptVariables":{"key":"scriptVariables"},"continueOnFailure":True,"queryFileUri":"queryFileUri","jarFileUris":["jarFileUris","jarFileUris"],"properties":{"key":"properties"},"queryList":{"queries":["queries","queries"]}},"labels":{"key":"labels"},"hadoopJob":{"args":["args","args"],"mainClass":"mainClass","archiveUris":["archiveUris","archiveUris"],"loggingConfig":{"driverLogLevels":{"key":"LEVEL_UNSPECIFIED"}},"mainJarFileUri":"mainJarFileUri","fileUris":["fileUris","fileUris"],"jarFileUris":["jarFileUris","jarFileUris"],"properties":{"key":"properties"}},"pysparkJob":{"args":["args","args"],"archiveUris":["archiveUris","archiveUris"],"loggingConfig":{"driverLogLevels":{"key":"LEVEL_UNSPECIFIED"}},"mainPythonFileUri":"mainPythonFileUri","fileUris":["fileUris","fileUris"],"jarFileUris":["jarFileUris","jarFileUris"],"properties":{"key":"properties"},"pythonFileUris":["pythonFileUris","pythonFileUris"]},"reference":{"jobId":"jobId","projectId":"projectId"},"statusHistory":[{"substate":"UNSPECIFIED","details":"details","state":"STATE_UNSPECIFIED","stateStartTime":"stateStartTime"},{"substate":"UNSPECIFIED","details":"details","state":"STATE_UNSPECIFIED","stateStartTime":"stateStartTime"}],"jobUuid":"jobUuid","sparkSqlJob":{"scriptVariables":{"key":"scriptVariables"},"loggingConfig":{"driverLogLevels":{"key":"LEVEL_UNSPECIFIED"}},"queryFileUri":"queryFileUri","jarFileUris":["jarFileUris","jarFileUris"],"properties":{"key":"properties"},"queryList":{"queries":["queries","queries"]}},"driverSchedulingConfig":{"memoryMb":0,"vcores":6},"flinkJob":{"args":["args","args"],"mainClass":"mainClass","loggingConfig":{"driverLogLevels":{"key":"LEVEL_UNSPECIFIED"}},"mainJarFileUri":"mainJarFileUri","jarFileUris":["jarFileUris","jarFileUris"],"properties":{"key":"properties"},"savepointUri":"savepointUri"},"scheduling":{"maxFailuresTotal":5,"maxFailuresPerHour":1},"sparkRJob":{"args":["args","args"],"mainRFileUri":"mainRFileUri","archiveUris":["archiveUris","archiveUris"],"loggingConfig":{"driverLogLevels":{"key":"LEVEL_UNSPECIFIED"}},"fileUris":["fileUris","fileUris"],"properties":{"key":"properties"}},"pigJob":{"scriptVariables":{"key":"scriptVariables"},"loggingConfig":{"driverLogLevels":{"key":"LEVEL_UNSPECIFIED"}},"continueOnFailure":True,"queryFileUri":"queryFileUri","jarFileUris":["jarFileUris","jarFileUris"],"properties":{"key":"properties"},"queryList":{"queries":["queries","queries"]}},"placement":{"clusterUuid":"clusterUuid","clusterName":"clusterName","clusterLabels":{"key":"clusterLabels"}},"sparkJob":{"args":["args","args"],"mainClass":"mainClass","archiveUris":["archiveUris","archiveUris"],"loggingConfig":{"driverLogLevels":{"key":"LEVEL_UNSPECIFIED"}},"mainJarFileUri":"mainJarFileUri","fileUris":["fileUris","fileUris"],"jarFileUris":["jarFileUris","jarFileUris"],"properties":{"key":"properties"}},"status":{"substate":"UNSPECIFIED","details":"details","state":"STATE_UNSPECIFIED","stateStartTime":"stateStartTime"}}}
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
        path='/v1/projects/{project_id}/regions/{region}/jobs:submitAsOperation'.format(project_id='project_id_example', region='region_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dataproc_projects_regions_operations_cancel(client):
    """Test case for dataproc_projects_regions_operations_cancel

    
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
        method='POST',
        path='/v1/{namecance}'.format(name='name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dataproc_projects_regions_workflow_templates_create(client):
    """Test case for dataproc_projects_regions_workflow_templates_create

    
    """
    body = {"encryptionConfig":{"kmsKey":"kmsKey"},"createTime":"createTime","jobs":[{"stepId":"stepId","prerequisiteStepIds":["prerequisiteStepIds","prerequisiteStepIds"],"trinoJob":{"clientTags":["clientTags","clientTags"],"loggingConfig":{"driverLogLevels":{"key":"LEVEL_UNSPECIFIED"}},"continueOnFailure":True,"queryFileUri":"queryFileUri","outputFormat":"outputFormat","properties":{"key":"properties"},"queryList":{"queries":["queries","queries"]}},"prestoJob":{"clientTags":["clientTags","clientTags"],"loggingConfig":{"driverLogLevels":{"key":"LEVEL_UNSPECIFIED"}},"continueOnFailure":True,"queryFileUri":"queryFileUri","outputFormat":"outputFormat","properties":{"key":"properties"},"queryList":{"queries":["queries","queries"]}},"hiveJob":{"scriptVariables":{"key":"scriptVariables"},"continueOnFailure":True,"queryFileUri":"queryFileUri","jarFileUris":["jarFileUris","jarFileUris"],"properties":{"key":"properties"},"queryList":{"queries":["queries","queries"]}},"labels":{"key":"labels"},"hadoopJob":{"args":["args","args"],"mainClass":"mainClass","archiveUris":["archiveUris","archiveUris"],"loggingConfig":{"driverLogLevels":{"key":"LEVEL_UNSPECIFIED"}},"mainJarFileUri":"mainJarFileUri","fileUris":["fileUris","fileUris"],"jarFileUris":["jarFileUris","jarFileUris"],"properties":{"key":"properties"}},"pysparkJob":{"args":["args","args"],"archiveUris":["archiveUris","archiveUris"],"loggingConfig":{"driverLogLevels":{"key":"LEVEL_UNSPECIFIED"}},"mainPythonFileUri":"mainPythonFileUri","fileUris":["fileUris","fileUris"],"jarFileUris":["jarFileUris","jarFileUris"],"properties":{"key":"properties"},"pythonFileUris":["pythonFileUris","pythonFileUris"]},"sparkSqlJob":{"scriptVariables":{"key":"scriptVariables"},"loggingConfig":{"driverLogLevels":{"key":"LEVEL_UNSPECIFIED"}},"queryFileUri":"queryFileUri","jarFileUris":["jarFileUris","jarFileUris"],"properties":{"key":"properties"},"queryList":{"queries":["queries","queries"]}},"flinkJob":{"args":["args","args"],"mainClass":"mainClass","loggingConfig":{"driverLogLevels":{"key":"LEVEL_UNSPECIFIED"}},"mainJarFileUri":"mainJarFileUri","jarFileUris":["jarFileUris","jarFileUris"],"properties":{"key":"properties"},"savepointUri":"savepointUri"},"scheduling":{"maxFailuresTotal":5,"maxFailuresPerHour":1},"sparkRJob":{"args":["args","args"],"mainRFileUri":"mainRFileUri","archiveUris":["archiveUris","archiveUris"],"loggingConfig":{"driverLogLevels":{"key":"LEVEL_UNSPECIFIED"}},"fileUris":["fileUris","fileUris"],"properties":{"key":"properties"}},"pigJob":{"scriptVariables":{"key":"scriptVariables"},"loggingConfig":{"driverLogLevels":{"key":"LEVEL_UNSPECIFIED"}},"continueOnFailure":True,"queryFileUri":"queryFileUri","jarFileUris":["jarFileUris","jarFileUris"],"properties":{"key":"properties"},"queryList":{"queries":["queries","queries"]}},"sparkJob":{"args":["args","args"],"mainClass":"mainClass","archiveUris":["archiveUris","archiveUris"],"loggingConfig":{"driverLogLevels":{"key":"LEVEL_UNSPECIFIED"}},"mainJarFileUri":"mainJarFileUri","fileUris":["fileUris","fileUris"],"jarFileUris":["jarFileUris","jarFileUris"],"properties":{"key":"properties"}}},{"stepId":"stepId","prerequisiteStepIds":["prerequisiteStepIds","prerequisiteStepIds"],"trinoJob":{"clientTags":["clientTags","clientTags"],"loggingConfig":{"driverLogLevels":{"key":"LEVEL_UNSPECIFIED"}},"continueOnFailure":True,"queryFileUri":"queryFileUri","outputFormat":"outputFormat","properties":{"key":"properties"},"queryList":{"queries":["queries","queries"]}},"prestoJob":{"clientTags":["clientTags","clientTags"],"loggingConfig":{"driverLogLevels":{"key":"LEVEL_UNSPECIFIED"}},"continueOnFailure":True,"queryFileUri":"queryFileUri","outputFormat":"outputFormat","properties":{"key":"properties"},"queryList":{"queries":["queries","queries"]}},"hiveJob":{"scriptVariables":{"key":"scriptVariables"},"continueOnFailure":True,"queryFileUri":"queryFileUri","jarFileUris":["jarFileUris","jarFileUris"],"properties":{"key":"properties"},"queryList":{"queries":["queries","queries"]}},"labels":{"key":"labels"},"hadoopJob":{"args":["args","args"],"mainClass":"mainClass","archiveUris":["archiveUris","archiveUris"],"loggingConfig":{"driverLogLevels":{"key":"LEVEL_UNSPECIFIED"}},"mainJarFileUri":"mainJarFileUri","fileUris":["fileUris","fileUris"],"jarFileUris":["jarFileUris","jarFileUris"],"properties":{"key":"properties"}},"pysparkJob":{"args":["args","args"],"archiveUris":["archiveUris","archiveUris"],"loggingConfig":{"driverLogLevels":{"key":"LEVEL_UNSPECIFIED"}},"mainPythonFileUri":"mainPythonFileUri","fileUris":["fileUris","fileUris"],"jarFileUris":["jarFileUris","jarFileUris"],"properties":{"key":"properties"},"pythonFileUris":["pythonFileUris","pythonFileUris"]},"sparkSqlJob":{"scriptVariables":{"key":"scriptVariables"},"loggingConfig":{"driverLogLevels":{"key":"LEVEL_UNSPECIFIED"}},"queryFileUri":"queryFileUri","jarFileUris":["jarFileUris","jarFileUris"],"properties":{"key":"properties"},"queryList":{"queries":["queries","queries"]}},"flinkJob":{"args":["args","args"],"mainClass":"mainClass","loggingConfig":{"driverLogLevels":{"key":"LEVEL_UNSPECIFIED"}},"mainJarFileUri":"mainJarFileUri","jarFileUris":["jarFileUris","jarFileUris"],"properties":{"key":"properties"},"savepointUri":"savepointUri"},"scheduling":{"maxFailuresTotal":5,"maxFailuresPerHour":1},"sparkRJob":{"args":["args","args"],"mainRFileUri":"mainRFileUri","archiveUris":["archiveUris","archiveUris"],"loggingConfig":{"driverLogLevels":{"key":"LEVEL_UNSPECIFIED"}},"fileUris":["fileUris","fileUris"],"properties":{"key":"properties"}},"pigJob":{"scriptVariables":{"key":"scriptVariables"},"loggingConfig":{"driverLogLevels":{"key":"LEVEL_UNSPECIFIED"}},"continueOnFailure":True,"queryFileUri":"queryFileUri","jarFileUris":["jarFileUris","jarFileUris"],"properties":{"key":"properties"},"queryList":{"queries":["queries","queries"]}},"sparkJob":{"args":["args","args"],"mainClass":"mainClass","archiveUris":["archiveUris","archiveUris"],"loggingConfig":{"driverLogLevels":{"key":"LEVEL_UNSPECIFIED"}},"mainJarFileUri":"mainJarFileUri","fileUris":["fileUris","fileUris"],"jarFileUris":["jarFileUris","jarFileUris"],"properties":{"key":"properties"}}}],"dagTimeout":"dagTimeout","name":"name","updateTime":"updateTime","id":"id","placement":{"clusterSelector":{"zone":"zone","clusterLabels":{"key":"clusterLabels"}},"managedCluster":{"clusterName":"clusterName","config":{"encryptionConfig":{"kmsKey":"kmsKey","gcePdKmsKeyName":"gcePdKmsKeyName"},"softwareConfig":{"imageVersion":"imageVersion","optionalComponents":["COMPONENT_UNSPECIFIED","COMPONENT_UNSPECIFIED"],"properties":{"key":"properties"}},"lifecycleConfig":{"autoDeleteTime":"autoDeleteTime","idleStartTime":"idleStartTime","idleDeleteTtl":"idleDeleteTtl","autoDeleteTtl":"autoDeleteTtl"},"configBucket":"configBucket","masterConfig":{"instanceFlexibilityPolicy":{"instanceSelectionResults":[{"vmCount":5,"machineType":"machineType"},{"vmCount":5,"machineType":"machineType"}],"instanceSelectionList":[{"rank":5,"machineTypes":["machineTypes","machineTypes"]},{"rank":5,"machineTypes":["machineTypes","machineTypes"]}]},"minNumInstances":2,"machineTypeUri":"machineTypeUri","isPreemptible":True,"preemptibility":"PREEMPTIBILITY_UNSPECIFIED","managedGroupConfig":{"instanceGroupManagerUri":"instanceGroupManagerUri","instanceGroupManagerName":"instanceGroupManagerName","instanceTemplateName":"instanceTemplateName"},"imageUri":"imageUri","instanceNames":["instanceNames","instanceNames"],"instanceReferences":[{"instanceId":"instanceId","instanceName":"instanceName","publicEciesKey":"publicEciesKey","publicKey":"publicKey"},{"instanceId":"instanceId","instanceName":"instanceName","publicEciesKey":"publicEciesKey","publicKey":"publicKey"}],"minCpuPlatform":"minCpuPlatform","numInstances":7,"diskConfig":{"bootDiskType":"bootDiskType","bootDiskSizeGb":6,"localSsdInterface":"localSsdInterface","numLocalSsds":1},"accelerators":[{"acceleratorTypeUri":"acceleratorTypeUri","acceleratorCount":0},{"acceleratorTypeUri":"acceleratorTypeUri","acceleratorCount":0}],"startupConfig":{"requiredRegistrationFraction":9.301444243932576}},"workerConfig":{"instanceFlexibilityPolicy":{"instanceSelectionResults":[{"vmCount":5,"machineType":"machineType"},{"vmCount":5,"machineType":"machineType"}],"instanceSelectionList":[{"rank":5,"machineTypes":["machineTypes","machineTypes"]},{"rank":5,"machineTypes":["machineTypes","machineTypes"]}]},"minNumInstances":2,"machineTypeUri":"machineTypeUri","isPreemptible":True,"preemptibility":"PREEMPTIBILITY_UNSPECIFIED","managedGroupConfig":{"instanceGroupManagerUri":"instanceGroupManagerUri","instanceGroupManagerName":"instanceGroupManagerName","instanceTemplateName":"instanceTemplateName"},"imageUri":"imageUri","instanceNames":["instanceNames","instanceNames"],"instanceReferences":[{"instanceId":"instanceId","instanceName":"instanceName","publicEciesKey":"publicEciesKey","publicKey":"publicKey"},{"instanceId":"instanceId","instanceName":"instanceName","publicEciesKey":"publicEciesKey","publicKey":"publicKey"}],"minCpuPlatform":"minCpuPlatform","numInstances":7,"diskConfig":{"bootDiskType":"bootDiskType","bootDiskSizeGb":6,"localSsdInterface":"localSsdInterface","numLocalSsds":1},"accelerators":[{"acceleratorTypeUri":"acceleratorTypeUri","acceleratorCount":0},{"acceleratorTypeUri":"acceleratorTypeUri","acceleratorCount":0}],"startupConfig":{"requiredRegistrationFraction":9.301444243932576}},"secondaryWorkerConfig":{"instanceFlexibilityPolicy":{"instanceSelectionResults":[{"vmCount":5,"machineType":"machineType"},{"vmCount":5,"machineType":"machineType"}],"instanceSelectionList":[{"rank":5,"machineTypes":["machineTypes","machineTypes"]},{"rank":5,"machineTypes":["machineTypes","machineTypes"]}]},"minNumInstances":2,"machineTypeUri":"machineTypeUri","isPreemptible":True,"preemptibility":"PREEMPTIBILITY_UNSPECIFIED","managedGroupConfig":{"instanceGroupManagerUri":"instanceGroupManagerUri","instanceGroupManagerName":"instanceGroupManagerName","instanceTemplateName":"instanceTemplateName"},"imageUri":"imageUri","instanceNames":["instanceNames","instanceNames"],"instanceReferences":[{"instanceId":"instanceId","instanceName":"instanceName","publicEciesKey":"publicEciesKey","publicKey":"publicKey"},{"instanceId":"instanceId","instanceName":"instanceName","publicEciesKey":"publicEciesKey","publicKey":"publicKey"}],"minCpuPlatform":"minCpuPlatform","numInstances":7,"diskConfig":{"bootDiskType":"bootDiskType","bootDiskSizeGb":6,"localSsdInterface":"localSsdInterface","numLocalSsds":1},"accelerators":[{"acceleratorTypeUri":"acceleratorTypeUri","acceleratorCount":0},{"acceleratorTypeUri":"acceleratorTypeUri","acceleratorCount":0}],"startupConfig":{"requiredRegistrationFraction":9.301444243932576}},"gkeClusterConfig":{"gkeClusterTarget":"gkeClusterTarget","namespacedGkeDeploymentTarget":{"clusterNamespace":"clusterNamespace","targetGkeCluster":"targetGkeCluster"},"nodePoolTarget":[{"nodePool":"nodePool","nodePoolConfig":{"locations":["locations","locations"],"autoscaling":{"minNodeCount":2,"maxNodeCount":3},"config":{"preemptible":True,"minCpuPlatform":"minCpuPlatform","spot":True,"bootDiskKmsKey":"bootDiskKmsKey","accelerators":[{"acceleratorType":"acceleratorType","acceleratorCount":"acceleratorCount","gpuPartitionSize":"gpuPartitionSize"},{"acceleratorType":"acceleratorType","acceleratorCount":"acceleratorCount","gpuPartitionSize":"gpuPartitionSize"}],"localSsdCount":4,"machineType":"machineType"}},"roles":["ROLE_UNSPECIFIED","ROLE_UNSPECIFIED"]},{"nodePool":"nodePool","nodePoolConfig":{"locations":["locations","locations"],"autoscaling":{"minNodeCount":2,"maxNodeCount":3},"config":{"preemptible":True,"minCpuPlatform":"minCpuPlatform","spot":True,"bootDiskKmsKey":"bootDiskKmsKey","accelerators":[{"acceleratorType":"acceleratorType","acceleratorCount":"acceleratorCount","gpuPartitionSize":"gpuPartitionSize"},{"acceleratorType":"acceleratorType","acceleratorCount":"acceleratorCount","gpuPartitionSize":"gpuPartitionSize"}],"localSsdCount":4,"machineType":"machineType"}},"roles":["ROLE_UNSPECIFIED","ROLE_UNSPECIFIED"]}]},"securityConfig":{"identityConfig":{"userServiceAccountMapping":{"key":"userServiceAccountMapping"}},"kerberosConfig":{"tgtLifetimeHours":7,"keyPasswordUri":"keyPasswordUri","rootPrincipalPasswordUri":"rootPrincipalPasswordUri","kdcDbKeyUri":"kdcDbKeyUri","crossRealmTrustSharedPasswordUri":"crossRealmTrustSharedPasswordUri","keystoreUri":"keystoreUri","truststorePasswordUri":"truststorePasswordUri","crossRealmTrustKdc":"crossRealmTrustKdc","enableKerberos":True,"crossRealmTrustAdminServer":"crossRealmTrustAdminServer","kmsKeyUri":"kmsKeyUri","truststoreUri":"truststoreUri","realm":"realm","crossRealmTrustRealm":"crossRealmTrustRealm","keystorePasswordUri":"keystorePasswordUri"}},"autoscalingConfig":{"policyUri":"policyUri"},"metastoreConfig":{"dataprocMetastoreService":"dataprocMetastoreService"},"endpointConfig":{"httpPorts":{"key":"httpPorts"},"enableHttpPortAccess":True},"auxiliaryNodeGroups":[{"nodeGroupId":"nodeGroupId","nodeGroup":{"nodeGroupConfig":{"instanceFlexibilityPolicy":{"instanceSelectionResults":[{"vmCount":5,"machineType":"machineType"},{"vmCount":5,"machineType":"machineType"}],"instanceSelectionList":[{"rank":5,"machineTypes":["machineTypes","machineTypes"]},{"rank":5,"machineTypes":["machineTypes","machineTypes"]}]},"minNumInstances":2,"machineTypeUri":"machineTypeUri","isPreemptible":True,"preemptibility":"PREEMPTIBILITY_UNSPECIFIED","managedGroupConfig":{"instanceGroupManagerUri":"instanceGroupManagerUri","instanceGroupManagerName":"instanceGroupManagerName","instanceTemplateName":"instanceTemplateName"},"imageUri":"imageUri","instanceNames":["instanceNames","instanceNames"],"instanceReferences":[{"instanceId":"instanceId","instanceName":"instanceName","publicEciesKey":"publicEciesKey","publicKey":"publicKey"},{"instanceId":"instanceId","instanceName":"instanceName","publicEciesKey":"publicEciesKey","publicKey":"publicKey"}],"minCpuPlatform":"minCpuPlatform","numInstances":7,"diskConfig":{"bootDiskType":"bootDiskType","bootDiskSizeGb":6,"localSsdInterface":"localSsdInterface","numLocalSsds":1},"accelerators":[{"acceleratorTypeUri":"acceleratorTypeUri","acceleratorCount":0},{"acceleratorTypeUri":"acceleratorTypeUri","acceleratorCount":0}],"startupConfig":{"requiredRegistrationFraction":9.301444243932576}},"roles":["ROLE_UNSPECIFIED","ROLE_UNSPECIFIED"],"name":"name","labels":{"key":"labels"}}},{"nodeGroupId":"nodeGroupId","nodeGroup":{"nodeGroupConfig":{"instanceFlexibilityPolicy":{"instanceSelectionResults":[{"vmCount":5,"machineType":"machineType"},{"vmCount":5,"machineType":"machineType"}],"instanceSelectionList":[{"rank":5,"machineTypes":["machineTypes","machineTypes"]},{"rank":5,"machineTypes":["machineTypes","machineTypes"]}]},"minNumInstances":2,"machineTypeUri":"machineTypeUri","isPreemptible":True,"preemptibility":"PREEMPTIBILITY_UNSPECIFIED","managedGroupConfig":{"instanceGroupManagerUri":"instanceGroupManagerUri","instanceGroupManagerName":"instanceGroupManagerName","instanceTemplateName":"instanceTemplateName"},"imageUri":"imageUri","instanceNames":["instanceNames","instanceNames"],"instanceReferences":[{"instanceId":"instanceId","instanceName":"instanceName","publicEciesKey":"publicEciesKey","publicKey":"publicKey"},{"instanceId":"instanceId","instanceName":"instanceName","publicEciesKey":"publicEciesKey","publicKey":"publicKey"}],"minCpuPlatform":"minCpuPlatform","numInstances":7,"diskConfig":{"bootDiskType":"bootDiskType","bootDiskSizeGb":6,"localSsdInterface":"localSsdInterface","numLocalSsds":1},"accelerators":[{"acceleratorTypeUri":"acceleratorTypeUri","acceleratorCount":0},{"acceleratorTypeUri":"acceleratorTypeUri","acceleratorCount":0}],"startupConfig":{"requiredRegistrationFraction":9.301444243932576}},"roles":["ROLE_UNSPECIFIED","ROLE_UNSPECIFIED"],"name":"name","labels":{"key":"labels"}}}],"initializationActions":[{"executableFile":"executableFile","executionTimeout":"executionTimeout"},{"executableFile":"executableFile","executionTimeout":"executionTimeout"}],"gceClusterConfig":{"networkUri":"networkUri","metadata":{"key":"metadata"},"nodeGroupAffinity":{"nodeGroupUri":"nodeGroupUri"},"shieldedInstanceConfig":{"enableVtpm":True,"enableIntegrityMonitoring":True,"enableSecureBoot":True},"reservationAffinity":{"consumeReservationType":"TYPE_UNSPECIFIED","values":["values","values"],"key":"key"},"subnetworkUri":"subnetworkUri","serviceAccount":"serviceAccount","confidentialInstanceConfig":{"enableConfidentialCompute":True},"privateIpv6GoogleAccess":"PRIVATE_IPV6_GOOGLE_ACCESS_UNSPECIFIED","tags":["tags","tags"],"serviceAccountScopes":["serviceAccountScopes","serviceAccountScopes"],"internalIpOnly":True,"zoneUri":"zoneUri"},"tempBucket":"tempBucket","dataprocMetricConfig":{"metrics":[{"metricSource":"METRIC_SOURCE_UNSPECIFIED","metricOverrides":["metricOverrides","metricOverrides"]},{"metricSource":"METRIC_SOURCE_UNSPECIFIED","metricOverrides":["metricOverrides","metricOverrides"]}]}},"labels":{"key":"labels"}}},"parameters":[{"name":"name","description":"description","fields":["fields","fields"],"validation":{"regex":{"regexes":["regexes","regexes"]},"values":{"values":["values","values"]}}},{"name":"name","description":"description","fields":["fields","fields"],"validation":{"regex":{"regexes":["regexes","regexes"]},"values":{"values":["values","values"]}}}],"version":0,"labels":{"key":"labels"}}
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
        path='/v1/{parent}/workflowTemplates'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dataproc_projects_regions_workflow_templates_delete(client):
    """Test case for dataproc_projects_regions_workflow_templates_delete

    
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
                    ('version', 56)]
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

async def test_dataproc_projects_regions_workflow_templates_get(client):
    """Test case for dataproc_projects_regions_workflow_templates_get

    
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
                    ('version', 56),
                    ('pageSize', 56),
                    ('pageToken', 'page_token_example')]
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

async def test_dataproc_projects_regions_workflow_templates_get_iam_policy(client):
    """Test case for dataproc_projects_regions_workflow_templates_get_iam_policy

    
    """
    body = {"options":{"requestedPolicyVersion":0}}
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
        path='/v1/{resourceget_iam_polic}'.format(resource='resource_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dataproc_projects_regions_workflow_templates_instantiate(client):
    """Test case for dataproc_projects_regions_workflow_templates_instantiate

    
    """
    body = {"requestId":"requestId","parameters":{"key":"parameters"},"version":0}
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
        path='/v1/{nameinstantiat}'.format(name='name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dataproc_projects_regions_workflow_templates_instantiate_inline(client):
    """Test case for dataproc_projects_regions_workflow_templates_instantiate_inline

    
    """
    body = {"encryptionConfig":{"kmsKey":"kmsKey"},"createTime":"createTime","jobs":[{"stepId":"stepId","prerequisiteStepIds":["prerequisiteStepIds","prerequisiteStepIds"],"trinoJob":{"clientTags":["clientTags","clientTags"],"loggingConfig":{"driverLogLevels":{"key":"LEVEL_UNSPECIFIED"}},"continueOnFailure":True,"queryFileUri":"queryFileUri","outputFormat":"outputFormat","properties":{"key":"properties"},"queryList":{"queries":["queries","queries"]}},"prestoJob":{"clientTags":["clientTags","clientTags"],"loggingConfig":{"driverLogLevels":{"key":"LEVEL_UNSPECIFIED"}},"continueOnFailure":True,"queryFileUri":"queryFileUri","outputFormat":"outputFormat","properties":{"key":"properties"},"queryList":{"queries":["queries","queries"]}},"hiveJob":{"scriptVariables":{"key":"scriptVariables"},"continueOnFailure":True,"queryFileUri":"queryFileUri","jarFileUris":["jarFileUris","jarFileUris"],"properties":{"key":"properties"},"queryList":{"queries":["queries","queries"]}},"labels":{"key":"labels"},"hadoopJob":{"args":["args","args"],"mainClass":"mainClass","archiveUris":["archiveUris","archiveUris"],"loggingConfig":{"driverLogLevels":{"key":"LEVEL_UNSPECIFIED"}},"mainJarFileUri":"mainJarFileUri","fileUris":["fileUris","fileUris"],"jarFileUris":["jarFileUris","jarFileUris"],"properties":{"key":"properties"}},"pysparkJob":{"args":["args","args"],"archiveUris":["archiveUris","archiveUris"],"loggingConfig":{"driverLogLevels":{"key":"LEVEL_UNSPECIFIED"}},"mainPythonFileUri":"mainPythonFileUri","fileUris":["fileUris","fileUris"],"jarFileUris":["jarFileUris","jarFileUris"],"properties":{"key":"properties"},"pythonFileUris":["pythonFileUris","pythonFileUris"]},"sparkSqlJob":{"scriptVariables":{"key":"scriptVariables"},"loggingConfig":{"driverLogLevels":{"key":"LEVEL_UNSPECIFIED"}},"queryFileUri":"queryFileUri","jarFileUris":["jarFileUris","jarFileUris"],"properties":{"key":"properties"},"queryList":{"queries":["queries","queries"]}},"flinkJob":{"args":["args","args"],"mainClass":"mainClass","loggingConfig":{"driverLogLevels":{"key":"LEVEL_UNSPECIFIED"}},"mainJarFileUri":"mainJarFileUri","jarFileUris":["jarFileUris","jarFileUris"],"properties":{"key":"properties"},"savepointUri":"savepointUri"},"scheduling":{"maxFailuresTotal":5,"maxFailuresPerHour":1},"sparkRJob":{"args":["args","args"],"mainRFileUri":"mainRFileUri","archiveUris":["archiveUris","archiveUris"],"loggingConfig":{"driverLogLevels":{"key":"LEVEL_UNSPECIFIED"}},"fileUris":["fileUris","fileUris"],"properties":{"key":"properties"}},"pigJob":{"scriptVariables":{"key":"scriptVariables"},"loggingConfig":{"driverLogLevels":{"key":"LEVEL_UNSPECIFIED"}},"continueOnFailure":True,"queryFileUri":"queryFileUri","jarFileUris":["jarFileUris","jarFileUris"],"properties":{"key":"properties"},"queryList":{"queries":["queries","queries"]}},"sparkJob":{"args":["args","args"],"mainClass":"mainClass","archiveUris":["archiveUris","archiveUris"],"loggingConfig":{"driverLogLevels":{"key":"LEVEL_UNSPECIFIED"}},"mainJarFileUri":"mainJarFileUri","fileUris":["fileUris","fileUris"],"jarFileUris":["jarFileUris","jarFileUris"],"properties":{"key":"properties"}}},{"stepId":"stepId","prerequisiteStepIds":["prerequisiteStepIds","prerequisiteStepIds"],"trinoJob":{"clientTags":["clientTags","clientTags"],"loggingConfig":{"driverLogLevels":{"key":"LEVEL_UNSPECIFIED"}},"continueOnFailure":True,"queryFileUri":"queryFileUri","outputFormat":"outputFormat","properties":{"key":"properties"},"queryList":{"queries":["queries","queries"]}},"prestoJob":{"clientTags":["clientTags","clientTags"],"loggingConfig":{"driverLogLevels":{"key":"LEVEL_UNSPECIFIED"}},"continueOnFailure":True,"queryFileUri":"queryFileUri","outputFormat":"outputFormat","properties":{"key":"properties"},"queryList":{"queries":["queries","queries"]}},"hiveJob":{"scriptVariables":{"key":"scriptVariables"},"continueOnFailure":True,"queryFileUri":"queryFileUri","jarFileUris":["jarFileUris","jarFileUris"],"properties":{"key":"properties"},"queryList":{"queries":["queries","queries"]}},"labels":{"key":"labels"},"hadoopJob":{"args":["args","args"],"mainClass":"mainClass","archiveUris":["archiveUris","archiveUris"],"loggingConfig":{"driverLogLevels":{"key":"LEVEL_UNSPECIFIED"}},"mainJarFileUri":"mainJarFileUri","fileUris":["fileUris","fileUris"],"jarFileUris":["jarFileUris","jarFileUris"],"properties":{"key":"properties"}},"pysparkJob":{"args":["args","args"],"archiveUris":["archiveUris","archiveUris"],"loggingConfig":{"driverLogLevels":{"key":"LEVEL_UNSPECIFIED"}},"mainPythonFileUri":"mainPythonFileUri","fileUris":["fileUris","fileUris"],"jarFileUris":["jarFileUris","jarFileUris"],"properties":{"key":"properties"},"pythonFileUris":["pythonFileUris","pythonFileUris"]},"sparkSqlJob":{"scriptVariables":{"key":"scriptVariables"},"loggingConfig":{"driverLogLevels":{"key":"LEVEL_UNSPECIFIED"}},"queryFileUri":"queryFileUri","jarFileUris":["jarFileUris","jarFileUris"],"properties":{"key":"properties"},"queryList":{"queries":["queries","queries"]}},"flinkJob":{"args":["args","args"],"mainClass":"mainClass","loggingConfig":{"driverLogLevels":{"key":"LEVEL_UNSPECIFIED"}},"mainJarFileUri":"mainJarFileUri","jarFileUris":["jarFileUris","jarFileUris"],"properties":{"key":"properties"},"savepointUri":"savepointUri"},"scheduling":{"maxFailuresTotal":5,"maxFailuresPerHour":1},"sparkRJob":{"args":["args","args"],"mainRFileUri":"mainRFileUri","archiveUris":["archiveUris","archiveUris"],"loggingConfig":{"driverLogLevels":{"key":"LEVEL_UNSPECIFIED"}},"fileUris":["fileUris","fileUris"],"properties":{"key":"properties"}},"pigJob":{"scriptVariables":{"key":"scriptVariables"},"loggingConfig":{"driverLogLevels":{"key":"LEVEL_UNSPECIFIED"}},"continueOnFailure":True,"queryFileUri":"queryFileUri","jarFileUris":["jarFileUris","jarFileUris"],"properties":{"key":"properties"},"queryList":{"queries":["queries","queries"]}},"sparkJob":{"args":["args","args"],"mainClass":"mainClass","archiveUris":["archiveUris","archiveUris"],"loggingConfig":{"driverLogLevels":{"key":"LEVEL_UNSPECIFIED"}},"mainJarFileUri":"mainJarFileUri","fileUris":["fileUris","fileUris"],"jarFileUris":["jarFileUris","jarFileUris"],"properties":{"key":"properties"}}}],"dagTimeout":"dagTimeout","name":"name","updateTime":"updateTime","id":"id","placement":{"clusterSelector":{"zone":"zone","clusterLabels":{"key":"clusterLabels"}},"managedCluster":{"clusterName":"clusterName","config":{"encryptionConfig":{"kmsKey":"kmsKey","gcePdKmsKeyName":"gcePdKmsKeyName"},"softwareConfig":{"imageVersion":"imageVersion","optionalComponents":["COMPONENT_UNSPECIFIED","COMPONENT_UNSPECIFIED"],"properties":{"key":"properties"}},"lifecycleConfig":{"autoDeleteTime":"autoDeleteTime","idleStartTime":"idleStartTime","idleDeleteTtl":"idleDeleteTtl","autoDeleteTtl":"autoDeleteTtl"},"configBucket":"configBucket","masterConfig":{"instanceFlexibilityPolicy":{"instanceSelectionResults":[{"vmCount":5,"machineType":"machineType"},{"vmCount":5,"machineType":"machineType"}],"instanceSelectionList":[{"rank":5,"machineTypes":["machineTypes","machineTypes"]},{"rank":5,"machineTypes":["machineTypes","machineTypes"]}]},"minNumInstances":2,"machineTypeUri":"machineTypeUri","isPreemptible":True,"preemptibility":"PREEMPTIBILITY_UNSPECIFIED","managedGroupConfig":{"instanceGroupManagerUri":"instanceGroupManagerUri","instanceGroupManagerName":"instanceGroupManagerName","instanceTemplateName":"instanceTemplateName"},"imageUri":"imageUri","instanceNames":["instanceNames","instanceNames"],"instanceReferences":[{"instanceId":"instanceId","instanceName":"instanceName","publicEciesKey":"publicEciesKey","publicKey":"publicKey"},{"instanceId":"instanceId","instanceName":"instanceName","publicEciesKey":"publicEciesKey","publicKey":"publicKey"}],"minCpuPlatform":"minCpuPlatform","numInstances":7,"diskConfig":{"bootDiskType":"bootDiskType","bootDiskSizeGb":6,"localSsdInterface":"localSsdInterface","numLocalSsds":1},"accelerators":[{"acceleratorTypeUri":"acceleratorTypeUri","acceleratorCount":0},{"acceleratorTypeUri":"acceleratorTypeUri","acceleratorCount":0}],"startupConfig":{"requiredRegistrationFraction":9.301444243932576}},"workerConfig":{"instanceFlexibilityPolicy":{"instanceSelectionResults":[{"vmCount":5,"machineType":"machineType"},{"vmCount":5,"machineType":"machineType"}],"instanceSelectionList":[{"rank":5,"machineTypes":["machineTypes","machineTypes"]},{"rank":5,"machineTypes":["machineTypes","machineTypes"]}]},"minNumInstances":2,"machineTypeUri":"machineTypeUri","isPreemptible":True,"preemptibility":"PREEMPTIBILITY_UNSPECIFIED","managedGroupConfig":{"instanceGroupManagerUri":"instanceGroupManagerUri","instanceGroupManagerName":"instanceGroupManagerName","instanceTemplateName":"instanceTemplateName"},"imageUri":"imageUri","instanceNames":["instanceNames","instanceNames"],"instanceReferences":[{"instanceId":"instanceId","instanceName":"instanceName","publicEciesKey":"publicEciesKey","publicKey":"publicKey"},{"instanceId":"instanceId","instanceName":"instanceName","publicEciesKey":"publicEciesKey","publicKey":"publicKey"}],"minCpuPlatform":"minCpuPlatform","numInstances":7,"diskConfig":{"bootDiskType":"bootDiskType","bootDiskSizeGb":6,"localSsdInterface":"localSsdInterface","numLocalSsds":1},"accelerators":[{"acceleratorTypeUri":"acceleratorTypeUri","acceleratorCount":0},{"acceleratorTypeUri":"acceleratorTypeUri","acceleratorCount":0}],"startupConfig":{"requiredRegistrationFraction":9.301444243932576}},"secondaryWorkerConfig":{"instanceFlexibilityPolicy":{"instanceSelectionResults":[{"vmCount":5,"machineType":"machineType"},{"vmCount":5,"machineType":"machineType"}],"instanceSelectionList":[{"rank":5,"machineTypes":["machineTypes","machineTypes"]},{"rank":5,"machineTypes":["machineTypes","machineTypes"]}]},"minNumInstances":2,"machineTypeUri":"machineTypeUri","isPreemptible":True,"preemptibility":"PREEMPTIBILITY_UNSPECIFIED","managedGroupConfig":{"instanceGroupManagerUri":"instanceGroupManagerUri","instanceGroupManagerName":"instanceGroupManagerName","instanceTemplateName":"instanceTemplateName"},"imageUri":"imageUri","instanceNames":["instanceNames","instanceNames"],"instanceReferences":[{"instanceId":"instanceId","instanceName":"instanceName","publicEciesKey":"publicEciesKey","publicKey":"publicKey"},{"instanceId":"instanceId","instanceName":"instanceName","publicEciesKey":"publicEciesKey","publicKey":"publicKey"}],"minCpuPlatform":"minCpuPlatform","numInstances":7,"diskConfig":{"bootDiskType":"bootDiskType","bootDiskSizeGb":6,"localSsdInterface":"localSsdInterface","numLocalSsds":1},"accelerators":[{"acceleratorTypeUri":"acceleratorTypeUri","acceleratorCount":0},{"acceleratorTypeUri":"acceleratorTypeUri","acceleratorCount":0}],"startupConfig":{"requiredRegistrationFraction":9.301444243932576}},"gkeClusterConfig":{"gkeClusterTarget":"gkeClusterTarget","namespacedGkeDeploymentTarget":{"clusterNamespace":"clusterNamespace","targetGkeCluster":"targetGkeCluster"},"nodePoolTarget":[{"nodePool":"nodePool","nodePoolConfig":{"locations":["locations","locations"],"autoscaling":{"minNodeCount":2,"maxNodeCount":3},"config":{"preemptible":True,"minCpuPlatform":"minCpuPlatform","spot":True,"bootDiskKmsKey":"bootDiskKmsKey","accelerators":[{"acceleratorType":"acceleratorType","acceleratorCount":"acceleratorCount","gpuPartitionSize":"gpuPartitionSize"},{"acceleratorType":"acceleratorType","acceleratorCount":"acceleratorCount","gpuPartitionSize":"gpuPartitionSize"}],"localSsdCount":4,"machineType":"machineType"}},"roles":["ROLE_UNSPECIFIED","ROLE_UNSPECIFIED"]},{"nodePool":"nodePool","nodePoolConfig":{"locations":["locations","locations"],"autoscaling":{"minNodeCount":2,"maxNodeCount":3},"config":{"preemptible":True,"minCpuPlatform":"minCpuPlatform","spot":True,"bootDiskKmsKey":"bootDiskKmsKey","accelerators":[{"acceleratorType":"acceleratorType","acceleratorCount":"acceleratorCount","gpuPartitionSize":"gpuPartitionSize"},{"acceleratorType":"acceleratorType","acceleratorCount":"acceleratorCount","gpuPartitionSize":"gpuPartitionSize"}],"localSsdCount":4,"machineType":"machineType"}},"roles":["ROLE_UNSPECIFIED","ROLE_UNSPECIFIED"]}]},"securityConfig":{"identityConfig":{"userServiceAccountMapping":{"key":"userServiceAccountMapping"}},"kerberosConfig":{"tgtLifetimeHours":7,"keyPasswordUri":"keyPasswordUri","rootPrincipalPasswordUri":"rootPrincipalPasswordUri","kdcDbKeyUri":"kdcDbKeyUri","crossRealmTrustSharedPasswordUri":"crossRealmTrustSharedPasswordUri","keystoreUri":"keystoreUri","truststorePasswordUri":"truststorePasswordUri","crossRealmTrustKdc":"crossRealmTrustKdc","enableKerberos":True,"crossRealmTrustAdminServer":"crossRealmTrustAdminServer","kmsKeyUri":"kmsKeyUri","truststoreUri":"truststoreUri","realm":"realm","crossRealmTrustRealm":"crossRealmTrustRealm","keystorePasswordUri":"keystorePasswordUri"}},"autoscalingConfig":{"policyUri":"policyUri"},"metastoreConfig":{"dataprocMetastoreService":"dataprocMetastoreService"},"endpointConfig":{"httpPorts":{"key":"httpPorts"},"enableHttpPortAccess":True},"auxiliaryNodeGroups":[{"nodeGroupId":"nodeGroupId","nodeGroup":{"nodeGroupConfig":{"instanceFlexibilityPolicy":{"instanceSelectionResults":[{"vmCount":5,"machineType":"machineType"},{"vmCount":5,"machineType":"machineType"}],"instanceSelectionList":[{"rank":5,"machineTypes":["machineTypes","machineTypes"]},{"rank":5,"machineTypes":["machineTypes","machineTypes"]}]},"minNumInstances":2,"machineTypeUri":"machineTypeUri","isPreemptible":True,"preemptibility":"PREEMPTIBILITY_UNSPECIFIED","managedGroupConfig":{"instanceGroupManagerUri":"instanceGroupManagerUri","instanceGroupManagerName":"instanceGroupManagerName","instanceTemplateName":"instanceTemplateName"},"imageUri":"imageUri","instanceNames":["instanceNames","instanceNames"],"instanceReferences":[{"instanceId":"instanceId","instanceName":"instanceName","publicEciesKey":"publicEciesKey","publicKey":"publicKey"},{"instanceId":"instanceId","instanceName":"instanceName","publicEciesKey":"publicEciesKey","publicKey":"publicKey"}],"minCpuPlatform":"minCpuPlatform","numInstances":7,"diskConfig":{"bootDiskType":"bootDiskType","bootDiskSizeGb":6,"localSsdInterface":"localSsdInterface","numLocalSsds":1},"accelerators":[{"acceleratorTypeUri":"acceleratorTypeUri","acceleratorCount":0},{"acceleratorTypeUri":"acceleratorTypeUri","acceleratorCount":0}],"startupConfig":{"requiredRegistrationFraction":9.301444243932576}},"roles":["ROLE_UNSPECIFIED","ROLE_UNSPECIFIED"],"name":"name","labels":{"key":"labels"}}},{"nodeGroupId":"nodeGroupId","nodeGroup":{"nodeGroupConfig":{"instanceFlexibilityPolicy":{"instanceSelectionResults":[{"vmCount":5,"machineType":"machineType"},{"vmCount":5,"machineType":"machineType"}],"instanceSelectionList":[{"rank":5,"machineTypes":["machineTypes","machineTypes"]},{"rank":5,"machineTypes":["machineTypes","machineTypes"]}]},"minNumInstances":2,"machineTypeUri":"machineTypeUri","isPreemptible":True,"preemptibility":"PREEMPTIBILITY_UNSPECIFIED","managedGroupConfig":{"instanceGroupManagerUri":"instanceGroupManagerUri","instanceGroupManagerName":"instanceGroupManagerName","instanceTemplateName":"instanceTemplateName"},"imageUri":"imageUri","instanceNames":["instanceNames","instanceNames"],"instanceReferences":[{"instanceId":"instanceId","instanceName":"instanceName","publicEciesKey":"publicEciesKey","publicKey":"publicKey"},{"instanceId":"instanceId","instanceName":"instanceName","publicEciesKey":"publicEciesKey","publicKey":"publicKey"}],"minCpuPlatform":"minCpuPlatform","numInstances":7,"diskConfig":{"bootDiskType":"bootDiskType","bootDiskSizeGb":6,"localSsdInterface":"localSsdInterface","numLocalSsds":1},"accelerators":[{"acceleratorTypeUri":"acceleratorTypeUri","acceleratorCount":0},{"acceleratorTypeUri":"acceleratorTypeUri","acceleratorCount":0}],"startupConfig":{"requiredRegistrationFraction":9.301444243932576}},"roles":["ROLE_UNSPECIFIED","ROLE_UNSPECIFIED"],"name":"name","labels":{"key":"labels"}}}],"initializationActions":[{"executableFile":"executableFile","executionTimeout":"executionTimeout"},{"executableFile":"executableFile","executionTimeout":"executionTimeout"}],"gceClusterConfig":{"networkUri":"networkUri","metadata":{"key":"metadata"},"nodeGroupAffinity":{"nodeGroupUri":"nodeGroupUri"},"shieldedInstanceConfig":{"enableVtpm":True,"enableIntegrityMonitoring":True,"enableSecureBoot":True},"reservationAffinity":{"consumeReservationType":"TYPE_UNSPECIFIED","values":["values","values"],"key":"key"},"subnetworkUri":"subnetworkUri","serviceAccount":"serviceAccount","confidentialInstanceConfig":{"enableConfidentialCompute":True},"privateIpv6GoogleAccess":"PRIVATE_IPV6_GOOGLE_ACCESS_UNSPECIFIED","tags":["tags","tags"],"serviceAccountScopes":["serviceAccountScopes","serviceAccountScopes"],"internalIpOnly":True,"zoneUri":"zoneUri"},"tempBucket":"tempBucket","dataprocMetricConfig":{"metrics":[{"metricSource":"METRIC_SOURCE_UNSPECIFIED","metricOverrides":["metricOverrides","metricOverrides"]},{"metricSource":"METRIC_SOURCE_UNSPECIFIED","metricOverrides":["metricOverrides","metricOverrides"]}]}},"labels":{"key":"labels"}}},"parameters":[{"name":"name","description":"description","fields":["fields","fields"],"validation":{"regex":{"regexes":["regexes","regexes"]},"values":{"values":["values","values"]}}},{"name":"name","description":"description","fields":["fields","fields"],"validation":{"regex":{"regexes":["regexes","regexes"]},"values":{"values":["values","values"]}}}],"version":0,"labels":{"key":"labels"}}
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
                    ('requestId', 'request_id_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/{parent}/workflowTemplates:instantiateInline'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dataproc_projects_regions_workflow_templates_list(client):
    """Test case for dataproc_projects_regions_workflow_templates_list

    
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
                    ('pageToken', 'page_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/{parent}/workflowTemplates'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dataproc_projects_regions_workflow_templates_set_iam_policy(client):
    """Test case for dataproc_projects_regions_workflow_templates_set_iam_policy

    
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

async def test_dataproc_projects_regions_workflow_templates_test_iam_permissions(client):
    """Test case for dataproc_projects_regions_workflow_templates_test_iam_permissions

    
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

async def test_dataproc_projects_regions_workflow_templates_update(client):
    """Test case for dataproc_projects_regions_workflow_templates_update

    
    """
    body = {"encryptionConfig":{"kmsKey":"kmsKey"},"createTime":"createTime","jobs":[{"stepId":"stepId","prerequisiteStepIds":["prerequisiteStepIds","prerequisiteStepIds"],"trinoJob":{"clientTags":["clientTags","clientTags"],"loggingConfig":{"driverLogLevels":{"key":"LEVEL_UNSPECIFIED"}},"continueOnFailure":True,"queryFileUri":"queryFileUri","outputFormat":"outputFormat","properties":{"key":"properties"},"queryList":{"queries":["queries","queries"]}},"prestoJob":{"clientTags":["clientTags","clientTags"],"loggingConfig":{"driverLogLevels":{"key":"LEVEL_UNSPECIFIED"}},"continueOnFailure":True,"queryFileUri":"queryFileUri","outputFormat":"outputFormat","properties":{"key":"properties"},"queryList":{"queries":["queries","queries"]}},"hiveJob":{"scriptVariables":{"key":"scriptVariables"},"continueOnFailure":True,"queryFileUri":"queryFileUri","jarFileUris":["jarFileUris","jarFileUris"],"properties":{"key":"properties"},"queryList":{"queries":["queries","queries"]}},"labels":{"key":"labels"},"hadoopJob":{"args":["args","args"],"mainClass":"mainClass","archiveUris":["archiveUris","archiveUris"],"loggingConfig":{"driverLogLevels":{"key":"LEVEL_UNSPECIFIED"}},"mainJarFileUri":"mainJarFileUri","fileUris":["fileUris","fileUris"],"jarFileUris":["jarFileUris","jarFileUris"],"properties":{"key":"properties"}},"pysparkJob":{"args":["args","args"],"archiveUris":["archiveUris","archiveUris"],"loggingConfig":{"driverLogLevels":{"key":"LEVEL_UNSPECIFIED"}},"mainPythonFileUri":"mainPythonFileUri","fileUris":["fileUris","fileUris"],"jarFileUris":["jarFileUris","jarFileUris"],"properties":{"key":"properties"},"pythonFileUris":["pythonFileUris","pythonFileUris"]},"sparkSqlJob":{"scriptVariables":{"key":"scriptVariables"},"loggingConfig":{"driverLogLevels":{"key":"LEVEL_UNSPECIFIED"}},"queryFileUri":"queryFileUri","jarFileUris":["jarFileUris","jarFileUris"],"properties":{"key":"properties"},"queryList":{"queries":["queries","queries"]}},"flinkJob":{"args":["args","args"],"mainClass":"mainClass","loggingConfig":{"driverLogLevels":{"key":"LEVEL_UNSPECIFIED"}},"mainJarFileUri":"mainJarFileUri","jarFileUris":["jarFileUris","jarFileUris"],"properties":{"key":"properties"},"savepointUri":"savepointUri"},"scheduling":{"maxFailuresTotal":5,"maxFailuresPerHour":1},"sparkRJob":{"args":["args","args"],"mainRFileUri":"mainRFileUri","archiveUris":["archiveUris","archiveUris"],"loggingConfig":{"driverLogLevels":{"key":"LEVEL_UNSPECIFIED"}},"fileUris":["fileUris","fileUris"],"properties":{"key":"properties"}},"pigJob":{"scriptVariables":{"key":"scriptVariables"},"loggingConfig":{"driverLogLevels":{"key":"LEVEL_UNSPECIFIED"}},"continueOnFailure":True,"queryFileUri":"queryFileUri","jarFileUris":["jarFileUris","jarFileUris"],"properties":{"key":"properties"},"queryList":{"queries":["queries","queries"]}},"sparkJob":{"args":["args","args"],"mainClass":"mainClass","archiveUris":["archiveUris","archiveUris"],"loggingConfig":{"driverLogLevels":{"key":"LEVEL_UNSPECIFIED"}},"mainJarFileUri":"mainJarFileUri","fileUris":["fileUris","fileUris"],"jarFileUris":["jarFileUris","jarFileUris"],"properties":{"key":"properties"}}},{"stepId":"stepId","prerequisiteStepIds":["prerequisiteStepIds","prerequisiteStepIds"],"trinoJob":{"clientTags":["clientTags","clientTags"],"loggingConfig":{"driverLogLevels":{"key":"LEVEL_UNSPECIFIED"}},"continueOnFailure":True,"queryFileUri":"queryFileUri","outputFormat":"outputFormat","properties":{"key":"properties"},"queryList":{"queries":["queries","queries"]}},"prestoJob":{"clientTags":["clientTags","clientTags"],"loggingConfig":{"driverLogLevels":{"key":"LEVEL_UNSPECIFIED"}},"continueOnFailure":True,"queryFileUri":"queryFileUri","outputFormat":"outputFormat","properties":{"key":"properties"},"queryList":{"queries":["queries","queries"]}},"hiveJob":{"scriptVariables":{"key":"scriptVariables"},"continueOnFailure":True,"queryFileUri":"queryFileUri","jarFileUris":["jarFileUris","jarFileUris"],"properties":{"key":"properties"},"queryList":{"queries":["queries","queries"]}},"labels":{"key":"labels"},"hadoopJob":{"args":["args","args"],"mainClass":"mainClass","archiveUris":["archiveUris","archiveUris"],"loggingConfig":{"driverLogLevels":{"key":"LEVEL_UNSPECIFIED"}},"mainJarFileUri":"mainJarFileUri","fileUris":["fileUris","fileUris"],"jarFileUris":["jarFileUris","jarFileUris"],"properties":{"key":"properties"}},"pysparkJob":{"args":["args","args"],"archiveUris":["archiveUris","archiveUris"],"loggingConfig":{"driverLogLevels":{"key":"LEVEL_UNSPECIFIED"}},"mainPythonFileUri":"mainPythonFileUri","fileUris":["fileUris","fileUris"],"jarFileUris":["jarFileUris","jarFileUris"],"properties":{"key":"properties"},"pythonFileUris":["pythonFileUris","pythonFileUris"]},"sparkSqlJob":{"scriptVariables":{"key":"scriptVariables"},"loggingConfig":{"driverLogLevels":{"key":"LEVEL_UNSPECIFIED"}},"queryFileUri":"queryFileUri","jarFileUris":["jarFileUris","jarFileUris"],"properties":{"key":"properties"},"queryList":{"queries":["queries","queries"]}},"flinkJob":{"args":["args","args"],"mainClass":"mainClass","loggingConfig":{"driverLogLevels":{"key":"LEVEL_UNSPECIFIED"}},"mainJarFileUri":"mainJarFileUri","jarFileUris":["jarFileUris","jarFileUris"],"properties":{"key":"properties"},"savepointUri":"savepointUri"},"scheduling":{"maxFailuresTotal":5,"maxFailuresPerHour":1},"sparkRJob":{"args":["args","args"],"mainRFileUri":"mainRFileUri","archiveUris":["archiveUris","archiveUris"],"loggingConfig":{"driverLogLevels":{"key":"LEVEL_UNSPECIFIED"}},"fileUris":["fileUris","fileUris"],"properties":{"key":"properties"}},"pigJob":{"scriptVariables":{"key":"scriptVariables"},"loggingConfig":{"driverLogLevels":{"key":"LEVEL_UNSPECIFIED"}},"continueOnFailure":True,"queryFileUri":"queryFileUri","jarFileUris":["jarFileUris","jarFileUris"],"properties":{"key":"properties"},"queryList":{"queries":["queries","queries"]}},"sparkJob":{"args":["args","args"],"mainClass":"mainClass","archiveUris":["archiveUris","archiveUris"],"loggingConfig":{"driverLogLevels":{"key":"LEVEL_UNSPECIFIED"}},"mainJarFileUri":"mainJarFileUri","fileUris":["fileUris","fileUris"],"jarFileUris":["jarFileUris","jarFileUris"],"properties":{"key":"properties"}}}],"dagTimeout":"dagTimeout","name":"name","updateTime":"updateTime","id":"id","placement":{"clusterSelector":{"zone":"zone","clusterLabels":{"key":"clusterLabels"}},"managedCluster":{"clusterName":"clusterName","config":{"encryptionConfig":{"kmsKey":"kmsKey","gcePdKmsKeyName":"gcePdKmsKeyName"},"softwareConfig":{"imageVersion":"imageVersion","optionalComponents":["COMPONENT_UNSPECIFIED","COMPONENT_UNSPECIFIED"],"properties":{"key":"properties"}},"lifecycleConfig":{"autoDeleteTime":"autoDeleteTime","idleStartTime":"idleStartTime","idleDeleteTtl":"idleDeleteTtl","autoDeleteTtl":"autoDeleteTtl"},"configBucket":"configBucket","masterConfig":{"instanceFlexibilityPolicy":{"instanceSelectionResults":[{"vmCount":5,"machineType":"machineType"},{"vmCount":5,"machineType":"machineType"}],"instanceSelectionList":[{"rank":5,"machineTypes":["machineTypes","machineTypes"]},{"rank":5,"machineTypes":["machineTypes","machineTypes"]}]},"minNumInstances":2,"machineTypeUri":"machineTypeUri","isPreemptible":True,"preemptibility":"PREEMPTIBILITY_UNSPECIFIED","managedGroupConfig":{"instanceGroupManagerUri":"instanceGroupManagerUri","instanceGroupManagerName":"instanceGroupManagerName","instanceTemplateName":"instanceTemplateName"},"imageUri":"imageUri","instanceNames":["instanceNames","instanceNames"],"instanceReferences":[{"instanceId":"instanceId","instanceName":"instanceName","publicEciesKey":"publicEciesKey","publicKey":"publicKey"},{"instanceId":"instanceId","instanceName":"instanceName","publicEciesKey":"publicEciesKey","publicKey":"publicKey"}],"minCpuPlatform":"minCpuPlatform","numInstances":7,"diskConfig":{"bootDiskType":"bootDiskType","bootDiskSizeGb":6,"localSsdInterface":"localSsdInterface","numLocalSsds":1},"accelerators":[{"acceleratorTypeUri":"acceleratorTypeUri","acceleratorCount":0},{"acceleratorTypeUri":"acceleratorTypeUri","acceleratorCount":0}],"startupConfig":{"requiredRegistrationFraction":9.301444243932576}},"workerConfig":{"instanceFlexibilityPolicy":{"instanceSelectionResults":[{"vmCount":5,"machineType":"machineType"},{"vmCount":5,"machineType":"machineType"}],"instanceSelectionList":[{"rank":5,"machineTypes":["machineTypes","machineTypes"]},{"rank":5,"machineTypes":["machineTypes","machineTypes"]}]},"minNumInstances":2,"machineTypeUri":"machineTypeUri","isPreemptible":True,"preemptibility":"PREEMPTIBILITY_UNSPECIFIED","managedGroupConfig":{"instanceGroupManagerUri":"instanceGroupManagerUri","instanceGroupManagerName":"instanceGroupManagerName","instanceTemplateName":"instanceTemplateName"},"imageUri":"imageUri","instanceNames":["instanceNames","instanceNames"],"instanceReferences":[{"instanceId":"instanceId","instanceName":"instanceName","publicEciesKey":"publicEciesKey","publicKey":"publicKey"},{"instanceId":"instanceId","instanceName":"instanceName","publicEciesKey":"publicEciesKey","publicKey":"publicKey"}],"minCpuPlatform":"minCpuPlatform","numInstances":7,"diskConfig":{"bootDiskType":"bootDiskType","bootDiskSizeGb":6,"localSsdInterface":"localSsdInterface","numLocalSsds":1},"accelerators":[{"acceleratorTypeUri":"acceleratorTypeUri","acceleratorCount":0},{"acceleratorTypeUri":"acceleratorTypeUri","acceleratorCount":0}],"startupConfig":{"requiredRegistrationFraction":9.301444243932576}},"secondaryWorkerConfig":{"instanceFlexibilityPolicy":{"instanceSelectionResults":[{"vmCount":5,"machineType":"machineType"},{"vmCount":5,"machineType":"machineType"}],"instanceSelectionList":[{"rank":5,"machineTypes":["machineTypes","machineTypes"]},{"rank":5,"machineTypes":["machineTypes","machineTypes"]}]},"minNumInstances":2,"machineTypeUri":"machineTypeUri","isPreemptible":True,"preemptibility":"PREEMPTIBILITY_UNSPECIFIED","managedGroupConfig":{"instanceGroupManagerUri":"instanceGroupManagerUri","instanceGroupManagerName":"instanceGroupManagerName","instanceTemplateName":"instanceTemplateName"},"imageUri":"imageUri","instanceNames":["instanceNames","instanceNames"],"instanceReferences":[{"instanceId":"instanceId","instanceName":"instanceName","publicEciesKey":"publicEciesKey","publicKey":"publicKey"},{"instanceId":"instanceId","instanceName":"instanceName","publicEciesKey":"publicEciesKey","publicKey":"publicKey"}],"minCpuPlatform":"minCpuPlatform","numInstances":7,"diskConfig":{"bootDiskType":"bootDiskType","bootDiskSizeGb":6,"localSsdInterface":"localSsdInterface","numLocalSsds":1},"accelerators":[{"acceleratorTypeUri":"acceleratorTypeUri","acceleratorCount":0},{"acceleratorTypeUri":"acceleratorTypeUri","acceleratorCount":0}],"startupConfig":{"requiredRegistrationFraction":9.301444243932576}},"gkeClusterConfig":{"gkeClusterTarget":"gkeClusterTarget","namespacedGkeDeploymentTarget":{"clusterNamespace":"clusterNamespace","targetGkeCluster":"targetGkeCluster"},"nodePoolTarget":[{"nodePool":"nodePool","nodePoolConfig":{"locations":["locations","locations"],"autoscaling":{"minNodeCount":2,"maxNodeCount":3},"config":{"preemptible":True,"minCpuPlatform":"minCpuPlatform","spot":True,"bootDiskKmsKey":"bootDiskKmsKey","accelerators":[{"acceleratorType":"acceleratorType","acceleratorCount":"acceleratorCount","gpuPartitionSize":"gpuPartitionSize"},{"acceleratorType":"acceleratorType","acceleratorCount":"acceleratorCount","gpuPartitionSize":"gpuPartitionSize"}],"localSsdCount":4,"machineType":"machineType"}},"roles":["ROLE_UNSPECIFIED","ROLE_UNSPECIFIED"]},{"nodePool":"nodePool","nodePoolConfig":{"locations":["locations","locations"],"autoscaling":{"minNodeCount":2,"maxNodeCount":3},"config":{"preemptible":True,"minCpuPlatform":"minCpuPlatform","spot":True,"bootDiskKmsKey":"bootDiskKmsKey","accelerators":[{"acceleratorType":"acceleratorType","acceleratorCount":"acceleratorCount","gpuPartitionSize":"gpuPartitionSize"},{"acceleratorType":"acceleratorType","acceleratorCount":"acceleratorCount","gpuPartitionSize":"gpuPartitionSize"}],"localSsdCount":4,"machineType":"machineType"}},"roles":["ROLE_UNSPECIFIED","ROLE_UNSPECIFIED"]}]},"securityConfig":{"identityConfig":{"userServiceAccountMapping":{"key":"userServiceAccountMapping"}},"kerberosConfig":{"tgtLifetimeHours":7,"keyPasswordUri":"keyPasswordUri","rootPrincipalPasswordUri":"rootPrincipalPasswordUri","kdcDbKeyUri":"kdcDbKeyUri","crossRealmTrustSharedPasswordUri":"crossRealmTrustSharedPasswordUri","keystoreUri":"keystoreUri","truststorePasswordUri":"truststorePasswordUri","crossRealmTrustKdc":"crossRealmTrustKdc","enableKerberos":True,"crossRealmTrustAdminServer":"crossRealmTrustAdminServer","kmsKeyUri":"kmsKeyUri","truststoreUri":"truststoreUri","realm":"realm","crossRealmTrustRealm":"crossRealmTrustRealm","keystorePasswordUri":"keystorePasswordUri"}},"autoscalingConfig":{"policyUri":"policyUri"},"metastoreConfig":{"dataprocMetastoreService":"dataprocMetastoreService"},"endpointConfig":{"httpPorts":{"key":"httpPorts"},"enableHttpPortAccess":True},"auxiliaryNodeGroups":[{"nodeGroupId":"nodeGroupId","nodeGroup":{"nodeGroupConfig":{"instanceFlexibilityPolicy":{"instanceSelectionResults":[{"vmCount":5,"machineType":"machineType"},{"vmCount":5,"machineType":"machineType"}],"instanceSelectionList":[{"rank":5,"machineTypes":["machineTypes","machineTypes"]},{"rank":5,"machineTypes":["machineTypes","machineTypes"]}]},"minNumInstances":2,"machineTypeUri":"machineTypeUri","isPreemptible":True,"preemptibility":"PREEMPTIBILITY_UNSPECIFIED","managedGroupConfig":{"instanceGroupManagerUri":"instanceGroupManagerUri","instanceGroupManagerName":"instanceGroupManagerName","instanceTemplateName":"instanceTemplateName"},"imageUri":"imageUri","instanceNames":["instanceNames","instanceNames"],"instanceReferences":[{"instanceId":"instanceId","instanceName":"instanceName","publicEciesKey":"publicEciesKey","publicKey":"publicKey"},{"instanceId":"instanceId","instanceName":"instanceName","publicEciesKey":"publicEciesKey","publicKey":"publicKey"}],"minCpuPlatform":"minCpuPlatform","numInstances":7,"diskConfig":{"bootDiskType":"bootDiskType","bootDiskSizeGb":6,"localSsdInterface":"localSsdInterface","numLocalSsds":1},"accelerators":[{"acceleratorTypeUri":"acceleratorTypeUri","acceleratorCount":0},{"acceleratorTypeUri":"acceleratorTypeUri","acceleratorCount":0}],"startupConfig":{"requiredRegistrationFraction":9.301444243932576}},"roles":["ROLE_UNSPECIFIED","ROLE_UNSPECIFIED"],"name":"name","labels":{"key":"labels"}}},{"nodeGroupId":"nodeGroupId","nodeGroup":{"nodeGroupConfig":{"instanceFlexibilityPolicy":{"instanceSelectionResults":[{"vmCount":5,"machineType":"machineType"},{"vmCount":5,"machineType":"machineType"}],"instanceSelectionList":[{"rank":5,"machineTypes":["machineTypes","machineTypes"]},{"rank":5,"machineTypes":["machineTypes","machineTypes"]}]},"minNumInstances":2,"machineTypeUri":"machineTypeUri","isPreemptible":True,"preemptibility":"PREEMPTIBILITY_UNSPECIFIED","managedGroupConfig":{"instanceGroupManagerUri":"instanceGroupManagerUri","instanceGroupManagerName":"instanceGroupManagerName","instanceTemplateName":"instanceTemplateName"},"imageUri":"imageUri","instanceNames":["instanceNames","instanceNames"],"instanceReferences":[{"instanceId":"instanceId","instanceName":"instanceName","publicEciesKey":"publicEciesKey","publicKey":"publicKey"},{"instanceId":"instanceId","instanceName":"instanceName","publicEciesKey":"publicEciesKey","publicKey":"publicKey"}],"minCpuPlatform":"minCpuPlatform","numInstances":7,"diskConfig":{"bootDiskType":"bootDiskType","bootDiskSizeGb":6,"localSsdInterface":"localSsdInterface","numLocalSsds":1},"accelerators":[{"acceleratorTypeUri":"acceleratorTypeUri","acceleratorCount":0},{"acceleratorTypeUri":"acceleratorTypeUri","acceleratorCount":0}],"startupConfig":{"requiredRegistrationFraction":9.301444243932576}},"roles":["ROLE_UNSPECIFIED","ROLE_UNSPECIFIED"],"name":"name","labels":{"key":"labels"}}}],"initializationActions":[{"executableFile":"executableFile","executionTimeout":"executionTimeout"},{"executableFile":"executableFile","executionTimeout":"executionTimeout"}],"gceClusterConfig":{"networkUri":"networkUri","metadata":{"key":"metadata"},"nodeGroupAffinity":{"nodeGroupUri":"nodeGroupUri"},"shieldedInstanceConfig":{"enableVtpm":True,"enableIntegrityMonitoring":True,"enableSecureBoot":True},"reservationAffinity":{"consumeReservationType":"TYPE_UNSPECIFIED","values":["values","values"],"key":"key"},"subnetworkUri":"subnetworkUri","serviceAccount":"serviceAccount","confidentialInstanceConfig":{"enableConfidentialCompute":True},"privateIpv6GoogleAccess":"PRIVATE_IPV6_GOOGLE_ACCESS_UNSPECIFIED","tags":["tags","tags"],"serviceAccountScopes":["serviceAccountScopes","serviceAccountScopes"],"internalIpOnly":True,"zoneUri":"zoneUri"},"tempBucket":"tempBucket","dataprocMetricConfig":{"metrics":[{"metricSource":"METRIC_SOURCE_UNSPECIFIED","metricOverrides":["metricOverrides","metricOverrides"]},{"metricSource":"METRIC_SOURCE_UNSPECIFIED","metricOverrides":["metricOverrides","metricOverrides"]}]}},"labels":{"key":"labels"}}},"parameters":[{"name":"name","description":"description","fields":["fields","fields"],"validation":{"regex":{"regexes":["regexes","regexes"]},"values":{"values":["values","values"]}}},{"name":"name","description":"description","fields":["fields","fields"],"validation":{"regex":{"regexes":["regexes","regexes"]},"values":{"values":["values","values"]}}}],"version":0,"labels":{"key":"labels"}}
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

