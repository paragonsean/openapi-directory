# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.ownership import Ownership
from openapi_server.models.ownership_pages import OwnershipPages


pytestmark = pytest.mark.asyncio

async def test_ownership_get(client):
    """Test case for ownership_get

    Returns a paginated list of app licenses
    """
    params = [('query', 'query_example'),
                    ('sort', 'sort_example'),
                    ('pageNumber', 56),
                    ('limit', 56)]
    headers = { 
        'Accept': '*/*',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v2/ownership',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_ownership_install_post(client):
    """Test case for ownership_install_post

    Aquires an app license for a user (installs app)
    """
    params = [('appId', 'app_id_example'),
                    ('userId', 'user_id_example'),
                    ('modelId', 'model_id_example'),
                    ('model', 'model_example'),
                    ('customData', 'custom_data_example')]
    headers = { 
        'Accept': '*/*',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='POST',
        path='/v2/ownership/install',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_ownership_ownership_id_get(client):
    """Test case for ownership_ownership_id_get

    Returns an ownership record
    """
    headers = { 
        'Accept': '*/*',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v2/ownership/{ownership_id}'.format(ownership_id='ownership_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_ownership_ownership_id_patch(client):
    """Test case for ownership_ownership_id_patch

    Updates ownership fields
    """
    params = [('customData', 'custom_data_example'),
                    ('expires', 56)]
    headers = { 
        'Accept': '*/*',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='PATCH',
        path='/v2/ownership/{ownership_id}'.format(ownership_id='ownership_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_ownership_ownership_id_post(client):
    """Test case for ownership_ownership_id_post

    Updates an ownership record
    """
    params = [('customData', 'custom_data_example'),
                    ('expires', 56)]
    headers = { 
        'Accept': '*/*',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='POST',
        path='/v2/ownership/{ownership_id}'.format(ownership_id='ownership_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_ownership_uninstall_ownership_id_post(client):
    """Test case for ownership_uninstall_ownership_id_post

    Uninstalls a license for a particular user and app (uninstalls app)
    """
    params = [('userId', 'user_id_example'),
                    ('cancelOwnership', True),
                    ('customData', 'custom_data_example')]
    headers = { 
        'Accept': '*/*',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='POST',
        path='/v2/ownership/uninstall/{ownership_id}'.format(ownership_id='ownership_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

