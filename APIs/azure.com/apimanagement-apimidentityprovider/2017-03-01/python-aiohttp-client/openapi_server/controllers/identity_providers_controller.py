from typing import List, Dict
from aiohttp import web

from openapi_server.models.identity_provider_list_by_service_default_response import IdentityProviderListByServiceDefaultResponse
from openapi_server.models.identity_provider_update_parameters import IdentityProviderUpdateParameters
from openapi_server import util


async def identity_provider_update(request: web.Request, resource_group_name, service_name, identity_provider_name, if_match, api_version, subscription_id, parameters) -> web.Response:
    """identity_provider_update

    Updates an existing IdentityProvider configuration.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param service_name: The name of the API Management service.
    :type service_name: str
    :param identity_provider_name: Identity Provider Type identifier.
    :type identity_provider_name: str
    :param if_match: The entity state (Etag) version of the identity provider configuration to update. A value of \&quot;*\&quot; can be used for If-Match to unconditionally apply the operation.
    :type if_match: str
    :param api_version: Version of the API to be used with the client request.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param parameters: Update parameters.
    :type parameters: dict | bytes

    """
    parameters = IdentityProviderUpdateParameters.from_dict(parameters)
    return web.Response(status=200)
