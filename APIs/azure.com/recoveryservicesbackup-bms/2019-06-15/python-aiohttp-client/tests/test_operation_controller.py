# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.validate_operation_request import ValidateOperationRequest
from openapi_server.models.validate_operations_response import ValidateOperationsResponse


pytestmark = pytest.mark.asyncio

async def test_operation_validate(client):
    """Test case for operation_validate

    
    """
    parameters = {"objectType":"objectType"}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/Subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.RecoveryServices/vaults/{vault_name}/backupValidateOperation'.format(vault_name='vault_name_example', resource_group_name='resource_group_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

