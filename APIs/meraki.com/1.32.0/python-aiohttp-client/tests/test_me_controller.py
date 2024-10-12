# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.get_administered_identities_me200_response import GetAdministeredIdentitiesMe200Response


pytestmark = pytest.mark.asyncio

async def test_get_administered_identities_me_2(client):
    """Test case for get_administered_identities_me_2

    Returns the identity of the current user.
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/administered/identities/me',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

