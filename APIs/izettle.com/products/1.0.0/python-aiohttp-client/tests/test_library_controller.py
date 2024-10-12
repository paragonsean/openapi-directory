# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.library_response import LibraryResponse


pytestmark = pytest.mark.asyncio

async def test_get_library(client):
    """Test case for get_library

    Retrieve the entire library
    """
    params = [('eventLogUuid', 'event_log_uuid_example'),
                    ('limit', 500),
                    ('offset', 'offset_example'),
                    ('all', True)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/organizations/{organization_uuid}/library'.format(organization_uuid='organization_uuid_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

