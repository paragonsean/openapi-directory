# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.beez_up_common_error_response_message import BeezUPCommonErrorResponseMessage
from openapi_server.models.cost_settings import CostSettings
from openapi_server.models.general_settings import GeneralSettings
from openapi_server.models.upgrade_offer_required import UpgradeOfferRequired


pytestmark = pytest.mark.asyncio

async def test_configure_channel_catalog_cost_settings(client):
    """Test case for configure_channel_catalog_cost_settings

    Configure channel catalog cost settings
    """
    body = openapi_server.CostSettings()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/v2/user/channelCatalogs/{channel_catalog_id}/settings/cost'.format(channel_catalog_id='6d6b04de-406b-4539-8e7e-bf3e8da5dfb0'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_configure_channel_catalog_general_settings(client):
    """Test case for configure_channel_catalog_general_settings

    Configure channel catalog general settings
    """
    body = openapi_server.GeneralSettings()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/v2/user/channelCatalogs/{channel_catalog_id}/settings/general'.format(channel_catalog_id='6d6b04de-406b-4539-8e7e-bf3e8da5dfb0'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_disable_channel_catalog(client):
    """Test case for disable_channel_catalog

    Disable a channel catalog
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v2/user/channelCatalogs/{channel_catalog_id}/disable'.format(channel_catalog_id='6d6b04de-406b-4539-8e7e-bf3e8da5dfb0'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_enable_channel_catalog(client):
    """Test case for enable_channel_catalog

    Enable a channel catalog
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v2/user/channelCatalogs/{channel_catalog_id}/enable'.format(channel_catalog_id='6d6b04de-406b-4539-8e7e-bf3e8da5dfb0'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

