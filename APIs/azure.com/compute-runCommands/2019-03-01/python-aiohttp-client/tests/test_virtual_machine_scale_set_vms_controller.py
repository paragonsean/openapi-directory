# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.run_command_input import RunCommandInput
from openapi_server.models.run_command_result import RunCommandResult


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_virtual_machine_scale_set_vms_run_command(client):
    """Test case for virtual_machine_scale_set_vms_run_command

    
    """
    parameters = {"commandId":"commandId","parameters":[{"name":"name","value":"value"},{"name":"name","value":"value"}],"script":["script","script"]}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Compute/virtualMachineScaleSets/{vm_scale_set_name}/virtualmachines/{instance_id}/runCommand'.format(resource_group_name='resource_group_name_example', vm_scale_set_name='vm_scale_set_name_example', instance_id='instance_id_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

