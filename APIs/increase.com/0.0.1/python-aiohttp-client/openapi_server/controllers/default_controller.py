from typing import List, Dict
from aiohttp import web

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
from openapi_server import util


async def action_a_real_time_decision(request: web.Request, real_time_decision_id, body) -> web.Response:
    """Action a Real-Time Decision

    

    :param real_time_decision_id: 
    :type real_time_decision_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = ActionARealTimeDecisionParameters.from_dict(body)
    return web.Response(status=200)


async def approve_a_check_transfer(request: web.Request, check_transfer_id) -> web.Response:
    """Approve a Check Transfer

    

    :param check_transfer_id: 
    :type check_transfer_id: str

    """
    return web.Response(status=200)


async def approve_a_wire_transfer(request: web.Request, wire_transfer_id) -> web.Response:
    """Approve a Wire Transfer

    

    :param wire_transfer_id: 
    :type wire_transfer_id: str

    """
    return web.Response(status=200)


async def approve_an_account_transfer(request: web.Request, account_transfer_id) -> web.Response:
    """Approve an Account Transfer

    

    :param account_transfer_id: 
    :type account_transfer_id: str

    """
    return web.Response(status=200)


async def approve_an_ach_transfer(request: web.Request, ach_transfer_id) -> web.Response:
    """Approve an ACH Transfer

    Approves an ACH Transfer in a pending_approval state.

    :param ach_transfer_id: 
    :type ach_transfer_id: str

    """
    return web.Response(status=200)


async def cancel_a_pending_ach_transfer(request: web.Request, ach_transfer_id) -> web.Response:
    """Cancel a pending ACH Transfer

    Cancels an ACH Transfer in a pending_approval state.

    :param ach_transfer_id: 
    :type ach_transfer_id: str

    """
    return web.Response(status=200)


async def cancel_a_pending_check_transfer(request: web.Request, check_transfer_id) -> web.Response:
    """Cancel a pending Check Transfer

    

    :param check_transfer_id: 
    :type check_transfer_id: str

    """
    return web.Response(status=200)


async def cancel_a_pending_wire_transfer(request: web.Request, wire_transfer_id) -> web.Response:
    """Cancel a pending Wire Transfer

    

    :param wire_transfer_id: 
    :type wire_transfer_id: str

    """
    return web.Response(status=200)


async def cancel_an_account_transfer(request: web.Request, account_transfer_id) -> web.Response:
    """Cancel an Account Transfer

    

    :param account_transfer_id: 
    :type account_transfer_id: str

    """
    return web.Response(status=200)


async def close_an_account(request: web.Request, account_id) -> web.Response:
    """Close an Account

    

    :param account_id: 
    :type account_id: str

    """
    return web.Response(status=200)


async def complete_a_sandbox_account_transfer(request: web.Request, account_transfer_id) -> web.Response:
    """Complete a Sandbox Account Transfer

    If your account is configured to require approval for each transfer, this endpoint simulates the approval of an [Account Transfer](#account-transfers). You can also approve sandbox Account Transfers in the dashboard. This transfer must first have a &#x60;status&#x60; of &#x60;pending_approval&#x60;.

    :param account_transfer_id: 
    :type account_transfer_id: str

    """
    return web.Response(status=200)


async def complete_a_sandbox_real_time_payments_transfer(request: web.Request, real_time_payments_transfer_id, body) -> web.Response:
    """Complete a Sandbox Real Time Payments Transfer

    Simulates submission of a Real Time Payments transfer and handling the response from the destination financial institution. This transfer must first have a &#x60;status&#x60; of &#x60;pending_submission&#x60;.

    :param real_time_payments_transfer_id: 
    :type real_time_payments_transfer_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = CompleteASandboxRealTimePaymentsTransferParameters.from_dict(body)
    return web.Response(status=200)


async def create_a_bookkeeping_account(request: web.Request, body) -> web.Response:
    """Create a Bookkeeping Account

    

    :param body: 
    :type body: dict | bytes

    """
    body = CreateABookkeepingAccountParameters.from_dict(body)
    return web.Response(status=200)


async def create_a_bookkeeping_entry_set(request: web.Request, body) -> web.Response:
    """Create a Bookkeeping Entry Set

    

    :param body: 
    :type body: dict | bytes

    """
    body = CreateABookkeepingEntrySetParameters.from_dict(body)
    return web.Response(status=200)


async def create_a_card(request: web.Request, body) -> web.Response:
    """Create a Card

    

    :param body: 
    :type body: dict | bytes

    """
    body = CreateACardParameters.from_dict(body)
    return web.Response(status=200)


async def create_a_card_dispute(request: web.Request, body) -> web.Response:
    """Create a Card Dispute

    

    :param body: 
    :type body: dict | bytes

    """
    body = CreateACardDisputeParameters.from_dict(body)
    return web.Response(status=200)


async def create_a_card_profile(request: web.Request, body) -> web.Response:
    """Create a Card Profile

    

    :param body: 
    :type body: dict | bytes

    """
    body = CreateACardProfileParameters.from_dict(body)
    return web.Response(status=200)


async def create_a_check_deposit(request: web.Request, body) -> web.Response:
    """Create a Check Deposit

    

    :param body: 
    :type body: dict | bytes

    """
    body = CreateACheckDepositParameters.from_dict(body)
    return web.Response(status=200)


async def create_a_check_transfer(request: web.Request, body) -> web.Response:
    """Create a Check Transfer

    

    :param body: 
    :type body: dict | bytes

    """
    body = CreateACheckTransferParameters.from_dict(body)
    return web.Response(status=200)


async def create_a_file(request: web.Request, file, purpose, description=None) -> web.Response:
    """Create a File

    To upload a file to Increase, you&#39;ll need to send a request of Content-Type &#x60;multipart/form-data&#x60;. The request should contain the file you would like to upload, as well as the parameters for creating a file.

    :param file: The file contents. This should follow the specifications of [RFC 7578](https://datatracker.ietf.org/doc/html/rfc7578) which defines file transfers for the multipart/form-data protocol.
    :type file: str
    :param purpose: What the File will be used for in Increase&#39;s systems.
    :type purpose: str
    :param description: The description you choose to give the File.
    :type description: str

    """
    return web.Response(status=200)


async def create_a_limit(request: web.Request, body) -> web.Response:
    """Create a Limit

    

    :param body: 
    :type body: dict | bytes

    """
    body = CreateALimitParameters.from_dict(body)
    return web.Response(status=200)


async def create_a_real_time_payments_transfer(request: web.Request, body) -> web.Response:
    """Create a Real Time Payments Transfer

    

    :param body: 
    :type body: dict | bytes

    """
    body = CreateARealTimePaymentsTransferParameters.from_dict(body)
    return web.Response(status=200)


async def create_a_supplemental_document_for_an_entity(request: web.Request, entity_id, body) -> web.Response:
    """Create a supplemental document for an Entity

    

    :param entity_id: 
    :type entity_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = CreateASupplementalDocumentForAnEntityParameters.from_dict(body)
    return web.Response(status=200)


async def create_a_wire_drawdown_request(request: web.Request, body) -> web.Response:
    """Create a Wire Drawdown Request

    

    :param body: 
    :type body: dict | bytes

    """
    body = CreateAWireDrawdownRequestParameters.from_dict(body)
    return web.Response(status=200)


async def create_a_wire_transfer(request: web.Request, body) -> web.Response:
    """Create a Wire Transfer

    

    :param body: 
    :type body: dict | bytes

    """
    body = CreateAWireTransferParameters.from_dict(body)
    return web.Response(status=200)


async def create_an_account(request: web.Request, body) -> web.Response:
    """Create an Account

    

    :param body: 
    :type body: dict | bytes

    """
    body = CreateAnAccountParameters.from_dict(body)
    return web.Response(status=200)


async def create_an_account_number(request: web.Request, body) -> web.Response:
    """Create an Account Number

    

    :param body: 
    :type body: dict | bytes

    """
    body = CreateAnAccountNumberParameters.from_dict(body)
    return web.Response(status=200)


async def create_an_account_transfer(request: web.Request, body) -> web.Response:
    """Create an Account Transfer

    

    :param body: 
    :type body: dict | bytes

    """
    body = CreateAnAccountTransferParameters.from_dict(body)
    return web.Response(status=200)


async def create_an_ach_prenotification(request: web.Request, body) -> web.Response:
    """Create an ACH Prenotification

    

    :param body: 
    :type body: dict | bytes

    """
    body = CreateAnAchPrenotificationParameters.from_dict(body)
    return web.Response(status=200)


async def create_an_ach_return(request: web.Request, body) -> web.Response:
    """Create an ACH Return

    

    :param body: 
    :type body: dict | bytes

    """
    body = CreateAnAchReturnParameters.from_dict(body)
    return web.Response(status=200)


async def create_an_ach_transfer(request: web.Request, body) -> web.Response:
    """Create an ACH Transfer

    

    :param body: 
    :type body: dict | bytes

    """
    body = CreateAnAchTransferParameters.from_dict(body)
    return web.Response(status=200)


async def create_an_entity(request: web.Request, body) -> web.Response:
    """Create an Entity

    

    :param body: 
    :type body: dict | bytes

    """
    body = CreateAnEntityParameters.from_dict(body)
    return web.Response(status=200)


async def create_an_event_subscription(request: web.Request, body) -> web.Response:
    """Create an Event Subscription

    

    :param body: 
    :type body: dict | bytes

    """
    body = CreateAnEventSubscriptionParameters.from_dict(body)
    return web.Response(status=200)


async def create_an_export(request: web.Request, body) -> web.Response:
    """Create an Export

    

    :param body: 
    :type body: dict | bytes

    """
    body = CreateAnExportParameters.from_dict(body)
    return web.Response(status=200)


async def create_an_external_account(request: web.Request, body) -> web.Response:
    """Create an External Account

    

    :param body: 
    :type body: dict | bytes

    """
    body = CreateAnExternalAccountParameters.from_dict(body)
    return web.Response(status=200)


async def deposit_a_sandbox_check_transfer(request: web.Request, check_transfer_id) -> web.Response:
    """Deposit a Sandbox Check Transfer

    Simulates a [Check Transfer](#check-transfers) being deposited at a bank. This transfer must first have a &#x60;status&#x60; of &#x60;mailed&#x60;.

    :param check_transfer_id: 
    :type check_transfer_id: str

    """
    return web.Response(status=200)


async def list_account_numbers(request: web.Request, cursor=None, limit=None, status=None, account_id=None, created_at_after=None, created_at_before=None, created_at_on_or_after=None, created_at_on_or_before=None) -> web.Response:
    """List Account Numbers

    

    :param cursor: 
    :type cursor: str
    :param limit: 
    :type limit: int
    :param status: 
    :type status: str
    :param account_id: 
    :type account_id: str
    :param created_at_after: 
    :type created_at_after: str
    :param created_at_before: 
    :type created_at_before: str
    :param created_at_on_or_after: 
    :type created_at_on_or_after: str
    :param created_at_on_or_before: 
    :type created_at_on_or_before: str

    """
    created_at_after = util.deserialize_datetime(created_at_after)
    created_at_before = util.deserialize_datetime(created_at_before)
    created_at_on_or_after = util.deserialize_datetime(created_at_on_or_after)
    created_at_on_or_before = util.deserialize_datetime(created_at_on_or_before)
    return web.Response(status=200)


async def list_account_statements(request: web.Request, cursor=None, limit=None, account_id=None, statement_period_start_after=None, statement_period_start_before=None, statement_period_start_on_or_after=None, statement_period_start_on_or_before=None) -> web.Response:
    """List Account Statements

    

    :param cursor: 
    :type cursor: str
    :param limit: 
    :type limit: int
    :param account_id: 
    :type account_id: str
    :param statement_period_start_after: 
    :type statement_period_start_after: str
    :param statement_period_start_before: 
    :type statement_period_start_before: str
    :param statement_period_start_on_or_after: 
    :type statement_period_start_on_or_after: str
    :param statement_period_start_on_or_before: 
    :type statement_period_start_on_or_before: str

    """
    statement_period_start_after = util.deserialize_datetime(statement_period_start_after)
    statement_period_start_before = util.deserialize_datetime(statement_period_start_before)
    statement_period_start_on_or_after = util.deserialize_datetime(statement_period_start_on_or_after)
    statement_period_start_on_or_before = util.deserialize_datetime(statement_period_start_on_or_before)
    return web.Response(status=200)


async def list_account_transfers(request: web.Request, cursor=None, limit=None, account_id=None, created_at_after=None, created_at_before=None, created_at_on_or_after=None, created_at_on_or_before=None) -> web.Response:
    """List Account Transfers

    

    :param cursor: 
    :type cursor: str
    :param limit: 
    :type limit: int
    :param account_id: 
    :type account_id: str
    :param created_at_after: 
    :type created_at_after: str
    :param created_at_before: 
    :type created_at_before: str
    :param created_at_on_or_after: 
    :type created_at_on_or_after: str
    :param created_at_on_or_before: 
    :type created_at_on_or_before: str

    """
    created_at_after = util.deserialize_datetime(created_at_after)
    created_at_before = util.deserialize_datetime(created_at_before)
    created_at_on_or_after = util.deserialize_datetime(created_at_on_or_after)
    created_at_on_or_before = util.deserialize_datetime(created_at_on_or_before)
    return web.Response(status=200)


async def list_accounts(request: web.Request, cursor=None, limit=None, entity_id=None, status=None, created_at_after=None, created_at_before=None, created_at_on_or_after=None, created_at_on_or_before=None) -> web.Response:
    """List Accounts

    

    :param cursor: 
    :type cursor: str
    :param limit: 
    :type limit: int
    :param entity_id: 
    :type entity_id: str
    :param status: 
    :type status: str
    :param created_at_after: 
    :type created_at_after: str
    :param created_at_before: 
    :type created_at_before: str
    :param created_at_on_or_after: 
    :type created_at_on_or_after: str
    :param created_at_on_or_before: 
    :type created_at_on_or_before: str

    """
    created_at_after = util.deserialize_datetime(created_at_after)
    created_at_before = util.deserialize_datetime(created_at_before)
    created_at_on_or_after = util.deserialize_datetime(created_at_on_or_after)
    created_at_on_or_before = util.deserialize_datetime(created_at_on_or_before)
    return web.Response(status=200)


async def list_ach_prenotifications(request: web.Request, cursor=None, limit=None, created_at_after=None, created_at_before=None, created_at_on_or_after=None, created_at_on_or_before=None) -> web.Response:
    """List ACH Prenotifications

    

    :param cursor: 
    :type cursor: str
    :param limit: 
    :type limit: int
    :param created_at_after: 
    :type created_at_after: str
    :param created_at_before: 
    :type created_at_before: str
    :param created_at_on_or_after: 
    :type created_at_on_or_after: str
    :param created_at_on_or_before: 
    :type created_at_on_or_before: str

    """
    created_at_after = util.deserialize_datetime(created_at_after)
    created_at_before = util.deserialize_datetime(created_at_before)
    created_at_on_or_after = util.deserialize_datetime(created_at_on_or_after)
    created_at_on_or_before = util.deserialize_datetime(created_at_on_or_before)
    return web.Response(status=200)


async def list_ach_transfers(request: web.Request, cursor=None, limit=None, account_id=None, external_account_id=None, created_at_after=None, created_at_before=None, created_at_on_or_after=None, created_at_on_or_before=None) -> web.Response:
    """List ACH Transfers

    

    :param cursor: 
    :type cursor: str
    :param limit: 
    :type limit: int
    :param account_id: 
    :type account_id: str
    :param external_account_id: 
    :type external_account_id: str
    :param created_at_after: 
    :type created_at_after: str
    :param created_at_before: 
    :type created_at_before: str
    :param created_at_on_or_after: 
    :type created_at_on_or_after: str
    :param created_at_on_or_before: 
    :type created_at_on_or_before: str

    """
    created_at_after = util.deserialize_datetime(created_at_after)
    created_at_before = util.deserialize_datetime(created_at_before)
    created_at_on_or_after = util.deserialize_datetime(created_at_on_or_after)
    created_at_on_or_before = util.deserialize_datetime(created_at_on_or_before)
    return web.Response(status=200)


async def list_bookkeeping_accounts(request: web.Request, cursor=None, limit=None) -> web.Response:
    """List Bookkeeping Accounts

    

    :param cursor: 
    :type cursor: str
    :param limit: 
    :type limit: int

    """
    return web.Response(status=200)


async def list_bookkeeping_entries(request: web.Request, cursor=None, limit=None) -> web.Response:
    """List Bookkeeping Entries

    

    :param cursor: 
    :type cursor: str
    :param limit: 
    :type limit: int

    """
    return web.Response(status=200)


async def list_card_disputes(request: web.Request, cursor=None, limit=None, created_at_after=None, created_at_before=None, created_at_on_or_after=None, created_at_on_or_before=None, status_in=None) -> web.Response:
    """List Card Disputes

    

    :param cursor: 
    :type cursor: str
    :param limit: 
    :type limit: int
    :param created_at_after: 
    :type created_at_after: str
    :param created_at_before: 
    :type created_at_before: str
    :param created_at_on_or_after: 
    :type created_at_on_or_after: str
    :param created_at_on_or_before: 
    :type created_at_on_or_before: str
    :param status_in: 
    :type status_in: List[str]

    """
    created_at_after = util.deserialize_datetime(created_at_after)
    created_at_before = util.deserialize_datetime(created_at_before)
    created_at_on_or_after = util.deserialize_datetime(created_at_on_or_after)
    created_at_on_or_before = util.deserialize_datetime(created_at_on_or_before)
    return web.Response(status=200)


async def list_card_profiles(request: web.Request, cursor=None, limit=None, status_in=None) -> web.Response:
    """List Card Profiles

    

    :param cursor: 
    :type cursor: str
    :param limit: 
    :type limit: int
    :param status_in: 
    :type status_in: List[str]

    """
    return web.Response(status=200)


async def list_cards(request: web.Request, cursor=None, limit=None, account_id=None, created_at_after=None, created_at_before=None, created_at_on_or_after=None, created_at_on_or_before=None) -> web.Response:
    """List Cards

    

    :param cursor: 
    :type cursor: str
    :param limit: 
    :type limit: int
    :param account_id: 
    :type account_id: str
    :param created_at_after: 
    :type created_at_after: str
    :param created_at_before: 
    :type created_at_before: str
    :param created_at_on_or_after: 
    :type created_at_on_or_after: str
    :param created_at_on_or_before: 
    :type created_at_on_or_before: str

    """
    created_at_after = util.deserialize_datetime(created_at_after)
    created_at_before = util.deserialize_datetime(created_at_before)
    created_at_on_or_after = util.deserialize_datetime(created_at_on_or_after)
    created_at_on_or_before = util.deserialize_datetime(created_at_on_or_before)
    return web.Response(status=200)


async def list_check_deposits(request: web.Request, cursor=None, limit=None, account_id=None, created_at_after=None, created_at_before=None, created_at_on_or_after=None, created_at_on_or_before=None) -> web.Response:
    """List Check Deposits

    

    :param cursor: 
    :type cursor: str
    :param limit: 
    :type limit: int
    :param account_id: 
    :type account_id: str
    :param created_at_after: 
    :type created_at_after: str
    :param created_at_before: 
    :type created_at_before: str
    :param created_at_on_or_after: 
    :type created_at_on_or_after: str
    :param created_at_on_or_before: 
    :type created_at_on_or_before: str

    """
    created_at_after = util.deserialize_datetime(created_at_after)
    created_at_before = util.deserialize_datetime(created_at_before)
    created_at_on_or_after = util.deserialize_datetime(created_at_on_or_after)
    created_at_on_or_before = util.deserialize_datetime(created_at_on_or_before)
    return web.Response(status=200)


async def list_check_transfers(request: web.Request, cursor=None, limit=None, account_id=None, created_at_after=None, created_at_before=None, created_at_on_or_after=None, created_at_on_or_before=None) -> web.Response:
    """List Check Transfers

    

    :param cursor: 
    :type cursor: str
    :param limit: 
    :type limit: int
    :param account_id: 
    :type account_id: str
    :param created_at_after: 
    :type created_at_after: str
    :param created_at_before: 
    :type created_at_before: str
    :param created_at_on_or_after: 
    :type created_at_on_or_after: str
    :param created_at_on_or_before: 
    :type created_at_on_or_before: str

    """
    created_at_after = util.deserialize_datetime(created_at_after)
    created_at_before = util.deserialize_datetime(created_at_before)
    created_at_on_or_after = util.deserialize_datetime(created_at_on_or_after)
    created_at_on_or_before = util.deserialize_datetime(created_at_on_or_before)
    return web.Response(status=200)


async def list_declined_transactions(request: web.Request, cursor=None, limit=None, account_id=None, created_at_after=None, created_at_before=None, created_at_on_or_after=None, created_at_on_or_before=None, route_id=None) -> web.Response:
    """List Declined Transactions

    

    :param cursor: 
    :type cursor: str
    :param limit: 
    :type limit: int
    :param account_id: 
    :type account_id: str
    :param created_at_after: 
    :type created_at_after: str
    :param created_at_before: 
    :type created_at_before: str
    :param created_at_on_or_after: 
    :type created_at_on_or_after: str
    :param created_at_on_or_before: 
    :type created_at_on_or_before: str
    :param route_id: 
    :type route_id: str

    """
    created_at_after = util.deserialize_datetime(created_at_after)
    created_at_before = util.deserialize_datetime(created_at_before)
    created_at_on_or_after = util.deserialize_datetime(created_at_on_or_after)
    created_at_on_or_before = util.deserialize_datetime(created_at_on_or_before)
    return web.Response(status=200)


async def list_digital_wallet_tokens(request: web.Request, cursor=None, limit=None, card_id=None, created_at_after=None, created_at_before=None, created_at_on_or_after=None, created_at_on_or_before=None) -> web.Response:
    """List Digital Wallet Tokens

    

    :param cursor: 
    :type cursor: str
    :param limit: 
    :type limit: int
    :param card_id: 
    :type card_id: str
    :param created_at_after: 
    :type created_at_after: str
    :param created_at_before: 
    :type created_at_before: str
    :param created_at_on_or_after: 
    :type created_at_on_or_after: str
    :param created_at_on_or_before: 
    :type created_at_on_or_before: str

    """
    created_at_after = util.deserialize_datetime(created_at_after)
    created_at_before = util.deserialize_datetime(created_at_before)
    created_at_on_or_after = util.deserialize_datetime(created_at_on_or_after)
    created_at_on_or_before = util.deserialize_datetime(created_at_on_or_before)
    return web.Response(status=200)


async def list_documents(request: web.Request, cursor=None, limit=None, entity_id=None, category_in=None, created_at_after=None, created_at_before=None, created_at_on_or_after=None, created_at_on_or_before=None) -> web.Response:
    """List Documents

    

    :param cursor: 
    :type cursor: str
    :param limit: 
    :type limit: int
    :param entity_id: 
    :type entity_id: str
    :param category_in: 
    :type category_in: List[str]
    :param created_at_after: 
    :type created_at_after: str
    :param created_at_before: 
    :type created_at_before: str
    :param created_at_on_or_after: 
    :type created_at_on_or_after: str
    :param created_at_on_or_before: 
    :type created_at_on_or_before: str

    """
    created_at_after = util.deserialize_datetime(created_at_after)
    created_at_before = util.deserialize_datetime(created_at_before)
    created_at_on_or_after = util.deserialize_datetime(created_at_on_or_after)
    created_at_on_or_before = util.deserialize_datetime(created_at_on_or_before)
    return web.Response(status=200)


async def list_entities(request: web.Request, cursor=None, limit=None, created_at_after=None, created_at_before=None, created_at_on_or_after=None, created_at_on_or_before=None) -> web.Response:
    """List Entities

    

    :param cursor: 
    :type cursor: str
    :param limit: 
    :type limit: int
    :param created_at_after: 
    :type created_at_after: str
    :param created_at_before: 
    :type created_at_before: str
    :param created_at_on_or_after: 
    :type created_at_on_or_after: str
    :param created_at_on_or_before: 
    :type created_at_on_or_before: str

    """
    created_at_after = util.deserialize_datetime(created_at_after)
    created_at_before = util.deserialize_datetime(created_at_before)
    created_at_on_or_after = util.deserialize_datetime(created_at_on_or_after)
    created_at_on_or_before = util.deserialize_datetime(created_at_on_or_before)
    return web.Response(status=200)


async def list_event_subscriptions(request: web.Request, cursor=None, limit=None) -> web.Response:
    """List Event Subscriptions

    

    :param cursor: 
    :type cursor: str
    :param limit: 
    :type limit: int

    """
    return web.Response(status=200)


async def list_events(request: web.Request, cursor=None, limit=None, created_at_after=None, created_at_before=None, created_at_on_or_after=None, created_at_on_or_before=None, category_in=None, associated_object_id=None) -> web.Response:
    """List Events

    

    :param cursor: 
    :type cursor: str
    :param limit: 
    :type limit: int
    :param created_at_after: 
    :type created_at_after: str
    :param created_at_before: 
    :type created_at_before: str
    :param created_at_on_or_after: 
    :type created_at_on_or_after: str
    :param created_at_on_or_before: 
    :type created_at_on_or_before: str
    :param category_in: 
    :type category_in: List[str]
    :param associated_object_id: 
    :type associated_object_id: str

    """
    created_at_after = util.deserialize_datetime(created_at_after)
    created_at_before = util.deserialize_datetime(created_at_before)
    created_at_on_or_after = util.deserialize_datetime(created_at_on_or_after)
    created_at_on_or_before = util.deserialize_datetime(created_at_on_or_before)
    return web.Response(status=200)


async def list_exports(request: web.Request, cursor=None, limit=None) -> web.Response:
    """List Exports

    

    :param cursor: 
    :type cursor: str
    :param limit: 
    :type limit: int

    """
    return web.Response(status=200)


async def list_external_accounts(request: web.Request, cursor=None, limit=None, status_in=None) -> web.Response:
    """List External Accounts

    

    :param cursor: 
    :type cursor: str
    :param limit: 
    :type limit: int
    :param status_in: 
    :type status_in: List[str]

    """
    return web.Response(status=200)


async def list_files(request: web.Request, cursor=None, limit=None, created_at_after=None, created_at_before=None, created_at_on_or_after=None, created_at_on_or_before=None, purpose_in=None) -> web.Response:
    """List Files

    

    :param cursor: 
    :type cursor: str
    :param limit: 
    :type limit: int
    :param created_at_after: 
    :type created_at_after: str
    :param created_at_before: 
    :type created_at_before: str
    :param created_at_on_or_after: 
    :type created_at_on_or_after: str
    :param created_at_on_or_before: 
    :type created_at_on_or_before: str
    :param purpose_in: 
    :type purpose_in: List[str]

    """
    created_at_after = util.deserialize_datetime(created_at_after)
    created_at_before = util.deserialize_datetime(created_at_before)
    created_at_on_or_after = util.deserialize_datetime(created_at_on_or_after)
    created_at_on_or_before = util.deserialize_datetime(created_at_on_or_before)
    return web.Response(status=200)


async def list_inbound_ach_transfer_returns(request: web.Request, cursor=None, limit=None) -> web.Response:
    """List Inbound ACH Transfer Returns

    

    :param cursor: 
    :type cursor: str
    :param limit: 
    :type limit: int

    """
    return web.Response(status=200)


async def list_inbound_wire_drawdown_requests(request: web.Request, cursor=None, limit=None) -> web.Response:
    """List Inbound Wire Drawdown Requests

    

    :param cursor: 
    :type cursor: str
    :param limit: 
    :type limit: int

    """
    return web.Response(status=200)


async def list_limits(request: web.Request, cursor=None, limit=None, model_id=None, status=None) -> web.Response:
    """List Limits

    

    :param cursor: 
    :type cursor: str
    :param limit: 
    :type limit: int
    :param model_id: 
    :type model_id: str
    :param status: 
    :type status: str

    """
    return web.Response(status=200)


async def list_oauth_connections(request: web.Request, cursor=None, limit=None) -> web.Response:
    """List OAuth Connections

    

    :param cursor: 
    :type cursor: str
    :param limit: 
    :type limit: int

    """
    return web.Response(status=200)


async def list_pending_transactions(request: web.Request, cursor=None, limit=None, account_id=None, route_id=None, source_id=None, status_in=None, created_at_after=None, created_at_before=None, created_at_on_or_after=None, created_at_on_or_before=None) -> web.Response:
    """List Pending Transactions

    

    :param cursor: 
    :type cursor: str
    :param limit: 
    :type limit: int
    :param account_id: 
    :type account_id: str
    :param route_id: 
    :type route_id: str
    :param source_id: 
    :type source_id: str
    :param status_in: 
    :type status_in: List[str]
    :param created_at_after: 
    :type created_at_after: str
    :param created_at_before: 
    :type created_at_before: str
    :param created_at_on_or_after: 
    :type created_at_on_or_after: str
    :param created_at_on_or_before: 
    :type created_at_on_or_before: str

    """
    created_at_after = util.deserialize_datetime(created_at_after)
    created_at_before = util.deserialize_datetime(created_at_before)
    created_at_on_or_after = util.deserialize_datetime(created_at_on_or_after)
    created_at_on_or_before = util.deserialize_datetime(created_at_on_or_before)
    return web.Response(status=200)


async def list_programs(request: web.Request, cursor=None, limit=None) -> web.Response:
    """List Programs

    

    :param cursor: 
    :type cursor: str
    :param limit: 
    :type limit: int

    """
    return web.Response(status=200)


async def list_real_time_payments_transfers(request: web.Request, cursor=None, limit=None, account_id=None, external_account_id=None, created_at_after=None, created_at_before=None, created_at_on_or_after=None, created_at_on_or_before=None) -> web.Response:
    """List Real Time Payments Transfers

    

    :param cursor: 
    :type cursor: str
    :param limit: 
    :type limit: int
    :param account_id: 
    :type account_id: str
    :param external_account_id: 
    :type external_account_id: str
    :param created_at_after: 
    :type created_at_after: str
    :param created_at_before: 
    :type created_at_before: str
    :param created_at_on_or_after: 
    :type created_at_on_or_after: str
    :param created_at_on_or_before: 
    :type created_at_on_or_before: str

    """
    created_at_after = util.deserialize_datetime(created_at_after)
    created_at_before = util.deserialize_datetime(created_at_before)
    created_at_on_or_after = util.deserialize_datetime(created_at_on_or_after)
    created_at_on_or_before = util.deserialize_datetime(created_at_on_or_before)
    return web.Response(status=200)


async def list_routing_numbers(request: web.Request, routing_number, cursor=None, limit=None) -> web.Response:
    """List Routing Numbers

    You can use this API to confirm if a routing number is valid, such as when a user is providing you with bank account details. Since routing numbers uniquely identify a bank, this will always return 0 or 1 entry. In Sandbox, the only valid routing number for this method is 110000000.

    :param routing_number: 
    :type routing_number: str
    :param cursor: 
    :type cursor: str
    :param limit: 
    :type limit: int

    """
    return web.Response(status=200)


async def list_transactions(request: web.Request, cursor=None, limit=None, account_id=None, created_at_after=None, created_at_before=None, created_at_on_or_after=None, created_at_on_or_before=None, category_in=None, route_id=None) -> web.Response:
    """List Transactions

    

    :param cursor: 
    :type cursor: str
    :param limit: 
    :type limit: int
    :param account_id: 
    :type account_id: str
    :param created_at_after: 
    :type created_at_after: str
    :param created_at_before: 
    :type created_at_before: str
    :param created_at_on_or_after: 
    :type created_at_on_or_after: str
    :param created_at_on_or_before: 
    :type created_at_on_or_before: str
    :param category_in: 
    :type category_in: List[str]
    :param route_id: 
    :type route_id: str

    """
    created_at_after = util.deserialize_datetime(created_at_after)
    created_at_before = util.deserialize_datetime(created_at_before)
    created_at_on_or_after = util.deserialize_datetime(created_at_on_or_after)
    created_at_on_or_before = util.deserialize_datetime(created_at_on_or_before)
    return web.Response(status=200)


async def list_wire_drawdown_requests(request: web.Request, cursor=None, limit=None) -> web.Response:
    """List Wire Drawdown Requests

    

    :param cursor: 
    :type cursor: str
    :param limit: 
    :type limit: int

    """
    return web.Response(status=200)


async def list_wire_transfers(request: web.Request, cursor=None, limit=None, account_id=None, external_account_id=None, created_at_after=None, created_at_before=None, created_at_on_or_after=None, created_at_on_or_before=None) -> web.Response:
    """List Wire Transfers

    

    :param cursor: 
    :type cursor: str
    :param limit: 
    :type limit: int
    :param account_id: 
    :type account_id: str
    :param external_account_id: 
    :type external_account_id: str
    :param created_at_after: 
    :type created_at_after: str
    :param created_at_before: 
    :type created_at_before: str
    :param created_at_on_or_after: 
    :type created_at_on_or_after: str
    :param created_at_on_or_before: 
    :type created_at_on_or_before: str

    """
    created_at_after = util.deserialize_datetime(created_at_after)
    created_at_before = util.deserialize_datetime(created_at_before)
    created_at_on_or_after = util.deserialize_datetime(created_at_on_or_after)
    created_at_on_or_before = util.deserialize_datetime(created_at_on_or_before)
    return web.Response(status=200)


async def look_up_the_balance_for_an_account(request: web.Request, body) -> web.Response:
    """Look up the balance for an Account

    

    :param body: 
    :type body: dict | bytes

    """
    body = LookUpTheBalanceForAnAccountParameters.from_dict(body)
    return web.Response(status=200)


async def mail_a_sandbox_check_transfer(request: web.Request, check_transfer_id) -> web.Response:
    """Mail a Sandbox Check Transfer

    Simulates the mailing of a [Check Transfer](#check-transfers), which happens once per weekday in production but can be sped up in sandbox. This transfer must first have a &#x60;status&#x60; of &#x60;pending_approval&#x60; or &#x60;pending_submission&#x60;.

    :param check_transfer_id: 
    :type check_transfer_id: str

    """
    return web.Response(status=200)


async def reject_a_sandbox_check_deposit(request: web.Request, check_deposit_id) -> web.Response:
    """Reject a Sandbox Check Deposit

    Simulates the rejection of a [Check Deposit](#check-deposits) by Increase due to factors like poor image quality. This Check Deposit must first have a &#x60;status&#x60; of &#x60;pending&#x60;.

    :param check_deposit_id: 
    :type check_deposit_id: str

    """
    return web.Response(status=200)


async def request_a_stop_payment_on_a_check_transfer(request: web.Request, check_transfer_id) -> web.Response:
    """Request a stop payment on a Check Transfer

    

    :param check_transfer_id: 
    :type check_transfer_id: str

    """
    return web.Response(status=200)


async def retrieve_a_card(request: web.Request, card_id) -> web.Response:
    """Retrieve a Card

    

    :param card_id: 
    :type card_id: str

    """
    return web.Response(status=200)


async def retrieve_a_card_dispute(request: web.Request, card_dispute_id) -> web.Response:
    """Retrieve a Card Dispute

    

    :param card_dispute_id: 
    :type card_dispute_id: str

    """
    return web.Response(status=200)


async def retrieve_a_card_profile(request: web.Request, card_profile_id) -> web.Response:
    """Retrieve a Card Profile

    

    :param card_profile_id: 
    :type card_profile_id: str

    """
    return web.Response(status=200)


async def retrieve_a_check_deposit(request: web.Request, check_deposit_id) -> web.Response:
    """Retrieve a Check Deposit

    

    :param check_deposit_id: 
    :type check_deposit_id: str

    """
    return web.Response(status=200)


async def retrieve_a_check_transfer(request: web.Request, check_transfer_id) -> web.Response:
    """Retrieve a Check Transfer

    

    :param check_transfer_id: 
    :type check_transfer_id: str

    """
    return web.Response(status=200)


async def retrieve_a_declined_transaction(request: web.Request, declined_transaction_id) -> web.Response:
    """Retrieve a Declined Transaction

    

    :param declined_transaction_id: 
    :type declined_transaction_id: str

    """
    return web.Response(status=200)


async def retrieve_a_digital_wallet_token(request: web.Request, digital_wallet_token_id) -> web.Response:
    """Retrieve a Digital Wallet Token

    

    :param digital_wallet_token_id: 
    :type digital_wallet_token_id: str

    """
    return web.Response(status=200)


async def retrieve_a_document(request: web.Request, document_id) -> web.Response:
    """Retrieve a Document

    

    :param document_id: 
    :type document_id: str

    """
    return web.Response(status=200)


async def retrieve_a_file(request: web.Request, file_id) -> web.Response:
    """Retrieve a File

    

    :param file_id: 
    :type file_id: str

    """
    return web.Response(status=200)


async def retrieve_a_limit(request: web.Request, limit_id) -> web.Response:
    """Retrieve a Limit

    

    :param limit_id: 
    :type limit_id: str

    """
    return web.Response(status=200)


async def retrieve_a_pending_transaction(request: web.Request, pending_transaction_id) -> web.Response:
    """Retrieve a Pending Transaction

    

    :param pending_transaction_id: 
    :type pending_transaction_id: str

    """
    return web.Response(status=200)


async def retrieve_a_program(request: web.Request, program_id) -> web.Response:
    """Retrieve a Program

    

    :param program_id: 
    :type program_id: str

    """
    return web.Response(status=200)


async def retrieve_a_real_time_decision(request: web.Request, real_time_decision_id) -> web.Response:
    """Retrieve a Real-Time Decision

    

    :param real_time_decision_id: 
    :type real_time_decision_id: str

    """
    return web.Response(status=200)


async def retrieve_a_real_time_payments_transfer(request: web.Request, real_time_payments_transfer_id) -> web.Response:
    """Retrieve a Real Time Payments Transfer

    

    :param real_time_payments_transfer_id: 
    :type real_time_payments_transfer_id: str

    """
    return web.Response(status=200)


async def retrieve_a_transaction(request: web.Request, transaction_id) -> web.Response:
    """Retrieve a Transaction

    

    :param transaction_id: 
    :type transaction_id: str

    """
    return web.Response(status=200)


async def retrieve_a_wire_drawdown_request(request: web.Request, wire_drawdown_request_id) -> web.Response:
    """Retrieve a Wire Drawdown Request

    

    :param wire_drawdown_request_id: 
    :type wire_drawdown_request_id: str

    """
    return web.Response(status=200)


async def retrieve_a_wire_transfer(request: web.Request, wire_transfer_id) -> web.Response:
    """Retrieve a Wire Transfer

    

    :param wire_transfer_id: 
    :type wire_transfer_id: str

    """
    return web.Response(status=200)


async def retrieve_an_account(request: web.Request, account_id) -> web.Response:
    """Retrieve an Account

    

    :param account_id: 
    :type account_id: str

    """
    return web.Response(status=200)


async def retrieve_an_account_number(request: web.Request, account_number_id) -> web.Response:
    """Retrieve an Account Number

    

    :param account_number_id: 
    :type account_number_id: str

    """
    return web.Response(status=200)


async def retrieve_an_account_statement(request: web.Request, account_statement_id) -> web.Response:
    """Retrieve an Account Statement

    

    :param account_statement_id: 
    :type account_statement_id: str

    """
    return web.Response(status=200)


async def retrieve_an_account_transfer(request: web.Request, account_transfer_id) -> web.Response:
    """Retrieve an Account Transfer

    

    :param account_transfer_id: 
    :type account_transfer_id: str

    """
    return web.Response(status=200)


async def retrieve_an_ach_prenotification(request: web.Request, ach_prenotification_id) -> web.Response:
    """Retrieve an ACH Prenotification

    

    :param ach_prenotification_id: 
    :type ach_prenotification_id: str

    """
    return web.Response(status=200)


async def retrieve_an_ach_transfer(request: web.Request, ach_transfer_id) -> web.Response:
    """Retrieve an ACH Transfer

    

    :param ach_transfer_id: 
    :type ach_transfer_id: str

    """
    return web.Response(status=200)


async def retrieve_an_entity(request: web.Request, entity_id) -> web.Response:
    """Retrieve an Entity

    

    :param entity_id: 
    :type entity_id: str

    """
    return web.Response(status=200)


async def retrieve_an_event(request: web.Request, event_id) -> web.Response:
    """Retrieve an Event

    

    :param event_id: 
    :type event_id: str

    """
    return web.Response(status=200)


async def retrieve_an_event_subscription(request: web.Request, event_subscription_id) -> web.Response:
    """Retrieve an Event Subscription

    

    :param event_subscription_id: 
    :type event_subscription_id: str

    """
    return web.Response(status=200)


async def retrieve_an_export(request: web.Request, export_id) -> web.Response:
    """Retrieve an Export

    

    :param export_id: 
    :type export_id: str

    """
    return web.Response(status=200)


async def retrieve_an_external_account(request: web.Request, external_account_id) -> web.Response:
    """Retrieve an External Account

    

    :param external_account_id: 
    :type external_account_id: str

    """
    return web.Response(status=200)


async def retrieve_an_inbound_ach_transfer_return(request: web.Request, inbound_ach_transfer_return_id) -> web.Response:
    """Retrieve an Inbound ACH Transfer Return

    

    :param inbound_ach_transfer_return_id: 
    :type inbound_ach_transfer_return_id: str

    """
    return web.Response(status=200)


async def retrieve_an_inbound_wire_drawdown_request(request: web.Request, inbound_wire_drawdown_request_id) -> web.Response:
    """Retrieve an Inbound Wire Drawdown Request

    

    :param inbound_wire_drawdown_request_id: 
    :type inbound_wire_drawdown_request_id: str

    """
    return web.Response(status=200)


async def retrieve_an_oauth_connection(request: web.Request, oauth_connection_id) -> web.Response:
    """Retrieve an OAuth Connection

    

    :param oauth_connection_id: 
    :type oauth_connection_id: str

    """
    return web.Response(status=200)


async def retrieve_group_details(request: web.Request, ) -> web.Response:
    """Retrieve Group details

    Returns details for the currently authenticated Group.


    """
    return web.Response(status=200)


async def retrieve_sensitive_details_for_a_card(request: web.Request, card_id) -> web.Response:
    """Retrieve sensitive details for a Card

    

    :param card_id: 
    :type card_id: str

    """
    return web.Response(status=200)


async def return_a_sandbox_ach_transfer(request: web.Request, ach_transfer_id, body) -> web.Response:
    """Return a Sandbox ACH Transfer

    Simulates the return of an [ACH Transfer](#ach-transfers) by the Federal Reserve due to an error condition. This will also create a Transaction to account for the returned funds. This transfer must first have a &#x60;status&#x60; of &#x60;submitted&#x60;.

    :param ach_transfer_id: 
    :type ach_transfer_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = ReturnASandboxAchTransferParameters.from_dict(body)
    return web.Response(status=200)


async def return_a_sandbox_check_deposit(request: web.Request, check_deposit_id) -> web.Response:
    """Return a Sandbox Check Deposit

    Simulates the return of a [Check Deposit](#check-deposits). This Check Deposit must first have a &#x60;status&#x60; of &#x60;submitted&#x60;.

    :param check_deposit_id: 
    :type check_deposit_id: str

    """
    return web.Response(status=200)


async def return_a_sandbox_check_transfer(request: web.Request, check_transfer_id, body) -> web.Response:
    """Return a Sandbox Check Transfer

    Simulates a [Check Transfer](#check-transfers) being returned via USPS to Increase. This transfer must first have a &#x60;status&#x60; of &#x60;mailed&#x60;.

    :param check_transfer_id: 
    :type check_transfer_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = ReturnASandboxCheckTransferParameters.from_dict(body)
    return web.Response(status=200)


async def reverse_a_sandbox_wire_transfer(request: web.Request, wire_transfer_id) -> web.Response:
    """Reverse a Sandbox Wire Transfer

    Simulates the reversal of a [Wire Transfer](#wire-transfers) by the Federal Reserve due to error conditions. This will also create a [Transaction](#transaction) to account for the returned funds. This Wire Transfer must first have a &#x60;status&#x60; of &#x60;complete&#x60;.&#39;

    :param wire_transfer_id: 
    :type wire_transfer_id: str

    """
    return web.Response(status=200)


async def simulate_a_real_time_payments_transfer_to_your_account(request: web.Request, body) -> web.Response:
    """Simulate a Real Time Payments Transfer to your account

    Simulates an inbound Real Time Payments transfer to your account. Real Time Payments are a beta feature.

    :param body: 
    :type body: dict | bytes

    """
    body = SimulateARealTimePaymentsTransferToYourAccountParameters.from_dict(body)
    return web.Response(status=200)


async def simulate_a_refund_on_a_card(request: web.Request, body) -> web.Response:
    """Simulate a refund on a card

    Simulates refunding a card transaction. The full value of the original sandbox transaction is refunded.

    :param body: 
    :type body: dict | bytes

    """
    body = SimulateARefundOnACardParameters.from_dict(body)
    return web.Response(status=200)


async def simulate_a_tax_document_being_created(request: web.Request, body) -> web.Response:
    """Simulate a tax document being created

    Simulates an tax document being created for an account.

    :param body: 
    :type body: dict | bytes

    """
    body = SimulateATaxDocumentBeingCreatedParameters.from_dict(body)
    return web.Response(status=200)


async def simulate_a_wire_transfer_to_your_account(request: web.Request, body) -> web.Response:
    """Simulate a Wire Transfer to your account

    Simulates an inbound Wire Transfer to your account.

    :param body: 
    :type body: dict | bytes

    """
    body = SimulateAWireTransferToYourAccountParameters.from_dict(body)
    return web.Response(status=200)


async def simulate_an_account_statement_being_created(request: web.Request, body) -> web.Response:
    """Simulate an Account Statement being created

    Simulates an [Account Statement](#account-statements) being created for an account. In production, Account Statements are generated once per month.

    :param body: 
    :type body: dict | bytes

    """
    body = SimulateAnAccountStatementBeingCreatedParameters.from_dict(body)
    return web.Response(status=200)


async def simulate_an_ach_transfer_to_your_account(request: web.Request, body) -> web.Response:
    """Simulate an ACH Transfer to your account

    Simulates an inbound ACH transfer to your account. This imitates initiating a transaction to an Increase account from a different financial institution. The transfer may be either a credit or a debit depending on if the &#x60;amount&#x60; is positive or negative. The result of calling this API will be either a [Transaction](#transactions) or a [Declined Transaction](#declined-transactions) depending on whether or not the transfer is allowed.

    :param body: 
    :type body: dict | bytes

    """
    body = SimulateAnAchTransferToYourAccountParameters.from_dict(body)
    return web.Response(status=200)


async def simulate_an_authorization_on_a_card(request: web.Request, body) -> web.Response:
    """Simulate an authorization on a Card

    Simulates a purchase authorization on a [Card](#cards). Depending on the balance available to the card and the &#x60;amount&#x60; submitted, the authorization activity will result in a [Pending Transaction](#pending-transactions) of type &#x60;card_authorization&#x60; or a [Declined Transaction](#declined-transactions) of type &#x60;card_decline&#x60;. You can pass either a Card id or a [Digital Wallet Token](#digital-wallet-tokens) id to simulate the two different ways purchases can be made.

    :param body: 
    :type body: dict | bytes

    """
    body = SimulateAnAuthorizationOnACardParameters.from_dict(body)
    return web.Response(status=200)


async def simulate_an_inbound_wire_drawdown_request_being_created(request: web.Request, body) -> web.Response:
    """Simulate an Inbound Wire Drawdown request being created

    Simulates the receival of an [Inbound Wire Drawdown Request](#inbound-wire-drawdown-requests).

    :param body: 
    :type body: dict | bytes

    """
    body = SimulateAnInboundWireDrawdownRequestBeingCreatedParameters.from_dict(body)
    return web.Response(status=200)


async def simulate_an_interest_payment_to_your_account(request: web.Request, body) -> web.Response:
    """Simulate an Interest Payment to your account

    Simulates an interest payment to your account. In production, this happens automatically on the first of each month.

    :param body: 
    :type body: dict | bytes

    """
    body = SimulateAnInterestPaymentToYourAccountParameters.from_dict(body)
    return web.Response(status=200)


async def simulate_digital_wallet_provisioning_for_a_card(request: web.Request, body) -> web.Response:
    """Simulate digital wallet provisioning for a card

    Simulates a user attempting add a [Card](#cards) to a digital wallet such as Apple Pay.

    :param body: 
    :type body: dict | bytes

    """
    body = SimulateDigitalWalletProvisioningForACardParameters.from_dict(body)
    return web.Response(status=200)


async def simulate_settling_a_card_authorization(request: web.Request, body) -> web.Response:
    """Simulate settling a card authorization

    Simulates the settlement of an authorization by a card acquirer. After a card authorization is created, the merchant will eventually send a settlement. This simulates that event, which may occur many days after the purchase in production. The amount settled can be different from the amount originally authorized, for example, when adding a tip to a restaurant bill.

    :param body: 
    :type body: dict | bytes

    """
    body = SimulateSettlingACardAuthorizationParameters.from_dict(body)
    return web.Response(status=200)


async def simulates_advancing_the_state_of_a_card_dispute(request: web.Request, card_dispute_id, body) -> web.Response:
    """Simulates advancing the state of a card dispute

    After a [Card Dispute](#card-disputes) is created in production, the dispute will be reviewed. Since no review happens in sandbox, this endpoint simulates moving a Card Dispute into a rejected or accepted state. A Card Dispute can only be actioned one time and must have a status of &#x60;pending_reviewing&#x60;.

    :param card_dispute_id: 
    :type card_dispute_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = SimulatesAdvancingTheStateOfACardDisputeParameters.from_dict(body)
    return web.Response(status=200)


async def submit_a_sandbox_ach_transfer(request: web.Request, ach_transfer_id) -> web.Response:
    """Submit a Sandbox ACH Transfer

    Simulates the submission of an [ACH Transfer](#ach-transfers) to the Federal Reserve. This transfer must first have a &#x60;status&#x60; of &#x60;pending_approval&#x60; or &#x60;pending_submission&#x60;. In production, Increase submits ACH Transfers to the Federal Reserve three times per day on weekdays. Since sandbox ACH Transfers are not submitted to the Federal Reserve, this endpoint allows you to skip that delay and transition the ACH Transfer to a status of &#x60;submitted&#x60;.

    :param ach_transfer_id: 
    :type ach_transfer_id: str

    """
    return web.Response(status=200)


async def submit_a_sandbox_check_deposit(request: web.Request, check_deposit_id) -> web.Response:
    """Submit a Sandbox Check Deposit

    Simulates the submission of a [Check Deposit](#check-deposits) to the Federal Reserve. This Check Deposit must first have a &#x60;status&#x60; of &#x60;pending&#x60;.

    :param check_deposit_id: 
    :type check_deposit_id: str

    """
    return web.Response(status=200)


async def submit_a_sandbox_wire_transfer(request: web.Request, wire_transfer_id) -> web.Response:
    """Submit a Sandbox Wire Transfer

    Simulates the submission of a [Wire Transfer](#wire-transfers) to the Federal Reserve. This transfer must first have a &#x60;status&#x60; of &#x60;pending_approval&#x60; or &#x60;pending_creating&#x60;.

    :param wire_transfer_id: 
    :type wire_transfer_id: str

    """
    return web.Response(status=200)


async def update_a_card(request: web.Request, card_id, body) -> web.Response:
    """Update a Card

    

    :param card_id: 
    :type card_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateACardParameters.from_dict(body)
    return web.Response(status=200)


async def update_a_limit(request: web.Request, limit_id, body) -> web.Response:
    """Update a Limit

    

    :param limit_id: 
    :type limit_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateALimitParameters.from_dict(body)
    return web.Response(status=200)


async def update_an_account(request: web.Request, account_id, body) -> web.Response:
    """Update an Account

    

    :param account_id: 
    :type account_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateAnAccountParameters.from_dict(body)
    return web.Response(status=200)


async def update_an_account_number(request: web.Request, account_number_id, body) -> web.Response:
    """Update an Account Number

    

    :param account_number_id: 
    :type account_number_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateAnAccountNumberParameters.from_dict(body)
    return web.Response(status=200)


async def update_an_event_subscription(request: web.Request, event_subscription_id, body) -> web.Response:
    """Update an Event Subscription

    

    :param event_subscription_id: 
    :type event_subscription_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateAnEventSubscriptionParameters.from_dict(body)
    return web.Response(status=200)


async def update_an_external_account(request: web.Request, external_account_id, body) -> web.Response:
    """Update an External Account

    

    :param external_account_id: 
    :type external_account_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateAnExternalAccountParameters.from_dict(body)
    return web.Response(status=200)
