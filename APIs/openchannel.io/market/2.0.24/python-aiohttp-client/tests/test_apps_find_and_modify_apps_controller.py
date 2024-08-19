# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.app import App
from openapi_server.models.app_pages import AppPages
from openapi_server.models.app_version import AppVersion
from openapi_server.models.search_pages import SearchPages
from openapi_server.models.version_pages import VersionPages


pytestmark = pytest.mark.asyncio

async def test_apps_app_id_delete(client):
    """Test case for apps_app_id_delete

    Removes app and all versions
    """
    params = [('developerId', 'developer_id_example')]
    headers = { 
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='DELETE',
        path='/v2/apps/{app_id}'.format(app_id='app_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_apps_app_id_get(client):
    """Test case for apps_app_id_get

    Returns a single APPROVED or SUSPENDED app
    """
    params = [('userId', 'user_id_example'),
                    ('trackViews', True)]
    headers = { 
        'Accept': '*/*',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v2/apps/{app_id}'.format(app_id='app_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_apps_app_id_live_post(client):
    """Test case for apps_app_id_live_post

    Change the live app to another, previously approved version
    """
    params = [('developerId', 'developer_id_example'),
                    ('version', 'version_example')]
    headers = { 
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='POST',
        path='/v2/apps/{app_id}/live'.format(app_id='app_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_apps_app_id_publish_post(client):
    """Test case for apps_app_id_publish_post

    Publishes the current working version of the app to the marketplace
    """
    params = [('developerId', 'developer_id_example'),
                    ('version', 56),
                    ('autoApprove', True)]
    headers = { 
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='POST',
        path='/v2/apps/{app_id}/publish'.format(app_id='app_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_apps_app_id_versions_version_delete(client):
    """Test case for apps_app_id_versions_version_delete

    Removes AppVersion
    """
    params = [('developerId', 'developer_id_example')]
    headers = { 
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='DELETE',
        path='/v2/apps/{app_id}/versions/{version}'.format(app_id='app_id_example', version='version_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_apps_app_id_versions_version_get(client):
    """Test case for apps_app_id_versions_version_get

    Returns a single AppVersion
    """
    params = [('developerId', 'developer_id_example')]
    headers = { 
        'Accept': '*/*',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v2/apps/{app_id}/versions/{version}'.format(app_id='app_id_example', version=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_apps_app_id_versions_version_patch(client):
    """Test case for apps_app_id_versions_version_patch

    Updates the app fields or creates a new version
    """
    params = [('developerId', 'developer_id_example'),
                    ('name', 'name_example'),
                    ('type', 'type_example'),
                    ('model', 'model_example'),
                    ('customData', 'custom_data_example'),
                    ('attributes', 'attributes_example'),
                    ('restrict', 'restrict_example'),
                    ('allow', 'allow_example'),
                    ('access', 'access_example'),
                    ('approvalRequired', 'approval_required_example')]
    headers = { 
        'Accept': '*/*',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='PATCH',
        path='/v2/apps/{app_id}/versions/{version}'.format(app_id='app_id_example', version='version_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_apps_app_id_versions_version_post(client):
    """Test case for apps_app_id_versions_version_post

    Updates the app or creates a new version
    """
    params = [('developerId', 'developer_id_example'),
                    ('name', 'name_example'),
                    ('type', 'type_example'),
                    ('model', 'model_example'),
                    ('customData', 'custom_data_example'),
                    ('attributes', 'attributes_example'),
                    ('restrict', 'restrict_example'),
                    ('allow', 'allow_example'),
                    ('access', 'access_example'),
                    ('approvalRequired', 'approval_required_example')]
    headers = { 
        'Accept': '*/*',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='POST',
        path='/v2/apps/{app_id}/versions/{version}'.format(app_id='app_id_example', version='version_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_apps_app_id_versions_version_status_post(client):
    """Test case for apps_app_id_versions_version_status_post

    Allows a developer or administrator to change the status of apps
    """
    params = [('developerId', 'developer_id_example'),
                    ('status', 'status_example'),
                    ('modifiedBy', administrator),
                    ('reason', 'reason_example')]
    headers = { 
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='POST',
        path='/v2/apps/{app_id}/versions/{version}/status'.format(app_id='app_id_example', version=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_apps_by_safe_name_safe_name_get(client):
    """Test case for apps_by_safe_name_safe_name_get

    Returns a single APPROVED or SUSPENDED app
    """
    params = [('userId', 'user_id_example'),
                    ('trackViews', True)]
    headers = { 
        'Accept': '*/*',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v2/apps/bySafeName/{safe_name}'.format(safe_name='safe_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_apps_get(client):
    """Test case for apps_get

    Returns a paginated list of APPROVED or SUSPENDED apps
    """
    params = [('query', 'query_example'),
                    ('sort', 'sort_example'),
                    ('pageNumber', 56),
                    ('limit', 56),
                    ('userId', 'user_id_example'),
                    ('isOwner', True)]
    headers = { 
        'Accept': '*/*',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v2/apps',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_apps_post(client):
    """Test case for apps_post

    Adds a new app for this developer
    """
    params = [('developerId', 'developer_id_example'),
                    ('name', 'name_example'),
                    ('type', 'type_example'),
                    ('model', 'model_example'),
                    ('customData', 'custom_data_example'),
                    ('attributes', 'attributes_example'),
                    ('restrict', 'restrict_example'),
                    ('allow', 'allow_example'),
                    ('access', 'access_example')]
    headers = { 
        'Accept': '*/*',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='POST',
        path='/v2/apps',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_apps_text_search_get(client):
    """Test case for apps_text_search_get

    Searches through the text of fields to find APPROVED or SUSPENDED apps
    """
    params = [('query', 'query_example'),
                    ('text', 'text_example'),
                    ('fields', 'fields_example'),
                    ('pageNumber', 56),
                    ('limit', 56),
                    ('userId', 'user_id_example'),
                    ('isOwned', True)]
    headers = { 
        'Accept': '*/*',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v2/apps/textSearch',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_apps_versions_get(client):
    """Test case for apps_versions_get

    Returns a paginated list of AppVersions
    """
    params = [('query', 'query_example'),
                    ('sort', 'sort_example'),
                    ('pageNumber', 56),
                    ('limit', 56),
                    ('developerId', 'developer_id_example')]
    headers = { 
        'Accept': '*/*',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v2/apps/versions',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

