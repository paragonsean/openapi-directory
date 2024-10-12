# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.job_definition import JobDefinition
from openapi_server.models.job_history_list_result import JobHistoryListResult
from openapi_server.models.job_list_result import JobListResult


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_jobs_create_or_update(client):
    """Test case for jobs_create_or_update

    
    """
    job = {"name":"name","id":"id","type":"type","properties":{"recurrence":{"schedule":{"hours":[5,5],"monthlyOccurrences":[{"Occurrence":7,"day":"Monday"},{"Occurrence":7,"day":"Monday"}],"weekDays":["Monday","Monday"],"minutes":[5,5],"monthDays":[2,2]},"count":6,"interval":1,"endTime":"2000-01-23T04:56:07.000+00:00","frequency":"Minute"},"action":{"request":{"headers":{"key":"headers"},"method":"method","body":"body","uri":"uri","authentication":{"type":"NotSpecified"}},"serviceBusTopicMessage":{"topicPath":"topicPath"},"retryPolicy":{"retryCount":0,"retryInterval":"retryInterval","retryType":"None"},"serviceBusQueueMessage":{"queueName":"queueName"},"errorAction":{"request":{"headers":{"key":"headers"},"method":"method","body":"body","uri":"uri","authentication":{"type":"NotSpecified"}},"serviceBusTopicMessage":{"topicPath":"topicPath"},"retryPolicy":{"retryCount":0,"retryInterval":"retryInterval","retryType":"None"},"serviceBusQueueMessage":{"queueName":"queueName"},"queueMessage":{"sasToken":"sasToken","queueName":"queueName","message":"message","storageAccount":"storageAccount"},"type":"Http"},"queueMessage":{"sasToken":"sasToken","queueName":"queueName","message":"message","storageAccount":"storageAccount"},"type":"Http"},"startTime":"2000-01-23T04:56:07.000+00:00","state":"Enabled","status":{"nextExecutionTime":"2000-01-23T04:56:07.000+00:00","executionCount":9,"faultedCount":2,"lastExecutionTime":"2000-01-23T04:56:07.000+00:00","failureCount":3}}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Scheduler/jobCollections/{job_collection_name}/jobs/{job_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', job_collection_name='job_collection_name_example', job_name='job_name_example'),
        headers=headers,
        json=job,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_jobs_delete(client):
    """Test case for jobs_delete

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Scheduler/jobCollections/{job_collection_name}/jobs/{job_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', job_collection_name='job_collection_name_example', job_name='job_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_jobs_get(client):
    """Test case for jobs_get

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Scheduler/jobCollections/{job_collection_name}/jobs/{job_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', job_collection_name='job_collection_name_example', job_name='job_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_jobs_list(client):
    """Test case for jobs_list

    
    """
    params = [('api-version', 'api_version_example'),
                    ('$top', 56),
                    ('$skip', 56),
                    ('$filter', 'filter_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Scheduler/jobCollections/{job_collection_name}/jobs'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', job_collection_name='job_collection_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_jobs_list_job_history(client):
    """Test case for jobs_list_job_history

    
    """
    params = [('api-version', 'api_version_example'),
                    ('$top', 56),
                    ('$skip', 56),
                    ('$filter', 'filter_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Scheduler/jobCollections/{job_collection_name}/jobs/{job_name}/history'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', job_collection_name='job_collection_name_example', job_name='job_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_jobs_patch(client):
    """Test case for jobs_patch

    
    """
    job = {"name":"name","id":"id","type":"type","properties":{"recurrence":{"schedule":{"hours":[5,5],"monthlyOccurrences":[{"Occurrence":7,"day":"Monday"},{"Occurrence":7,"day":"Monday"}],"weekDays":["Monday","Monday"],"minutes":[5,5],"monthDays":[2,2]},"count":6,"interval":1,"endTime":"2000-01-23T04:56:07.000+00:00","frequency":"Minute"},"action":{"request":{"headers":{"key":"headers"},"method":"method","body":"body","uri":"uri","authentication":{"type":"NotSpecified"}},"serviceBusTopicMessage":{"topicPath":"topicPath"},"retryPolicy":{"retryCount":0,"retryInterval":"retryInterval","retryType":"None"},"serviceBusQueueMessage":{"queueName":"queueName"},"errorAction":{"request":{"headers":{"key":"headers"},"method":"method","body":"body","uri":"uri","authentication":{"type":"NotSpecified"}},"serviceBusTopicMessage":{"topicPath":"topicPath"},"retryPolicy":{"retryCount":0,"retryInterval":"retryInterval","retryType":"None"},"serviceBusQueueMessage":{"queueName":"queueName"},"queueMessage":{"sasToken":"sasToken","queueName":"queueName","message":"message","storageAccount":"storageAccount"},"type":"Http"},"queueMessage":{"sasToken":"sasToken","queueName":"queueName","message":"message","storageAccount":"storageAccount"},"type":"Http"},"startTime":"2000-01-23T04:56:07.000+00:00","state":"Enabled","status":{"nextExecutionTime":"2000-01-23T04:56:07.000+00:00","executionCount":9,"faultedCount":2,"lastExecutionTime":"2000-01-23T04:56:07.000+00:00","failureCount":3}}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Scheduler/jobCollections/{job_collection_name}/jobs/{job_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', job_collection_name='job_collection_name_example', job_name='job_name_example'),
        headers=headers,
        json=job,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_jobs_run(client):
    """Test case for jobs_run

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Scheduler/jobCollections/{job_collection_name}/jobs/{job_name}/run'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', job_collection_name='job_collection_name_example', job_name='job_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

