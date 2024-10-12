# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.live_website_tracking_parameter import LiveWebsiteTrackingParameter


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_v2_live_website_tracking_parameters_json_post(client):
    """Test case for v2_live_website_tracking_parameters_json_post

    Create an Live Website Tracking Parameter
    """
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'application/x-www-form-urlencoded',
    }
    data = {
        'person_id': 56
        }
    response = await client.request(
        method='POST',
        path='/v2/live_website_tracking_parameters.json',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

