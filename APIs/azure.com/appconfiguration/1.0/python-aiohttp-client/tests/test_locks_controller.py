# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.key_value import KeyValue


pytestmark = pytest.mark.asyncio

async def test_delete_lock(client):
    """Test case for delete_lock

    Unlocks a key-value.
    """
    params = [('label', 'label_example'),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'sync_token': 'sync_token_example',
        'if_match': 'if_match_example',
        'if_none_match': 'if_none_match_example',
    }
    response = await client.request(
        method='DELETE',
        path='/locks/{key}'.format(key='key_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_put_lock(client):
    """Test case for put_lock

    Locks a key-value.
    """
    params = [('label', 'label_example'),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'sync_token': 'sync_token_example',
        'if_match': 'if_match_example',
        'if_none_match': 'if_none_match_example',
    }
    response = await client.request(
        method='PUT',
        path='/locks/{key}'.format(key='key_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

