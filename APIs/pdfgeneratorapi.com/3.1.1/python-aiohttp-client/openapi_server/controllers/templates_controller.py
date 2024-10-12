from typing import List, Dict
from aiohttp import web

from openapi_server.models.create_template200_response import CreateTemplate200Response
from openapi_server.models.delete_template200_response import DeleteTemplate200Response
from openapi_server.models.get_editor_url200_response import GetEditorUrl200Response
from openapi_server.models.get_templates200_response import GetTemplates200Response
from openapi_server.models.get_templates401_response import GetTemplates401Response
from openapi_server.models.get_templates403_response import GetTemplates403Response
from openapi_server.models.get_templates404_response import GetTemplates404Response
from openapi_server.models.get_templates422_response import GetTemplates422Response
from openapi_server.models.get_templates500_response import GetTemplates500Response
from openapi_server.models.template_definition_new import TemplateDefinitionNew
from openapi_server import util


async def copy_template(request: web.Request, template_id, name=None) -> web.Response:
    """Copy template

    Creates a copy of a template to the workspace specified in authentication parameters.

    :param template_id: Template unique identifier
    :type template_id: int
    :param name: Name for the copied template. If name is not specified then the original name is used.
    :type name: str

    """
    return web.Response(status=200)


async def create_template(request: web.Request, body) -> web.Response:
    """Create template

    Creates a new template. If template configuration is not specified in the request body then an empty template is created. Template is placed to the workspace specified in authentication params. Template configuration must be sent in the request body.

    :param body: Template configuration as JSON string
    :type body: dict | bytes

    """
    body = TemplateDefinitionNew.from_dict(body)
    return web.Response(status=200)


async def delete_template(request: web.Request, template_id) -> web.Response:
    """Delete template

    Deletes the template from workspace

    :param template_id: Template unique identifier
    :type template_id: int

    """
    return web.Response(status=200)


async def get_editor_url(request: web.Request, template_id, body, language=None) -> web.Response:
    """Open editor

    Returns an unique URL which you can use to redirect your user to the editor from your application or use the generated URL as iframe source to show the editor within your application. 

    :param template_id: Template unique identifier
    :type template_id: int
    :param body: Data used to generate the PDF. This can be JSON encoded string or a public URL to your JSON file.
    :type body: 
    :param language: Specify the editor UI language. Defaults to organization editor language.
    :type language: str

    """
    return web.Response(status=200)


async def get_template(request: web.Request, template_id) -> web.Response:
    """Get template

    Returns template configuration

    :param template_id: Template unique identifier
    :type template_id: int

    """
    return web.Response(status=200)


async def get_templates(request: web.Request, ) -> web.Response:
    """Get templates

    Returns a list of templates available for the authenticated workspace


    """
    return web.Response(status=200)


async def update_template(request: web.Request, template_id, body) -> web.Response:
    """Update template

    Updates template configuration. The template configuration for pages and layout must be complete as the entire configuration is replaced and not merged.

    :param template_id: Template unique identifier
    :type template_id: int
    :param body: Template configuration as JSON string
    :type body: dict | bytes

    """
    body = TemplateDefinitionNew.from_dict(body)
    return web.Response(status=200)
