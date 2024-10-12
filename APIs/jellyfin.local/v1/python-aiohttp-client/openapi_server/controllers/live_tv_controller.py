from typing import List, Dict
from aiohttp import web

from openapi_server.models.base_item_dto import BaseItemDto
from openapi_server.models.base_item_dto_query_result import BaseItemDtoQueryResult
from openapi_server.models.channel_mapping_options_dto import ChannelMappingOptionsDto
from openapi_server.models.channel_type import ChannelType
from openapi_server.models.get_programs_dto import GetProgramsDto
from openapi_server.models.guide_info import GuideInfo
from openapi_server.models.image_type import ImageType
from openapi_server.models.item_fields import ItemFields
from openapi_server.models.listings_provider_info import ListingsProviderInfo
from openapi_server.models.live_tv_info import LiveTvInfo
from openapi_server.models.name_id_pair import NameIdPair
from openapi_server.models.problem_details import ProblemDetails
from openapi_server.models.recording_status import RecordingStatus
from openapi_server.models.series_timer_info_dto import SeriesTimerInfoDto
from openapi_server.models.series_timer_info_dto_query_result import SeriesTimerInfoDtoQueryResult
from openapi_server.models.set_channel_mapping_dto import SetChannelMappingDto
from openapi_server.models.sort_order import SortOrder
from openapi_server.models.timer_info_dto import TimerInfoDto
from openapi_server.models.timer_info_dto_query_result import TimerInfoDtoQueryResult
from openapi_server.models.tuner_channel_mapping import TunerChannelMapping
from openapi_server.models.tuner_host_info import TunerHostInfo
from openapi_server import util


async def add_listing_provider(request: web.Request, pw=None, validate_listings=None, validate_login=None, body=None) -> web.Response:
    """Adds a listings provider.

    

    :param pw: Password.
    :type pw: str
    :param validate_listings: Validate listings.
    :type validate_listings: bool
    :param validate_login: Validate login.
    :type validate_login: bool
    :param body: New listings info.
    :type body: dict | bytes

    """
    body = ListingsProviderInfo.from_dict(body)
    return web.Response(status=200)


async def add_tuner_host(request: web.Request, body=None) -> web.Response:
    """Adds a tuner host.

    

    :param body: New tuner host.
    :type body: dict | bytes

    """
    body = TunerHostInfo.from_dict(body)
    return web.Response(status=200)


async def cancel_series_timer(request: web.Request, timer_id) -> web.Response:
    """Cancels a live tv series timer.

    

    :param timer_id: Timer id.
    :type timer_id: str

    """
    return web.Response(status=200)


async def cancel_timer(request: web.Request, timer_id) -> web.Response:
    """Cancels a live tv timer.

    

    :param timer_id: Timer id.
    :type timer_id: str

    """
    return web.Response(status=200)


async def create_series_timer(request: web.Request, body=None) -> web.Response:
    """Creates a live tv series timer.

    

    :param body: New series timer info.
    :type body: dict | bytes

    """
    body = SeriesTimerInfoDto.from_dict(body)
    return web.Response(status=200)


async def create_timer(request: web.Request, body=None) -> web.Response:
    """Creates a live tv timer.

    

    :param body: New timer info.
    :type body: dict | bytes

    """
    body = TimerInfoDto.from_dict(body)
    return web.Response(status=200)


async def delete_listing_provider(request: web.Request, id=None) -> web.Response:
    """Delete listing provider.

    

    :param id: Listing provider id.
    :type id: str

    """
    return web.Response(status=200)


async def delete_recording(request: web.Request, recording_id) -> web.Response:
    """Deletes a live tv recording.

    

    :param recording_id: Recording id.
    :type recording_id: str
    :type recording_id: str

    """
    return web.Response(status=200)


async def delete_tuner_host(request: web.Request, id=None) -> web.Response:
    """Deletes a tuner host.

    

    :param id: Tuner host id.
    :type id: str

    """
    return web.Response(status=200)


async def discover_tuners(request: web.Request, new_devices_only=None) -> web.Response:
    """Discover tuners.

    

    :param new_devices_only: Only discover new tuners.
    :type new_devices_only: bool

    """
    return web.Response(status=200)


async def discvover_tuners(request: web.Request, new_devices_only=None) -> web.Response:
    """Discover tuners.

    

    :param new_devices_only: Only discover new tuners.
    :type new_devices_only: bool

    """
    return web.Response(status=200)


async def get_channel(request: web.Request, channel_id, user_id=None) -> web.Response:
    """Gets a live tv channel.

    

    :param channel_id: Channel id.
    :type channel_id: str
    :type channel_id: str
    :param user_id: Optional. Attach user data.
    :type user_id: str
    :type user_id: str

    """
    return web.Response(status=200)


