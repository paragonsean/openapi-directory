from typing import List, Dict
from aiohttp import web

from openapi_server.models.counter import Counter
from openapi_server.models.import_job import ImportJob
from openapi_server import util


async def activate_import_job(request: web.Request, id) -> web.Response:
    """Activate an ImportJob

    Make an ImportJob active, so that it is executed

    :param id: Unique identifier of ImportJob to manage
    :type id: str

    """
    return web.Response(status=200)


async def create_import_job(request: web.Request, body) -> web.Response:
    """Create ImportJob

    Create a new ImportJob

    :param body: 
    :type body: dict | bytes

    """
    body = ImportJob.from_dict(body)
    return web.Response(status=200)


async def delete_import_job(request: web.Request, id) -> web.Response:
    """Delete ImportJob

    Delete an ImportJob

    :param id: Unique identifier of ImportJob to manage
    :type id: str

    """
    return web.Response(status=200)


async def get_import_job_counter(request: web.Request, ) -> web.Response:
    """Get the ImportJobs counter

    


    """
    return web.Response(status=200)


async def get_import_jobs(request: web.Request, page=None, size=None, name=None) -> web.Response:
    """Get ImportJobs

    Retrieve a list of ImportJobs

    :param page: Page of ImportJobs to retrieve (starts at and defaults to 0)
    :type page: int
    :param size: Size of a page. Maximum number of ImportJobs to include in a response (defaults to 20)
    :type size: int
    :param name: Name like criterion for query
    :type name: str

    """
    return web.Response(status=200)


async def jobs_id_get(request: web.Request, id) -> web.Response:
    """Get ImportJob

    Retrieve an ImportJob using its identifier

    :param id: Unique identifier of ImportJob to manage
    :type id: str

    """
    return web.Response(status=200)


async def jobs_id_post(request: web.Request, id, body) -> web.Response:
    """Update ImportJob

    Update an ImportJob

    :param id: Unique identifier of ImportJob to manage
    :type id: str
    :param body: 
    :type body: dict | bytes

    """
    body = ImportJob.from_dict(body)
    return web.Response(status=200)


async def start_import_job(request: web.Request, id) -> web.Response:
    """Start an ImportJob

    Starting an ImportJob forces it to immediatly import mock definitions

    :param id: Unique identifier of ImportJob to manage
    :type id: str

    """
    return web.Response(status=200)


async def stop_import_job(request: web.Request, id) -> web.Response:
    """Stop an ImportJob

    Stopping an ImportJob desactivate it, so that it won&#39;t execute at next schedule

    :param id: Unique identifier of ImportJob to manage
    :type id: str

    """
    return web.Response(status=200)


async def upload_artifact(request: web.Request, main_artifact, file) -> web.Response:
    """Upload an artifact

    Uploads an artifact to be imported by Microcks.

    :param main_artifact: Flag telling if this should be considered as primary or secondary artifact. Default to &#39;true&#39;
    :type main_artifact: bool
    :param file: The artifact to upload
    :type file: str

    """
    return web.Response(status=200)
