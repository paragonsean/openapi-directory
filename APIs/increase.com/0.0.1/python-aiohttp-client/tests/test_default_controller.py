# coding: utf-8

import pytest
import json
from aiohttp import web
from aiohttp import FormData

from openapi_server.models.account import Account
from openapi_server.models.account_list import AccountList
from openapi_server.models.account_number import AccountNumber
from openapi_server.models.account_number_list import AccountNumberList
from openapi_server.models.account_statement import AccountStatement
from openapi_server.models.account_statement_list import AccountStatementList
from openapi_server.models.account_transfer import AccountTransfer
from openapi_server.models.account_transfer_list import AccountTransferList
from openapi_server.models.ach_prenotification import AchPrenotification
from openapi_server.models.ach_prenotification_list import AchPrenotificationList
from openapi_server.models.ach_transfer import AchTransfer
from openapi_server.models.ach_transfer_list import AchTransferList
from openapi_server.models.action_a_real_time_decision_parameters import ActionARealTimeDecisionParameters
from openapi_server.models.balance_lookup import BalanceLookup
from openapi_server.models.bookkeeping_account import BookkeepingAccount
from openapi_server.models.bookkeeping_account_list import BookkeepingAccountList
from openapi_server.models.bookkeeping_entry_list import BookkeepingEntryList
from openapi_server.models.bookkeeping_entry_set import BookkeepingEntrySet
from openapi_server.models.card import Card
from openapi_server.models.card_details import CardDetails
from openapi_server.models.card_dispute import CardDispute
from openapi_server.models.card_dispute_list import CardDisputeList
from openapi_server.models.card_list import CardList
from openapi_server.models.card_profile import CardProfile
from openapi_server.models.card_profile_list import CardProfileList
from openapi_server.models.check_deposit import CheckDeposit
from openapi_server.models.check_deposit_list import CheckDepositList
from openapi_server.models.check_transfer import CheckTransfer
from openapi_server.models.check_transfer_list import CheckTransferList
from openapi_server.models.complete_a_sandbox_real_time_payments_transfer_parameters import CompleteASandboxRealTimePaymentsTransferParameters
from openapi_server.models.create_a_bookkeeping_account_parameters import CreateABookkeepingAccountParameters
from openapi_server.models.create_a_bookkeeping_entry_set_parameters import CreateABookkeepingEntrySetParameters
from openapi_server.models.create_a_card_dispute_parameters import CreateACardDisputeParameters
from openapi_server.models.create_a_card_parameters import CreateACardParameters
from openapi_server.models.create_a_card_profile_parameters import CreateACardProfileParameters
from openapi_server.models.create_a_check_deposit_parameters import CreateACheckDepositParameters
from openapi_server.models.create_a_check_transfer_parameters import CreateACheckTransferParameters
from openapi_server.models.create_a_limit_parameters import CreateALimitParameters
from openapi_server.models.create_a_real_time_payments_transfer_parameters import CreateARealTimePaymentsTransferParameters
from openapi_server.models.create_a_supplemental_document_for_an_entity_parameters import CreateASupplementalDocumentForAnEntityParameters
from openapi_server.models.create_a_wire_drawdown_request_parameters import CreateAWireDrawdownRequestParameters
from openapi_server.models.create_a_wire_transfer_parameters import CreateAWireTransferParameters
from openapi_server.models.create_an_account_number_parameters import CreateAnAccountNumberParameters
from openapi_server.models.create_an_account_parameters import CreateAnAccountParameters
from openapi_server.models.create_an_account_transfer_parameters import CreateAnAccountTransferParameters
from openapi_server.models.create_an_ach_prenotification_parameters import CreateAnAchPrenotificationParameters
from openapi_server.models.create_an_ach_return_parameters import CreateAnAchReturnParameters
from openapi_server.models.create_an_ach_transfer_parameters import CreateAnAchTransferParameters
from openapi_server.models.create_an_entity_parameters import CreateAnEntityParameters
from openapi_server.models.create_an_event_subscription_parameters import CreateAnEventSubscriptionParameters
from openapi_server.models.create_an_export_parameters import CreateAnExportParameters
from openapi_server.models.create_an_external_account_parameters import CreateAnExternalAccountParameters
from openapi_server.models.declined_transaction import DeclinedTransaction
from openapi_server.models.declined_transaction_list import DeclinedTransactionList
from openapi_server.models.digital_wallet_token import DigitalWalletToken
from openapi_server.models.digital_wallet_token_list import DigitalWalletTokenList
from openapi_server.models.document import Document
from openapi_server.models.document_list import DocumentList
from openapi_server.models.entity import Entity
from openapi_server.models.entity_list import EntityList
from openapi_server.models.error import Error
from openapi_server.models.event import Event
from openapi_server.models.event_list import EventList
from openapi_server.models.event_subscription import EventSubscription
from openapi_server.models.event_subscription_list import EventSubscriptionList
from openapi_server.models.export import Export
from openapi_server.models.export_list import ExportList
from openapi_server.models.external_account import ExternalAccount
from openapi_server.models.external_account_list import ExternalAccountList
from openapi_server.models.file_list import FileList
from openapi_server.models.group import Group
from openapi_server.models.inbound_ach_transfer_return import InboundAchTransferReturn
from openapi_server.models.inbound_ach_transfer_return_list import InboundAchTransferReturnList
from openapi_server.models.inbound_ach_transfer_simulation_result import InboundAchTransferSimulationResult
from openapi_server.models.inbound_card_authorization_simulation_result import InboundCardAuthorizationSimulationResult
from openapi_server.models.inbound_digital_wallet_token_request_simulation_result import InboundDigitalWalletTokenRequestSimulationResult
from openapi_server.models.inbound_real_time_payments_transfer_simulation_result import InboundRealTimePaymentsTransferSimulationResult
from openapi_server.models.inbound_wire_drawdown_request import InboundWireDrawdownRequest
from openapi_server.models.inbound_wire_drawdown_request_list import InboundWireDrawdownRequestList
from openapi_server.models.inbound_wire_transfer_simulation_result import InboundWireTransferSimulationResult
from openapi_server.models.interest_payment_simulation_result import InterestPaymentSimulationResult
from openapi_server.models.limit import Limit
from openapi_server.models.limit_list import LimitList
from openapi_server.models.look_up_the_balance_for_an_account_parameters import LookUpTheBalanceForAnAccountParameters
from openapi_server.models.oauth_connection import OauthConnection
from openapi_server.models.oauth_connection_list import OauthConnectionList
from openapi_server.models.pending_transaction import PendingTransaction
from openapi_server.models.pending_transaction_list import PendingTransactionList
from openapi_server.models.program import Program
from openapi_server.models.program_list import ProgramList
from openapi_server.models.real_time_decision import RealTimeDecision
from openapi_server.models.real_time_payments_transfer import RealTimePaymentsTransfer
from openapi_server.models.real_time_payments_transfer_list import RealTimePaymentsTransferList
from openapi_server.models.return_a_sandbox_ach_transfer_parameters import ReturnASandboxAchTransferParameters
from openapi_server.models.return_a_sandbox_check_transfer_parameters import ReturnASandboxCheckTransferParameters
from openapi_server.models.routing_number_list import RoutingNumberList
from openapi_server.models.simulate_a_real_time_payments_transfer_to_your_account_parameters import SimulateARealTimePaymentsTransferToYourAccountParameters
from openapi_server.models.simulate_a_refund_on_a_card_parameters import SimulateARefundOnACardParameters
from openapi_server.models.simulate_a_tax_document_being_created_parameters import SimulateATaxDocumentBeingCreatedParameters
from openapi_server.models.simulate_a_wire_transfer_to_your_account_parameters import SimulateAWireTransferToYourAccountParameters
from openapi_server.models.simulate_an_account_statement_being_created_parameters import SimulateAnAccountStatementBeingCreatedParameters
from openapi_server.models.simulate_an_ach_transfer_to_your_account_parameters import SimulateAnAchTransferToYourAccountParameters
from openapi_server.models.simulate_an_authorization_on_a_card_parameters import SimulateAnAuthorizationOnACardParameters
from openapi_server.models.simulate_an_inbound_wire_drawdown_request_being_created_parameters import SimulateAnInboundWireDrawdownRequestBeingCreatedParameters
from openapi_server.models.simulate_an_interest_payment_to_your_account_parameters import SimulateAnInterestPaymentToYourAccountParameters
from openapi_server.models.simulate_digital_wallet_provisioning_for_a_card_parameters import SimulateDigitalWalletProvisioningForACardParameters
from openapi_server.models.simulate_settling_a_card_authorization_parameters import SimulateSettlingACardAuthorizationParameters
from openapi_server.models.simulates_advancing_the_state_of_a_card_dispute_parameters import SimulatesAdvancingTheStateOfACardDisputeParameters
from openapi_server.models.transaction import Transaction
from openapi_server.models.transaction_list import TransactionList
from openapi_server.models.update_a_card_parameters import UpdateACardParameters
from openapi_server.models.update_a_limit_parameters import UpdateALimitParameters
from openapi_server.models.update_an_account_number_parameters import UpdateAnAccountNumberParameters
from openapi_server.models.update_an_account_parameters import UpdateAnAccountParameters
from openapi_server.models.update_an_event_subscription_parameters import UpdateAnEventSubscriptionParameters
from openapi_server.models.update_an_external_account_parameters import UpdateAnExternalAccountParameters
from openapi_server.models.wire_drawdown_request import WireDrawdownRequest
from openapi_server.models.wire_drawdown_request_list import WireDrawdownRequestList
from openapi_server.models.wire_transfer import WireTransfer
from openapi_server.models.wire_transfer_list import WireTransferList


