from typing import List, Dict
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
from openapi_server import util


async def post_accountfundsbelowthreshold(request: web.Request, account_funds_below_threshold_notification=None) -> web.Response:
    """Liable account&#39;s funds are below configured threshold

    Adyen sends this notification when the current funds of your liable account are below the configured threshold.

    :param account_funds_below_threshold_notification: 
    :type account_funds_below_threshold_notification: dict | bytes

    """
    account_funds_below_threshold_notification = AccountFundsBelowThresholdNotification.from_dict(account_funds_below_threshold_notification)
    return web.Response(status=200)


async def post_accountholderpayout(request: web.Request, account_holder_payout_notification=None) -> web.Response:
    """Paid out to account holder

    Adyen sends this notification when a [payout request](https://docs.adyen.com/api-explorer/#/Fund/latest/post/payoutAccountHolder) to an account holder is processed and the payout is scheduled.

    :param account_holder_payout_notification: 
    :type account_holder_payout_notification: dict | bytes

    """
    account_holder_payout_notification = AccountHolderPayoutNotification.from_dict(account_holder_payout_notification)
    return web.Response(status=200)


async def post_beneficiarysetup(request: web.Request, beneficiary_setup_notification=None) -> web.Response:
    """Beneficiary defined

    Adyen sends this notification when a [benefactor/beneficiary relationship is created](https://docs.adyen.com/api-explorer/#/Fund/latest/post/transferFunds).

    :param beneficiary_setup_notification: 
    :type beneficiary_setup_notification: dict | bytes

    """
    beneficiary_setup_notification = BeneficiarySetupNotification.from_dict(beneficiary_setup_notification)
    return web.Response(status=200)


async def post_compensatenegativebalance(request: web.Request, compensate_negative_balance_notification=None) -> web.Response:
    """Negative account balances compensated

    Adyen sends this notification when funds are transferred from your platform&#39;s liable account to an overdrawn account to compensate for the overdraft.

    :param compensate_negative_balance_notification: 
    :type compensate_negative_balance_notification: dict | bytes

    """
    compensate_negative_balance_notification = CompensateNegativeBalanceNotification.from_dict(compensate_negative_balance_notification)
    return web.Response(status=200)


async def post_directdebitinitiated(request: web.Request, direct_debit_initiated_notification=None) -> web.Response:
    """Automated direct debit initiated

    Adyen sends this notification when a [direct debit is initiated](https://docs.adyen.com/api-explorer/#/Fund/latest/post/debitAccountHolder).

    :param direct_debit_initiated_notification: 
    :type direct_debit_initiated_notification: dict | bytes

    """
    direct_debit_initiated_notification = DirectDebitInitiatedNotification.from_dict(direct_debit_initiated_notification)
    return web.Response(status=200)


async def post_refundfundstransfer(request: web.Request, refund_funds_transfer_notification=None) -> web.Response:
    """Funds transfer between accounts refunded

    Adyen sends this notification when [funds transferred between accounts are refunded](https://docs.adyen.com/api-explorer/#/Fund/v6/latest/refundFundsTransfer).

    :param refund_funds_transfer_notification: 
    :type refund_funds_transfer_notification: dict | bytes

    """
    refund_funds_transfer_notification = RefundFundsTransferNotification.from_dict(refund_funds_transfer_notification)
    return web.Response(status=200)


async def post_scheduledrefunds(request: web.Request, scheduled_refunds_notification=None) -> web.Response:
    """&#39;Refund Transfers Not Paid Out&#39; call processed and refunds scheduled

    Adyen sends this notification when a request to [refund transfers that are not yet paid out](https://docs.adyen.com/api-explorer/#/Fund/latest/refundNotPaidOutTransfers) is processed and the associated refunds are scheduled.

    :param scheduled_refunds_notification: 
    :type scheduled_refunds_notification: dict | bytes

    """
    scheduled_refunds_notification = ScheduledRefundsNotification.from_dict(scheduled_refunds_notification)
    return web.Response(status=200)


async def post_transferfunds(request: web.Request, transfer_funds_notification=None) -> web.Response:
    """Funds transferred between accounts

    Adyen sends this notification when [funds are transferred between accounts](https://docs.adyen.com/api-explorer/#/Fund/latest/post/transferFunds).

    :param transfer_funds_notification: 
    :type transfer_funds_notification: dict | bytes

    """
    transfer_funds_notification = TransferFundsNotification.from_dict(transfer_funds_notification)
    return web.Response(status=200)
