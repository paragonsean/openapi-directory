# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_job_operation_results_get(client):
    """Test case for job_operation_results_get

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/Subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.RecoveryServices/vaults/{vault_name}/backupJobs/{job_name}/operationResults/{operation_id}'.format(vault_name='vault_name_example', resource_group_name='resource_group_name_example', subscription_id='subscription_id_example', job_name='job_name_example', operation_id='operation_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

