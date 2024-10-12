# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.account_holder_balance_request import AccountHolderBalanceRequest
from openapi_server.models.account_holder_balance_response import AccountHolderBalanceResponse
from openapi_server.models.account_holder_transaction_list_request import AccountHolderTransactionListRequest
from openapi_server.models.account_holder_transaction_list_response import AccountHolderTransactionListResponse
from openapi_server.models.debit_account_holder_request import DebitAccountHolderRequest
from openapi_server.models.debit_account_holder_response import DebitAccountHolderResponse
from openapi_server.models.payout_account_holder_request import PayoutAccountHolderRequest
from openapi_server.models.payout_account_holder_response import PayoutAccountHolderResponse
from openapi_server.models.refund_funds_transfer_request import RefundFundsTransferRequest
from openapi_server.models.refund_funds_transfer_response import RefundFundsTransferResponse
from openapi_server.models.refund_not_paid_out_transfers_request import RefundNotPaidOutTransfersRequest
from openapi_server.models.refund_not_paid_out_transfers_response import RefundNotPaidOutTransfersResponse
from openapi_server.models.service_error import ServiceError
from openapi_server.models.setup_beneficiary_request import SetupBeneficiaryRequest
from openapi_server.models.setup_beneficiary_response import SetupBeneficiaryResponse
from openapi_server.models.transfer_funds_request import TransferFundsRequest
from openapi_server.models.transfer_funds_response import TransferFundsResponse


pytestmark = pytest.mark.asyncio

async def test_post_account_holder_balance(client):
    """Test case for post_account_holder_balance

    Get the balances of an account holder
    """
    body = {"accountHolderCode":"accountHolderCode"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/cal/services/Fund/v3/accountHolderBalance',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_account_holder_transaction_list(client):
    """Test case for post_account_holder_transaction_list

    Get a list of transactions
    """
    body = {"transactionListsPerAccount":[{"TransactionListForAccount":{"accountCode":"accountCode","page":0}},{"TransactionListForAccount":{"accountCode":"accountCode","page":0}}],"accountHolderCode":"accountHolderCode","transactionStatuses":["BalanceNotPaidOutTransfer","BalanceNotPaidOutTransfer"]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/cal/services/Fund/v3/accountHolderTransactionList',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_debit_account_holder(client):
    """Test case for post_debit_account_holder

    Send a direct debit request
    """
    body = {"accountHolderCode":"accountHolderCode","amount":{"currency":"currency","value":0},"bankAccountUUID":"bankAccountUUID","splits":[{"reference":"reference","amount":{"currency":"currency","value":0},"description":"description","type":"BalanceAccount","account":"account"},{"reference":"reference","amount":{"currency":"currency","value":0},"description":"description","type":"BalanceAccount","account":"account"}],"merchantAccount":"merchantAccount","description":"description"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/cal/services/Fund/v3/debitAccountHolder',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_payout_account_holder(client):
    """Test case for post_payout_account_holder

    Pay out from an account to the account holder
    """
    body = {"accountCode":"accountCode","accountHolderCode":"accountHolderCode","amount":{"currency":"currency","value":0},"bankAccountUUID":"bankAccountUUID","description":"description","merchantReference":"merchantReference"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/cal/services/Fund/v3/payoutAccountHolder',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_refund_funds_transfer(client):
    """Test case for post_refund_funds_transfer

    Refund a funds transfer
    """
    body = {"originalReference":"originalReference","amount":{"currency":"currency","value":0},"merchantReference":"merchantReference"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/cal/services/Fund/v3/refundFundsTransfer',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_refund_not_paid_out_transfers(client):
    """Test case for post_refund_not_paid_out_transfers

    Refund all transactions of an account since the most recent payout
    """
    body = {"accountCode":"accountCode","accountHolderCode":"accountHolderCode"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/cal/services/Fund/v3/refundNotPaidOutTransfers',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_setup_beneficiary(client):
    """Test case for post_setup_beneficiary

    Designate a beneficiary account and transfer the benefactor's current balance
    """
    body = {"sourceAccountCode":"sourceAccountCode","destinationAccountCode":"destinationAccountCode","merchantReference":"merchantReference"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/cal/services/Fund/v3/setupBeneficiary',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_transfer_funds(client):
    """Test case for post_transfer_funds

    Transfer funds between platform accounts
    """
    body = {"amount":{"currency":"currency","value":0},"sourceAccountCode":"sourceAccountCode","destinationAccountCode":"destinationAccountCode","transferCode":"transferCode","merchantReference":"merchantReference"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/cal/services/Fund/v3/transferFunds',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

