# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.group_get_default_response import GroupGetDefaultResponse
from openapi_server.models.group_user_create200_response import GroupUserCreate200Response
from openapi_server.models.group_user_list200_response import GroupUserList200Response


pytestmark = pytest.mark.asyncio

async def test_group_user_create(client):
    """Test case for group_user_create

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'apim_key': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/groups/{group_id}/users/{uid}'.format(group_id='group_id_example', uid='uid_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_group_user_delete(client):
    """Test case for group_user_delete

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'apim_key': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/groups/{group_id}/users/{uid}'.format(group_id='group_id_example', uid='uid_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_group_user_list(client):
    """Test case for group_user_list

    
    """
    params = [('$filter', 'filter_example'),
                    ('$top', 56),
                    ('$skip', 56),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'apim_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/groups/{group_id}/users'.format(group_id='group_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

