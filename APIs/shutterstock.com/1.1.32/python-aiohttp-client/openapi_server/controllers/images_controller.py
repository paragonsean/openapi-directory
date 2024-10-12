from typing import List, Dict
from aiohttp import web

from openapi_server.models.bulk_image_search_results import BulkImageSearchResults
from openapi_server.models.bulk_search_images_contributor_country_parameter import BulkSearchImagesContributorCountryParameter
from openapi_server.models.bulk_search_images_region_parameter import BulkSearchImagesRegionParameter
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
from openapi_server.models.image import Image
from openapi_server.models.image_data_list import ImageDataList
from openapi_server.models.image_search_results import ImageSearchResults
from openapi_server.models.language import Language
from openapi_server.models.license_image_request import LicenseImageRequest
from openapi_server.models.license_image_result_data_list import LicenseImageResultDataList
from openapi_server.models.recommendation_data_list import RecommendationDataList
from openapi_server.models.redownload_image import RedownloadImage
from openapi_server.models.search_entities_request import SearchEntitiesRequest
from openapi_server.models.search_entities_response import SearchEntitiesResponse
from openapi_server.models.search_image import SearchImage
from openapi_server.models.suggestions import Suggestions
from openapi_server.models.updated_media_data_list import UpdatedMediaDataList
from openapi_server.models.url import Url
from openapi_server import util


async def add_image_collection_items(request: web.Request, id, body) -> web.Response:
    """Add images to collections

    This endpoint adds one or more images to a collection by image IDs.

    :param id: Collection ID
    :type id: str
    :param body: Array of image IDs to add to the collection
    :type body: dict | bytes

    """
    body = CollectionItemRequest.from_dict(body)
    return web.Response(status=200)


async def bulk_search_images(request: web.Request, body, added_date=None, added_date_start=None, aspect_ratio_min=None, aspect_ratio_max=None, aspect_ratio=None, added_date_end=None, category=None, color=None, contributor=None, contributor_country=None, fields=None, height=None, height_from=None, height_to=None, image_type=None, keyword_safe_search=None, language=None, license=None, model=None, orientation=None, page=None, per_page=None, people_model_released=None, people_age=None, people_ethnicity=None, people_gender=None, people_number=None, region=None, safe=None, sort=None, spellcheck_query=None, view=None, width=None, width_from=None, width_to=None) -> web.Response:
    """Run multiple image searches

    This endpoint runs up to 5 image searches in a single request and returns up to 20 results per search. You can provide global search parameters in the query parameters and override them for each search in the body parameter. The query and body parameters are the same as in the &#x60;GET /v2/images/search&#x60; endpoint.

    :param body: List of queries to request results for and filters to apply per query; these values override the defaults in the query parameters
    :type body: list | bytes
    :param added_date: Show images added on the specified date
    :type added_date: str
    :param added_date_start: Show images added on or after the specified date
    :type added_date_start: str
    :param aspect_ratio_min: Show images with the specified aspect ratio or higher, using a positive decimal of the width divided by the height, such as 1.7778 for a 16:9 image
    :type aspect_ratio_min: 
    :param aspect_ratio_max: Show images with the specified aspect ratio or lower, using a positive decimal of the width divided by the height, such as 1.7778 for a 16:9 image
    :type aspect_ratio_max: 
    :param aspect_ratio: Show images with the specified aspect ratio, using a positive decimal of the width divided by the height, such as 1.7778 for a 16:9 image
    :type aspect_ratio: 
    :param added_date_end: Show images added before the specified date
    :type added_date_end: str
    :param category: Show images with the specified Shutterstock-defined category; specify a category name or ID
    :type category: str
    :param color: Specify either a hexadecimal color in the format &#39;4F21EA&#39; or &#39;grayscale&#39;; the API returns images that use similar colors
    :type color: str
    :param contributor: Show images with the specified contributor names or IDs, allows multiple
    :type contributor: List[str]
    :param contributor_country: Show images from contributors in one or more specified countries, or start with NOT to exclude a country from the search
    :type contributor_country: dict | bytes
    :param fields: Fields to display in the response; see the documentation for the fields parameter in the overview section
    :type fields: str
    :param height: (Deprecated; use height_from and height_to instead) Show images with the specified height
    :type height: int
    :param height_from: Show images with the specified height or larger, in pixels
    :type height_from: int
    :param height_to: Show images with the specified height or smaller, in pixels
    :type height_to: int
    :param image_type: Show images of the specified type
    :type image_type: List[str]
    :param keyword_safe_search: Hide results with potentially unsafe keywords
    :type keyword_safe_search: bool
    :param language: Set query and result language (uses Accept-Language header if not set)
    :type language: dict | bytes
    :param license: Show only images with the specified license
    :type license: List[str]
    :param model: Show image results with the specified model IDs
    :type model: List[str]
    :param orientation: Show image results with horizontal or vertical orientation
    :type orientation: str
    :param page: Page number
    :type page: int
    :param per_page: Number of results per page
    :type per_page: int
    :param people_model_released: Show images of people with a signed model release
    :type people_model_released: bool
    :param people_age: Show images that feature people of the specified age category
    :type people_age: str
    :param people_ethnicity: Show images with people of the specified ethnicities, or start with NOT to show images without those ethnicities
    :type people_ethnicity: List[str]
    :param people_gender: Show images with people of the specified gender
    :type people_gender: str
    :param people_number: Show images with the specified number of people
    :type people_number: int
    :param region: Raise or lower search result rankings based on the result&#39;s relevance to a specified region; you can provide a country code or an IP address from which the API infers a country
    :type region: dict | bytes
    :param safe: Enable or disable safe search
    :type safe: bool
    :param sort: Sort by
    :type sort: str
    :param spellcheck_query: Spellcheck the search query and return results on suggested spellings
    :type spellcheck_query: bool
    :param view: Amount of detail to render in the response
    :type view: str
    :param width: (Deprecated; use width_from and width_to instead) Show images with the specified width
    :type width: int
    :param width_from: Show images with the specified width or larger, in pixels
    :type width_from: int
    :param width_to: Show images with the specified width or smaller, in pixels
    :type width_to: int

    """
    body = [SearchImage.from_dict(d) for d in body]
    added_date = util.deserialize_date(added_date)
    added_date_start = util.deserialize_date(added_date_start)
    added_date_end = util.deserialize_date(added_date_end)
    contributor_country = .from_dict(contributor_country)
    language = .from_dict(language)
    region = .from_dict(region)
    return web.Response(status=200)


