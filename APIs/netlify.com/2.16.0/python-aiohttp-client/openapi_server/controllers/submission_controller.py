from typing import List, Dict
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.submission import Submission
from openapi_server import util


async def delete_submission(request: web.Request, submission_id) -> web.Response:
    """delete_submission

    

    :param submission_id: 
    :type submission_id: str

    """
    return web.Response(status=200)


async def list_form_submission(request: web.Request, submission_id, query=None, page=None, per_page=None) -> web.Response:
    """list_form_submission

    

    :param submission_id: 
    :type submission_id: str
    :param query: 
    :type query: str
    :param page: 
    :type page: int
    :param per_page: 
    :type per_page: int

    """
    return web.Response(status=200)


async def list_form_submissions(request: web.Request, form_id, page=None, per_page=None) -> web.Response:
    """list_form_submissions

    

    :param form_id: 
    :type form_id: str
    :param page: 
    :type page: int
    :param per_page: 
    :type per_page: int

    """
    return web.Response(status=200)


async def list_site_submissions(request: web.Request, site_id, page=None, per_page=None) -> web.Response:
    """list_site_submissions

    

    :param site_id: 
    :type site_id: str
    :param page: 
    :type page: int
    :param per_page: 
    :type per_page: int

    """
    return web.Response(status=200)
