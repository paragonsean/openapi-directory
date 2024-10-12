from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_model import ErrorModel
from openapi_server.models.invoice_recipient_preflight import InvoiceRecipientPreflight
from openapi_server.models.invoice_submission import InvoiceSubmission
from openapi_server.models.invoice_submission_evidence import InvoiceSubmissionEvidence
from openapi_server.models.invoice_submission_result import InvoiceSubmissionResult
from openapi_server.models.preflight_invoice_recipient_result import PreflightInvoiceRecipientResult
from openapi_server import util


async def create_invoice_submission(request: web.Request, body) -> web.Response:
    """Submit a new invoice

    DEPRECATED. Use the new /document_submissions endpoint. Submit an invoice for delivery.

    :param body: Invoice to submit
    :type body: dict | bytes

    """
    body = InvoiceSubmission.from_dict(body)
    return web.Response(status=200)


async def preflight_invoice_recipient(request: web.Request, body) -> web.Response:
    """DEPRECATED. Preflight an invoice recipient

    Deprecated. Use the new /discovery endpoint. Check whether Storecove can deliver an invoice for a list of ids.

    :param body: The invoice recipient to preflight
    :type body: dict | bytes

    """
    body = InvoiceRecipientPreflight.from_dict(body)
    return web.Response(status=200)


async def show_invoice_submission_evidence(request: web.Request, guid) -> web.Response:
    """DEPRECATED. Get InvoiceSubmission Evidence

    Deprecated. Use the new /document_submissions/{guid}/evidence endpoint. Get evidence for an InvoiceSubmission by GUID with corresponding status

    :param guid: InvoiceSubmission GUID
    :type guid: str
    :type guid: str

    """
    return web.Response(status=200)
