# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.offer import Offer
from openapi_server.models.offer_list_response import OfferListResponse
from openapi_server.models.private_store_list import PrivateStoreList
from openapi_server.models.private_store_properties import PrivateStoreProperties


pytestmark = pytest.mark.asyncio

async def test_private_store_create_or_update(client):
    """Test case for private_store_create_or_update

    
    """
    payload = {"name":"name","availability":"enabled"}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/providers/Microsoft.Marketplace/privateStores/{private_store_id}'.format(private_store_id='private_store_id_example'),
        headers=headers,
        json=payload,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_private_store_delete(client):
    """Test case for private_store_delete

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='DELETE',
        path='/providers/Microsoft.Marketplace/privateStores/{private_store_id}'.format(private_store_id='private_store_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_private_store_get(client):
    """Test case for private_store_get

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/providers/Microsoft.Marketplace/privateStores/{private_store_id}'.format(private_store_id='private_store_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_private_store_list(client):
    """Test case for private_store_list

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/providers/Microsoft.Marketplace/privateStores',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_private_store_offer_create_or_update(client):
    """Test case for private_store_offer_create_or_update

    
    """
    payload = {"summary":"summary","publisherDisplayName":"publisherDisplayName","displayName":"displayName","plans":[{"displayName":"displayName","planId":"planId"},{"displayName":"displayName","planId":"planId"}],"description":"description","longSummary":"longSummary","eTag":"eTag","id":"id"}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/providers/Microsoft.Marketplace/privateStores/{private_store_id}/offers/{offer_id}'.format(offer_id='offer_id_example', private_store_id='private_store_id_example'),
        headers=headers,
        json=payload,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_private_store_offer_delete(client):
    """Test case for private_store_offer_delete

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='DELETE',
        path='/providers/Microsoft.Marketplace/privateStores/{private_store_id}/offers/{offer_id}'.format(offer_id='offer_id_example', private_store_id='private_store_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_private_store_offer_get(client):
    """Test case for private_store_offer_get

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/providers/Microsoft.Marketplace/privateStores/{private_store_id}/offers/{offer_id}'.format(offer_id='offer_id_example', private_store_id='private_store_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_private_store_offers_list(client):
    """Test case for private_store_offers_list

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/providers/Microsoft.Marketplace/privateStores/{private_store_id}/offers'.format(private_store_id='private_store_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

