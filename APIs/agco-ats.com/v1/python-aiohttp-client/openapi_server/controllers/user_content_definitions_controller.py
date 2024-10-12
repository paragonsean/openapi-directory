from typing import List, Dict
from aiohttp import web

from openapi_server.models.api_models_api_error import APIModelsApiError
from openapi_server.models.api_paged_response_content_submission_shared_business_entities_user_content_definition import APIPagedResponseContentSubmissionSharedBusinessEntitiesUserContentDefinition
from openapi_server.models.content_submission_shared_business_entities_user_content_definition import ContentSubmissionSharedBusinessEntitiesUserContentDefinition
from openapi_server import util


async def user_content_definitions_delete_user_content_definition(request: web.Request, user_content_definition_id) -> web.Response:
    """Delete a UserContentDefinition

    Deletes an UserContentDefinition. When successful, the response is empty.  If unsuccessful, an appropriate              ApiError is returned.

    :param user_content_definition_id: The ID of the UserContentDefinition to delete
    :type user_content_definition_id: int

    """
    return web.Response(status=200)


async def user_content_definitions_get_user_content_definition(request: web.Request, user_content_definition_id) -> web.Response:
    """Get a UserContentDefinition by ID

    Gets a UserContentDefinition by ID. When successful, the response is the requested UserContentDefinition.              If unsuccessful, an appropriate ApiError is returned.

    :param user_content_definition_id: The ID of the UserContentDefinition to get.
    :type user_content_definition_id: int

    """
    return web.Response(status=200)


async def user_content_definitions_get_user_content_definitions(request: web.Request, limit=None, offset=None, user_id=None, content_definition_id=None) -> web.Response:
    """Get UserContentDefinitions

    Gets a collection of UserContentDefinitions. When successful, the response is a PagedResponse of UserContentDefinitions.              If unsuccessful, an appropriate ApiError is returned.

    :param limit: Optional. The page limit.  If not specified, the default page limit is 10.
    :type limit: int
    :param offset: Optional. The page offset.  If not specified, the default page offset is 0.
    :type offset: int
    :param user_id: Optional. Filter by UserID.
    :type user_id: int
    :param content_definition_id: Optional. Filter by ContentDefinitionID
    :type content_definition_id: int

    """
    return web.Response(status=200)


async def user_content_definitions_post_user_content_definition(request: web.Request, body) -> web.Response:
    """Create a UserContentDefinition

    Creates a UserContentDefinition.  The body of the POST is the UserContentDefinition to create.              The UserContentDefinitionID will be assigned on creation of the Job.  When successful, the response              is the UserContentDefinitionID.  If unsuccessful, an appropriate ApiError is returned.

    :param body: The UserContentDefinition to create.
    :type body: dict | bytes

    """
    body = ContentSubmissionSharedBusinessEntitiesUserContentDefinition.from_dict(body)
    return web.Response(status=200)
