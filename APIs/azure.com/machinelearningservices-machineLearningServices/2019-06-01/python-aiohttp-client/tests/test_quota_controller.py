# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.list_workspace_quotas import ListWorkspaceQuotas
from openapi_server.models.machine_learning_service_error import MachineLearningServiceError
from openapi_server.models.quota_update_parameters import QuotaUpdateParameters
from openapi_server.models.update_workspace_quotas_result import UpdateWorkspaceQuotasResult


pytestmark = pytest.mark.asyncio

async def test_quotas_list(client):
    """Test case for quotas_list

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/providers/Microsoft.MachineLearningServices/locations/{location}/Quotas'.format(subscription_id='subscription_id_example', location='location_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_quotas_update(client):
    """Test case for quotas_update

    
    """
    parameters = {"value":[{"unit":"Count","limit":0,"id":"id","type":"type"},{"unit":"Count","limit":0,"id":"id","type":"type"}]}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/providers/Microsoft.MachineLearningServices/locations/{location}/updateQuotas'.format(location='location_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

