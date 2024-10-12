from typing import List, Dict
from aiohttp import web

from openapi_server.models.base_item_dto import BaseItemDto
from openapi_server.models.base_item_dto_query_result import BaseItemDtoQueryResult
from openapi_server.models.image_type import ImageType
from openapi_server.models.item_fields import ItemFields
from openapi_server.models.user_item_data_dto import UserItemDataDto
from openapi_server import util


async def delete_user_item_rating(request: web.Request, user_id, item_id) -> web.Response:
    """Deletes a user&#39;s saved personal rating for an item.

    

    :param user_id: User id.
    :type user_id: str
    :type user_id: str
    :param item_id: Item id.
    :type item_id: str
    :type item_id: str

    """
    return web.Response(status=200)


async def get_intros(request: web.Request, user_id, item_id) -> web.Response:
    """Gets intros to play before the main media item plays.

    

    :param user_id: User id.
    :type user_id: str
    :type user_id: str
    :param item_id: Item id.
    :type item_id: str
    :type item_id: str

    """
    return web.Response(status=200)


async def get_item(request: web.Request, user_id, item_id) -> web.Response:
    """Gets an item from a user&#39;s library.

    

    :param user_id: User id.
    :type user_id: str
    :type user_id: str
    :param item_id: Item id.
    :type item_id: str
    :type item_id: str

    """
    return web.Response(status=200)


async def get_latest_media(request: web.Request, user_id, parent_id=None, fields=None, include_item_types=None, is_played=None, enable_images=None, image_type_limit=None, enable_image_types=None, enable_user_data=None, limit=None, group_items=None) -> web.Response:
    """Gets latest media.

    

    :param user_id: User id.
    :type user_id: str
    :type user_id: str
    :param parent_id: Specify this to localize the search to a specific item or folder. Omit to use the root.
    :type parent_id: str
    :type parent_id: str
    :param fields: Optional. Specify additional fields of information to return in the output.
    :type fields: list | bytes
    :param include_item_types: Optional. If specified, results will be filtered based on item type. This allows multiple, comma delimited.
    :type include_item_types: List[str]
    :param is_played: Filter by items that are played, or not.
    :type is_played: bool
    :param enable_images: Optional. include image information in output.
    :type enable_images: bool
    :param image_type_limit: Optional. the max number of images to return, per image type.
    :type image_type_limit: int
    :param enable_image_types: Optional. The image types to include in the output.
    :type enable_image_types: list | bytes
    :param enable_user_data: Optional. include user data.
    :type enable_user_data: bool
    :param limit: Return item limit.
    :type limit: int
    :param group_items: Whether or not to group items into a parent container.
    :type group_items: bool

    """
    fields = [ItemFields.from_dict(d) for d in fields]
    enable_image_types = [ImageType.from_dict(d) for d in enable_image_types]
    return web.Response(status=200)


async def get_local_trailers(request: web.Request, user_id, item_id) -> web.Response:
    """Gets local trailers for an item.

    

    :param user_id: User id.
    :type user_id: str
    :type user_id: str
    :param item_id: Item id.
    :type item_id: str
    :type item_id: str

    """
    return web.Response(status=200)


async def get_root_folder(request: web.Request, user_id) -> web.Response:
    """Gets the root folder from a user&#39;s library.

    

    :param user_id: User id.
    :type user_id: str
    :type user_id: str

    """
    return web.Response(status=200)


async def get_special_features(request: web.Request, user_id, item_id) -> web.Response:
    """Gets special features for an item.

    

    :param user_id: User id.
    :type user_id: str
    :type user_id: str
    :param item_id: Item id.
    :type item_id: str
    :type item_id: str

    """
    return web.Response(status=200)


async def mark_favorite_item(request: web.Request, user_id, item_id) -> web.Response:
    """Marks an item as a favorite.

    

    :param user_id: User id.
    :type user_id: str
    :type user_id: str
    :param item_id: Item id.
    :type item_id: str
    :type item_id: str

    """
    return web.Response(status=200)


async def unmark_favorite_item(request: web.Request, user_id, item_id) -> web.Response:
    """Unmarks item as a favorite.

    

    :param user_id: User id.
    :type user_id: str
    :type user_id: str
    :param item_id: Item id.
    :type item_id: str
    :type item_id: str

    """
    return web.Response(status=200)


async def update_user_item_rating(request: web.Request, user_id, item_id, likes=None) -> web.Response:
    """Updates a user&#39;s rating for an item.

    

    :param user_id: User id.
    :type user_id: str
    :type user_id: str
    :param item_id: Item id.
    :type item_id: str
    :type item_id: str
    :param likes: Whether this M:Jellyfin.Api.Controllers.UserLibraryController.UpdateUserItemRating(System.Guid,System.Guid,System.Nullable{System.Boolean}) is likes.
    :type likes: bool

    """
    return web.Response(status=200)
