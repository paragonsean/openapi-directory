from typing import List, Dict
from aiohttp import web

from openapi_server.models.admin_create_corpus_request import AdminCreateCorpusRequest
from openapi_server.models.admin_create_corpus_response import AdminCreateCorpusResponse
from openapi_server.models.admin_delete_corpus_request import AdminDeleteCorpusRequest
from openapi_server.models.admin_delete_corpus_response import AdminDeleteCorpusResponse
from openapi_server.models.admin_list_corpora_request import AdminListCorporaRequest
from openapi_server.models.admin_list_corpora_response import AdminListCorporaResponse
from openapi_server.models.admin_reset_corpus_request import AdminResetCorpusRequest
from openapi_server.models.admin_reset_corpus_response import AdminResetCorpusResponse
from openapi_server.models.googlerpc_status import GooglerpcStatus
from openapi_server import util


async def create_corpus(request: web.Request, customer_id, body) -> web.Response:
    """create_corpus

    Create Corpus

    :param customer_id: The Customer ID to use for the request.
    :type customer_id: int
    :param body: 
    :type body: dict | bytes

    """
    body = AdminCreateCorpusRequest.from_dict(body)
    return web.Response(status=200)


async def delete_corpus(request: web.Request, customer_id, body) -> web.Response:
    """delete_corpus

    Delete Corpus

    :param customer_id: The Customer ID to use for the request.
    :type customer_id: int
    :param body: 
    :type body: dict | bytes

    """
    body = AdminDeleteCorpusRequest.from_dict(body)
    return web.Response(status=200)


async def list_corpora(request: web.Request, customer_id, body) -> web.Response:
    """list_corpora

    List Corpora

    :param customer_id: The Customer ID to use for the request.
    :type customer_id: int
    :param body: 
    :type body: dict | bytes

    """
    body = AdminListCorporaRequest.from_dict(body)
    return web.Response(status=200)


async def reset_corpus(request: web.Request, customer_id, body) -> web.Response:
    """reset_corpus

    Reset Corpus

    :param customer_id: The Customer ID to use for the request.
    :type customer_id: int
    :param body: 
    :type body: dict | bytes

    """
    body = AdminResetCorpusRequest.from_dict(body)
    return web.Response(status=200)
