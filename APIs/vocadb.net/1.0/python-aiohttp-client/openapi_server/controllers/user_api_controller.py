from typing import List, Dict
from aiohttp import web

from openapi_server.models.advanced_search_filter_params import AdvancedSearchFilterParams
from openapi_server.models.album_for_user_for_api_contract import AlbumForUserForApiContract
from openapi_server.models.album_for_user_for_api_contract_partial_find_result import AlbumForUserForApiContractPartialFindResult
from openapi_server.models.album_optional_fields import AlbumOptionalFields
from openapi_server.models.album_sort_rule import AlbumSortRule
from openapi_server.models.artist_for_user_for_api_contract import ArtistForUserForApiContract
from openapi_server.models.artist_for_user_for_api_contract_partial_find_result import ArtistForUserForApiContractPartialFindResult
from openapi_server.models.artist_optional_fields import ArtistOptionalFields
from openapi_server.models.artist_sort_rule import ArtistSortRule
from openapi_server.models.artist_type import ArtistType
from openapi_server.models.comment_for_api_contract import CommentForApiContract
from openapi_server.models.comment_for_api_contract_partial_find_result import CommentForApiContractPartialFindResult
from openapi_server.models.content_language_preference import ContentLanguagePreference
from openapi_server.models.create_report_model import CreateReportModel
from openapi_server.models.disc_type import DiscType
from openapi_server.models.entry_edit_data_contract import EntryEditDataContract
from openapi_server.models.entry_type import EntryType
from openapi_server.models.logical_grouping import LogicalGrouping
from openapi_server.models.media_type import MediaType
from openapi_server.models.name_match_mode import NameMatchMode
from openapi_server.models.pv_services import PVServices
from openapi_server.models.purchase_status import PurchaseStatus
from openapi_server.models.purchase_statuses import PurchaseStatuses
from openapi_server.models.rated_song_for_user_for_api_contract_partial_find_result import RatedSongForUserForApiContractPartialFindResult
from openapi_server.models.rated_song_for_user_sort_rule import RatedSongForUserSortRule
from openapi_server.models.release_event_for_api_contract import ReleaseEventForApiContract
from openapi_server.models.song_list_for_api_contract_partial_find_result import SongListForApiContractPartialFindResult
from openapi_server.models.song_list_optional_fields import SongListOptionalFields
from openapi_server.models.song_list_sort_rule import SongListSortRule
from openapi_server.models.song_optional_fields import SongOptionalFields
from openapi_server.models.song_vote_rating import SongVoteRating
from openapi_server.models.user_event_relationship_type import UserEventRelationshipType
from openapi_server.models.user_for_api_contract import UserForApiContract
from openapi_server.models.user_for_api_contract_partial_find_result import UserForApiContractPartialFindResult
from openapi_server.models.user_group_id import UserGroupId
from openapi_server.models.user_inbox_type import UserInboxType
from openapi_server.models.user_message_contract import UserMessageContract
from openapi_server.models.user_message_contract_partial_find_result import UserMessageContractPartialFindResult
from openapi_server.models.user_optional_fields import UserOptionalFields
from openapi_server.models.user_sort_rule import UserSortRule
from openapi_server import util


async def api_users_current_album_collection_statuses_album_id_get(request: web.Request, album_id) -> web.Response:
    """api_users_current_album_collection_statuses_album_id_get

    

    :param album_id: 
    :type album_id: int

    """
    return web.Response(status=200)


async def api_users_current_albums_album_id_post(request: web.Request, album_id, collection_status=None, media_type=None, rating=None) -> web.Response:
    """api_users_current_albums_album_id_post

    

    :param album_id: 
    :type album_id: int
    :param collection_status: 
    :type collection_status: dict | bytes
    :param media_type: 
    :type media_type: dict | bytes
    :param rating: 
    :type rating: int

    """
    collection_status = .from_dict(collection_status)
    media_type = .from_dict(media_type)
    return web.Response(status=200)


async def api_users_current_followed_artists_artist_id_get(request: web.Request, artist_id) -> web.Response:
    """api_users_current_followed_artists_artist_id_get

    

    :param artist_id: 
    :type artist_id: int

    """
    return web.Response(status=200)


async def api_users_current_followed_tags_tag_id_delete(request: web.Request, tag_id) -> web.Response:
    """api_users_current_followed_tags_tag_id_delete

    

    :param tag_id: 
    :type tag_id: int

    """
    return web.Response(status=200)


