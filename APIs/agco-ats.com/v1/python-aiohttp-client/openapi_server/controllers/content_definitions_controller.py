from typing import List, Dict
from aiohttp import web

from openapi_server.models.api_models_api_error import APIModelsApiError
from openapi_server.models.api_paged_response_content_submission_shared_business_entities_content_definition import APIPagedResponseContentSubmissionSharedBusinessEntitiesContentDefinition
from openapi_server.models.api_paged_response_content_submission_shared_business_entities_content_definition_attribute import APIPagedResponseContentSubmissionSharedBusinessEntitiesContentDefinitionAttribute
from openapi_server.models.content_submission_shared_business_entities_content_definition import ContentSubmissionSharedBusinessEntitiesContentDefinition
from openapi_server.models.content_submission_shared_business_entities_content_definition_attribute import ContentSubmissionSharedBusinessEntitiesContentDefinitionAttribute
from openapi_server import util


async def content_definitions_delete_content_definition(request: web.Request, content_definition_id) -> web.Response:
    """Delete a ContentDefinition

    Deletes an ContentDefinition. When successful, the response is empty.  If unsuccessful, an appropriate              ApiError is returned.

    :param content_definition_id: The ID of the ContentDefinition to delete
    :type content_definition_id: int

    """
    return web.Response(status=200)


async def content_definitions_delete_content_definition_attribute(request: web.Request, content_definition_attribute_id) -> web.Response:
    """Remove an Attribute from a ContentDefinition

    No Documentation Found.

    :param content_definition_attribute_id: The ID of the Attribute to remove.
    :type content_definition_attribute_id: int

    """
    return web.Response(status=200)


async def content_definitions_get_content_definition(request: web.Request, content_definition_id, include_attributes=None) -> web.Response:
    """Get a ContentDefinition by ID

    Gets a ContentDefinition by ID. When successful, the response is the requested ContentDefinition.              If unsuccessful, an appropriate ApiError is returned.

    :param content_definition_id: The ID of the ContentDefinition to get.
    :type content_definition_id: int
    :param include_attributes: Names of Attributes to include when retrieving this definition. This should be a comma-separated list. If not provided, Attributes are not included. If &#39;*&#39;, all Attributes are included.
    :type include_attributes: str

    """
    return web.Response(status=200)


async def content_definitions_get_content_definition_attributes(request: web.Request, content_definition_id, limit=None, offset=None, name=None) -> web.Response:
    """Get Attributes for a ContentDefinition

    No Documentation Found.

    :param content_definition_id: The ID of the ContentDefinition.
    :type content_definition_id: int
    :param limit: Optional. The page limit.  If not specified, the default page limit is 10.
    :type limit: int
    :param offset: Optional. The page offset.  If not specified, the default page offset is 0.
    :type offset: int
    :param name: Optional. Filter the attributes by Name.
    :type name: str

    """
    return web.Response(status=200)


async def content_definitions_get_content_definitions(request: web.Request, limit=None, offset=None, user_id=None, include_attributes=None, name=None, type_id=None, package_type_id=None) -> web.Response:
    """Get ContentDefinitions

    Gets a collection of ContentDefinitions. When successful, the response is a PagedResponse of ContentDefinitions.              If unsuccessful, an appropriate ApiError is returned.

    :param limit: Optional. The page limit.  If not specified, the default page limit is 10.
    :type limit: int
    :param offset: Optional. The page offset.  If not specified, the default page offset is 0.
    :type offset: int
    :param user_id: Optional. Filter by UserID.
    :type user_id: int
    :param include_attributes: Names of Attributes to include when retrieving this definition. This should be a comma-separated list. If not provided, Attributes are not included. If &#39;*&#39;, all Attributes are included.
    :type include_attributes: str
    :param name: Optional. Filter by Name. Supports beginning and ending wildcard (*).
    :type name: str
    :param type_id: Optional. Filter by TypeID.
    :type type_id: int
    :param package_type_id: Optional. Filter by PackageTypeID.
    :type package_type_id: str

    """
    return web.Response(status=200)


async def content_definitions_post_content_definition(request: web.Request, body) -> web.Response:
    """Create a ContentDefinition

    Creates a ContentDefinition.  The body of the POST is the ContentDefinition to create.              The ContentDefinitionID will be assigned on creation of the Job.  When successful, the response              is the JobID.  If unsuccessful, an appropriate ApiError is returned.

    :param body: The ContentDefinition to create.
    :type body: dict | bytes

    """
    body = ContentSubmissionSharedBusinessEntitiesContentDefinition.from_dict(body)
    return web.Response(status=200)


async def content_definitions_post_content_definition_attribute(request: web.Request, content_definition_id, body) -> web.Response:
    """Add an Attribute to a ContentDefinition

    No Documentation Found.

    :param content_definition_id: The ID of the ContentDefinition
    :type content_definition_id: int
    :param body: The Attribute to add.
    :type body: dict | bytes

    """
    body = ContentSubmissionSharedBusinessEntitiesContentDefinitionAttribute.from_dict(body)
    return web.Response(status=200)


async def content_definitions_post_content_definition_attributes(request: web.Request, content_definition_id, body) -> web.Response:
    """No Documentation Found.

    No Documentation Found.

    :param content_definition_id: 
    :type content_definition_id: int
    :param body: 
    :type body: list | bytes

    """
    body = [ContentSubmissionSharedBusinessEntitiesContentDefinitionAttribute.from_dict(d) for d in body]
    return web.Response(status=200)


async def content_definitions_put_content_definition(request: web.Request, content_definition_id, body) -> web.Response:
    """Update a ContentDefinition

    Updates a ContentDefinition.  The body of the PUT is the updated ContentDefinition.                When successful, the response is empty.  If unsuccessful, an appropriate ApiError is returned.

    :param content_definition_id: The ID of the ContentDefinition to update
    :type content_definition_id: int
    :param body: The updated ContentDefinition
    :type body: dict | bytes

    """
    body = ContentSubmissionSharedBusinessEntitiesContentDefinition.from_dict(body)
    return web.Response(status=200)


async def content_definitions_put_content_definition_attribute_async(request: web.Request, content_definition_attribute_id, body) -> web.Response:
    """Update an Attribute for a ContentDefinition

    No Documentation Found.

    :param content_definition_attribute_id: The ID of the Attribute to update.
    :type content_definition_attribute_id: int
    :param body: The Attribute to update.
    :type body: dict | bytes

    """
    body = ContentSubmissionSharedBusinessEntitiesContentDefinitionAttribute.from_dict(body)
    return web.Response(status=200)


async def content_definitions_put_content_definition_attributes(request: web.Request, body) -> web.Response:
    """No Documentation Found.

    No Documentation Found.

    :param body: 
    :type body: list | bytes

    """
    body = [ContentSubmissionSharedBusinessEntitiesContentDefinitionAttribute.from_dict(d) for d in body]
    return web.Response(status=200)
