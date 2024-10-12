# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_get_stored_alerts(client):
    """Test case for get_stored_alerts

    Read all the saved alerts for a thing from long term storage.  You can query a maximum of 1 day per request and a granularly of 1 hour.
    """
    params = [('key', 'key_example'),
                    ('date', '_date_example'),
                    ('hour', 'hour_example'),
                    ('responseType', 'response_type_example')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/get/stored/alerts/for/{thing}'.format(thing='thing_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_stored_dweets_for_thing_get(client):
    """Test case for get_stored_dweets_for_thing_get

    Read all the saved dweets for a thing from long term storage.  You can query a maximum of 1 day per request and a granularly of 1 hour.
    """
    params = [('key', 'key_example'),
                    ('date', '_date_example'),
                    ('hour', 'hour_example'),
                    ('responseType', 'response_type_example')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/get/stored/dweets/for/{thing}'.format(thing='thing_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

