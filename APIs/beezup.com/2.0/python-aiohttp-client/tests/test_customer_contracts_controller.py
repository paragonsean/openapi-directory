# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.beez_up_common_error_response_message import BeezUPCommonErrorResponseMessage
from openapi_server.models.billing_period_list import BillingPeriodList
from openapi_server.models.contracts import Contracts
from openapi_server.models.create_contract import CreateContract
from openapi_server.models.create_contract_response import CreateContractResponse
from openapi_server.models.offer import Offer
from openapi_server.models.offer_request import OfferRequest
from openapi_server.models.standard_offers import StandardOffers
from openapi_server.models.terminate_contract import TerminateContract


pytestmark = pytest.mark.asyncio

async def test_create_contract(client):
    """Test case for create_contract

    Create a new contract
    """
    body = openapi_server.CreateContract()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v2/user/customer/contracts',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_next_contract(client):
    """Test case for delete_next_contract

    Delete your next contract
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='DELETE',
        path='/v2/user/customer/contracts/next',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_billing_periods(client):
    """Test case for get_billing_periods

    Get billing periods conditions
    """
    headers = { 
        'Accept': 'application/json',
        'if_none_match': 'if_none_match_example',
    }
    response = await client.request(
        method='GET',
        path='/v2/user/customer/billingPeriods',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_contracts(client):
    """Test case for get_contracts

    Get contract list
    """
    headers = { 
        'Accept': 'application/json',
        'if_none_match': 'if_none_match_example',
    }
    response = await client.request(
        method='GET',
        path='/v2/user/customer/contracts',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_offer(client):
    """Test case for get_offer

    Get offer pricing
    """
    body = openapi_server.OfferRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v2/user/customer/offers',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_standard_offers(client):
    """Test case for get_standard_offers

    Get all standard offers
    """
    headers = { 
        'Accept': 'application/json',
        'if_none_match': 'if_none_match_example',
    }
    response = await client.request(
        method='GET',
        path='/v2/user/customer/offers',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_reactivate_current_contract(client):
    """Test case for reactivate_current_contract

    Reactivate your terminated contract.
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v2/user/customer/contracts/current/reenableAutoRenewal',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_terminate_current_contract(client):
    """Test case for terminate_current_contract

    Schedule termination of your current contract at the end of the commitment.
    """
    body = openapi_server.TerminateContract()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v2/user/customer/contracts/current/disableAutoRenewal',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

