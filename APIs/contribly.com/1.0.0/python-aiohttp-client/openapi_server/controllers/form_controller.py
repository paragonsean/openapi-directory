from typing import List, Dict
from aiohttp import web

from openapi_server.models.form import Form
from openapi_server.models.form_response import FormResponse
from openapi_server.models.form_response_submission import FormResponseSubmission
from openapi_server.models.form_submission import FormSubmission
from openapi_server import util


async def form_responses_get(request: web.Request, user=None, form=None, contribution=None) -> web.Response:
    """List form responses

    

    :param user: Restrict results to responses submitted by this user.
    :type user: str
    :param form: Restrict results to responses submitted to this form.
    :type form: str
    :param contribution: Restrict results to responses relating to this contribution.
    :type contribution: str

    """
    return web.Response(status=200)


async def form_responses_id_get(request: web.Request, id) -> web.Response:
    """Get a single form response by id

    

    :param id: Id of the assignment to return
    :type id: str

    """
    return web.Response(status=200)


async def form_responses_post(request: web.Request, body) -> web.Response:
    """Submit a response to a form

    

    :param body: Form response
    :type body: dict | bytes

    """
    body = FormResponseSubmission.from_dict(body)
    return web.Response(status=200)


async def forms_get(request: web.Request, owned_by) -> web.Response:
    """List forms

    

    :param owned_by: Restrict results to forms owned by this user.
    :type owned_by: str

    """
    return web.Response(status=200)


async def forms_id_delete(request: web.Request, id) -> web.Response:
    """Delete this form and all of it&#39;s responses.

    

    :param id: Id of the form to delete
    :type id: str

    """
    return web.Response(status=200)


async def forms_id_get(request: web.Request, id) -> web.Response:
    """Get a single form by id

    

    :param id: Id of the form to return
    :type id: str

    """
    return web.Response(status=200)


async def forms_post(request: web.Request, body) -> web.Response:
    """Create a form

    

    :param body: Form object to be created
    :type body: dict | bytes

    """
    body = FormSubmission.from_dict(body)
    return web.Response(status=200)