pytestmark = pytest.mark.asyncio

async def test_action_a_real_time_decision(client):
    """Test case for action_a_real_time_decision

    Action a Real-Time Decision
    """
    body = openapi_server.ActionARealTimeDecisionParameters()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/real_time_decisions/{real_time_decision_id}/action'.format(real_time_decision_id='real_time_decision_j76n2e810ezcg3zh5qtn'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_approve_a_check_transfer(client):
    """Test case for approve_a_check_transfer

    Approve a Check Transfer
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/check_transfers/{check_transfer_id}/approve'.format(check_transfer_id='check_transfer_30b43acfu9vw8fyc4f5'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_approve_a_wire_transfer(client):
    """Test case for approve_a_wire_transfer

    Approve a Wire Transfer
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/wire_transfers/{wire_transfer_id}/approve'.format(wire_transfer_id='wire_transfer_5akynk7dqsq25qwk9q2u'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_approve_an_account_transfer(client):
    """Test case for approve_an_account_transfer

    Approve an Account Transfer
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/account_transfers/{account_transfer_id}/approve'.format(account_transfer_id='account_transfer_7k9qe1ysdgqztnt63l7n'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_approve_an_ach_transfer(client):
    """Test case for approve_an_ach_transfer

    Approve an ACH Transfer
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/ach_transfers/{ach_transfer_id}/approve'.format(ach_transfer_id='ach_transfer_uoxatyh3lt5evrsdvo7q'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_cancel_a_pending_ach_transfer(client):
    """Test case for cancel_a_pending_ach_transfer

    Cancel a pending ACH Transfer
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/ach_transfers/{ach_transfer_id}/cancel'.format(ach_transfer_id='ach_transfer_uoxatyh3lt5evrsdvo7q'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_cancel_a_pending_check_transfer(client):
    """Test case for cancel_a_pending_check_transfer

    Cancel a pending Check Transfer
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/check_transfers/{check_transfer_id}/cancel'.format(check_transfer_id='check_transfer_30b43acfu9vw8fyc4f5'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_cancel_a_pending_wire_transfer(client):
    """Test case for cancel_a_pending_wire_transfer

    Cancel a pending Wire Transfer
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/wire_transfers/{wire_transfer_id}/cancel'.format(wire_transfer_id='wire_transfer_5akynk7dqsq25qwk9q2u'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_cancel_an_account_transfer(client):
    """Test case for cancel_an_account_transfer

    Cancel an Account Transfer
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/account_transfers/{account_transfer_id}/cancel'.format(account_transfer_id='account_transfer_7k9qe1ysdgqztnt63l7n'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_close_an_account(client):
    """Test case for close_an_account

    Close an Account
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/accounts/{account_id}/close'.format(account_id='account_in71c4amph0vgo2qllky'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_complete_a_sandbox_account_transfer(client):
    """Test case for complete_a_sandbox_account_transfer

    Complete a Sandbox Account Transfer
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/simulations/account_transfers/{account_transfer_id}/complete'.format(account_transfer_id='account_transfer_7k9qe1ysdgqztnt63l7n'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_complete_a_sandbox_real_time_payments_transfer(client):
    """Test case for complete_a_sandbox_real_time_payments_transfer

    Complete a Sandbox Real Time Payments Transfer
    """
    body = openapi_server.CompleteASandboxRealTimePaymentsTransferParameters()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/simulations/real_time_payments_transfers/{real_time_payments_transfer_id}/complete'.format(real_time_payments_transfer_id='real_time_payments_transfer_iyuhl5kdn7ssmup83mvq'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_a_bookkeeping_account(client):
    """Test case for create_a_bookkeeping_account

    Create a Bookkeeping Account
    """
    body = openapi_server.CreateABookkeepingAccountParameters()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/bookkeeping_accounts',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_a_bookkeeping_entry_set(client):
    """Test case for create_a_bookkeeping_entry_set

    Create a Bookkeeping Entry Set
    """
    body = openapi_server.CreateABookkeepingEntrySetParameters()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/bookkeeping_entry_sets',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_a_card(client):
    """Test case for create_a_card

    Create a Card
    """
    body = openapi_server.CreateACardParameters()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/cards',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_a_card_dispute(client):
    """Test case for create_a_card_dispute

    Create a Card Dispute
    """
    body = openapi_server.CreateACardDisputeParameters()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/card_disputes',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_a_card_profile(client):
    """Test case for create_a_card_profile

    Create a Card Profile
    """
    body = openapi_server.CreateACardProfileParameters()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/card_profiles',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_a_check_deposit(client):
    """Test case for create_a_check_deposit

    Create a Check Deposit
    """
    body = openapi_server.CreateACheckDepositParameters()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/check_deposits',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_a_check_transfer(client):
    """Test case for create_a_check_transfer

    Create a Check Transfer
    """
    body = openapi_server.CreateACheckTransferParameters()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/check_transfers',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("multipart/form-data not supported by Connexion")
