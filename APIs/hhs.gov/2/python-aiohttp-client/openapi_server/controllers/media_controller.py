from typing import List, Dict
from aiohttp import web

from openapi_server.models.media_item import MediaItem
from openapi_server.models.media_item_wrapped import MediaItemWrapped
from openapi_server.models.resources_media_id_youtube_meta_data_json_get200_response import ResourcesMediaIdYoutubeMetaDataJsonGet200Response
from openapi_server.models.syndicate_marshaller_wrapped import SyndicateMarshallerWrapped
from openapi_server import util


async def resources_media_featured_json_get(request: web.Request, sort=None, max=None, offset=None) -> web.Response:
    """Get the list of featured content in the syndication system

    Get the list of featured content in the syndication system

    :param sort: The name of the property to which sorting will be applied
    :type sort: str
    :param max: The maximum number of records to return
    :type max: int
    :param offset: Return records starting at the offset index.
    :type offset: int

    """
    return web.Response(status=200)


async def resources_media_id_content_get(request: web.Request, id, called_by_build=None) -> web.Response:
    """Get content for MediaItem

    The actual media content (html, image, etc...)

    :param id: The id of the media to show content for.
    :type id: int
    :param called_by_build: The method that called this method
    :type called_by_build: bool

    """
    return web.Response(status=200)


async def resources_media_id_embed_json_get(request: web.Request, id, flavor=None, width=None, height=None, iframe_name=None, exclude_jquery=None, exclude_div=None, div_id=None, display_method=None) -> web.Response:
    """Get embed code for MediaItem

    Get the javascript or iframe embed code for this item (to embed it on a web page).

    :param id: The id of the media to get embed code for.
    :type id: int
    :param flavor: Currently supports &#39;iframe&#39;, defaults to &#39;javascript&#39;.
    :type flavor: str
    :param width: The width of the generated iframe.
    :type width: int
    :param height: The height of the generated iframe.
    :type height: int
    :param iframe_name: The name of the iframe element
    :type iframe_name: str
    :param exclude_jquery: Should a reference to the JQuery Library be omitted?
    :type exclude_jquery: bool
    :param exclude_div: Should the div to insert content into be omitted?
    :type exclude_div: bool
    :param div_id: Should the div to insert content into have a specific name?
    :type div_id: str
    :param display_method: Method used to render an html request. Accepts one: [mv, list, feed]
    :type display_method: str

    """
    return web.Response(status=200)


async def resources_media_id_json_get(request: web.Request, id) -> web.Response:
    """Get MediaItem by ID

    Information about a specific media item

    :param id: The id of the record to look up
    :type id: int

    """
    return web.Response(status=200)


async def resources_media_id_preview_jpg_get(request: web.Request, id) -> web.Response:
    """Get Tag by ID

    Get the jpg preview of the content item where applicable.

    :param id: The id of the media to get a preview for.
    :type id: int

    """
    return web.Response(status=200)


async def resources_media_id_related_media_format_get(request: web.Request, id, format, max=None, offset=None, sort=None) -> web.Response:
    """Get related MediaItems by ID

    Get the media related to the current media item.

    :param id: The id of the media item to get related media for
    :type id: int
    :param format: Automatically added
    :type format: str
    :param max: The maximum number of records to return
    :type max: int
    :param offset: Return records starting at the offset index.
    :type offset: int
    :param sort: The name of the property to which sorting will be applied
    :type sort: str

    """
    return web.Response(status=200)