async def get_channel_mapping_options(request: web.Request, provider_id=None) -> web.Response:
    """Get channel mapping options.

    

    :param provider_id: Provider id.
    :type provider_id: str

    """
    return web.Response(status=200)


async def get_default_listing_provider(request: web.Request, ) -> web.Response:
    """Gets default listings provider info.

    


    """
    return web.Response(status=200)


async def get_default_timer(request: web.Request, program_id=None) -> web.Response:
    """Gets the default values for a new timer.

    

    :param program_id: Optional. To attach default values based on a program.
    :type program_id: str

    """
    return web.Response(status=200)


async def get_guide_info(request: web.Request, ) -> web.Response:
    """Get guid info.

    


    """
    return web.Response(status=200)


async def get_lineups(request: web.Request, id=None, type=None, location=None, country=None) -> web.Response:
    """Gets available lineups.

    

    :param id: Provider id.
    :type id: str
    :param type: Provider type.
    :type type: str
    :param location: Location.
    :type location: str
    :param country: Country.
    :type country: str

    """
    return web.Response(status=200)


async def get_live_recording_file(request: web.Request, recording_id) -> web.Response:
    """Gets a live tv recording stream.

    

    :param recording_id: Recording id.
    :type recording_id: str

    """
    return web.Response(status=200)


async def get_live_stream_file(request: web.Request, stream_id, container) -> web.Response:
    """Gets a live tv channel stream.

    

    :param stream_id: Stream id.
    :type stream_id: str
    :param container: Container type.
    :type container: str

    """
    return web.Response(status=200)


async def get_live_tv_channels(request: web.Request, type=None, user_id=None, start_index=None, is_movie=None, is_series=None, is_news=None, is_kids=None, is_sports=None, limit=None, is_favorite=None, is_liked=None, is_disliked=None, enable_images=None, image_type_limit=None, enable_image_types=None, fields=None, enable_user_data=None, sort_by=None, sort_order=None, enable_favorite_sorting=None, add_current_program=None) -> web.Response:
    """Gets available live tv channels.

    

    :param type: Optional. Filter by channel type.
    :type type: dict | bytes
    :param user_id: Optional. Filter by user and attach user data.
    :type user_id: str
    :type user_id: str
    :param start_index: Optional. The record index to start at. All items with a lower index will be dropped from the results.
    :type start_index: int
    :param is_movie: Optional. Filter for movies.
    :type is_movie: bool
    :param is_series: Optional. Filter for series.
    :type is_series: bool
    :param is_news: Optional. Filter for news.
    :type is_news: bool
    :param is_kids: Optional. Filter for kids.
    :type is_kids: bool
    :param is_sports: Optional. Filter for sports.
    :type is_sports: bool
    :param limit: Optional. The maximum number of records to return.
    :type limit: int
    :param is_favorite: Optional. Filter by channels that are favorites, or not.
    :type is_favorite: bool
    :param is_liked: Optional. Filter by channels that are liked, or not.
    :type is_liked: bool
    :param is_disliked: Optional. Filter by channels that are disliked, or not.
    :type is_disliked: bool
    :param enable_images: Optional. Include image information in output.
    :type enable_images: bool
    :param image_type_limit: Optional. The max number of images to return, per image type.
    :type image_type_limit: int
    :param enable_image_types: \&quot;Optional. The image types to include in the output.
    :type enable_image_types: list | bytes
    :param fields: Optional. Specify additional fields of information to return in the output.
    :type fields: list | bytes
    :param enable_user_data: Optional. Include user data.
    :type enable_user_data: bool
    :param sort_by: Optional. Key to sort by.
    :type sort_by: List[str]
    :param sort_order: Optional. Sort order.
    :type sort_order: dict | bytes
    :param enable_favorite_sorting: Optional. Incorporate favorite and like status into channel sorting.
    :type enable_favorite_sorting: bool
    :param add_current_program: Optional. Adds current program info to each channel.
    :type add_current_program: bool

    """
    type = .from_dict(type)
    enable_image_types = [ImageType.from_dict(d) for d in enable_image_types]
    fields = [ItemFields.from_dict(d) for d in fields]
    sort_order = .from_dict(sort_order)
    return web.Response(status=200)


async def get_live_tv_info(request: web.Request, ) -> web.Response:
    """Gets available live tv services.

    


    """
    return web.Response(status=200)


