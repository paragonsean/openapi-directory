from typing import List, Dict
from aiohttp import web

from openapi_server.models.base_item_dto_query_result import BaseItemDtoQueryResult
from openapi_server.models.image_type import ImageType
from openapi_server.models.item_fields import ItemFields
from openapi_server.models.item_filter import ItemFilter
from openapi_server.models.location_type import LocationType
from openapi_server.models.series_status import SeriesStatus
from openapi_server.models.video_type import VideoType
from openapi_server import util


async def get_items(request: web.Request, user_id=None, max_official_rating=None, has_theme_song=None, has_theme_video=None, has_subtitles=None, has_special_feature=None, has_trailer=None, adjacent_to=None, parent_index_number=None, has_parental_rating=None, is_hd=None, is4_k=None, location_types=None, exclude_location_types=None, is_missing=None, is_unaired=None, min_community_rating=None, min_critic_rating=None, min_premiere_date=None, min_date_last_saved=None, min_date_last_saved_for_user=None, max_premiere_date=None, has_overview=None, has_imdb_id=None, has_tmdb_id=None, has_tvdb_id=None, exclude_item_ids=None, start_index=None, limit=None, recursive=None, search_term=None, sort_order=None, parent_id=None, fields=None, exclude_item_types=None, include_item_types=None, filters=None, is_favorite=None, media_types=None, image_types=None, sort_by=None, is_played=None, genres=None, official_ratings=None, tags=None, years=None, enable_user_data=None, image_type_limit=None, enable_image_types=None, person=None, person_ids=None, person_types=None, studios=None, artists=None, exclude_artist_ids=None, artist_ids=None, album_artist_ids=None, contributing_artist_ids=None, albums=None, album_ids=None, ids=None, video_types=None, min_official_rating=None, is_locked=None, is_place_holder=None, has_official_rating=None, collapse_box_set_items=None, min_width=None, min_height=None, max_width=None, max_height=None, is3_d=None, series_status=None, name_starts_with_or_greater=None, name_starts_with=None, name_less_than=None, studio_ids=None, genre_ids=None, enable_total_record_count=None, enable_images=None) -> web.Response:
    """Gets items based on a query.

    

    :param user_id: The user id supplied as query parameter.
    :type user_id: str
    :type user_id: str
    :param max_official_rating: Optional filter by maximum official rating (PG, PG-13, TV-MA, etc).
    :type max_official_rating: str
    :param has_theme_song: Optional filter by items with theme songs.
    :type has_theme_song: bool
    :param has_theme_video: Optional filter by items with theme videos.
    :type has_theme_video: bool
    :param has_subtitles: Optional filter by items with subtitles.
    :type has_subtitles: bool
    :param has_special_feature: Optional filter by items with special features.
    :type has_special_feature: bool
    :param has_trailer: Optional filter by items with trailers.
    :type has_trailer: bool
    :param adjacent_to: Optional. Return items that are siblings of a supplied item.
    :type adjacent_to: str
    :param parent_index_number: Optional filter by parent index number.
    :type parent_index_number: int
    :param has_parental_rating: Optional filter by items that have or do not have a parental rating.
    :type has_parental_rating: bool
    :param is_hd: Optional filter by items that are HD or not.
    :type is_hd: bool
    :param is4_k: Optional filter by items that are 4K or not.
    :type is4_k: bool
    :param location_types: Optional. If specified, results will be filtered based on LocationType. This allows multiple, comma delimited.
    :type location_types: list | bytes
    :param exclude_location_types: Optional. If specified, results will be filtered based on the LocationType. This allows multiple, comma delimited.
    :type exclude_location_types: list | bytes
    :param is_missing: Optional filter by items that are missing episodes or not.
    :type is_missing: bool
    :param is_unaired: Optional filter by items that are unaired episodes or not.
    :type is_unaired: bool
    :param min_community_rating: Optional filter by minimum community rating.
    :type min_community_rating: float
    :param min_critic_rating: Optional filter by minimum critic rating.
    :type min_critic_rating: float
    :param min_premiere_date: Optional. The minimum premiere date. Format &#x3D; ISO.
    :type min_premiere_date: str
    :param min_date_last_saved: Optional. The minimum last saved date. Format &#x3D; ISO.
    :type min_date_last_saved: str
    :param min_date_last_saved_for_user: Optional. The minimum last saved date for the current user. Format &#x3D; ISO.
    :type min_date_last_saved_for_user: str
    :param max_premiere_date: Optional. The maximum premiere date. Format &#x3D; ISO.
    :type max_premiere_date: str
    :param has_overview: Optional filter by items that have an overview or not.
    :type has_overview: bool
    :param has_imdb_id: Optional filter by items that have an imdb id or not.
    :type has_imdb_id: bool
    :param has_tmdb_id: Optional filter by items that have a tmdb id or not.
    :type has_tmdb_id: bool
    :param has_tvdb_id: Optional filter by items that have a tvdb id or not.
    :type has_tvdb_id: bool
    :param exclude_item_ids: Optional. If specified, results will be filtered by excluding item ids. This allows multiple, comma delimited.
    :type exclude_item_ids: List[str]
    :param start_index: Optional. The record index to start at. All items with a lower index will be dropped from the results.
    :type start_index: int
    :param limit: Optional. The maximum number of records to return.
    :type limit: int
    :param recursive: When searching within folders, this determines whether or not the search will be recursive. true/false.
    :type recursive: bool
    :param search_term: Optional. Filter based on a search term.
    :type search_term: str
    :param sort_order: Sort Order - Ascending,Descending.
    :type sort_order: str
    :param parent_id: Specify this to localize the search to a specific item or folder. Omit to use the root.
    :type parent_id: str
    :type parent_id: str
    :param fields: Optional. Specify additional fields of information to return in the output. This allows multiple, comma delimited. Options: Budget, Chapters, DateCreated, Genres, HomePageUrl, IndexOptions, MediaStreams, Overview, ParentId, Path, People, ProviderIds, PrimaryImageAspectRatio, Revenue, SortName, Studios, Taglines.
    :type fields: list | bytes
    :param exclude_item_types: Optional. If specified, results will be filtered based on item type. This allows multiple, comma delimited.
    :type exclude_item_types: List[str]
    :param include_item_types: Optional. If specified, results will be filtered based on the item type. This allows multiple, comma delimited.
    :type include_item_types: List[str]
    :param filters: Optional. Specify additional filters to apply. This allows multiple, comma delimited. Options: IsFolder, IsNotFolder, IsUnplayed, IsPlayed, IsFavorite, IsResumable, Likes, Dislikes.
    :type filters: list | bytes
    :param is_favorite: Optional filter by items that are marked as favorite, or not.
    :type is_favorite: bool
    :param media_types: Optional filter by MediaType. Allows multiple, comma delimited.
    :type media_types: List[str]
    :param image_types: Optional. If specified, results will be filtered based on those containing image types. This allows multiple, comma delimited.
    :type image_types: list | bytes
    :param sort_by: Optional. Specify one or more sort orders, comma delimited. Options: Album, AlbumArtist, Artist, Budget, CommunityRating, CriticRating, DateCreated, DatePlayed, PlayCount, PremiereDate, ProductionYear, SortName, Random, Revenue, Runtime.
    :type sort_by: str
    :param is_played: Optional filter by items that are played, or not.
    :type is_played: bool
    :param genres: Optional. If specified, results will be filtered based on genre. This allows multiple, pipe delimited.
    :type genres: List[str]
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
    :param person_ids: Optional. If specified, results will be filtered to include only those containing the specified person id.
    :type person_ids: List[str]
    :param person_types: Optional. If specified, along with Person, results will be filtered to include only those containing the specified person and PersonType. Allows multiple, comma-delimited.
    :type person_types: List[str]
    :param studios: Optional. If specified, results will be filtered based on studio. This allows multiple, pipe delimited.
    :type studios: List[str]
    :param artists: Optional. If specified, results will be filtered based on artists. This allows multiple, pipe delimited.
    :type artists: List[str]
    :param exclude_artist_ids: Optional. If specified, results will be filtered based on artist id. This allows multiple, pipe delimited.
    :type exclude_artist_ids: List[str]
    :param artist_ids: Optional. If specified, results will be filtered to include only those containing the specified artist id.
    :type artist_ids: List[str]
    :param album_artist_ids: Optional. If specified, results will be filtered to include only those containing the specified album artist id.
    :type album_artist_ids: List[str]
    :param contributing_artist_ids: Optional. If specified, results will be filtered to include only those containing the specified contributing artist id.
    :type contributing_artist_ids: List[str]
    :param albums: Optional. If specified, results will be filtered based on album. This allows multiple, pipe delimited.
    :type albums: List[str]
    :param album_ids: Optional. If specified, results will be filtered based on album id. This allows multiple, pipe delimited.
    :type album_ids: List[str]
    :param ids: Optional. If specific items are needed, specify a list of item id&#39;s to retrieve. This allows multiple, comma delimited.
    :type ids: List[str]
    :param video_types: Optional filter by VideoType (videofile, dvd, bluray, iso). Allows multiple, comma delimited.
    :type video_types: list | bytes
    :param min_official_rating: Optional filter by minimum official rating (PG, PG-13, TV-MA, etc).
    :type min_official_rating: str
    :param is_locked: Optional filter by items that are locked.
    :type is_locked: bool
    :param is_place_holder: Optional filter by items that are placeholders.
    :type is_place_holder: bool
    :param has_official_rating: Optional filter by items that have official ratings.
    :type has_official_rating: bool
    :param collapse_box_set_items: Whether or not to hide items behind their boxsets.
    :type collapse_box_set_items: bool
    :param min_width: Optional. Filter by the minimum width of the item.
    :type min_width: int
    :param min_height: Optional. Filter by the minimum height of the item.
    :type min_height: int
    :param max_width: Optional. Filter by the maximum width of the item.
    :type max_width: int
    :param max_height: Optional. Filter by the maximum height of the item.
    :type max_height: int
    :param is3_d: Optional filter by items that are 3D, or not.
    :type is3_d: bool
    :param series_status: Optional filter by Series Status. Allows multiple, comma delimited.
    :type series_status: list | bytes
    :param name_starts_with_or_greater: Optional filter by items whose name is sorted equally or greater than a given input string.
    :type name_starts_with_or_greater: str
    :param name_starts_with: Optional filter by items whose name is sorted equally than a given input string.
    :type name_starts_with: str
    :param name_less_than: Optional filter by items whose name is equally or lesser than a given input string.
    :type name_less_than: str
    :param studio_ids: Optional. If specified, results will be filtered based on studio id. This allows multiple, pipe delimited.
    :type studio_ids: List[str]
    :param genre_ids: Optional. If specified, results will be filtered based on genre id. This allows multiple, pipe delimited.
    :type genre_ids: List[str]
    :param enable_total_record_count: Optional. Enable the total record count.
    :type enable_total_record_count: bool
    :param enable_images: Optional, include image information in output.
    :type enable_images: bool

    """
    location_types = [LocationType.from_dict(d) for d in location_types]
    exclude_location_types = [LocationType.from_dict(d) for d in exclude_location_types]
    min_premiere_date = util.deserialize_datetime(min_premiere_date)
    min_date_last_saved = util.deserialize_datetime(min_date_last_saved)
    min_date_last_saved_for_user = util.deserialize_datetime(min_date_last_saved_for_user)
    max_premiere_date = util.deserialize_datetime(max_premiere_date)
    fields = [ItemFields.from_dict(d) for d in fields]
    filters = [ItemFilter.from_dict(d) for d in filters]
    image_types = [ImageType.from_dict(d) for d in image_types]
    enable_image_types = [ImageType.from_dict(d) for d in enable_image_types]
    video_types = [VideoType.from_dict(d) for d in video_types]
    series_status = [SeriesStatus.from_dict(d) for d in series_status]
    return web.Response(status=200)


