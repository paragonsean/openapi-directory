# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.container_logs import ContainerLogs
from openapi_server.models.fabric_error import FabricError


pytestmark = pytest.mark.asyncio

async def test_mesh_code_package_get_container_logs(client):
    """Test case for mesh_code_package_get_container_logs

    Gets the logs from the container.
    """
    params = [('api-version', 6.4-preview),
                    ('Tail', 'tail_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/Resources/Applications/{application_resource_name}/Services/{service_resource_name}/Replicas/{replica_name}/CodePackages/{code_package_name}/Logs'.format(application_resource_name='application_resource_name_example', service_resource_name='service_resource_name_example', replica_name='replica_name_example', code_package_name='code_package_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

