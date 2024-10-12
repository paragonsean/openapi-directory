# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.bulkexports_v1_export_export_custom_job import BulkexportsV1ExportExportCustomJob
from openapi_server.models.list_export_custom_job_response import ListExportCustomJobResponse


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_create_export_custom_job(client):
    """Test case for create_export_custom_job

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    data = {
        'email': 'email_example',
        'end_day': 'end_day_example',
        'friendly_name': 'friendly_name_example',
        'start_day': 'start_day_example',
        'webhook_method': 'webhook_method_example',
        'webhook_url': 'webhook_url_example'
        }
    response = await client.request(
        method='POST',
        path='/v1/Exports/{resource_type}/Jobs'.format(resource_type='resource_type_example'),
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_export_custom_job(client):
    """Test case for list_export_custom_job

    
    """
    params = [('PageSize', 56),
                    ('Page', 56),
                    ('PageToken', 'page_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v1/Exports/{resource_type}/Jobs'.format(resource_type='resource_type_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

