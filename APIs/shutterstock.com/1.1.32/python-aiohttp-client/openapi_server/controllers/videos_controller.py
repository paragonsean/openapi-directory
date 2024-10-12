from typing import List, Dict
from aiohttp import web

from openapi_server.models.category_data_list import CategoryDataList
from openapi_server.models.collection import Collection
from openapi_server.models.collection_create_request import CollectionCreateRequest
from openapi_server.models.collection_create_response import CollectionCreateResponse
from openapi_server.models.collection_data_list import CollectionDataList
from openapi_server.models.collection_item_data_list import CollectionItemDataList
from openapi_server.models.collection_item_request import CollectionItemRequest
from openapi_server.models.collection_update_request import CollectionUpdateRequest
from openapi_server.models.download_history_data_list import DownloadHistoryDataList
from openapi_server.models.featured_collection import FeaturedCollection
from openapi_server.models.featured_collection_data_list import FeaturedCollectionDataList
from openapi_server.models.language import Language
from openapi_server.models.license_video_request import LicenseVideoRequest
from openapi_server.models.license_video_result_data_list import LicenseVideoResultDataList
from openapi_server.models.redownload_video import RedownloadVideo
from openapi_server.models.suggestions import Suggestions
from openapi_server.models.updated_media_data_list import UpdatedMediaDataList
from openapi_server.models.url import Url
from openapi_server.models.video import Video
from openapi_server.models.video_collection_item_data_list import VideoCollectionItemDataList
from openapi_server.models.video_data_list import VideoDataList
from openapi_server.models.video_search_results import VideoSearchResults
from openapi_server import util


async def add_video_collection_items(request: web.Request, id, body) -> web.Response:
    """Add videos to collections

    This endpoint adds one or more videos to a collection by video IDs.

    :param id: The ID of the collection to which items should be added
    :type id: str
    :param body: Array of video IDs to add to the collection
    :type body: dict | bytes

    """
    body = CollectionItemRequest.from_dict(body)
    return web.Response(status=200)


async def create_video_collection(request: web.Request, body) -> web.Response:
    """Create video collections

    This endpoint creates one or more collections (clipboxes). To add videos to collections, use &#x60;POST /v2/videos/collections/{id}/items&#x60;.

    :param body: Collection metadata
    :type body: dict | bytes

    """
    body = CollectionCreateRequest.from_dict(body)
    return web.Response(status=200)


async def delete_video_collection(request: web.Request, id) -> web.Response:
    """Delete video collections

    This endpoint deletes a collection.

    :param id: The ID of the collection to delete
    :type id: str

    """
    return web.Response(status=200)


async def delete_video_collection_items(request: web.Request, id, item_id=None) -> web.Response:
    """Remove videos from collections

    This endpoint removes one or more videos from a collection.

    :param id: The ID of the Collection from which items will be deleted
    :type id: str
    :param item_id: One or more video IDs to remove from the collection
    :type item_id: List[str]

    """
    return web.Response(status=200)


async def download_videos(request: web.Request, id, body) -> web.Response:
    """Download videos

    This endpoint redownloads videos that you have already received a license for.

    :param id: The license ID of the item to (re)download. The download links in the response are valid for 8 hours.
    :type id: str
    :param body: Information about the videos to redownload
    :type body: dict | bytes

    """
    body = RedownloadVideo.from_dict(body)
    return web.Response(status=200)


async def find_similar_videos(request: web.Request, id, language=None, page=None, per_page=None, view=None) -> web.Response:
    """List similar videos

    This endpoint searches for videos that are similar to a video that you specify.

    :param id: The ID of a video for which similar videos should be returned
    :type id: str
    :param language: Language for the keywords and categories in the response
    :type language: dict | bytes
    :param page: Page number
    :type page: int
    :param per_page: Number of results per page
    :type per_page: int
    :param view: Amount of detail to render in the response
    :type view: str

    """
    language = .from_dict(language)
    return web.Response(status=200)


async def get_featured_video_collection(request: web.Request, id, embed=None) -> web.Response:
    """Get the details of featured video collections

    This endpoint gets more detailed information about a featured video collection, including its cover video and timestamps for its creation and most recent update. To get the videos, use &#x60;GET /v2/videos/collections/featured/{id}/items&#x60;.

    :param id: Collection ID
    :type id: str
    :param embed: What information to include in the response, such as a URL to the collection
    :type embed: str

    """
    return web.Response(status=200)


async def get_featured_video_collection_items(request: web.Request, id, page=None, per_page=None) -> web.Response:
    """Get the contents of featured video collections

    This endpoint lists the IDs of videos in a featured collection and the date that each was added.

    :param id: Collection ID
    :type id: str
    :param page: Page number
    :type page: int
    :param per_page: Number of results per page
    :type per_page: int

    """
    return web.Response(status=200)


async def get_featured_video_collection_list(request: web.Request, embed=None) -> web.Response:
    """List featured video collections

    This endpoint lists featured video collections and a name and cover video for each collection.

    :param embed: What information to include in the response, such as a URL to the collection
    :type embed: str

    """
    return web.Response(status=200)


