from typing import List, Dict
from aiohttp import web

from openapi_server.models.app_patch import AppPatch
from openapi_server.models.app_post import AppPost
from openapi_server.models.app_response import AppResponse
from openapi_server.models.error import Error
from openapi_server import util


async def accounts_account_id_apps_get(request: web.Request, account_id) -> web.Response:
    """Lists apps

    List all applications for the specified account ID.

    :param account_id: The account ID for which to retrieve the associated applications.
    :type account_id: str

    """
    return web.Response(status=200)


async def accounts_account_id_apps_post(request: web.Request, account_id, body=None) -> web.Response:
    """Creates an app

    Creates an application with the specified properties.

    :param account_id: The account ID of the account in which to create the application.
    :type account_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = AppPost.from_dict(body)
    return web.Response(status=200)


async def apps_id_delete(request: web.Request, id) -> web.Response:
    """Deletes an app

    Deletes the application with the specified application ID.

    :param id: The ID of the application to be deleted.
    :type id: str

    """
    return web.Response(status=200)


async def apps_id_patch(request: web.Request, id, body=None) -> web.Response:
    """Updates an app

    Updates the application with the specified application ID.

    :param id: The ID of application to be updated.
    :type id: str
    :param body: 
    :type body: dict | bytes

    """
    body = AppPatch.from_dict(body)
    return web.Response(status=200)


async def apps_id_pkcs12_post(request: web.Request, id, p12_file, p12_pass) -> web.Response:
    """Updates app&#39;s APNs info from a &#x60;.p12&#x60; file

    Updates the application&#39;s Apple Push Notification service (APNs) information.

    :param id: The application ID.
    :type id: str
    :param p12_file: The &#x60;.p12&#x60; file containing the app&#39;s APNs information.
    :type p12_file: str
    :param p12_pass: The password for the corresponding &#x60;.p12&#x60; file.
    :type p12_pass: str

    """
    return web.Response(status=200)
