# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.replication_eligibility_results import ReplicationEligibilityResults
from openapi_server.models.replication_eligibility_results_collection import ReplicationEligibilityResultsCollection


pytestmark = pytest.mark.asyncio

async def test_replication_eligibility_results_get(client):
    """Test case for replication_eligibility_results_get

    Gets the validation errors in case the VM is unsuitable for protection.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/Subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Compute/virtualMachines/{virtual_machine_name}/providers/Microsoft.RecoveryServices/replicationEligibilityResults/default'.format(resource_group_name='resource_group_name_example', subscription_id='subscription_id_example', virtual_machine_name='virtual_machine_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_replication_eligibility_results_list(client):
    """Test case for replication_eligibility_results_list

    Gets the validation errors in case the VM is unsuitable for protection.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/Subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Compute/virtualMachines/{virtual_machine_name}/providers/Microsoft.RecoveryServices/replicationEligibilityResults'.format(resource_group_name='resource_group_name_example', subscription_id='subscription_id_example', virtual_machine_name='virtual_machine_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

