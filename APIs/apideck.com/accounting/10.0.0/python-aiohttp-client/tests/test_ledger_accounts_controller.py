# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.bad_request_response import BadRequestResponse
from openapi_server.models.create_ledger_account_response import CreateLedgerAccountResponse
from openapi_server.models.delete_ledger_account_response import DeleteLedgerAccountResponse
from openapi_server.models.get_ledger_account_response import GetLedgerAccountResponse
from openapi_server.models.get_ledger_accounts_response import GetLedgerAccountsResponse
from openapi_server.models.ledger_account import LedgerAccount
from openapi_server.models.not_found_response import NotFoundResponse
from openapi_server.models.payment_required_response import PaymentRequiredResponse
from openapi_server.models.unauthorized_response import UnauthorizedResponse
from openapi_server.models.unexpected_error_response import UnexpectedErrorResponse
from openapi_server.models.unprocessable_response import UnprocessableResponse
from openapi_server.models.update_ledger_account_response import UpdateLedgerAccountResponse


pytestmark = pytest.mark.asyncio

async def test_ledger_accounts_add(client):
    """Test case for ledger_accounts_add

    Create Ledger Account
    """
    body = {"code":"453","fully_qualified_name":"Asset.Bank.Checking_Account","display_id":"1-12345","created_at":"2020-09-30T07:43:32Z","description":"Main checking account","sub_account":False,"type":"bank","last_reconciliation_date":"2020-09-30","tax_rate":{"code":"N-T","rate":10,"name":"GST on Purchases","id":"123456"},"custom_mappings":"{}","updated_at":"2020-09-30T07:43:32Z","sub_type":"CHECKING_ACCOUNT","current_balance":20000,"currency":"USD","categories":[{"name":"Finance Charges Expense","id":"12345"},{"name":"Finance Charges Expense","id":"12345"}],"id":"12345","opening_balance":75000,"bank_account":{"bsb_number":"062-001","account_number":"123465","bank_code":"BNH","account_type":"credit_card","account_name":"SPACEX LLC","iban":"CH2989144532982975332","bank_name":"Monzo","currency":"USD","routing_number":"012345678","bic":"AUDSCHGGXXX","branch_identifier":"001"},"level":1,"active":True,"classification":"asset","created_by":"12345","parent_account":{"display_id":"1-1100","name":"Bank Accounts","id":"12345"},"tax_type":"NONE","sub_accounts":[{"account_sub_name":"Petty Cash","id":"12345"},{"account_sub_name":"Petty Cash","id":"12345"}],"nominal_code":"N091","row_version":"1-12345","name":"Bank account","updated_by":"12345","header":True,"status":"active"}
    params = [('raw', False)]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_apideck_consumer_id': 'x_apideck_consumer_id_example',
        'x_apideck_app_id': 'dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX',
        'x_apideck_service_id': 'x_apideck_service_id_example',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/accounting/ledger-accounts',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_ledger_accounts_all(client):
    """Test case for ledger_accounts_all

    List Ledger Accounts
    """
    params = [('raw', False),
                    ('cursor', 'cursor_example'),
                    ('limit', 20),
                    ('pass_through', None),
                    ('fields', 'id,updated_at')]
    headers = { 
        'Accept': 'application/json',
        'x_apideck_consumer_id': 'x_apideck_consumer_id_example',
        'x_apideck_app_id': 'dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX',
        'x_apideck_service_id': 'x_apideck_service_id_example',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/accounting/ledger-accounts',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_ledger_accounts_delete(client):
    """Test case for ledger_accounts_delete

    Delete Ledger Account
    """
    params = [('raw', False)]
    headers = { 
        'Accept': 'application/json',
        'x_apideck_consumer_id': 'x_apideck_consumer_id_example',
        'x_apideck_app_id': 'dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX',
        'x_apideck_service_id': 'x_apideck_service_id_example',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/accounting/ledger-accounts/{id}'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_ledger_accounts_one(client):
    """Test case for ledger_accounts_one

    Get Ledger Account
    """
    params = [('raw', False),
                    ('fields', 'id,updated_at')]
    headers = { 
        'Accept': 'application/json',
        'x_apideck_consumer_id': 'x_apideck_consumer_id_example',
        'x_apideck_app_id': 'dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX',
        'x_apideck_service_id': 'x_apideck_service_id_example',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/accounting/ledger-accounts/{id}'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_ledger_accounts_update(client):
    """Test case for ledger_accounts_update

    Update Ledger Account
    """
    body = {"code":"453","fully_qualified_name":"Asset.Bank.Checking_Account","display_id":"1-12345","created_at":"2020-09-30T07:43:32Z","description":"Main checking account","sub_account":False,"type":"bank","last_reconciliation_date":"2020-09-30","tax_rate":{"code":"N-T","rate":10,"name":"GST on Purchases","id":"123456"},"custom_mappings":"{}","updated_at":"2020-09-30T07:43:32Z","sub_type":"CHECKING_ACCOUNT","current_balance":20000,"currency":"USD","categories":[{"name":"Finance Charges Expense","id":"12345"},{"name":"Finance Charges Expense","id":"12345"}],"id":"12345","opening_balance":75000,"bank_account":{"bsb_number":"062-001","account_number":"123465","bank_code":"BNH","account_type":"credit_card","account_name":"SPACEX LLC","iban":"CH2989144532982975332","bank_name":"Monzo","currency":"USD","routing_number":"012345678","bic":"AUDSCHGGXXX","branch_identifier":"001"},"level":1,"active":True,"classification":"asset","created_by":"12345","parent_account":{"display_id":"1-1100","name":"Bank Accounts","id":"12345"},"tax_type":"NONE","sub_accounts":[{"account_sub_name":"Petty Cash","id":"12345"},{"account_sub_name":"Petty Cash","id":"12345"}],"nominal_code":"N091","row_version":"1-12345","name":"Bank account","updated_by":"12345","header":True,"status":"active"}
    params = [('raw', False)]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_apideck_consumer_id': 'x_apideck_consumer_id_example',
        'x_apideck_app_id': 'dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX',
        'x_apideck_service_id': 'x_apideck_service_id_example',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/accounting/ledger-accounts/{id}'.format(id='id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

