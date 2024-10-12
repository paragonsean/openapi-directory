from typing import List, Dict
from aiohttp import web

from openapi_server.models.age_of_people_filter_type import AgeOfPeopleFilterType
from openapi_server.models.blended_image_sort_order import BlendedImageSortOrder
from openapi_server.models.collections_filter_type import CollectionsFilterType
from openapi_server.models.compositions_filter_type import CompositionsFilterType
from openapi_server.models.create_image_search_facets_fields import CreateImageSearchFacetsFields
from openapi_server.models.create_video_search_facets_fields import CreateVideoSearchFacetsFields
from openapi_server.models.creative_image_search_results import CreativeImageSearchResults
from openapi_server.models.creative_image_sort_order import CreativeImageSortOrder
from openapi_server.models.creative_images_field_values import CreativeImagesFieldValues
from openapi_server.models.creative_video_search_results import CreativeVideoSearchResults
from openapi_server.models.creative_video_sort_order import CreativeVideoSortOrder
from openapi_server.models.creative_videos_field_values import CreativeVideosFieldValues
from openapi_server.models.editorial_graphical_style import EditorialGraphicalStyle
from openapi_server.models.editorial_image_search_facets_fields import EditorialImageSearchFacetsFields
from openapi_server.models.editorial_image_search_results import EditorialImageSearchResults
from openapi_server.models.editorial_images_field_values import EditorialImagesFieldValues
from openapi_server.models.editorial_segment_contract import EditorialSegmentContract
from openapi_server.models.editorial_video_search_facets_fields import EditorialVideoSearchFacetsFields
from openapi_server.models.editorial_video_search_results import EditorialVideoSearchResults
from openapi_server.models.editorial_video_type import EditorialVideoType
from openapi_server.models.editorial_videos_field_values import EditorialVideosFieldValues
from openapi_server.models.ethnicity_filter_type import EthnicityFilterType
from openapi_server.models.event_field_values import EventFieldValues
from openapi_server.models.event_search_sort_order import EventSearchSortOrder
from openapi_server.models.events_search_result import EventsSearchResult
from openapi_server.models.graphical_style import GraphicalStyle
from openapi_server.models.graphical_styles_filter_type import GraphicalStylesFilterType
from openapi_server.models.image_orientation_request import ImageOrientationRequest
from openapi_server.models.image_search_item_search_results import ImageSearchItemSearchResults
from openapi_server.models.image_techniques_filter_type import ImageTechniquesFilterType
from openapi_server.models.images_field_values import ImagesFieldValues
from openapi_server.models.license_model_video_request import LicenseModelVideoRequest
from openapi_server.models.number_of_people_filter_type import NumberOfPeopleFilterType
from openapi_server.models.release_status import ReleaseStatus
from openapi_server.models.search_by_image_resource_results import SearchByImageResourceResults
from openapi_server.models.search_file_type import SearchFileType
from openapi_server.models.sort_order import SortOrder
from openapi_server.models.tee_shirt_size import TeeShirtSize
from openapi_server.models.video_aspect_ratio_filter_type import VideoAspectRatioFilterType
from openapi_server.models.video_formats_request import VideoFormatsRequest
from openapi_server.models.video_frame_rates import VideoFrameRates
from openapi_server.models.video_orientation_request import VideoOrientationRequest
from openapi_server.models.viewpoints_filter_type import ViewpointsFilterType
from openapi_server import util


async def v3_search_by_image_uploads_file_name_put(request: web.Request, file_name, body=None) -> web.Response:
    """Upload image for use by the search creative images/videos operations

    

    :param file_name: 
    :type file_name: str
    :param body: 
    :type body: str

    """
    return web.Response(status=200)


async def v3_search_events_get(request: web.Request, accept_language=None, gi_country_code=None, editorial_segment=None, date_from=None, date_to=None, fields=None, page=None, page_size=None, phrase=None, sort_order=None) -> web.Response:
    """Search for events

    Use this endpoint to search Getty Images news, sports and entertainment events. Getty Images photographers and videographers cover editorially relevant events occurring around the world.  All images or video clips produced in association with an event, are assigned the same EventID. EventIDs are part of the meta-data returned in Search Results. Only content produced under a Getty Images brand name (Getty Images News, Getty Images Sports, Getty Images Entertainment, Film Magic, Wire Image) will be consistently assigned an EventID. The Event framework may also be used to group similar content, such as \&quot;Hats from the Royal Wedding\&quot; or \&quot;Odd-ballOffbeat images of the week\&quot;.     You&#39;ll need an API key and access token to use this resource.   You can show different information in the response by specifying values on the \&quot;fields\&quot; parameter (see details below). You can search with only an API key, and that will give you search results that are equivalent to doing a search on the GettyImages.com site without being logged in (anonymous search).  If you are a Getty Images API customer and would like to ensure that your API searches return only assets that you have a license to use, you need to also include an authorization token in the header of your request.  Please consult our [Authorization FAQ](http://developers.gettyimages.com/en/authorization-faq.html) for more information on authorization tokens, and our [Authorization Workflows](https://github.com/gettyimages/gettyimages-api/blob/master/OAuth2Workflow.md) for code examples of getting a token. 

    :param accept_language: Provide a header to specify the language of result values. Supported values: cs (iStock only), de, en-GB, en-US, es, fi (iStock only), fr, hu (iStock only), id (iStock only), it, ja, ko (creative assets only), nl, pl (creative assets only), pt-BR, pt-PT, ro (iStock only), ru (creative assets only), sv, th (iStock only), tr, uk (iStock only), vi (iStock only), zh-HK (creative assets only).
    :type accept_language: str
    :param gi_country_code: Receive regionally relevant search results based on the value specified. Accepts only ISO Alpha-3 country codes. The Countries operation can be used to retrieve the codes.
    :type gi_country_code: str
    :param editorial_segment: Filters to events with a matching editorial segment.
    :type editorial_segment: dict | bytes
    :param date_from: Filters to events that start on or after this date. Use ISO 8601 format (e.g., 1999-12-31). Defaults to UTC unless otherwise specified.
    :type date_from: str
    :param date_to: Filters to events that start on or before this date. Use ISO 8601 format (e.g., 1999-12-31). Defaults to UTC unless otherwise specified.
    :type date_to: str
    :param fields: Specifies fields to return. Default set is &#39;id&#39;,&#39;name&#39;,&#39;start_date&#39;.
    :type fields: list | bytes
    :param page: Request results starting at a page number (default is 1, maximum is 50).
    :type page: int
    :param page_size: Request number of events to return in each page. Default is 30, maximum page_size is 100.
    :type page_size: int
    :param phrase: Filters to events related to this phrase
    :type phrase: str
    :param sort_order: Specifies the order in which to sort the results. Default is &#x60;newest&#x60;.
    :type sort_order: dict | bytes

    """
    editorial_segment = .from_dict(editorial_segment)
    date_from = util.deserialize_datetime(date_from)
    date_to = util.deserialize_datetime(date_to)
    fields = [EventFieldValues.from_dict(d) for d in fields]
    sort_order = .from_dict(sort_order)
    return web.Response(status=200)


