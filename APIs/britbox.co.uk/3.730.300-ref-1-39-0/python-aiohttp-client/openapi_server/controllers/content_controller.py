from typing import List, Dict
from aiohttp import web

from openapi_server.models.item_clip_files_list import ItemClipFilesList
from openapi_server.models.item_detail import ItemDetail
from openapi_server.models.item_downloadable_list import ItemDownloadableList
from openapi_server.models.item_downloadable_request import ItemDownloadableRequest
from openapi_server.models.item_list import ItemList
from openapi_server.models.item_schedule_list import ItemScheduleList
from openapi_server.models.media_file import MediaFile
from openapi_server.models.next_playback_item import NextPlaybackItem
from openapi_server.models.plan import Plan
from openapi_server.models.search_results import SearchResults
from openapi_server.models.service_error import ServiceError
from openapi_server import util


async def get_anon_next_playback_item(request: web.Request, item_id, max_rating=None, expand=None, device=None, segments=None, ff=None, lang=None) -> web.Response:
    """get_anon_next_playback_item

    Identical to GET /account/profile/items/{itemId}/next route but for users that are not logged in i.e. this endpoint does not require authorisation 

    :param item_id: The identifier of the source item to base the next to watch item off. 
    :type item_id: str
    :param max_rating: The maximum rating (inclusive) of an item returned, e.g. &#39;auoflc-pg&#39;.
    :type max_rating: str
    :param expand: If no value is specified no dependencies are expanded.  If &#39;parent&#39; is specified then only the direct parent will be expanded. For example if an &#x60;Episode&#x60; then the &#x60;Season&#x60; would be included.  If &#39;ancestors&#39; is specified then the full parent chain is expanded. For example if an &#x60;Episode&#x60; then both the &#x60;Season&#x60; and &#x60;Show&#x60; would be included. 
    :type expand: str
    :param device: The type of device the content is targeting.
    :type device: str
    :param segments: The list of segments to filter the response by.
    :type segments: List[str]
    :param ff: The set of opt in feature flags which cause breaking changes to responses.  While Rocket APIs look to avoid breaking changes under the active major version, the formats of responses may need to evolve over this time.  These feature flags allow clients to select which response formats they expect and avoid breaking clients as these formats evolve under the current major version.  ### Flags  - &#x60;all&#x60; - Enable all flags. Useful for testing. _Don&#39;t use in production_. - &#x60;idp&#x60; - Dynamic item detail pages with schedulable rows. - &#x60;ldp&#x60; - Dynamic list detail pages with schedulable rows. - &#x60;hb&#x60; - Hubble formatted image urls. - &#x60;rpt&#x60; - Updated resume point threshold logic. - &#x60;cas&#x60; - \&quot;Custom Asset Search\&quot;, inlcude &#x60;customAssets&#x60; in search results. - &#x60;lrl&#x60; - Do not pre-populate related list if more than &#x60;max_list_prefetch&#x60; down the page. - &#x60;cd&#x60; - Custom Destination support.  See the &#x60;feature-flags.md&#x60; for available flag details. 
    :type ff: List[str]
    :param lang: Language code for the preferred language to be returned in the response.  Parameter value is case-insensitive and should be   - a valid 2 letter language code without region such as en, de   - or with region such as en_us, en_au  If undefined then defaults to &#39;en&#39;, unless the server has been configured with a custom default.  See https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes 
    :type lang: str

    """
    return web.Response(status=200)