async def api_users_current_followed_tags_tag_id_post(request: web.Request, tag_id) -> web.Response:
    """api_users_current_followed_tags_tag_id_post

    

    :param tag_id: 
    :type tag_id: int

    """
    return web.Response(status=200)


async def api_users_current_get(request: web.Request, fields=None) -> web.Response:
    """api_users_current_get

    

    :param fields: 
    :type fields: dict | bytes

    """
    fields = .from_dict(fields)
    return web.Response(status=200)


async def api_users_current_rated_songs_song_id_get(request: web.Request, song_id) -> web.Response:
    """api_users_current_rated_songs_song_id_get

    

    :param song_id: 
    :type song_id: int

    """
    return web.Response(status=200)


async def api_users_current_refresh_entry_edit_post(request: web.Request, entry_type=None, entry_id=None) -> web.Response:
    """api_users_current_refresh_entry_edit_post

    

    :param entry_type: 
    :type entry_type: dict | bytes
    :param entry_id: 
    :type entry_id: int

    """
    entry_type = .from_dict(entry_type)
    return web.Response(status=200)


async def api_users_current_song_tags_song_id_post(request: web.Request, song_id) -> web.Response:
    """api_users_current_song_tags_song_id_post

    

    :param song_id: 
    :type song_id: int

    """
    return web.Response(status=200)


async def api_users_get(request: web.Request, query=None, groups=None, join_date_after=None, join_date_before=None, name_match_mode=None, start=None, max_results=None, get_total_count=None, sort=None, include_disabled=None, only_verified=None, knows_language=None, fields=None) -> web.Response:
    """api_users_get

    

    :param query: 
    :type query: str
    :param groups: 
    :type groups: dict | bytes
    :param join_date_after: 
    :type join_date_after: str
    :param join_date_before: 
    :type join_date_before: str
    :param name_match_mode: 
    :type name_match_mode: dict | bytes
    :param start: 
    :type start: int
    :param max_results: 
    :type max_results: int
    :param get_total_count: 
    :type get_total_count: bool
    :param sort: 
    :type sort: dict | bytes
    :param include_disabled: 
    :type include_disabled: bool
    :param only_verified: 
    :type only_verified: bool
    :param knows_language: 
    :type knows_language: str
    :param fields: 
    :type fields: dict | bytes

    """
    groups = .from_dict(groups)
    join_date_after = util.deserialize_datetime(join_date_after)
    join_date_before = util.deserialize_datetime(join_date_before)
    name_match_mode = .from_dict(name_match_mode)
    sort = .from_dict(sort)
    fields = .from_dict(fields)
    return web.Response(status=200)


async def api_users_id_album_collection_statuses_album_id_get(request: web.Request, id, album_id) -> web.Response:
    """api_users_id_album_collection_statuses_album_id_get

    

    :param id: 
    :type id: int
    :param album_id: 
    :type album_id: int

    """
    return web.Response(status=200)


async def api_users_id_albums_get(request: web.Request, id, query=None, tag_id=None, tag=None, artist_id=None, purchase_statuses=None, release_event_id=None, album_types=None, advanced_filters=None, start=None, max_results=None, get_total_count=None, sort=None, name_match_mode=None, fields=None, lang=None, media_type=None) -> web.Response:
    """api_users_id_albums_get

    

    :param id: 
    :type id: int
    :param query: 
    :type query: str
    :param tag_id: 
    :type tag_id: int
    :param tag: 
    :type tag: str
    :param artist_id: 
    :type artist_id: int
    :param purchase_statuses: 
    :type purchase_statuses: dict | bytes
    :param release_event_id: 
    :type release_event_id: int
    :param album_types: 
    :type album_types: dict | bytes
    :param advanced_filters: 
    :type advanced_filters: list | bytes
    :param start: 
    :type start: int
    :param max_results: 
    :type max_results: int
    :param get_total_count: 
    :type get_total_count: bool
    :param sort: 
    :type sort: dict | bytes
    :param name_match_mode: 
    :type name_match_mode: dict | bytes
    :param fields: 
    :type fields: dict | bytes
    :param lang: 
    :type lang: dict | bytes
    :param media_type: 
    :type media_type: dict | bytes

    """
    purchase_statuses = .from_dict(purchase_statuses)
    album_types = .from_dict(album_types)
    advanced_filters = [AdvancedSearchFilterParams.from_dict(d) for d in advanced_filters]
    sort = .from_dict(sort)
    name_match_mode = .from_dict(name_match_mode)
    fields = .from_dict(fields)
    lang = .from_dict(lang)
    media_type = .from_dict(media_type)
    return web.Response(status=200)