async def v3_search_images_creative_by_image_get(request: web.Request, accept_language=None, gi_country_code=None, asset_id=None, exclude_editorial_use_only=None, facet_fields=None, facet_max_count=None, fields=None, image_url=None, include_facets=None, page=None, page_size=None, product_types=None) -> web.Response:
    """Search for creative images based on url

    Search for **similar creative images** by passing an &#x60;image_url&#x60; to an uploaded image OR an &#x60;asset_id&#x60; of an asset in our catalog.  All responses will have the &#x60;exclude_nudity&#x60; filter automatically applied.  ## Searching by URL  Before calling the search by image endpoint, an image in JPEG format must be uploaded to &#x60;https://api.gettyimages.com/v3/search/by-image/uploads/{CLIENT_IMAGE.jpg}&#x60;, where the client defines the &#x60;{CLIENT_IMAGE.jpg}&#x60; portion of the URL.  For example, using cURL:  &#x60;&#x60;&#x60; sh curl -i -X PUT https://api.gettyimages.com/v3/search/by-image/uploads/my-test-image.jpg -H &#39;Content-Type: image/jpeg&#39; -H &#39;Api-Key: API_KEY&#39; --data-binary \&quot;@testimage.jpg\&quot; &#x60;&#x60;&#x60;  Once the image has been uploaded, use the full URL in the &#x60;image_url&#x60; parameter, e.g. &#x60;image_url&#x3D;https://api.gettyimages.com/v3/search/by-image/uploads/my-test-image.jpg&#x60;.  - Uploaded files must be 10MB or smaller. - Uploads to the same URL will overwrite each other, so ensure that the client application is handling naming uniqueness appropriately. - Uploads expire after 24 hours. - Uploads and searches must be performed using the _same_ API Key.  ## Searching by asset id  When searching by &#x60;asset_id&#x60;, any image or video asset id in the Getty/iStock catalog can be used as the source for similar images. 

    :param accept_language: Provide a header to specify the language of result values. Supported values: cs (iStock only), de, en-GB, en-US, es, fi (iStock only), fr, hu (iStock only), id (iStock only), it, ja, ko (creative assets only), nl, pl (creative assets only), pt-BR, pt-PT, ro (iStock only), ru (creative assets only), sv, th (iStock only), tr, uk (iStock only), vi (iStock only), zh-HK (creative assets only).
    :type accept_language: str
    :param gi_country_code: Receive regionally relevant search results based on the value specified. Accepts only ISO Alpha-3 country codes. The Countries operation can be used to retrieve the codes.
    :type gi_country_code: str
    :param asset_id: Specifies the Getty image id to use in the search.
    :type asset_id: str
    :param exclude_editorial_use_only: Exclude images that are only available for editorial (non-commercial) use. Default value is false.
    :type exclude_editorial_use_only: bool
    :param facet_fields: Specifies the facets to return in the response. Facets provide additional search parameters to refine your results.                      The include_facets parameter must be set to \&quot;true\&quot; for facets to be returned.
    :type facet_fields: list | bytes
    :param facet_max_count: Specifies the maximum number of facets to return per type. Default is 300.
    :type facet_max_count: int
    :param fields: Specifies fields to return. Defaults to &#39;summary_set&#39;. NOTE: Bytes, height, and width returned by &#39;download_sizes&#39; field are estimates.
    :type fields: list | bytes
    :param image_url: Specifies the location of the image to use in the search.
    :type image_url: str
    :param include_facets: Specifies whether or not to include facets in the result set. Default is \&quot;false\&quot;.
    :type include_facets: bool
    :param page: Request results starting at a page number (default is 1).
    :type page: int
    :param page_size: Request number of images to return in each page. Default is 30, maximum page_size is 100.
    :type page_size: int
    :param product_types: Filter images to those from one of your product types.                       Allowed values are easyaccess, imagepack, premiumaccess and royaltyfreesubscription.                       If you have more than one instance of a product, you may also include the ID of the product instance you wish to filter on.                       For example, some users may have more than one premiumaccess product, so the product_types value would be premiumaccess:1234.                       Product ID can be obtained from the GET /products response.
    :type product_types: List[str]

    """
    facet_fields = [CreateImageSearchFacetsFields.from_dict(d) for d in facet_fields]
    fields = [CreativeImagesFieldValues.from_dict(d) for d in fields]
    return web.Response(status=200)


async def v3_search_images_creative_get(request: web.Request, accept_language=None, gi_country_code=None, age_of_people=None, artists=None, collection_codes=None, collections_filter_type=None, color=None, compositions=None, download_product=None, embed_content_only=None, ethnicity=None, exclude_keyword_ids=None, exclude_nudity=None, exclude_editorial_use_only=None, fields=None, file_types=None, graphical_styles=None, graphical_styles_filter_type=None, include_related_searches=None, keyword_ids=None, minimum_size=None, number_of_people=None, orientations=None, page=None, page_size=None, phrase=None, safe_search=None, sort_order=None, facet_fields=None, include_facets=None, facet_max_count=None) -> web.Response:
    """Search for creative images only

    Use this endpoint to search our contemporary stock photos, illustrations and archival images.  You&#39;ll need an API key and access token to use this resource.   You can show different information in the response by specifying values on the \&quot;fields\&quot; parameter (see details below). You can search with only an API key, and that will give you search results that are equivalent to doing a search on the GettyImages.com site without being logged in (anonymous search).  If you are a Getty Images API customer and would like to ensure that your API searches return only assets that you have a license to use, you need to also include an authorization token in the header of your request.  Please consult our [Authorization FAQ](http://developers.gettyimages.com/en/authorization-faq.html) for more information on authorization tokens, and our [Authorization Workflows](https://github.com/gettyimages/gettyimages-api/blob/master/OAuth2Workflow.md) for code examples of getting a token.  Search requests without a phrase parameter are not supported and may not always work.  ## Working with Fields Sets  Fields sets are used in the **fields** request parameter to receive a suite of metadata fields. The following fields sets are available:  #### Summary Fields Set  The **summary_set** query string parameter fields value represents a small batch of metadata fields that are often used to  build search response results. The following fields are provided for every image in your result set when you include **summary_set** in your request.  &#x60;&#x60;&#x60; {     \&quot;images\&quot;:      [         \&quot;asset_family\&quot;,         \&quot;caption\&quot;,         \&quot;collection_code\&quot;,         \&quot;collection_id\&quot;,         \&quot;collection_name\&quot;,         \&quot;display_sizes\&quot;:          [             {                 \&quot;name\&quot;: \&quot;thumb\&quot;             }         ],         \&quot;license_model\&quot;,         \&quot;max_dimensions\&quot;,         \&quot;title\&quot;     ] } &#x60;&#x60;&#x60;  #### Detail Fields Set  The **detail_set** query string parameter fields value represents a large batch of metadata fields that are often used to  build a detailed view of images. The following fields are provided for every image in your result set when you include **detail_set** in your request.  &#x60;&#x60;&#x60; {     \&quot;images\&quot;:      [         \&quot;allowed_use\&quot;,         \&quot;artist\&quot;,         \&quot;asset_family\&quot;,         \&quot;call_for_image\&quot;,         \&quot;caption\&quot;,         \&quot;collection_code\&quot;,         \&quot;collection_id\&quot;,         \&quot;collection_name\&quot;,         \&quot;copyright\&quot;,         \&quot;date_created\&quot;,         \&quot;display_sizes\&quot;:          [             {                 \&quot;name\&quot;: \&quot;comp\&quot;             },             {                 \&quot;name\&quot;: \&quot;preview\&quot;             },             {                 \&quot;name\&quot;: \&quot;thumb\&quot;             }         ],         \&quot;editorial_segments\&quot;,         \&quot;event_ids\&quot;,         \&quot;graphical_style\&quot;,         \&quot;license_model\&quot;,         \&quot;max_dimensions\&quot;,         \&quot;orientation\&quot;,         \&quot;product_types\&quot;,         \&quot;quality_rank\&quot;,         \&quot;referral_destinations\&quot;,         \&quot;title\&quot;     ] ] &#x60;&#x60;&#x60;  #### Display Fields Set  The **display_set** query string parameter fields value represents the fields that provide you with URLs for the low resolution files that are most frequently used to build a UI displaying search results. The following fields are provided for every image  in your result set when you include **display_set** in your request.  The URI provided is subject to change at any time and must be used as-is with no modification.  &#x60;&#x60;&#x60; {     \&quot;images\&quot;:     [         \&quot;display_sizes\&quot;:          [             {                 \&quot;is_watermarked\&quot;: &lt;boolean&gt;,                 \&quot;name\&quot;: \&quot;comp\&quot;,                 \&quot;uri\&quot;: \&quot;&lt;link&gt;\&quot;             },             {                 \&quot;is_watermarked\&quot;: &lt;boolean&gt;,                 \&quot;name\&quot;: \&quot;preview\&quot;,                 \&quot;uri\&quot;: \&quot;&lt;link&gt;\&quot;             },             {                 \&quot;is_watermarked\&quot;: &lt;boolean&gt;,                 \&quot;name\&quot;: \&quot;thumb\&quot;,                 \&quot;uri\&quot;: \&quot;&lt;link&gt;\&quot;             }         ]     ] } &#x60;&#x60;&#x60;

    :param accept_language: Provide a header to specify the language of result values. Supported values: cs (iStock only), de, en-GB, en-US, es, fi (iStock only), fr, hu (iStock only), id (iStock only), it, ja, ko (creative assets only), nl, pl (creative assets only), pt-BR, pt-PT, ro (iStock only), ru (creative assets only), sv, th (iStock only), tr, uk (iStock only), vi (iStock only), zh-HK (creative assets only).
    :type accept_language: str
    :param gi_country_code: Receive regionally relevant search results based on the value specified. Accepts only ISO Alpha-3 country codes. The Countries operation can be used to retrieve the codes.
    :type gi_country_code: str
    :param age_of_people: Filter based on the age of individuals in an image.
    :type age_of_people: list | bytes
    :param artists: Search for images by specific artists (free-text, comma-separated list of artists).
    :type artists: str
    :param collection_codes: Filter by collection codes (comma-separated list). Include or exclude based on collections_filter_type.
    :type collection_codes: List[str]
    :param collections_filter_type: Use to include or exclude collections from search. The default is include
    :type collections_filter_type: dict | bytes
    :param color: Filter based on predominant color in an image. Use 6 character hexadecimal format (e.g., #002244).
    :type color: str
    :param compositions: Filter based on image composition.
    :type compositions: list | bytes
    :param download_product: Filters based on which product the asset will download against.                      Allowed values are easyaccess, editorialsubscription, imagepack, premiumaccess and royaltyfreesubscription.                      If you have more than one instance of a product, you may also include the ID of the product instance you wish to filter on.                       For example, some users may have more than one premiumaccess product, so the download_product value would be premiumaccess:1234.                       Product ID can be obtained from the GET /products response.
    :type download_product: str
    :param embed_content_only: Restrict search results to embeddable images. The default is false.
    :type embed_content_only: bool
    :param ethnicity: Filter search results based on the ethnicity of individuals in an image.
    :type ethnicity: list | bytes
    :param exclude_keyword_ids: Return only images not tagged with specific keyword(s). Specify using a comma-separated list of keyword Ids. If keyword Ids and phrase are both specified, only those images matching the query phrase which also do not contain the requested keyword(s) are returned.
    :type exclude_keyword_ids: List[int]
    :param exclude_nudity: Excludes images containing nudity. The default is false.
    :type exclude_nudity: bool
    :param exclude_editorial_use_only: Exclude images that are only available for editorial (non-commercial) use. Default value is false.
    :type exclude_editorial_use_only: bool
    :param fields: Specifies fields to return. Defaults to &#39;summary_set&#39;. NOTE: Bytes, height, and width returned by &#39;download_sizes&#39; field are estimates.
    :type fields: list | bytes
    :param file_types: Return only images having a specific file type.
    :type file_types: list | bytes
    :param graphical_styles: Filter based on graphical style of the image.
    :type graphical_styles: list | bytes
    :param graphical_styles_filter_type: Provides searching based on specified graphical style(s). The default is include.
    :type graphical_styles_filter_type: dict | bytes
    :param include_related_searches: Specifies whether or not to include related searches in the response. The default is false.
    :type include_related_searches: bool
    :param keyword_ids: Return only images tagged with specific keyword(s). Specify using a comma-separated list of keyword Ids. If keyword Ids and phrase are both specified, only those images matching the query phrase which also contain the requested keyword(s) are returned.
    :type keyword_ids: List[int]
    :param minimum_size: Filter based on minimum size requested. The default is x-small.
    :type minimum_size: dict | bytes
    :param number_of_people: Filter based on the number of people in the image.
    :type number_of_people: list | bytes
    :param orientations: Return only images with selected aspect ratios.
    :type orientations: list | bytes
    :param page: Request results starting at a page number (default is 1).
    :type page: int
    :param page_size: Request number of images to return in each page. Default is 30, maximum page_size is 100.
    :type page_size: int
    :param phrase: Search images using a search phrase.
    :type phrase: str
    :param safe_search: Setting safe_search to \&quot;true\&quot; excludes images containing nudity, death, profanity, drugs and alcohol, suggestive content, and graphic content from the result set. The default is false. Because this is a keyword-based filter, it&#39;s possible that a small number of unsafe images may not be caught by the filter. Please direct feedback to your Getty Images Account or API support representative.
    :type safe_search: bool
    :param sort_order: Select sort order of results.  The default is best_match
    :type sort_order: dict | bytes
    :param facet_fields: Specifies the facets to return in the response. Facets provide additional search parameters to refine your results.                     The include_facets parameter must be set to \&quot;true\&quot; for facets to be returned.
    :type facet_fields: list | bytes
    :param include_facets: Specifies whether or not to include facets in the result set. Default is \&quot;false\&quot;.
    :type include_facets: bool
    :param facet_max_count: Specifies the maximum number of facets to return per type. Default is 300.
    :type facet_max_count: int

    """
    age_of_people = [AgeOfPeopleFilterType.from_dict(d) for d in age_of_people]
    collections_filter_type = .from_dict(collections_filter_type)
    compositions = [CompositionsFilterType.from_dict(d) for d in compositions]
    ethnicity = [EthnicityFilterType.from_dict(d) for d in ethnicity]
    fields = [CreativeImagesFieldValues.from_dict(d) for d in fields]
    file_types = [SearchFileType.from_dict(d) for d in file_types]
    graphical_styles = [GraphicalStyle.from_dict(d) for d in graphical_styles]
    graphical_styles_filter_type = .from_dict(graphical_styles_filter_type)
    minimum_size = .from_dict(minimum_size)
    number_of_people = [NumberOfPeopleFilterType.from_dict(d) for d in number_of_people]
    orientations = [ImageOrientationRequest.from_dict(d) for d in orientations]
    sort_order = .from_dict(sort_order)
    facet_fields = [CreateImageSearchFacetsFields.from_dict(d) for d in facet_fields]
    return web.Response(status=200)


