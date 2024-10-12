# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.quota_by_counter_keys_list_by_service_default_response import QuotaByCounterKeysListByServiceDefaultResponse
from openapi_server.models.quota_counter_contract import QuotaCounterContract
from openapi_server.models.quota_counter_value_contract import QuotaCounterValueContract


pytestmark = pytest.mark.asyncio

async def test_quota_by_period_keys_get(client):
    """Test case for quota_by_period_keys_get

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.ApiManagement/service/{service_name}/quotas/{quota_counter_key}/{quota_period_key}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', service_name='service_name_example', quota_counter_key='quota_counter_key_example', quota_period_key='quota_period_key_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_quota_by_period_keys_update(client):
    """Test case for quota_by_period_keys_update

    
    """
    parameters = {"callsCount":0,"kbTransferred":6.027456183070403}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.ApiManagement/service/{service_name}/quotas/{quota_counter_key}/{quota_period_key}'.format(resource_group_name='resource_group_name_example', service_name='service_name_example', quota_counter_key='quota_counter_key_example', quota_period_key='quota_period_key_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

