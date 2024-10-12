# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.api_error import ApiError
from openapi_server.models.who_is_response import WhoIsResponse


pytestmark = pytest.mark.asyncio

async def test_resolve_who_is_entry_0(client):
    """Test case for resolve_who_is_entry_0

    Resolve owner of id4n
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/whois/{id4n}'.format(id4n='id4n_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

