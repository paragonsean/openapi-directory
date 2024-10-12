# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.deployment import Deployment
from openapi_server.models.deployment_extended import DeploymentExtended


pytestmark = pytest.mark.asyncio

async def test_virtual_machines_quick_create(client):
    """Test case for virtual_machines_quick_create

    
    """
    parameters = {"properties":{"mode":"Incremental","templateLink":{"uri":"https://raw.githubusercontent.com/stankovski/azure-rest-api-specs/master/arm-compute/quickstart-templates/vm-simple-linux.json"},"parameters":{"adminUsername":{"value":"value"},"dnsLabelPrefix":{"value":"value"},"osVersion":{"value":"14.04.2-LTS"},"adminPassword":{"value":"value"}}}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourcegroups/{resource_group_name}/providers/Microsoft.Resources/deployments/{deployment_name}'.format(resource_group_name='resource_group_name_example', deployment_name='deployment_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