async def create_image_collection(request: web.Request, body) -> web.Response:
    """Create image collections

    This endpoint creates one or more image collections (lightboxes). To add images to the collections, use &#x60;POST /v2/images/collections/{id}/items&#x60;.

    :param body: The names of the new collections
    :type body: dict | bytes

    """
    body = CollectionCreateRequest.from_dict(body)
    return web.Response(status=200)


async def delete_image_collection(request: web.Request, id) -> web.Response:
    """Delete image collections

    This endpoint deletes an image collection.

    :param id: Collection ID
    :type id: str

    """
    return web.Response(status=200)


async def delete_image_collection_items(request: web.Request, id, item_id=None) -> web.Response:
    """Remove images from collections

    This endpoint removes one or more images from a collection.

    :param id: Collection ID
    :type id: str
    :param item_id: One or more image IDs to remove from the collection
    :type item_id: List[str]

    """
    return web.Response(status=200)


async def download_image(request: web.Request, id, body) -> web.Response:
    """Download images

    This endpoint redownloads images that you have already received a license for. The download links in the response are valid for 8 hours.

    :param id: License ID
    :type id: str
    :param body: Information about the images to redownload
    :type body: dict | bytes

    """
    body = RedownloadImage.from_dict(body)
    return web.Response(status=200)


async def get_featured_image_collection(request: web.Request, id, embed=None, asset_hint=None) -> web.Response:
    """Get the details of featured image collections

    This endpoint gets more detailed information about a featured collection, including its cover image and timestamps for its creation and most recent update. To get the images, use &#x60;GET /v2/images/collections/featured/{id}/items&#x60;.

    :param id: Collection ID
    :type id: str
    :param embed: Which sharing information to include in the response, such as a URL to the collection
    :type embed: str
    :param asset_hint: Cover image size
    :type asset_hint: str

    """
    return web.Response(status=200)


async def get_featured_image_collection_items(request: web.Request, id, page=None, per_page=None) -> web.Response:
    """Get the contents of featured image collections

    This endpoint lists the IDs of images in a featured collection and the date that each was added.

    :param id: Collection ID
    :type id: str
    :param page: Page number
    :type page: int
    :param per_page: Number of results per page
    :type per_page: int

    """
    return web.Response(status=200)


