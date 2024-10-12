from typing import List, Dict
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
from openapi_server import util


async def post_account_holder_balance(request: web.Request, body=None) -> web.Response:
    """Get the balances of an account holder

    Returns the account balances of an account holder. An account&#39;s balances are organized according by currencies. This mean that an account may have multiple balances: one for each currency.

    :param body: 
    :type body: dict | bytes

    """
    body = AccountHolderBalanceRequest.from_dict(body)
    return web.Response(status=200)


async def post_account_holder_transaction_list(request: web.Request, body=None) -> web.Response:
    """Get a list of transactions

    Returns a list of transactions for an account holder&#39;s accounts. You can specify the accounts and transaction statuses to be included on the list. The call returns a maximum of 50 transactions for each account. To retrieve all transactions, you must make another call with the &#39;page&#39; value incremented. Transactions are listed in chronological order, with the most recent transaction first.

    :param body: 
    :type body: dict | bytes

    """
    body = AccountHolderTransactionListRequest.from_dict(body)
    return web.Response(status=200)


async def post_debit_account_holder(request: web.Request, body=None) -> web.Response:
    """Send a direct debit request

    Sends a direct debit request to an account holder&#39;s bank account. If the direct debit is successful, the funds are settled in the accounts specified in the split instructions. Adyen sends the result of the direct debit in a [&#x60;DIRECT_DEBIT_INITIATED&#x60;](https://docs.adyen.com/api-explorer/#/NotificationService/latest/post/DIRECT_DEBIT_INITIATED) notification webhook.   To learn more about direct debits, see [Top up accounts](https://docs.adyen.com/marketplaces-and-platforms/classic/top-up-accounts).

    :param body: 
    :type body: dict | bytes

    """
    body = DebitAccountHolderRequest.from_dict(body)
    return web.Response(status=200)


async def post_payout_account_holder(request: web.Request, body=None) -> web.Response:
    """Pay out from an account to the account holder

    Pays out a specified amount from an account to the bank account of account holder.

    :param body: 
    :type body: dict | bytes

    """
    body = PayoutAccountHolderRequest.from_dict(body)
    return web.Response(status=200)


async def post_refund_funds_transfer(request: web.Request, body=None) -> web.Response:
    """Refund a funds transfer

    Refunds funds transferred from one account to another. Both accounts must be in the same platform, but can have different account holders. 

    :param body: 
    :type body: dict | bytes

    """
    body = RefundFundsTransferRequest.from_dict(body)
    return web.Response(status=200)


async def post_refund_not_paid_out_transfers(request: web.Request, body=None) -> web.Response:
    """Refund all transactions of an account since the most recent payout

    Refunds all the transactions of an account that have taken place since the most recent payout. This request is on a account basis (as opposed to a payment basis), so only the portion of the payment that was made to the specified account is refunded. The commissions, fees, and payments to other accounts remain in the accounts to which they were sent as designated by the original payment&#39;s split details.

    :param body: 
    :type body: dict | bytes

    """
    body = RefundNotPaidOutTransfersRequest.from_dict(body)
    return web.Response(status=200)


async def post_setup_beneficiary(request: web.Request, body=None) -> web.Response:
    """Designate a beneficiary account and transfer the benefactor&#39;s current balance

    Defines a benefactor and a beneficiary relationship between two accounts. At the time of benefactor/beneficiary setup, the funds in the benefactor account are transferred to the beneficiary account, and any further payments to the benefactor account are automatically sent to the beneficiary account. A series of benefactor/beneficiaries may not exceed four beneficiaries and may not have a cycle in it.

    :param body: 
    :type body: dict | bytes

    """
    body = SetupBeneficiaryRequest.from_dict(body)
    return web.Response(status=200)


async def post_transfer_funds(request: web.Request, body=None) -> web.Response:
    """Transfer funds between platform accounts

    Transfers funds from one account to another account. Both accounts must be in the same platform, but can have different account holders. The transfer must include a transfer code, which should be determined by the platform, in compliance with local regulations.

    :param body: 
    :type body: dict | bytes

    """
    body = TransferFundsRequest.from_dict(body)
    return web.Response(status=200)
