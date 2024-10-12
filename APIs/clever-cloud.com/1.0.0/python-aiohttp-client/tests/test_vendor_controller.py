# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.application import Application
from openapi_server.models.wannabe_addon_billing import WannabeAddonBilling


pytestmark = pytest.mark.asyncio

async def test_get_vendor_apps_0(client):
    """Test case for get_vendor_apps_0

    
    """
    params = [('offset', 56)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/vendor/apps',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_vendor_apps_addon_id_0(client):
    """Test case for get_vendor_apps_addon_id_0

    
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/v2/vendor/apps/{addon_id}'.format(addon_id='addon_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_vendor_billing_owner_id_0(client):
    """Test case for post_vendor_billing_owner_id_0

    
    """
    body = {"cost":0.8008281904610115}
    headers = { 
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v2/vendor/apps/{addon_id}/consumptions'.format(addon_id='addon_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_put_vendor_apps_addon_id_0(client):
    """Test case for put_vendor_apps_addon_id_0

    
    """
    headers = { 
    }
    response = await client.request(
        method='PUT',
        path='/v2/vendor/apps/{addon_id}'.format(addon_id='addon_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_vendor_addons_post_1(client):
    """Test case for vendor_addons_post_1

    
    """
    headers = { 
    }
    response = await client.request(
        method='POST',
        path='/v2/vendor//addons',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_vendor_apps_addon_id_logscollector_get_0(client):
    """Test case for vendor_apps_addon_id_logscollector_get_0

    
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/v2/vendor//apps/{addon_id}/logscollector'.format(addon_id='addon_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_vendor_apps_addon_id_migration_callback_put_0(client):
    """Test case for vendor_apps_addon_id_migration_callback_put_0

    
    """
    params = [('plan_id', 'plan_id_example'),
                    ('region', 'region_example')]
    headers = { 
    }
    response = await client.request(
        method='PUT',
        path='/v2/vendor/apps/{addon_id}/migration_callback'.format(addon_id='addon_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

