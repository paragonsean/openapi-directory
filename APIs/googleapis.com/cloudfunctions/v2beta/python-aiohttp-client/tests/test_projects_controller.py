# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.function import Function
from openapi_server.models.generate_download_url_response import GenerateDownloadUrlResponse
from openapi_server.models.generate_upload_url_request import GenerateUploadUrlRequest
from openapi_server.models.generate_upload_url_response import GenerateUploadUrlResponse
from openapi_server.models.list_functions_response import ListFunctionsResponse
from openapi_server.models.list_locations_response import ListLocationsResponse
from openapi_server.models.list_operations_response import ListOperationsResponse
from openapi_server.models.list_runtimes_response import ListRuntimesResponse
from openapi_server.models.operation import Operation
from openapi_server.models.policy import Policy
from openapi_server.models.set_iam_policy_request import SetIamPolicyRequest
from openapi_server.models.test_iam_permissions_request import TestIamPermissionsRequest
from openapi_server.models.test_iam_permissions_response import TestIamPermissionsResponse


pytestmark = pytest.mark.asyncio

async def test_cloudfunctions_projects_locations_functions_abort_function_upgrade(client):
    """Test case for cloudfunctions_projects_locations_functions_abort_function_upgrade

    
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
        path='/v2beta/{nameabort_function_upgrad}'.format(name='name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_cloudfunctions_projects_locations_functions_commit_function_upgrade(client):
    """Test case for cloudfunctions_projects_locations_functions_commit_function_upgrade

    
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
        path='/v2beta/{namecommit_function_upgrad}'.format(name='name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_cloudfunctions_projects_locations_functions_create(client):
    """Test case for cloudfunctions_projects_locations_functions_create

    
    """
    body = {"upgradeInfo":{"buildConfig":{"dockerRepository":"dockerRepository","automaticUpdatePolicy":"{}","runtime":"runtime","sourceToken":"sourceToken","serviceAccount":"serviceAccount","source":{"gitUri":"gitUri","storageSource":{"bucket":"bucket","generation":"generation","object":"object"},"repoSource":{"repoName":"repoName","branchName":"branchName","commitSha":"commitSha","dir":"dir","tagName":"tagName","projectId":"projectId"}},"workerPool":"workerPool","sourceProvenance":{"gitUri":"gitUri","resolvedStorageSource":{"bucket":"bucket","generation":"generation","object":"object"},"resolvedRepoSource":{"repoName":"repoName","branchName":"branchName","commitSha":"commitSha","dir":"dir","tagName":"tagName","projectId":"projectId"}},"build":"build","environmentVariables":{"key":"environmentVariables"},"dockerRegistry":"DOCKER_REGISTRY_UNSPECIFIED","onDeployUpdatePolicy":{"runtimeVersion":"runtimeVersion"},"entryPoint":"entryPoint"},"upgradeState":"UPGRADE_STATE_UNSPECIFIED","serviceConfig":{"maxInstanceRequestConcurrency":6,"allTrafficOnLatestRevision":True,"secretVolumes":[{"mountPath":"mountPath","versions":[{"path":"path","version":"version"},{"path":"path","version":"version"}],"secret":"secret","projectId":"projectId"},{"mountPath":"mountPath","versions":[{"path":"path","version":"version"},{"path":"path","version":"version"}],"secret":"secret","projectId":"projectId"}],"vpcConnector":"vpcConnector","availableCpu":"availableCpu","ingressSettings":"INGRESS_SETTINGS_UNSPECIFIED","uri":"uri","revision":"revision","securityLevel":"SECURITY_LEVEL_UNSPECIFIED","serviceAccountEmail":"serviceAccountEmail","availableMemory":"availableMemory","environmentVariables":{"key":"environmentVariables"},"maxInstanceCount":0,"service":"service","timeoutSeconds":5,"minInstanceCount":1,"secretEnvironmentVariables":[{"secret":"secret","projectId":"projectId","version":"version","key":"key"},{"secret":"secret","projectId":"projectId","version":"version","key":"key"}],"vpcConnectorEgressSettings":"VPC_CONNECTOR_EGRESS_SETTINGS_UNSPECIFIED"},"eventTrigger":{"serviceAccountEmail":"serviceAccountEmail","eventFilters":[{"attribute":"attribute","value":"value","operator":"operator"},{"attribute":"attribute","value":"value","operator":"operator"}],"retryPolicy":"RETRY_POLICY_UNSPECIFIED","service":"service","channel":"channel","eventType":"eventType","trigger":"trigger","triggerRegion":"triggerRegion","pubsubTopic":"pubsubTopic"}},"stateMessages":[{"severity":"SEVERITY_UNSPECIFIED","message":"message","type":"type"},{"severity":"SEVERITY_UNSPECIFIED","message":"message","type":"type"}],"eventTrigger":{"serviceAccountEmail":"serviceAccountEmail","eventFilters":[{"attribute":"attribute","value":"value","operator":"operator"},{"attribute":"attribute","value":"value","operator":"operator"}],"retryPolicy":"RETRY_POLICY_UNSPECIFIED","service":"service","channel":"channel","eventType":"eventType","trigger":"trigger","triggerRegion":"triggerRegion","pubsubTopic":"pubsubTopic"},"description":"description","satisfiesPzs":True,"updateTime":"updateTime","kmsKeyName":"kmsKeyName","url":"url","labels":{"key":"labels"},"buildConfig":{"dockerRepository":"dockerRepository","automaticUpdatePolicy":"{}","runtime":"runtime","sourceToken":"sourceToken","serviceAccount":"serviceAccount","source":{"gitUri":"gitUri","storageSource":{"bucket":"bucket","generation":"generation","object":"object"},"repoSource":{"repoName":"repoName","branchName":"branchName","commitSha":"commitSha","dir":"dir","tagName":"tagName","projectId":"projectId"}},"workerPool":"workerPool","sourceProvenance":{"gitUri":"gitUri","resolvedStorageSource":{"bucket":"bucket","generation":"generation","object":"object"},"resolvedRepoSource":{"repoName":"repoName","branchName":"branchName","commitSha":"commitSha","dir":"dir","tagName":"tagName","projectId":"projectId"}},"build":"build","environmentVariables":{"key":"environmentVariables"},"dockerRegistry":"DOCKER_REGISTRY_UNSPECIFIED","onDeployUpdatePolicy":{"runtimeVersion":"runtimeVersion"},"entryPoint":"entryPoint"},"environment":"ENVIRONMENT_UNSPECIFIED","serviceConfig":{"maxInstanceRequestConcurrency":6,"allTrafficOnLatestRevision":True,"secretVolumes":[{"mountPath":"mountPath","versions":[{"path":"path","version":"version"},{"path":"path","version":"version"}],"secret":"secret","projectId":"projectId"},{"mountPath":"mountPath","versions":[{"path":"path","version":"version"},{"path":"path","version":"version"}],"secret":"secret","projectId":"projectId"}],"vpcConnector":"vpcConnector","availableCpu":"availableCpu","ingressSettings":"INGRESS_SETTINGS_UNSPECIFIED","uri":"uri","revision":"revision","securityLevel":"SECURITY_LEVEL_UNSPECIFIED","serviceAccountEmail":"serviceAccountEmail","availableMemory":"availableMemory","environmentVariables":{"key":"environmentVariables"},"maxInstanceCount":0,"service":"service","timeoutSeconds":5,"minInstanceCount":1,"secretEnvironmentVariables":[{"secret":"secret","projectId":"projectId","version":"version","key":"key"},{"secret":"secret","projectId":"projectId","version":"version","key":"key"}],"vpcConnectorEgressSettings":"VPC_CONNECTOR_EGRESS_SETTINGS_UNSPECIFIED"},"createTime":"createTime","name":"name","state":"STATE_UNSPECIFIED"}
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
                    ('functionId', 'function_id_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v2beta/{parent}/functions'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_cloudfunctions_projects_locations_functions_delete(client):
    """Test case for cloudfunctions_projects_locations_functions_delete

    
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
        path='/v2beta/{name}'.format(name='name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_cloudfunctions_projects_locations_functions_generate_download_url(client):
    """Test case for cloudfunctions_projects_locations_functions_generate_download_url

    
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
        path='/v2beta/{namegenerate_download_ur}'.format(name='name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_cloudfunctions_projects_locations_functions_generate_upload_url(client):
    """Test case for cloudfunctions_projects_locations_functions_generate_upload_url

    
    """
    body = {"environment":"ENVIRONMENT_UNSPECIFIED","kmsKeyName":"kmsKeyName"}
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
        path='/v2beta/{parent}/functions:generateUploadUrl'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_cloudfunctions_projects_locations_functions_get_iam_policy(client):
    """Test case for cloudfunctions_projects_locations_functions_get_iam_policy

    
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
        path='/v2beta/{resourceget_iam_polic}'.format(resource='resource_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_cloudfunctions_projects_locations_functions_list(client):
    """Test case for cloudfunctions_projects_locations_functions_list

    
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
        path='/v2beta/{parent}/functions'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_cloudfunctions_projects_locations_functions_patch(client):
    """Test case for cloudfunctions_projects_locations_functions_patch

    
    """
    body = {"upgradeInfo":{"buildConfig":{"dockerRepository":"dockerRepository","automaticUpdatePolicy":"{}","runtime":"runtime","sourceToken":"sourceToken","serviceAccount":"serviceAccount","source":{"gitUri":"gitUri","storageSource":{"bucket":"bucket","generation":"generation","object":"object"},"repoSource":{"repoName":"repoName","branchName":"branchName","commitSha":"commitSha","dir":"dir","tagName":"tagName","projectId":"projectId"}},"workerPool":"workerPool","sourceProvenance":{"gitUri":"gitUri","resolvedStorageSource":{"bucket":"bucket","generation":"generation","object":"object"},"resolvedRepoSource":{"repoName":"repoName","branchName":"branchName","commitSha":"commitSha","dir":"dir","tagName":"tagName","projectId":"projectId"}},"build":"build","environmentVariables":{"key":"environmentVariables"},"dockerRegistry":"DOCKER_REGISTRY_UNSPECIFIED","onDeployUpdatePolicy":{"runtimeVersion":"runtimeVersion"},"entryPoint":"entryPoint"},"upgradeState":"UPGRADE_STATE_UNSPECIFIED","serviceConfig":{"maxInstanceRequestConcurrency":6,"allTrafficOnLatestRevision":True,"secretVolumes":[{"mountPath":"mountPath","versions":[{"path":"path","version":"version"},{"path":"path","version":"version"}],"secret":"secret","projectId":"projectId"},{"mountPath":"mountPath","versions":[{"path":"path","version":"version"},{"path":"path","version":"version"}],"secret":"secret","projectId":"projectId"}],"vpcConnector":"vpcConnector","availableCpu":"availableCpu","ingressSettings":"INGRESS_SETTINGS_UNSPECIFIED","uri":"uri","revision":"revision","securityLevel":"SECURITY_LEVEL_UNSPECIFIED","serviceAccountEmail":"serviceAccountEmail","availableMemory":"availableMemory","environmentVariables":{"key":"environmentVariables"},"maxInstanceCount":0,"service":"service","timeoutSeconds":5,"minInstanceCount":1,"secretEnvironmentVariables":[{"secret":"secret","projectId":"projectId","version":"version","key":"key"},{"secret":"secret","projectId":"projectId","version":"version","key":"key"}],"vpcConnectorEgressSettings":"VPC_CONNECTOR_EGRESS_SETTINGS_UNSPECIFIED"},"eventTrigger":{"serviceAccountEmail":"serviceAccountEmail","eventFilters":[{"attribute":"attribute","value":"value","operator":"operator"},{"attribute":"attribute","value":"value","operator":"operator"}],"retryPolicy":"RETRY_POLICY_UNSPECIFIED","service":"service","channel":"channel","eventType":"eventType","trigger":"trigger","triggerRegion":"triggerRegion","pubsubTopic":"pubsubTopic"}},"stateMessages":[{"severity":"SEVERITY_UNSPECIFIED","message":"message","type":"type"},{"severity":"SEVERITY_UNSPECIFIED","message":"message","type":"type"}],"eventTrigger":{"serviceAccountEmail":"serviceAccountEmail","eventFilters":[{"attribute":"attribute","value":"value","operator":"operator"},{"attribute":"attribute","value":"value","operator":"operator"}],"retryPolicy":"RETRY_POLICY_UNSPECIFIED","service":"service","channel":"channel","eventType":"eventType","trigger":"trigger","triggerRegion":"triggerRegion","pubsubTopic":"pubsubTopic"},"description":"description","satisfiesPzs":True,"updateTime":"updateTime","kmsKeyName":"kmsKeyName","url":"url","labels":{"key":"labels"},"buildConfig":{"dockerRepository":"dockerRepository","automaticUpdatePolicy":"{}","runtime":"runtime","sourceToken":"sourceToken","serviceAccount":"serviceAccount","source":{"gitUri":"gitUri","storageSource":{"bucket":"bucket","generation":"generation","object":"object"},"repoSource":{"repoName":"repoName","branchName":"branchName","commitSha":"commitSha","dir":"dir","tagName":"tagName","projectId":"projectId"}},"workerPool":"workerPool","sourceProvenance":{"gitUri":"gitUri","resolvedStorageSource":{"bucket":"bucket","generation":"generation","object":"object"},"resolvedRepoSource":{"repoName":"repoName","branchName":"branchName","commitSha":"commitSha","dir":"dir","tagName":"tagName","projectId":"projectId"}},"build":"build","environmentVariables":{"key":"environmentVariables"},"dockerRegistry":"DOCKER_REGISTRY_UNSPECIFIED","onDeployUpdatePolicy":{"runtimeVersion":"runtimeVersion"},"entryPoint":"entryPoint"},"environment":"ENVIRONMENT_UNSPECIFIED","serviceConfig":{"maxInstanceRequestConcurrency":6,"allTrafficOnLatestRevision":True,"secretVolumes":[{"mountPath":"mountPath","versions":[{"path":"path","version":"version"},{"path":"path","version":"version"}],"secret":"secret","projectId":"projectId"},{"mountPath":"mountPath","versions":[{"path":"path","version":"version"},{"path":"path","version":"version"}],"secret":"secret","projectId":"projectId"}],"vpcConnector":"vpcConnector","availableCpu":"availableCpu","ingressSettings":"INGRESS_SETTINGS_UNSPECIFIED","uri":"uri","revision":"revision","securityLevel":"SECURITY_LEVEL_UNSPECIFIED","serviceAccountEmail":"serviceAccountEmail","availableMemory":"availableMemory","environmentVariables":{"key":"environmentVariables"},"maxInstanceCount":0,"service":"service","timeoutSeconds":5,"minInstanceCount":1,"secretEnvironmentVariables":[{"secret":"secret","projectId":"projectId","version":"version","key":"key"},{"secret":"secret","projectId":"projectId","version":"version","key":"key"}],"vpcConnectorEgressSettings":"VPC_CONNECTOR_EGRESS_SETTINGS_UNSPECIFIED"},"createTime":"createTime","name":"name","state":"STATE_UNSPECIFIED"}
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
        path='/v2beta/{name}'.format(name='name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_cloudfunctions_projects_locations_functions_redirect_function_upgrade_traffic(client):
    """Test case for cloudfunctions_projects_locations_functions_redirect_function_upgrade_traffic

    
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
        path='/v2beta/{nameredirect_function_upgrade_traffi}'.format(name='name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_cloudfunctions_projects_locations_functions_rollback_function_upgrade_traffic(client):
    """Test case for cloudfunctions_projects_locations_functions_rollback_function_upgrade_traffic

    
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
        path='/v2beta/{namerollback_function_upgrade_traffi}'.format(name='name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_cloudfunctions_projects_locations_functions_set_iam_policy(client):
    """Test case for cloudfunctions_projects_locations_functions_set_iam_policy

    
    """
    body = {"updateMask":"updateMask","policy":{"bindings":[{"condition":{"expression":"expression","description":"description","location":"location","title":"title"},"role":"role","members":["members","members"]},{"condition":{"expression":"expression","description":"description","location":"location","title":"title"},"role":"role","members":["members","members"]}],"etag":"etag","version":0,"auditConfigs":[{"auditLogConfigs":[{"logType":"LOG_TYPE_UNSPECIFIED","exemptedMembers":["exemptedMembers","exemptedMembers"]},{"logType":"LOG_TYPE_UNSPECIFIED","exemptedMembers":["exemptedMembers","exemptedMembers"]}],"service":"service"},{"auditLogConfigs":[{"logType":"LOG_TYPE_UNSPECIFIED","exemptedMembers":["exemptedMembers","exemptedMembers"]},{"logType":"LOG_TYPE_UNSPECIFIED","exemptedMembers":["exemptedMembers","exemptedMembers"]}],"service":"service"}]}}
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
        path='/v2beta/{resourceset_iam_polic}'.format(resource='resource_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_cloudfunctions_projects_locations_functions_setup_function_upgrade_config(client):
    """Test case for cloudfunctions_projects_locations_functions_setup_function_upgrade_config

    
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
        path='/v2beta/{namesetup_function_upgrade_confi}'.format(name='name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_cloudfunctions_projects_locations_functions_test_iam_permissions(client):
    """Test case for cloudfunctions_projects_locations_functions_test_iam_permissions

    
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
        path='/v2beta/{resourcetest_iam_permission}'.format(resource='resource_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_cloudfunctions_projects_locations_list(client):
    """Test case for cloudfunctions_projects_locations_list

    
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
        path='/v2beta/{name}/locations'.format(name='name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_cloudfunctions_projects_locations_operations_get(client):
    """Test case for cloudfunctions_projects_locations_operations_get

    
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
        path='/v2beta/{name}'.format(name='name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_cloudfunctions_projects_locations_operations_list(client):
    """Test case for cloudfunctions_projects_locations_operations_list

    
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
        path='/v2beta/{name}/operations'.format(name='name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_cloudfunctions_projects_locations_runtimes_list(client):
    """Test case for cloudfunctions_projects_locations_runtimes_list

    
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
                    ('filter', 'filter_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v2beta/{parent}/runtimes'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

