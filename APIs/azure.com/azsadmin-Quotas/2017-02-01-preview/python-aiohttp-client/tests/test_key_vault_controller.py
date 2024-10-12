# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.quota_list import QuotaList


pytestmark = pytest.mark.asyncio

async def test_quotas_list(client):
    """Test case for quotas_list

    
    """
    params = [('api-version', '2017-02-01-preview')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/providers/Microsoft.KeyVault.Admin/locations/{location}/quotas'.format(subscription_id='subscription_id_example', location='location_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

