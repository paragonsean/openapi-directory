from typing import List, Dict
from aiohttp import web

from openapi_server.models.base_item_dto_query_result import BaseItemDtoQueryResult
from openapi_server.models.image_type import ImageType
from openapi_server.models.item_fields import ItemFields
from openapi_server import util


async def get_instant_mix_from_album(request: web.Request, id, user_id=None, limit=None, fields=None, enable_images=None, enable_user_data=None, image_type_limit=None, enable_image_types=None) -> web.Response:
    """Creates an instant playlist based on a given song.

    

    :param id: The item id.
    :type id: str
    :type id: str
    :param user_id: Optional. Filter by user id, and attach user data.
    :type user_id: str
    :type user_id: str
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


async def get_instant_mix_from_artists(request: web.Request, id, user_id=None, limit=None, fields=None, enable_images=None, enable_user_data=None, image_type_limit=None, enable_image_types=None) -> web.Response:
    """Creates an instant playlist based on a given song.

    

    :param id: The item id.
    :type id: str
    :type id: str
    :param user_id: Optional. Filter by user id, and attach user data.
    :type user_id: str
    :type user_id: str
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


async def get_instant_mix_from_item(request: web.Request, id, user_id=None, limit=None, fields=None, enable_images=None, enable_user_data=None, image_type_limit=None, enable_image_types=None) -> web.Response:
    """Creates an instant playlist based on a given song.

    

    :param id: The item id.
    :type id: str
    :type id: str
    :param user_id: Optional. Filter by user id, and attach user data.
    :type user_id: str
    :type user_id: str
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


async def get_instant_mix_from_music_genre(request: web.Request, name, user_id=None, limit=None, fields=None, enable_images=None, enable_user_data=None, image_type_limit=None, enable_image_types=None) -> web.Response:
    """Creates an instant playlist based on a given song.

    

    :param name: The genre name.
    :type name: str
    :param user_id: Optional. Filter by user id, and attach user data.
    :type user_id: str
    :type user_id: str
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


async def get_instant_mix_from_music_genres(request: web.Request, id, user_id=None, limit=None, fields=None, enable_images=None, enable_user_data=None, image_type_limit=None, enable_image_types=None) -> web.Response:
    """Creates an instant playlist based on a given song.

    

    :param id: The item id.
    :type id: str
    :type id: str
    :param user_id: Optional. Filter by user id, and attach user data.
    :type user_id: str
    :type user_id: str
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


async def get_instant_mix_from_playlist(request: web.Request, id, user_id=None, limit=None, fields=None, enable_images=None, enable_user_data=None, image_type_limit=None, enable_image_types=None) -> web.Response:
    """Creates an instant playlist based on a given song.

    

    :param id: The item id.
    :type id: str
    :type id: str
    :param user_id: Optional. Filter by user id, and attach user data.
    :type user_id: str
    :type user_id: str
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


async def get_instant_mix_from_song(request: web.Request, id, user_id=None, limit=None, fields=None, enable_images=None, enable_user_data=None, image_type_limit=None, enable_image_types=None) -> web.Response:
    """Creates an instant playlist based on a given song.

    

    :param id: The item id.
    :type id: str
    :type id: str
    :param user_id: Optional. Filter by user id, and attach user data.
    :type user_id: str
    :type user_id: str
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
