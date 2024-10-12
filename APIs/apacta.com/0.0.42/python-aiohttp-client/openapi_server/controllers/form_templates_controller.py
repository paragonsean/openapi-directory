from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_not_found import ErrorNotFound
from openapi_server.models.form_templates_form_template_id_get200_response import FormTemplatesFormTemplateIdGet200Response
from openapi_server.models.form_templates_get200_response import FormTemplatesGet200Response
from openapi_server import util


async def form_templates_form_template_id_get(request: web.Request, form_template_id) -> web.Response:
    """View one form template

    

    :param form_template_id: 
    :type form_template_id: str

    """
    return web.Response(status=200)


async def form_templates_get(request: web.Request, name=None, identifier=None, pdf_template_identifier=None, description=None) -> web.Response:
    """Get array of form_templates for your company

    

    :param name: Used to filter on the &#x60;name&#x60; of the form_templates
    :type name: str
    :param identifier: Used to filter on the &#x60;identifier&#x60; of the form_templates
    :type identifier: str
    :param pdf_template_identifier: Used to filter on the &#x60;pdf_template_identifier&#x60; of the form_templates
    :type pdf_template_identifier: str
    :param description: Used to filter on the &#x60;description&#x60; of the form_templates
    :type description: str

    """
    return web.Response(status=200)
