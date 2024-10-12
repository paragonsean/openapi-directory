# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.app_portal_access_in import AppPortalAccessIn
from openapi_server.models.app_portal_access_out import AppPortalAccessOut
from openapi_server.models.application_token_expire_in import ApplicationTokenExpireIn
from openapi_server.models.dashboard_access_out import DashboardAccessOut
from openapi_server.models.http_validation_error import HTTPValidationError
from openapi_server.models.http_error_out import HttpErrorOut


pytestmark = pytest.mark.asyncio

async def test_expire_all_api_v1_auth_app_app_id_expire_all_post(client):
    """Test case for expire_all_api_v1_auth_app_app_id_expire_all_post

    Expire All
    """
    body = {"expiry":60}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'idempotency_key': 'idempotency_key_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/auth/app/{app_id}/expire-all'.format(app_id='app_1srOrx2ZWZBpBUvZwXKQmoEYga2'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_app_portal_access_api_v1_auth_app_portal_access_app_id_post(client):
    """Test case for get_app_portal_access_api_v1_auth_app_portal_access_app_id_post

    Get Consumer App Portal Access
    """
    body = {"featureFlags":[]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'idempotency_key': 'idempotency_key_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/auth/app-portal-access/{app_id}'.format(app_id='app_1srOrx2ZWZBpBUvZwXKQmoEYga2'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_dashboard_access_api_v1_auth_dashboard_access_app_id_post(client):
    """Test case for get_dashboard_access_api_v1_auth_dashboard_access_app_id_post

    Get Dashboard Access
    """
    headers = { 
        'Accept': 'application/json',
        'idempotency_key': 'idempotency_key_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/auth/dashboard-access/{app_id}'.format(app_id='app_1srOrx2ZWZBpBUvZwXKQmoEYga2'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_logout_api_v1_auth_logout_post(client):
    """Test case for logout_api_v1_auth_logout_post

    Logout
    """
    headers = { 
        'Accept': 'application/json',
        'idempotency_key': 'idempotency_key_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/auth/logout/',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