async def get_item(request: web.Request, id, max_rating=None, expand=None, select_season=None, use_custom_id=None, device=None, sub=None, segments=None, ff=None, lang=None) -> web.Response:
    """get_item

    Returns the details of an item with the specified id.

    :param id: The identifier of the item to load.  The custom identifier of an item can be used here if the &#x60;use_custom_id&#x60; parameter is true. 
    :type id: str
    :param max_rating: The maximum rating (inclusive) of items returned, e.g. &#39;auoflc-pg&#39;.
    :type max_rating: str
    :param expand: If no value is specified no dependencies are expanded.  If &#39;children&#39; is specified then the list of any direct children will be expanded. For example seasons of a show or episodes of a season.  If &#39;all&#39; is specified then the parent chain will be expanded along with any child list at each level. For example if an episode is specified then its season will be expanded and that season&#39;s episode list. The season will have its show expanded and the show will have its season list expanded.  The &#39;all&#39; options is useful when you deep link into a show/season/episode for the first time as it provides full context for navigating around the show page. Subsequent navigation around children of the show should only need to request expand of children.  If &#39;ancestors&#39; is specified then only the parent chain is included.  If &#39;parent&#39; is specified then only the direct parent is included.  If an expand is specified which is not relevant to the item type, it will be ignored. 
    :type expand: str
    :param select_season: Given a provided show id, it can be useful to get the details of a child season. This option provides a means to return the &#x60;first&#x60; or &#x60;latest&#x60; season of a show given the show id.  The &#x60;expand&#x60; parameter also works here so for example you could land on a show page and request the latest season along with &#x60;expand&#x3D;all&#x60;. This would then return the detail of the latest season with its list of child episode summaries, and also expand the detail of the show with its list of seasons summaries.  Note the &#x60;id&#x60; parameter must be a show id for this parameter to work correctly. 
    :type select_season: str
    :param use_custom_id: Set to true when passing a custom Id as the &#x60;id&#x60; path parameter.
    :type use_custom_id: bool
    :param device: The type of device the content is targeting.
    :type device: str
    :param sub: The active subscription code.
    :type sub: str
    :param segments: The list of segments to filter the response by.
    :type segments: List[str]
    :param ff: The set of opt in feature flags which cause breaking changes to responses.  While Rocket APIs look to avoid breaking changes under the active major version, the formats of responses may need to evolve over this time.  These feature flags allow clients to select which response formats they expect and avoid breaking clients as these formats evolve under the current major version.  ### Flags  - &#x60;all&#x60; - Enable all flags. Useful for testing. _Don&#39;t use in production_. - &#x60;idp&#x60; - Dynamic item detail pages with schedulable rows. - &#x60;ldp&#x60; - Dynamic list detail pages with schedulable rows. - &#x60;hb&#x60; - Hubble formatted image urls. - &#x60;rpt&#x60; - Updated resume point threshold logic. - &#x60;cas&#x60; - \&quot;Custom Asset Search\&quot;, inlcude &#x60;customAssets&#x60; in search results. - &#x60;lrl&#x60; - Do not pre-populate related list if more than &#x60;max_list_prefetch&#x60; down the page. - &#x60;cd&#x60; - Custom Destination support.  See the &#x60;feature-flags.md&#x60; for available flag details. 
    :type ff: List[str]
    :param lang: Language code for the preferred language to be returned in the response.  Parameter value is case-insensitive and should be   - a valid 2 letter language code without region such as en, de   - or with region such as en_us, en_au  If undefined then defaults to &#39;en&#39;, unless the server has been configured with a custom default.  See https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes 
    :type lang: str

    """
    return web.Response(status=200)


