# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_cookies_delete_get(client):
    """Test case for cookies_delete_get

    Deletes cookie(s) as provided by the query string and redirects to cookie list.
    """
    params = [('freeform', {'key': 'freeform_example'})]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/cookies/delete',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_cookies_get(client):
    """Test case for cookies_get

    Returns cookie data.
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/cookies',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_cookies_set_get(client):
    """Test case for cookies_set_get

    Sets cookie(s) as provided by the query string and redirects to cookie list.
    """
    params = [('freeform', {'key': 'freeform_example'})]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/cookies/set',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_cookies_set_name_value_get(client):
    """Test case for cookies_set_name_value_get

    Sets a cookie and redirects to cookie list.
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/cookies/set/{name}/{value}'.format(name='name_example', value='value_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

