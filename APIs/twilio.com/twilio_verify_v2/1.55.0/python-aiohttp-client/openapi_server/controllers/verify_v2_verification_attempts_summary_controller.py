from typing import List, Dict
from aiohttp import web

from openapi_server.models.verification_attempts_summary_enum_channels import VerificationAttemptsSummaryEnumChannels
from openapi_server.models.verify_v2_verification_attempts_summary import VerifyV2VerificationAttemptsSummary
from openapi_server import util


async def fetch_verification_attempts_summary(request: web.Request, verify_service_sid=None, date_created_after=None, date_created_before=None, country=None, channel=None, destination_prefix=None) -> web.Response:
    """fetch_verification_attempts_summary

    Get a summary of how many attempts were made and how many were converted.

    :param verify_service_sid: Filter used to consider only Verification Attempts of the given verify service on the summary aggregation.
    :type verify_service_sid: str
    :param date_created_after: Datetime filter used to consider only Verification Attempts created after this datetime on the summary aggregation. Given as GMT in ISO 8601 formatted datetime string: yyyy-MM-dd&#39;T&#39;HH:mm:ss&#39;Z.
    :type date_created_after: str
    :param date_created_before: Datetime filter used to consider only Verification Attempts created before this datetime on the summary aggregation. Given as GMT in ISO 8601 formatted datetime string: yyyy-MM-dd&#39;T&#39;HH:mm:ss&#39;Z.
    :type date_created_before: str
    :param country: Filter used to consider only Verification Attempts sent to the specified destination country on the summary aggregation.
    :type country: str
    :param channel: Filter Verification Attempts considered on the summary aggregation by communication channel. Valid values are &#x60;SMS&#x60;, &#x60;CALL&#x60; and &#x60;WHATSAPP&#x60;
    :type channel: str
    :param destination_prefix: Filter the Verification Attempts considered on the summary aggregation by Destination prefix. It is the prefix of a phone number in E.164 format.
    :type destination_prefix: str

    """
    date_created_after = util.deserialize_datetime(date_created_after)
    date_created_before = util.deserialize_datetime(date_created_before)
    return web.Response(status=200)
