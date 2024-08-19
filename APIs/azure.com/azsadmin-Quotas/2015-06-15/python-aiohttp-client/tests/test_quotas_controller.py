# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.quota import Quota
from openapi_server.models.quota_list import QuotaList


pytestmark = pytest.mark.asyncio

async def test_quotas_get(client):
    """Test case for quotas_get

    
    """
    params = [('api-version', '2015-06-15')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/providers/Microsoft.Network.Admin/locations/{location}/quotas/{resource_name}'.format(subscription_id='subscription_id_example', location='location_example', resource_name='resource_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_quotas_list(client):
    """Test case for quotas_list

    
    """
    params = [('api-version', '2015-06-15'),
                    ('$filter', 'filter_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/providers/Microsoft.Network.Admin/locations/{location}/quotas'.format(subscription_id='subscription_id_example', location='location_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