async def get_live_tv_programs(request: web.Request, channel_ids=None, user_id=None, min_start_date=None, has_aired=None, is_airing=None, max_start_date=None, min_end_date=None, max_end_date=None, is_movie=None, is_series=None, is_news=None, is_kids=None, is_sports=None, start_index=None, limit=None, sort_by=None, sort_order=None, genres=None, genre_ids=None, enable_images=None, image_type_limit=None, enable_image_types=None, enable_user_data=None, series_timer_id=None, library_series_id=None, fields=None, enable_total_record_count=None) -> web.Response:
    """Gets available live tv epgs.

    

    :param channel_ids: The channels to return guide information for.
    :type channel_ids: List[str]
    :param user_id: Optional. Filter by user id.
    :type user_id: str
    :type user_id: str
    :param min_start_date: Optional. The minimum premiere start date.
    :type min_start_date: str
    :param has_aired: Optional. Filter by programs that have completed airing, or not.
    :type has_aired: bool
    :param is_airing: Optional. Filter by programs that are currently airing, or not.
    :type is_airing: bool
    :param max_start_date: Optional. The maximum premiere start date.
    :type max_start_date: str
    :param min_end_date: Optional. The minimum premiere end date.
    :type min_end_date: str
    :param max_end_date: Optional. The maximum premiere end date.
    :type max_end_date: str
    :param is_movie: Optional. Filter for movies.
    :type is_movie: bool
    :param is_series: Optional. Filter for series.
    :type is_series: bool
    :param is_news: Optional. Filter for news.
    :type is_news: bool
    :param is_kids: Optional. Filter for kids.
    :type is_kids: bool
    :param is_sports: Optional. Filter for sports.
    :type is_sports: bool
    :param start_index: Optional. The record index to start at. All items with a lower index will be dropped from the results.
    :type start_index: int
    :param limit: Optional. The maximum number of records to return.
    :type limit: int
    :param sort_by: Optional. Specify one or more sort orders, comma delimited. Options: Name, StartDate.
    :type sort_by: str
    :param sort_order: Sort Order - Ascending,Descending.
    :type sort_order: str
    :param genres: The genres to return guide information for.
    :type genres: List[str]
    :param genre_ids: The genre ids to return guide information for.
    :type genre_ids: List[str]
    :param enable_images: Optional. Include image information in output.
    :type enable_images: bool
    :param image_type_limit: Optional. The max number of images to return, per image type.
    :type image_type_limit: int
    :param enable_image_types: Optional. The image types to include in the output.
    :type enable_image_types: list | bytes
    :param enable_user_data: Optional. Include user data.
    :type enable_user_data: bool
    :param series_timer_id: Optional. Filter by series timer id.
    :type series_timer_id: str
    :param library_series_id: Optional. Filter by library series id.
    :type library_series_id: str
    :type library_series_id: str
    :param fields: Optional. Specify additional fields of information to return in the output.
    :type fields: list | bytes
    :param enable_total_record_count: Retrieve total record count.
    :type enable_total_record_count: bool

    """
    min_start_date = util.deserialize_datetime(min_start_date)
    max_start_date = util.deserialize_datetime(max_start_date)
    min_end_date = util.deserialize_datetime(min_end_date)
    max_end_date = util.deserialize_datetime(max_end_date)
    enable_image_types = [ImageType.from_dict(d) for d in enable_image_types]
    fields = [ItemFields.from_dict(d) for d in fields]
    return web.Response(status=200)


async def get_program(request: web.Request, program_id, user_id=None) -> web.Response:
    """Gets a live tv program.

    

    :param program_id: Program id.
    :type program_id: str
    :param user_id: Optional. Attach user data.
    :type user_id: str
    :type user_id: str

    """
    return web.Response(status=200)


async def get_programs(request: web.Request, body=None) -> web.Response:
    """Gets available live tv epgs.

    

    :param body: Request body.
    :type body: dict | bytes

    """
    body = GetProgramsDto.from_dict(body)
    return web.Response(status=200)


