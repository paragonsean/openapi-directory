from typing import List, Dict
from aiohttp import web

from openapi_server.models.api_v2010_account_recording_recording_add_on_result import ApiV2010AccountRecordingRecordingAddOnResult
from openapi_server.models.list_recording_add_on_result_response import ListRecordingAddOnResultResponse
from openapi_server import util


async def delete_recording_add_on_result(request: web.Request, account_sid, reference_sid, sid) -> web.Response:
    """delete_recording_add_on_result

    Delete a result and purge all associated Payloads

    :param account_sid: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Recording AddOnResult resources to delete.
    :type account_sid: str
    :param reference_sid: The SID of the recording to which the result to delete belongs.
    :type reference_sid: str
    :param sid: The Twilio-provided string that uniquely identifies the Recording AddOnResult resource to delete.
    :type sid: str

    """
    return web.Response(status=200)


async def fetch_recording_add_on_result(request: web.Request, account_sid, reference_sid, sid) -> web.Response:
    """fetch_recording_add_on_result

    Fetch an instance of an AddOnResult

    :param account_sid: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Recording AddOnResult resource to fetch.
    :type account_sid: str
    :param reference_sid: The SID of the recording to which the result to fetch belongs.
    :type reference_sid: str
    :param sid: The Twilio-provided string that uniquely identifies the Recording AddOnResult resource to fetch.
    :type sid: str

    """
    return web.Response(status=200)


async def list_recording_add_on_result(request: web.Request, account_sid, reference_sid, page_size=None, page=None, page_token=None) -> web.Response:
    """list_recording_add_on_result

    Retrieve a list of results belonging to the recording

    :param account_sid: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Recording AddOnResult resources to read.
    :type account_sid: str
    :param reference_sid: The SID of the recording to which the result to read belongs.
    :type reference_sid: str
    :param page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
    :type page_size: int
    :param page: The page index. This value is simply for client state.
    :type page: int
    :param page_token: The page token. This is provided by the API.
    :type page_token: str

    """
    return web.Response(status=200)
