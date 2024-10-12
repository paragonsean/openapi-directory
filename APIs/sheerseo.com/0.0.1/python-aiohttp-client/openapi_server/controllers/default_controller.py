from typing import List, Dict
from aiohttp import web

from openapi_server.models.collect_request import CollectRequest
from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.rank_collect_response import RankCollectResponse
from openapi_server.models.rank_submit_request import RankSubmitRequest
from openapi_server.models.rank_submit_response import RankSubmitResponse
from openapi_server.models.serp_collect_response import SerpCollectResponse
from openapi_server.models.serp_submit_request import SerpSubmitRequest
from openapi_server.models.serp_submit_response import SerpSubmitResponse
from openapi_server import util


async def rank_collect(request: web.Request, body) -> web.Response:
    """rank_collect

    Submit serp jobs

    :param body: The body of the reqest to collect SERPs
    :type body: dict | bytes

    """
    body = CollectRequest.from_dict(body)
    return web.Response(status=200)


async def rank_submit(request: web.Request, body) -> web.Response:
    """rank_submit

    Submit rank jobs

    :param body: The body of the reqest to submit SERPs
    :type body: dict | bytes

    """
    body = RankSubmitRequest.from_dict(body)
    return web.Response(status=200)


async def serp_collect(request: web.Request, body) -> web.Response:
    """serp_collect

    Submit serp jobs

    :param body: The body of the reqest to collect SERPs
    :type body: dict | bytes

    """
    body = CollectRequest.from_dict(body)
    return web.Response(status=200)


async def serp_submit(request: web.Request, body) -> web.Response:
    """serp_submit

    Submit serp jobs

    :param body: The body of the reqest to submit SERPs
    :type body: dict | bytes

    """
    body = SerpSubmitRequest.from_dict(body)
    return web.Response(status=200)
