from typing import List, Dict
from aiohttp import web

from openapi_server.models.csr_summary import CsrSummary
from openapi_server.models.csr_summary_list_response import CsrSummaryListResponse
from openapi_server.models.generic_csr_request import GenericCsrRequest
from openapi_server import util


async def delete_csr(request: web.Request, id) -> web.Response:
    """Delete a certificate signing request

    Deletes a certificate signing request corresponding to the provided ID.

    :param id: Certificate signing request ID.
    :type id: str

    """
    return web.Response(status=200)


async def generate_csr(request: web.Request, body) -> web.Response:
    """Generate a new private key and return a certificate signing request

    Generates a new private key and returns a base64 encoded PKCS#10 certificate signing request (CSR).

    :param body: Information for client certificate request.
    :type body: dict | bytes

    """
    body = GenericCsrRequest.from_dict(body)
    return web.Response(status=200)


async def get_all_csrs(request: web.Request, ) -> web.Response:
    """Get all certificate signing requests

    Returns a list of summaries for every outstanding certificate signing request (CSR).


    """
    return web.Response(status=200)
