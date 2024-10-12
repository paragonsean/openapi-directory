# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.country import Country
from openapi_server.models.instance import Instance
from openapi_server.models.provider import Provider
from openapi_server.models.zone import Zone


pytestmark = pytest.mark.asyncio

async def test_get_products_addon_providers_0(client):
    """Test case for get_products_addon_providers_0

    
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/products/addonproviders',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_products_addon_providers_provider_id_0(client):
    """Test case for get_products_addon_providers_provider_id_0

    
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/products/addonproviders/{provider_id}'.format(provider_id='provider_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_products_countries_0(client):
    """Test case for get_products_countries_0

    
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/products/countries',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_products_countrycodes_0(client):
    """Test case for get_products_countrycodes_0

    
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/products/countrycodes',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_products_instances_0(client):
    """Test case for get_products_instances_0

    
    """
    params = [('for', '_for_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/products/instances',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_products_instances_type_version_0(client):
    """Test case for get_products_instances_type_version_0

    
    """
    params = [('for', '_for_example'),
                    ('app', 'app_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/products/instances/{type_version}'.format(type='type_example', version='version_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_products_packages_0(client):
    """Test case for get_products_packages_0

    
    """
    params = [('coupon', 'coupon_example'),
                    ('orgaId', 'orga_id_example'),
                    ('currency', 'currency_example')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/v2/products/packages',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_products_prices_0(client):
    """Test case for get_products_prices_0

    
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/v2/products/prices',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_products_zones_0(client):
    """Test case for get_products_zones_0

    
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/products/zones',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_products_addonproviders_provider_id_versions_get_0(client):
    """Test case for products_addonproviders_provider_id_versions_get_0

    
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/v2/products/addonproviders/{provider_id}/versions'.format(provider_id='provider_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_products_mfa_kinds_get_0(client):
    """Test case for products_mfa_kinds_get_0

    
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/v2/products/mfa_kinds',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

