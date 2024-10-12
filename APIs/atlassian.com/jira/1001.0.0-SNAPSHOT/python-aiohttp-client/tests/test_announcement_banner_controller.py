# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.announcement_banner_configuration import AnnouncementBannerConfiguration
from openapi_server.models.announcement_banner_configuration_update import AnnouncementBannerConfigurationUpdate
from openapi_server.models.error_collection import ErrorCollection


pytestmark = pytest.mark.asyncio

async def test_get_banner(client):
    """Test case for get_banner

    Get announcement banner configuration
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/rest/api/3/announcementBanner',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_set_banner(client):
    """Test case for set_banner

    Update announcement banner configuration
    """
    body = {"visibility":"visibility","isEnabled":True,"isDismissible":True,"message":"message"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='PUT',
        path='/rest/api/3/announcementBanner',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