async def v3_search_images_editorial_get(request: web.Request, accept_language=None, gi_country_code=None, age_of_people=None, artists=None, collection_codes=None, collections_filter_type=None, compositions=None, date_from=None, date_to=None, download_product=None, editorial_segments=None, embed_content_only=None, ethnicity=None, event_ids=None, exclude_keyword_ids=None, fields=None, file_types=None, graphical_styles=None, graphical_styles_filter_type=None, include_related_searches=None, keyword_ids=None, minimum_size=None, number_of_people=None, orientations=None, page=None, page_size=None, phrase=None, sort_order=None, specific_people=None, minimum_quality_rank=None, facet_fields=None, include_facets=None, facet_max_count=None) -> web.Response:
    """Search for editorial images only

    Use this endpoint to search our editorial stock photos, illustrations and archival images.  Editorial images represent newsworthy events or illustrate matters of general interest, such as news, sport and entertainment and are generally intended for editorial use.  You&#39;ll need an API key and access token to use this resource.  You can show different information in the response by specifying values on the \&quot;fields\&quot; parameter (see details below). You can search with only an API key, and that will give you search results that are equivalent to doing a search on the GettyImages.com site without being logged in (anonymous search).  If you are a Getty Images API customer and would like to ensure that your API searches return only assets that you have a license to use, you need to also include an authorization token in the header of your request.  Please consult our [Authorization FAQ](http://developers.gettyimages.com/en/authorization-faq.html) for more information on authorization tokens, and our [Authorization Workflows](https://github.com/gettyimages/gettyimages-api/blob/master/OAuth2Workflow.md) for code examples of getting a token. To include your API token in the search request, add it to the headers as a Bearer token (example in curl):   -H \&quot;Authorization: Bearer &lt;your-token&gt;\&quot;  Search requests without a phrase parameter are not supported and may not always work.  ## Working with Fields Sets  Fields sets are used in the **fields** request parameter to receive a suite of metadata fields. The following fields sets are available:  #### Summary Fields Set  The **summary_set** query string parameter fields value represents a small batch of metadata fields that are often used to build search response results. The following fields are provided for every image in your result set when you include **summary_set** in your request.  &#x60;&#x60;&#x60; {     \&quot;images\&quot;:      [         \&quot;asset_family\&quot;,         \&quot;caption\&quot;,         \&quot;collection_code\&quot;,         \&quot;collection_id\&quot;,         \&quot;collection_name\&quot;,         \&quot;display_sizes\&quot;:          [             {                 \&quot;name\&quot;: \&quot;thumb\&quot;             }         ],         \&quot;license_model\&quot;,         \&quot;max_dimensions\&quot;,         \&quot;title\&quot;     ] } &#x60;&#x60;&#x60;  #### Detail Fields Set  The **detail_set** query string parameter fields value represents a large batch of metadata fields that are often used to build a detailed view of images. The following fields are provided for every image in your result set when you include **detail_set** in your request.  &#x60;&#x60;&#x60; {     \&quot;images\&quot;:      [         \&quot;allowed_use\&quot;,         \&quot;artist\&quot;,         \&quot;asset_family\&quot;,         \&quot;call_for_image\&quot;,         \&quot;caption\&quot;,         \&quot;collection_code\&quot;,         \&quot;collection_id\&quot;,         \&quot;collection_name\&quot;,         \&quot;copyright\&quot;,         \&quot;date_created\&quot;,         \&quot;display_sizes\&quot;:          [             {                 \&quot;name\&quot;: \&quot;comp\&quot;             },             {                 \&quot;name\&quot;: \&quot;preview\&quot;             },             {                 \&quot;name\&quot;: \&quot;thumb\&quot;             }         ],         \&quot;editorial_segments\&quot;,         \&quot;event_ids\&quot;,         \&quot;graphical_style\&quot;,         \&quot;license_model\&quot;,         \&quot;max_dimensions\&quot;,         \&quot;orientation\&quot;,         \&quot;product_types\&quot;,         \&quot;quality_rank\&quot;,         \&quot;referral_destinations\&quot;,         \&quot;title\&quot;     ] ] &#x60;&#x60;&#x60;  #### Display Fields Set  The **display_set** query string parameter fields value represents the fields that provide you with URLs for the low resolution files that are most frequently used to build a UI displaying search results. The following fields are provided for every image in your result set when you include **display_set** in your request.  The URI provided is subject to change at any time and must be used as-is with no modification.  &#x60;&#x60;&#x60; {     \&quot;images\&quot;:     [         \&quot;display_sizes\&quot;:          [             {                 \&quot;is_watermarked\&quot;: &lt;boolean&gt;,                 \&quot;name\&quot;: \&quot;comp\&quot;,                 \&quot;uri\&quot;: \&quot;&lt;link&gt;\&quot;             },             {                 \&quot;is_watermarked\&quot;: &lt;boolean&gt;,                 \&quot;name\&quot;: \&quot;preview\&quot;,                 \&quot;uri\&quot;: \&quot;&lt;link&gt;\&quot;             },             {                 \&quot;is_watermarked\&quot;: &lt;boolean&gt;,                 \&quot;name\&quot;: \&quot;thumb\&quot;,                 \&quot;uri\&quot;: \&quot;&lt;link&gt;\&quot;             }         ]     ] } &#x60;&#x60;&#x60;

    :param accept_language: Provide a header to specify the language of result values. Supported values: cs (iStock only), de, en-GB, en-US, es, fi (iStock only), fr, hu (iStock only), id (iStock only), it, ja, ko (creative assets only), nl, pl (creative assets only), pt-BR, pt-PT, ro (iStock only), ru (creative assets only), sv, th (iStock only), tr, uk (iStock only), vi (iStock only), zh-HK (creative assets only).
    :type accept_language: str
    :param gi_country_code: Receive regionally relevant search results based on the value specified. Accepts only ISO Alpha-3 country codes. The Countries operation can be used to retrieve the codes.
    :type gi_country_code: str
    :param age_of_people: Filter based on the age of individuals in an image.
    :type age_of_people: list | bytes
    :param artists: Search for images by specific artists (free-text, comma-separated list of artists).
    :type artists: str
    :param collection_codes: Filter by collections (comma-separated list of collection codes). Include or exclude based on collections_filter_type.
    :type collection_codes: List[str]
    :param collections_filter_type: Use to include or exclude collections from search. The default is include
    :type collections_filter_type: dict | bytes
    :param compositions: Filter based on image composition.
    :type compositions: list | bytes
    :param date_from: Return only images that are created on or after this date. Use ISO 8601 format (e.g., 1999-12-31).
    :type date_from: str
    :param date_to: Return only images that are created on or before this date. Use ISO 8601 format (e.g., 1999-12-31).
    :type date_to: str
    :param download_product: Filters based on which product the asset will download against.                      Allowed values are easyaccess, editorialsubscription, imagepack, premiumaccess and royaltyfreesubscription.                      If you have more than one instance of a product, you may also include the ID of the product instance you wish to filter on.                       For example, some users may have more than one premiumaccess product, so the download_product value would be premiumaccess:1234.                       Product ID can be obtained from the GET /products response.
    :type download_product: str
    :param editorial_segments: Return only events with a matching editorial segment.
    :type editorial_segments: list | bytes
    :param embed_content_only: Restrict search results to embeddable images. The default is false.
    :type embed_content_only: bool
    :param ethnicity: Filter search results based on the ethnicity of individuals in an image.
    :type ethnicity: list | bytes
    :param event_ids: Filter based on specific events
    :type event_ids: List[int]
    :param exclude_keyword_ids: Return only images not tagged with specific keyword(s). Specify using a comma-separated list of keyword Ids. If keyword Ids and phrase are both specified, only those images matching the query phrase which also do not contain the requested keyword(s) are returned.
    :type exclude_keyword_ids: List[int]
    :param fields: Specifies fields to return. Defaults to &#39;summary_set&#39;. NOTE: Bytes, height, and width returned by &#39;download_sizes&#39; field are estimates.
    :type fields: list | bytes
    :param file_types: Return only images having a specific file type.
    :type file_types: list | bytes
    :param graphical_styles: Filter based on graphical style of the image.
    :type graphical_styles: list | bytes
    :param graphical_styles_filter_type: Provides searching based on specified graphical style(s). The default is include.
    :type graphical_styles_filter_type: dict | bytes
    :param include_related_searches: Specifies whether or not to include related searches in the response. The default is false.
    :type include_related_searches: bool
    :param keyword_ids: Return only images tagged with specific keyword(s). Specify using a comma-separated list of keyword Ids. If keyword Ids and phrase are both specified, only those images matching the query phrase which also contain the requested keyword(s) are returned.
    :type keyword_ids: List[int]
    :param minimum_size: Filter based on minimum size requested. The default is x-small.
    :type minimum_size: dict | bytes
    :param number_of_people: Filter based on the number of people in the image.
    :type number_of_people: list | bytes
    :param orientations: Return only images with selected aspect ratios.
    :type orientations: list | bytes
    :param page: Request results starting at a page number (default is 1).
    :type page: int
    :param page_size: Request number of images to return in each page. Default is 30, maximum page_size is 100.
    :type page_size: int
    :param phrase: Search images using a search phrase.
    :type phrase: str
    :param sort_order: Select sort order of results.  The default is best_match
    :type sort_order: dict | bytes
    :param specific_people: Return only images associated with specific people (using a comma-delimited list).
    :type specific_people: List[str]
    :param minimum_quality_rank: Filter search results based on minimum quality ranking. Possible values 1, 2, 3 with 1 being best.
    :type minimum_quality_rank: int
    :param facet_fields: Specifies the facets to return in the response. Facets provide additional search parameters to refine your results.                     The include_facets parameter must be set to \&quot;true\&quot; for facets to be returned.
    :type facet_fields: list | bytes
    :param include_facets: Specifies whether or not to include facets in the result set. Default is \&quot;false\&quot;.
    :type include_facets: bool
    :param facet_max_count: Specifies the maximum number of facets to return per type. Default is 300.
    :type facet_max_count: int

    """
    age_of_people = [AgeOfPeopleFilterType.from_dict(d) for d in age_of_people]
    collections_filter_type = .from_dict(collections_filter_type)
    compositions = [CompositionsFilterType.from_dict(d) for d in compositions]
    date_from = util.deserialize_datetime(date_from)
    date_to = util.deserialize_datetime(date_to)
    editorial_segments = [EditorialSegmentContract.from_dict(d) for d in editorial_segments]
    ethnicity = [EthnicityFilterType.from_dict(d) for d in ethnicity]
    fields = [EditorialImagesFieldValues.from_dict(d) for d in fields]
    file_types = [SearchFileType.from_dict(d) for d in file_types]
    graphical_styles = [EditorialGraphicalStyle.from_dict(d) for d in graphical_styles]
    graphical_styles_filter_type = .from_dict(graphical_styles_filter_type)
    minimum_size = .from_dict(minimum_size)
    number_of_people = [NumberOfPeopleFilterType.from_dict(d) for d in number_of_people]
    orientations = [ImageOrientationRequest.from_dict(d) for d in orientations]
    sort_order = .from_dict(sort_order)
    facet_fields = [EditorialImageSearchFacetsFields.from_dict(d) for d in facet_fields]
    return web.Response(status=200)


