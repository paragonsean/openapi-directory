from typing import List, Dict
from aiohttp import web

from openapi_server.models.list_verification_attempt_response import ListVerificationAttemptResponse
from openapi_server.models.verification_attempt_enum_channels import VerificationAttemptEnumChannels
from openapi_server.models.verification_attempt_enum_conversion_status import VerificationAttemptEnumConversionStatus
from openapi_server.models.verify_v2_verification_attempt import VerifyV2VerificationAttempt
from openapi_server import util


async def fetch_verification_attempt(request: web.Request, sid) -> web.Response:
    """fetch_verification_attempt

    Fetch a specific verification attempt.

    :param sid: The unique SID identifier of a Verification Attempt
    :type sid: str

    """
    return web.Response(status=200)


async def list_verification_attempt(request: web.Request, date_created_after=None, date_created_before=None, channel_data_to=None, country=None, channel=None, verify_service_sid=None, verification_sid=None, status=None, page_size=None, page=None, page_token=None) -> web.Response:
    """list_verification_attempt

    List all the verification attempts for a given Account.

    :param date_created_after: Datetime filter used to consider only Verification Attempts created after this datetime on the summary aggregation. Given as GMT in ISO 8601 formatted datetime string: yyyy-MM-dd&#39;T&#39;HH:mm:ss&#39;Z.
    :type date_created_after: str
    :param date_created_before: Datetime filter used to consider only Verification Attempts created before this datetime on the summary aggregation. Given as GMT in ISO 8601 formatted datetime string: yyyy-MM-dd&#39;T&#39;HH:mm:ss&#39;Z.
    :type date_created_before: str
    :param channel_data_to: Destination of a verification. It is phone number in E.164 format.
    :type channel_data_to: str
    :param country: Filter used to query Verification Attempts sent to the specified destination country.
    :type country: str
    :param channel: Filter used to query Verification Attempts by communication channel. Valid values are &#x60;SMS&#x60; and &#x60;CALL&#x60;
    :type channel: str
    :param verify_service_sid: Filter used to query Verification Attempts by verify service. Only attempts of the provided SID will be returned.
    :type verify_service_sid: str
    :param verification_sid: Filter used to return all the Verification Attempts of a single verification. Only attempts of the provided verification SID will be returned.
    :type verification_sid: str
    :param status: Filter used to query Verification Attempts by conversion status. Valid values are &#x60;UNCONVERTED&#x60;, for attempts that were not converted, and &#x60;CONVERTED&#x60;, for attempts that were confirmed.
    :type status: str
    :param page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
    :type page_size: int
    :param page: The page index. This value is simply for client state.
    :type page: int
    :param page_token: The page token. This is provided by the API.
    :type page_token: str

    """
    date_created_after = util.deserialize_datetime(date_created_after)
    date_created_before = util.deserialize_datetime(date_created_before)
    return web.Response(status=200)
