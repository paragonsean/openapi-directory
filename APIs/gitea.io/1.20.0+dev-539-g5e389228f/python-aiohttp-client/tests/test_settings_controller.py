# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.general_api_settings import GeneralAPISettings
from openapi_server.models.general_attachment_settings import GeneralAttachmentSettings
from openapi_server.models.general_repo_settings import GeneralRepoSettings
from openapi_server.models.general_ui_settings import GeneralUISettings


pytestmark = pytest.mark.asyncio

async def test_get_general_api_settings(client):
    """Test case for get_general_api_settings

    Get instance's global settings for api
    """
    headers = { 
        'Accept': 'application/json',
        'TOTPHeader': 'special-key',
        'AuthorizationHeaderToken': 'special-key',
        'SudoHeader': 'special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
        'AccessToken': 'special-key',
        'SudoParam': 'special-key',
        'Token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/settings/api',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_general_attachment_settings(client):
    """Test case for get_general_attachment_settings

    Get instance's global settings for Attachment
    """
    headers = { 
        'Accept': 'application/json',
        'TOTPHeader': 'special-key',
        'AuthorizationHeaderToken': 'special-key',
        'SudoHeader': 'special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
        'AccessToken': 'special-key',
        'SudoParam': 'special-key',
        'Token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/settings/attachment',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_general_repository_settings(client):
    """Test case for get_general_repository_settings

    Get instance's global settings for repositories
    """
    headers = { 
        'Accept': 'application/json',
        'TOTPHeader': 'special-key',
        'AuthorizationHeaderToken': 'special-key',
        'SudoHeader': 'special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
        'AccessToken': 'special-key',
        'SudoParam': 'special-key',
        'Token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/settings/repository',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_general_ui_settings(client):
    """Test case for get_general_ui_settings

    Get instance's global settings for ui
    """
    headers = { 
        'Accept': 'application/json',
        'TOTPHeader': 'special-key',
        'AuthorizationHeaderToken': 'special-key',
        'SudoHeader': 'special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
        'AccessToken': 'special-key',
        'SudoParam': 'special-key',
        'Token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/settings/ui',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