async def v3_search_images_get(request: web.Request, accept_language=None, gi_country_code=None, age_of_people=None, artists=None, collection_codes=None, collections_filter_type=None, color=None, compositions=None, download_product=None, embed_content_only=None, event_ids=None, ethnicity=None, exclude_nudity=None, fields=None, file_types=None, graphical_styles=None, graphical_styles_filter_type=None, include_related_searches=None, keyword_ids=None, minimum_size=None, number_of_people=None, orientations=None, page=None, page_size=None, phrase=None, sort_order=None, specific_people=None) -> web.Response:
    """Search for both creative and editorial images - *** DEPRECATED ***

    ## _This endpoint draws from such a large diversity of content, the results will not be as relevant as when the more specific Creative or Editorial endpoints are used. Additionally, the response time for this endpoint is slower compared to that for Creative and Editorial-specific endpoints. For these reasons,_ _**it is highly recommended that those endpoints are used instead of this blended endpoint.**_    You&#39;ll need an API key and access token to use this resource.  You can show different information in the response by specifying values on the \&quot;fields\&quot; parameter (see details below). You can search with only an API key, and that will give you search results that are equivalent to doing a search on the GettyImages.com site without being logged in (anonymous search).  If you are a Getty Images API customer and would like to ensure that your API searches return only assets that you have a license to use, you need to also include an authorization token in the header of your request.  Please consult our [Authorization FAQ](http://developers.gettyimages.com/en/authorization-faq.html) for more information on authorization tokens, and our [Authorization Workflows](https://github.com/gettyimages/gettyimages-api/blob/master/OAuth2Workflow.md) for code examples of getting a token.&lt;br&gt; To include your API token in the search request, add it to the headers as a Bearer token (example in curl):   -H \&quot;Authorization: Bearer &lt;your-token&gt;\&quot;  Search requests without a phrase parameter are not supported and may not always work.  ## Working with Fields Sets  Fields sets are used in the **fields** request parameter to receive a suite of metadata fields. The following fields sets are available:  #### Summary Fields Set  The **summary_set** query string parameter fields value represents a small batch of metadata fields that are often used to build search response results. The following fields are provided for every image in your result set when you include **summary_set** in your request.  &#x60;&#x60;&#x60; {     \&quot;images\&quot;:      [         \&quot;asset_family\&quot;,         \&quot;caption\&quot;,         \&quot;collection_code\&quot;,         \&quot;collection_id\&quot;,         \&quot;collection_name\&quot;,         \&quot;display_sizes\&quot;:          [             {                 \&quot;name\&quot;: \&quot;thumb\&quot;             }         ],         \&quot;license_model\&quot;,         \&quot;max_dimensions\&quot;,         \&quot;title\&quot;     ] } &#x60;&#x60;&#x60;  #### Detail Fields Set  The **detail_set** query string parameter fields value represents a large batch of metadata fields that are often used to build a detailed view of images.  The following fields are provided for every image in your result set when you include **detail_set** in your request.  &#x60;&#x60;&#x60; {     \&quot;images\&quot;:      [         \&quot;allowed_use\&quot;,         \&quot;artist\&quot;,         \&quot;asset_family\&quot;,         \&quot;call_for_image\&quot;,         \&quot;caption\&quot;,         \&quot;collection_code\&quot;,         \&quot;collection_id\&quot;,         \&quot;collection_name\&quot;,         \&quot;copyright\&quot;,         \&quot;date_created\&quot;,         \&quot;display_sizes\&quot;:          [             {                 \&quot;name\&quot;: \&quot;comp\&quot;             },             {                 \&quot;name\&quot;: \&quot;preview\&quot;             },             {                 \&quot;name\&quot;: \&quot;thumb\&quot;             }         ],         \&quot;editorial_segments\&quot;,         \&quot;event_ids\&quot;,         \&quot;graphical_style\&quot;,         \&quot;license_model\&quot;,         \&quot;max_dimensions\&quot;,         \&quot;orientation\&quot;,         \&quot;product_types\&quot;,         \&quot;quality_rank\&quot;,         \&quot;referral_destinations\&quot;,         \&quot;title\&quot;     ] ] &#x60;&#x60;&#x60;  #### Display Fields Set  The **display_set** query string parameter fields value represents the fields that provide you with URLs for the low resolution files that are most  frequently used to build a UI displaying search results. The following fields are provided for every image in your result set when you include **display_set** in your request.  The URI provided is subject to change at any time and must be used as-is with no modification.  &#x60;&#x60;&#x60; {     \&quot;images\&quot;:     [         \&quot;display_sizes\&quot;:          [             {                 \&quot;is_watermarked\&quot;: &lt;boolean&gt;,                 \&quot;name\&quot;: \&quot;comp\&quot;,                 \&quot;uri\&quot;: \&quot;&lt;link&gt;\&quot;             },             {                 \&quot;is_watermarked\&quot;: &lt;boolean&gt;,                 \&quot;name\&quot;: \&quot;preview\&quot;,                 \&quot;uri\&quot;: \&quot;&lt;link&gt;\&quot;             },             {                 \&quot;is_watermarked\&quot;: &lt;boolean&gt;,                 \&quot;name\&quot;: \&quot;thumb\&quot;,                 \&quot;uri\&quot;: \&quot;&lt;link&gt;\&quot;             }         ]     ] } &#x60;&#x60;&#x60;  ## Request Usage Considerations  - Specifying the \&quot;entity_details\&quot; response field can have significant performance implications. The field should be used only when necessary. 

    :param accept_language: Provide a header to specify the language of result values. Supported values: cs (iStock only), de, en-GB, en-US, es, fi (iStock only), fr, hu (iStock only), id (iStock only), it, ja, ko (creative assets only), nl, pl (creative assets only), pt-BR, pt-PT, ro (iStock only), ru (creative assets only), sv, th (iStock only), tr, uk (iStock only), vi (iStock only), zh-HK (creative assets only).
    :type accept_language: str
    :param gi_country_code: Receive regionally relevant search results based on the value specified. Accepts only ISO Alpha-3 country codes. The Countries operation can be used to retrieve the codes.
    :type gi_country_code: str
    :param age_of_people: Filter based on the age of individuals in an image.
    :type age_of_people: list | bytes
    :param artists: Search for images by specific artists (free-text, comma-separated list of artists).
    :type artists: str
    :param collection_codes: Filter by collection codes (comma-separated list). Include or exclude based on collections_filter_type.
    :type collection_codes: List[str]
    :param collections_filter_type: Provides searching based on specified collection(s). The default is Include
    :type collections_filter_type: dict | bytes
    :param color: Filter based on predominant color in an image. Use 6 character hexidecimal format (e.g., #002244). Note: when specified, results will not contain editorial images.
    :type color: str
    :param compositions: Filter based on image composition.
    :type compositions: list | bytes
    :param download_product: Filters based on which product the asset will download against.                      Allowed values are easyaccess, editorialsubscription, imagepack, premiumaccess and royaltyfreesubscription.                      If you have more than one instance of a product, you may also include the ID of the product instance you wish to filter on.                       For example, some users may have more than one premiumaccess product, so the download_product value would be premiumaccess:1234.                       Product ID can be obtained from the GET /products response.
    :type download_product: str
    :param embed_content_only: Restrict search results to embeddable images. The default is false.
    :type embed_content_only: bool
    :param event_ids: Filter based on specific events
    :type event_ids: List[int]
    :param ethnicity: Filter search results based on the ethnicity of individuals in an image.
    :type ethnicity: list | bytes
    :param exclude_nudity: Excludes images containing nudity. The default is false.
    :type exclude_nudity: bool
    :param fields: Specifies fields to return. Defaults to &#39;summary_set&#39;.
    :type fields: list | bytes
    :param file_types: Return only images having a specific file type.
    :type file_types: list | bytes
    :param graphical_styles: Filter based on graphical style of the image.
    :type graphical_styles: list | bytes
    :param graphical_styles_filter_type: Provides searching based on specified graphical style(s). The default is Include
    :type graphical_styles_filter_type: dict | bytes
    :param include_related_searches: Specifies whether or not to include related searches in the response. The default is false.
    :type include_related_searches: bool
    :param keyword_ids: Return only images tagged with specific keyword(s). Specify using a comma-separated list of keyword Ids. If keyword Ids and phrase are both specified, only those images matching the query phrase which also contain the requested keyword(s) are returned.
    :type keyword_ids: List[int]
    :param minimum_size: Filter based on minimum size requested. The default is x-small
    :type minimum_size: dict | bytes
    :param number_of_people: Filter based on the number of people in the image.
    :type number_of_people: list | bytes
    :param orientations: Return only images with selected aspect ratios.
    :type orientations: list | bytes
    :param page: Request results starting at a page number (default is 1).
    :type page: int
    :param page_size: Request number of images to return in each page. Default is 30, maximum page_size is 100.
    :type page_size: int
    :param phrase: Search images using a search phrase.
    :type phrase: str
    :param sort_order: Select sort order of results.  The default is best_match
    :type sort_order: dict | bytes
    :param specific_people: Return only images associated with specific people (using a comma-delimited list).
    :type specific_people: List[str]

    """
    age_of_people = [AgeOfPeopleFilterType.from_dict(d) for d in age_of_people]
    collections_filter_type = .from_dict(collections_filter_type)
    compositions = [CompositionsFilterType.from_dict(d) for d in compositions]
    ethnicity = [EthnicityFilterType.from_dict(d) for d in ethnicity]
    fields = [ImagesFieldValues.from_dict(d) for d in fields]
    file_types = [SearchFileType.from_dict(d) for d in file_types]
    graphical_styles = [GraphicalStyle.from_dict(d) for d in graphical_styles]
    graphical_styles_filter_type = .from_dict(graphical_styles_filter_type)
    minimum_size = .from_dict(minimum_size)
    number_of_people = [NumberOfPeopleFilterType.from_dict(d) for d in number_of_people]
    orientations = [ImageOrientationRequest.from_dict(d) for d in orientations]
    sort_order = .from_dict(sort_order)
    return web.Response(status=200)


