# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.tde_certificate import TdeCertificate


pytestmark = pytest.mark.asyncio

async def test_tde_certificates_create(client):
    """Test case for tde_certificates_create

    
    """
    parameters = {"properties":{"certPassword":"certPassword","privateBlob":"privateBlob"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Sql/servers/{server_name}/tdeCertificates'.format(resource_group_name='resource_group_name_example', server_name='server_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

