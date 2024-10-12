# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.organizer import Organizer


pytestmark = pytest.mark.asyncio

async def test_get_all_organisers(client):
    """Test case for get_all_organisers

    DEPRECATED: Get Organizers
    """
    headers = { 
        'Accept': 'application/json',
        'authorization': 'authorization_example',
    }
    response = await client.request(
        method='GET',
        path='/G2T/rest/accounts/{account_key}/organizers'.format(account_key=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

