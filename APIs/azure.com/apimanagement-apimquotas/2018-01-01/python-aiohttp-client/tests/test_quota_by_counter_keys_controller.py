# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.quota_by_counter_keys_list_by_service_default_response import QuotaByCounterKeysListByServiceDefaultResponse
from openapi_server.models.quota_counter_collection import QuotaCounterCollection
from openapi_server.models.quota_counter_value_contract_properties import QuotaCounterValueContractProperties


pytestmark = pytest.mark.asyncio

async def test_quota_by_counter_keys_list_by_service(client):
    """Test case for quota_by_counter_keys_list_by_service

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.ApiManagement/service/{service_name}/quotas/{quota_counter_key}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', service_name='service_name_example', quota_counter_key='quota_counter_key_example'),
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
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.ApiManagement/service/{service_name}/quotas/{quota_counter_key}'.format(resource_group_name='resource_group_name_example', service_name='service_name_example', quota_counter_key='quota_counter_key_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

