# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.offer_delegation import OfferDelegation
from openapi_server.models.offer_delegation_list import OfferDelegationList


pytestmark = pytest.mark.asyncio

async def test_offer_delegations_create_or_update(client):
    """Test case for offer_delegations_create_or_update

    
    """
    new_offer_delegation = {"properties":{"subscriptionId":"subscriptionId"}}
    params = [('api-version', '2015-11-01')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourcegroups/{resource_group_name}/providers/Microsoft.Subscriptions.Admin/offers/{offer}/offerDelegations/{offer_delegation_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', offer='offer_example', offer_delegation_name='offer_delegation_name_example'),
        headers=headers,
        json=new_offer_delegation,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_offer_delegations_delete(client):
    """Test case for offer_delegations_delete

    
    """
    params = [('api-version', '2015-11-01')]
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourcegroups/{resource_group_name}/providers/Microsoft.Subscriptions.Admin/offers/{offer}/offerDelegations/{offer_delegation_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', offer='offer_example', offer_delegation_name='offer_delegation_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_offer_delegations_get(client):
    """Test case for offer_delegations_get

    
    """
    params = [('api-version', '2015-11-01')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourcegroups/{resource_group_name}/providers/Microsoft.Subscriptions.Admin/offers/{offer}/offerDelegations/{offer_delegation_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', offer='offer_example', offer_delegation_name='offer_delegation_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_offer_delegations_list(client):
    """Test case for offer_delegations_list

    
    """
    params = [('api-version', '2015-11-01')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourcegroups/{resource_group_name}/providers/Microsoft.Subscriptions.Admin/offers/{offer}/offerDelegations'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', offer='offer_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

