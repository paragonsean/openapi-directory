from typing import List, Dict
from aiohttp import web

from openapi_server.models.api_models_api_error import APIModelsApiError
from openapi_server.models.api_paged_response_content_submission_shared_business_entities_content_submission import APIPagedResponseContentSubmissionSharedBusinessEntitiesContentSubmission
from openapi_server.models.api_paged_response_content_submission_shared_business_entities_content_submission_attribute import APIPagedResponseContentSubmissionSharedBusinessEntitiesContentSubmissionAttribute
from openapi_server.models.build_system_shared_interfaces_i_job_run import BuildSystemSharedInterfacesIJobRun
from openapi_server.models.content_submission_shared_business_entities_content_submission import ContentSubmissionSharedBusinessEntitiesContentSubmission
from openapi_server.models.content_submission_shared_business_entities_content_submission_attribute import ContentSubmissionSharedBusinessEntitiesContentSubmissionAttribute
from openapi_server import util


async def content_submissions_delete_content_submission(request: web.Request, content_submission_id) -> web.Response:
    """Delete a ContentSubmission

    Deletes an ContentSubmission. When successful, the response is empty.  If unsuccessful, an appropriate              ApiError is returned.

    :param content_submission_id: The ID of the ContentSubmission to delete
    :type content_submission_id: int

    """
    return web.Response(status=200)


async def content_submissions_delete_content_submission_attribute(request: web.Request, content_submission_attribute_id) -> web.Response:
    """Remove an Attribute from a ContentSubmission

    No Documentation Found.

    :param content_submission_attribute_id: The ID of the Attribute to remove.
    :type content_submission_attribute_id: int

    """
    return web.Response(status=200)


async def content_submissions_get_content_submission(request: web.Request, content_submission_id, include_attributes=None) -> web.Response:
    """Get a ContentSubmission by ID

    Gets a ContentSubmission by ID. When successful, the response is the requested ContentSubmission.              If unsuccessful, an appropriate ApiError is returned.

    :param content_submission_id: The ID of the ContentSubmission to get.
    :type content_submission_id: int
    :param include_attributes: Names of Attributes to include when retrieving this submission. This should be a comma-separated list.
    :type include_attributes: str

    """
    return web.Response(status=200)


async def content_submissions_get_content_submission_attributes(request: web.Request, content_submission_id, limit=None, offset=None, name=None) -> web.Response:
    """Get Attributes for a ContentSubmission

    No Documentation Found.

    :param content_submission_id: The ID of the ContentSubmission.
    :type content_submission_id: int
    :param limit: Optional. The page limit.  If not specified, the default page limit is 10.
    :type limit: int
    :param offset: Optional. The page offset.  If not specified, the default page offset is 0.
    :type offset: int
    :param name: Optional. Filter the attributes by Name.
    :type name: str

    """
    return web.Response(status=200)


async def content_submissions_get_content_submission_status(request: web.Request, content_submission_id, include_activity_run_details=None) -> web.Response:
    """Get the status of a ContentSubmission

    No Documentation Found.

    :param content_submission_id: The ID of the ContentSubmission to get.
    :type content_submission_id: int
    :param include_activity_run_details: True to include all status details if JobRun. Defaults to false
    :type include_activity_run_details: bool

    """
    return web.Response(status=200)


