# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.key_value import KeyValue
from openapi_server.models.key_value_list_result import KeyValueListResult


pytestmark = pytest.mark.asyncio

async def test_check_key_value(client):
    """Test case for check_key_value

    Requests the headers and status of the given resource.
    """
    params = [('label', 'label_example'),
                    ('api-version', 'api_version_example'),
                    ('$Select', ['select_example'])]
    headers = { 
        'sync_token': 'sync_token_example',
        'accept_datetime': 'accept_datetime_example',
        'if_match': 'if_match_example',
        'if_none_match': 'if_none_match_example',
    }
    response = await client.request(
        method='HEAD',
        path='/kv/{key}'.format(key='key_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_check_key_values(client):
    """Test case for check_key_values

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
        path='/kv',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_key_value(client):
    """Test case for delete_key_value

    Deletes a key-value.
    """
    params = [('label', 'label_example'),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'sync_token': 'sync_token_example',
        'if_match': 'if_match_example',
    }
    response = await client.request(
        method='DELETE',
        path='/kv/{key}'.format(key='key_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_key_value(client):
    """Test case for get_key_value

    Gets a single key-value.
    """
    params = [('label', 'label_example'),
                    ('api-version', 'api_version_example'),
                    ('$Select', ['select_example'])]
    headers = { 
        'Accept': 'application/json',
        'sync_token': 'sync_token_example',
        'accept_datetime': 'accept_datetime_example',
        'if_match': 'if_match_example',
        'if_none_match': 'if_none_match_example',
    }
    response = await client.request(
        method='GET',
        path='/kv/{key}'.format(key='key_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_key_values(client):
    """Test case for get_key_values

    Gets a list of key-values.
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
        path='/kv',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_put_key_value(client):
    """Test case for put_key_value

    Creates a key-value.
    """
    entity = {"content_type":"content_type","etag":"etag","label":"label","locked":True,"last_modified":"2000-01-23T04:56:07.000+00:00","value":"value","key":"key","tags":{"key":"tags"}}
    params = [('label', 'label_example'),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/vnd.microsoft.appconfig.kv+json',
        'sync_token': 'sync_token_example',
        'if_match': 'if_match_example',
        'if_none_match': 'if_none_match_example',
    }
    response = await client.request(
        method='PUT',
        path='/kv/{key}'.format(key='key_example'),
        headers=headers,
        json=entity,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

