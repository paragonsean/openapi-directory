from typing import List, Dict
from aiohttp import web

from openapi_server.models.mapping_job import MappingJob
from openapi_server.models.mapping_job_result import MappingJobResult
from openapi_server.models.mapping_values_key_get200_response import MappingValuesKeyGet200Response
from openapi_server import util


async def mapping_post(request: web.Request, body=None) -> web.Response:
    """mapping_post

    Allows mapping from third-party identifiers to FIGIs.

    :param body: A list of third-party identifiers and extra filters.
    :type body: list | bytes

    """
    body = [MappingJob.from_dict(d) for d in body]
    return web.Response(status=200)


async def mapping_values_key_get(request: web.Request, key) -> web.Response:
    """mapping_values_key_get

    Get values for enum-like fields.

    :param key: Key of MappingJob for which to get possible values.
    :type key: str

    """
    return web.Response(status=200)
