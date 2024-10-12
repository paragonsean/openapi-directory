from typing import List, Dict
from aiohttp import web

from openapi_server.models.term import Term
from openapi_server import util


async def get_ont_dags_using_get(request: web.Request, acc_id) -> web.Response:
    """Returns child and parent terms for Accession ID

    

    :param acc_id: Accession ID
    :type acc_id: str

    """
    return web.Response(status=200)


async def get_term_using_get(request: web.Request, acc_id) -> web.Response:
    """Returns term for Accession ID

    

    :param acc_id: Term Accession ID
    :type acc_id: str

    """
    return web.Response(status=200)


async def is_descendant_of_using_get(request: web.Request, acc_id1, acc_id2) -> web.Response:
    """Returns true or false for terms

    

    :param acc_id1: Child Term Accession ID
    :type acc_id1: str
    :param acc_id2: Parent Term Accession ID
    :type acc_id2: str

    """
    return web.Response(status=200)
