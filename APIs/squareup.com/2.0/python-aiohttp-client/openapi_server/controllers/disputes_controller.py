from typing import List, Dict
from aiohttp import web

from openapi_server.models.accept_dispute_response import AcceptDisputeResponse
from openapi_server.models.create_dispute_evidence_text_request import CreateDisputeEvidenceTextRequest
from openapi_server.models.create_dispute_evidence_text_response import CreateDisputeEvidenceTextResponse
from openapi_server.models.delete_dispute_evidence_response import DeleteDisputeEvidenceResponse
from openapi_server.models.list_dispute_evidence_response import ListDisputeEvidenceResponse
from openapi_server.models.list_disputes_response import ListDisputesResponse
from openapi_server.models.retrieve_dispute_evidence_response import RetrieveDisputeEvidenceResponse
from openapi_server.models.retrieve_dispute_response import RetrieveDisputeResponse
from openapi_server.models.submit_evidence_response import SubmitEvidenceResponse
from openapi_server import util


async def accept_dispute(request: web.Request, dispute_id) -> web.Response:
    """AcceptDispute

    Accepts the loss on a dispute. Square returns the disputed amount to the cardholder and updates the dispute state to ACCEPTED.  Square debits the disputed amount from the seller’s Square account. If the Square account does not have sufficient funds, Square debits the associated bank account.

    :param dispute_id: The ID of the dispute you want to accept.
    :type dispute_id: str

    """
    return web.Response(status=200)


async def create_dispute_evidence_text(request: web.Request, dispute_id, body) -> web.Response:
    """CreateDisputeEvidenceText

    Uploads text to use as evidence for a dispute challenge.

    :param dispute_id: The ID of the dispute you want to upload evidence for.
    :type dispute_id: str
    :param body: An object containing the fields to POST for the request.  See the corresponding object definition for field details.
    :type body: dict | bytes

    """
    body = CreateDisputeEvidenceTextRequest.from_dict(body)
    return web.Response(status=200)


async def delete_dispute_evidence(request: web.Request, dispute_id, evidence_id) -> web.Response:
    """DeleteDisputeEvidence

    Removes specified evidence from a dispute.  Square does not send the bank any evidence that is removed. Also, you cannot remove evidence after submitting it to the bank using [SubmitEvidence](https://developer.squareup.com/reference/square_2021-08-18/disputes-api/submit-evidence).

    :param dispute_id: The ID of the dispute you want to remove evidence from.
    :type dispute_id: str
    :param evidence_id: The ID of the evidence you want to remove.
    :type evidence_id: str

    """
    return web.Response(status=200)


async def list_dispute_evidence(request: web.Request, dispute_id, cursor=None) -> web.Response:
    """ListDisputeEvidence

    Returns a list of evidence associated with a dispute.

    :param dispute_id: The ID of the dispute.
    :type dispute_id: str
    :param cursor: A pagination cursor returned by a previous call to this endpoint. Provide this cursor to retrieve the next set of results for the original query. For more information, see [Pagination](https://developer.squareup.com/docs/basics/api101/pagination).
    :type cursor: str

    """
    return web.Response(status=200)


async def list_disputes(request: web.Request, cursor=None, states=None, location_id=None) -> web.Response:
    """ListDisputes

    Returns a list of disputes associated with a particular account.

    :param cursor: A pagination cursor returned by a previous call to this endpoint. Provide this cursor to retrieve the next set of results for the original query. For more information, see [Pagination](https://developer.squareup.com/docs/basics/api101/pagination).
    :type cursor: str
    :param states: The dispute states to filter the result. If not specified, the endpoint returns all open disputes (the dispute status is not &#x60;INQUIRY_CLOSED&#x60;, &#x60;WON&#x60;, or &#x60;LOST&#x60;).
    :type states: str
    :param location_id: The ID of the location for which to return a list of disputes. If not specified, the endpoint returns all open disputes (the dispute status is not &#x60;INQUIRY_CLOSED&#x60;, &#x60;WON&#x60;, or &#x60;LOST&#x60;) associated with all locations.
    :type location_id: str

    """
    return web.Response(status=200)


async def retrieve_dispute(request: web.Request, dispute_id) -> web.Response:
    """RetrieveDispute

    Returns details about a specific dispute.

    :param dispute_id: The ID of the dispute you want more details about.
    :type dispute_id: str

    """
    return web.Response(status=200)


async def retrieve_dispute_evidence(request: web.Request, dispute_id, evidence_id) -> web.Response:
    """RetrieveDisputeEvidence

    Returns the evidence metadata specified by the evidence ID in the request URL path  You must maintain a copy of the evidence you upload if you want to reference it later. You cannot download the evidence after you upload it.

    :param dispute_id: The ID of the dispute that you want to retrieve evidence from.
    :type dispute_id: str
    :param evidence_id: The ID of the evidence to retrieve.
    :type evidence_id: str

    """
    return web.Response(status=200)


async def submit_evidence(request: web.Request, dispute_id) -> web.Response:
    """SubmitEvidence

    Submits evidence to the cardholder&#39;s bank.  Before submitting evidence, Square compiles all available evidence. This includes evidence uploaded using the [CreateDisputeEvidenceFile](https://developer.squareup.com/reference/square_2021-08-18/disputes-api/create-dispute-evidence-file) and [CreateDisputeEvidenceText](https://developer.squareup.com/reference/square_2021-08-18/disputes-api/create-dispute-evidence-text) endpoints and evidence automatically provided by Square, when available.

    :param dispute_id: The ID of the dispute that you want to submit evidence for.
    :type dispute_id: str

    """
    return web.Response(status=200)
