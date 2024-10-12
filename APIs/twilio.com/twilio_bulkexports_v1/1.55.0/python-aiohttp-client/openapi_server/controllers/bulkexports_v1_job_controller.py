from typing import List, Dict
from aiohttp import web

from openapi_server.models.bulkexports_v1_export_job import BulkexportsV1ExportJob
from openapi_server import util


async def delete_job(request: web.Request, job_sid) -> web.Response:
    """delete_job

    

    :param job_sid: The unique string that that we created to identify the Bulk Export job
    :type job_sid: str

    """
    return web.Response(status=200)


async def fetch_job(request: web.Request, job_sid) -> web.Response:
    """fetch_job

    

    :param job_sid: The unique string that that we created to identify the Bulk Export job
    :type job_sid: str

    """
    return web.Response(status=200)