async def get_updated_videos(request: web.Request, start_date=None, end_date=None, interval=None, page=None, per_page=None, sort=None) -> web.Response:
    """List updated videos

    This endpoint lists videos that have been updated in the specified time period to update content management systems (CMS) or digital asset management (DAM) systems. In most cases, use the &#x60;interval&#x60; parameter to show videos that were updated recently, but you can also use the &#x60;start_date&#x60; and &#x60;end_date&#x60; parameters to specify a range of no more than three days. Do not use the &#x60;interval&#x60; parameter with either &#x60;start_date&#x60; or &#x60;end_date&#x60;.

    :param start_date: Show videos updated on or after the specified date
    :type start_date: str
    :param end_date: Show videos updated before the specified date
    :type end_date: str
    :param interval: Show videos updated in the specified time period, where the time period is an interval (like SQL INTERVAL) such as 1 DAY, 6 HOUR, or 30 MINUTE; the default is 1 HOUR, which shows videos that were updated in the hour preceding the request
    :type interval: str
    :param page: Page number
    :type page: int
    :param per_page: Number of results per page
    :type per_page: int
    :param sort: Sort by oldest or newest videos first
    :type sort: str

    """
    start_date = util.deserialize_date(start_date)
    end_date = util.deserialize_date(end_date)
    return web.Response(status=200)


async def get_video(request: web.Request, id, language=None, view=None, search_id=None) -> web.Response:
    """Get details about videos

    This endpoint shows information about a video, including URLs to previews and the sizes that it is available in.

    :param id: Video ID
    :type id: str
    :param language: Language for the keywords and categories in the response
    :type language: dict | bytes
    :param view: Amount of detail to render in the response
    :type view: str
    :param search_id: The ID of the search that is related to this request
    :type search_id: str

    """
    language = .from_dict(language)
    return web.Response(status=200)


async def get_video_collection(request: web.Request, id, embed=None, share_code=None) -> web.Response:
    """Get the details of video collections

    This endpoint gets more detailed information about a collection, including the timestamp for its creation and the number of videos in it. To get the videos in collections, use GET /v2/videos/collections/{id}/items.

    :param id: The ID of the collection to return
    :type id: str
    :param embed: Which sharing information to include in the response, such as a URL to the collection
    :type embed: List[str]
    :param share_code: Code to retrieve a shared collection
    :type share_code: str

    """
    return web.Response(status=200)


async def get_video_collection_items(request: web.Request, id, page=None, per_page=None, share_code=None, sort=None) -> web.Response:
    """Get the contents of video collections

    This endpoint lists the IDs of videos in a collection and the date that each was added.

    :param id: Collection ID
    :type id: str
    :param page: Page number
    :type page: int
    :param per_page: Number of results per page
    :type per_page: int
    :param share_code: Code to retrieve the contents of a shared collection
    :type share_code: str
    :param sort: Sort order
    :type sort: str

    """
    return web.Response(status=200)


async def get_video_collection_list(request: web.Request, page=None, per_page=None, embed=None) -> web.Response:
    """List video collections

    This endpoint lists your collections of videos and their basic attributes.

    :param page: Page number
    :type page: int
    :param per_page: Number of results per page
    :type per_page: int
    :param embed: Which sharing information to include in the response, such as a URL to the collection
    :type embed: List[str]

    """
    return web.Response(status=200)


async def get_video_license_list(request: web.Request, video_id=None, license=None, page=None, per_page=None, sort=None, username=None, start_date=None, end_date=None, download_availability=None, team_history=None) -> web.Response:
    """List video licenses

    This endpoint lists existing licenses.

    :param video_id: Show licenses for the specified video ID
    :type video_id: str
    :param license: Show videos that are available with the specified license, such as &#x60;standard&#x60; or &#x60;enhanced&#x60;; prepending a &#x60;-&#x60; sign excludes results from that license
    :type license: str
    :param page: Page number
    :type page: int
    :param per_page: Number of results per page
    :type per_page: int
    :param sort: Sort by oldest or newest videos first
    :type sort: str
    :param username: Filter licenses by username of licensee
    :type username: str
    :param start_date: Show licenses created on or after the specified date
    :type start_date: str
    :param end_date: Show licenses created before the specified date
    :type end_date: str
    :param download_availability: Filter licenses by download availability
    :type download_availability: str
    :param team_history: Set to true to see license history for all members of your team.
    :type team_history: bool

    """
    start_date = util.deserialize_datetime(start_date)
    end_date = util.deserialize_datetime(end_date)
    return web.Response(status=200)


async def get_video_list(request: web.Request, id, view=None, search_id=None) -> web.Response:
    """List videos

    This endpoint lists information about one or more videos, including the aspect ratio and URLs to previews.

    :param id: One or more video IDs
    :type id: List[str]
    :param view: Amount of detail to render in the response
    :type view: str
    :param search_id: The ID of the search that is related to this request
    :type search_id: str

    """
    return web.Response(status=200)


async def get_video_suggestions(request: web.Request, query, limit=None) -> web.Response:
    """Get suggestions for a search term

    This endpoint provides autocomplete suggestions for partial search terms.

    :param query: Search term for which you want keyword suggestions
    :type query: str
    :param limit: Limit the number of the suggestions
    :type limit: int

    """
    return web.Response(status=200)


