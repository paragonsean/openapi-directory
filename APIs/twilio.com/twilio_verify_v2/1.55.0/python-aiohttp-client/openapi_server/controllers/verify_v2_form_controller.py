from typing import List, Dict
from aiohttp import web

from openapi_server.models.form_enum_form_types import FormEnumFormTypes
from openapi_server.models.verify_v2_form import VerifyV2Form
from openapi_server import util


async def fetch_form(request: web.Request, form_type) -> web.Response:
    """fetch_form

    Fetch the forms for a specific Form Type.

    :param form_type: The Type of this Form. Currently only &#x60;form-push&#x60; is supported.
    :type form_type: str

    """
    return web.Response(status=200)
