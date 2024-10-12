# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.quota_by_counter_keys_list_default_response import QuotaByCounterKeysListDefaultResponse
from openapi_server.models.quota_counter_collection import QuotaCounterCollection
from openapi_server.models.quota_counter_value_contract_properties import QuotaCounterValueContractProperties


pytestmark = pytest.mark.asyncio

async def test_quota_by_counter_keys_list(client):
    """Test case for quota_by_counter_keys_list

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'apim_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/quotas/{quota_counter_key}'.format(quota_counter_key='quota_counter_key_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_quota_by_counter_keys_update(client):
    """Test case for quota_by_counter_keys_update

    
    """
    parameters = {"callsCount":6,"kbTransferred":1.4658129805029452}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'apim_key': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/quotas/{quota_counter_key}'.format(quota_counter_key='quota_counter_key_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

