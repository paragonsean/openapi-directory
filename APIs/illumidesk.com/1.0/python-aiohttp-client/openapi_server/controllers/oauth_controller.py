from typing import List, Dict
from aiohttp import web

from openapi_server.models.application import Application
from openapi_server.models.application_data import ApplicationData
from openapi_server.models.application_error import ApplicationError
from openapi_server.models.not_found import NotFound
from openapi_server import util


async def oauth_application_create(request: web.Request, namespace, application_data=None) -> web.Response:
    """Create a new OAuth2 application

    

    :param namespace: User or team name.
    :type namespace: str
    :param application_data: 
    :type application_data: dict | bytes

    """
    application_data = ApplicationData.from_dict(application_data)
    return web.Response(status=200)


async def oauth_application_delete(request: web.Request, namespace, application) -> web.Response:
    """Delete an application by id

    

    :param namespace: User or team name.
    :type namespace: str
    :param application: Application unique identifier expressed as UUID or name.
    :type application: str

    """
    return web.Response(status=200)


async def oauth_application_read(request: web.Request, namespace, application) -> web.Response:
    """Get an application by id

    

    :param namespace: User or team name.
    :type namespace: str
    :param application: Application unique identifier expressed as UUID or name.
    :type application: str

    """
    return web.Response(status=200)


async def oauth_application_replace(request: web.Request, namespace, application, oauth_application_data=None) -> web.Response:
    """Replace an application by id

    

    :param namespace: User or team name.
    :type namespace: str
    :param application: Application unique identifier expressed as UUID or name.
    :type application: str
    :param oauth_application_data: 
    :type oauth_application_data: dict | bytes

    """
    oauth_application_data = ApplicationData.from_dict(oauth_application_data)
    return web.Response(status=200)


async def oauth_application_update(request: web.Request, namespace, application, application_data=None) -> web.Response:
    """Update an application by id

    

    :param namespace: User or team name.
    :type namespace: str
    :param application: Application unique identifier expressed as UUID or name.
    :type application: str
    :param application_data: 
    :type application_data: dict | bytes

    """
    application_data = ApplicationData.from_dict(application_data)
    return web.Response(status=200)


async def oauth_applications_list(request: web.Request, namespace, limit=None, offset=None, ordering=None) -> web.Response:
    """Retrieve oauth applications

    

    :param namespace: User or team name.
    :type namespace: str
    :param limit: Set limit when retrieving items.
    :type limit: str
    :param offset: Offset when retrieving items.
    :type offset: str
    :param ordering: Set order when retrieving items.
    :type ordering: str

    """
    return web.Response(status=200)
