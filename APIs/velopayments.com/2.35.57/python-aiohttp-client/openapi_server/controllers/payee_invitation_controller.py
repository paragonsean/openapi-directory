from typing import List, Dict
from aiohttp import web

from openapi_server.models.create_payee_v3_request import CreatePayeeV3Request
from openapi_server.models.create_payees_csv_response_v3 import CreatePayeesCSVResponseV3
from openapi_server.models.create_payees_csv_response_v4 import CreatePayeesCSVResponseV4
from openapi_server.models.create_payees_request_v3 import CreatePayeesRequestV3
from openapi_server.models.create_payees_request_v4 import CreatePayeesRequestV4
from openapi_server.models.inline_response400 import InlineResponse400
from openapi_server.models.inline_response401 import InlineResponse401
from openapi_server.models.inline_response403 import InlineResponse403
from openapi_server.models.inline_response404 import InlineResponse404
from openapi_server.models.inline_response409 import InlineResponse409
from openapi_server.models.invite_payee_request_v3 import InvitePayeeRequestV3
from openapi_server.models.invite_payee_request_v4 import InvitePayeeRequestV4
from openapi_server.models.paged_payee_invitation_status_response_v3 import PagedPayeeInvitationStatusResponseV3
from openapi_server.models.paged_payee_invitation_status_response_v4 import PagedPayeeInvitationStatusResponseV4
from openapi_server.models.query_batch_response_v3 import QueryBatchResponseV3
from openapi_server.models.query_batch_response_v4 import QueryBatchResponseV4
from openapi_server.models.v4_create_payee_request import V4CreatePayeeRequest
from openapi_server import util


async def create_payee_v3(request: web.Request, body=None) -> web.Response:
    """Initiate Payee Creation

    &lt;p&gt;Use v4 instead&lt;/p&gt; Initiate the process of creating 1 to 2000 payees in a batch Use the response location header to query for status (201 - Created, 400 - invalid request body. In addition to standard semantic validations, a 400 will also result if there is a duplicate remote id within the batch / if there is a duplicate email within the batch, i.e. if there is a conflict between the data provided for one payee within the batch and that provided for another payee within the same batch). The validation at this stage is intra-batch only. Validation against payees who have already been invited occurs subsequently during processing of the batch. 

    :param body: Post payees to create.
    :type body: dict | bytes

    """
    body = CreatePayeesRequestV3.from_dict(body)
    return web.Response(status=200)


async def get_payees_invitation_status_v3(request: web.Request, payor_id, payee_id=None, invitation_status=None, page=None, page_size=None) -> web.Response:
    """Get Payee Invitation Status

    &lt;p&gt;Use v4 instead&lt;/p&gt; &lt;p&gt;Returns a filtered, paginated list of payees associated with a payor, along with invitation status and grace period end date.&lt;/p&gt; 

    :param payor_id: The account owner Payor ID
    :type payor_id: str
    :type payor_id: str
    :param payee_id: The UUID of the payee.
    :type payee_id: str
    :type payee_id: str
    :param invitation_status: The invitation status of the payees.
    :type invitation_status: str
    :param page: Page number. Default is 1.
    :type page: int
    :param page_size: Page size. Default is 25. Max allowable is 100.
    :type page_size: int

    """
    return web.Response(status=200)


async def get_payees_invitation_status_v4(request: web.Request, payor_id, payee_id=None, invitation_status=None, page=None, page_size=None) -> web.Response:
    """Get Payee Invitation Status

    Returns a filtered, paginated list of payees associated with a payor, along with invitation status and grace period end date. 

    :param payor_id: The account owner Payor ID
    :type payor_id: str
    :type payor_id: str
    :param payee_id: The UUID of the payee.
    :type payee_id: str
    :type payee_id: str
    :param invitation_status: The invitation status of the payees.
    :type invitation_status: str
    :param page: Page number. Default is 1.
    :type page: int
    :param page_size: Page size. Default is 25. Max allowable is 100.
    :type page_size: int

    """
    return web.Response(status=200)


async def query_batch_status_v3(request: web.Request, batch_id) -> web.Response:
    """Query Batch Status

    &lt;p&gt;Use v4 instead&lt;/p&gt; Fetch the status of a specific batch of payees. The batch is fully processed when status is ACCEPTED and pendingCount is 0 ( 200 - OK, 404 - batch not found ). 

    :param batch_id: Batch Id
    :type batch_id: str
    :type batch_id: str

    """
    return web.Response(status=200)


async def query_batch_status_v4(request: web.Request, batch_id) -> web.Response:
    """Query Batch Status

    Fetch the status of a specific batch of payees. The batch is fully processed when status is ACCEPTED and pendingCount is 0 ( 200 - OK, 404 - batch not found ). 

    :param batch_id: Batch Id
    :type batch_id: str
    :type batch_id: str

    """
    return web.Response(status=200)


async def resend_payee_invite_v3(request: web.Request, payee_id, body) -> web.Response:
    """Resend Payee Invite

    &lt;p&gt;Use v4 instead&lt;/p&gt; &lt;p&gt;Resend an invite to the Payee The payee must have already been invited by the payor and not yet accepted or declined&lt;/p&gt; &lt;p&gt;Any previous invites to the payee by this Payor will be invalidated&lt;/p&gt; 

    :param payee_id: The UUID of the payee.
    :type payee_id: str
    :type payee_id: str
    :param body: Provide Payor Id in body of request
    :type body: dict | bytes

    """
    body = InvitePayeeRequestV3.from_dict(body)
    return web.Response(status=200)


async def resend_payee_invite_v4(request: web.Request, payee_id, body) -> web.Response:
    """Resend Payee Invite

    &lt;p&gt;Resend an invite to the Payee The payee must have already been invited by the payor and not yet accepted or declined&lt;/p&gt; &lt;p&gt;Any previous invites to the payee by this Payor will be invalidated&lt;/p&gt; 

    :param payee_id: The UUID of the payee.
    :type payee_id: str
    :type payee_id: str
    :param body: Provide Payor Id in body of request
    :type body: dict | bytes

    """
    body = InvitePayeeRequestV4.from_dict(body)
    return web.Response(status=200)


async def v4_create_payee(request: web.Request, body=None) -> web.Response:
    """Initiate Payee Creation

    &lt;p&gt;Initiate the process of creating 1 to 2000 payees in a batch&lt;/p&gt; &lt;p&gt;Use the batchId in the response to query for status.&lt;/p&gt; &lt;p&gt;In addition to standard semantic validations, a 400 will also result if: &lt;/p&gt; &lt;ul&gt; &lt;li&gt;there is a duplicate remote id within the batch&lt;/li&gt; &lt;li&gt;there is a duplicate email within the batch, i.e. if there is a conflict between the data provided for one payee within the batch and that provided for another payee within the same batch).&lt;/li&gt; &lt;/ul&gt; &lt;p&gt;The validation at this stage is intra-batch only.&lt;/p&gt; &lt;p&gt;Validation against payees who have already been invited occurs subsequently during processing of the batch.&lt;/p&gt; 

    :param body: Post payees to create.
    :type body: dict | bytes

    """
    body = CreatePayeesRequestV4.from_dict(body)
    return web.Response(status=200)
