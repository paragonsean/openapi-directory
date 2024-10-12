# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.json_setlists import JsonSetlists


pytestmark = pytest.mark.asyncio

async def test_resource10_user_user_id_attended_get_user_attended_setlists_get(client):
    """Test case for resource10_user_user_id_attended_get_user_attended_setlists_get

    .
    """
    params = [('p', 1)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/rest/1.0/user/{user_id}/attended'.format(user_id='user_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

