# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.key_list_result import KeyListResult


pytestmark = pytest.mark.asyncio

async def test_check_keys(client):
    """Test case for check_keys

    Requests the headers and status of the given resource.
    """
    params = [('name', 'name_example'),
                    ('api-version', 'api_version_example'),
                    ('After', 'after_example')]
    headers = { 
        'sync_token': 'sync_token_example',
        'accept_datetime': 'accept_datetime_example',
    }
    response = await client.request(
        method='HEAD',
        path='/keys',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_keys(client):
    """Test case for get_keys

    Gets a list of keys.
    """
    params = [('name', 'name_example'),
                    ('api-version', 'api_version_example'),
                    ('After', 'after_example')]
    headers = { 
        'Accept': 'application/json',
        'sync_token': 'sync_token_example',
        'accept_datetime': 'accept_datetime_example',
    }
    response = await client.request(
        method='GET',
        path='/keys',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