async def get_items_by_user_id(request: web.Request, user_id, max_official_rating=None, has_theme_song=None, has_theme_video=None, has_subtitles=None, has_special_feature=None, has_trailer=None, adjacent_to=None, parent_index_number=None, has_parental_rating=None, is_hd=None, is4_k=None, location_types=None, exclude_location_types=None, is_missing=None, is_unaired=None, min_community_rating=None, min_critic_rating=None, min_premiere_date=None, min_date_last_saved=None, min_date_last_saved_for_user=None, max_premiere_date=None, has_overview=None, has_imdb_id=None, has_tmdb_id=None, has_tvdb_id=None, exclude_item_ids=None, start_index=None, limit=None, recursive=None, search_term=None, sort_order=None, parent_id=None, fields=None, exclude_item_types=None, include_item_types=None, filters=None, is_favorite=None, media_types=None, image_types=None, sort_by=None, is_played=None, genres=None, official_ratings=None, tags=None, years=None, enable_user_data=None, image_type_limit=None, enable_image_types=None, person=None, person_ids=None, person_types=None, studios=None, artists=None, exclude_artist_ids=None, artist_ids=None, album_artist_ids=None, contributing_artist_ids=None, albums=None, album_ids=None, ids=None, video_types=None, min_official_rating=None, is_locked=None, is_place_holder=None, has_official_rating=None, collapse_box_set_items=None, min_width=None, min_height=None, max_width=None, max_height=None, is3_d=None, series_status=None, name_starts_with_or_greater=None, name_starts_with=None, name_less_than=None, studio_ids=None, genre_ids=None, enable_total_record_count=None, enable_images=None) -> web.Response:
    """Gets items based on a query.

    

    :param user_id: The user id supplied as query parameter.
    :type user_id: str
    :type user_id: str
    :param max_official_rating: Optional filter by maximum official rating (PG, PG-13, TV-MA, etc).
    :type max_official_rating: str
    :param has_theme_song: Optional filter by items with theme songs.
    :type has_theme_song: bool
    :param has_theme_video: Optional filter by items with theme videos.
    :type has_theme_video: bool
    :param has_subtitles: Optional filter by items with subtitles.
    :type has_subtitles: bool
    :param has_special_feature: Optional filter by items with special features.
    :type has_special_feature: bool
    :param has_trailer: Optional filter by items with trailers.
    :type has_trailer: bool
    :param adjacent_to: Optional. Return items that are siblings of a supplied item.
    :type adjacent_to: str
    :param parent_index_number: Optional filter by parent index number.
    :type parent_index_number: int
    :param has_parental_rating: Optional filter by items that have or do not have a parental rating.
    :type has_parental_rating: bool
    :param is_hd: Optional filter by items that are HD or not.
    :type is_hd: bool
    :param is4_k: Optional filter by items that are 4K or not.
    :type is4_k: bool
    :param location_types: Optional. If specified, results will be filtered based on LocationType. This allows multiple, comma delimeted.
    :type location_types: list | bytes
    :param exclude_location_types: Optional. If specified, results will be filtered based on the LocationType. This allows multiple, comma delimeted.
    :type exclude_location_types: list | bytes
    :param is_missing: Optional filter by items that are missing episodes or not.
    :type is_missing: bool
    :param is_unaired: Optional filter by items that are unaired episodes or not.
    :type is_unaired: bool
    :param min_community_rating: Optional filter by minimum community rating.
    :type min_community_rating: float
    :param min_critic_rating: Optional filter by minimum critic rating.
    :type min_critic_rating: float
    :param min_premiere_date: Optional. The minimum premiere date. Format &#x3D; ISO.
    :type min_premiere_date: str
    :param min_date_last_saved: Optional. The minimum last saved date. Format &#x3D; ISO.
    :type min_date_last_saved: str
    :param min_date_last_saved_for_user: Optional. The minimum last saved date for the current user. Format &#x3D; ISO.
    :type min_date_last_saved_for_user: str
    :param max_premiere_date: Optional. The maximum premiere date. Format &#x3D; ISO.
    :type max_premiere_date: str
    :param has_overview: Optional filter by items that have an overview or not.
    :type has_overview: bool
    :param has_imdb_id: Optional filter by items that have an imdb id or not.
    :type has_imdb_id: bool
    :param has_tmdb_id: Optional filter by items that have a tmdb id or not.
    :type has_tmdb_id: bool
    :param has_tvdb_id: Optional filter by items that have a tvdb id or not.
    :type has_tvdb_id: bool
    :param exclude_item_ids: Optional. If specified, results will be filtered by exxcluding item ids. This allows multiple, comma delimeted.
    :type exclude_item_ids: List[str]
    :param start_index: Optional. The record index to start at. All items with a lower index will be dropped from the results.
    :type start_index: int
    :param limit: Optional. The maximum number of records to return.
    :type limit: int
    :param recursive: When searching within folders, this determines whether or not the search will be recursive. true/false.
    :type recursive: bool
    :param search_term: Optional. Filter based on a search term.
    :type search_term: str
    :param sort_order: Sort Order - Ascending,Descending.
    :type sort_order: str
    :param parent_id: Specify this to localize the search to a specific item or folder. Omit to use the root.
    :type parent_id: str
    :type parent_id: str
    :param fields: Optional. Specify additional fields of information to return in the output. This allows multiple, comma delimeted. Options: Budget, Chapters, DateCreated, Genres, HomePageUrl, IndexOptions, MediaStreams, Overview, ParentId, Path, People, ProviderIds, PrimaryImageAspectRatio, Revenue, SortName, Studios, Taglines.
    :type fields: list | bytes
    :param exclude_item_types: Optional. If specified, results will be filtered based on item type. This allows multiple, comma delimeted.
    :type exclude_item_types: List[str]
    :param include_item_types: Optional. If specified, results will be filtered based on the item type. This allows multiple, comma delimeted.
    :type include_item_types: List[str]
    :param filters: Optional. Specify additional filters to apply. This allows multiple, comma delimeted. Options: IsFolder, IsNotFolder, IsUnplayed, IsPlayed, IsFavorite, IsResumable, Likes, Dislikes.
    :type filters: list | bytes
    :param is_favorite: Optional filter by items that are marked as favorite, or not.
    :type is_favorite: bool
    :param media_types: Optional filter by MediaType. Allows multiple, comma delimited.
    :type media_types: List[str]
    :param image_types: Optional. If specified, results will be filtered based on those containing image types. This allows multiple, comma delimited.
    :type image_types: list | bytes
    :param sort_by: Optional. Specify one or more sort orders, comma delimeted. Options: Album, AlbumArtist, Artist, Budget, CommunityRating, CriticRating, DateCreated, DatePlayed, PlayCount, PremiereDate, ProductionYear, SortName, Random, Revenue, Runtime.
    :type sort_by: str
    :param is_played: Optional filter by items that are played, or not.
    :type is_played: bool
    :param genres: Optional. If specified, results will be filtered based on genre. This allows multiple, pipe delimeted.
    :type genres: List[str]
    :param official_ratings: Optional. If specified, results will be filtered based on OfficialRating. This allows multiple, pipe delimeted.
    :type official_ratings: List[str]
    :param tags: Optional. If specified, results will be filtered based on tag. This allows multiple, pipe delimeted.
    :type tags: List[str]
    :param years: Optional. If specified, results will be filtered based on production year. This allows multiple, comma delimeted.
    :type years: List[int]
    :param enable_user_data: Optional, include user data.
    :type enable_user_data: bool
    :param image_type_limit: Optional, the max number of images to return, per image type.
    :type image_type_limit: int
    :param enable_image_types: Optional. The image types to include in the output.
    :type enable_image_types: list | bytes
    :param person: Optional. If specified, results will be filtered to include only those containing the specified person.
    :type person: str
    :param person_ids: Optional. If specified, results will be filtered to include only those containing the specified person id.
    :type person_ids: List[str]
    :param person_types: Optional. If specified, along with Person, results will be filtered to include only those containing the specified person and PersonType. Allows multiple, comma-delimited.
    :type person_types: List[str]
    :param studios: Optional. If specified, results will be filtered based on studio. This allows multiple, pipe delimeted.
    :type studios: List[str]
    :param artists: Optional. If specified, results will be filtered based on artists. This allows multiple, pipe delimeted.
    :type artists: List[str]
    :param exclude_artist_ids: Optional. If specified, results will be filtered based on artist id. This allows multiple, pipe delimeted.
    :type exclude_artist_ids: List[str]
    :param artist_ids: Optional. If specified, results will be filtered to include only those containing the specified artist id.
    :type artist_ids: List[str]
    :param album_artist_ids: Optional. If specified, results will be filtered to include only those containing the specified album artist id.
    :type album_artist_ids: List[str]
    :param contributing_artist_ids: Optional. If specified, results will be filtered to include only those containing the specified contributing artist id.
    :type contributing_artist_ids: List[str]
    :param albums: Optional. If specified, results will be filtered based on album. This allows multiple, pipe delimeted.
    :type albums: List[str]
    :param album_ids: Optional. If specified, results will be filtered based on album id. This allows multiple, pipe delimeted.
    :type album_ids: List[str]
    :param ids: Optional. If specific items are needed, specify a list of item id&#39;s to retrieve. This allows multiple, comma delimited.
    :type ids: List[str]
    :param video_types: Optional filter by VideoType (videofile, dvd, bluray, iso). Allows multiple, comma delimeted.
    :type video_types: list | bytes
    :param min_official_rating: Optional filter by minimum official rating (PG, PG-13, TV-MA, etc).
    :type min_official_rating: str
    :param is_locked: Optional filter by items that are locked.
    :type is_locked: bool
    :param is_place_holder: Optional filter by items that are placeholders.
    :type is_place_holder: bool
    :param has_official_rating: Optional filter by items that have official ratings.
    :type has_official_rating: bool
    :param collapse_box_set_items: Whether or not to hide items behind their boxsets.
    :type collapse_box_set_items: bool
    :param min_width: Optional. Filter by the minimum width of the item.
    :type min_width: int
    :param min_height: Optional. Filter by the minimum height of the item.
    :type min_height: int
    :param max_width: Optional. Filter by the maximum width of the item.
    :type max_width: int
    :param max_height: Optional. Filter by the maximum height of the item.
    :type max_height: int
    :param is3_d: Optional filter by items that are 3D, or not.
    :type is3_d: bool
    :param series_status: Optional filter by Series Status. Allows multiple, comma delimeted.
    :type series_status: list | bytes
    :param name_starts_with_or_greater: Optional filter by items whose name is sorted equally or greater than a given input string.
    :type name_starts_with_or_greater: str
    :param name_starts_with: Optional filter by items whose name is sorted equally than a given input string.
    :type name_starts_with: str
    :param name_less_than: Optional filter by items whose name is equally or lesser than a given input string.
    :type name_less_than: str
    :param studio_ids: Optional. If specified, results will be filtered based on studio id. This allows multiple, pipe delimeted.
    :type studio_ids: List[str]
    :param genre_ids: Optional. If specified, results will be filtered based on genre id. This allows multiple, pipe delimeted.
    :type genre_ids: List[str]
    :param enable_total_record_count: Optional. Enable the total record count.
    :type enable_total_record_count: bool
    :param enable_images: Optional, include image information in output.
    :type enable_images: bool

    """
    location_types = [LocationType.from_dict(d) for d in location_types]
    exclude_location_types = [LocationType.from_dict(d) for d in exclude_location_types]
    min_premiere_date = util.deserialize_datetime(min_premiere_date)
    min_date_last_saved = util.deserialize_datetime(min_date_last_saved)
    min_date_last_saved_for_user = util.deserialize_datetime(min_date_last_saved_for_user)
    max_premiere_date = util.deserialize_datetime(max_premiere_date)
    fields = [ItemFields.from_dict(d) for d in fields]
    filters = [ItemFilter.from_dict(d) for d in filters]
    image_types = [ImageType.from_dict(d) for d in image_types]
    enable_image_types = [ImageType.from_dict(d) for d in enable_image_types]
    video_types = [VideoType.from_dict(d) for d in video_types]
    series_status = [SeriesStatus.from_dict(d) for d in series_status]
    return web.Response(status=200)