async def content_submissions_get_content_submissions(request: web.Request, limit=None, offset=None, user_id=None, content_definition_id=None, include_attributes=None, release_id=None, type_id=None, version=None, include_definition=None) -> web.Response:
    """Get ContentSubmissions

    Gets a collection of ContentSubmissions. When successful, the response is a PagedResponse of ContentSubmissions. Additional searches: attributes[Name]&#x3D;Value. This can be used to search for submissions that have the specified values for attributes. Beginning and ending wildcard (*) supported for value.              If unsuccessful, an appropriate ApiError is returned.

    :param limit: Optional. The page limit.  If not specified, the default page limit is 10.
    :type limit: int
    :param offset: Optional. The page offset.  If not specified, the default page offset is 0.
    :type offset: int
    :param user_id: Optional. Filter by UserID.
    :type user_id: int
    :param content_definition_id: Optional. Filter by ContentDefinitionID
    :type content_definition_id: int
    :param include_attributes: Names of Attributes to include when retrieving this submission. This should be a comma-separated list. If not provided, Attributes are not included. If &#39;*&#39;, all Attributes are included.
    :type include_attributes: str
    :param release_id: Optional. Filter the submissions by whether they are part of the Release with the specified Release ID.
    :type release_id: int
    :param type_id: Optional. Filter submissions by their ContentDefinition&#39;s Type ID.
    :type type_id: int
    :param version: Optional. Filter submissions by their Version.
    :type version: int
    :param include_definition: Optional. If true, includes the ContentDefinition for each submission.
    :type include_definition: bool

    """
    return web.Response(status=200)


async def content_submissions_post_content_submission(request: web.Request, body) -> web.Response:
    """Create a ContentSubmission

    Creates a ContentSubmission.  The body of the POST is the ContentSubmission to create.              The ContentSubmissionID will be assigned on creation of the Job.  When successful, the response              is the ContentSubmissionID.  If unsuccessful, an appropriate ApiError is returned.

    :param body: The ContentSubmission to create.
    :type body: dict | bytes

    """
    body = ContentSubmissionSharedBusinessEntitiesContentSubmission.from_dict(body)
    return web.Response(status=200)


async def content_submissions_post_content_submission_attribute(request: web.Request, content_submission_id, body) -> web.Response:
    """Add an Attribute to a ContentSubmission

    No Documentation Found.

    :param content_submission_id: The ID of the ContentSubmission
    :type content_submission_id: int
    :param body: The Attribute to add.
    :type body: dict | bytes

    """
    body = ContentSubmissionSharedBusinessEntitiesContentSubmissionAttribute.from_dict(body)
    return web.Response(status=200)


async def content_submissions_post_content_submission_attributes(request: web.Request, content_submission_id, body) -> web.Response:
    """No Documentation Found.

    No Documentation Found.

    :param content_submission_id: 
    :type content_submission_id: int
    :param body: 
    :type body: list | bytes

    """
    body = [ContentSubmissionSharedBusinessEntitiesContentSubmissionAttribute.from_dict(d) for d in body]
    return web.Response(status=200)


async def content_submissions_put_content_submission(request: web.Request, content_submission_id, body) -> web.Response:
    """Update a ContentSubmission

    Updates a ContentSubmission.  The body of the PUT is the updated ContentSubmission.                When successful, the response is empty.  If unsuccessful, an appropriate ApiError is returned.

    :param content_submission_id: The ID of the ContentSubmission to update
    :type content_submission_id: int
    :param body: The updated ContentSubmission
    :type body: dict | bytes

    """
    body = ContentSubmissionSharedBusinessEntitiesContentSubmission.from_dict(body)
    return web.Response(status=200)


async def content_submissions_put_content_submission_attribute_async(request: web.Request, content_submission_attribute_id, body) -> web.Response:
    """Update an Attribute for a ContentSubmission

    No Documentation Found.

    :param content_submission_attribute_id: The ID of the Attribute to update.
    :type content_submission_attribute_id: int
    :param body: The Attribute to update.
    :type body: dict | bytes

    """
    body = ContentSubmissionSharedBusinessEntitiesContentSubmissionAttribute.from_dict(body)
    return web.Response(status=200)


async def content_submissions_put_content_submission_attributes(request: web.Request, body) -> web.Response:
    """No Documentation Found.

    No Documentation Found.

    :param body: 
    :type body: list | bytes

    """
    body = [ContentSubmissionSharedBusinessEntitiesContentSubmissionAttribute.from_dict(d) for d in body]
    return web.Response(status=200)
