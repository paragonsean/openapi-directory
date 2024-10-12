from typing import List, Dict
from aiohttp import web

from openapi_server.models.api_core_dto_retargeting_retargeting_script import ApiCoreDtoRetargetingRetargetingScript
from openapi_server.models.api_core_responses_count_responce import ApiCoreResponsesCountResponce
from openapi_server.models.api_core_responses_entities_response_api_core_responses_entity_uri_system_int64 import ApiCoreResponsesEntitiesResponseApiCoreResponsesEntityUriSystemInt64
from openapi_server.models.api_core_responses_entity_uri_system_int64 import ApiCoreResponsesEntityUriSystemInt64
from openapi_server import util


async def retargeting_count(request: web.Request, ) -> web.Response:
    """Retrieve count of retargeting scripts

    


    """
    return web.Response(status=200)


async def retargeting_delete(request: web.Request, id) -> web.Response:
    """Deletes a retargeting script (and remove associations)

    

    :param id: The id of the retargeting script
    :type id: int

    """
    return web.Response(status=200)


async def retargeting_get(request: web.Request, offset=None, limit=None) -> web.Response:
    """List of all the retargeting scripts associated to the user

    

    :param offset: Where to start when retrieving elements. Default is 0 if not specified.
    :type offset: int
    :param limit: Maximum elements to retrieve. Default to 20 if not specified.
    :type limit: int

    """
    return web.Response(status=200)


async def retargeting_get_datapoints(request: web.Request, id, offset=None, limit=None, status=None, tags=None, text_search=None, only_favorites=None, sort_by=None, sort_direction=None, created_after=None, created_before=None) -> web.Response:
    """List of all the datapoints associated to the retargeting script.

    

    :param id: Id of the retargeting script
    :type id: int
    :param offset: Where to start when retrieving elements. Default is 0 if not specified.
    :type offset: int
    :param limit: Maximum elements to retrieve. Default to 20 if not specified.
    :type limit: int
    :param status: Status of the datapoint
    :type status: str
    :param tags: A comma separated list of tags you want to filter with.
    :type tags: str
    :param text_search: Filter fields by this pattern
    :type text_search: str
    :param only_favorites: Filter fields by favourite status
    :type only_favorites: bool
    :param sort_by: Field to sort by
    :type sort_by: str
    :param sort_direction: Direction of sort \&quot;asc\&quot; or \&quot;desc\&quot;
    :type sort_direction: str
    :param created_after: Exclude datapoints created before this date (YYYYMMDD)
    :type created_after: str
    :param created_before: Exclude datapoints created after this date (YYYYMMDD)
    :type created_before: str

    """
    return web.Response(status=200)


async def retargeting_get_datapoints_count(request: web.Request, id, status=None, tags=None, text_search=None, only_favorites=None, created_after=None, created_before=None) -> web.Response:
    """Count the datapoints associated to the retargeting script.

    

    :param id: Id of the group
    :type id: int
    :param status: Status of the datapoint
    :type status: str
    :param tags: A comma separated list of tags you want to filter with.
    :type tags: str
    :param text_search: Filter fields by this pattern
    :type text_search: str
    :param only_favorites: Filter fields by favourite status
    :type only_favorites: bool
    :param created_after: Exclude datapoints created before this date (YYYYMMDD)
    :type created_after: str
    :param created_before: Exclude datapoints created after this date (YYYYMMDD)
    :type created_before: str

    """
    return web.Response(status=200)


async def retargeting_id_get(request: web.Request, id) -> web.Response:
    """Get a retargeting script object

    

    :param id: The id of the retargeting script
    :type id: int

    """
    return web.Response(status=200)


async def retargeting_post(request: web.Request, id, body) -> web.Response:
    """Updates a retargeting script

    

    :param id: The id of the retargeting script
    :type id: int
    :param body: The body of the retargeting script
    :type body: dict | bytes

    """
    body = ApiCoreDtoRetargetingRetargetingScript.from_dict(body)
    return web.Response(status=200)


async def retargeting_put(request: web.Request, body) -> web.Response:
    """Creates a retargeting script

    

    :param body: The body of the retargeting script
    :type body: dict | bytes

    """
    body = ApiCoreDtoRetargetingRetargetingScript.from_dict(body)
    return web.Response(status=200)
