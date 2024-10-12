from typing import List, Dict
from aiohttp import web

from openapi_server.models.account_holder_create_notification import AccountHolderCreateNotification
from openapi_server.models.account_holder_status_change_notification import AccountHolderStatusChangeNotification
from openapi_server.models.account_holder_store_status_change_notification import AccountHolderStoreStatusChangeNotification
from openapi_server.models.account_holder_upcoming_deadline_notification import AccountHolderUpcomingDeadlineNotification
from openapi_server.models.account_holder_update_notification import AccountHolderUpdateNotification
from openapi_server.models.account_holder_verification_notification import AccountHolderVerificationNotification
from openapi_server.models.notification_response import NotificationResponse
from openapi_server import util


async def post_accountholdercreated(request: web.Request, account_holder_create_notification=None) -> web.Response:
    """Account holder created

    Adyen sends this webhook when [an account holder is created](https://docs.adyen.com/api-explorer/#/Account/latest/post/createAccountHolder).

    :param account_holder_create_notification: 
    :type account_holder_create_notification: dict | bytes

    """
    account_holder_create_notification = AccountHolderCreateNotification.from_dict(account_holder_create_notification)
    return web.Response(status=200)


async def post_accountholderstatuschange(request: web.Request, account_holder_status_change_notification=None) -> web.Response:
    """Account holder status changed

    Adyen sends this webhook when [the status of an account holder is changed](https://docs.adyen.com/api-explorer/#/Account/latest/post/updateAccountHolderState).

    :param account_holder_status_change_notification: 
    :type account_holder_status_change_notification: dict | bytes

    """
    account_holder_status_change_notification = AccountHolderStatusChangeNotification.from_dict(account_holder_status_change_notification)
    return web.Response(status=200)


async def post_accountholderstorestatuschange(request: web.Request, account_holder_store_status_change_notification=None) -> web.Response:
    """Store status changed

    Adyen sends this webhook when [the status of a store](https://docs.adyen.com/api-explorer/#/Account/latest/post/createAccountHolder__reqParam_accountHolderDetails-storeDetails-status) associated with an account holder is changed.

    :param account_holder_store_status_change_notification: 
    :type account_holder_store_status_change_notification: dict | bytes

    """
    account_holder_store_status_change_notification = AccountHolderStoreStatusChangeNotification.from_dict(account_holder_store_status_change_notification)
    return web.Response(status=200)


async def post_accountholderupcomingdeadline(request: web.Request, account_holder_upcoming_deadline_notification=None) -> web.Response:
    """Upcoming deadline

    Adyen sends this notification when an account holder&#39;s deadline to fulfill the requirements of a specific event is coming up.

    :param account_holder_upcoming_deadline_notification: 
    :type account_holder_upcoming_deadline_notification: dict | bytes

    """
    account_holder_upcoming_deadline_notification = AccountHolderUpcomingDeadlineNotification.from_dict(account_holder_upcoming_deadline_notification)
    return web.Response(status=200)


async def post_accountholderupdated(request: web.Request, account_holder_update_notification=None) -> web.Response:
    """Account holder updated

    Adyen sends this webhook when [an account holder is updated](https://docs.adyen.com/api-explorer/#/Account/latest/post/updateAccountHolder).

    :param account_holder_update_notification: 
    :type account_holder_update_notification: dict | bytes

    """
    account_holder_update_notification = AccountHolderUpdateNotification.from_dict(account_holder_update_notification)
    return web.Response(status=200)


async def post_accountholderverification(request: web.Request, account_holder_verification_notification=None) -> web.Response:
    """Verification results received

    Adyen sends this webhook when verification results are available.

    :param account_holder_verification_notification: 
    :type account_holder_verification_notification: dict | bytes

    """
    account_holder_verification_notification = AccountHolderVerificationNotification.from_dict(account_holder_verification_notification)
    return web.Response(status=200)