async def v3_search_videos_creative_by_image_get(request: web.Request, accept_language=None, gi_country_code=None, asset_id=None, exclude_editorial_use_only=None, facet_fields=None, facet_max_count=None, fields=None, image_url=None, include_facets=None, page=None, page_size=None, product_types=None) -> web.Response:
    """Search for creative videos based on url

    Search for **similar creative videos** by passing an &#x60;image_url&#x60; to an uploaded image/frame grab from a video OR an &#x60;asset_id&#x60; of an asset in our catalog.  All responses will have the &#x60;exclude_nudity&#x60; filter automatically applied.  ## Searching by URL  Before calling the search by image endpoint, an image or frame grab in JPEG format must be uploaded to &#x60;https://api.gettyimages.com/v3/search/by-image/uploads/{CLIENT_IMAGE.jpg}&#x60;, where the client defines the &#x60;{CLIENT_IMAGE.jpg}&#x60; portion of the URL.  For example, using cURL:  &#x60;&#x60;&#x60; sh curl -i -X PUT https://api.gettyimages.com/v3/search/by-image/uploads/my-test-image.jpg -H &#39;Content-Type: image/jpeg&#39; -H &#39;Api-Key: API_KEY&#39; --data-binary \&quot;@testimage.jpg\&quot; &#x60;&#x60;&#x60;  Once the image has been uploaded, use the full URL in the &#x60;image_url&#x60; parameter, e.g. &#x60;image_url&#x3D;https://api.gettyimages.com/v3/search/by-image/uploads/my-test-image.jpg&#x60;.  - Uploaded files must be 10MB or smaller - Uploads to the same URL will overwrite each other, so ensure that the client application is handling naming uniqueness appropriately. - Uploads expire after 24 hours. - Uploads and searches must be performed using the _same_ API Key.  ## Searching by asset id  When searching by &#x60;asset_id&#x60;, any image or video asset id in the Getty/iStock catalog can be used as the source for similar videos. 

    :param accept_language: Provide a header to specify the language of result values. Supported values: cs (iStock only), de, en-GB, en-US, es, fi (iStock only), fr, hu (iStock only), id (iStock only), it, ja, ko (creative assets only), nl, pl (creative assets only), pt-BR, pt-PT, ro (iStock only), ru (creative assets only), sv, th (iStock only), tr, uk (iStock only), vi (iStock only), zh-HK (creative assets only).
    :type accept_language: str
    :param gi_country_code: Receive regionally relevant search results based on the value specified. Accepts only ISO Alpha-3 country codes. The Countries operation can be used to retrieve the codes.
    :type gi_country_code: str
    :param asset_id: Specifies the Getty video id to use in the search.
    :type asset_id: str
    :param exclude_editorial_use_only: Exclude videos that are only available for editorial (non-commercial) use. Default value is false.
    :type exclude_editorial_use_only: bool
    :param facet_fields: Specifies the facets to return in the response. Facets provide additional search parameters to refine your results.                      The include_facets parameter must be set to \&quot;true\&quot; for facets to be returned.
    :type facet_fields: list | bytes
    :param facet_max_count: Specifies the maximum number of facets to return per type. Default is 300.
    :type facet_max_count: int
    :param fields: Specifies fields to return. Defaults to &#39;summary_set&#39;. NOTE: Bytes returned by &#39;download_sizes&#39; field is an estimate.
    :type fields: list | bytes
    :param image_url: Specifies the location of the image to use in the search.
    :type image_url: str
    :param include_facets: Specifies whether or not to include facets in the result set. Default is \&quot;false\&quot;.
    :type include_facets: bool
    :param page: Request results starting at a page number (default is 1).
    :type page: int
    :param page_size: Request number of images to return in each page. Default is 30, maximum page_size is 100.
    :type page_size: int
    :param product_types: Filter images to those from one of your product types.                       Allowed values are easyaccess, imagepack, premiumaccess and royaltyfreesubscription.                       If you have more than one instance of a product, you may also include the ID of the product instance you wish to filter on.                       For example, some users may have more than one premiumaccess product, so the product_types value would be premiumaccess:1234.                       Product ID can be obtained from the GET /products response.
    :type product_types: List[str]

    """
    facet_fields = [CreateVideoSearchFacetsFields.from_dict(d) for d in facet_fields]
    fields = [CreativeVideosFieldValues.from_dict(d) for d in fields]
    return web.Response(status=200)


