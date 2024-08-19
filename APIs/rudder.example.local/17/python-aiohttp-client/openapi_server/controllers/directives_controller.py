from typing import List, Dict
from aiohttp import web

from openapi_server.models.check_directive200_response import CheckDirective200Response
from openapi_server.models.create_directive200_response import CreateDirective200Response
from openapi_server.models.delete_directive200_response import DeleteDirective200Response
from openapi_server.models.directive import Directive
from openapi_server.models.directive_details200_response import DirectiveDetails200Response
from openapi_server.models.directive_new import DirectiveNew
from openapi_server.models.list_directives200_response import ListDirectives200Response
from openapi_server.models.update_directive200_response import UpdateDirective200Response
from openapi_server import util


async def check_directive(request: web.Request, directive_id, body) -> web.Response:
    """Check that update on a directive is valid

    Check that update on a directive is valid

    :param directive_id: Id of the directive
    :type directive_id: str
    :type directive_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = Directive.from_dict(body)
    return web.Response(status=200)


async def create_directive(request: web.Request, body=None) -> web.Response:
    """Create a directive

    Create a new directive from provided parameters. You can specify a source directive to clone it.

    :param body: 
    :type body: dict | bytes

    """
    body = DirectiveNew.from_dict(body)
    return web.Response(status=200)


async def delete_directive(request: web.Request, directive_id) -> web.Response:
    """Delete a directive

    Delete a directive

    :param directive_id: Id of the directive
    :type directive_id: str
    :type directive_id: str

    """
    return web.Response(status=200)


async def directive_details(request: web.Request, directive_id) -> web.Response:
    """Get directive details

    Get all information about a given directive

    :param directive_id: Id of the directive
    :type directive_id: str
    :type directive_id: str

    """
    return web.Response(status=200)


async def list_directives(request: web.Request, ) -> web.Response:
    """List all directives

    List all directives


    """
    return web.Response(status=200)


async def update_directive(request: web.Request, directive_id, body) -> web.Response:
    """Update a directive details

    Update directive information

    :param directive_id: Id of the directive
    :type directive_id: str
    :type directive_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = Directive.from_dict(body)
    return web.Response(status=200)
