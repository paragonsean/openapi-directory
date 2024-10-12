# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.external_transaction import ExternalTransaction
from openapi_server.models.refund_external_transaction_request import RefundExternalTransactionRequest


pytestmark = pytest.mark.asyncio

async def test_androidpublisher_externaltransactions_createexternaltransaction(client):
    """Test case for androidpublisher_externaltransactions_createexternaltransaction

    
    """
    body = {"oneTimeTransaction":{"externalTransactionToken":"externalTransactionToken"},"recurringTransaction":{"externalTransactionToken":"externalTransactionToken","externalSubscription":{"subscriptionType":"SUBSCRIPTION_TYPE_UNSPECIFIED"},"initialExternalTransactionId":"initialExternalTransactionId","migratedTransactionProgram":"EXTERNAL_TRANSACTION_PROGRAM_UNSPECIFIED"},"currentTaxAmount":{"priceMicros":"priceMicros","currency":"currency"},"originalTaxAmount":{"priceMicros":"priceMicros","currency":"currency"},"transactionTime":"transactionTime","testPurchase":"{}","createTime":"createTime","currentPreTaxAmount":{"priceMicros":"priceMicros","currency":"currency"},"originalPreTaxAmount":{"priceMicros":"priceMicros","currency":"currency"},"externalTransactionId":"externalTransactionId","packageName":"packageName","transactionState":"TRANSACTION_STATE_UNSPECIFIED","userTaxAddress":{"regionCode":"regionCode","administrativeArea":"administrativeArea"}}
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example'),
                    ('externalTransactionId', 'external_transaction_id_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/androidpublisher/v3/{parent}/externalTransactions'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_androidpublisher_externaltransactions_getexternaltransaction(client):
    """Test case for androidpublisher_externaltransactions_getexternaltransaction

    
    """
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/androidpublisher/v3/{name}'.format(name='name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_androidpublisher_externaltransactions_refundexternaltransaction(client):
    """Test case for androidpublisher_externaltransactions_refundexternaltransaction

    
    """
    body = {"fullRefund":"{}","refundTime":"refundTime","partialRefund":{"refundPreTaxAmount":{"priceMicros":"priceMicros","currency":"currency"},"refundId":"refundId"}}
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/androidpublisher/v3/{namerefun}'.format(name='name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