async def get_resume_items(request: web.Request, user_id, start_index=None, limit=None, search_term=None, parent_id=None, fields=None, media_types=None, enable_user_data=None, image_type_limit=None, enable_image_types=None, exclude_item_types=None, include_item_types=None, enable_total_record_count=None, enable_images=None) -> web.Response:
    """Gets items based on a query.

    

    :param user_id: The user id.
    :type user_id: str
    :type user_id: str
    :param start_index: The start index.
    :type start_index: int
    :param limit: The item limit.
    :type limit: int
    :param search_term: The search term.
    :type search_term: str
    :param parent_id: Specify this to localize the search to a specific item or folder. Omit to use the root.
    :type parent_id: str
    :type parent_id: str
    :param fields: Optional. Specify additional fields of information to return in the output. This allows multiple, comma delimited. Options: Budget, Chapters, DateCreated, Genres, HomePageUrl, IndexOptions, MediaStreams, Overview, ParentId, Path, People, ProviderIds, PrimaryImageAspectRatio, Revenue, SortName, Studios, Taglines.
    :type fields: list | bytes
    :param media_types: Optional. Filter by MediaType. Allows multiple, comma delimited.
    :type media_types: List[str]
    :param enable_user_data: Optional. Include user data.
    :type enable_user_data: bool
    :param image_type_limit: Optional. The max number of images to return, per image type.
    :type image_type_limit: int
    :param enable_image_types: Optional. The image types to include in the output.
    :type enable_image_types: list | bytes
    :param exclude_item_types: Optional. If specified, results will be filtered based on item type. This allows multiple, comma delimited.
    :type exclude_item_types: List[str]
    :param include_item_types: Optional. If specified, results will be filtered based on the item type. This allows multiple, comma delimited.
    :type include_item_types: List[str]
    :param enable_total_record_count: Optional. Enable the total record count.
    :type enable_total_record_count: bool
    :param enable_images: Optional. Include image information in output.
    :type enable_images: bool

    """
    fields = [ItemFields.from_dict(d) for d in fields]
    enable_image_types = [ImageType.from_dict(d) for d in enable_image_types]
    return web.Response(status=200)