async def get_item_children_list(request: web.Request, id, page=None, page_size=None, max_rating=None, order=None, device=None, sub=None, segments=None, ff=None, lang=None) -> web.Response:
    """get_item_children_list

    Returns the List of child summary items under an item.  If the item is a Season then the children will be episodes and ordered by episode number.  If the item is a Show then the children will be Seasons and ordered by season number.  Returns 404 if no children found. 

    :param id: The identifier of the item whose children to load.
    :type id: str
    :param page: The page of items to load. Starts from page 1.
    :type page: int
    :param page_size: The number of items to return in a page.
    :type page_size: int
    :param max_rating: The maximum rating (inclusive) of items returned, e.g. &#39;auoflc-pg&#39;.
    :type max_rating: str
    :param order: The list sort order, either &#39;asc&#39; or &#39;desc&#39;.
    :type order: str
    :param device: The type of device the content is targeting.
    :type device: str
    :param sub: The active subscription code.
    :type sub: str
    :param segments: The list of segments to filter the response by.
    :type segments: List[str]
    :param ff: The set of opt in feature flags which cause breaking changes to responses.  While Rocket APIs look to avoid breaking changes under the active major version, the formats of responses may need to evolve over this time.  These feature flags allow clients to select which response formats they expect and avoid breaking clients as these formats evolve under the current major version.  ### Flags  - &#x60;all&#x60; - Enable all flags. Useful for testing. _Don&#39;t use in production_. - &#x60;idp&#x60; - Dynamic item detail pages with schedulable rows. - &#x60;ldp&#x60; - Dynamic list detail pages with schedulable rows. - &#x60;hb&#x60; - Hubble formatted image urls. - &#x60;rpt&#x60; - Updated resume point threshold logic. - &#x60;cas&#x60; - \&quot;Custom Asset Search\&quot;, inlcude &#x60;customAssets&#x60; in search results. - &#x60;lrl&#x60; - Do not pre-populate related list if more than &#x60;max_list_prefetch&#x60; down the page. - &#x60;cd&#x60; - Custom Destination support.  See the &#x60;feature-flags.md&#x60; for available flag details. 
    :type ff: List[str]
    :param lang: Language code for the preferred language to be returned in the response.  Parameter value is case-insensitive and should be   - a valid 2 letter language code without region such as en, de   - or with region such as en_us, en_au  If undefined then defaults to &#39;en&#39;, unless the server has been configured with a custom default.  See https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes 
    :type lang: str

    """
    return web.Response(status=200)


async def get_item_downloadables(request: web.Request, body, ff=None, lang=None) -> web.Response:
    """get_item_downloadables

    Returns the details of an item with the specified id.

    :param body: The item Axis ids joined string with comma.
    :type body: dict | bytes
    :param ff: The set of opt in feature flags which cause breaking changes to responses.  While Rocket APIs look to avoid breaking changes under the active major version, the formats of responses may need to evolve over this time.  These feature flags allow clients to select which response formats they expect and avoid breaking clients as these formats evolve under the current major version.  ### Flags  - &#x60;all&#x60; - Enable all flags. Useful for testing. _Don&#39;t use in production_. - &#x60;idp&#x60; - Dynamic item detail pages with schedulable rows. - &#x60;ldp&#x60; - Dynamic list detail pages with schedulable rows. - &#x60;hb&#x60; - Hubble formatted image urls. - &#x60;rpt&#x60; - Updated resume point threshold logic. - &#x60;cas&#x60; - \&quot;Custom Asset Search\&quot;, inlcude &#x60;customAssets&#x60; in search results. - &#x60;lrl&#x60; - Do not pre-populate related list if more than &#x60;max_list_prefetch&#x60; down the page. - &#x60;cd&#x60; - Custom Destination support.  See the &#x60;feature-flags.md&#x60; for available flag details. 
    :type ff: List[str]
    :param lang: Language code for the preferred language to be returned in the response.  Parameter value is case-insensitive and should be   - a valid 2 letter language code without region such as en, de   - or with region such as en_us, en_au  If undefined then defaults to &#39;en&#39;, unless the server has been configured with a custom default.  See https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes 
    :type lang: str

    """
    body = ItemDownloadableRequest.from_dict(body)
    return web.Response(status=200)


