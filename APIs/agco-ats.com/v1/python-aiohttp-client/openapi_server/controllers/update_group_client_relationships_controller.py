from typing import List, Dict
from aiohttp import web

from openapi_server.models.api_models_api_error import APIModelsApiError
from openapi_server.models.api_paged_response_update_system_models_update_group_client_relationship import APIPagedResponseUpdateSystemModelsUpdateGroupClientRelationship
from openapi_server.models.update_system_models_update_group_client_relationship import UpdateSystemModelsUpdateGroupClientRelationship
from openapi_server import util


async def update_group_client_relationships_get_subscription(request: web.Request, relationship_id) -> web.Response:
    """Get a subscription by RelationshipID

    No Documentation Found.

    :param relationship_id: The RelationshipID.
    :type relationship_id: str

    """
    return web.Response(status=200)


async def update_group_client_relationships_get_subscriptions(request: web.Request, client_id=None, update_group_id=None, limit=None, offset=None, active=None) -> web.Response:
    """Get a list of current Client Subscriptions.

    No Documentation Found.

    :param client_id: Optional. Filter by Client ID
    :type client_id: str
    :param update_group_id: Optional. Filter by Update Group ID
    :type update_group_id: str
    :param limit: Optional. The page limit. The default page limit is 10.
    :type limit: int
    :param offset: Optional. The page offset. The default page offset is 0.
    :type offset: int
    :param active: Optional. Filter by Active
    :type active: bool

    """
    return web.Response(status=200)


async def update_group_client_relationships_post_subscription(request: web.Request, body) -> web.Response:
    """Add a subscription

    No Documentation Found.

    :param body: The UpdateGroupClientRelationship to add.
    :type body: dict | bytes

    """
    body = UpdateSystemModelsUpdateGroupClientRelationship.from_dict(body)
    return web.Response(status=200)


async def update_group_client_relationships_put_subscription(request: web.Request, relationship_id, body) -> web.Response:
    """Updates a Subscription

    No Documentation Found.

    :param relationship_id: The relationship id of the UpdateGroupClientRelationship
    :type relationship_id: str
    :param body: The updated UpdateGroupClientRelationship
    :type body: dict | bytes

    """
    body = UpdateSystemModelsUpdateGroupClientRelationship.from_dict(body)
    return web.Response(status=200)


async def update_group_client_relationships_put_subscription_by_client_id_update_group_id(request: web.Request, client_id, update_group_id, active) -> web.Response:
    """DEPRECATED. Set client subscription status for an update group.

    No Documentation Found.

    :param client_id: The Client ID.  This can be a client ID that has not been registered yet.
    :type client_id: str
    :param update_group_id: The Update Group ID
    :type update_group_id: str
    :param active: Subscribe the client to the Update Group.
    :type active: bool

    """
    return web.Response(status=200)
