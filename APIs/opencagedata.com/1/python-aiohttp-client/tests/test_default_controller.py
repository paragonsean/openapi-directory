# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.response import Response


pytestmark = pytest.mark.asyncio

async def test_vversion_format_get(client):
    """Test case for vversion_format_get

    
    """
    params = [('q', 'q_example'),
                    ('key', 'key_example'),
                    ('abbrv', True),
                    ('address_only', True),
                    ('add_request', True),
                    ('bounds', 'bounds_example'),
                    ('countrycode', 'countrycode_example'),
                    ('jsonp', 'jsonp_example'),
                    ('language', 'language_example'),
                    ('limit', 56),
                    ('min_confidence', 56),
                    ('no_annotations', True),
                    ('no_dedupe', True),
                    ('no_record', True),
                    ('pretty', True),
                    ('proximity', 'proximity_example'),
                    ('roadinfo', True)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/geocode/v{version}/{format}'.format(version=56, format='format_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