async def get_item_related_list(request: web.Request, id, page=None, page_size=None, max_rating=None, device=None, sub=None, segments=None, ff=None, lang=None) -> web.Response:
    """get_item_related_list

    Returns the list of items related to the parent item.  Note for now, due to the size of the list being unknown, only a single page will be returned. 

    :param id: The identifier of the item to based related items off.
    :type id: str
    :param page: The page of items to load. Starts from page 1.
    :type page: int
    :param page_size: The number of items to return in a page.
    :type page_size: int
    :param max_rating: The maximum rating (inclusive) of items returned, e.g. &#39;auoflc-pg&#39;.
    :type max_rating: str
    :param device: The type of device the content is targeting.
    :type device: str
    :param sub: The active subscription code.
    :type sub: str
    :param segments: The list of segments to filter the response by.
    :type segments: List[str]
    :param ff: The set of opt in feature flags which cause breaking changes to responses.  While Rocket APIs look to avoid breaking changes under the active major version, the formats of responses may need to evolve over this time.  These feature flags allow clients to select which response formats they expect and avoid breaking clients as these formats evolve under the current major version.  ### Flags  - &#x60;all&#x60; - Enable all flags. Useful for testing. _Don&#39;t use in production_. - &#x60;idp&#x60; - Dynamic item detail pages with schedulable rows. - &#x60;ldp&#x60; - Dynamic list detail pages with schedulable rows. - &#x60;hb&#x60; - Hubble formatted image urls. - &#x60;rpt&#x60; - Updated resume point threshold logic. - &#x60;cas&#x60; - \&quot;Custom Asset Search\&quot;, inlcude &#x60;customAssets&#x60; in search results. - &#x60;lrl&#x60; - Do not pre-populate related list if more than &#x60;max_list_prefetch&#x60; down the page. - &#x60;cd&#x60; - Custom Destination support.  See the &#x60;feature-flags.md&#x60; for available flag details. 
    :type ff: List[str]
    :param lang: Language code for the preferred language to be returned in the response.  Parameter value is case-insensitive and should be   - a valid 2 letter language code without region such as en, de   - or with region such as en_us, en_au  If undefined then defaults to &#39;en&#39;, unless the server has been configured with a custom default.  See https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes 
    :type lang: str

    """
    return web.Response(status=200)


async def get_items_media_clip_files(request: web.Request, body, ff=None, lang=None) -> web.Response:
    """get_items_media_clip_files

    Get the media clip files associated with items. 

    :param body: The item Axis ids joined string with comma.
    :type body: dict | bytes
    :param ff: The set of opt in feature flags which cause breaking changes to responses.  While Rocket APIs look to avoid breaking changes under the active major version, the formats of responses may need to evolve over this time.  These feature flags allow clients to select which response formats they expect and avoid breaking clients as these formats evolve under the current major version.  ### Flags  - &#x60;all&#x60; - Enable all flags. Useful for testing. _Don&#39;t use in production_. - &#x60;idp&#x60; - Dynamic item detail pages with schedulable rows. - &#x60;ldp&#x60; - Dynamic list detail pages with schedulable rows. - &#x60;hb&#x60; - Hubble formatted image urls. - &#x60;rpt&#x60; - Updated resume point threshold logic. - &#x60;cas&#x60; - \&quot;Custom Asset Search\&quot;, inlcude &#x60;customAssets&#x60; in search results. - &#x60;lrl&#x60; - Do not pre-populate related list if more than &#x60;max_list_prefetch&#x60; down the page. - &#x60;cd&#x60; - Custom Destination support.  See the &#x60;feature-flags.md&#x60; for available flag details. 
    :type ff: List[str]
    :param lang: Language code for the preferred language to be returned in the response.  Parameter value is case-insensitive and should be   - a valid 2 letter language code without region such as en, de   - or with region such as en_us, en_au  If undefined then defaults to &#39;en&#39;, unless the server has been configured with a custom default.  See https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes 
    :type lang: str

    """
    body = ItemDownloadableRequest.from_dict(body)
    return web.Response(status=200)


