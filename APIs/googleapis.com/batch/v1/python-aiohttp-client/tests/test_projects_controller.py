# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.job import Job
from openapi_server.models.list_jobs_response import ListJobsResponse
from openapi_server.models.list_locations_response import ListLocationsResponse
from openapi_server.models.list_operations_response import ListOperationsResponse
from openapi_server.models.list_tasks_response import ListTasksResponse
from openapi_server.models.operation import Operation
from openapi_server.models.report_agent_state_request import ReportAgentStateRequest
from openapi_server.models.report_agent_state_response import ReportAgentStateResponse


pytestmark = pytest.mark.asyncio

async def test_batch_projects_locations_jobs_create(client):
    """Test case for batch_projects_locations_jobs_create

    
    """
    body = {"logsPolicy":{"cloudLoggingOption":{"useGenericTaskMonitoredResource":True},"logsPath":"logsPath","destination":"DESTINATION_UNSPECIFIED"},"uid":"uid","taskGroups":[{"requireHostsFile":True,"taskCount":"taskCount","taskCountPerNode":"taskCountPerNode","taskEnvironments":[{"encryptedVariables":{"cipherText":"cipherText","keyName":"keyName"},"variables":{"key":"variables"},"secretVariables":{"key":"secretVariables"}},{"encryptedVariables":{"cipherText":"cipherText","keyName":"keyName"},"variables":{"key":"variables"},"secretVariables":{"key":"secretVariables"}}],"parallelism":"parallelism","name":"name","taskSpec":{"environment":{"encryptedVariables":{"cipherText":"cipherText","keyName":"keyName"},"variables":{"key":"variables"},"secretVariables":{"key":"secretVariables"}},"environments":{"key":"environments"},"lifecyclePolicies":[{"actionCondition":{"exitCodes":[6,6]},"action":"ACTION_UNSPECIFIED"},{"actionCondition":{"exitCodes":[6,6]},"action":"ACTION_UNSPECIFIED"}],"volumes":[{"mountPath":"mountPath","gcs":{"remotePath":"remotePath"},"mountOptions":["mountOptions","mountOptions"],"nfs":{"server":"server","remotePath":"remotePath"},"deviceName":"deviceName"},{"mountPath":"mountPath","gcs":{"remotePath":"remotePath"},"mountOptions":["mountOptions","mountOptions"],"nfs":{"server":"server","remotePath":"remotePath"},"deviceName":"deviceName"}],"maxRunDuration":"maxRunDuration","maxRetryCount":1,"computeResource":{"bootDiskMib":"bootDiskMib","cpuMilli":"cpuMilli","memoryMib":"memoryMib"},"runnables":[{"container":{"imageUri":"imageUri","password":"password","enableImageStreaming":True,"entrypoint":"entrypoint","options":"options","volumes":["volumes","volumes"],"blockExternalNetwork":True,"commands":["commands","commands"],"username":"username"},"environment":{"encryptedVariables":{"cipherText":"cipherText","keyName":"keyName"},"variables":{"key":"variables"},"secretVariables":{"key":"secretVariables"}},"barrier":{"name":"name"},"background":True,"displayName":"displayName","alwaysRun":True,"ignoreExitStatus":True,"script":{"path":"path","text":"text"},"timeout":"timeout","labels":{"key":"labels"}},{"container":{"imageUri":"imageUri","password":"password","enableImageStreaming":True,"entrypoint":"entrypoint","options":"options","volumes":["volumes","volumes"],"blockExternalNetwork":True,"commands":["commands","commands"],"username":"username"},"environment":{"encryptedVariables":{"cipherText":"cipherText","keyName":"keyName"},"variables":{"key":"variables"},"secretVariables":{"key":"secretVariables"}},"barrier":{"name":"name"},"background":True,"displayName":"displayName","alwaysRun":True,"ignoreExitStatus":True,"script":{"path":"path","text":"text"},"timeout":"timeout","labels":{"key":"labels"}}]},"runAsNonRoot":True,"permissiveSsh":True,"schedulingPolicy":"SCHEDULING_POLICY_UNSPECIFIED"},{"requireHostsFile":True,"taskCount":"taskCount","taskCountPerNode":"taskCountPerNode","taskEnvironments":[{"encryptedVariables":{"cipherText":"cipherText","keyName":"keyName"},"variables":{"key":"variables"},"secretVariables":{"key":"secretVariables"}},{"encryptedVariables":{"cipherText":"cipherText","keyName":"keyName"},"variables":{"key":"variables"},"secretVariables":{"key":"secretVariables"}}],"parallelism":"parallelism","name":"name","taskSpec":{"environment":{"encryptedVariables":{"cipherText":"cipherText","keyName":"keyName"},"variables":{"key":"variables"},"secretVariables":{"key":"secretVariables"}},"environments":{"key":"environments"},"lifecyclePolicies":[{"actionCondition":{"exitCodes":[6,6]},"action":"ACTION_UNSPECIFIED"},{"actionCondition":{"exitCodes":[6,6]},"action":"ACTION_UNSPECIFIED"}],"volumes":[{"mountPath":"mountPath","gcs":{"remotePath":"remotePath"},"mountOptions":["mountOptions","mountOptions"],"nfs":{"server":"server","remotePath":"remotePath"},"deviceName":"deviceName"},{"mountPath":"mountPath","gcs":{"remotePath":"remotePath"},"mountOptions":["mountOptions","mountOptions"],"nfs":{"server":"server","remotePath":"remotePath"},"deviceName":"deviceName"}],"maxRunDuration":"maxRunDuration","maxRetryCount":1,"computeResource":{"bootDiskMib":"bootDiskMib","cpuMilli":"cpuMilli","memoryMib":"memoryMib"},"runnables":[{"container":{"imageUri":"imageUri","password":"password","enableImageStreaming":True,"entrypoint":"entrypoint","options":"options","volumes":["volumes","volumes"],"blockExternalNetwork":True,"commands":["commands","commands"],"username":"username"},"environment":{"encryptedVariables":{"cipherText":"cipherText","keyName":"keyName"},"variables":{"key":"variables"},"secretVariables":{"key":"secretVariables"}},"barrier":{"name":"name"},"background":True,"displayName":"displayName","alwaysRun":True,"ignoreExitStatus":True,"script":{"path":"path","text":"text"},"timeout":"timeout","labels":{"key":"labels"}},{"container":{"imageUri":"imageUri","password":"password","enableImageStreaming":True,"entrypoint":"entrypoint","options":"options","volumes":["volumes","volumes"],"blockExternalNetwork":True,"commands":["commands","commands"],"username":"username"},"environment":{"encryptedVariables":{"cipherText":"cipherText","keyName":"keyName"},"variables":{"key":"variables"},"secretVariables":{"key":"secretVariables"}},"barrier":{"name":"name"},"background":True,"displayName":"displayName","alwaysRun":True,"ignoreExitStatus":True,"script":{"path":"path","text":"text"},"timeout":"timeout","labels":{"key":"labels"}}]},"runAsNonRoot":True,"permissiveSsh":True,"schedulingPolicy":"SCHEDULING_POLICY_UNSPECIFIED"}],"createTime":"createTime","name":"name","updateTime":"updateTime","priority":"priority","allocationPolicy":{"instances":[{"instanceTemplate":"instanceTemplate","installGpuDrivers":True,"policy":{"disks":[{"existingDisk":"existingDisk","newDisk":{"image":"image","sizeGb":"sizeGb","type":"type","diskInterface":"diskInterface","snapshot":"snapshot"},"deviceName":"deviceName"},{"existingDisk":"existingDisk","newDisk":{"image":"image","sizeGb":"sizeGb","type":"type","diskInterface":"diskInterface","snapshot":"snapshot"},"deviceName":"deviceName"}],"minCpuPlatform":"minCpuPlatform","provisioningModel":"PROVISIONING_MODEL_UNSPECIFIED","accelerators":[{"driverVersion":"driverVersion","count":"count","installGpuDrivers":True,"type":"type"},{"driverVersion":"driverVersion","count":"count","installGpuDrivers":True,"type":"type"}],"reservation":"reservation","bootDisk":{"image":"image","sizeGb":"sizeGb","type":"type","diskInterface":"diskInterface","snapshot":"snapshot"},"machineType":"machineType"}},{"instanceTemplate":"instanceTemplate","installGpuDrivers":True,"policy":{"disks":[{"existingDisk":"existingDisk","newDisk":{"image":"image","sizeGb":"sizeGb","type":"type","diskInterface":"diskInterface","snapshot":"snapshot"},"deviceName":"deviceName"},{"existingDisk":"existingDisk","newDisk":{"image":"image","sizeGb":"sizeGb","type":"type","diskInterface":"diskInterface","snapshot":"snapshot"},"deviceName":"deviceName"}],"minCpuPlatform":"minCpuPlatform","provisioningModel":"PROVISIONING_MODEL_UNSPECIFIED","accelerators":[{"driverVersion":"driverVersion","count":"count","installGpuDrivers":True,"type":"type"},{"driverVersion":"driverVersion","count":"count","installGpuDrivers":True,"type":"type"}],"reservation":"reservation","bootDisk":{"image":"image","sizeGb":"sizeGb","type":"type","diskInterface":"diskInterface","snapshot":"snapshot"},"machineType":"machineType"}}],"location":{"allowedLocations":["allowedLocations","allowedLocations"]},"serviceAccount":{"scopes":["scopes","scopes"],"email":"email"},"placement":{"collocation":"collocation","maxDistance":"maxDistance"},"labels":{"key":"labels"},"network":{"networkInterfaces":[{"noExternalIpAddress":True,"subnetwork":"subnetwork","network":"network"},{"noExternalIpAddress":True,"subnetwork":"subnetwork","network":"network"}]},"tags":["tags","tags"]},"notifications":[{"message":{"newTaskState":"STATE_UNSPECIFIED","type":"TYPE_UNSPECIFIED","newJobState":"STATE_UNSPECIFIED"},"pubsubTopic":"pubsubTopic"},{"message":{"newTaskState":"STATE_UNSPECIFIED","type":"TYPE_UNSPECIFIED","newJobState":"STATE_UNSPECIFIED"},"pubsubTopic":"pubsubTopic"}],"labels":{"key":"labels"},"status":{"runDuration":"runDuration","taskGroups":{"key":{"instances":[{"provisioningModel":"PROVISIONING_MODEL_UNSPECIFIED","taskPack":"taskPack","bootDisk":{"image":"image","sizeGb":"sizeGb","type":"type","diskInterface":"diskInterface","snapshot":"snapshot"},"machineType":"machineType"},{"provisioningModel":"PROVISIONING_MODEL_UNSPECIFIED","taskPack":"taskPack","bootDisk":{"image":"image","sizeGb":"sizeGb","type":"type","diskInterface":"diskInterface","snapshot":"snapshot"},"machineType":"machineType"}],"counts":{"key":"counts"}}},"state":"STATE_UNSPECIFIED","statusEvents":[{"taskState":"STATE_UNSPECIFIED","eventTime":"eventTime","description":"description","taskExecution":{"exitCode":0},"type":"type"},{"taskState":"STATE_UNSPECIFIED","eventTime":"eventTime","description":"description","taskExecution":{"exitCode":0},"type":"type"}]}}
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
                    ('jobId', 'job_id_example'),
                    ('requestId', 'request_id_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/{parent}/jobs'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_batch_projects_locations_jobs_list(client):
    """Test case for batch_projects_locations_jobs_list

    
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
        path='/v1/{parent}/jobs'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_batch_projects_locations_jobs_task_groups_tasks_list(client):
    """Test case for batch_projects_locations_jobs_task_groups_tasks_list

    
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
        path='/v1/{parent}/tasks'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_batch_projects_locations_list(client):
    """Test case for batch_projects_locations_list

    
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

async def test_batch_projects_locations_operations_cancel(client):
    """Test case for batch_projects_locations_operations_cancel

    
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

async def test_batch_projects_locations_operations_delete(client):
    """Test case for batch_projects_locations_operations_delete

    
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
                    ('reason', 'reason_example'),
                    ('requestId', 'request_id_example')]
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

async def test_batch_projects_locations_operations_get(client):
    """Test case for batch_projects_locations_operations_get

    
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
        path='/v1/{name}'.format(name='name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_batch_projects_locations_operations_list(client):
    """Test case for batch_projects_locations_operations_list

    
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

async def test_batch_projects_locations_state_report(client):
    """Test case for batch_projects_locations_state_report

    
    """
    body = {"metadata":{"imageVersion":"imageVersion","creator":"creator","instance":"instance","instanceId":"instanceId","creationTime":"creationTime","instancePreemptionNoticeReceived":True,"zone":"zone","version":"version","osRelease":{"key":"osRelease"}},"agentInfo":{"jobId":"jobId","taskGroupId":"taskGroupId","state":"AGENT_STATE_UNSPECIFIED","tasks":[{"runnable":"runnable","taskId":"taskId","taskStatus":{"state":"STATE_UNSPECIFIED","statusEvents":[{"taskState":"STATE_UNSPECIFIED","eventTime":"eventTime","description":"description","taskExecution":{"exitCode":0},"type":"type"},{"taskState":"STATE_UNSPECIFIED","eventTime":"eventTime","description":"description","taskExecution":{"exitCode":0},"type":"type"}]}},{"runnable":"runnable","taskId":"taskId","taskStatus":{"state":"STATE_UNSPECIFIED","statusEvents":[{"taskState":"STATE_UNSPECIFIED","eventTime":"eventTime","description":"description","taskExecution":{"exitCode":0},"type":"type"},{"taskState":"STATE_UNSPECIFIED","eventTime":"eventTime","description":"description","taskExecution":{"exitCode":0},"type":"type"}]}}],"reportTime":"reportTime"},"agentTimingInfo":{"agentStartupTime":"agentStartupTime","bootTime":"bootTime","scriptStartupTime":"scriptStartupTime"}}
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
        path='/v1/{parent}/state:report'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

