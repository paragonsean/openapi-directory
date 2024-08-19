# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.payment_instrument_group import PaymentInstrumentGroup
from openapi_server.models.payment_instrument_group_info import PaymentInstrumentGroupInfo
from openapi_server.models.rest_service_error import RestServiceError
from openapi_server.models.transaction_rules_response import TransactionRulesResponse


pytestmark = pytest.mark.asyncio

async def test_get_payment_instrument_groups_id(client):
    """Test case for get_payment_instrument_groups_id

    Get a payment instrument group
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/bcl/v1/paymentInstrumentGroups/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_payment_instrument_groups_id_transaction_rules(client):
    """Test case for get_payment_instrument_groups_id_transaction_rules

    Get all transaction rules for a payment instrument group
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/bcl/v1/paymentInstrumentGroups/{id}/transactionRules'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_payment_instrument_groups(client):
    """Test case for post_payment_instrument_groups

    Create a payment instrument group
    """
    body = {"reference":"reference","txVariant":"txVariant","description":"description","balancePlatform":"balancePlatform","properties":{"key":"properties"}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/bcl/v1/paymentInstrumentGroups',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