async def get_list(request: web.Request, id, page=None, page_size=None, max_rating=None, order=None, order_by=None, param=None, item_type=None, device=None, sub=None, segments=None, ff=None, lang=None) -> web.Response:
    """get_list

    Returns a list of items under the specified item list

    :param id: The identifier of the list to load.
    :type id: str
    :param page: The page of items to load. Starts from page 1.
    :type page: int
    :param page_size: The number of items to return in a page.
    :type page_size: int
    :param max_rating: The maximum rating (inclusive) of items returned, e.g. &#39;auoflc-pg&#39;.
    :type max_rating: str
    :param order: The list sort order, either &#39;asc&#39; or &#39;desc&#39;.
    :type order: str
    :param order_by: What to order by.
    :type order_by: str
    :param param: The list parameter in format &#39;key:value&#39;, e.g. &#39;genre:action&#39;.
    :type param: str
    :param item_type: The item type to filter by. Defaults to unspecified.
    :type item_type: str
    :param device: The type of device the content is targeting.
    :type device: str
    :param sub: The active subscription code.
    :type sub: str
    :param segments: The list of segments to filter the response by.
    :type segments: List[str]
    :param ff: The set of opt in feature flags which cause breaking changes to responses.  While Rocket APIs look to avoid breaking changes under the active major version, the formats of responses may need to evolve over this time.  These feature flags allow clients to select which response formats they expect and avoid breaking clients as these formats evolve under the current major version.  ### Flags  - &#x60;all&#x60; - Enable all flags. Useful for testing. _Don&#39;t use in production_. - &#x60;idp&#x60; - Dynamic item detail pages with schedulable rows. - &#x60;ldp&#x60; - Dynamic list detail pages with schedulable rows. - &#x60;hb&#x60; - Hubble formatted image urls. - &#x60;rpt&#x60; - Updated resume point threshold logic. - &#x60;cas&#x60; - \&quot;Custom Asset Search\&quot;, inlcude &#x60;customAssets&#x60; in search results. - &#x60;lrl&#x60; - Do not pre-populate related list if more than &#x60;max_list_prefetch&#x60; down the page. - &#x60;cd&#x60; - Custom Destination support.  See the &#x60;feature-flags.md&#x60; for available flag details. 
    :type ff: List[str]
    :param lang: Language code for the preferred language to be returned in the response.  Parameter value is case-insensitive and should be   - a valid 2 letter language code without region such as en, de   - or with region such as en_us, en_au  If undefined then defaults to &#39;en&#39;, unless the server has been configured with a custom default.  See https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes 
    :type lang: str

    """
    return web.Response(status=200)


async def get_lists(request: web.Request, ids, page_size=None, max_rating=None, order=None, order_by=None, item_type=None, device=None, sub=None, segments=None, ff=None, lang=None) -> web.Response:
    """get_lists

    Returns an array of item lists with their first page of content resolved.

    :param ids: A comma delimited list of item list identifiers.  These can be list ids e.g. &#x60;14354,65473,3234&#x60;  Or more complex sort/filter queries using pipes e.g.  &#x60;14354|max_rating&#x3D;AUOFLC-E|order&#x3D;asc|order_by&#x3D;year-added,65473|page_size&#x3D;30,3234&#x60;  _Note the id must always come first for each encoded list query_  List parameters may be provide without the &#x60;param&#x3D;&#x60; prefix e.g. &#x60;14354|genre:action&#x60;  Only the following options can be present.   - &#x60;order&#x60;   - &#x60;order_by&#x60;   - &#x60;max_rating&#x60;   - &#x60;page_size&#x60;   - &#x60;item_type&#x60;   - &#x60;param&#x60; 
    :type ids: List[str]
    :param page_size: The number of items to return in a page.
    :type page_size: int
    :param max_rating: The maximum rating (inclusive) of items returned, e.g. &#39;auoflc-pg&#39;.
    :type max_rating: str
    :param order: The list sort order, either &#39;asc&#39; or &#39;desc&#39;.
    :type order: str
    :param order_by: What to order by.
    :type order_by: str
    :param item_type: The item type to filter by. Defaults to unspecified.
    :type item_type: str
    :param device: The type of device the content is targeting.
    :type device: str
    :param sub: The active subscription code.
    :type sub: str
    :param segments: The list of segments to filter the response by.
    :type segments: List[str]
    :param ff: The set of opt in feature flags which cause breaking changes to responses.  While Rocket APIs look to avoid breaking changes under the active major version, the formats of responses may need to evolve over this time.  These feature flags allow clients to select which response formats they expect and avoid breaking clients as these formats evolve under the current major version.  ### Flags  - &#x60;all&#x60; - Enable all flags. Useful for testing. _Don&#39;t use in production_. - &#x60;idp&#x60; - Dynamic item detail pages with schedulable rows. - &#x60;ldp&#x60; - Dynamic list detail pages with schedulable rows. - &#x60;hb&#x60; - Hubble formatted image urls. - &#x60;rpt&#x60; - Updated resume point threshold logic. - &#x60;cas&#x60; - \&quot;Custom Asset Search\&quot;, inlcude &#x60;customAssets&#x60; in search results. - &#x60;lrl&#x60; - Do not pre-populate related list if more than &#x60;max_list_prefetch&#x60; down the page. - &#x60;cd&#x60; - Custom Destination support.  See the &#x60;feature-flags.md&#x60; for available flag details. 
    :type ff: List[str]
    :param lang: Language code for the preferred language to be returned in the response.  Parameter value is case-insensitive and should be   - a valid 2 letter language code without region such as en, de   - or with region such as en_us, en_au  If undefined then defaults to &#39;en&#39;, unless the server has been configured with a custom default.  See https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes 
    :type lang: str

    """
    return web.Response(status=200)


