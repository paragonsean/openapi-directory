# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.container_logs import ContainerLogs
from openapi_server.models.error_model import ErrorModel


pytestmark = pytest.mark.asyncio

async def test_code_package_get_container_log(client):
    """Test case for code_package_get_container_log

    Gets the logs for the container.
    """
    params = [('api-version', 2018-07-01-preview),
                    ('tail', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.ServiceFabricMesh/applications/{application_name}/services/{service_name}/replicas/{replica_name}/codePackages/{code_package_name}/logs'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', application_name='application_name_example', service_name='service_name_example', replica_name='replica_name_example', code_package_name='code_package_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

