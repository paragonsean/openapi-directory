# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.bundle_download_entity import BundleDownloadEntity


pytestmark = pytest.mark.asyncio

async def test_get_bundle_downloads(client):
    """Test case for get_bundle_downloads

    List Bundle Downloads
    """
    params = [('cursor', 'cursor_example'),
                    ('per_page', 56),
                    ('sort_by', None),
                    ('filter', None),
                    ('filter_gt', None),
                    ('filter_gteq', None),
                    ('filter_lt', None),
                    ('filter_lteq', None),
                    ('bundle_id', 56),
                    ('bundle_registration_id', 56)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/rest/v1/bundle_downloads',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