async def get_recommended_programs(request: web.Request, user_id=None, limit=None, is_airing=None, has_aired=None, is_series=None, is_movie=None, is_news=None, is_kids=None, is_sports=None, enable_images=None, image_type_limit=None, enable_image_types=None, genre_ids=None, fields=None, enable_user_data=None, enable_total_record_count=None) -> web.Response:
    """Gets recommended live tv epgs.

    

    :param user_id: Optional. filter by user id.
    :type user_id: str
    :type user_id: str
    :param limit: Optional. The maximum number of records to return.
    :type limit: int
    :param is_airing: Optional. Filter by programs that are currently airing, or not.
    :type is_airing: bool
    :param has_aired: Optional. Filter by programs that have completed airing, or not.
    :type has_aired: bool
    :param is_series: Optional. Filter for series.
    :type is_series: bool
    :param is_movie: Optional. Filter for movies.
    :type is_movie: bool
    :param is_news: Optional. Filter for news.
    :type is_news: bool
    :param is_kids: Optional. Filter for kids.
    :type is_kids: bool
    :param is_sports: Optional. Filter for sports.
    :type is_sports: bool
    :param enable_images: Optional. Include image information in output.
    :type enable_images: bool
    :param image_type_limit: Optional. The max number of images to return, per image type.
    :type image_type_limit: int
    :param enable_image_types: Optional. The image types to include in the output.
    :type enable_image_types: list | bytes
    :param genre_ids: The genres to return guide information for.
    :type genre_ids: List[str]
    :param fields: Optional. Specify additional fields of information to return in the output.
    :type fields: list | bytes
    :param enable_user_data: Optional. include user data.
    :type enable_user_data: bool
    :param enable_total_record_count: Retrieve total record count.
    :type enable_total_record_count: bool

    """
    enable_image_types = [ImageType.from_dict(d) for d in enable_image_types]
    fields = [ItemFields.from_dict(d) for d in fields]
    return web.Response(status=200)


async def get_recording(request: web.Request, recording_id, user_id=None) -> web.Response:
    """Gets a live tv recording.

    

    :param recording_id: Recording id.
    :type recording_id: str
    :type recording_id: str
    :param user_id: Optional. Attach user data.
    :type user_id: str
    :type user_id: str

    """
    return web.Response(status=200)


async def get_recording_folders(request: web.Request, user_id=None) -> web.Response:
    """Gets recording folders.

    

    :param user_id: Optional. Filter by user and attach user data.
    :type user_id: str
    :type user_id: str

    """
    return web.Response(status=200)


async def get_recording_group(request: web.Request, group_id) -> web.Response:
    """Get recording group.

    

    :param group_id: Group id.
    :type group_id: str
    :type group_id: str

    """
    return web.Response(status=200)


async def get_recording_groups(request: web.Request, user_id=None) -> web.Response:
    """Gets live tv recording groups.

    

    :param user_id: Optional. Filter by user and attach user data.
    :type user_id: str
    :type user_id: str

    """
    return web.Response(status=200)


async def get_recordings(request: web.Request, channel_id=None, user_id=None, start_index=None, limit=None, status=None, is_in_progress=None, series_timer_id=None, enable_images=None, image_type_limit=None, enable_image_types=None, fields=None, enable_user_data=None, is_movie=None, is_series=None, is_kids=None, is_sports=None, is_news=None, is_library_item=None, enable_total_record_count=None) -> web.Response:
    """Gets live tv recordings.

    

    :param channel_id: Optional. Filter by channel id.
    :type channel_id: str
    :param user_id: Optional. Filter by user and attach user data.
    :type user_id: str
    :type user_id: str
    :param start_index: Optional. The record index to start at. All items with a lower index will be dropped from the results.
    :type start_index: int
    :param limit: Optional. The maximum number of records to return.
    :type limit: int
    :param status: Optional. Filter by recording status.
    :type status: dict | bytes
    :param is_in_progress: Optional. Filter by recordings that are in progress, or not.
    :type is_in_progress: bool
    :param series_timer_id: Optional. Filter by recordings belonging to a series timer.
    :type series_timer_id: str
    :param enable_images: Optional. Include image information in output.
    :type enable_images: bool
    :param image_type_limit: Optional. The max number of images to return, per image type.
    :type image_type_limit: int
    :param enable_image_types: Optional. The image types to include in the output.
    :type enable_image_types: list | bytes
    :param fields: Optional. Specify additional fields of information to return in the output.
    :type fields: list | bytes
    :param enable_user_data: Optional. Include user data.
    :type enable_user_data: bool
    :param is_movie: Optional. Filter for movies.
    :type is_movie: bool
    :param is_series: Optional. Filter for series.
    :type is_series: bool
    :param is_kids: Optional. Filter for kids.
    :type is_kids: bool
    :param is_sports: Optional. Filter for sports.
    :type is_sports: bool
    :param is_news: Optional. Filter for news.
    :type is_news: bool
    :param is_library_item: Optional. Filter for is library item.
    :type is_library_item: bool
    :param enable_total_record_count: Optional. Return total record count.
    :type enable_total_record_count: bool

    """
    status = .from_dict(status)
    enable_image_types = [ImageType.from_dict(d) for d in enable_image_types]
    fields = [ItemFields.from_dict(d) for d in fields]
    return web.Response(status=200)


