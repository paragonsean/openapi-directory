# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.rest_service_error import RestServiceError
from openapi_server.models.transaction_rule import TransactionRule
from openapi_server.models.transaction_rule_info import TransactionRuleInfo
from openapi_server.models.transaction_rule_response import TransactionRuleResponse


pytestmark = pytest.mark.asyncio

async def test_delete_transaction_rules_transaction_rule_id(client):
    """Test case for delete_transaction_rules_transaction_rule_id

    Delete a transaction rule
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/bcl/v1/transactionRules/{transaction_rule_id}'.format(transaction_rule_id='transaction_rule_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_transaction_rules_transaction_rule_id(client):
    """Test case for get_transaction_rules_transaction_rule_id

    Get a transaction rule
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/bcl/v1/transactionRules/{transaction_rule_id}'.format(transaction_rule_id='transaction_rule_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_patch_transaction_rules_transaction_rule_id(client):
    """Test case for patch_transaction_rules_transaction_rule_id

    Update a transaction rule
    """
    body = {"amount":{"currency":"currency","value":5},"endDate":"endDate","entryModes":["barcode","barcode"],"description":"description","paymentInstrumentId":"paymentInstrumentId","countries":["countries","countries"],"type":"allowList","reference":"reference","mccs":["mccs","mccs"],"processingTypes":["atmWithdraw","atmWithdraw"],"interval":{"type":"daily"},"maxTransactions":0,"balancePlatformId":"balancePlatformId","paymentInstrumentGroupId":"paymentInstrumentGroupId","startDate":"startDate","status":"active"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/bcl/v1/transactionRules/{transaction_rule_id}'.format(transaction_rule_id='transaction_rule_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_transaction_rules(client):
    """Test case for post_transaction_rules

    Create a transaction rule
    """
    body = {"amount":{"currency":"currency","value":5},"endDate":"endDate","entryModes":["barcode","barcode"],"description":"description","paymentInstrumentId":"paymentInstrumentId","countries":["countries","countries"],"type":"allowList","reference":"reference","mccs":["mccs","mccs"],"processingTypes":["atmWithdraw","atmWithdraw"],"interval":{"type":"daily"},"maxTransactions":0,"balancePlatformId":"balancePlatformId","paymentInstrumentGroupId":"paymentInstrumentGroupId","startDate":"startDate","status":"active"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/bcl/v1/transactionRules',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

