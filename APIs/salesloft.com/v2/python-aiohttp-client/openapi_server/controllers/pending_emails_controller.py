from typing import List, Dict
from aiohttp import web

from openapi_server.models.pending_email import PendingEmail
from openapi_server import util


async def v2_pending_emails_id_json_put(request: web.Request, id, message_id, status, error_message=None, sent_at=None) -> web.Response:
    """Updates the status of an email sent by an External Email Client

    Updates the status of an email sent by an External Email Client. Does not affect lofted emails. 

    :param id: Email ID
    :type id: str
    :param message_id: The message id of the email that was sent
    :type message_id: str
    :param status: Delivery status of the email.  Valid statuses are &#39;sent&#39; and &#39;failed&#39;
    :type status: str
    :param error_message: The error message indicating why the email failed to send
    :type error_message: str
    :param sent_at: The time that the email was actually sent in iso8601 format
    :type sent_at: str

    """
    return web.Response(status=200)


async def v2_pending_emails_json_get(request: web.Request, per_page=None, page=None, include_paging_counts=None, limit_paging_counts=None) -> web.Response:
    """Fetches a list of emails ready to be sent by an external email service. Only emails sent with an External Email Client will appear here.

    Fetches a list of emails ready to be sent by an external email service. 

    :param per_page: How many records to show per page in the range [1, 100]. Defaults to 25
    :type per_page: int
    :param page: The current page to fetch results from. Defaults to 1
    :type page: int
    :param include_paging_counts: Whether to include total_pages and total_count in the metadata. Defaults to false
    :type include_paging_counts: bool
    :param limit_paging_counts: Specifies whether the max limit of 10k records should be applied to pagination counts. Affects the total_count and total_pages data
    :type limit_paging_counts: bool

    """
    return web.Response(status=200)
