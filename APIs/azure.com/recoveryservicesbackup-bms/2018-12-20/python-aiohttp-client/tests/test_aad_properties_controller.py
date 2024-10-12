# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.aad_properties_resource import AADPropertiesResource


pytestmark = pytest.mark.asyncio

async def test_aad_properties_get(client):
    """Test case for aad_properties_get

    Fetches the AAD properties from target region BCM stamp.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/Subscriptions/{subscription_id}/providers/Microsoft.RecoveryServices/locations/{azure_region}/backupAadProperties/default'.format(azure_region='azure_region_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

