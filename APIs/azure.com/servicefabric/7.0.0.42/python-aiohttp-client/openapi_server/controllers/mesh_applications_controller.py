from typing import List, Dict
from aiohttp import web

from openapi_server.models.application_resource_description import ApplicationResourceDescription
from openapi_server.models.application_resource_upgrade_progress_info import ApplicationResourceUpgradeProgressInfo
from openapi_server.models.fabric_error import FabricError
from openapi_server.models.paged_application_resource_description_list import PagedApplicationResourceDescriptionList
from openapi_server import util


async def mesh_application_create_or_update(request: web.Request, api_version, application_resource_name, application_resource_description) -> web.Response:
    """Creates or updates a Application resource.

    Creates a Application resource with the specified name, description and properties. If Application resource with the same name exists, then it is updated with the specified description and properties.

    :param api_version: The version of the API. This parameter is required and its value must be &#39;6.4-preview&#39;.
    :type api_version: str
    :param application_resource_name: The identity of the application.
    :type application_resource_name: str
    :param application_resource_description: Description for creating a Application resource.
    :type application_resource_description: dict | bytes

    """
    application_resource_description = ApplicationResourceDescription.from_dict(application_resource_description)
    return web.Response(status=200)


async def mesh_application_delete(request: web.Request, api_version, application_resource_name) -> web.Response:
    """Deletes the Application resource.

    Deletes the Application resource identified by the name.

    :param api_version: The version of the API. This parameter is required and its value must be &#39;6.4-preview&#39;.
    :type api_version: str
    :param application_resource_name: The identity of the application.
    :type application_resource_name: str

    """
    return web.Response(status=200)


async def mesh_application_get(request: web.Request, api_version, application_resource_name) -> web.Response:
    """Gets the Application resource with the given name.

    Gets the information about the Application resource with the given name. The information include the description and other properties of the Application.

    :param api_version: The version of the API. This parameter is required and its value must be &#39;6.4-preview&#39;.
    :type api_version: str
    :param application_resource_name: The identity of the application.
    :type application_resource_name: str

    """
    return web.Response(status=200)


async def mesh_application_get_upgrade_progress(request: web.Request, api_version, application_resource_name) -> web.Response:
    """Gets the progress of the latest upgrade performed on this application resource.

    Gets the upgrade progress information about the Application resource with the given name. The information include percentage of completion and other upgrade state information of the Application resource.

    :param api_version: The version of the API. This parameter is required and its value must be &#39;7.0&#39;.  Service Fabric REST API version is based on the runtime version in which the API was introduced or was changed. Service Fabric runtime supports more than one version of the API. This version is the latest supported version of the API. If a lower API version is passed, the returned response may be different from the one documented in this specification.  Additionally the runtime accepts any version that is higher than the latest supported version up to the current version of the runtime. So if the latest API version is 6.0 and the runtime is 6.1, the runtime will accept version 6.1 for that API. However the behavior of the API will be as per the documented 6.0 version.
    :type api_version: str
    :param application_resource_name: The identity of the application.
    :type application_resource_name: str

    """
    return web.Response(status=200)


async def mesh_application_list(request: web.Request, api_version) -> web.Response:
    """Lists all the application resources.

    Gets the information about all application resources in a given resource group. The information include the description and other properties of the Application.

    :param api_version: The version of the API. This parameter is required and its value must be &#39;6.4-preview&#39;.
    :type api_version: str

    """
    return web.Response(status=200)
