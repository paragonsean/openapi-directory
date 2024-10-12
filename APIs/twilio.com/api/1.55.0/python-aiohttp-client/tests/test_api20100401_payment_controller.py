# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.api_v2010_account_call_payments import ApiV2010AccountCallPayments
from openapi_server.models.payments_enum_bank_account_type import PaymentsEnumBankAccountType
from openapi_server.models.payments_enum_capture import PaymentsEnumCapture
from openapi_server.models.payments_enum_payment_method import PaymentsEnumPaymentMethod
from openapi_server.models.payments_enum_status import PaymentsEnumStatus
from openapi_server.models.payments_enum_token_type import PaymentsEnumTokenType


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_create_payments(client):
    """Test case for create_payments

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    data = {
        'bank_account_type': openapi_server.PaymentsEnumBankAccountType(),
        'charge_amount': 3.4,
        'currency': 'currency_example',
        'description': 'description_example',
        'idempotency_key': 'idempotency_key_example',
        'input': 'input_example',
        'min_postal_code_length': 56,
        'parameter': None,
        'payment_connector': 'payment_connector_example',
        'payment_method': openapi_server.PaymentsEnumPaymentMethod(),
        'postal_code': True,
        'security_code': True,
        'status_callback': 'status_callback_example',
        'timeout': 56,
        'token_type': openapi_server.PaymentsEnumTokenType(),
        'valid_card_types': 'valid_card_types_example'
        }
    response = await client.request(
        method='POST',
        path='/2010-04-01/Accounts/{account_sid}/Calls/{call_sid}/Payments.json'.format(account_sid='account_sid_example', call_sid='call_sid_example'),
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_update_payments(client):
    """Test case for update_payments

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    data = {
        'capture': openapi_server.PaymentsEnumCapture(),
        'idempotency_key': 'idempotency_key_example',
        'status': openapi_server.PaymentsEnumStatus(),
        'status_callback': 'status_callback_example'
        }
    response = await client.request(
        method='POST',
        path='/2010-04-01/Accounts/{account_sid}/Calls/{call_sid}/Payments/{sid_jso}'.format(account_sid='account_sid_example', call_sid='call_sid_example', sid='sid_example'),
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

