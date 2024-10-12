# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.google_cloud_datapipelines_v1_list_jobs_response import GoogleCloudDatapipelinesV1ListJobsResponse
from openapi_server.models.google_cloud_datapipelines_v1_list_pipelines_response import GoogleCloudDatapipelinesV1ListPipelinesResponse
from openapi_server.models.google_cloud_datapipelines_v1_pipeline import GoogleCloudDatapipelinesV1Pipeline
from openapi_server.models.google_cloud_datapipelines_v1_run_pipeline_response import GoogleCloudDatapipelinesV1RunPipelineResponse


pytestmark = pytest.mark.asyncio

async def test_datapipelines_projects_locations_pipelines_create(client):
    """Test case for datapipelines_projects_locations_pipelines_create

    
    """
    body = {"schedulerServiceAccountEmail":"schedulerServiceAccountEmail","createTime":"createTime","scheduleInfo":{"schedule":"schedule","nextJobTime":"nextJobTime","timeZone":"timeZone"},"displayName":"displayName","name":"name","workload":{"dataflowFlexTemplateRequest":{"validateOnly":True,"location":"location","projectId":"projectId","launchParameter":{"jobName":"jobName","launchOptions":{"key":"launchOptions"},"environment":{"additionalUserLabels":{"key":"additionalUserLabels"},"workerRegion":"workerRegion","flexrsGoal":"FLEXRS_UNSPECIFIED","kmsKeyName":"kmsKeyName","network":"network","additionalExperiments":["additionalExperiments","additionalExperiments"],"enableStreamingEngine":True,"tempLocation":"tempLocation","workerZone":"workerZone","maxWorkers":6,"serviceAccountEmail":"serviceAccountEmail","zone":"zone","ipConfiguration":"WORKER_IP_UNSPECIFIED","subnetwork":"subnetwork","numWorkers":1,"machineType":"machineType"},"transformNameMappings":{"key":"transformNameMappings"},"update":True,"containerSpecGcsPath":"containerSpecGcsPath","parameters":{"key":"parameters"}}},"dataflowLaunchTemplateRequest":{"gcsPath":"gcsPath","validateOnly":True,"launchParameters":{"jobName":"jobName","environment":{"additionalUserLabels":{"key":"additionalUserLabels"},"workerRegion":"workerRegion","kmsKeyName":"kmsKeyName","network":"network","additionalExperiments":["additionalExperiments","additionalExperiments"],"enableStreamingEngine":True,"tempLocation":"tempLocation","workerZone":"workerZone","bypassTempDirValidation":True,"maxWorkers":5,"serviceAccountEmail":"serviceAccountEmail","zone":"zone","ipConfiguration":"WORKER_IP_UNSPECIFIED","subnetwork":"subnetwork","numWorkers":5,"machineType":"machineType"},"transformNameMapping":{"key":"transformNameMapping"},"update":True,"parameters":{"key":"parameters"}},"location":"location","projectId":"projectId"}},"pipelineSources":{"key":"pipelineSources"},"state":"STATE_UNSPECIFIED","type":"PIPELINE_TYPE_UNSPECIFIED","jobCount":0,"lastUpdateTime":"lastUpdateTime"}
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
        path='/v1/{parent}/pipelines'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_datapipelines_projects_locations_pipelines_delete(client):
    """Test case for datapipelines_projects_locations_pipelines_delete

    
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
        path='/v1/{name}'.format(name='name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_datapipelines_projects_locations_pipelines_get(client):
    """Test case for datapipelines_projects_locations_pipelines_get

    
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

async def test_datapipelines_projects_locations_pipelines_jobs_list(client):
    """Test case for datapipelines_projects_locations_pipelines_jobs_list

    
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
        path='/v1/{parent}/jobs'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_datapipelines_projects_locations_pipelines_list(client):
    """Test case for datapipelines_projects_locations_pipelines_list

    
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
        path='/v1/{parent}/pipelines'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_datapipelines_projects_locations_pipelines_patch(client):
    """Test case for datapipelines_projects_locations_pipelines_patch

    
    """
    body = {"schedulerServiceAccountEmail":"schedulerServiceAccountEmail","createTime":"createTime","scheduleInfo":{"schedule":"schedule","nextJobTime":"nextJobTime","timeZone":"timeZone"},"displayName":"displayName","name":"name","workload":{"dataflowFlexTemplateRequest":{"validateOnly":True,"location":"location","projectId":"projectId","launchParameter":{"jobName":"jobName","launchOptions":{"key":"launchOptions"},"environment":{"additionalUserLabels":{"key":"additionalUserLabels"},"workerRegion":"workerRegion","flexrsGoal":"FLEXRS_UNSPECIFIED","kmsKeyName":"kmsKeyName","network":"network","additionalExperiments":["additionalExperiments","additionalExperiments"],"enableStreamingEngine":True,"tempLocation":"tempLocation","workerZone":"workerZone","maxWorkers":6,"serviceAccountEmail":"serviceAccountEmail","zone":"zone","ipConfiguration":"WORKER_IP_UNSPECIFIED","subnetwork":"subnetwork","numWorkers":1,"machineType":"machineType"},"transformNameMappings":{"key":"transformNameMappings"},"update":True,"containerSpecGcsPath":"containerSpecGcsPath","parameters":{"key":"parameters"}}},"dataflowLaunchTemplateRequest":{"gcsPath":"gcsPath","validateOnly":True,"launchParameters":{"jobName":"jobName","environment":{"additionalUserLabels":{"key":"additionalUserLabels"},"workerRegion":"workerRegion","kmsKeyName":"kmsKeyName","network":"network","additionalExperiments":["additionalExperiments","additionalExperiments"],"enableStreamingEngine":True,"tempLocation":"tempLocation","workerZone":"workerZone","bypassTempDirValidation":True,"maxWorkers":5,"serviceAccountEmail":"serviceAccountEmail","zone":"zone","ipConfiguration":"WORKER_IP_UNSPECIFIED","subnetwork":"subnetwork","numWorkers":5,"machineType":"machineType"},"transformNameMapping":{"key":"transformNameMapping"},"update":True,"parameters":{"key":"parameters"}},"location":"location","projectId":"projectId"}},"pipelineSources":{"key":"pipelineSources"},"state":"STATE_UNSPECIFIED","type":"PIPELINE_TYPE_UNSPECIFIED","jobCount":0,"lastUpdateTime":"lastUpdateTime"}
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
        path='/v1/{name}'.format(name='name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_datapipelines_projects_locations_pipelines_run(client):
    """Test case for datapipelines_projects_locations_pipelines_run

    
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
        path='/v1/{nameru}'.format(name='name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_datapipelines_projects_locations_pipelines_stop(client):
    """Test case for datapipelines_projects_locations_pipelines_stop

    
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
        path='/v1/{namesto}'.format(name='name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

