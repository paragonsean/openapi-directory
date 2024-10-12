# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.async_request_status import AsyncRequestStatus


pytestmark = pytest.mark.asyncio

async def test_create_managed_volume_generate_script_job(client):
    """Test case for create_managed_volume_generate_script_job

    Generate and download unified view script
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/managed_volume/snapshot/export/{id}/script'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

