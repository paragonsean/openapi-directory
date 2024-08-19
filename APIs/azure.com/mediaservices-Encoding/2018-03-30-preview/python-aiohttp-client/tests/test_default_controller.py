# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.api_error import ApiError
from openapi_server.models.job import Job
from openapi_server.models.job_collection import JobCollection
from openapi_server.models.transform import Transform
from openapi_server.models.transform_collection import TransformCollection


pytestmark = pytest.mark.asyncio

async def test_jobs_cancel_job(client):
    """Test case for jobs_cancel_job

    Cancel Job
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Media/mediaServices/{account_name}/transforms/{transform_name}/jobs/{job_name}/cancelJob'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', account_name='account_name_example', transform_name='transform_name_example', job_name='job_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_jobs_create(client):
    """Test case for jobs_create

    Create Job
    """
    parameters = {"properties":{"outputs":[{"@odata.type":"@odata.type","progress":0,"state":"Canceled","error":{"code":"ServiceError","details":[{"code":"code","message":"message"},{"code":"code","message":"message"}],"category":"Service","message":"message","retry":"DoNotRetry"}},{"@odata.type":"@odata.type","progress":0,"state":"Canceled","error":{"code":"ServiceError","details":[{"code":"code","message":"message"},{"code":"code","message":"message"}],"category":"Service","message":"message","retry":"DoNotRetry"}}],"input":{"@odata.type":"@odata.type","label":"label"},"created":"2000-01-23T04:56:07.000+00:00","description":"description","lastModified":"2000-01-23T04:56:07.000+00:00","state":"Canceled","priority":"Low"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Media/mediaServices/{account_name}/transforms/{transform_name}/jobs/{job_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', account_name='account_name_example', transform_name='transform_name_example', job_name='job_name_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_jobs_delete(client):
    """Test case for jobs_delete

    Delete Job
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Media/mediaServices/{account_name}/transforms/{transform_name}/jobs/{job_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', account_name='account_name_example', transform_name='transform_name_example', job_name='job_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_jobs_get(client):
    """Test case for jobs_get

    Get Job
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Media/mediaServices/{account_name}/transforms/{transform_name}/jobs/{job_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', account_name='account_name_example', transform_name='transform_name_example', job_name='job_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_jobs_list(client):
    """Test case for jobs_list

    List Jobs
    """
    params = [('api-version', 'api_version_example'),
                    ('$filter', 'filter_example'),
                    ('$top', 56),
                    ('$skip', 56)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Media/mediaServices/{account_name}/transforms/{transform_name}/jobs'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', account_name='account_name_example', transform_name='transform_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_transforms_create_or_update(client):
    """Test case for transforms_create_or_update

    Create or Update Transform
    """
    parameters = {"properties":{"outputs":[{"onError":"StopProcessingJob","relativePriority":"Low","preset":{"@odata.type":"@odata.type"}},{"onError":"StopProcessingJob","relativePriority":"Low","preset":{"@odata.type":"@odata.type"}}],"created":"2000-01-23T04:56:07.000+00:00","description":"description","lastModified":"2000-01-23T04:56:07.000+00:00"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Media/mediaServices/{account_name}/transforms/{transform_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', account_name='account_name_example', transform_name='transform_name_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_transforms_delete(client):
    """Test case for transforms_delete

    Delete Transform
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Media/mediaServices/{account_name}/transforms/{transform_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', account_name='account_name_example', transform_name='transform_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_transforms_get(client):
    """Test case for transforms_get

    Get Transform
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Media/mediaServices/{account_name}/transforms/{transform_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', account_name='account_name_example', transform_name='transform_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_transforms_list(client):
    """Test case for transforms_list

    List Transforms
    """
    params = [('api-version', 'api_version_example'),
                    ('$filter', 'filter_example'),
                    ('$top', 56),
                    ('$skip', 56)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Media/mediaServices/{account_name}/transforms'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', account_name='account_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_transforms_update(client):
    """Test case for transforms_update

    Update Transform
    """
    parameters = {"properties":{"outputs":[{"onError":"StopProcessingJob","relativePriority":"Low","preset":{"@odata.type":"@odata.type"}},{"onError":"StopProcessingJob","relativePriority":"Low","preset":{"@odata.type":"@odata.type"}}],"created":"2000-01-23T04:56:07.000+00:00","description":"description","lastModified":"2000-01-23T04:56:07.000+00:00"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PATCH',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Media/mediaServices/{account_name}/transforms/{transform_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', account_name='account_name_example', transform_name='transform_name_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

