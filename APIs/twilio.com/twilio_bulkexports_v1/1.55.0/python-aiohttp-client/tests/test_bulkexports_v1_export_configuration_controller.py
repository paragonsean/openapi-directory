# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.bulkexports_v1_export_configuration import BulkexportsV1ExportConfiguration


pytestmark = pytest.mark.asyncio

async def test_fetch_export_configuration(client):
    """Test case for fetch_export_configuration

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v1/Exports/{resource_type}/Configuration'.format(resource_type='resource_type_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_update_export_configuration(client):
    """Test case for update_export_configuration

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    data = {
        'enabled': True,
        'webhook_method': 'webhook_method_example',
        'webhook_url': 'webhook_url_example'
        }
    response = await client.request(
        method='POST',
        path='/v1/Exports/{resource_type}/Configuration'.format(resource_type='resource_type_example'),
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