async def v3_search_videos_creative_get(request: web.Request, accept_language=None, gi_country_code=None, age_of_people=None, artists=None, aspect_ratios=None, collection_codes=None, collections_filter_type=None, compositions=None, download_product=None, exclude_nudity=None, exclude_editorial_use_only=None, exclude_keyword_ids=None, fields=None, format_available=None, frame_rates=None, image_techniques=None, include_related_searches=None, keyword_ids=None, license_models=None, orientations=None, min_clip_length=None, max_clip_length=None, page=None, page_size=None, phrase=None, safe_search=None, sort_order=None, release_status=None, facet_fields=None, facet_max_count=None, include_facets=None, viewpoints=None) -> web.Response:
    """Search for creative videos

    Use this endpoint to search premium stock video, from archival film to contemporary 4K and HD footage.  You&#39;ll need an API key and access token to use this resource.  You can show different information in the response by specifying values on the \&quot;fields\&quot; parameter (see details below). You can search with only an API key, and that will give you search results that are equivalent to doing a search on the GettyImages.com site without being logged in (anonymous search).  If you are a Getty Images API customer and would like to ensure that your API searches return only  assets that you have a license to use, you need to also include an authorization token in the header of your request. Please consult our [Authorization FAQ](http://developers.gettyimages.com/en/authorization-faq.html) for more information on authorization tokens.  Search requests without a phrase parameter are not supported and may not always work.  ## Working with Fields Sets  Fields sets are used in the **fields** request parameter to receive a suite of metadata fields. The following fields sets are available:  #### Summary Fields Set  The **summary_set** query string parameter fields value represents a small batch of metadata fields that are often used to build search response results. The following fields are provided for every video in your result set when you include **summary_set** in your request.  &#x60;&#x60;&#x60; {     \&quot;videos\&quot;:      [         \&quot;asset_family\&quot;,          \&quot;caption\&quot;,         \&quot;collection_code\&quot;,         \&quot;collection_name\&quot;,         \&quot;display_sizes\&quot;:         [             {                 \&quot;name\&quot;: \&quot;comp\&quot;             },             {                 \&quot;name\&quot;: \&quot;preview\&quot;             },             {                 \&quot;name\&quot;: \&quot;thumb\&quot;             }         ],         \&quot;license_model\&quot;,         \&quot;title\&quot;     ] } &#x60;&#x60;&#x60;  #### Detail Fields Set  The **detail_set** query string parameter fields value represents a large batch of metadata fields that are often used to build a  detailed view of videos. The following fields are provided for every video in your result set when you include **detail_set** in your request.  &#x60;&#x60;&#x60; {     \&quot;videos\&quot;:      [         \&quot;allowed_use\&quot;,         \&quot;artist\&quot;,         \&quot;asset_family\&quot;,    \&quot;call_for_image\&quot;,         \&quot;caption\&quot;,          \&quot;clip_length\&quot;,         \&quot;collection_code\&quot;,         \&quot;collection_id\&quot;,         \&quot;collection_name\&quot;,          \&quot;color_type\&quot;,         \&quot;copyright\&quot;,         \&quot;date_created\&quot;,         \&quot;display_sizes\&quot;:         [             {                 \&quot;name\&quot;: \&quot;comp\&quot;             },             {                 \&quot;name\&quot;: \&quot;preview\&quot;             },             {                 \&quot;name\&quot;: \&quot;thumb\&quot;             }         ],         \&quot;era\&quot;,         \&quot;license_model\&quot;,         \&quot;mastered_to\&quot;,         \&quot;originally_shot_on\&quot;,         \&quot;product_types\&quot;,         \&quot;quality_rank\&quot;,         \&quot;shot_speed\&quot;,         \&quot;source\&quot;,         \&quot;title\&quot;     ] } &#x60;&#x60;&#x60;  #### Display Fields Set  The **display_set** query string parameter fields value represents the fields that provide you with URLs for the low resolution files  that are most frequently used to build a UI displaying search results. The following fields are provided for every video in your result  set when you include **display_set** in your request.  The URI provided is subject to change at any time and must be used as-is with no modification.  &#x60;&#x60;&#x60; {     \&quot;videos\&quot;:     [         \&quot;display_sizes\&quot;:          [             {                 \&quot;is_watermarked\&quot;: &lt;boolean&gt;,                 \&quot;name\&quot;: \&quot;comp\&quot;,                 \&quot;uri\&quot;: \&quot;&lt;link&gt;\&quot;             },             {                 \&quot;is_watermarked\&quot;: &lt;boolean&gt;,                 \&quot;name\&quot;: \&quot;preview\&quot;,                 \&quot;uri\&quot;: \&quot;&lt;link&gt;\&quot;             },             {                 \&quot;is_watermarked\&quot;: &lt;boolean&gt;,                 \&quot;name\&quot;: \&quot;thumb\&quot;,                 \&quot;uri\&quot;: \&quot;&lt;link&gt;\&quot;             }         ]     ] } &#x60;&#x60;&#x60;

    :param accept_language: Provide a header to specify the language of result values. Supported values: cs (iStock only), de, en-GB, en-US, es, fi (iStock only), fr, hu (iStock only), id (iStock only), it, ja, ko (creative assets only), nl, pl (creative assets only), pt-BR, pt-PT, ro (iStock only), ru (creative assets only), sv, th (iStock only), tr, uk (iStock only), vi (iStock only), zh-HK (creative assets only).
    :type accept_language: str
    :param gi_country_code: Receive regionally relevant search results based on the value specified. Accepts only ISO Alpha-3 country codes. The Countries operation can be used to retrieve the codes.
    :type gi_country_code: str
    :param age_of_people: Provides filtering according to the age of individuals in a video.
    :type age_of_people: list | bytes
    :param artists: Search for videos by specific artists (free-text, comma-separated list of artists).
    :type artists: str
    :param aspect_ratios: Search for videos by specific aspect ratios.
    :type aspect_ratios: list | bytes
    :param collection_codes: Provides filtering by collection code.
    :type collection_codes: List[str]
    :param collections_filter_type: Use to include or exclude collections from search. The default is include
    :type collections_filter_type: dict | bytes
    :param compositions: Filter based on video composition.
    :type compositions: list | bytes
    :param download_product: Filters based on which product the asset will download against.                      Allowed values are easyaccess, editorialsubscription, imagepack, premiumaccess and royaltyfreesubscription.                      If you have more than one instance of a product, you may also include the ID of the product instance you wish to filter on.                       For example, some users may have more than one premiumaccess product, so the download_product value would be premiumaccess:1234.                       Product ID can be obtained from the GET /products response.
    :type download_product: str
    :param exclude_nudity: Excludes videos containing nudity. The default is false.
    :type exclude_nudity: bool
    :param exclude_editorial_use_only: Exclude videos that are only available for editorial (non-commercial) use. Default value is false.
    :type exclude_editorial_use_only: bool
    :param exclude_keyword_ids: Return only videos not tagged with specific keyword(s). Specify using a comma-separated list of keyword Ids. If keyword Ids and phrase are both specified, only those videos matching the query phrase which also do not contain the requested keyword(s) are returned.
    :type exclude_keyword_ids: List[int]
    :param fields: Specifies fields to return. Defaults to &#39;summary_set&#39;. NOTE: Bytes returned by &#39;download_sizes&#39; field is an estimate.
    :type fields: list | bytes
    :param format_available: Filters according to the digital video format available on a film asset.
    :type format_available: dict | bytes
    :param frame_rates: Provides filtering by video frame rate (frames/second).
    :type frame_rates: list | bytes
    :param image_techniques: Filter based on image technique.
    :type image_techniques: list | bytes
    :param include_related_searches: Specifies whether or not to include related searches in the response. The default is false.
    :type include_related_searches: bool
    :param keyword_ids: Return only videos tagged with specific keyword(s). Specify using a comma-separated list of keyword Ids. If keyword Ids and phrase are both specified, only those videos matching the query phrase which also contain the requested keyword(s) are returned.
    :type keyword_ids: List[int]
    :param license_models: Specifies the video licensing model(s).
    :type license_models: list | bytes
    :param orientations: Return only videos with selected orientations.
    :type orientations: list | bytes
    :param min_clip_length: Provides filtering by minimum length of video clip, in seconds
    :type min_clip_length: int
    :param max_clip_length: Provides filtering by maximum length of video, in seconds
    :type max_clip_length: int
    :param page: Identifies page to return. Default is 1.
    :type page: int
    :param page_size: Specifies page size. Default is 30, maximum page_size is 100.
    :type page_size: int
    :param phrase: Free-text search query.
    :type phrase: str
    :param safe_search: Setting safe_search to \&quot;true\&quot; excludes images containing nudity, death, profanity, drugs and alcohol, suggestive content, and graphic content from the result set. The default is false. Because this is a keyword-based filter, it&#39;s possible that a small number of unsafe images may not be caught by the filter. Please direct feedback to your Getty Images Account or API support representative.
    :type safe_search: bool
    :param sort_order: Select sort order of results.  The default is best_match
    :type sort_order: dict | bytes
    :param release_status: Allows filtering by type of model release.
    :type release_status: dict | bytes
    :param facet_fields: Specifies the facets to return in the response. Facets provide additional search parameters to refine your results.                     The include_facets parameter must be set to \&quot;true\&quot; for facets to be returned.
    :type facet_fields: list | bytes
    :param facet_max_count: Specifies the maximum number of facets to return per type. Default is 300.
    :type facet_max_count: int
    :param include_facets: Specifies whether or not to include facets in the result set. Default is \&quot;false\&quot;.
    :type include_facets: bool
    :param viewpoints: Filter based on viewpoint.
    :type viewpoints: list | bytes

    """
    age_of_people = [AgeOfPeopleFilterType.from_dict(d) for d in age_of_people]
    aspect_ratios = [VideoAspectRatioFilterType.from_dict(d) for d in aspect_ratios]
    collections_filter_type = .from_dict(collections_filter_type)
    compositions = [CompositionsFilterType.from_dict(d) for d in compositions]
    fields = [CreativeVideosFieldValues.from_dict(d) for d in fields]
    format_available = .from_dict(format_available)
    frame_rates = [VideoFrameRates.from_dict(d) for d in frame_rates]
    image_techniques = [ImageTechniquesFilterType.from_dict(d) for d in image_techniques]
    license_models = [LicenseModelVideoRequest.from_dict(d) for d in license_models]
    orientations = [VideoOrientationRequest.from_dict(d) for d in orientations]
    sort_order = .from_dict(sort_order)
    release_status = .from_dict(release_status)
    facet_fields = [CreateVideoSearchFacetsFields.from_dict(d) for d in facet_fields]
    viewpoints = [ViewpointsFilterType.from_dict(d) for d in viewpoints]
    return web.Response(status=200)


