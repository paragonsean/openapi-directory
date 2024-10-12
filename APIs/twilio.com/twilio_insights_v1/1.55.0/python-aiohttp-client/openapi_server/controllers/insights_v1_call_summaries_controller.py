from typing import List, Dict
from aiohttp import web

from openapi_server.models.call_summaries_enum_answered_by import CallSummariesEnumAnsweredBy
from openapi_server.models.call_summaries_enum_processing_state_request import CallSummariesEnumProcessingStateRequest
from openapi_server.models.call_summaries_enum_sort_by import CallSummariesEnumSortBy
from openapi_server.models.list_call_summaries_response import ListCallSummariesResponse
from openapi_server import util


async def list_call_summaries(request: web.Request, _from=None, to=None, from_carrier=None, to_carrier=None, from_country_code=None, to_country_code=None, branded=None, verified_caller=None, has_tag=None, start_time=None, end_time=None, call_type=None, call_state=None, direction=None, processing_state=None, sort_by=None, subaccount=None, abnormal_session=None, answered_by=None, answered_by_annotation=None, connectivity_issue_annotation=None, quality_issue_annotation=None, spam_annotation=None, call_score_annotation=None, page_size=None, page=None, page_token=None) -> web.Response:
    """list_call_summaries

    Get a list of Call Summaries.

    :param _from: A calling party. Could be an E.164 number, a SIP URI, or a Twilio Client registered name.
    :type _from: str
    :param to: A called party. Could be an E.164 number, a SIP URI, or a Twilio Client registered name.
    :type to: str
    :param from_carrier: An origination carrier.
    :type from_carrier: str
    :param to_carrier: A destination carrier.
    :type to_carrier: str
    :param from_country_code: A source country code based on phone number in From.
    :type from_country_code: str
    :param to_country_code: A destination country code. Based on phone number in To.
    :type to_country_code: str
    :param branded: A boolean flag indicating whether or not the calls were branded using Twilio Branded Calls.
    :type branded: bool
    :param verified_caller: A boolean flag indicating whether or not the caller was verified using SHAKEN/STIR.
    :type verified_caller: bool
    :param has_tag: A boolean flag indicating the presence of one or more [Voice Insights Call Tags](https://www.twilio.com/docs/voice/voice-insights/api/call/details-call-tags).
    :type has_tag: bool
    :param start_time: A Start time of the calls. xm (x minutes), xh (x hours), xd (x days), 1w, 30m, 3d, 4w or datetime-ISO. Defaults to 4h.
    :type start_time: str
    :param end_time: An End Time of the calls. xm (x minutes), xh (x hours), xd (x days), 1w, 30m, 3d, 4w or datetime-ISO. Defaults to 0m.
    :type end_time: str
    :param call_type: A Call Type of the calls. One of &#x60;carrier&#x60;, &#x60;sip&#x60;, &#x60;trunking&#x60; or &#x60;client&#x60;.
    :type call_type: str
    :param call_state: A Call State of the calls. One of &#x60;ringing&#x60;, &#x60;completed&#x60;, &#x60;busy&#x60;, &#x60;fail&#x60;, &#x60;noanswer&#x60;, &#x60;canceled&#x60;, &#x60;answered&#x60;, &#x60;undialed&#x60;.
    :type call_state: str
    :param direction: A Direction of the calls. One of &#x60;outbound_api&#x60;, &#x60;outbound_dial&#x60;, &#x60;inbound&#x60;, &#x60;trunking_originating&#x60;, &#x60;trunking_terminating&#x60;.
    :type direction: str
    :param processing_state: A Processing State of the Call Summaries. One of &#x60;completed&#x60;, &#x60;partial&#x60; or &#x60;all&#x60;.
    :type processing_state: str
    :param sort_by: A Sort By criterion for the returned list of Call Summaries. One of &#x60;start_time&#x60; or &#x60;end_time&#x60;.
    :type sort_by: str
    :param subaccount: A unique SID identifier of a Subaccount.
    :type subaccount: str
    :param abnormal_session: A boolean flag indicating an abnormal session where the last SIP response was not 200 OK.
    :type abnormal_session: bool
    :param answered_by: An Answered By value for the calls based on &#x60;Answering Machine Detection (AMD)&#x60;. One of &#x60;unknown&#x60;, &#x60;machine_start&#x60;, &#x60;machine_end_beep&#x60;, &#x60;machine_end_silence&#x60;, &#x60;machine_end_other&#x60;, &#x60;human&#x60; or &#x60;fax&#x60;.
    :type answered_by: str
    :param answered_by_annotation: Either machine or human.
    :type answered_by_annotation: str
    :param connectivity_issue_annotation: A Connectivity Issue with the calls. One of &#x60;no_connectivity_issue&#x60;, &#x60;invalid_number&#x60;, &#x60;caller_id&#x60;, &#x60;dropped_call&#x60;, or &#x60;number_reachability&#x60;.
    :type connectivity_issue_annotation: str
    :param quality_issue_annotation: A subjective Quality Issue with the calls. One of &#x60;no_quality_issue&#x60;, &#x60;low_volume&#x60;, &#x60;choppy_robotic&#x60;, &#x60;echo&#x60;, &#x60;dtmf&#x60;, &#x60;latency&#x60;, &#x60;owa&#x60;, &#x60;static_noise&#x60;.
    :type quality_issue_annotation: str
    :param spam_annotation: A boolean flag indicating spam calls.
    :type spam_annotation: bool
    :param call_score_annotation: A Call Score of the calls. Use a range of 1-5 to indicate the call experience score, with the following mapping as a reference for the rated call [5: Excellent, 4: Good, 3 : Fair, 2 : Poor, 1: Bad].
    :type call_score_annotation: str
    :param page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
    :type page_size: int
    :param page: The page index. This value is simply for client state.
    :type page: int
    :param page_token: The page token. This is provided by the API.
    :type page_token: str

    """
    return web.Response(status=200)