async def test_create_a_file(client):
    """Test case for create_a_file

    Create a File
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'multipart/form-data',
        'Authorization': 'Bearer special-key',
    }
    data = FormData()
    data.add_field('description', 'description_example')
    data.add_field('file', '/path/to/file')
    data.add_field('purpose', 'purpose_example')
    response = await client.request(
        method='POST',
        path='/files',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_a_limit(client):
    """Test case for create_a_limit

    Create a Limit
    """
    body = openapi_server.CreateALimitParameters()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/limits',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_a_real_time_payments_transfer(client):
    """Test case for create_a_real_time_payments_transfer

    Create a Real Time Payments Transfer
    """
    body = openapi_server.CreateARealTimePaymentsTransferParameters()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/real_time_payments_transfers',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_a_supplemental_document_for_an_entity(client):
    """Test case for create_a_supplemental_document_for_an_entity

    Create a supplemental document for an Entity
    """
    body = openapi_server.CreateASupplementalDocumentForAnEntityParameters()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/entities/{entity_id}/supplemental_documents'.format(entity_id='entity_n8y8tnk2p9339ti393yi'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_a_wire_drawdown_request(client):
    """Test case for create_a_wire_drawdown_request

    Create a Wire Drawdown Request
    """
    body = openapi_server.CreateAWireDrawdownRequestParameters()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/wire_drawdown_requests',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_a_wire_transfer(client):
    """Test case for create_a_wire_transfer

    Create a Wire Transfer
    """
    body = openapi_server.CreateAWireTransferParameters()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/wire_transfers',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_an_account(client):
    """Test case for create_an_account

    Create an Account
    """
    body = openapi_server.CreateAnAccountParameters()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/accounts',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_an_account_number(client):
    """Test case for create_an_account_number

    Create an Account Number
    """
    body = openapi_server.CreateAnAccountNumberParameters()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/account_numbers',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_an_account_transfer(client):
    """Test case for create_an_account_transfer

    Create an Account Transfer
    """
    body = openapi_server.CreateAnAccountTransferParameters()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/account_transfers',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_an_ach_prenotification(client):
    """Test case for create_an_ach_prenotification

    Create an ACH Prenotification
    """
    body = openapi_server.CreateAnAchPrenotificationParameters()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/ach_prenotifications',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_an_ach_return(client):
    """Test case for create_an_ach_return

    Create an ACH Return
    """
    body = openapi_server.CreateAnAchReturnParameters()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/inbound_ach_transfer_returns',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_an_ach_transfer(client):
    """Test case for create_an_ach_transfer

    Create an ACH Transfer
    """
    body = openapi_server.CreateAnAchTransferParameters()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/ach_transfers',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_an_entity(client):
    """Test case for create_an_entity

    Create an Entity
    """
    body = openapi_server.CreateAnEntityParameters()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/entities',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_an_event_subscription(client):
    """Test case for create_an_event_subscription

    Create an Event Subscription
    """
    body = openapi_server.CreateAnEventSubscriptionParameters()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/event_subscriptions',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_an_export(client):
    """Test case for create_an_export

    Create an Export
    """
    body = openapi_server.CreateAnExportParameters()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/exports',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_an_external_account(client):
    """Test case for create_an_external_account

    Create an External Account
    """
    body = openapi_server.CreateAnExternalAccountParameters()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/external_accounts',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_deposit_a_sandbox_check_transfer(client):
    """Test case for deposit_a_sandbox_check_transfer

    Deposit a Sandbox Check Transfer
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/simulations/check_transfers/{check_transfer_id}/deposit'.format(check_transfer_id='check_transfer_30b43acfu9vw8fyc4f5'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_account_numbers(client):
    """Test case for list_account_numbers

    List Account Numbers
    """
    params = [('cursor', 'cursor_example'),
                    ('limit', 56),
                    ('status', 'status_example'),
                    ('account_id', 'account_id_example'),
                    ('created_at.after', '2013-10-20T19:20:30+01:00'),
                    ('created_at.before', '2013-10-20T19:20:30+01:00'),
                    ('created_at.on_or_after', '2013-10-20T19:20:30+01:00'),
                    ('created_at.on_or_before', '2013-10-20T19:20:30+01:00')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/account_numbers',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_account_statements(client):
    """Test case for list_account_statements

    List Account Statements
    """
    params = [('cursor', 'cursor_example'),
                    ('limit', 56),
                    ('account_id', 'account_in71c4amph0vgo2qllky'),
                    ('statement_period_start.after', '2013-10-20T19:20:30+01:00'),
                    ('statement_period_start.before', '2013-10-20T19:20:30+01:00'),
                    ('statement_period_start.on_or_after', '2013-10-20T19:20:30+01:00'),
                    ('statement_period_start.on_or_before', '2013-10-20T19:20:30+01:00')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/account_statements',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_account_transfers(client):
    """Test case for list_account_transfers

    List Account Transfers
    """
    params = [('cursor', 'cursor_example'),
                    ('limit', 56),
                    ('account_id', 'account_in71c4amph0vgo2qllky'),
                    ('created_at.after', '2013-10-20T19:20:30+01:00'),
                    ('created_at.before', '2013-10-20T19:20:30+01:00'),
                    ('created_at.on_or_after', '2013-10-20T19:20:30+01:00'),
                    ('created_at.on_or_before', '2013-10-20T19:20:30+01:00')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/account_transfers',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_accounts(client):
    """Test case for list_accounts

    List Accounts
    """
    params = [('cursor', 'cursor_example'),
                    ('limit', 56),
                    ('entity_id', 'entity_n8y8tnk2p9339ti393yi'),
                    ('status', 'status_example'),
                    ('created_at.after', '2013-10-20T19:20:30+01:00'),
                    ('created_at.before', '2013-10-20T19:20:30+01:00'),
                    ('created_at.on_or_after', '2013-10-20T19:20:30+01:00'),
                    ('created_at.on_or_before', '2013-10-20T19:20:30+01:00')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/accounts',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_ach_prenotifications(client):
    """Test case for list_ach_prenotifications

    List ACH Prenotifications
    """
    params = [('cursor', 'cursor_example'),
                    ('limit', 56),
                    ('created_at.after', '2013-10-20T19:20:30+01:00'),
                    ('created_at.before', '2013-10-20T19:20:30+01:00'),
                    ('created_at.on_or_after', '2013-10-20T19:20:30+01:00'),
                    ('created_at.on_or_before', '2013-10-20T19:20:30+01:00')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/ach_prenotifications',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_ach_transfers(client):
    """Test case for list_ach_transfers

    List ACH Transfers
    """
    params = [('cursor', 'cursor_example'),
                    ('limit', 56),
                    ('account_id', 'account_in71c4amph0vgo2qllky'),
                    ('external_account_id', 'external_account_id_example'),
                    ('created_at.after', '2013-10-20T19:20:30+01:00'),
                    ('created_at.before', '2013-10-20T19:20:30+01:00'),
                    ('created_at.on_or_after', '2013-10-20T19:20:30+01:00'),
                    ('created_at.on_or_before', '2013-10-20T19:20:30+01:00')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/ach_transfers',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_bookkeeping_accounts(client):
    """Test case for list_bookkeeping_accounts

    List Bookkeeping Accounts
    """
    params = [('cursor', 'cursor_example'),
                    ('limit', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/bookkeeping_accounts',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_bookkeeping_entries(client):
    """Test case for list_bookkeeping_entries

    List Bookkeeping Entries
    """
    params = [('cursor', 'cursor_example'),
                    ('limit', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/bookkeeping_entries',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_card_disputes(client):
    """Test case for list_card_disputes

    List Card Disputes
    """
    params = [('cursor', 'cursor_example'),
                    ('limit', 56),
                    ('created_at.after', '2013-10-20T19:20:30+01:00'),
                    ('created_at.before', '2013-10-20T19:20:30+01:00'),
                    ('created_at.on_or_after', '2013-10-20T19:20:30+01:00'),
                    ('created_at.on_or_before', '2013-10-20T19:20:30+01:00'),
                    ('status.in', ['status_in_example'])]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/card_disputes',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_card_profiles(client):
    """Test case for list_card_profiles

    List Card Profiles
    """
    params = [('cursor', 'cursor_example'),
                    ('limit', 56),
                    ('status.in', ['status_in_example'])]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/card_profiles',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_cards(client):
    """Test case for list_cards

    List Cards
    """
    params = [('cursor', 'cursor_example'),
                    ('limit', 56),
                    ('account_id', 'account_in71c4amph0vgo2qllky'),
                    ('created_at.after', '2013-10-20T19:20:30+01:00'),
                    ('created_at.before', '2013-10-20T19:20:30+01:00'),
                    ('created_at.on_or_after', '2013-10-20T19:20:30+01:00'),
                    ('created_at.on_or_before', '2013-10-20T19:20:30+01:00')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/cards',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_check_deposits(client):
    """Test case for list_check_deposits

    List Check Deposits
    """
    params = [('cursor', 'cursor_example'),
                    ('limit', 56),
                    ('account_id', 'account_in71c4amph0vgo2qllky'),
                    ('created_at.after', '2013-10-20T19:20:30+01:00'),
                    ('created_at.before', '2013-10-20T19:20:30+01:00'),
                    ('created_at.on_or_after', '2013-10-20T19:20:30+01:00'),
                    ('created_at.on_or_before', '2013-10-20T19:20:30+01:00')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/check_deposits',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_check_transfers(client):
    """Test case for list_check_transfers

    List Check Transfers
    """
    params = [('cursor', 'cursor_example'),
                    ('limit', 56),
                    ('account_id', 'account_in71c4amph0vgo2qllky'),
                    ('created_at.after', '2013-10-20T19:20:30+01:00'),
                    ('created_at.before', '2013-10-20T19:20:30+01:00'),
                    ('created_at.on_or_after', '2013-10-20T19:20:30+01:00'),
                    ('created_at.on_or_before', '2013-10-20T19:20:30+01:00')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/check_transfers',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_declined_transactions(client):
    """Test case for list_declined_transactions

    List Declined Transactions
    """
    params = [('cursor', 'cursor_example'),
                    ('limit', 56),
                    ('account_id', 'account_id_example'),
                    ('created_at.after', '2013-10-20T19:20:30+01:00'),
                    ('created_at.before', '2013-10-20T19:20:30+01:00'),
                    ('created_at.on_or_after', '2013-10-20T19:20:30+01:00'),
                    ('created_at.on_or_before', '2013-10-20T19:20:30+01:00'),
                    ('route_id', 'route_id_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/declined_transactions',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_digital_wallet_tokens(client):
    """Test case for list_digital_wallet_tokens

    List Digital Wallet Tokens
    """
    params = [('cursor', 'cursor_example'),
                    ('limit', 56),
                    ('card_id', 'card_oubs0hwk5rn6knuecxg2'),
                    ('created_at.after', '2013-10-20T19:20:30+01:00'),
                    ('created_at.before', '2013-10-20T19:20:30+01:00'),
                    ('created_at.on_or_after', '2013-10-20T19:20:30+01:00'),
                    ('created_at.on_or_before', '2013-10-20T19:20:30+01:00')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/digital_wallet_tokens',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_documents(client):
    """Test case for list_documents

    List Documents
    """
    params = [('cursor', 'cursor_example'),
                    ('limit', 56),
                    ('entity_id', 'entity_id_example'),
                    ('category.in', ['category_in_example']),
                    ('created_at.after', '2013-10-20T19:20:30+01:00'),
                    ('created_at.before', '2013-10-20T19:20:30+01:00'),
                    ('created_at.on_or_after', '2013-10-20T19:20:30+01:00'),
                    ('created_at.on_or_before', '2013-10-20T19:20:30+01:00')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/documents',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_entities(client):
    """Test case for list_entities

    List Entities
    """
    params = [('cursor', 'cursor_example'),
                    ('limit', 56),
                    ('created_at.after', '2013-10-20T19:20:30+01:00'),
                    ('created_at.before', '2013-10-20T19:20:30+01:00'),
                    ('created_at.on_or_after', '2013-10-20T19:20:30+01:00'),
                    ('created_at.on_or_before', '2013-10-20T19:20:30+01:00')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/entities',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_event_subscriptions(client):
    """Test case for list_event_subscriptions

    List Event Subscriptions
    """
    params = [('cursor', 'cursor_example'),
                    ('limit', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/event_subscriptions',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_events(client):
    """Test case for list_events

    List Events
    """
    params = [('cursor', 'cursor_example'),
                    ('limit', 56),
                    ('created_at.after', '2013-10-20T19:20:30+01:00'),
                    ('created_at.before', '2013-10-20T19:20:30+01:00'),
                    ('created_at.on_or_after', '2013-10-20T19:20:30+01:00'),
                    ('created_at.on_or_before', '2013-10-20T19:20:30+01:00'),
                    ('category.in', ['category_in_example']),
                    ('associated_object_id', 'associated_object_id_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/events',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_exports(client):
    """Test case for list_exports

    List Exports
    """
    params = [('cursor', 'cursor_example'),
                    ('limit', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/exports',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_external_accounts(client):
    """Test case for list_external_accounts

    List External Accounts
    """
    params = [('cursor', 'cursor_example'),
                    ('limit', 56),
                    ('status.in', ['status_in_example'])]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/external_accounts',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_files(client):
    """Test case for list_files

    List Files
    """
    params = [('cursor', 'cursor_example'),
                    ('limit', 56),
                    ('created_at.after', '2013-10-20T19:20:30+01:00'),
                    ('created_at.before', '2013-10-20T19:20:30+01:00'),
                    ('created_at.on_or_after', '2013-10-20T19:20:30+01:00'),
                    ('created_at.on_or_before', '2013-10-20T19:20:30+01:00'),
                    ('purpose.in', ['purpose_in_example'])]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/files',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_inbound_ach_transfer_returns(client):
    """Test case for list_inbound_ach_transfer_returns

    List Inbound ACH Transfer Returns
    """
    params = [('cursor', 'cursor_example'),
                    ('limit', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/inbound_ach_transfer_returns',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_inbound_wire_drawdown_requests(client):
    """Test case for list_inbound_wire_drawdown_requests

    List Inbound Wire Drawdown Requests
    """
    params = [('cursor', 'cursor_example'),
                    ('limit', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/inbound_wire_drawdown_requests',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_limits(client):
    """Test case for list_limits

    List Limits
    """
    params = [('cursor', 'cursor_example'),
                    ('limit', 56),
                    ('model_id', 'account_number_v18nkfqm6afpsrvy82b2'),
                    ('status', 'active')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/limits',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_oauth_connections(client):
    """Test case for list_oauth_connections

    List OAuth Connections
    """
    params = [('cursor', 'cursor_example'),
                    ('limit', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/oauth_connections',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_pending_transactions(client):
    """Test case for list_pending_transactions

    List Pending Transactions
    """
    params = [('cursor', 'cursor_example'),
                    ('limit', 56),
                    ('account_id', 'account_id_example'),
                    ('route_id', 'route_id_example'),
                    ('source_id', 'source_id_example'),
                    ('status.in', ['status_in_example']),
                    ('created_at.after', '2013-10-20T19:20:30+01:00'),
                    ('created_at.before', '2013-10-20T19:20:30+01:00'),
                    ('created_at.on_or_after', '2013-10-20T19:20:30+01:00'),
                    ('created_at.on_or_before', '2013-10-20T19:20:30+01:00')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/pending_transactions',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_programs(client):
    """Test case for list_programs

    List Programs
    """
    params = [('cursor', 'cursor_example'),
                    ('limit', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/programs',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_real_time_payments_transfers(client):
    """Test case for list_real_time_payments_transfers

    List Real Time Payments Transfers
    """
    params = [('cursor', 'cursor_example'),
                    ('limit', 56),
                    ('account_id', 'account_in71c4amph0vgo2qllky'),
                    ('external_account_id', 'external_account_id_example'),
                    ('created_at.after', '2013-10-20T19:20:30+01:00'),
                    ('created_at.before', '2013-10-20T19:20:30+01:00'),
                    ('created_at.on_or_after', '2013-10-20T19:20:30+01:00'),
                    ('created_at.on_or_before', '2013-10-20T19:20:30+01:00')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/real_time_payments_transfers',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_routing_numbers(client):
    """Test case for list_routing_numbers

    List Routing Numbers
    """
    params = [('cursor', 'cursor_example'),
                    ('limit', 56),
                    ('routing_number', '021000021')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/routing_numbers',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_transactions(client):
    """Test case for list_transactions

    List Transactions
    """
    params = [('cursor', 'cursor_example'),
                    ('limit', 56),
                    ('account_id', 'account_id_example'),
                    ('created_at.after', '2013-10-20T19:20:30+01:00'),
                    ('created_at.before', '2013-10-20T19:20:30+01:00'),
                    ('created_at.on_or_after', '2013-10-20T19:20:30+01:00'),
                    ('created_at.on_or_before', '2013-10-20T19:20:30+01:00'),
                    ('category.in', ['category_in_example']),
                    ('route_id', 'route_id_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/transactions',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_wire_drawdown_requests(client):
    """Test case for list_wire_drawdown_requests

    List Wire Drawdown Requests
    """
    params = [('cursor', 'cursor_example'),
                    ('limit', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/wire_drawdown_requests',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_wire_transfers(client):
    """Test case for list_wire_transfers

    List Wire Transfers
    """
    params = [('cursor', 'cursor_example'),
                    ('limit', 56),
                    ('account_id', 'account_in71c4amph0vgo2qllky'),
                    ('external_account_id', 'external_account_id_example'),
                    ('created_at.after', '2013-10-20T19:20:30+01:00'),
                    ('created_at.before', '2013-10-20T19:20:30+01:00'),
                    ('created_at.on_or_after', '2013-10-20T19:20:30+01:00'),
                    ('created_at.on_or_before', '2013-10-20T19:20:30+01:00')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/wire_transfers',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_look_up_the_balance_for_an_account(client):
    """Test case for look_up_the_balance_for_an_account

    Look up the balance for an Account
    """
    body = openapi_server.LookUpTheBalanceForAnAccountParameters()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/balance_lookups',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_mail_a_sandbox_check_transfer(client):
    """Test case for mail_a_sandbox_check_transfer

    Mail a Sandbox Check Transfer
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/simulations/check_transfers/{check_transfer_id}/mail'.format(check_transfer_id='check_transfer_30b43acfu9vw8fyc4f5'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_reject_a_sandbox_check_deposit(client):
    """Test case for reject_a_sandbox_check_deposit

    Reject a Sandbox Check Deposit
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/simulations/check_deposits/{check_deposit_id}/reject'.format(check_deposit_id='check_deposit_f06n9gpg7sxn8t19lfc1'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_request_a_stop_payment_on_a_check_transfer(client):
    """Test case for request_a_stop_payment_on_a_check_transfer

    Request a stop payment on a Check Transfer
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/check_transfers/{check_transfer_id}/stop_payment'.format(check_transfer_id='check_transfer_30b43acfu9vw8fyc4f5'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_retrieve_a_card(client):
    """Test case for retrieve_a_card

    Retrieve a Card
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/cards/{card_id}'.format(card_id='card_oubs0hwk5rn6knuecxg2'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_retrieve_a_card_dispute(client):
    """Test case for retrieve_a_card_dispute

    Retrieve a Card Dispute
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/card_disputes/{card_dispute_id}'.format(card_dispute_id='card_dispute_h9sc95nbl1cgltpp7men'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_retrieve_a_card_profile(client):
    """Test case for retrieve_a_card_profile

    Retrieve a Card Profile
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/card_profiles/{card_profile_id}'.format(card_profile_id='card_profile_cox5y73lob2eqly18piy'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_retrieve_a_check_deposit(client):
    """Test case for retrieve_a_check_deposit

    Retrieve a Check Deposit
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/check_deposits/{check_deposit_id}'.format(check_deposit_id='check_deposit_instruction_q2shv7x9qhevfm71kor8'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_retrieve_a_check_transfer(client):
    """Test case for retrieve_a_check_transfer

    Retrieve a Check Transfer
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/check_transfers/{check_transfer_id}'.format(check_transfer_id='check_transfer_30b43acfu9vw8fyc4f5'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_retrieve_a_declined_transaction(client):
    """Test case for retrieve_a_declined_transaction

    Retrieve a Declined Transaction
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/declined_transactions/{declined_transaction_id}'.format(declined_transaction_id='declined_transaction_17jbn0yyhvkt4v4ooym8'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_retrieve_a_digital_wallet_token(client):
    """Test case for retrieve_a_digital_wallet_token

    Retrieve a Digital Wallet Token
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/digital_wallet_tokens/{digital_wallet_token_id}'.format(digital_wallet_token_id='digital_wallet_token_izi62go3h51p369jrie0'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_retrieve_a_document(client):
    """Test case for retrieve_a_document

    Retrieve a Document
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/documents/{document_id}'.format(document_id='document_qjtqc6s4c14ve2q89izm'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_retrieve_a_file(client):
    """Test case for retrieve_a_file

    Retrieve a File
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/files/{file_id}'.format(file_id='file_makxrc67oh9l6sg7w9yc'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_retrieve_a_limit(client):
    """Test case for retrieve_a_limit

    Retrieve a Limit
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/limits/{limit_id}'.format(limit_id='limit_fku42k0qtc8ulsuas38q'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_retrieve_a_pending_transaction(client):
    """Test case for retrieve_a_pending_transaction

    Retrieve a Pending Transaction
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/pending_transactions/{pending_transaction_id}'.format(pending_transaction_id='pending_transaction_k1sfetcau2qbvjbzgju4'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_retrieve_a_program(client):
    """Test case for retrieve_a_program

    Retrieve a Program
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/programs/{program_id}'.format(program_id='program_i2v2os4mwza1oetokh9i'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_retrieve_a_real_time_decision(client):
    """Test case for retrieve_a_real_time_decision

    Retrieve a Real-Time Decision
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/real_time_decisions/{real_time_decision_id}'.format(real_time_decision_id='real_time_decision_j76n2e810ezcg3zh5qtn'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_retrieve_a_real_time_payments_transfer(client):
    """Test case for retrieve_a_real_time_payments_transfer

    Retrieve a Real Time Payments Transfer
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/real_time_payments_transfers/{real_time_payments_transfer_id}'.format(real_time_payments_transfer_id='real_time_payments_transfer_iyuhl5kdn7ssmup83mvq'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_retrieve_a_transaction(client):
    """Test case for retrieve_a_transaction

    Retrieve a Transaction
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/transactions/{transaction_id}'.format(transaction_id='transaction_uyrp7fld2ium70oa7oi'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_retrieve_a_wire_drawdown_request(client):
    """Test case for retrieve_a_wire_drawdown_request

    Retrieve a Wire Drawdown Request
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/wire_drawdown_requests/{wire_drawdown_request_id}'.format(wire_drawdown_request_id='wire_drawdown_request_q6lmocus3glo0lr2bfv3'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_retrieve_a_wire_transfer(client):
    """Test case for retrieve_a_wire_transfer

    Retrieve a Wire Transfer
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/wire_transfers/{wire_transfer_id}'.format(wire_transfer_id='wire_transfer_5akynk7dqsq25qwk9q2u'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_retrieve_an_account(client):
    """Test case for retrieve_an_account

    Retrieve an Account
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/accounts/{account_id}'.format(account_id='account_in71c4amph0vgo2qllky'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_retrieve_an_account_number(client):
    """Test case for retrieve_an_account_number

    Retrieve an Account Number
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/account_numbers/{account_number_id}'.format(account_number_id='account_number_v18nkfqm6afpsrvy82b2'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_retrieve_an_account_statement(client):
    """Test case for retrieve_an_account_statement

    Retrieve an Account Statement
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/account_statements/{account_statement_id}'.format(account_statement_id='account_statement_lkc03a4skm2k7f38vj15'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_retrieve_an_account_transfer(client):
    """Test case for retrieve_an_account_transfer

    Retrieve an Account Transfer
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/account_transfers/{account_transfer_id}'.format(account_transfer_id='account_transfer_7k9qe1ysdgqztnt63l7n'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_retrieve_an_ach_prenotification(client):
    """Test case for retrieve_an_ach_prenotification

    Retrieve an ACH Prenotification
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/ach_prenotifications/{ach_prenotification_id}'.format(ach_prenotification_id='ach_prenotification_ubjf9qqsxl3obbcn1u34'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_retrieve_an_ach_transfer(client):
    """Test case for retrieve_an_ach_transfer

    Retrieve an ACH Transfer
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/ach_transfers/{ach_transfer_id}'.format(ach_transfer_id='ach_transfer_uoxatyh3lt5evrsdvo7q'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_retrieve_an_entity(client):
    """Test case for retrieve_an_entity

    Retrieve an Entity
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/entities/{entity_id}'.format(entity_id='entity_n8y8tnk2p9339ti393yi'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_retrieve_an_event(client):
    """Test case for retrieve_an_event

    Retrieve an Event
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/events/{event_id}'.format(event_id='event_001dzz0r20rzr4zrhrr1364hy80'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_retrieve_an_event_subscription(client):
    """Test case for retrieve_an_event_subscription

    Retrieve an Event Subscription
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/event_subscriptions/{event_subscription_id}'.format(event_subscription_id='event_subscription_001dzz0r20rcdxgb013zqb8m04g'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_retrieve_an_export(client):
    """Test case for retrieve_an_export

    Retrieve an Export
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/exports/{export_id}'.format(export_id='export_8s4m48qz3bclzje0zwh9'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_retrieve_an_external_account(client):
    """Test case for retrieve_an_external_account

    Retrieve an External Account
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/external_accounts/{external_account_id}'.format(external_account_id='external_account_ukk55lr923a3ac0pp7iv'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_retrieve_an_inbound_ach_transfer_return(client):
    """Test case for retrieve_an_inbound_ach_transfer_return

    Retrieve an Inbound ACH Transfer Return
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/inbound_ach_transfer_returns/{inbound_ach_transfer_return_id}'.format(inbound_ach_transfer_return_id='inbound_ach_transfer_return_fhcxk5huskwhmt7iz0gk'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_retrieve_an_inbound_wire_drawdown_request(client):
    """Test case for retrieve_an_inbound_wire_drawdown_request

    Retrieve an Inbound Wire Drawdown Request
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/inbound_wire_drawdown_requests/{inbound_wire_drawdown_request_id}'.format(inbound_wire_drawdown_request_id='inbound_wire_drawdown_request_u5a92ikqhz1ytphn799e'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_retrieve_an_oauth_connection(client):
    """Test case for retrieve_an_oauth_connection

    Retrieve an OAuth Connection
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/oauth_connections/{oauth_connection_id}'.format(oauth_connection_id='connection_dauknoksyr4wilz4e6my'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_retrieve_group_details(client):
    """Test case for retrieve_group_details

    Retrieve Group details
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/groups/current',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_retrieve_sensitive_details_for_a_card(client):
    """Test case for retrieve_sensitive_details_for_a_card

    Retrieve sensitive details for a Card
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/cards/{card_id}/details'.format(card_id='card_oubs0hwk5rn6knuecxg2'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_return_a_sandbox_ach_transfer(client):
    """Test case for return_a_sandbox_ach_transfer

    Return a Sandbox ACH Transfer
    """
    body = openapi_server.ReturnASandboxAchTransferParameters()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/simulations/ach_transfers/{ach_transfer_id}/return'.format(ach_transfer_id='ach_transfer_uoxatyh3lt5evrsdvo7q'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_return_a_sandbox_check_deposit(client):
    """Test case for return_a_sandbox_check_deposit

    Return a Sandbox Check Deposit
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/simulations/check_deposits/{check_deposit_id}/return'.format(check_deposit_id='check_deposit_f06n9gpg7sxn8t19lfc1'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_return_a_sandbox_check_transfer(client):
    """Test case for return_a_sandbox_check_transfer

    Return a Sandbox Check Transfer
    """
    body = openapi_server.ReturnASandboxCheckTransferParameters()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/simulations/check_transfers/{check_transfer_id}/return'.format(check_transfer_id='check_transfer_30b43acfu9vw8fyc4f5'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_reverse_a_sandbox_wire_transfer(client):
    """Test case for reverse_a_sandbox_wire_transfer

    Reverse a Sandbox Wire Transfer
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/simulations/wire_transfers/{wire_transfer_id}/reverse'.format(wire_transfer_id='wire_transfer_5akynk7dqsq25qwk9q2u'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_simulate_a_real_time_payments_transfer_to_your_account(client):
    """Test case for simulate_a_real_time_payments_transfer_to_your_account

    Simulate a Real Time Payments Transfer to your account
    """
    body = openapi_server.SimulateARealTimePaymentsTransferToYourAccountParameters()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/simulations/inbound_real_time_payments_transfers',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_simulate_a_refund_on_a_card(client):
    """Test case for simulate_a_refund_on_a_card

    Simulate a refund on a card
    """
    body = openapi_server.SimulateARefundOnACardParameters()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/simulations/card_refunds',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_simulate_a_tax_document_being_created(client):
    """Test case for simulate_a_tax_document_being_created

    Simulate a tax document being created
    """
    body = openapi_server.SimulateATaxDocumentBeingCreatedParameters()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/simulations/documents',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_simulate_a_wire_transfer_to_your_account(client):
    """Test case for simulate_a_wire_transfer_to_your_account

    Simulate a Wire Transfer to your account
    """
    body = openapi_server.SimulateAWireTransferToYourAccountParameters()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/simulations/inbound_wire_transfers',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_simulate_an_account_statement_being_created(client):
    """Test case for simulate_an_account_statement_being_created

    Simulate an Account Statement being created
    """
    body = openapi_server.SimulateAnAccountStatementBeingCreatedParameters()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/simulations/account_statements',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_simulate_an_ach_transfer_to_your_account(client):
    """Test case for simulate_an_ach_transfer_to_your_account

    Simulate an ACH Transfer to your account
    """
    body = openapi_server.SimulateAnAchTransferToYourAccountParameters()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/simulations/inbound_ach_transfers',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_simulate_an_authorization_on_a_card(client):
    """Test case for simulate_an_authorization_on_a_card

    Simulate an authorization on a Card
    """
    body = openapi_server.SimulateAnAuthorizationOnACardParameters()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/simulations/card_authorizations',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_simulate_an_inbound_wire_drawdown_request_being_created(client):
    """Test case for simulate_an_inbound_wire_drawdown_request_being_created

    Simulate an Inbound Wire Drawdown request being created
    """
    body = openapi_server.SimulateAnInboundWireDrawdownRequestBeingCreatedParameters()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/simulations/inbound_wire_drawdown_requests',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_simulate_an_interest_payment_to_your_account(client):
    """Test case for simulate_an_interest_payment_to_your_account

    Simulate an Interest Payment to your account
    """
    body = openapi_server.SimulateAnInterestPaymentToYourAccountParameters()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/simulations/interest_payment',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_simulate_digital_wallet_provisioning_for_a_card(client):
    """Test case for simulate_digital_wallet_provisioning_for_a_card

    Simulate digital wallet provisioning for a card
    """
    body = openapi_server.SimulateDigitalWalletProvisioningForACardParameters()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/simulations/digital_wallet_token_requests',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_simulate_settling_a_card_authorization(client):
    """Test case for simulate_settling_a_card_authorization

    Simulate settling a card authorization
    """
    body = openapi_server.SimulateSettlingACardAuthorizationParameters()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/simulations/card_settlements',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_simulates_advancing_the_state_of_a_card_dispute(client):
    """Test case for simulates_advancing_the_state_of_a_card_dispute

    Simulates advancing the state of a card dispute
    """
    body = openapi_server.SimulatesAdvancingTheStateOfACardDisputeParameters()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/simulations/card_disputes/{card_dispute_id}/action'.format(card_dispute_id='card_dispute_h9sc95nbl1cgltpp7men'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_submit_a_sandbox_ach_transfer(client):
    """Test case for submit_a_sandbox_ach_transfer

    Submit a Sandbox ACH Transfer
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/simulations/ach_transfers/{ach_transfer_id}/submit'.format(ach_transfer_id='ach_transfer_uoxatyh3lt5evrsdvo7q'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_submit_a_sandbox_check_deposit(client):
    """Test case for submit_a_sandbox_check_deposit

    Submit a Sandbox Check Deposit
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/simulations/check_deposits/{check_deposit_id}/submit'.format(check_deposit_id='check_deposit_f06n9gpg7sxn8t19lfc1'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_submit_a_sandbox_wire_transfer(client):
    """Test case for submit_a_sandbox_wire_transfer

    Submit a Sandbox Wire Transfer
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/simulations/wire_transfers/{wire_transfer_id}/submit'.format(wire_transfer_id='wire_transfer_5akynk7dqsq25qwk9q2u'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_a_card(client):
    """Test case for update_a_card

    Update a Card
    """
    body = openapi_server.UpdateACardParameters()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/cards/{card_id}'.format(card_id='card_oubs0hwk5rn6knuecxg2'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_a_limit(client):
    """Test case for update_a_limit

    Update a Limit
    """
    body = openapi_server.UpdateALimitParameters()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/limits/{limit_id}'.format(limit_id='limit_fku42k0qtc8ulsuas38q'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_an_account(client):
    """Test case for update_an_account

    Update an Account
    """
    body = openapi_server.UpdateAnAccountParameters()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/accounts/{account_id}'.format(account_id='account_in71c4amph0vgo2qllky'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_an_account_number(client):
    """Test case for update_an_account_number

    Update an Account Number
    """
    body = openapi_server.UpdateAnAccountNumberParameters()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/account_numbers/{account_number_id}'.format(account_number_id='account_number_v18nkfqm6afpsrvy82b2'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_an_event_subscription(client):
    """Test case for update_an_event_subscription

    Update an Event Subscription
    """
    body = openapi_server.UpdateAnEventSubscriptionParameters()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/event_subscriptions/{event_subscription_id}'.format(event_subscription_id='event_subscription_001dzz0r20rcdxgb013zqb8m04g'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_an_external_account(client):
    """Test case for update_an_external_account

    Update an External Account
    """
    body = openapi_server.UpdateAnExternalAccountParameters()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/external_accounts/{external_account_id}'.format(external_account_id='external_account_ukk55lr923a3ac0pp7iv'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

