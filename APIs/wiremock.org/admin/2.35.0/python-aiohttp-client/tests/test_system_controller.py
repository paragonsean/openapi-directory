# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.admin_settings_post_request import AdminSettingsPostRequest


pytestmark = pytest.mark.asyncio

async def test_admin_reset_post(client):
    """Test case for admin_reset_post

    Reset mappings and request journal
    """
    headers = { 
    }
    response = await client.request(
        method='POST',
        path='/__admin/reset',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_admin_settings_post(client):
    """Test case for admin_settings_post

    Update global settings
    """
    body = openapi_server.AdminSettingsPostRequest()
    headers = { 
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/__admin/settings',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_admin_shutdown_post(client):
    """Test case for admin_shutdown_post

    
    """
    headers = { 
    }
    response = await client.request(
        method='POST',
        path='/__admin/shutdown',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

