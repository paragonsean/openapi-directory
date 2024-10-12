# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_crr_operation_results_get(client):
    """Test case for crr_operation_results_get

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/Subscriptions/{subscription_id}/providers/Microsoft.RecoveryServices/locations/{azure_region}/backupCrrOperationResults/{operation_id}'.format(azure_region='azure_region_example', subscription_id='subscription_id_example', operation_id='operation_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