async def get_featured_image_collection_list(request: web.Request, embed=None, type=None, asset_hint=None) -> web.Response:
    """List featured image collections

    This endpoint lists featured collections of specific types and a name and cover image for each collection.

    :param embed: Which sharing information to include in the response, such as a URL to the collection
    :type embed: str
    :param type: The types of collections to return
    :type type: List[str]
    :param asset_hint: Cover image size
    :type asset_hint: str

    """
    return web.Response(status=200)


async def get_image(request: web.Request, id, language=None, view=None, search_id=None) -> web.Response:
    """Get details about images

    This endpoint shows information about an image, including a URL to a preview image and the sizes that it is available in.

    :param id: Image ID
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


async def get_image_collection(request: web.Request, id, embed=None, share_code=None) -> web.Response:
    """Get the details of image collections

    This endpoint gets more detailed information about a collection, including its cover image and timestamps for its creation and most recent update. To get the images in collections, use &#x60;GET /v2/images/collections/{id}/items&#x60;.

    :param id: Collection ID
    :type id: str
    :param embed: Which sharing information to include in the response, such as a URL to the collection
    :type embed: List[str]
    :param share_code: Code to retrieve a shared collection
    :type share_code: str

    """
    return web.Response(status=200)


async def get_image_collection_items(request: web.Request, id, page=None, per_page=None, share_code=None, sort=None) -> web.Response:
    """Get the contents of image collections

    This endpoint lists the IDs of images in a collection and the date that each was added.

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


async def get_image_collection_list(request: web.Request, embed=None, page=None, per_page=None) -> web.Response:
    """List image collections

    This endpoint lists your collections of images and their basic attributes.

    :param embed: Which sharing information to include in the response, such as a URL to the collection
    :type embed: List[str]
    :param page: Page number
    :type page: int
    :param per_page: Number of results per page
    :type per_page: int

    """
    return web.Response(status=200)


async def get_image_keyword_suggestions(request: web.Request, body) -> web.Response:
    """Get keywords from text

    This endpoint returns up to 10 important keywords from a block of plain text.

    :param body: Plain text to extract keywords from
    :type body: dict | bytes

    """
    body = SearchEntitiesRequest.from_dict(body)
    return web.Response(status=200)


