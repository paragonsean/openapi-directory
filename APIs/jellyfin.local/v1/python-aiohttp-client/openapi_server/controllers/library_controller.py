from typing import List, Dict
from aiohttp import web

from openapi_server.models.all_theme_media_result import AllThemeMediaResult
from openapi_server.models.base_item_dto import BaseItemDto
from openapi_server.models.base_item_dto_query_result import BaseItemDtoQueryResult
from openapi_server.models.item_counts import ItemCounts
from openapi_server.models.item_fields import ItemFields
from openapi_server.models.library_options_result_dto import LibraryOptionsResultDto
from openapi_server.models.media_update_info_dto import MediaUpdateInfoDto
from openapi_server.models.problem_details import ProblemDetails
from openapi_server.models.theme_media_result import ThemeMediaResult
from openapi_server import util


async def delete_item(request: web.Request, item_id) -> web.Response:
    """Deletes an item from the library and filesystem.

    

    :param item_id: The item id.
    :type item_id: str
    :type item_id: str

    """
    return web.Response(status=200)


async def delete_items(request: web.Request, ids=None) -> web.Response:
    """Deletes items from the library and filesystem.

    

    :param ids: The item ids.
    :type ids: List[str]

    """
    return web.Response(status=200)


async def get_ancestors(request: web.Request, item_id, user_id=None) -> web.Response:
    """Gets all parents of an item.

    

    :param item_id: The item id.
    :type item_id: str
    :type item_id: str
    :param user_id: Optional. Filter by user id, and attach user data.
    :type user_id: str
    :type user_id: str

    """
    return web.Response(status=200)


async def get_critic_reviews(request: web.Request, item_id) -> web.Response:
    """Gets critic review for an item.

    

    :param item_id: 
    :type item_id: str

    """
    return web.Response(status=200)


async def get_download(request: web.Request, item_id) -> web.Response:
    """Downloads item media.

    

    :param item_id: The item id.
    :type item_id: str
    :type item_id: str

    """
    return web.Response(status=200)


async def get_file(request: web.Request, item_id) -> web.Response:
    """Get the original file of an item.

    

    :param item_id: The item id.
    :type item_id: str
    :type item_id: str

    """
    return web.Response(status=200)


async def get_item_counts(request: web.Request, user_id=None, is_favorite=None) -> web.Response:
    """Get item counts.

    

    :param user_id: Optional. Get counts from a specific user&#39;s library.
    :type user_id: str
    :type user_id: str
    :param is_favorite: Optional. Get counts of favorite items.
    :type is_favorite: bool

    """
    return web.Response(status=200)


async def get_library_options_info(request: web.Request, library_content_type=None, is_new_library=None) -> web.Response:
    """Gets the library options info.

    

    :param library_content_type: Library content type.
    :type library_content_type: str
    :param is_new_library: Whether this is a new library.
    :type is_new_library: bool

    """
    return web.Response(status=200)


async def get_media_folders(request: web.Request, is_hidden=None) -> web.Response:
    """Gets all user media folders.

    

    :param is_hidden: Optional. Filter by folders that are marked hidden, or not.
    :type is_hidden: bool

    """
    return web.Response(status=200)


async def get_physical_paths(request: web.Request, ) -> web.Response:
    """Gets a list of physical paths from virtual folders.

    


    """
    return web.Response(status=200)


async def get_similar_albums(request: web.Request, item_id, exclude_artist_ids=None, user_id=None, limit=None, fields=None) -> web.Response:
    """Gets similar items.

    

    :param item_id: The item id.
    :type item_id: str
    :type item_id: str
    :param exclude_artist_ids: Exclude artist ids.
    :type exclude_artist_ids: List[str]
    :param user_id: Optional. Filter by user id, and attach user data.
    :type user_id: str
    :type user_id: str
    :param limit: Optional. The maximum number of records to return.
    :type limit: int
    :param fields: Optional. Specify additional fields of information to return in the output. This allows multiple, comma delimited. Options: Budget, Chapters, DateCreated, Genres, HomePageUrl, IndexOptions, MediaStreams, Overview, ParentId, Path, People, ProviderIds, PrimaryImageAspectRatio, Revenue, SortName, Studios, Taglines, TrailerUrls.
    :type fields: list | bytes

    """
    fields = [ItemFields.from_dict(d) for d in fields]
    return web.Response(status=200)


