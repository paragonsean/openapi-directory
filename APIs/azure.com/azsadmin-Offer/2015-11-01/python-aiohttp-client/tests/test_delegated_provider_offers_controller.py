# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.offer import Offer
from openapi_server.models.offer_list import OfferList


pytestmark = pytest.mark.asyncio

async def test_delegated_provider_offers_get(client):
    """Test case for delegated_provider_offers_get

    
    """
    params = [('api-version', '2015-11-01')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/delegatedProviders/{delegated_provider_id}/offers/{offer_name}'.format(delegated_provider_id='delegated_provider_id_example', offer_name='offer_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delegated_provider_offers_list(client):
    """Test case for delegated_provider_offers_list

    
    """
    params = [('api-version', '2015-11-01')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/delegatedProviders/{delegated_provider_id}/offers'.format(delegated_provider_id='delegated_provider_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