async def resources_media_id_syndicate_format_get(request: web.Request, id, format, css_class=None, strip_styles=None, strip_scripts=None, strip_images=None, strip_breaks=None, strip_classes=None, font_size=None, image_float=None, image_margin=None, autoplay=None, rel=None) -> web.Response:
    """Get syndicated content for MediaItem

    Get syndicated content.

    :param id: The id of the media to show embed code for.
    :type id: int
    :param format: Automatically added
    :type format: str
    :param css_class: The css class to target for extraction.
    :type css_class: str
    :param strip_styles: Remove in-line styles from content.
    :type strip_styles: bool
    :param strip_scripts: Remove script tags from content.
    :type strip_scripts: bool
    :param strip_images: Remove image tags from content.
    :type strip_images: bool
    :param strip_breaks: Remove break tags from content.
    :type strip_breaks: bool
    :param strip_classes: Remove class attributes from content (except &#39;syndicate&#39;).
    :type strip_classes: bool
    :param font_size: Set font size (in points) of p, div, and span tags.
    :type font_size: int
    :param image_float: Accepts valid CSS float options, such as &#39;left&#39; or &#39;right&#39;. Will inject a style into the content before rendering.
    :type image_float: str
    :param image_margin: Accepts 4 CSV values representing pixel sizes of margin similar to CSS. Default format is &#39;north,east,south,west&#39; - for example &#39;0,10,10,0&#39; would put a 10 pixel margin on the right and bottom sides of an image. Will inject a style into the content before rendering.
    :type image_margin: str
    :param autoplay: If content is a video, the embeded video will auto play when loaded.
    :type autoplay: bool
    :param rel: If content is a video, related items will be shown at the end of playback.
    :type rel: bool

    """
    return web.Response(status=200)


async def resources_media_id_thumbnail_jpg_get(request: web.Request, id) -> web.Response:
    """Get JPG thumbnail for MediaItem

    Get the jpg thumbnail of the content item where applicable.

    :param id: The id of the media to get a thumbnail for.
    :type id: int

    """
    return web.Response(status=200)


async def resources_media_id_youtube_meta_data_json_get(request: web.Request, id) -> web.Response:
    """Get Youtube metadata for MediaItem

    Youtube meta-data for a video item.

    :param id: The id of the video to show meta data for.
    :type id: int

    """
    return web.Response(status=200)


