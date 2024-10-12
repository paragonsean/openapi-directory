# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.creator_roles_list200_response import CreatorRolesList200Response


pytestmark = pytest.mark.asyncio

async def test_creator_roles_list(client):
    """Test case for creator_roles_list

    Get a list of creator positions (jobs).
    """
    params = [('page', 56),
                    ('page_size', 56)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/creator-roles',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

