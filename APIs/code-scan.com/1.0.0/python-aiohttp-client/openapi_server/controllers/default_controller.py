from typing import List, Dict
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.job import Job
from openapi_server.models.new_job import NewJob
from openapi_server import util


async def job_get(request: web.Request, job_id) -> web.Response:
    """Get the status of a job

    Fetches the status of a job

    :param job_id: Id of the Job to retrieve
    :type job_id: str

    """
    return web.Response(status=200)


async def job_post(request: web.Request, job) -> web.Response:
    """Queues a job

    Creates a new job

    :param job: Id of the Job to retrieve
    :type job: dict | bytes

    """
    job = NewJob.from_dict(job)
    return web.Response(status=200)
