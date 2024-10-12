from typing import List, Dict
from aiohttp import web

from openapi_server.models.api_v2010_account_recording_recording_add_on_result_recording_add_on_result_payload import ApiV2010AccountRecordingRecordingAddOnResultRecordingAddOnResultPayload
from openapi_server.models.list_recording_add_on_result_payload_response import ListRecordingAddOnResultPayloadResponse
from openapi_server import util


async def delete_recording_add_on_result_payload(request: web.Request, account_sid, reference_sid, add_on_result_sid, sid) -> web.Response:
    """delete_recording_add_on_result_payload

    Delete a payload from the result along with all associated Data

    :param account_sid: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Recording AddOnResult Payload resources to delete.
    :type account_sid: str
    :param reference_sid: The SID of the recording to which the AddOnResult resource that contains the payloads to delete belongs.
    :type reference_sid: str
    :param add_on_result_sid: The SID of the AddOnResult to which the payloads to delete belongs.
    :type add_on_result_sid: str
    :param sid: The Twilio-provided string that uniquely identifies the Recording AddOnResult Payload resource to delete.
    :type sid: str

    """
    return web.Response(status=200)


async def fetch_recording_add_on_result_payload(request: web.Request, account_sid, reference_sid, add_on_result_sid, sid) -> web.Response:
    """fetch_recording_add_on_result_payload

    Fetch an instance of a result payload

    :param account_sid: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Recording AddOnResult Payload resource to fetch.
    :type account_sid: str
    :param reference_sid: The SID of the recording to which the AddOnResult resource that contains the payload to fetch belongs.
    :type reference_sid: str
    :param add_on_result_sid: The SID of the AddOnResult to which the payload to fetch belongs.
    :type add_on_result_sid: str
    :param sid: The Twilio-provided string that uniquely identifies the Recording AddOnResult Payload resource to fetch.
    :type sid: str

    """
    return web.Response(status=200)


async def list_recording_add_on_result_payload(request: web.Request, account_sid, reference_sid, add_on_result_sid, page_size=None, page=None, page_token=None) -> web.Response:
    """list_recording_add_on_result_payload

    Retrieve a list of payloads belonging to the AddOnResult

    :param account_sid: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Recording AddOnResult Payload resources to read.
    :type account_sid: str
    :param reference_sid: The SID of the recording to which the AddOnResult resource that contains the payloads to read belongs.
    :type reference_sid: str
    :param add_on_result_sid: The SID of the AddOnResult to which the payloads to read belongs.
    :type add_on_result_sid: str
    :param page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
    :type page_size: int
    :param page: The page index. This value is simply for client state.
    :type page: int
    :param page_token: The page token. This is provided by the API.
    :type page_token: str

    """
    return web.Response(status=200)
