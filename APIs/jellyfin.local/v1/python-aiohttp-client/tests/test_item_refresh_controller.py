# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.metadata_refresh_mode import MetadataRefreshMode
from openapi_server.models.problem_details import ProblemDetails


pytestmark = pytest.mark.asyncio

async def test_post(client):
    """Test case for post

    Refreshes metadata for an item.
    """
    params = [('metadataRefreshMode', openapi_server.MetadataRefreshMode()),
                    ('imageRefreshMode', openapi_server.MetadataRefreshMode()),
                    ('replaceAllMetadata', False),
                    ('replaceAllImages', False)]
    headers = { 
        'Accept': 'application/json',
        'CustomAuthentication': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/Items/{item_id}/Refresh'.format(item_id='item_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

