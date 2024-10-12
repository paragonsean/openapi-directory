from typing import List, Dict
from aiohttp import web

from openapi_server.models.base_item_dto_query_result import BaseItemDtoQueryResult
from openapi_server.models.create_playlist_dto import CreatePlaylistDto
from openapi_server.models.image_type import ImageType
from openapi_server.models.item_fields import ItemFields
from openapi_server.models.playlist_creation_result import PlaylistCreationResult
from openapi_server import util


async def add_to_playlist(request: web.Request, playlist_id, ids=None, user_id=None) -> web.Response:
    """Adds items to a playlist.

    

    :param playlist_id: The playlist id.
    :type playlist_id: str
    :type playlist_id: str
    :param ids: Item id, comma delimited.
    :type ids: List[str]
    :param user_id: The userId.
    :type user_id: str
    :type user_id: str

    """
    return web.Response(status=200)


async def create_playlist(request: web.Request, name=None, ids=None, user_id=None, media_type=None, body=None) -> web.Response:
    """Creates a new playlist.

    For backwards compatibility parameters can be sent via Query or Body, with Query having higher precedence.

    :param name: The playlist name.
    :type name: str
    :param ids: The item ids.
    :type ids: List[str]
    :param user_id: The user id.
    :type user_id: str
    :type user_id: str
    :param media_type: The media type.
    :type media_type: str
    :param body: The create playlist payload.
    :type body: dict | bytes

    """
    body = CreatePlaylistDto.from_dict(body)
    return web.Response(status=200)


async def get_playlist_items(request: web.Request, playlist_id, user_id, start_index=None, limit=None, fields=None, enable_images=None, enable_user_data=None, image_type_limit=None, enable_image_types=None) -> web.Response:
    """Gets the original items of a playlist.

    

    :param playlist_id: The playlist id.
    :type playlist_id: str
    :type playlist_id: str
    :param user_id: User id.
    :type user_id: str
    :type user_id: str
    :param start_index: Optional. The record index to start at. All items with a lower index will be dropped from the results.
    :type start_index: int
    :param limit: Optional. The maximum number of records to return.
    :type limit: int
    :param fields: Optional. Specify additional fields of information to return in the output.
    :type fields: list | bytes
    :param enable_images: Optional. Include image information in output.
    :type enable_images: bool
    :param enable_user_data: Optional. Include user data.
    :type enable_user_data: bool
    :param image_type_limit: Optional. The max number of images to return, per image type.
    :type image_type_limit: int
    :param enable_image_types: Optional. The image types to include in the output.
    :type enable_image_types: list | bytes

    """
    fields = [ItemFields.from_dict(d) for d in fields]
    enable_image_types = [ImageType.from_dict(d) for d in enable_image_types]
    return web.Response(status=200)


async def move_item(request: web.Request, playlist_id, item_id, new_index) -> web.Response:
    """Moves a playlist item.

    

    :param playlist_id: The playlist id.
    :type playlist_id: str
    :param item_id: The item id.
    :type item_id: str
    :param new_index: The new index.
    :type new_index: int

    """
    return web.Response(status=200)


async def remove_from_playlist(request: web.Request, playlist_id, entry_ids=None) -> web.Response:
    """Removes items from a playlist.

    

    :param playlist_id: The playlist id.
    :type playlist_id: str
    :param entry_ids: The item ids, comma delimited.
    :type entry_ids: List[str]

    """
    return web.Response(status=200)
