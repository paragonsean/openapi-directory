from typing import List, Dict
from aiohttp import web

from openapi_server.models.base_item_dto import BaseItemDto
from openapi_server.models.base_item_dto_query_result import BaseItemDtoQueryResult
from openapi_server.models.image_type import ImageType
from openapi_server.models.item_fields import ItemFields
from openapi_server.models.item_filter import ItemFilter
from openapi_server import util


async def get_album_artists(request: web.Request, min_community_rating=None, start_index=None, limit=None, search_term=None, parent_id=None, fields=None, exclude_item_types=None, include_item_types=None, filters=None, is_favorite=None, media_types=None, genres=None, genre_ids=None, official_ratings=None, tags=None, years=None, enable_user_data=None, image_type_limit=None, enable_image_types=None, person=None, person_ids=None, person_types=None, studios=None, studio_ids=None, user_id=None, name_starts_with_or_greater=None, name_starts_with=None, name_less_than=None, enable_images=None, enable_total_record_count=None) -> web.Response:
    """Gets all album artists from a given item, folder, or the entire library.

    

    :param min_community_rating: Optional filter by minimum community rating.
    :type min_community_rating: float
    :param start_index: Optional. The record index to start at. All items with a lower index will be dropped from the results.
    :type start_index: int
    :param limit: Optional. The maximum number of records to return.
    :type limit: int
    :param search_term: Optional. Search term.
    :type search_term: str
    :param parent_id: Specify this to localize the search to a specific item or folder. Omit to use the root.
    :type parent_id: str
    :type parent_id: str
    :param fields: Optional. Specify additional fields of information to return in the output.
    :type fields: list | bytes
    :param exclude_item_types: Optional. If specified, results will be filtered out based on item type. This allows multiple, comma delimited.
    :type exclude_item_types: List[str]
    :param include_item_types: Optional. If specified, results will be filtered based on item type. This allows multiple, comma delimited.
    :type include_item_types: List[str]
    :param filters: Optional. Specify additional filters to apply.
    :type filters: list | bytes
    :param is_favorite: Optional filter by items that are marked as favorite, or not.
    :type is_favorite: bool
    :param media_types: Optional filter by MediaType. Allows multiple, comma delimited.
    :type media_types: List[str]
    :param genres: Optional. If specified, results will be filtered based on genre. This allows multiple, pipe delimited.
    :type genres: List[str]
    :param genre_ids: Optional. If specified, results will be filtered based on genre id. This allows multiple, pipe delimited.
    :type genre_ids: List[str]
    :param official_ratings: Optional. If specified, results will be filtered based on OfficialRating. This allows multiple, pipe delimited.
    :type official_ratings: List[str]
    :param tags: Optional. If specified, results will be filtered based on tag. This allows multiple, pipe delimited.
    :type tags: List[str]
    :param years: Optional. If specified, results will be filtered based on production year. This allows multiple, comma delimited.
    :type years: List[int]
    :param enable_user_data: Optional, include user data.
    :type enable_user_data: bool
    :param image_type_limit: Optional, the max number of images to return, per image type.
    :type image_type_limit: int
    :param enable_image_types: Optional. The image types to include in the output.
    :type enable_image_types: list | bytes
    :param person: Optional. If specified, results will be filtered to include only those containing the specified person.
    :type person: str
    :param person_ids: Optional. If specified, results will be filtered to include only those containing the specified person ids.
    :type person_ids: List[str]
    :param person_types: Optional. If specified, along with Person, results will be filtered to include only those containing the specified person and PersonType. Allows multiple, comma-delimited.
    :type person_types: List[str]
    :param studios: Optional. If specified, results will be filtered based on studio. This allows multiple, pipe delimited.
    :type studios: List[str]
    :param studio_ids: Optional. If specified, results will be filtered based on studio id. This allows multiple, pipe delimited.
    :type studio_ids: List[str]
    :param user_id: User id.
    :type user_id: str
    :type user_id: str
    :param name_starts_with_or_greater: Optional filter by items whose name is sorted equally or greater than a given input string.
    :type name_starts_with_or_greater: str
    :param name_starts_with: Optional filter by items whose name is sorted equally than a given input string.
    :type name_starts_with: str
    :param name_less_than: Optional filter by items whose name is equally or lesser than a given input string.
    :type name_less_than: str
    :param enable_images: Optional, include image information in output.
    :type enable_images: bool
    :param enable_total_record_count: Total record count.
    :type enable_total_record_count: bool

    """
    fields = [ItemFields.from_dict(d) for d in fields]
    filters = [ItemFilter.from_dict(d) for d in filters]
    enable_image_types = [ImageType.from_dict(d) for d in enable_image_types]
    return web.Response(status=200)


