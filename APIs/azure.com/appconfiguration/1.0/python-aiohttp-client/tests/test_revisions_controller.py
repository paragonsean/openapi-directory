# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.key_value_list_result import KeyValueListResult


pytestmark = pytest.mark.asyncio

async def test_check_revisions(client):
    """Test case for check_revisions

    Requests the headers and status of the given resource.
    """
    params = [('key', 'key_example'),
                    ('label', 'label_example'),
                    ('api-version', 'api_version_example'),
                    ('After', 'after_example'),
                    ('$Select', ['select_example'])]
    headers = { 
        'sync_token': 'sync_token_example',
        'accept_datetime': 'accept_datetime_example',
    }
    response = await client.request(
        method='HEAD',
        path='/revisions',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_revisions(client):
    """Test case for get_revisions

    Gets a list of key-value revisions.
    """
    params = [('key', 'key_example'),
                    ('label', 'label_example'),
                    ('api-version', 'api_version_example'),
                    ('After', 'after_example'),
                    ('$Select', ['select_example'])]
    headers = { 
        'Accept': 'application/json',
        'sync_token': 'sync_token_example',
        'accept_datetime': 'accept_datetime_example',
    }
    response = await client.request(
        method='GET',
        path='/revisions',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

