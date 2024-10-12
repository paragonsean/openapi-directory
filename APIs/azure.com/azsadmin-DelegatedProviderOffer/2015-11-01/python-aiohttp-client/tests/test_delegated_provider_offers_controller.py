# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.delegated_provider_offer import DelegatedProviderOffer
from openapi_server.models.delegated_provider_offer_list import DelegatedProviderOfferList


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
        path='/subscriptions/{subscription_id}/providers/Microsoft.Subscriptions.Admin/delegatedProviders/{delegated_provider_subscription_id}/offers/{offer}'.format(subscription_id='subscription_id_example', delegated_provider_subscription_id='delegated_provider_subscription_id_example', offer='offer_example'),
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
        path='/subscriptions/{subscription_id}/providers/Microsoft.Subscriptions.Admin/delegatedProviders/{delegated_provider_subscription_id}/offers'.format(subscription_id='subscription_id_example', delegated_provider_subscription_id='delegated_provider_subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

