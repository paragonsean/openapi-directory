# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.default_payload import DefaultPayload
from openapi_server.models.get_user_projects200_response import GetUserProjects200Response


pytestmark = pytest.mark.asyncio

async def test_get_user_projects(client):
    """Test case for get_user_projects

    List all active projects for the user
    """
    params = [('page', 56),
                    ('size', 56)]
    headers = { 
        'Accept': 'application/json',
        'DjangoRestToken': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/projects/{username}'.format(username='username_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

