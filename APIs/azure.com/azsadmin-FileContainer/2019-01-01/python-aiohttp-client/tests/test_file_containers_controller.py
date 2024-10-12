# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.file_container import FileContainer
from openapi_server.models.file_container_parameters import FileContainerParameters
from openapi_server.models.file_containers_list import FileContainersList


pytestmark = pytest.mark.asyncio

async def test_file_containers_create(client):
    """Test case for file_containers_create

    
    """
    file_container_parameters = {"sourceUri":"sourceUri","postCopyAction":"None"}
    params = [('api-version', '2019-01-01')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/providers/Microsoft.Deployment.Admin/locations/global/fileContainers/{file_container_id}'.format(subscription_id='subscription_id_example', file_container_id='file_container_id_example'),
        headers=headers,
        json=file_container_parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_file_containers_delete(client):
    """Test case for file_containers_delete

    Deletes specified file container.
    """
    params = [('api-version', '2019-01-01')]
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/providers/Microsoft.Deployment.Admin/locations/global/fileContainers/{file_container_id}'.format(subscription_id='subscription_id_example', file_container_id='file_container_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_file_containers_get(client):
    """Test case for file_containers_get

    
    """
    params = [('api-version', '2019-01-01')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/providers/Microsoft.Deployment.Admin/locations/global/fileContainers/{file_container_id}'.format(subscription_id='subscription_id_example', file_container_id='file_container_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_file_containers_list(client):
    """Test case for file_containers_list

    
    """
    params = [('api-version', '2019-01-01')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/providers/Microsoft.Deployment.Admin/locations/global/fileContainers'.format(subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

