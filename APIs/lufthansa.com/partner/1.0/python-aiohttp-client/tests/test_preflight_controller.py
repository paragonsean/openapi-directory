# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_auto_check_in(client):
    """Test case for auto_check_in

    Auto Check-In
    """
    params = [('emailAddress', 'email_address_example')]
    headers = { 
        'Accept': 'application/json',
        'accept': 'accept_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/v1/preflight/autocheckin/{ticketnumber}'.format(ticketnumber='ticketnumber_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

