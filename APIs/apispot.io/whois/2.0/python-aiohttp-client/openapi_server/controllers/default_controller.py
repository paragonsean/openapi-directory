from typing import List, Dict
from aiohttp import web

from openapi_server.models.array_of_batch import ArrayOfBatch
from openapi_server.models.batch import Batch
from openapi_server.models.check_domain200_response import CheckDomain200Response
from openapi_server.models.create_batch_request import CreateBatchRequest
from openapi_server.models.domain_rank200_response import DomainRank200Response
from openapi_server import util


async def check_domain(request: web.Request, domain) -> web.Response:
    """check_domain

    Check domain availability

    :param domain: Domain
    :type domain: str

    """
    return web.Response(status=200)


async def create_batch(request: web.Request, body) -> web.Response:
    """create_batch

    Create batch. Batch is then being processed until all provided items have been completed. At any time it can be &#x60;get&#x60; to provide current status with results optionally.

    :param body: 
    :type body: dict | bytes

    """
    body = CreateBatchRequest.from_dict(body)
    return web.Response(status=200)


async def delete_batch(request: web.Request, id) -> web.Response:
    """delete_batch

    Delete batch

    :param id: Batch ID
    :type id: str

    """
    return web.Response(status=200)


async def domain_rank(request: web.Request, domain) -> web.Response:
    """domain_rank

    Check domain rank (authority).

    :param domain: Domain
    :type domain: str

    """
    return web.Response(status=200)


async def get_batch(request: web.Request, id) -> web.Response:
    """get_batch

    Get batch

    :param id: Batch ID
    :type id: str

    """
    return web.Response(status=200)


async def get_batches(request: web.Request, ) -> web.Response:
    """get_batches

    Get your batches


    """
    return web.Response(status=200)


async def query_db(request: web.Request, query) -> web.Response:
    """query_db

    Query domain database

    :param query: Query (contact name, dns, domain etc)
    :type query: str

    """
    return web.Response(status=200)


async def whois(request: web.Request, domain, format=None) -> web.Response:
    """whois

    WHOIS query for a domain

    :param domain: Domain
    :type domain: str
    :param format: 
    :type format: str

    """
    return web.Response(status=200)
