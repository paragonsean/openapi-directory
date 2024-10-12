# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.easee_charger import EaseeCharger


pytestmark = pytest.mark.asyncio

async def test_easee_sessions(client):
    """Test case for easee_sessions

    Returns lastSession info for all easee wallboxes (chargers) given user has access to.
    """
    params = [('username', 'username_example'),
                    ('password', 'password_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2.0/alternative/easee/lastSessions',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

