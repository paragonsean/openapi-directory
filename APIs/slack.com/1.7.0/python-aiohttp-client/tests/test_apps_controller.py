# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.api_permissions_scopes_list_success_schema import ApiPermissionsScopesListSuccessSchema
from openapi_server.models.apps_permissions_info_error_schema import AppsPermissionsInfoErrorSchema
from openapi_server.models.apps_permissions_info_schema import AppsPermissionsInfoSchema
from openapi_server.models.apps_permissions_request_error_schema import AppsPermissionsRequestErrorSchema
from openapi_server.models.apps_permissions_request_schema import AppsPermissionsRequestSchema
from openapi_server.models.apps_permissions_resources_list_error_schema import AppsPermissionsResourcesListErrorSchema
from openapi_server.models.apps_permissions_resources_list_success_schema import AppsPermissionsResourcesListSuccessSchema
from openapi_server.models.apps_permissions_scopes_list_error_schema import AppsPermissionsScopesListErrorSchema
from openapi_server.models.apps_uninstall_error_schema import AppsUninstallErrorSchema
from openapi_server.models.apps_uninstall_schema import AppsUninstallSchema
from openapi_server.models.default_error_template import DefaultErrorTemplate
from openapi_server.models.default_success_template import DefaultSuccessTemplate


pytestmark = pytest.mark.asyncio

async def test_apps_event_authorizations_list_0(client):
    """Test case for apps_event_authorizations_list_0

    
    """
    params = [('event_context', 'event_context_example'),
                    ('cursor', 'cursor_example'),
                    ('limit', 56)]
    headers = { 
        'Accept': 'application/json',
        'token': 'token_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/apps.event.authorizations.list',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_apps_permissions_info_0(client):
    """Test case for apps_permissions_info_0

    
    """
    params = [('token', 'token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/apps.permissions.info',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_apps_permissions_request_0(client):
    """Test case for apps_permissions_request_0

    
    """
    params = [('token', 'token_example'),
                    ('scopes', 'scopes_example'),
                    ('trigger_id', 'trigger_id_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/apps.permissions.request',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_apps_permissions_resources_list_0(client):
    """Test case for apps_permissions_resources_list_0

    
    """
    params = [('token', 'token_example'),
                    ('cursor', 'cursor_example'),
                    ('limit', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/apps.permissions.resources.list',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_apps_permissions_scopes_list_0(client):
    """Test case for apps_permissions_scopes_list_0

    
    """
    params = [('token', 'token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/apps.permissions.scopes.list',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_apps_permissions_users_list_0(client):
    """Test case for apps_permissions_users_list_0

    
    """
    params = [('token', 'token_example'),
                    ('cursor', 'cursor_example'),
                    ('limit', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/apps.permissions.users.list',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_apps_permissions_users_request_0(client):
    """Test case for apps_permissions_users_request_0

    
    """
    params = [('token', 'token_example'),
                    ('scopes', 'scopes_example'),
                    ('trigger_id', 'trigger_id_example'),
                    ('user', 'user_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/apps.permissions.users.request',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_apps_uninstall(client):
    """Test case for apps_uninstall

    
    """
    params = [('token', 'token_example'),
                    ('client_id', 'client_id_example'),
                    ('client_secret', 'client_secret_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/apps.uninstall',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

