from typing import List, Dict
from aiohttp import web

from openapi_server.models.find_form_by_form_name200_response import FindFormByFormName200Response
from openapi_server.models.find_form_by_form_name404_response import FindFormByFormName404Response
from openapi_server.models.find_forms200_response import FindForms200Response
from openapi_server.models.find_forms401_response import FindForms401Response
from openapi_server.models.find_forms429_response import FindForms429Response
from openapi_server import util


async def find_form_by_form_name(request: web.Request, form_name) -> web.Response:
    """Find form by form name

    Returns a single form and the full revision history

    :param form_name: The VA form_name of the form being requested. The exact form name must be passed, including proper placement of prefixes and/or hyphens.
    :type form_name: str

    """
    return web.Response(status=200)


async def find_forms(request: web.Request, query=None) -> web.Response:
    """Returns all VA Forms and their last revision date

    Returns an index of all available VA forms. Optionally, pass a query parameter to filter forms by form number or title.

    :param query: Returns form data based on entered form name.
    :type query: str

    """
    return web.Response(status=200)
