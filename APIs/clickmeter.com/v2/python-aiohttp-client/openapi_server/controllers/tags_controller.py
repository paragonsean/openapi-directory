from typing import List, Dict
from aiohttp import web

from openapi_server.models.api_core_dto_tags_tag import ApiCoreDtoTagsTag
from openapi_server.models.api_core_requests_generic_text_patch import ApiCoreRequestsGenericTextPatch
from openapi_server.models.api_core_requests_patch_body import ApiCoreRequestsPatchBody
from openapi_server.models.api_core_responses_count_responce import ApiCoreResponsesCountResponce
from openapi_server.models.api_core_responses_entities_response_api_core_responses_entity_uri_system_int64 import ApiCoreResponsesEntitiesResponseApiCoreResponsesEntityUriSystemInt64
from openapi_server.models.api_core_responses_entity_uri_system_int64 import ApiCoreResponsesEntityUriSystemInt64
from openapi_server import util


async def tags_count(request: web.Request, name=None, datapoints=None, groups=None, type=None) -> web.Response:
    """List of all the groups associated to the user filtered by this tag.

    

    :param name: Name of the tag
    :type name: str
    :param datapoints: Comma separated list of datapoints id to filter by
    :type datapoints: str
    :param groups: Comma separated list of groups id to filter by
    :type groups: str
    :param type: Type of entity related to the tag
    :type type: str

    """
    return web.Response(status=200)


async def tags_delete(request: web.Request, tag_id) -> web.Response:
    """Delete a tag

    

    :param tag_id: Id of the tag
    :type tag_id: int

    """
    return web.Response(status=200)


async def tags_delete_related_datapoints(request: web.Request, tag_id) -> web.Response:
    """Delete the association of this tag with all datapoints

    

    :param tag_id: Id of the tag
    :type tag_id: int

    """
    return web.Response(status=200)


async def tags_delete_related_groups(request: web.Request, tag_id) -> web.Response:
    """Delete the association of this tag with all groups

    

    :param tag_id: Id of the tag
    :type tag_id: int

    """
    return web.Response(status=200)


async def tags_get(request: web.Request, offset=None, limit=None, name=None, datapoints=None, groups=None, type=None) -> web.Response:
    """List of all the groups associated to the user filtered by this tag.

    

    :param offset: Where to start when retrieving elements. Default is 0 if not specified.
    :type offset: int
    :param limit: Maximum elements to retrieve. Default to 20 if not specified.
    :type limit: int
    :param name: Name of the tag
    :type name: str
    :param datapoints: Comma separated list of datapoints id to filter by
    :type datapoints: str
    :param groups: Comma separated list of groups id to filter by
    :type groups: str
    :param type: Type of entity related to the tag
    :type type: str

    """
    return web.Response(status=200)


async def tags_get_datapoints(request: web.Request, tag_id, offset=None, limit=None, type=None, status=None, text_search=None, created_after=None, created_before=None) -> web.Response:
    """List of all the datapoints associated to the user filtered by this tag

    

    :param tag_id: Id of the tag.
    :type tag_id: int
    :param offset: Where to start when retrieving elements. Default is 0 if not specified.
    :type offset: int
    :param limit: Maximum elements to retrieve. Default to 20 if not specified.
    :type limit: int
    :param type: Type of the datapoint (\&quot;tp\&quot;/\&quot;tl\&quot;)
    :type type: str
    :param status: Status of the datapoint
    :type status: str
    :param text_search: Filter fields by this pattern
    :type text_search: str
    :param created_after: Exclude datapoints created before this date (YYYYMMDD)
    :type created_after: str
    :param created_before: Exclude datapoints created after this date (YYYYMMDD)
    :type created_before: str

    """
    return web.Response(status=200)


async def tags_get_datapoints_count(request: web.Request, tag_id, type=None, status=None, text_search=None, created_after=None, created_before=None) -> web.Response:
    """Count the datapoints associated to the user filtered by this tag

    

    :param tag_id: Id of the tag.
    :type tag_id: int
    :param type: Type of the datapoint (\&quot;tp\&quot;/\&quot;tl\&quot;)
    :type type: str
    :param status: Status of the datapoint
    :type status: str
    :param text_search: Filter fields by this pattern
    :type text_search: str
    :param created_after: Exclude datapoints created before this date (YYYYMMDD)
    :type created_after: str
    :param created_before: Exclude datapoints created after this date (YYYYMMDD)
    :type created_before: str

    """
    return web.Response(status=200)


async def tags_get_groups(request: web.Request, tag_id, offset=None, limit=None, status=None, text_search=None, created_after=None, created_before=None) -> web.Response:
    """List of all the groups associated to the user filtered by this tag.

    

    :param tag_id: Id of the tag.
    :type tag_id: int
    :param offset: Where to start when retrieving elements. Default is 0 if not specified.
    :type offset: int
    :param limit: Maximum elements to retrieve. Default to 20 if not specified.
    :type limit: int
    :param status: Status of the datapoint
    :type status: str
    :param text_search: Filter fields by this pattern
    :type text_search: str
    :param created_after: Exclude groups created before this date (YYYYMMDD)
    :type created_after: str
    :param created_before: Exclude groups created after this date (YYYYMMDD)
    :type created_before: str

    """
    return web.Response(status=200)


async def tags_get_groups_count(request: web.Request, tag_id, status=None, text_search=None, created_after=None, created_before=None) -> web.Response:
    """Count the groups associated to the user filtered by this tag

    

    :param tag_id: Id of the tag.
    :type tag_id: int
    :param status: Status of the datapoint
    :type status: str
    :param text_search: Filter fields by this pattern
    :type text_search: str
    :param created_after: Exclude groups created before this date (YYYYMMDD)
    :type created_after: str
    :param created_before: Exclude groups created after this date (YYYYMMDD)
    :type created_before: str

    """
    return web.Response(status=200)


async def tags_patch_data_point(request: web.Request, tag_id, body) -> web.Response:
    """Associate/Deassociate a tag with a datapoint

    

    :param tag_id: Id of the tag
    :type tag_id: int
    :param body: The body patch
    :type body: dict | bytes

    """
    body = ApiCoreRequestsPatchBody.from_dict(body)
    return web.Response(status=200)


async def tags_patch_group(request: web.Request, tag_id, body) -> web.Response:
    """Associate/Deassociate a tag with a group

    

    :param tag_id: Id of the tag
    :type tag_id: int
    :param body: The body patch
    :type body: dict | bytes

    """
    body = ApiCoreRequestsPatchBody.from_dict(body)
    return web.Response(status=200)


async def tags_patch_tag_name(request: web.Request, tag_id, body) -> web.Response:
    """Fast patch a tag name

    

    :param tag_id: Id of the tag
    :type tag_id: int
    :param body: The body patch
    :type body: dict | bytes

    """
    body = ApiCoreRequestsGenericTextPatch.from_dict(body)
    return web.Response(status=200)


async def tags_put(request: web.Request, body) -> web.Response:
    """Create a tag

    

    :param body: The body of the tag
    :type body: dict | bytes

    """
    body = ApiCoreDtoTagsTag.from_dict(body)
    return web.Response(status=200)


async def tags_tag_id_get(request: web.Request, tag_id) -> web.Response:
    """Retrieve a tag

    

    :param tag_id: Id of the tag
    :type tag_id: int

    """
    return web.Response(status=200)