async def get_public_item_media_files(request: web.Request, id, delivery, resolution, formats=None, device=None, sub=None, segments=None, ff=None, lang=None) -> web.Response:
    """get_public_item_media_files

    Get the free / public video files associated with an item given maximum resolution, device type and one or more delivery types.  Returns an array of video file objects which each include a url to a video.  The first entry in the array contains what is predicted to be the best match. The remainder of the entries, if any, may contain resolutions below what was requests. For example if you request HD-720 the response may also contain SD entries.  If you specify multiple delivery types, then the response array will insert types in the order you specify them in the query. For example &#x60;stream,progressive&#x60; would return an array with 0 or more stream files followed by 0 or more progressive files.  If no files are found a 404 is returned. 

    :param id: The identifier of the item whose video files to load.
    :type id: str
    :param delivery: The video delivery type you require.
    :type delivery: List[str]
    :param resolution: The maximum resolution the device to playback the media can present.
    :type resolution: str
    :param formats: The set of media file formats that the device supports, in the order of preference.  When provided, Rocket API returns only media files in formats specified in this parameter. For each resolution, only the first media file of matching supported format is returned. Files of different resolutions may be of different supported media file formats.  &#x60;external&#x60; value is reserved for project customizations where the real MIME type of the file on the specified URL is unknown at the time of ingestion.  When not provided, Rocket API uses the legacy &#x60;User-Agent&#x60; header-based logic to find matching media files. 
    :type formats: List[str]
    :param device: The type of device the content is targeting.
    :type device: str
    :param sub: The active subscription code.
    :type sub: str
    :param segments: The list of segments to filter the response by.
    :type segments: List[str]
    :param ff: The set of opt in feature flags which cause breaking changes to responses.  While Rocket APIs look to avoid breaking changes under the active major version, the formats of responses may need to evolve over this time.  These feature flags allow clients to select which response formats they expect and avoid breaking clients as these formats evolve under the current major version.  ### Flags  - &#x60;all&#x60; - Enable all flags. Useful for testing. _Don&#39;t use in production_. - &#x60;idp&#x60; - Dynamic item detail pages with schedulable rows. - &#x60;ldp&#x60; - Dynamic list detail pages with schedulable rows. - &#x60;hb&#x60; - Hubble formatted image urls. - &#x60;rpt&#x60; - Updated resume point threshold logic. - &#x60;cas&#x60; - \&quot;Custom Asset Search\&quot;, inlcude &#x60;customAssets&#x60; in search results. - &#x60;lrl&#x60; - Do not pre-populate related list if more than &#x60;max_list_prefetch&#x60; down the page. - &#x60;cd&#x60; - Custom Destination support.  See the &#x60;feature-flags.md&#x60; for available flag details. 
    :type ff: List[str]
    :param lang: Language code for the preferred language to be returned in the response.  Parameter value is case-insensitive and should be   - a valid 2 letter language code without region such as en, de   - or with region such as en_us, en_au  If undefined then defaults to &#39;en&#39;, unless the server has been configured with a custom default.  See https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes 
    :type lang: str

    """
    return web.Response(status=200)


