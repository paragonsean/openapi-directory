# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.get_user_content_by_date_json200_response import GETUserContentByDateJson200Response
from openapi_server.models.get_user_content_recent_json200_response import GETUserContentRecentJson200Response
from openapi_server.models.get_user_content_url_json200_response import GETUserContentUrlJson200Response
from openapi_server.models.get_user_content_user_json200_response import GETUserContentUserJson200Response


pytestmark = pytest.mark.asyncio

async def test_g_et_user_content_by_date_json(client):
    """Test case for g_et_user_content_by_date_json

    Comments by Date
    """
    params = [('date', '_date_example')]
    headers = { 
        'Accept': 'application/json',
        'api-key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/svc/community/v3/user-content/by-date.json',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_g_et_user_content_recent_json(client):
    """Test case for g_et_user_content_recent_json

    Recent User Comments
    """
    headers = { 
        'Accept': 'application/json',
        'api-key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/svc/community/v3/user-content/recent.json',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_g_et_user_content_url_json(client):
    """Test case for g_et_user_content_url_json

    Comments by URL
    """
    params = [('url', 'url_example')]
    headers = { 
        'Accept': 'application/json',
        'api-key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/svc/community/v3/user-content/url.json',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_g_et_user_content_user_json(client):
    """Test case for g_et_user_content_user_json

    Comments by User
    """
    params = [('userID', 56)]
    headers = { 
        'Accept': 'application/json',
        'api-key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/svc/community/v3/user-content/user.json',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

