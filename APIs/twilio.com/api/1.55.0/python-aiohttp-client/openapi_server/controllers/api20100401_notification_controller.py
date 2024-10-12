from typing import List, Dict
from aiohttp import web

from openapi_server.models.api_v2010_account_call_call_notification_instance import ApiV2010AccountCallCallNotificationInstance
from openapi_server.models.api_v2010_account_notification_instance import ApiV2010AccountNotificationInstance
from openapi_server.models.list_call_notification_response import ListCallNotificationResponse
from openapi_server.models.list_notification_response import ListNotificationResponse
from openapi_server import util


async def fetch_call_notification(request: web.Request, account_sid, call_sid, sid) -> web.Response:
    """fetch_call_notification

    

    :param account_sid: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Call Notification resource to fetch.
    :type account_sid: str
    :param call_sid: The [Call](https://www.twilio.com/docs/voice/api/call-resource) SID of the Call Notification resource to fetch.
    :type call_sid: str
    :param sid: The Twilio-provided string that uniquely identifies the Call Notification resource to fetch.
    :type sid: str

    """
    return web.Response(status=200)


async def fetch_notification(request: web.Request, account_sid, sid) -> web.Response:
    """fetch_notification

    Fetch a notification belonging to the account used to make the request

    :param account_sid: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Notification resource to fetch.
    :type account_sid: str
    :param sid: The Twilio-provided string that uniquely identifies the Notification resource to fetch.
    :type sid: str

    """
    return web.Response(status=200)


async def list_call_notification(request: web.Request, account_sid, call_sid, log=None, message_date=None, message_date2=None, message_date3=None, page_size=None, page=None, page_token=None) -> web.Response:
    """list_call_notification

    

    :param account_sid: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Call Notification resources to read.
    :type account_sid: str
    :param call_sid: The [Call](https://www.twilio.com/docs/voice/api/call-resource) SID of the Call Notification resources to read.
    :type call_sid: str
    :param log: Only read notifications of the specified log level. Can be:  &#x60;0&#x60; to read only ERROR notifications or &#x60;1&#x60; to read only WARNING notifications. By default, all notifications are read.
    :type log: int
    :param message_date: Only show notifications for the specified date, formatted as &#x60;YYYY-MM-DD&#x60;. You can also specify an inequality, such as &#x60;&lt;&#x3D;YYYY-MM-DD&#x60; for messages logged at or before midnight on a date, or &#x60;&gt;&#x3D;YYYY-MM-DD&#x60; for messages logged at or after midnight on a date.
    :type message_date: str
    :param message_date2: Only show notifications for the specified date, formatted as &#x60;YYYY-MM-DD&#x60;. You can also specify an inequality, such as &#x60;&lt;&#x3D;YYYY-MM-DD&#x60; for messages logged at or before midnight on a date, or &#x60;&gt;&#x3D;YYYY-MM-DD&#x60; for messages logged at or after midnight on a date.
    :type message_date2: str
    :param message_date3: Only show notifications for the specified date, formatted as &#x60;YYYY-MM-DD&#x60;. You can also specify an inequality, such as &#x60;&lt;&#x3D;YYYY-MM-DD&#x60; for messages logged at or before midnight on a date, or &#x60;&gt;&#x3D;YYYY-MM-DD&#x60; for messages logged at or after midnight on a date.
    :type message_date3: str
    :param page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
    :type page_size: int
    :param page: The page index. This value is simply for client state.
    :type page: int
    :param page_token: The page token. This is provided by the API.
    :type page_token: str

    """
    message_date = util.deserialize_date(message_date)
    message_date2 = util.deserialize_date(message_date2)
    message_date3 = util.deserialize_date(message_date3)
    return web.Response(status=200)


async def list_notification(request: web.Request, account_sid, log=None, message_date=None, message_date2=None, message_date3=None, page_size=None, page=None, page_token=None) -> web.Response:
    """list_notification

    Retrieve a list of notifications belonging to the account used to make the request

    :param account_sid: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Notification resources to read.
    :type account_sid: str
    :param log: Only read notifications of the specified log level. Can be:  &#x60;0&#x60; to read only ERROR notifications or &#x60;1&#x60; to read only WARNING notifications. By default, all notifications are read.
    :type log: int
    :param message_date: Only show notifications for the specified date, formatted as &#x60;YYYY-MM-DD&#x60;. You can also specify an inequality, such as &#x60;&lt;&#x3D;YYYY-MM-DD&#x60; for messages logged at or before midnight on a date, or &#x60;&gt;&#x3D;YYYY-MM-DD&#x60; for messages logged at or after midnight on a date.
    :type message_date: str
    :param message_date2: Only show notifications for the specified date, formatted as &#x60;YYYY-MM-DD&#x60;. You can also specify an inequality, such as &#x60;&lt;&#x3D;YYYY-MM-DD&#x60; for messages logged at or before midnight on a date, or &#x60;&gt;&#x3D;YYYY-MM-DD&#x60; for messages logged at or after midnight on a date.
    :type message_date2: str
    :param message_date3: Only show notifications for the specified date, formatted as &#x60;YYYY-MM-DD&#x60;. You can also specify an inequality, such as &#x60;&lt;&#x3D;YYYY-MM-DD&#x60; for messages logged at or before midnight on a date, or &#x60;&gt;&#x3D;YYYY-MM-DD&#x60; for messages logged at or after midnight on a date.
    :type message_date3: str
    :param page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
    :type page_size: int
    :param page: The page index. This value is simply for client state.
    :type page: int
    :param page_token: The page token. This is provided by the API.
    :type page_token: str

    """
    message_date = util.deserialize_date(message_date)
    message_date2 = util.deserialize_date(message_date2)
    message_date3 = util.deserialize_date(message_date3)
    return web.Response(status=200)
