from typing import List, Dict
from aiohttp import web

from openapi_server.models.base_item_dto import BaseItemDto
from openapi_server.models.base_item_dto_query_result import BaseItemDtoQueryResult
from openapi_server.models.image_type import ImageType
from openapi_server.models.item_fields import ItemFields
from openapi_server.models.item_filter import ItemFilter
from openapi_server.models.problem_details import ProblemDetails
from openapi_server import util


async def get_person(request: web.Request, name, user_id=None) -> web.Response:
    """Get person by name.

    

    :param name: Person name.
    :type name: str
    :param user_id: Optional. Filter by user id, and attach user data.
    :type user_id: str
    :type user_id: str

    """
    return web.Response(status=200)


async def get_persons(request: web.Request, limit=None, search_term=None, fields=None, filters=None, is_favorite=None, enable_user_data=None, image_type_limit=None, enable_image_types=None, exclude_person_types=None, person_types=None, appears_in_item_id=None, user_id=None, enable_images=None) -> web.Response:
    """Gets all persons.

    

    :param limit: Optional. The maximum number of records to return.
    :type limit: int
    :param search_term: The search term.
    :type search_term: str
    :param fields: Optional. Specify additional fields of information to return in the output.
    :type fields: list | bytes
    :param filters: Optional. Specify additional filters to apply.
    :type filters: list | bytes
    :param is_favorite: Optional filter by items that are marked as favorite, or not. userId is required.
    :type is_favorite: bool
    :param enable_user_data: Optional, include user data.
    :type enable_user_data: bool
    :param image_type_limit: Optional, the max number of images to return, per image type.
    :type image_type_limit: int
    :param enable_image_types: Optional. The image types to include in the output.
    :type enable_image_types: list | bytes
    :param exclude_person_types: Optional. If specified results will be filtered to exclude those containing the specified PersonType. Allows multiple, comma-delimited.
    :type exclude_person_types: List[str]
    :param person_types: Optional. If specified results will be filtered to include only those containing the specified PersonType. Allows multiple, comma-delimited.
    :type person_types: List[str]
    :param appears_in_item_id: Optional. If specified, person results will be filtered on items related to said persons.
    :type appears_in_item_id: str
    :type appears_in_item_id: str
    :param user_id: User id.
    :type user_id: str
    :type user_id: str
    :param enable_images: Optional, include image information in output.
    :type enable_images: bool

    """
    fields = [ItemFields.from_dict(d) for d in fields]
    filters = [ItemFilter.from_dict(d) for d in filters]
    enable_image_types = [ImageType.from_dict(d) for d in enable_image_types]
    return web.Response(status=200)