async def get_schedules(request: web.Request, channels, _date, hour, duration, intersect=None, device=None, sub=None, segments=None, ff=None, lang=None) -> web.Response:
    """get_schedules

    Returns schedules for a defined set of channels over a requested period.  Schedules are requested in hour blocks and returned grouped by the channel they belong to.  For example, to load 12 hours of schedules for channels &#x60;4343&#x60; and &#x60;5234&#x60;, on 21/2/2017 starting from 08:00.  &#x60;&#x60;&#x60; channels&#x3D;4343,5234 date&#x3D;2017-02-21 hour&#x3D;8 duration&#x3D;12 &#x60;&#x60;&#x60;  Please remember that &#x60;date&#x60; and &#x60;hour&#x60; combined represent a normal datetime,  so they should be converted to UTC on the client - this will help to avoid  issues with EPG schedules near midnight.  If a channel id is passed which doesn&#39;t exist then this endpoint will return an empty schedule list for it. If instead we returned 404, this would invalidate all other channel schedules in the same request which would be unfriendly for clients presenting these channel schedules. 

    :param channels: The list of channel ids to get schedules for.
    :type channels: List[str]
    :param _date: The date to target in ISO format, e.g. &#x60;2017-05-23&#x60; (converted to UTC - see main description).  The base hour requested will belong to this date. 
    :type _date: str
    :param hour: The base hour in the day, defined by the &#x60;date&#x60; parameter, you wish to load schedules for  (converted to UTC - see main description).  From 0 to 23, where 0 is midnight. 
    :type hour: int
    :param duration: The number of hours of schedules to load from the base &#x60;hour&#x60; parameter.  This may be negative or positive depending on whether you want to load past or future schedules.  Minimum value is -24, maximum is 24. A value of zero is invalid. 
    :type duration: int
    :param intersect: Flag indicating whether schedules should intersect or be contained in the provided interval.  If set to &#x60;true&#x60;, the result will contain all schedules where either schedule start time or end time touches the provided interval.  If set to &#x60;false&#x60;, only schedules fully contained in the given period will be returned. 
    :type intersect: bool
    :param device: The type of device the content is targeting.
    :type device: str
    :param sub: The active subscription code.
    :type sub: str
    :param segments: The list of segments to filter the response by.
    :type segments: List[str]
    :param ff: The set of opt in feature flags which cause breaking changes to responses.  While Rocket APIs look to avoid breaking changes under the active major version, the formats of responses may need to evolve over this time.  These feature flags allow clients to select which response formats they expect and avoid breaking clients as these formats evolve under the current major version.  ### Flags  - &#x60;all&#x60; - Enable all flags. Useful for testing. _Don&#39;t use in production_. - &#x60;idp&#x60; - Dynamic item detail pages with schedulable rows. - &#x60;ldp&#x60; - Dynamic list detail pages with schedulable rows. - &#x60;hb&#x60; - Hubble formatted image urls. - &#x60;rpt&#x60; - Updated resume point threshold logic. - &#x60;cas&#x60; - \&quot;Custom Asset Search\&quot;, inlcude &#x60;customAssets&#x60; in search results. - &#x60;lrl&#x60; - Do not pre-populate related list if more than &#x60;max_list_prefetch&#x60; down the page. - &#x60;cd&#x60; - Custom Destination support.  See the &#x60;feature-flags.md&#x60; for available flag details. 
    :type ff: List[str]
    :param lang: Language code for the preferred language to be returned in the response.  Parameter value is case-insensitive and should be   - a valid 2 letter language code without region such as en, de   - or with region such as en_us, en_au  If undefined then defaults to &#39;en&#39;, unless the server has been configured with a custom default.  See https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes 
    :type lang: str

    """
    _date = util.deserialize_date(_date)
    return web.Response(status=200)


