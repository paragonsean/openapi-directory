# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_status_codes_delete(client):
    """Test case for status_codes_delete

    Return status code or random status code if more than one are given
    """
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/status/{codes}'.format(codes='codes_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_status_codes_get(client):
    """Test case for status_codes_get

    Return status code or random status code if more than one are given
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/status/{codes}'.format(codes='codes_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_status_codes_patch(client):
    """Test case for status_codes_patch

    Return status code or random status code if more than one are given
    """
    headers = { 
    }
    response = await client.request(
        method='PATCH',
        path='/status/{codes}'.format(codes='codes_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_status_codes_post(client):
    """Test case for status_codes_post

    Return status code or random status code if more than one are given
    """
    headers = { 
    }
    response = await client.request(
        method='POST',
        path='/status/{codes}'.format(codes='codes_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_status_codes_put(client):
    """Test case for status_codes_put

    Return status code or random status code if more than one are given
    """
    headers = { 
    }
    response = await client.request(
        method='PUT',
        path='/status/{codes}'.format(codes='codes_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_status_codes_trace(client):
    """Test case for status_codes_trace

    Return status code or random status code if more than one are given
    """
    headers = { 
    }
    response = await client.request(
        method='TRACE',
        path='/status/{codes}'.format(codes='codes_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

