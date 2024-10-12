from typing import List, Dict
from aiohttp import web

from openapi_server.models.annotation_enum_answered_by import AnnotationEnumAnsweredBy
from openapi_server.models.annotation_enum_connectivity_issue import AnnotationEnumConnectivityIssue
from openapi_server.models.insights_v1_call_annotation import InsightsV1CallAnnotation
from openapi_server import util


async def fetch_annotation(request: web.Request, call_sid) -> web.Response:
    """fetch_annotation

    Get the Annotation for a specific Call.

    :param call_sid: The unique SID identifier of the Call.
    :type call_sid: str

    """
    return web.Response(status=200)


async def update_annotation(request: web.Request, call_sid, answered_by=None, call_score=None, comment=None, connectivity_issue=None, incident=None, quality_issues=None, spam=None) -> web.Response:
    """update_annotation

    Update an Annotation for a specific Call.

    :param call_sid: The unique string that Twilio created to identify this Call resource. It always starts with a CA.
    :type call_sid: str
    :param answered_by: 
    :type answered_by: str
    :param call_score: Specify the call score. This is of type integer. Use a range of 1-5 to indicate the call experience score, with the following mapping as a reference for rating the call [5: Excellent, 4: Good, 3 : Fair, 2 : Poor, 1: Bad].
    :type call_score: int
    :param comment: Specify any comments pertaining to the call. &#x60;comment&#x60; has a maximum character limit of 100. Twilio does not treat this field as PII, so no PII should be included in the &#x60;comment&#x60;.
    :type comment: str
    :param connectivity_issue: 
    :type connectivity_issue: str
    :param incident: Associate this call with an incident or support ticket. The &#x60;incident&#x60; parameter is of type string with a maximum character limit of 100. Twilio does not treat this field as PII, so no PII should be included in &#x60;incident&#x60;.
    :type incident: str
    :param quality_issues: Specify if the call had any subjective quality issues. Possible values, one or more of &#x60;no_quality_issue&#x60;, &#x60;low_volume&#x60;, &#x60;choppy_robotic&#x60;, &#x60;echo&#x60;, &#x60;dtmf&#x60;, &#x60;latency&#x60;, &#x60;owa&#x60;, &#x60;static_noise&#x60;. Use comma separated values to indicate multiple quality issues for the same call.
    :type quality_issues: str
    :param spam: A boolean flag to indicate if the call was a spam call. Use this to provide feedback on whether calls placed from your account were marked as spam, or if inbound calls received by your account were unwanted spam. Use &#x60;true&#x60; if the call was a spam call.
    :type spam: bool

    """
    return web.Response(status=200)