async def plans_id_get(request: web.Request, id, device=None, sub=None, segments=None, ff=None, lang=None) -> web.Response:
    """plans_id_get

    Returns the details of a Plan with the specified id.

    :param id: The identifier of the Plan to load.
    :type id: str
    :param device: The type of device the content is targeting.
    :type device: str
    :param sub: The active subscription code.
    :type sub: str
    :param segments: The list of segments to filter the response by.
    :type segments: List[str]
    :param ff: The set of opt in feature flags which cause breaking changes to responses.  While Rocket APIs look to avoid breaking changes under the active major version, the formats of responses may need to evolve over this time.  These feature flags allow clients to select which response formats they expect and avoid breaking clients as these formats evolve under the current major version.  ### Flags  - &#x60;all&#x60; - Enable all flags. Useful for testing. _Don&#39;t use in production_. - &#x60;idp&#x60; - Dynamic item detail pages with schedulable rows. - &#x60;ldp&#x60; - Dynamic list detail pages with schedulable rows. - &#x60;hb&#x60; - Hubble formatted image urls. - &#x60;rpt&#x60; - Updated resume point threshold logic. - &#x60;cas&#x60; - \&quot;Custom Asset Search\&quot;, inlcude &#x60;customAssets&#x60; in search results. - &#x60;lrl&#x60; - Do not pre-populate related list if more than &#x60;max_list_prefetch&#x60; down the page. - &#x60;cd&#x60; - Custom Destination support.  See the &#x60;feature-flags.md&#x60; for available flag details. 
    :type ff: List[str]
    :param lang: Language code for the preferred language to be returned in the response.  Parameter value is case-insensitive and should be   - a valid 2 letter language code without region such as en, de   - or with region such as en_us, en_au  If undefined then defaults to &#39;en&#39;, unless the server has been configured with a custom default.  See https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes 
    :type lang: str

    """
    return web.Response(status=200)


async def search(request: web.Request, term, include=None, group=None, max_results=None, max_rating=None, device=None, sub=None, segments=None, ff=None, lang=None) -> web.Response:
    """search

    Search the catalog of items and people.

    :param term: The search term to query.
    :type term: str
    :param include: By default people, movies and tv (shows + programs) will be included in the search results.  If the &#x60;cas&#x60; feature flag is set, \&quot;other\&quot; items (&#x60;customAsset&#x60;s) will also be included by default  If you don&#39;t want all of these types you can specifiy the specific includes you care about. 
    :type include: List[str]
    :param group: When this option is set, instead of all search result items being returned in a single list, they will instead be returned under two lists. One for movies and another for tv (shows + programs).  if the &#x60;cas&#x60; feature flag is set, a third &#x60;other&#x60; list will be included containing &#x60;customAsset&#x60; results  Default is undefined meaning items will be returned in a single list.  The array of &#x60;people&#x60; results will always be separate from items. 
    :type group: bool
    :param max_results: The maximum number of results to return.
    :type max_results: int
    :param max_rating: The maximum rating (inclusive) of items returned, e.g. &#39;auoflc-pg&#39;.
    :type max_rating: str
    :param device: The type of device the content is targeting.
    :type device: str
    :param sub: The active subscription code.
    :type sub: str
    :param segments: The list of segments to filter the response by.
    :type segments: List[str]
    :param ff: The set of opt in feature flags which cause breaking changes to responses.  While Rocket APIs look to avoid breaking changes under the active major version, the formats of responses may need to evolve over this time.  These feature flags allow clients to select which response formats they expect and avoid breaking clients as these formats evolve under the current major version.  ### Flags  - &#x60;all&#x60; - Enable all flags. Useful for testing. _Don&#39;t use in production_. - &#x60;idp&#x60; - Dynamic item detail pages with schedulable rows. - &#x60;ldp&#x60; - Dynamic list detail pages with schedulable rows. - &#x60;hb&#x60; - Hubble formatted image urls. - &#x60;rpt&#x60; - Updated resume point threshold logic. - &#x60;cas&#x60; - \&quot;Custom Asset Search\&quot;, inlcude &#x60;customAssets&#x60; in search results. - &#x60;lrl&#x60; - Do not pre-populate related list if more than &#x60;max_list_prefetch&#x60; down the page. - &#x60;cd&#x60; - Custom Destination support.  See the &#x60;feature-flags.md&#x60; for available flag details. 
    :type ff: List[str]
    :param lang: Language code for the preferred language to be returned in the response.  Parameter value is case-insensitive and should be   - a valid 2 letter language code without region such as en, de   - or with region such as en_us, en_au  If undefined then defaults to &#39;en&#39;, unless the server has been configured with a custom default.  See https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes 
    :type lang: str

    """
    return web.Response(status=200)
