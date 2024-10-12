# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.balance_account import BalanceAccount
from openapi_server.models.balance_account_info import BalanceAccountInfo
from openapi_server.models.balance_account_update_request import BalanceAccountUpdateRequest
from openapi_server.models.paginated_payment_instruments_response import PaginatedPaymentInstrumentsResponse
from openapi_server.models.rest_service_error import RestServiceError


pytestmark = pytest.mark.asyncio

async def test_get_balance_accounts_id(client):
    """Test case for get_balance_accounts_id

    Get a balance account
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/bcl/v1/balanceAccounts/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_balance_accounts_id_payment_instruments(client):
    """Test case for get_balance_accounts_id_payment_instruments

    Get all payment instruments for a balance account
    """
    params = [('offset', 56),
                    ('limit', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/bcl/v1/balanceAccounts/{id}/paymentInstruments'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_patch_balance_accounts_id(client):
    """Test case for patch_balance_accounts_id

    Update a balance account
    """
    body = {"reference":"reference","accountHolderId":"accountHolderId","sweepConfigurations":{"key":{"balanceAccountId":"balanceAccountId","schedule":{"cronExpression":"cronExpression","type":"daily"},"merchantAccount":"merchantAccount","targetAmount":{"currency":"currency","value":5},"transferInstrumentId":"transferInstrumentId","triggerAmount":{"currency":"currency","value":5},"id":"id","sweepAmount":{"currency":"currency","value":5},"type":"push","status":"active"}},"defaultCurrencyCode":"defaultCurrencyCode","description":"description","timeZone":"timeZone","status":"Active"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/bcl/v1/balanceAccounts/{id}'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_balance_accounts(client):
    """Test case for post_balance_accounts

    Create a balance account
    """
    body = {"reference":"reference","accountHolderId":"accountHolderId","sweepConfigurations":{"key":{"balanceAccountId":"balanceAccountId","schedule":{"cronExpression":"cronExpression","type":"daily"},"merchantAccount":"merchantAccount","targetAmount":{"currency":"currency","value":5},"transferInstrumentId":"transferInstrumentId","triggerAmount":{"currency":"currency","value":5},"id":"id","sweepAmount":{"currency":"currency","value":5},"type":"push","status":"active"}},"defaultCurrencyCode":"defaultCurrencyCode","description":"description","timeZone":"timeZone"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/bcl/v1/balanceAccounts',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

