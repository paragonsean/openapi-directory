# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.api_overview import ApiOverview
from openapi_server.models.meta_root200_response import MetaRoot200Response


pytestmark = pytest.mark.asyncio

async def test_meta_get(client):
    """Test case for meta_get

    Get GitHub Enterprise Server meta information
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/meta',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_meta_get_octocat(client):
    """Test case for meta_get_octocat

    Get Octocat
    """
    params = [('s', 's_example')]
    headers = { 
        'Accept': 'application/octocat-stream',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/octocat',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_meta_get_zen(client):
    """Test case for meta_get_zen

    Get the Zen of GitHub
    """
    headers = { 
        'Accept': 'text/plain',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/zen',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_meta_root(client):
    """Test case for meta_root

    GitHub API Root
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

