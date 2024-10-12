# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.container_host_mapping import ContainerHostMapping


pytestmark = pytest.mark.asyncio

async def test_container_host_mappings_get_container_host_mapping(client):
    """Test case for container_host_mappings_get_container_host_mapping

    Returns container host mapping object for a container host resource ID if an associated controller exists.
    """
    container_host_mapping = {"containerHostResourceId":"containerHostResourceId","mappedControllerResourceId":"mappedControllerResourceId"}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/providers/Microsoft.DevSpaces/locations/{location}/checkContainerHostMapping'.format(location='location_example'),
        headers=headers,
        json=container_host_mapping,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

