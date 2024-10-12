from typing import List, Dict
from aiohttp import web

from openapi_server.models.api_v2010_account_message_media import ApiV2010AccountMessageMedia
from openapi_server.models.list_media_response import ListMediaResponse
from openapi_server import util


async def delete_media(request: web.Request, account_sid, message_sid, sid) -> web.Response:
    """delete_media

    Delete the Media resource.

    :param account_sid: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that is associated with the Media resource.
    :type account_sid: str
    :param message_sid: The SID of the Message resource that is associated with the Media resource.
    :type message_sid: str
    :param sid: The unique identifier of the to-be-deleted Media resource.
    :type sid: str

    """
    return web.Response(status=200)


async def fetch_media(request: web.Request, account_sid, message_sid, sid) -> web.Response:
    """fetch_media

    Fetch a single Media resource associated with a specific Message resource

    :param account_sid: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) associated with the Media resource.
    :type account_sid: str
    :param message_sid: The SID of the Message resource that is associated with the Media resource.
    :type message_sid: str
    :param sid: The Twilio-provided string that uniquely identifies the Media resource to fetch.
    :type sid: str

    """
    return web.Response(status=200)


async def list_media(request: web.Request, account_sid, message_sid, date_created=None, date_created2=None, date_created3=None, page_size=None, page=None, page_token=None) -> web.Response:
    """list_media

    Read a list of Media resources associated with a specific Message resource

    :param account_sid: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that is associated with the Media resources.
    :type account_sid: str
    :param message_sid: The SID of the Message resource that is associated with the Media resources.
    :type message_sid: str
    :param date_created: Only include Media resources that were created on this date. Specify a date as &#x60;YYYY-MM-DD&#x60; in GMT, for example: &#x60;2009-07-06&#x60;, to read Media that were created on this date. You can also specify an inequality, such as &#x60;StartTime&lt;&#x3D;YYYY-MM-DD&#x60;, to read Media that were created on or before midnight of this date, and &#x60;StartTime&gt;&#x3D;YYYY-MM-DD&#x60; to read Media that were created on or after midnight of this date.
    :type date_created: str
    :param date_created2: Only include Media resources that were created on this date. Specify a date as &#x60;YYYY-MM-DD&#x60; in GMT, for example: &#x60;2009-07-06&#x60;, to read Media that were created on this date. You can also specify an inequality, such as &#x60;StartTime&lt;&#x3D;YYYY-MM-DD&#x60;, to read Media that were created on or before midnight of this date, and &#x60;StartTime&gt;&#x3D;YYYY-MM-DD&#x60; to read Media that were created on or after midnight of this date.
    :type date_created2: str
    :param date_created3: Only include Media resources that were created on this date. Specify a date as &#x60;YYYY-MM-DD&#x60; in GMT, for example: &#x60;2009-07-06&#x60;, to read Media that were created on this date. You can also specify an inequality, such as &#x60;StartTime&lt;&#x3D;YYYY-MM-DD&#x60;, to read Media that were created on or before midnight of this date, and &#x60;StartTime&gt;&#x3D;YYYY-MM-DD&#x60; to read Media that were created on or after midnight of this date.
    :type date_created3: str
    :param page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
    :type page_size: int
    :param page: The page index. This value is simply for client state.
    :type page: int
    :param page_token: The page token. This is provided by the API.
    :type page_token: str

    """
    date_created = util.deserialize_datetime(date_created)
    date_created2 = util.deserialize_datetime(date_created2)
    date_created3 = util.deserialize_datetime(date_created3)
    return web.Response(status=200)
