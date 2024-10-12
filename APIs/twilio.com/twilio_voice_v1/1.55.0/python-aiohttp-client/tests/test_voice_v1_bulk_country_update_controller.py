# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.voice_v1_dialing_permissions_dialing_permissions_country_bulk_update import VoiceV1DialingPermissionsDialingPermissionsCountryBulkUpdate


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_create_dialing_permissions_country_bulk_update(client):
    """Test case for create_dialing_permissions_country_bulk_update

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    data = {
        'update_request': 'update_request_example'
        }
    response = await client.request(
        method='POST',
        path='/v1/DialingPermissions/BulkCountryUpdates',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