async def resources_media_json_get(request: web.Request, max=None, offset=None, sort=None, order=None, media_types=None, name=None, collection_id=None, name_contains=None, description_contains=None, source_url=None, source_url_contains=None, custom_thumbnail_url=None, custom_thumbnail_url_contains=None, date_content_authored=None, date_content_updated=None, date_content_published=None, date_content_reviewed=None, date_syndication_captured=None, date_syndication_updated=None, content_authored_since_date=None, content_authored_before_date=None, content_authored_in_range=None, content_updated_since_date=None, content_updated_before_date=None, content_updated_in_range=None, content_published_since_date=None, content_published_before_date=None, content_published_in_range=None, content_reviewed_since_date=None, content_reviewed_before_date=None, content_reviewed_in_range=None, syndication_captured_since_date=None, syndication_captured_before_date=None, syndication_captured_in_range=None, syndication_updated_since_date=None, syndication_updated_before_date=None, syndication_updated_in_range=None, syndication_visible_since_date=None, syndication_visible_before_date=None, syndication_visible_in_range=None, language_id=None, language_name=None, language_iso_code=None, hash=None, hash_contains=None, source_id=None, source_name=None, source_name_contains=None, source_acronym=None, source_acronym_contains=None, tag_ids=None, restrict_to_set=None, created_by=None) -> web.Response:
    """Get MediaItems

    Media Items Listings

    :param max: The maximum number of records to return
    :type max: int
    :param offset: The offset of the records set to return for pagination.
    :type offset: int
    :param sort: * Set of fields to sort the records by.
    :type sort: str
    :param order: * The ascending or descending order.
    :type order: str
    :param media_types: Find all media items belonging to the specified media type[s].
    :type media_types: str
    :param name: Find all media items containing the provided name, case insensitive.
    :type name: str
    :param collection_id: Restrict filtering to media items in a specific collection.
    :type collection_id: int
    :param name_contains: Find all media items containing the partial name, case insensitive.
    :type name_contains: str
    :param description_contains: Find all media items containing the provided partial description, case insensitive.
    :type description_contains: str
    :param source_url: Find all media items which have the provided sourceUrl, case insensitive.
    :type source_url: str
    :param source_url_contains: Find all media items which contain the provided partial sourceUrl, case insensitive.
    :type source_url_contains: str
    :param custom_thumbnail_url: Find all media items which have the provided customThumbnailUrl, case insensitive.
    :type custom_thumbnail_url: str
    :param custom_thumbnail_url_contains: Find all media items which contain the provided partial customThumbnailUrl, case insensitive.
    :type custom_thumbnail_url_contains: str
    :param date_content_authored: Find all media items authored on the provided day (RFC 3339, time ignored).
    :type date_content_authored: str
    :param date_content_updated: Find all media items updated on the provided day (RFC 3339, time ignored).
    :type date_content_updated: str
    :param date_content_published: Find all media items published on the provided day (RFC 3339, time ignored).
    :type date_content_published: str
    :param date_content_reviewed: Find all media items reviewed on the provided day (RFC 3339, time ignored).
    :type date_content_reviewed: str
    :param date_syndication_captured: Find all media items syndicated on the provided day (RFC 3339, time ignored).
    :type date_syndication_captured: str
    :param date_syndication_updated: Find all media items updated through the syndication system on the provided day, (RFC 3339, time ignored).
    :type date_syndication_updated: str
    :param content_authored_since_date: Find all media items authored since the provided day (RFC 3339, time ignored).
    :type content_authored_since_date: str
    :param content_authored_before_date: Find all media items authored before the provided day (RFC 3339, time ignored).
    :type content_authored_before_date: str
    :param content_authored_in_range: Find all media items authored between the provided start and end days (RFC 3339, comma separated, time ignored).
    :type content_authored_in_range: str
    :param content_updated_since_date: Find all media items updated since the provided day (RFC 3339, time ignored).
    :type content_updated_since_date: str
    :param content_updated_before_date: Find all media items updated before the provided day (RFC 3339, time ignored).
    :type content_updated_before_date: str
    :param content_updated_in_range: Find all media items updated between the provided start and end days (RFC 3339, comma separated, time ignored).
    :type content_updated_in_range: str
    :param content_published_since_date: Find all media items updated since the provided day (RFC 3339, time ignored).
    :type content_published_since_date: str
    :param content_published_before_date: Find all media items published before the provided day (RFC 3339, time ignored).
    :type content_published_before_date: str
    :param content_published_in_range: Find all media items published between the provided start and end days (RFC 3339, comma separated, time ignored).
    :type content_published_in_range: str
    :param content_reviewed_since_date: Find all media items reviewed since the provided day (RFC 3339, time ignored).
    :type content_reviewed_since_date: str
    :param content_reviewed_before_date: Find all media items reviewed before the provided day (RFC 3339, time ignored).
    :type content_reviewed_before_date: str
    :param content_reviewed_in_range: Find all media items reviewed between the provided start and end days (RFC 3339, comma separated, time ignored).
    :type content_reviewed_in_range: str
    :param syndication_captured_since_date: Find all media items authored since the provided day (RFC 3339, time ignored).
    :type syndication_captured_since_date: str
    :param syndication_captured_before_date: Find all media items authored before the provided day (RFC 3339, time ignored).
    :type syndication_captured_before_date: str
    :param syndication_captured_in_range: Find all media items authored between the provided start and end days (RFC 3339, comma separated, time ignored).
    :type syndication_captured_in_range: str
    :param syndication_updated_since_date: Find all media items updated since the provided day, (RFC 3339, time ignored).
    :type syndication_updated_since_date: str
    :param syndication_updated_before_date: Find all media items updated before the provided day, (RFC 3339, time ignored).
    :type syndication_updated_before_date: str
    :param syndication_updated_in_range: Find all media items updated between the provided start and end days, (RFC 3339, comma separated, time ignored).
    :type syndication_updated_in_range: str
    :param syndication_visible_since_date: Find all media items visible since the provided day, (RFC 3339, time ignored).
    :type syndication_visible_since_date: str
    :param syndication_visible_before_date: Find all media items visible before the provided day, (RFC 3339, time ignored).
    :type syndication_visible_before_date: str
    :param syndication_visible_in_range: Find all media items visible between the provided start and end days, (RFC 3339, comma separated, time ignored).
    :type syndication_visible_in_range: str
    :param language_id: Find all media items written in the language specified by Id.
    :type language_id: int
    :param language_name: Find all media items written in the language specified by name, case insensitive.
    :type language_name: str
    :param language_iso_code: Find all media items written in the language specified by 639-2 isoCode , case insensitive.
    :type language_iso_code: str
    :param hash: Find all media items which match the provided hash, case insensitive.
    :type hash: str
    :param hash_contains: Find all media items which match the provided partial hash, case insensitive.
    :type hash_contains: str
    :param source_id: Find all media items that belong to the source specified by Id.
    :type source_id: int
    :param source_name: Find all media items that belong to the source specified by name, case insensitive.
    :type source_name: str
    :param source_name_contains: Find all media items that belong to the source specified by partial name, case insensitive.
    :type source_name_contains: str
    :param source_acronym: Find all media items that belong to the source specified by acronym, case insensitive.
    :type source_acronym: str
    :param source_acronym_contains: Find all media items that belong to the source specified by partial acronym, case insensitive.
    :type source_acronym_contains: str
    :param tag_ids: Find only media items tagged with the specified tag Ids.
    :type tag_ids: str
    :param restrict_to_set: Find only media from within the supplied list of Ids.
    :type restrict_to_set: str
    :param created_by: Find all media items containing the createdBy value.
    :type created_by: str

    """
    date_content_authored = util.deserialize_date(date_content_authored)
    date_content_updated = util.deserialize_date(date_content_updated)
    date_content_published = util.deserialize_date(date_content_published)
    date_content_reviewed = util.deserialize_date(date_content_reviewed)
    date_syndication_captured = util.deserialize_date(date_syndication_captured)
    date_syndication_updated = util.deserialize_date(date_syndication_updated)
    content_authored_since_date = util.deserialize_date(content_authored_since_date)
    content_authored_before_date = util.deserialize_date(content_authored_before_date)
    content_updated_since_date = util.deserialize_date(content_updated_since_date)
    content_updated_before_date = util.deserialize_date(content_updated_before_date)
    content_published_since_date = util.deserialize_date(content_published_since_date)
    content_published_before_date = util.deserialize_date(content_published_before_date)
    content_reviewed_since_date = util.deserialize_date(content_reviewed_since_date)
    content_reviewed_before_date = util.deserialize_date(content_reviewed_before_date)
    syndication_captured_since_date = util.deserialize_date(syndication_captured_since_date)
    syndication_captured_before_date = util.deserialize_date(syndication_captured_before_date)
    syndication_updated_since_date = util.deserialize_date(syndication_updated_since_date)
    syndication_updated_before_date = util.deserialize_date(syndication_updated_before_date)
    syndication_visible_since_date = util.deserialize_date(syndication_visible_since_date)
    syndication_visible_before_date = util.deserialize_date(syndication_visible_before_date)
    syndication_visible_in_range = util.deserialize_date(syndication_visible_in_range)
    return web.Response(status=200)


async def resources_media_most_popular_media_format_get(request: web.Request, format, max=None, offset=None) -> web.Response:
    """Get MediaItems by popularity

    Get the media with the highest ratings.

    :param format: Automatically added
    :type format: str
    :param max: The maximum number of records to return
    :type max: int
    :param offset: The offset of the records set to return for pagination.
    :type offset: int

    """
    return web.Response(status=200)


async def resources_media_search_results_json_get(request: web.Request, q, max=None, offset=None) -> web.Response:
    """Get MediaItems by search query

    Full search

    :param q: The search query supplied by the user
    :type q: str
    :param max: The maximum number of records to return
    :type max: int
    :param offset: The offset of the records set to return for pagination.
    :type offset: int

    """
    return web.Response(status=200)
