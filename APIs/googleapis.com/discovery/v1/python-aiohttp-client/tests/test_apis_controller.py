# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.directory_list import DirectoryList
from openapi_server.models.rest_description import RestDescription


pytestmark = pytest.mark.asyncio

async def test_discovery_apis_get_rest(client):
    """Test case for discovery_apis_get_rest

    
    """
    params = [('alt', 'alt_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('userIp', 'user_ip_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/discovery/v1/apis/{api}/{version}/rest'.format(api='api_example', version='version_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_discovery_apis_list(client):
    """Test case for discovery_apis_list

    
    """
    params = [('alt', 'alt_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('userIp', 'user_ip_example'),
                    ('name', 'name_example'),
                    ('preferred', True)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/discovery/v1/apis',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

