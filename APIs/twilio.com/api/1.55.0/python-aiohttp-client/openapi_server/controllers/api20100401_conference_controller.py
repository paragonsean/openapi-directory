from typing import List, Dict
from aiohttp import web

from openapi_server.models.api_v2010_account_conference import ApiV2010AccountConference
from openapi_server.models.conference_enum_status import ConferenceEnumStatus
from openapi_server.models.conference_enum_update_status import ConferenceEnumUpdateStatus
from openapi_server.models.list_conference_response import ListConferenceResponse
from openapi_server import util


async def fetch_conference(request: web.Request, account_sid, sid) -> web.Response:
    """fetch_conference

    Fetch an instance of a conference

    :param account_sid: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Conference resource(s) to fetch.
    :type account_sid: str
    :param sid: The Twilio-provided string that uniquely identifies the Conference resource to fetch
    :type sid: str

    """
    return web.Response(status=200)


async def list_conference(request: web.Request, account_sid, date_created=None, date_created2=None, date_created3=None, date_updated=None, date_updated2=None, date_updated3=None, friendly_name=None, status=None, page_size=None, page=None, page_token=None) -> web.Response:
    """list_conference

    Retrieve a list of conferences belonging to the account used to make the request

    :param account_sid: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Conference resource(s) to read.
    :type account_sid: str
    :param date_created: The &#x60;date_created&#x60; value, specified as &#x60;YYYY-MM-DD&#x60;, of the resources to read. To read conferences that started on or before midnight on a date, use &#x60;&lt;&#x3D;YYYY-MM-DD&#x60;, and to specify  conferences that started on or after midnight on a date, use &#x60;&gt;&#x3D;YYYY-MM-DD&#x60;.
    :type date_created: str
    :param date_created2: The &#x60;date_created&#x60; value, specified as &#x60;YYYY-MM-DD&#x60;, of the resources to read. To read conferences that started on or before midnight on a date, use &#x60;&lt;&#x3D;YYYY-MM-DD&#x60;, and to specify  conferences that started on or after midnight on a date, use &#x60;&gt;&#x3D;YYYY-MM-DD&#x60;.
    :type date_created2: str
    :param date_created3: The &#x60;date_created&#x60; value, specified as &#x60;YYYY-MM-DD&#x60;, of the resources to read. To read conferences that started on or before midnight on a date, use &#x60;&lt;&#x3D;YYYY-MM-DD&#x60;, and to specify  conferences that started on or after midnight on a date, use &#x60;&gt;&#x3D;YYYY-MM-DD&#x60;.
    :type date_created3: str
    :param date_updated: The &#x60;date_updated&#x60; value, specified as &#x60;YYYY-MM-DD&#x60;, of the resources to read. To read conferences that were last updated on or before midnight on a date, use &#x60;&lt;&#x3D;YYYY-MM-DD&#x60;, and to specify conferences that were last updated on or after midnight on a given date, use  &#x60;&gt;&#x3D;YYYY-MM-DD&#x60;.
    :type date_updated: str
    :param date_updated2: The &#x60;date_updated&#x60; value, specified as &#x60;YYYY-MM-DD&#x60;, of the resources to read. To read conferences that were last updated on or before midnight on a date, use &#x60;&lt;&#x3D;YYYY-MM-DD&#x60;, and to specify conferences that were last updated on or after midnight on a given date, use  &#x60;&gt;&#x3D;YYYY-MM-DD&#x60;.
    :type date_updated2: str
    :param date_updated3: The &#x60;date_updated&#x60; value, specified as &#x60;YYYY-MM-DD&#x60;, of the resources to read. To read conferences that were last updated on or before midnight on a date, use &#x60;&lt;&#x3D;YYYY-MM-DD&#x60;, and to specify conferences that were last updated on or after midnight on a given date, use  &#x60;&gt;&#x3D;YYYY-MM-DD&#x60;.
    :type date_updated3: str
    :param friendly_name: The string that identifies the Conference resources to read.
    :type friendly_name: str
    :param status: The status of the resources to read. Can be: &#x60;init&#x60;, &#x60;in-progress&#x60;, or &#x60;completed&#x60;.
    :type status: str
    :param page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
    :type page_size: int
    :param page: The page index. This value is simply for client state.
    :type page: int
    :param page_token: The page token. This is provided by the API.
    :type page_token: str

    """
    date_created = util.deserialize_date(date_created)
    date_created2 = util.deserialize_date(date_created2)
    date_created3 = util.deserialize_date(date_created3)
    date_updated = util.deserialize_date(date_updated)
    date_updated2 = util.deserialize_date(date_updated2)
    date_updated3 = util.deserialize_date(date_updated3)
    return web.Response(status=200)


async def update_conference(request: web.Request, account_sid, sid, announce_method=None, announce_url=None, status=None) -> web.Response:
    """update_conference

    

    :param account_sid: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Conference resource(s) to update.
    :type account_sid: str
    :param sid: The Twilio-provided string that uniquely identifies the Conference resource to update
    :type sid: str
    :param announce_method: The HTTP method used to call &#x60;announce_url&#x60;. Can be: &#x60;GET&#x60; or &#x60;POST&#x60; and the default is &#x60;POST&#x60;
    :type announce_method: str
    :param announce_url: The URL we should call to announce something into the conference. The URL may return an MP3 file, a WAV file, or a TwiML document that contains &#x60;&lt;Play&gt;&#x60;, &#x60;&lt;Say&gt;&#x60;, &#x60;&lt;Pause&gt;&#x60;, or &#x60;&lt;Redirect&gt;&#x60; verbs.
    :type announce_url: str
    :param status: 
    :type status: str

    """
    return web.Response(status=200)