async def get_similar_artists(request: web.Request, item_id, exclude_artist_ids=None, user_id=None, limit=None, fields=None) -> web.Response:
    """Gets similar items.

    

    :param item_id: The item id.
    :type item_id: str
    :type item_id: str
    :param exclude_artist_ids: Exclude artist ids.
    :type exclude_artist_ids: List[str]
    :param user_id: Optional. Filter by user id, and attach user data.
    :type user_id: str
    :type user_id: str
    :param limit: Optional. The maximum number of records to return.
    :type limit: int
    :param fields: Optional. Specify additional fields of information to return in the output. This allows multiple, comma delimited. Options: Budget, Chapters, DateCreated, Genres, HomePageUrl, IndexOptions, MediaStreams, Overview, ParentId, Path, People, ProviderIds, PrimaryImageAspectRatio, Revenue, SortName, Studios, Taglines, TrailerUrls.
    :type fields: list | bytes

    """
    fields = [ItemFields.from_dict(d) for d in fields]
    return web.Response(status=200)


async def get_similar_items(request: web.Request, item_id, exclude_artist_ids=None, user_id=None, limit=None, fields=None) -> web.Response:
    """Gets similar items.

    

    :param item_id: The item id.
    :type item_id: str
    :type item_id: str
    :param exclude_artist_ids: Exclude artist ids.
    :type exclude_artist_ids: List[str]
    :param user_id: Optional. Filter by user id, and attach user data.
    :type user_id: str
    :type user_id: str
    :param limit: Optional. The maximum number of records to return.
    :type limit: int
    :param fields: Optional. Specify additional fields of information to return in the output. This allows multiple, comma delimited. Options: Budget, Chapters, DateCreated, Genres, HomePageUrl, IndexOptions, MediaStreams, Overview, ParentId, Path, People, ProviderIds, PrimaryImageAspectRatio, Revenue, SortName, Studios, Taglines, TrailerUrls.
    :type fields: list | bytes

    """
    fields = [ItemFields.from_dict(d) for d in fields]
    return web.Response(status=200)


async def get_similar_movies(request: web.Request, item_id, exclude_artist_ids=None, user_id=None, limit=None, fields=None) -> web.Response:
    """Gets similar items.

    

    :param item_id: The item id.
    :type item_id: str
    :type item_id: str
    :param exclude_artist_ids: Exclude artist ids.
    :type exclude_artist_ids: List[str]
    :param user_id: Optional. Filter by user id, and attach user data.
    :type user_id: str
    :type user_id: str
    :param limit: Optional. The maximum number of records to return.
    :type limit: int
    :param fields: Optional. Specify additional fields of information to return in the output. This allows multiple, comma delimited. Options: Budget, Chapters, DateCreated, Genres, HomePageUrl, IndexOptions, MediaStreams, Overview, ParentId, Path, People, ProviderIds, PrimaryImageAspectRatio, Revenue, SortName, Studios, Taglines, TrailerUrls.
    :type fields: list | bytes

    """
    fields = [ItemFields.from_dict(d) for d in fields]
    return web.Response(status=200)


async def get_similar_shows(request: web.Request, item_id, exclude_artist_ids=None, user_id=None, limit=None, fields=None) -> web.Response:
    """Gets similar items.

    

    :param item_id: The item id.
    :type item_id: str
    :type item_id: str
    :param exclude_artist_ids: Exclude artist ids.
    :type exclude_artist_ids: List[str]
    :param user_id: Optional. Filter by user id, and attach user data.
    :type user_id: str
    :type user_id: str
    :param limit: Optional. The maximum number of records to return.
    :type limit: int
    :param fields: Optional. Specify additional fields of information to return in the output. This allows multiple, comma delimited. Options: Budget, Chapters, DateCreated, Genres, HomePageUrl, IndexOptions, MediaStreams, Overview, ParentId, Path, People, ProviderIds, PrimaryImageAspectRatio, Revenue, SortName, Studios, Taglines, TrailerUrls.
    :type fields: list | bytes

    """
    fields = [ItemFields.from_dict(d) for d in fields]
    return web.Response(status=200)