async def get_recordings_series(request: web.Request, channel_id=None, user_id=None, group_id=None, start_index=None, limit=None, status=None, is_in_progress=None, series_timer_id=None, enable_images=None, image_type_limit=None, enable_image_types=None, fields=None, enable_user_data=None, enable_total_record_count=None) -> web.Response:
    """Gets live tv recording series.

    

    :param channel_id: Optional. Filter by channel id.
    :type channel_id: str
    :param user_id: Optional. Filter by user and attach user data.
    :type user_id: str
    :type user_id: str
    :param group_id: Optional. Filter by recording group.
    :type group_id: str
    :param start_index: Optional. The record index to start at. All items with a lower index will be dropped from the results.
    :type start_index: int
    :param limit: Optional. The maximum number of records to return.
    :type limit: int
    :param status: Optional. Filter by recording status.
    :type status: dict | bytes
    :param is_in_progress: Optional. Filter by recordings that are in progress, or not.
    :type is_in_progress: bool
    :param series_timer_id: Optional. Filter by recordings belonging to a series timer.
    :type series_timer_id: str
    :param enable_images: Optional. Include image information in output.
    :type enable_images: bool
    :param image_type_limit: Optional. The max number of images to return, per image type.
    :type image_type_limit: int
    :param enable_image_types: Optional. The image types to include in the output.
    :type enable_image_types: list | bytes
    :param fields: Optional. Specify additional fields of information to return in the output.
    :type fields: list | bytes
    :param enable_user_data: Optional. Include user data.
    :type enable_user_data: bool
    :param enable_total_record_count: Optional. Return total record count.
    :type enable_total_record_count: bool

    """
    status = .from_dict(status)
    enable_image_types = [ImageType.from_dict(d) for d in enable_image_types]
    fields = [ItemFields.from_dict(d) for d in fields]
    return web.Response(status=200)


async def get_schedules_direct_countries(request: web.Request, ) -> web.Response:
    """Gets available countries.

    


    """
    return web.Response(status=200)


async def get_series_timer(request: web.Request, timer_id) -> web.Response:
    """Gets a live tv series timer.

    

    :param timer_id: Timer id.
    :type timer_id: str

    """
    return web.Response(status=200)


async def get_series_timers(request: web.Request, sort_by=None, sort_order=None) -> web.Response:
    """Gets live tv series timers.

    

    :param sort_by: Optional. Sort by SortName or Priority.
    :type sort_by: str
    :param sort_order: Optional. Sort in Ascending or Descending order.
    :type sort_order: dict | bytes

    """
    sort_order = .from_dict(sort_order)
    return web.Response(status=200)


async def get_timer(request: web.Request, timer_id) -> web.Response:
    """Gets a timer.

    

    :param timer_id: Timer id.
    :type timer_id: str

    """
    return web.Response(status=200)


async def get_timers(request: web.Request, channel_id=None, series_timer_id=None, is_active=None, is_scheduled=None) -> web.Response:
    """Gets the live tv timers.

    

    :param channel_id: Optional. Filter by channel id.
    :type channel_id: str
    :param series_timer_id: Optional. Filter by timers belonging to a series timer.
    :type series_timer_id: str
    :param is_active: Optional. Filter by timers that are active.
    :type is_active: bool
    :param is_scheduled: Optional. Filter by timers that are scheduled.
    :type is_scheduled: bool

    """
    return web.Response(status=200)


async def get_tuner_host_types(request: web.Request, ) -> web.Response:
    """Get tuner host types.

    


    """
    return web.Response(status=200)


async def reset_tuner(request: web.Request, tuner_id) -> web.Response:
    """Resets a tv tuner.

    

    :param tuner_id: Tuner id.
    :type tuner_id: str

    """
    return web.Response(status=200)


async def set_channel_mapping(request: web.Request, body) -> web.Response:
    """Set channel mappings.

    

    :param body: The set channel mapping dto.
    :type body: dict | bytes

    """
    body = SetChannelMappingDto.from_dict(body)
    return web.Response(status=200)


async def update_series_timer(request: web.Request, timer_id, body=None) -> web.Response:
    """Updates a live tv series timer.

    

    :param timer_id: Timer id.
    :type timer_id: str
    :param body: New series timer info.
    :type body: dict | bytes

    """
    body = SeriesTimerInfoDto.from_dict(body)
    return web.Response(status=200)


async def update_timer(request: web.Request, timer_id, body=None) -> web.Response:
    """Updates a live tv timer.

    

    :param timer_id: Timer id.
    :type timer_id: str
    :param body: New timer info.
    :type body: dict | bytes

    """
    body = TimerInfoDto.from_dict(body)
    return web.Response(status=200)