async def get_artist_by_name(request: web.Request, name, user_id=None) -> web.Response:
    """Gets an artist by name.

    

    :param name: Studio name.
    :type name: str
    :param user_id: Optional. Filter by user id, and attach user data.
    :type user_id: str
    :type user_id: str

    """
    return web.Response(status=200)


async def get_artists(request: web.Request, min_community_rating=None, start_index=None, limit=None, search_term=None, parent_id=None, fields=None, exclude_item_types=None, include_item_types=None, filters=None, is_favorite=None, media_types=None, genres=None, genre_ids=None, official_ratings=None, tags=None, years=None, enable_user_data=None, image_type_limit=None, enable_image_types=None, person=None, person_ids=None, person_types=None, studios=None, studio_ids=None, user_id=None, name_starts_with_or_greater=None, name_starts_with=None, name_less_than=None, enable_images=None, enable_total_record_count=None) -> web.Response:
    """Gets all artists from a given item, folder, or the entire library.

    

    :param min_community_rating: Optional filter by minimum community rating.
    :type min_community_rating: float
    :param start_index: Optional. The record index to start at. All items with a lower index will be dropped from the results.
    :type start_index: int
    :param limit: Optional. The maximum number of records to return.
    :type limit: int
    :param search_term: Optional. Search term.
    :type search_term: str
    :param parent_id: Specify this to localize the search to a specific item or folder. Omit to use the root.
    :type parent_id: str
    :type parent_id: str
    :param fields: Optional. Specify additional fields of information to return in the output.
    :type fields: list | bytes
    :param exclude_item_types: Optional. If specified, results will be filtered out based on item type. This allows multiple, comma delimited.
    :type exclude_item_types: List[str]
    :param include_item_types: Optional. If specified, results will be filtered based on item type. This allows multiple, comma delimited.
    :type include_item_types: List[str]
    :param filters: Optional. Specify additional filters to apply.
    :type filters: list | bytes
    :param is_favorite: Optional filter by items that are marked as favorite, or not.
    :type is_favorite: bool
    :param media_types: Optional filter by MediaType. Allows multiple, comma delimited.
    :type media_types: List[str]
    :param genres: Optional. If specified, results will be filtered based on genre. This allows multiple, pipe delimited.
    :type genres: List[str]
    :param genre_ids: Optional. If specified, results will be filtered based on genre id. This allows multiple, pipe delimited.
    :type genre_ids: List[str]
    :param official_ratings: Optional. If specified, results will be filtered based on OfficialRating. This allows multiple, pipe delimited.
    :type official_ratings: List[str]
    :param tags: Optional. If specified, results will be filtered based on tag. This allows multiple, pipe delimited.
    :type tags: List[str]
    :param years: Optional. If specified, results will be filtered based on production year. This allows multiple, comma delimited.
    :type years: List[int]
    :param enable_user_data: Optional, include user data.
    :type enable_user_data: bool
    :param image_type_limit: Optional, the max number of images to return, per image type.
    :type image_type_limit: int
    :param enable_image_types: Optional. The image types to include in the output.
    :type enable_image_types: list | bytes
    :param person: Optional. If specified, results will be filtered to include only those containing the specified person.
    :type person: str
    :param person_ids: Optional. If specified, results will be filtered to include only those containing the specified person ids.
    :type person_ids: List[str]
    :param person_types: Optional. If specified, along with Person, results will be filtered to include only those containing the specified person and PersonType. Allows multiple, comma-delimited.
    :type person_types: List[str]
    :param studios: Optional. If specified, results will be filtered based on studio. This allows multiple, pipe delimited.
    :type studios: List[str]
    :param studio_ids: Optional. If specified, results will be filtered based on studio id. This allows multiple, pipe delimited.
    :type studio_ids: List[str]
    :param user_id: User id.
    :type user_id: str
    :type user_id: str
    :param name_starts_with_or_greater: Optional filter by items whose name is sorted equally or greater than a given input string.
    :type name_starts_with_or_greater: str
    :param name_starts_with: Optional filter by items whose name is sorted equally than a given input string.
    :type name_starts_with: str
    :param name_less_than: Optional filter by items whose name is equally or lesser than a given input string.
    :type name_less_than: str
    :param enable_images: Optional, include image information in output.
    :type enable_images: bool
    :param enable_total_record_count: Total record count.
    :type enable_total_record_count: bool

    """
    fields = [ItemFields.from_dict(d) for d in fields]
    filters = [ItemFilter.from_dict(d) for d in filters]
    enable_image_types = [ImageType.from_dict(d) for d in enable_image_types]
    return web.Response(status=200)
