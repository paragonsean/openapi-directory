# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.agreement_terms import AgreementTerms
from openapi_server.models.error_response import ErrorResponse


pytestmark = pytest.mark.asyncio

async def test_marketplace_agreements_cancel(client):
    """Test case for marketplace_agreements_cancel

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/providers/Microsoft.MarketplaceOrdering/agreements/{publisher_id}/offers/{offer_id}/plans/{plan_id}/cancel'.format(subscription_id='subscription_id_example', publisher_id='publisher_id_example', offer_id='offer_id_example', plan_id='plan_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_marketplace_agreements_create(client):
    """Test case for marketplace_agreements_create

    
    """
    parameters = {"properties":{"product":"product","retrieveDatetime":"2000-01-23T04:56:07.000+00:00","signature":"signature","accepted":True,"licenseTextLink":"licenseTextLink","publisher":"publisher","plan":"plan","privacyPolicyLink":"privacyPolicyLink"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/providers/Microsoft.MarketplaceOrdering/offerTypes/{offer_type}/publishers/{publisher_id}/offers/{offer_id}/plans/{plan_id}/agreements/current'.format(offer_type='offer_type_example', subscription_id='subscription_id_example', publisher_id='publisher_id_example', offer_id='offer_id_example', plan_id='plan_id_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_marketplace_agreements_get(client):
    """Test case for marketplace_agreements_get

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/providers/Microsoft.MarketplaceOrdering/offerTypes/{offer_type}/publishers/{publisher_id}/offers/{offer_id}/plans/{plan_id}/agreements/current'.format(subscription_id='subscription_id_example', offer_type='offer_type_example', publisher_id='publisher_id_example', offer_id='offer_id_example', plan_id='plan_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_marketplace_agreements_get_agreement(client):
    """Test case for marketplace_agreements_get_agreement

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/providers/Microsoft.MarketplaceOrdering/agreements/{publisher_id}/offers/{offer_id}/plans/{plan_id}'.format(subscription_id='subscription_id_example', publisher_id='publisher_id_example', offer_id='offer_id_example', plan_id='plan_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_marketplace_agreements_list(client):
    """Test case for marketplace_agreements_list

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/providers/Microsoft.MarketplaceOrdering/agreements'.format(subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_marketplace_agreements_sign(client):
    """Test case for marketplace_agreements_sign

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/providers/Microsoft.MarketplaceOrdering/agreements/{publisher_id}/offers/{offer_id}/plans/{plan_id}/sign'.format(subscription_id='subscription_id_example', publisher_id='publisher_id_example', offer_id='offer_id_example', plan_id='plan_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