async def get_image_license_list(request: web.Request, image_id=None, license=None, page=None, per_page=None, sort=None, username=None, start_date=None, end_date=None, download_availability=None, team_history=None) -> web.Response:
    """List image licenses

    This endpoint lists existing licenses.

    :param image_id: Show licenses for the specified image ID
    :type image_id: str
    :param license: Show images that are available with the specified license, such as &#x60;standard&#x60; or &#x60;enhanced&#x60;; prepending a &#x60;-&#x60; sign excludes results from that license
    :type license: str
    :param page: Page number
    :type page: int
    :param per_page: Number of results per page
    :type per_page: int
    :param sort: Sort order
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


async def get_image_list(request: web.Request, id, view=None, search_id=None) -> web.Response:
    """List images

    This endpoint lists information about one or more images, including the available sizes.

    :param id: One or more image IDs
    :type id: List[str]
    :param view: Amount of detail to render in the response
    :type view: str
    :param search_id: The ID of the search that is related to this request
    :type search_id: str

    """
    return web.Response(status=200)


async def get_image_recommendations(request: web.Request, id, max_items=None, safe=None) -> web.Response:
    """List recommended images

    This endpoint returns images that customers put in the same collection as the specified image IDs.

    :param id: Image IDs
    :type id: List[str]
    :param max_items: Maximum number of results returned in the response
    :type max_items: int
    :param safe: Restrict results to safe images
    :type safe: bool

    """
    return web.Response(status=200)


async def get_image_suggestions(request: web.Request, query, limit=None) -> web.Response:
    """Get suggestions for a search term

    This endpoint provides autocomplete suggestions for partial search terms.

    :param query: Search term for which you want keyword suggestions
    :type query: str
    :param limit: Limit the number of suggestions
    :type limit: int

    """
    return web.Response(status=200)


async def get_updated_images(request: web.Request, type=None, start_date=None, end_date=None, interval=None, page=None, per_page=None, sort=None) -> web.Response:
    """List updated images

    This endpoint lists images that have been updated in the specified time period to update content management systems (CMS) or digital asset management (DAM) systems. In most cases, use the &#x60;interval&#x60; parameter to show images that were updated recently, but you can also use the &#x60;start_date&#x60; and &#x60;end_date&#x60; parameters to specify a range of no more than three days. Do not use the &#x60;interval&#x60; parameter with either &#x60;start_date&#x60; or &#x60;end_date&#x60;.

    :param type: Show images that were added, deleted, or edited; by default, the endpoint returns images that were updated in any of these ways
    :type type: List[str]
    :param start_date: Show images updated on or after the specified date
    :type start_date: str
    :param end_date: Show images updated before the specified date
    :type end_date: str
    :param interval: Show images updated in the specified time period, where the time period is an interval (like SQL INTERVAL) such as 1 DAY, 6 HOUR, or 30 MINUTE; the default is 1 HOUR, which shows images that were updated in the hour preceding the request
    :type interval: str
    :param page: Page number
    :type page: int
    :param per_page: Number of results per page
    :type per_page: int
    :param sort: Sort order
    :type sort: str

    """
    start_date = util.deserialize_date(start_date)
    end_date = util.deserialize_date(end_date)
    return web.Response(status=200)


async def license_images(request: web.Request, body, subscription_id=None, format=None, size=None, search_id=None) -> web.Response:
    """License images

    This endpoint gets licenses for one or more images. You must specify the image IDs in the body parameter and other details like the format, size, and subscription ID either in the query parameter or with each image ID in the body parameter. Values in the body parameter override values in the query parameters. The download links in the response are valid for 8 hours.

    :param body: List of images to request licenses for and information about each license transaction; these values override the defaults in the query parameters
    :type body: dict | bytes
    :param subscription_id: Subscription ID to use to license the image
    :type subscription_id: str
    :param format: (Deprecated) Image format
    :type format: str
    :param size: Image size
    :type size: str
    :param search_id: Search ID that was provided in the results of an image search
    :type search_id: str

    """
    body = LicenseImageRequest.from_dict(body)
    return web.Response(status=200)


async def list_image_categories(request: web.Request, language=None) -> web.Response:
    """List image categories

    This endpoint lists the categories (Shutterstock-assigned genres) that images can belong to.

    :param language: Language for the keywords and categories in the response
    :type language: dict | bytes

    """
    language = .from_dict(language)
    return web.Response(status=200)


async def list_similar_images(request: web.Request, id, language=None, page=None, per_page=None, view=None) -> web.Response:
    """List similar images

    This endpoint returns images that are visually similar to an image that you specify.

    :param id: Image ID
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


async def rename_image_collection(request: web.Request, id, body) -> web.Response:
    """Rename image collections

    This endpoint sets a new name for an image collection.

    :param id: Collection ID
    :type id: str
    :param body: The new name for the collection
    :type body: dict | bytes

    """
    body = CollectionUpdateRequest.from_dict(body)
    return web.Response(status=200)