async def v3_search_videos_editorial_get(request: web.Request, accept_language=None, gi_country_code=None, age_of_people=None, artists=None, aspect_ratios=None, collection_codes=None, collections_filter_type=None, compositions=None, date_from=None, date_to=None, download_product=None, editorial_video_types=None, fields=None, format_available=None, frame_rates=None, image_techniques=None, include_related_searches=None, keyword_ids=None, min_clip_length=None, max_clip_length=None, orientations=None, page=None, page_size=None, phrase=None, sort_order=None, specific_people=None, release_status=None, facet_fields=None, include_facets=None, facet_max_count=None, viewpoints=None) -> web.Response:
    """Search for editorial videos

    Use this endpoint to search current and archival video clips of celebrities, newsmakers, and events.  You&#39;ll need an API key and access token to use this resource.  You can show different information in the response by specifying values on the \&quot;fields\&quot; parameter (see details below). You can search with only an API key, and that will give you search results that are equivalent to doing a search on the GettyImages.com site without being logged in (anonymous search).  If you are a Getty Images API customer and would like to ensure that your API searches return only assets that you have a license to use, you need to also include an authorization token in the header of your request.  Please consult our [Authorization FAQ](http://developers.gettyimages.com/en/authorization-faq.html) for more information on authorization tokens, and our [Authorization Workflows](https://github.com/gettyimages/gettyimages-api/blob/master/OAuth2Workflow.md) for code examples of getting a token.  Search requests without a phrase parameter are not supported and may not always work.  ## Working with Fields Sets  Fields sets are used in the **fields** request parameter to receive a suite of metadata fields. The following fields sets are available:  #### Summary Fields Set  The **summary_set** query string parameter fields value represents a small batch of metadata fields that are often used to build search response results. The following fields are provided for every video in your result set when you include **summary_set** in your request.  &#x60;&#x60;&#x60; {     \&quot;videos\&quot;:      [         \&quot;asset_family\&quot;,          \&quot;caption\&quot;,         \&quot;collection_code\&quot;,         \&quot;collection_name\&quot;,         \&quot;display_sizes\&quot;:         [             {                 \&quot;name\&quot;: \&quot;comp\&quot;             },             {                 \&quot;name\&quot;: \&quot;preview\&quot;             },             {                 \&quot;name\&quot;: \&quot;thumb\&quot;             }         ],         \&quot;license_model\&quot;,         \&quot;title\&quot;     ] } &#x60;&#x60;&#x60;  #### Detail Fields Set  The **detail_set** query string parameter fields value represents a large batch of metadata fields that are often used to build a detailed view of videos. The following fields are provided for every video in your result set when you include **detail_set** in your request.  &#x60;&#x60;&#x60; {     \&quot;videos\&quot;:      [         \&quot;allowed_use\&quot;,         \&quot;artist\&quot;,         \&quot;asset_family\&quot;,    \&quot;call_for_image\&quot;,         \&quot;caption\&quot;,          \&quot;clip_length\&quot;,         \&quot;collection_code\&quot;,         \&quot;collection_id\&quot;,         \&quot;collection_name\&quot;,          \&quot;color_type\&quot;,         \&quot;copyright\&quot;,         \&quot;date_created\&quot;,         \&quot;display_sizes\&quot;:         [             {                 \&quot;name\&quot;: \&quot;comp\&quot;             },             {                 \&quot;name\&quot;: \&quot;preview\&quot;             },             {                 \&quot;name\&quot;: \&quot;thumb\&quot;             }         ],         \&quot;era\&quot;,         \&quot;event_ids\&quot;,         \&quot;license_model\&quot;,         \&quot;mastered_to\&quot;,         \&quot;originally_shot_on\&quot;,         \&quot;product_types\&quot;,         \&quot;quality_rank\&quot;,         \&quot;shot_speed\&quot;,         \&quot;source\&quot;,         \&quot;title\&quot;     ] } &#x60;&#x60;&#x60;  #### Display Fields Set  The **display_set** query string parameter fields value represents the fields that provide you with URLs for the low resolution files that are most frequently used to build a UI displaying search results. The following fields are provided for every video in your result set when you include **display_set** in your request.  The URI provided is subject to change at any time and must be used as-is with no modification.  &#x60;&#x60;&#x60; {     \&quot;videos\&quot;:     [         \&quot;display_sizes\&quot;:          [             {                 \&quot;is_watermarked\&quot;: &lt;boolean&gt;,                 \&quot;name\&quot;: \&quot;comp\&quot;,                 \&quot;uri\&quot;: \&quot;&lt;link&gt;\&quot;             },             {                 \&quot;is_watermarked\&quot;: &lt;boolean&gt;,                 \&quot;name\&quot;: \&quot;preview\&quot;,                 \&quot;uri\&quot;: \&quot;&lt;link&gt;\&quot;             },             {                 \&quot;is_watermarked\&quot;: &lt;boolean&gt;,                 \&quot;name\&quot;: \&quot;thumb\&quot;,                 \&quot;uri\&quot;: \&quot;&lt;link&gt;\&quot;             }         ]     ] } &#x60;&#x60;&#x60;

    :param accept_language: Provide a header to specify the language of result values. Supported values: cs (iStock only), de, en-GB, en-US, es, fi (iStock only), fr, hu (iStock only), id (iStock only), it, ja, ko (creative assets only), nl, pl (creative assets only), pt-BR, pt-PT, ro (iStock only), ru (creative assets only), sv, th (iStock only), tr, uk (iStock only), vi (iStock only), zh-HK (creative assets only).
    :type accept_language: str
    :param gi_country_code: Receive regionally relevant search results based on the value specified. Accepts only ISO Alpha-3 country codes. The Countries operation can be used to retrieve the codes.
    :type gi_country_code: str
    :param age_of_people: Provides filtering according to the age of individuals in a video.
    :type age_of_people: list | bytes
    :param artists: Search for videos by specific artists (free-text, comma-separated list of artists).
    :type artists: str
    :param aspect_ratios: Search for videos by specific aspect ratios.
    :type aspect_ratios: list | bytes
    :param collection_codes: Provides filtering by collection code.
    :type collection_codes: List[str]
    :param collections_filter_type: Use to include or exclude collections from search. The default is include
    :type collections_filter_type: dict | bytes
    :param compositions: Filter based on video composition.
    :type compositions: list | bytes
    :param date_from: Return only images that are created on or after this date. Use ISO 8601 format (e.g., 1999-12-31).
    :type date_from: str
    :param date_to: Return only images that are created on or before this date. Use ISO 8601 format (e.g., 1999-12-31).
    :type date_to: str
    :param download_product: Filters based on which product the asset will download against.                      Allowed values are easyaccess, editorialsubscription, imagepack, premiumaccess and royaltyfreesubscription.                      If you have more than one instance of a product, you may also include the ID of the product instance you wish to filter on.                       For example, some users may have more than one premiumaccess product, so the download_product value would be premiumaccess:1234.                       Product ID can be obtained from the GET /products response.
    :type download_product: str
    :param editorial_video_types: Allows filtering by types of video.
    :type editorial_video_types: list | bytes
    :param fields: Specifies fields to return. Defaults to &#39;summary_set&#39;. NOTE: Bytes returned by &#39;download_sizes&#39; field is an estimate.
    :type fields: list | bytes
    :param format_available: Filters according to the digital video format available on a film asset.
    :type format_available: dict | bytes
    :param frame_rates: Provides filtering by video frame rate (frames/second).
    :type frame_rates: list | bytes
    :param image_techniques: Filter based on image technique.
    :type image_techniques: list | bytes
    :param include_related_searches: Specifies whether or not to include related searches in the response. The default is false.
    :type include_related_searches: bool
    :param keyword_ids: Return only videos tagged with specific keyword(s). Specify using a comma-separated list of keyword Ids. If keyword Ids and phrase are both specified, only those videos matching the query phrase which also contain the requested keyword(s) are returned.
    :type keyword_ids: List[int]
    :param min_clip_length: Provides filtering by minimum length of video clip, in seconds
    :type min_clip_length: int
    :param max_clip_length: Provides filtering by maximum length of video clip, in seconds
    :type max_clip_length: int
    :param orientations: Return only videos with selected orientations.
    :type orientations: list | bytes
    :param page: Identifies page to return. Default is 1.
    :type page: int
    :param page_size: Specifies page size. Default is 30, maximum page_size is 100.
    :type page_size: int
    :param phrase: Free-text search query.
    :type phrase: str
    :param sort_order: Select sort order of results.  The default is best_match
    :type sort_order: dict | bytes
    :param specific_people: Allows filtering by specific peoples&#39; names.
    :type specific_people: List[str]
    :param release_status: Allows filtering by type of model release.
    :type release_status: dict | bytes
    :param facet_fields: Specifies the facets to return in the response. Facets provide additional search parameters to refine your results.                     The include_facets parameter must be set to \&quot;true\&quot; for facets to be returned.
    :type facet_fields: list | bytes
    :param include_facets: Specifies whether or not to include facets in the result set. Default is \&quot;false\&quot;.
    :type include_facets: bool
    :param facet_max_count: Specifies the maximum number of facets to return per type. Default is 300.
    :type facet_max_count: int
    :param viewpoints: Filter based on viewpoint.
    :type viewpoints: list | bytes

    """
    age_of_people = [AgeOfPeopleFilterType.from_dict(d) for d in age_of_people]
    aspect_ratios = [VideoAspectRatioFilterType.from_dict(d) for d in aspect_ratios]
    collections_filter_type = .from_dict(collections_filter_type)
    compositions = [CompositionsFilterType.from_dict(d) for d in compositions]
    date_from = util.deserialize_datetime(date_from)
    date_to = util.deserialize_datetime(date_to)
    editorial_video_types = [EditorialVideoType.from_dict(d) for d in editorial_video_types]
    fields = [EditorialVideosFieldValues.from_dict(d) for d in fields]
    format_available = .from_dict(format_available)
    frame_rates = [VideoFrameRates.from_dict(d) for d in frame_rates]
    image_techniques = [ImageTechniquesFilterType.from_dict(d) for d in image_techniques]
    orientations = [VideoOrientationRequest.from_dict(d) for d in orientations]
    sort_order = .from_dict(sort_order)
    release_status = .from_dict(release_status)
    facet_fields = [EditorialVideoSearchFacetsFields.from_dict(d) for d in facet_fields]
    viewpoints = [ViewpointsFilterType.from_dict(d) for d in viewpoints]
    return web.Response(status=200)
