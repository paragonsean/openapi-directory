# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.get_alert_response import GetAlertResponse


pytestmark = pytest.mark.asyncio

async def test_api_public_v1_alerts_uuid_get(client):
    """Test case for api_public_v1_alerts_uuid_get

    Retrieve alert details.
    """
    headers = { 
        'Accept': 'application/json',
        'x_vo_api_id': 'x_vo_api_id_example',
        'x_vo_api_key': 'x_vo_api_key_example',
    }
    response = await client.request(
        method='GET',
        path='/api-public/v1/alerts/{uuid}'.format(uuid='uuid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

