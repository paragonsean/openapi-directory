# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_absolute_redirect_nget(client):
    """Test case for absolute_redirect_nget

    Absolutely 302 Redirects n times.
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/absolute-redirect/{n}'.format(n=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_redirect_nget(client):
    """Test case for redirect_nget

    302 Redirects n times.
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/redirect/{n}'.format(n=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_redirect_to_delete(client):
    """Test case for redirect_to_delete

    302/3XX Redirects to the given URL.
    """
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/redirect-to',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_redirect_to_get(client):
    """Test case for redirect_to_get

    302/3XX Redirects to the given URL.
    """
    params = [('url', 'url_example'),
                    ('status_code', 56)]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/redirect-to',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_redirect_to_patch(client):
    """Test case for redirect_to_patch

    302/3XX Redirects to the given URL.
    """
    headers = { 
    }
    response = await client.request(
        method='PATCH',
        path='/redirect-to',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_redirect_to_post(client):
    """Test case for redirect_to_post

    302/3XX Redirects to the given URL.
    """
    headers = { 
        'Content-Type': 'application/x-www-form-urlencoded',
    }
    data = {
        'status_code': 56,
        'url': 'url_example'
        }
    response = await client.request(
        method='POST',
        path='/redirect-to',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_redirect_to_put(client):
    """Test case for redirect_to_put

    302/3XX Redirects to the given URL.
    """
    headers = { 
        'Content-Type': 'application/x-www-form-urlencoded',
    }
    data = {
        'status_code': 56,
        'url': 'url_example'
        }
    response = await client.request(
        method='PUT',
        path='/redirect-to',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_redirect_to_trace(client):
    """Test case for redirect_to_trace

    302/3XX Redirects to the given URL.
    """
    headers = { 
    }
    response = await client.request(
        method='TRACE',
        path='/redirect-to',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_relative_redirect_nget(client):
    """Test case for relative_redirect_nget

    Relatively 302 Redirects n times.
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/relative-redirect/{n}'.format(n=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