async def api_users_id_events_get(request: web.Request, id, relationship_type=None) -> web.Response:
    """api_users_id_events_get

    

    :param id: 
    :type id: int
    :param relationship_type: 
    :type relationship_type: dict | bytes

    """
    relationship_type = .from_dict(relationship_type)
    return web.Response(status=200)


async def api_users_id_followed_artists_artist_id_get(request: web.Request, id, artist_id) -> web.Response:
    """api_users_id_followed_artists_artist_id_get

    

    :param id: 
    :type id: int
    :param artist_id: 
    :type artist_id: int

    """
    return web.Response(status=200)


async def api_users_id_followed_artists_get(request: web.Request, id, query=None, tag_id=None, artist_type=None, start=None, max_results=None, get_total_count=None, sort=None, name_match_mode=None, fields=None, lang=None) -> web.Response:
    """api_users_id_followed_artists_get

    

    :param id: 
    :type id: int
    :param query: 
    :type query: str
    :param tag_id: 
    :type tag_id: List[int]
    :param artist_type: 
    :type artist_type: dict | bytes
    :param start: 
    :type start: int
    :param max_results: 
    :type max_results: int
    :param get_total_count: 
    :type get_total_count: bool
    :param sort: 
    :type sort: dict | bytes
    :param name_match_mode: 
    :type name_match_mode: dict | bytes
    :param fields: 
    :type fields: dict | bytes
    :param lang: 
    :type lang: dict | bytes

    """
    artist_type = .from_dict(artist_type)
    sort = .from_dict(sort)
    name_match_mode = .from_dict(name_match_mode)
    fields = .from_dict(fields)
    lang = .from_dict(lang)
    return web.Response(status=200)


async def api_users_id_get(request: web.Request, id, fields=None) -> web.Response:
    """api_users_id_get

    

    :param id: 
    :type id: int
    :param fields: 
    :type fields: dict | bytes

    """
    fields = .from_dict(fields)
    return web.Response(status=200)


async def api_users_id_messages_delete(request: web.Request, id, message_id=None) -> web.Response:
    """api_users_id_messages_delete

    

    :param id: 
    :type id: int
    :param message_id: 
    :type message_id: List[int]

    """
    return web.Response(status=200)


async def api_users_id_messages_get(request: web.Request, id, inbox=None, unread=None, another_user_id=None, start=None, max_results=None, get_total_count=None) -> web.Response:
    """api_users_id_messages_get

    

    :param id: 
    :type id: int
    :param inbox: 
    :type inbox: dict | bytes
    :param unread: 
    :type unread: bool
    :param another_user_id: 
    :type another_user_id: int
    :param start: 
    :type start: int
    :param max_results: 
    :type max_results: int
    :param get_total_count: 
    :type get_total_count: bool

    """
    inbox = .from_dict(inbox)
    return web.Response(status=200)


async def api_users_id_messages_post(request: web.Request, id, body=None) -> web.Response:
    """api_users_id_messages_post

    

    :param id: 
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = UserMessageContract.from_dict(body)
    return web.Response(status=200)


async def api_users_id_profile_comments_get(request: web.Request, id, start=None, max_results=None, get_total_count=None) -> web.Response:
    """api_users_id_profile_comments_get

    

    :param id: 
    :type id: int
    :param start: 
    :type start: int
    :param max_results: 
    :type max_results: int
    :param get_total_count: 
    :type get_total_count: bool

    """
    return web.Response(status=200)


async def api_users_id_profile_comments_post(request: web.Request, id, body=None) -> web.Response:
    """api_users_id_profile_comments_post

    

    :param id: 
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = CommentForApiContract.from_dict(body)
    return web.Response(status=200)


