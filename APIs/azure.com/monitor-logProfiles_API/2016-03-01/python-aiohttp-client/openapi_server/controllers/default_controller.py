from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.log_profile_resource import LogProfileResource
from openapi_server.models.log_profile_resource_patch import LogProfileResourcePatch
from openapi_server import util


async def log_profiles_update(request: web.Request, subscription_id, log_profile_name, api_version, log_profiles_resource) -> web.Response:
    """log_profiles_update

    Updates an existing LogProfilesResource. To update other fields use the CreateOrUpdate method.

    :param subscription_id: The Azure subscription Id.
    :type subscription_id: str
    :param log_profile_name: The name of the log profile.
    :type log_profile_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param log_profiles_resource: Parameters supplied to the operation.
    :type log_profiles_resource: dict | bytes

    """
    log_profiles_resource = LogProfileResourcePatch.from_dict(log_profiles_resource)
    return web.Response(status=200)