async def license_videos(request: web.Request, body, subscription_id=None, size=None, search_id=None) -> web.Response:
    """License videos

    This endpoint gets licenses for one or more videos. You must specify the video IDs in the body parameter and the size and subscription ID either in the query parameter or with each video ID in the body parameter. Values in the body parameter override values in the query parameters. The download links in the response are valid for 8 hours.

    :param body: List of videos to request licenses for and information about each license transaction; these values override the defaults in the query parameters
    :type body: dict | bytes
    :param subscription_id: The subscription ID to use for licensing
    :type subscription_id: str
    :param size: The size of the video to license
    :type size: str
    :param search_id: The Search ID that led to this licensing event
    :type search_id: str

    """
    body = LicenseVideoRequest.from_dict(body)
    return web.Response(status=200)


async def list_video_categories(request: web.Request, language=None) -> web.Response:
    """List video categories

    This endpoint lists the categories (Shutterstock-assigned genres) that videos can belong to.

    :param language: Language for the keywords and categories in the response
    :type language: dict | bytes

    """
    language = .from_dict(language)
    return web.Response(status=200)


async def rename_video_collection(request: web.Request, id, body) -> web.Response:
    """Rename video collections

    This endpoint sets a new name for a collection.

    :param id: The ID of the collection to rename
    :type id: str
    :param body: The new name for the collection
    :type body: dict | bytes

    """
    body = CollectionUpdateRequest.from_dict(body)
    return web.Response(status=200)


async def search_videos(request: web.Request, added_date=None, added_date_start=None, added_date_end=None, aspect_ratio=None, category=None, contributor=None, contributor_country=None, duration=None, duration_from=None, duration_to=None, fps=None, fps_from=None, fps_to=None, keyword_safe_search=None, language=None, license=None, model=None, page=None, per_page=None, people_age=None, people_ethnicity=None, people_gender=None, people_number=None, people_model_released=None, query=None, resolution=None, safe=None, sort=None, view=None) -> web.Response:
    """Search for videos

    This endpoint searches for videos. If you specify more than one search parameter, the API uses an AND condition. Array parameters can be specified multiple times; in this case, the API uses an AND or an OR condition with those values, depending on the parameter. You can also filter search terms out in the &#x60;query&#x60; parameter by prefixing the term with NOT.

    :param added_date: Show videos added on the specified date
    :type added_date: str
    :param added_date_start: Show videos added on or after the specified date
    :type added_date_start: str
    :param added_date_end: Show videos added before the specified date
    :type added_date_end: str
    :param aspect_ratio: Show videos with the specified aspect ratio
    :type aspect_ratio: str
    :param category: Show videos with the specified Shutterstock-defined category; specify a category name or ID
    :type category: str
    :param contributor: Show videos with the specified artist names or IDs
    :type contributor: List[str]
    :param contributor_country: Show videos from contributors in one or more specified countries
    :type contributor_country: List[str]
    :param duration: (Deprecated; use duration_from and duration_to instead) Show videos with the specified duration in seconds
    :type duration: int
    :param duration_from: Show videos with the specified duration or longer in seconds
    :type duration_from: int
    :param duration_to: Show videos with the specified duration or shorter in seconds
    :type duration_to: int
    :param fps: (Deprecated; use fps_from and fps_to instead) Show videos with the specified frames per second
    :type fps: 
    :param fps_from: Show videos with the specified frames per second or more
    :type fps_from: 
    :param fps_to: Show videos with the specified frames per second or fewer
    :type fps_to: 
    :param keyword_safe_search: Hide results with potentially unsafe keywords
    :type keyword_safe_search: bool
    :param language: Set query and result language (uses Accept-Language header if not set)
    :type language: dict | bytes
    :param license: Show only videos with the specified license or licenses
    :type license: List[str]
    :param model: Show videos with each of the specified models
    :type model: List[str]
    :param page: Page number
    :type page: int
    :param per_page: Number of results per page
    :type per_page: int
    :param people_age: Show videos that feature people of the specified age range
    :type people_age: str
    :param people_ethnicity: Show videos with people of the specified ethnicities
    :type people_ethnicity: List[str]
    :param people_gender: Show videos with people with the specified gender
    :type people_gender: str
    :param people_number: Show videos with the specified number of people
    :type people_number: int
    :param people_model_released: Show only videos of people with a signed model release
    :type people_model_released: bool
    :param query: One or more search terms separated by spaces; you can use NOT to filter out videos that match a term
    :type query: str
    :param resolution: Show videos with the specified resolution
    :type resolution: str
    :param safe: Enable or disable safe search
    :type safe: bool
    :param sort: Sort by one of these categories
    :type sort: str
    :param view: Amount of detail to render in the response
    :type view: str

    """
    added_date = util.deserialize_date(added_date)
    added_date_start = util.deserialize_date(added_date_start)
    added_date_end = util.deserialize_date(added_date_end)
    language = .from_dict(language)
    return web.Response(status=200)