async def api_users_id_rated_songs_get(request: web.Request, id, query=None, tag_name=None, tag_id=None, artist_id=None, child_voicebanks=None, artist_grouping=None, rating=None, song_list_id=None, group_by_rating=None, pv_services=None, advanced_filters=None, start=None, max_results=None, get_total_count=None, sort=None, name_match_mode=None, fields=None, lang=None) -> web.Response:
    """api_users_id_rated_songs_get

    

    :param id: 
    :type id: int
    :param query: 
    :type query: str
    :param tag_name: 
    :type tag_name: str
    :param tag_id: 
    :type tag_id: List[int]
    :param artist_id: 
    :type artist_id: List[int]
    :param child_voicebanks: 
    :type child_voicebanks: bool
    :param artist_grouping: 
    :type artist_grouping: dict | bytes
    :param rating: 
    :type rating: dict | bytes
    :param song_list_id: 
    :type song_list_id: int
    :param group_by_rating: 
    :type group_by_rating: bool
    :param pv_services: 
    :type pv_services: dict | bytes
    :param advanced_filters: 
    :type advanced_filters: list | bytes
    :param start: 
    :type start: int
    :param max_results: 
    :type max_results: int
    :param get_total_count: 
    :type get_total_count: bool
    :param sort: 
    :type sort: dict | bytes
    :param name_match_mode: 
    :type name_match_mode: dict | bytes
    :param fields: 
    :type fields: dict | bytes
    :param lang: 
    :type lang: dict | bytes

    """
    artist_grouping = .from_dict(artist_grouping)
    rating = .from_dict(rating)
    pv_services = .from_dict(pv_services)
    advanced_filters = [AdvancedSearchFilterParams.from_dict(d) for d in advanced_filters]
    sort = .from_dict(sort)
    name_match_mode = .from_dict(name_match_mode)
    fields = .from_dict(fields)
    lang = .from_dict(lang)
    return web.Response(status=200)


async def api_users_id_rated_songs_song_id_get(request: web.Request, id, song_id) -> web.Response:
    """api_users_id_rated_songs_song_id_get

    

    :param id: 
    :type id: int
    :param song_id: 
    :type song_id: int

    """
    return web.Response(status=200)


async def api_users_id_reports_post(request: web.Request, id, body=None) -> web.Response:
    """api_users_id_reports_post

    

    :param id: 
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = CreateReportModel.from_dict(body)
    return web.Response(status=200)


async def api_users_id_settings_setting_name_post(request: web.Request, id, setting_name, body=None) -> web.Response:
    """api_users_id_settings_setting_name_post

    

    :param id: 
    :type id: int
    :param setting_name: 
    :type setting_name: str
    :param body: 
    :type body: str

    """
    return web.Response(status=200)


async def api_users_id_song_lists_get(request: web.Request, id, query=None, tag_id=None, child_tags=None, name_match_mode=None, start=None, max_results=None, get_total_count=None, sort=None, fields=None) -> web.Response:
    """api_users_id_song_lists_get

    

    :param id: 
    :type id: int
    :param query: 
    :type query: str
    :param tag_id: 
    :type tag_id: List[int]
    :param child_tags: 
    :type child_tags: bool
    :param name_match_mode: 
    :type name_match_mode: dict | bytes
    :param start: 
    :type start: int
    :param max_results: 
    :type max_results: int
    :param get_total_count: 
    :type get_total_count: bool
    :param sort: 
    :type sort: dict | bytes
    :param fields: 
    :type fields: dict | bytes

    """
    name_match_mode = .from_dict(name_match_mode)
    sort = .from_dict(sort)
    fields = .from_dict(fields)
    return web.Response(status=200)


async def api_users_messages_message_id_get(request: web.Request, message_id) -> web.Response:
    """api_users_messages_message_id_get

    

    :param message_id: 
    :type message_id: int

    """
    return web.Response(status=200)


async def api_users_names_get(request: web.Request, query=None, name_match_mode=None, max_results=None, include_disabled=None) -> web.Response:
    """api_users_names_get

    

    :param query: 
    :type query: str
    :param name_match_mode: 
    :type name_match_mode: dict | bytes
    :param max_results: 
    :type max_results: int
    :param include_disabled: 
    :type include_disabled: bool

    """
    name_match_mode = .from_dict(name_match_mode)
    return web.Response(status=200)


async def api_users_profile_comments_comment_id_delete(request: web.Request, comment_id) -> web.Response:
    """api_users_profile_comments_comment_id_delete

    

    :param comment_id: 
    :type comment_id: int

    """
    return web.Response(status=200)


async def api_users_profile_comments_comment_id_post(request: web.Request, comment_id, body=None) -> web.Response:
    """api_users_profile_comments_comment_id_post

    

    :param comment_id: 
    :type comment_id: int
    :param body: 
    :type body: dict | bytes

    """
    body = CommentForApiContract.from_dict(body)
    return web.Response(status=200)
