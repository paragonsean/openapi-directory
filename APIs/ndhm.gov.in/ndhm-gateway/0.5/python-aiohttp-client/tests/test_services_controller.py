# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.service_profile_response import ServiceProfileResponse


pytestmark = pytest.mark.asyncio

async def test_v05_hi_services_service_id_get(client):
    """Test case for v05_hi_services_service_id_get

    Get bridge service details/profile by the serviceId provided.
    """
    headers = { 
        'Accept': 'application/json',
        'authorization': 'authorization_example',
    }
    response = await client.request(
        method='GET',
        path='/gateway/v0.5/hi-services/{service_id}'.format(service_id='service_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

