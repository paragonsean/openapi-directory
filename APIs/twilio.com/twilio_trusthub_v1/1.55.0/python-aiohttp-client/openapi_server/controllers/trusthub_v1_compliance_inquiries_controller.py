from typing import List, Dict
from aiohttp import web

from openapi_server.models.trusthub_v1_compliance_inquiry import TrusthubV1ComplianceInquiry
from openapi_server import util


async def create_compliance_inquiry(request: web.Request, primary_profile_sid, notification_email=None) -> web.Response:
    """create_compliance_inquiry

    Create a new Compliance Inquiry for the authenticated account. This is necessary to start a new embedded session.

    :param primary_profile_sid: The unique SID identifier of the Primary Customer Profile that should be used as a parent. Only necessary when creating a secondary Customer Profile.
    :type primary_profile_sid: str
    :param notification_email: The email address that approval status updates will be sent to. If not specified, the email address associated with your primary customer profile will be used.
    :type notification_email: str

    """
    return web.Response(status=200)


async def update_compliance_inquiry(request: web.Request, customer_id, primary_profile_sid) -> web.Response:
    """update_compliance_inquiry

    Resume a specific Compliance Inquiry that has expired, or re-open a rejected Compliance Inquiry for editing.

    :param customer_id: The unique CustomerId matching the Customer Profile/Compliance Inquiry that should be resumed or resubmitted. This value will have been returned by the initial Compliance Inquiry creation call.
    :type customer_id: str
    :param primary_profile_sid: The unique SID identifier of the Primary Customer Profile that should be used as a parent. Only necessary when creating a secondary Customer Profile.
    :type primary_profile_sid: str

    """
    return web.Response(status=200)