async def get_similar_trailers(request: web.Request, item_id, exclude_artist_ids=None, user_id=None, limit=None, fields=None) -> web.Response:
    """Gets similar items.

    

    :param item_id: The item id.
    :type item_id: str
    :type item_id: str
    :param exclude_artist_ids: Exclude artist ids.
    :type exclude_artist_ids: List[str]
    :param user_id: Optional. Filter by user id, and attach user data.
    :type user_id: str
    :type user_id: str
    :param limit: Optional. The maximum number of records to return.
    :type limit: int
    :param fields: Optional. Specify additional fields of information to return in the output. This allows multiple, comma delimited. Options: Budget, Chapters, DateCreated, Genres, HomePageUrl, IndexOptions, MediaStreams, Overview, ParentId, Path, People, ProviderIds, PrimaryImageAspectRatio, Revenue, SortName, Studios, Taglines, TrailerUrls.
    :type fields: list | bytes

    """
    fields = [ItemFields.from_dict(d) for d in fields]
    return web.Response(status=200)


async def get_theme_media(request: web.Request, item_id, user_id=None, inherit_from_parent=None) -> web.Response:
    """Get theme songs and videos for an item.

    

    :param item_id: The item id.
    :type item_id: str
    :type item_id: str
    :param user_id: Optional. Filter by user id, and attach user data.
    :type user_id: str
    :type user_id: str
    :param inherit_from_parent: Optional. Determines whether or not parent items should be searched for theme media.
    :type inherit_from_parent: bool

    """
    return web.Response(status=200)


async def get_theme_songs(request: web.Request, item_id, user_id=None, inherit_from_parent=None) -> web.Response:
    """Get theme songs for an item.

    

    :param item_id: The item id.
    :type item_id: str
    :type item_id: str
    :param user_id: Optional. Filter by user id, and attach user data.
    :type user_id: str
    :type user_id: str
    :param inherit_from_parent: Optional. Determines whether or not parent items should be searched for theme media.
    :type inherit_from_parent: bool

    """
    return web.Response(status=200)


async def get_theme_videos(request: web.Request, item_id, user_id=None, inherit_from_parent=None) -> web.Response:
    """Get theme videos for an item.

    

    :param item_id: The item id.
    :type item_id: str
    :type item_id: str
    :param user_id: Optional. Filter by user id, and attach user data.
    :type user_id: str
    :type user_id: str
    :param inherit_from_parent: Optional. Determines whether or not parent items should be searched for theme media.
    :type inherit_from_parent: bool

    """
    return web.Response(status=200)


async def post_added_movies(request: web.Request, tmdb_id=None, imdb_id=None) -> web.Response:
    """Reports that new movies have been added by an external source.

    

    :param tmdb_id: The tmdbId.
    :type tmdb_id: str
    :param imdb_id: The imdbId.
    :type imdb_id: str

    """
    return web.Response(status=200)


async def post_added_series(request: web.Request, tvdb_id=None) -> web.Response:
    """Reports that new episodes of a series have been added by an external source.

    

    :param tvdb_id: The tvdbId.
    :type tvdb_id: str

    """
    return web.Response(status=200)


async def post_updated_media(request: web.Request, body) -> web.Response:
    """Reports that new movies have been added by an external source.

    

    :param body: A list of updated media paths.
    :type body: list | bytes

    """
    body = [MediaUpdateInfoDto.from_dict(d) for d in body]
    return web.Response(status=200)


async def post_updated_movies(request: web.Request, tmdb_id=None, imdb_id=None) -> web.Response:
    """Reports that new movies have been added by an external source.

    

    :param tmdb_id: The tmdbId.
    :type tmdb_id: str
    :param imdb_id: The imdbId.
    :type imdb_id: str

    """
    return web.Response(status=200)


async def post_updated_series(request: web.Request, tvdb_id=None) -> web.Response:
    """Reports that new episodes of a series have been added by an external source.

    

    :param tvdb_id: The tvdbId.
    :type tvdb_id: str

    """
    return web.Response(status=200)


async def refresh_library(request: web.Request, ) -> web.Response:
    """Starts a library scan.

    


    """
    return web.Response(status=200)
