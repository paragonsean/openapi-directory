# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.label_list_result import LabelListResult


pytestmark = pytest.mark.asyncio

async def test_check_labels(client):
    """Test case for check_labels

    Requests the headers and status of the given resource.
    """
    params = [('name', 'name_example'),
                    ('api-version', 'api_version_example'),
                    ('After', 'after_example'),
                    ('$Select', ['select_example'])]
    headers = { 
        'sync_token': 'sync_token_example',
        'accept_datetime': 'accept_datetime_example',
    }
    response = await client.request(
        method='HEAD',
        path='/labels',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_labels(client):
    """Test case for get_labels

    Gets a list of labels.
    """
    params = [('name', 'name_example'),
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
        path='/labels',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

