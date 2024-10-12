from typing import List, Dict
from aiohttp import web

from openapi_server.models.account_close_notification import AccountCloseNotification
from openapi_server.models.account_create_notification import AccountCreateNotification
from openapi_server.models.account_update_notification import AccountUpdateNotification
from openapi_server.models.notification_response import NotificationResponse
from openapi_server import util


async def post_accountclosed(request: web.Request, account_close_notification=None) -> web.Response:
    """Account closed

    Adyen sends this webhook when [an account is closed](https://docs.adyen.com/api-explorer/#/Account/latest/post/closeAccount).

    :param account_close_notification: 
    :type account_close_notification: dict | bytes

    """
    account_close_notification = AccountCloseNotification.from_dict(account_close_notification)
    return web.Response(status=200)


async def post_accountcreated(request: web.Request, account_create_notification=None) -> web.Response:
    """Account created

    Adyen sends this webhook when [an account is created](https://docs.adyen.com/api-explorer/#/Account/latest/post/createAccount).

    :param account_create_notification: 
    :type account_create_notification: dict | bytes

    """
    account_create_notification = AccountCreateNotification.from_dict(account_create_notification)
    return web.Response(status=200)


async def post_accountupdated(request: web.Request, account_update_notification=None) -> web.Response:
    """Account updated

    Adyen sends this webhook when [an account is updated](https://docs.adyen.com/api-explorer/#/Account/latest/post/updateAccount).

    :param account_update_notification: 
    :type account_update_notification: dict | bytes

    """
    account_update_notification = AccountUpdateNotification.from_dict(account_update_notification)
    return web.Response(status=200)
