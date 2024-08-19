# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.account_funds_below_threshold_notification import AccountFundsBelowThresholdNotification
from openapi_server.models.account_holder_payout_notification import AccountHolderPayoutNotification
from openapi_server.models.beneficiary_setup_notification import BeneficiarySetupNotification
from openapi_server.models.compensate_negative_balance_notification import CompensateNegativeBalanceNotification
from openapi_server.models.direct_debit_initiated_notification import DirectDebitInitiatedNotification
from openapi_server.models.notification_response import NotificationResponse
from openapi_server.models.refund_funds_transfer_notification import RefundFundsTransferNotification
from openapi_server.models.scheduled_refunds_notification import ScheduledRefundsNotification
from openapi_server.models.transfer_funds_notification import TransferFundsNotification


pytestmark = pytest.mark.asyncio

async def test_post_accountfundsbelowthreshold(client):
    """Test case for post_accountfundsbelowthreshold

    Liable account's funds are below configured threshold
    """
    account_funds_below_threshold_notification = openapi_server.AccountFundsBelowThresholdNotification()
    headers = { 
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='POST',
        path='/ACCOUNT_FUNDS_BELOW_THRESHOLD',
        headers=headers,
        json=account_funds_below_threshold_notification,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_accountholderpayout(client):
    """Test case for post_accountholderpayout

    Paid out to account holder
    """
    account_holder_payout_notification = openapi_server.AccountHolderPayoutNotification()
    headers = { 
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='POST',
        path='/ACCOUNT_HOLDER_PAYOUT',
        headers=headers,
        json=account_holder_payout_notification,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_beneficiarysetup(client):
    """Test case for post_beneficiarysetup

    Beneficiary defined
    """
    beneficiary_setup_notification = openapi_server.BeneficiarySetupNotification()
    headers = { 
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='POST',
        path='/BENEFICIARY_SETUP',
        headers=headers,
        json=beneficiary_setup_notification,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_compensatenegativebalance(client):
    """Test case for post_compensatenegativebalance

    Negative account balances compensated
    """
    compensate_negative_balance_notification = openapi_server.CompensateNegativeBalanceNotification()
    headers = { 
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='POST',
        path='/COMPENSATE_NEGATIVE_BALANCE',
        headers=headers,
        json=compensate_negative_balance_notification,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_directdebitinitiated(client):
    """Test case for post_directdebitinitiated

    Automated direct debit initiated
    """
    direct_debit_initiated_notification = openapi_server.DirectDebitInitiatedNotification()
    headers = { 
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='POST',
        path='/DIRECT_DEBIT_INITIATED',
        headers=headers,
        json=direct_debit_initiated_notification,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_refundfundstransfer(client):
    """Test case for post_refundfundstransfer

    Funds transfer between accounts refunded
    """
    refund_funds_transfer_notification = openapi_server.RefundFundsTransferNotification()
    headers = { 
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='POST',
        path='/REFUND_FUNDS_TRANSFER',
        headers=headers,
        json=refund_funds_transfer_notification,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_scheduledrefunds(client):
    """Test case for post_scheduledrefunds

    'Refund Transfers Not Paid Out' call processed and refunds scheduled
    """
    scheduled_refunds_notification = openapi_server.ScheduledRefundsNotification()
    headers = { 
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='POST',
        path='/SCHEDULED_REFUNDS',
        headers=headers,
        json=scheduled_refunds_notification,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_transferfunds(client):
    """Test case for post_transferfunds

    Funds transferred between accounts
    """
    transfer_funds_notification = openapi_server.TransferFundsNotification()
    headers = { 
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='POST',
        path='/TRANSFER_FUNDS',
        headers=headers,
        json=transfer_funds_notification,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

