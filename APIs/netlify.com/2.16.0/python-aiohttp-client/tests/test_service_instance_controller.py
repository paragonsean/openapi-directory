# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.service_instance import ServiceInstance


pytestmark = pytest.mark.asyncio

async def test_create_service_instance(client):
    """Test case for create_service_instance

    
    """
    config = None
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/sites/{site_id}/services/{addon}/instances'.format(site_id='site_id_example', addon='addon_example'),
        headers=headers,
        json=config,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_service_instance(client):
    """Test case for delete_service_instance

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v1/sites/{site_id}/services/{addon}/instances/{instance_id}'.format(site_id='site_id_example', addon='addon_example', instance_id='instance_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_service_instances_for_site(client):
    """Test case for list_service_instances_for_site

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/sites/{site_id}/service-instances'.format(site_id='site_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_show_service_instance(client):
    """Test case for show_service_instance

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/sites/{site_id}/services/{addon}/instances/{instance_id}'.format(site_id='site_id_example', addon='addon_example', instance_id='instance_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_service_instance(client):
    """Test case for update_service_instance

    
    """
    config = None
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v1/sites/{site_id}/services/{addon}/instances/{instance_id}'.format(site_id='site_id_example', addon='addon_example', instance_id='instance_id_example'),
        headers=headers,
        json=config,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

