# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.app_api_wfs_endpoints_wfs_get_values200_response import AppApiWfsEndpointsWFSGetValues200Response


pytestmark = pytest.mark.asyncio

async def test_app_api_wfs_endpoints_wfs_get_values(client):
    """Test case for app_api_wfs_endpoints_wfs_get_values

    Forecast winds, ion and molecular densities, and temperatures in the atmosphere 
    """
    params = [('latitude', 42),
                    ('longitude', 42),
                    ('altitude', 300),
                    ('year', 2020),
                    ('month', 5),
                    ('day', 23),
                    ('hour', 15),
                    ('minute', 10)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/wam-ipe',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

