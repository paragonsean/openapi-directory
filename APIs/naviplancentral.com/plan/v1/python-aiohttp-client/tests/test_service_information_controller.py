# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.service_information import ServiceInformation


pytestmark = pytest.mark.asyncio

async def test_service_information_statistics(client):
    """Test case for service_information_statistics

    This resource can be used to check the status of the service.
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/plan/api/ServiceInformation/Statistics',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