async def search_images(request: web.Request, added_date=None, added_date_start=None, aspect_ratio_min=None, aspect_ratio_max=None, aspect_ratio=None, ai_search=None, ai_labels_limit=None, ai_industry=None, ai_objective=None, added_date_end=None, category=None, color=None, contributor=None, contributor_country=None, fields=None, height=None, height_from=None, height_to=None, image_type=None, keyword_safe_search=None, language=None, license=None, model=None, orientation=None, page=None, per_page=None, people_model_released=None, people_age=None, people_ethnicity=None, people_gender=None, people_number=None, query=None, region=None, safe=None, sort=None, spellcheck_query=None, view=None, width=None, width_from=None, width_to=None) -> web.Response:
    """Search for images

    This endpoint searches for images. If you specify more than one search parameter, the API uses an AND condition. Array parameters can be specified multiple times; in this case, the API uses an AND or an OR condition with those values, depending on the parameter. You can also filter search terms out in the &#x60;query&#x60; parameter by prefixing the term with NOT. Free API accounts show results only from a limited library of media, not the full Shutterstock media library. Also, the number of search fields they can use in a request is limited.

    :param added_date: Show images added on the specified date
    :type added_date: str
    :param added_date_start: Show images added on or after the specified date
    :type added_date_start: str
    :param aspect_ratio_min: Show images with the specified aspect ratio or higher, using a positive decimal of the width divided by the height, such as 1.7778 for a 16:9 image
    :type aspect_ratio_min: 
    :param aspect_ratio_max: Show images with the specified aspect ratio or lower, using a positive decimal of the width divided by the height, such as 1.7778 for a 16:9 image
    :type aspect_ratio_max: 
    :param aspect_ratio: Show images with the specified aspect ratio, using a positive decimal of the width divided by the height, such as 1.7778 for a 16:9 image
    :type aspect_ratio: 
    :param ai_search: Set to true and specify the &#x60;ai_objective&#x60; and &#x60;ai_industry&#x60; parameters to use AI-powered search; the API returns information about how well images meet the objective for the industry 
    :type ai_search: bool
    :param ai_labels_limit: For AI-powered search, specify the maximum number of labels to return
    :type ai_labels_limit: int
    :param ai_industry: For AI-powered search, specify the industry to target; requires that the &#x60;ai_search&#x60; parameter is set to true
    :type ai_industry: str
    :param ai_objective: For AI-powered search, specify the goal of the media; requires that the &#x60;ai_search&#x60; parameter is set to true
    :type ai_objective: str
    :param added_date_end: Show images added before the specified date
    :type added_date_end: str
    :param category: Show images with the specified Shutterstock-defined category; specify a category name or ID
    :type category: str
    :param color: Specify either a hexadecimal color in the format &#39;4F21EA&#39; or &#39;grayscale&#39;; the API returns images that use similar colors
    :type color: str
    :param contributor: Show images with the specified contributor names or IDs, allows multiple
    :type contributor: List[str]
    :param contributor_country: Show images from contributors in one or more specified countries, or start with NOT to exclude a country from the search
    :type contributor_country: dict | bytes
    :param fields: Fields to display in the response; see the documentation for the fields parameter in the overview section
    :type fields: str
    :param height: (Deprecated; use height_from and height_to instead) Show images with the specified height
    :type height: int
    :param height_from: Show images with the specified height or larger, in pixels
    :type height_from: int
    :param height_to: Show images with the specified height or smaller, in pixels
    :type height_to: int
    :param image_type: Show images of the specified type
    :type image_type: List[str]
    :param keyword_safe_search: Hide results with potentially unsafe keywords
    :type keyword_safe_search: bool
    :param language: Set query and result language (uses Accept-Language header if not set)
    :type language: dict | bytes
    :param license: Show only images with the specified license
    :type license: List[str]
    :param model: Show image results with the specified model IDs
    :type model: List[str]
    :param orientation: Show image results with horizontal or vertical orientation
    :type orientation: str
    :param page: Page number
    :type page: int
    :param per_page: Number of results per page
    :type per_page: int
    :param people_model_released: Show images of people with a signed model release
    :type people_model_released: bool
    :param people_age: Show images that feature people of the specified age category
    :type people_age: str
    :param people_ethnicity: Show images with people of the specified ethnicities, or start with NOT to show images without those ethnicities
    :type people_ethnicity: List[str]
    :param people_gender: Show images with people of the specified gender
    :type people_gender: str
    :param people_number: Show images with the specified number of people
    :type people_number: int
    :param query: One or more search terms separated by spaces; you can use NOT to filter out images that match a term
    :type query: str
    :param region: Raise or lower search result rankings based on the result&#39;s relevance to a specified region; you can provide a country code or an IP address from which the API infers a country
    :type region: dict | bytes
    :param safe: Enable or disable safe search
    :type safe: bool
    :param sort: Sort by
    :type sort: str
    :param spellcheck_query: Spellcheck the search query and return results on suggested spellings
    :type spellcheck_query: bool
    :param view: Amount of detail to render in the response
    :type view: str
    :param width: (Deprecated; use width_from and width_to instead) Show images with the specified width
    :type width: int
    :param width_from: Show images with the specified width or larger, in pixels
    :type width_from: int
    :param width_to: Show images with the specified width or smaller, in pixels
    :type width_to: int

    """
    added_date = util.deserialize_date(added_date)
    added_date_start = util.deserialize_date(added_date_start)
    added_date_end = util.deserialize_date(added_date_end)
    contributor_country = .from_dict(contributor_country)
    language = .from_dict(language)
    region = .from_dict(region)
    return web.Response(status=200)
