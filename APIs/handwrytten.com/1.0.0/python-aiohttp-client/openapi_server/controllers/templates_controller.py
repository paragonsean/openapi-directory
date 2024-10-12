from typing import List, Dict
from aiohttp import web

from openapi_server.models.change_password200_response import ChangePassword200Response
from openapi_server.models.create_template_request import CreateTemplateRequest
from openapi_server.models.delete_template_request import DeleteTemplateRequest
from openapi_server.models.get_template_categories_authorized_request import GetTemplateCategoriesAuthorizedRequest
from openapi_server.models.get_template_detail_request import GetTemplateDetailRequest
from openapi_server.models.get_templatess_authorized_request import GetTemplatessAuthorizedRequest
from openapi_server.models.template import Template
from openapi_server.models.template_category import TemplateCategory
from openapi_server.models.update_template_request import UpdateTemplateRequest
from openapi_server import util


async def create_template(request: web.Request, body) -> web.Response:
    """Creates a New Template in the User’s Account

    Creates a new Template in the User’s Account

    :param body: additional parameters
    :type body: dict | bytes

    """
    body = CreateTemplateRequest.from_dict(body)
    return web.Response(status=200)


async def delete_template(request: web.Request, body) -> web.Response:
    """Deletes a users template

    Deletes a template in the User’s Account

    :param body: additional parameters
    :type body: dict | bytes

    """
    body = DeleteTemplateRequest.from_dict(body)
    return web.Response(status=200)


async def get_template_categories(request: web.Request, ) -> web.Response:
    """List template categories

    Lists the common template categories of all users. As you are not logged in, this is what you are limited to.


    """
    return web.Response(status=200)


async def get_template_categories_authorized(request: web.Request, body=None) -> web.Response:
    """List template categories

    Lists the template categories of all users. By passing the optional UID, any custom template categories are also available.

    :param body: additional parameters
    :type body: dict | bytes

    """
    body = GetTemplateCategoriesAuthorizedRequest.from_dict(body)
    return web.Response(status=200)


async def get_template_detail(request: web.Request, body) -> web.Response:
    """Get all info on a template

    Provides all details on a template

    :param body: additional parameters
    :type body: dict | bytes

    """
    body = GetTemplateDetailRequest.from_dict(body)
    return web.Response(status=200)


async def get_templates(request: web.Request, ) -> web.Response:
    """List template categories

    Lists the common template categories of all users. As you are not logged in, this is what you are limited to.


    """
    return web.Response(status=200)


async def get_templatess_authorized(request: web.Request, body=None) -> web.Response:
    """List template categories

    Lists the template categories of all users. By passing the optional UID, any custom template categories are also available.

    :param body: additional parameters
    :type body: dict | bytes

    """
    body = GetTemplatessAuthorizedRequest.from_dict(body)
    return web.Response(status=200)


async def update_template(request: web.Request, body) -> web.Response:
    """Updates an Existing Template in the User’s Account

    Updates an Existing Template in the User’s Account

    :param body: additional parameters
    :type body: dict | bytes

    """
    body = UpdateTemplateRequest.from_dict(body)
    return web.Response(status=200)
