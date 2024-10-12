from typing import List, Dict
from aiohttp import web

from openapi_server.models.document_submission import DocumentSubmission
from openapi_server.models.document_submission_evidence import DocumentSubmissionEvidence
from openapi_server.models.document_submission_result import DocumentSubmissionResult
from openapi_server.models.error_model import ErrorModel
from openapi_server import util


async def create_document_submission(request: web.Request, body) -> web.Response:
    """Submit a new document.

    Submit a document for delivery. This endpoint will replaces the /invoice_submissions endpoint which will soon be deprecated.

    :param body: Document to submit
    :type body: dict | bytes

    """
    body = DocumentSubmission.from_dict(body)
    return web.Response(status=200)


async def show_document_submission_evidence(request: web.Request, guid, evidence_type) -> web.Response:
    """Get DocumentSubmission Evidence

    Get evidence for a DocumentSubmission by GUID with corresponding status

    :param guid: DocumentSubmission GUID
    :type guid: str
    :type guid: str
    :param evidence_type: Type of evidence requested
    :type evidence_type: str

    """
    return web.Response(status=200)
