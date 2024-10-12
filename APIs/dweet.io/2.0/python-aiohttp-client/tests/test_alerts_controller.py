# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_create_alert_get(client):
    """Test case for create_alert_get

    Create an alert for a thing. A thing must be locked before an alert can be set.
    """
    params = [('key', 'key_example')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/alert/{who}/when/{thing}/{condition}'.format(who='who_example', thing='thing_example', condition='condition_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_alert(client):
    """Test case for get_alert

    Get the alert attached to a thing.
    """
    params = [('key', 'key_example')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/get/alert/for/{thing}'.format(thing='thing_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_remove_alert(client):
    """Test case for remove_alert

    Remove an alert for a thing.
    """
    params = [('key', 'key_example')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/remove/alert/for/{thing}'.format(thing='thing_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

