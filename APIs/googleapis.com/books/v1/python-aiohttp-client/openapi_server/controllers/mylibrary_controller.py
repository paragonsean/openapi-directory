from typing import List, Dict
from aiohttp import web

from openapi_server.models.annotation import Annotation
from openapi_server.models.annotations import Annotations
from openapi_server.models.annotations_summary import AnnotationsSummary
from openapi_server.models.bookshelf import Bookshelf
from openapi_server.models.bookshelves import Bookshelves
from openapi_server.models.reading_position import ReadingPosition
from openapi_server.models.volumes import Volumes
from openapi_server import util


async def books_mylibrary_annotations_delete(request: web.Request, annotation_id, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, source=None) -> web.Response:
    """books_mylibrary_annotations_delete

    Deletes an annotation.

    :param annotation_id: The ID for the annotation to delete.
    :type annotation_id: str
    :param xgafv: V1 error format.
    :type xgafv: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param alt: Data format for response.
    :type alt: str
    :param param_callback: JSONP
    :type param_callback: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str
    :param source: String to identify the originator of this request.
    :type source: str

    """
    return web.Response(status=200)


async def books_mylibrary_annotations_insert(request: web.Request, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, annotation_id=None, country=None, show_only_summary_in_response=None, source=None, body=None) -> web.Response:
    """books_mylibrary_annotations_insert

    Inserts a new annotation.

    :param xgafv: V1 error format.
    :type xgafv: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param alt: Data format for response.
    :type alt: str
    :param param_callback: JSONP
    :type param_callback: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str
    :param annotation_id: The ID for the annotation to insert.
    :type annotation_id: str
    :param country: ISO-3166-1 code to override the IP-based location.
    :type country: str
    :param show_only_summary_in_response: Requests that only the summary of the specified layer be provided in the response.
    :type show_only_summary_in_response: bool
    :param source: String to identify the originator of this request.
    :type source: str
    :param body: 
    :type body: dict | bytes

    """
    body = Annotation.from_dict(body)
    return web.Response(status=200)


async def books_mylibrary_annotations_list(request: web.Request, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, content_version=None, layer_id=None, layer_ids=None, max_results=None, page_token=None, show_deleted=None, source=None, updated_max=None, updated_min=None, volume_id=None) -> web.Response:
    """books_mylibrary_annotations_list

    Retrieves a list of annotations, possibly filtered.

    :param xgafv: V1 error format.
    :type xgafv: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param alt: Data format for response.
    :type alt: str
    :param param_callback: JSONP
    :type param_callback: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str
    :param content_version: The content version for the requested volume.
    :type content_version: str
    :param layer_id: The layer ID to limit annotation by.
    :type layer_id: str
    :param layer_ids: The layer ID(s) to limit annotation by.
    :type layer_ids: List[str]
    :param max_results: Maximum number of results to return
    :type max_results: int
    :param page_token: The value of the nextToken from the previous page.
    :type page_token: str
    :param show_deleted: Set to true to return deleted annotations. updatedMin must be in the request to use this. Defaults to false.
    :type show_deleted: bool
    :param source: String to identify the originator of this request.
    :type source: str
    :param updated_max: RFC 3339 timestamp to restrict to items updated prior to this timestamp (exclusive).
    :type updated_max: str
    :param updated_min: RFC 3339 timestamp to restrict to items updated since this timestamp (inclusive).
    :type updated_min: str
    :param volume_id: The volume to restrict annotations to.
    :type volume_id: str

    """
    return web.Response(status=200)


async def books_mylibrary_annotations_summary(request: web.Request, layer_ids, volume_id, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, source=None) -> web.Response:
    """books_mylibrary_annotations_summary

    Gets the summary of specified layers.

    :param layer_ids: Array of layer IDs to get the summary for.
    :type layer_ids: List[str]
    :param volume_id: Volume id to get the summary for.
    :type volume_id: str
    :param xgafv: V1 error format.
    :type xgafv: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param alt: Data format for response.
    :type alt: str
    :param param_callback: JSONP
    :type param_callback: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str
    :param source: Optional. String to identify the originator of this request.
    :type source: str

    """
    return web.Response(status=200)


async def books_mylibrary_annotations_update(request: web.Request, annotation_id, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, source=None, body=None) -> web.Response:
    """books_mylibrary_annotations_update

    Updates an existing annotation.

    :param annotation_id: The ID for the annotation to update.
    :type annotation_id: str
    :param xgafv: V1 error format.
    :type xgafv: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param alt: Data format for response.
    :type alt: str
    :param param_callback: JSONP
    :type param_callback: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str
    :param source: String to identify the originator of this request.
    :type source: str
    :param body: 
    :type body: dict | bytes

    """
    body = Annotation.from_dict(body)
    return web.Response(status=200)


async def books_mylibrary_bookshelves_add_volume(request: web.Request, shelf, volume_id, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, reason=None, source=None) -> web.Response:
    """books_mylibrary_bookshelves_add_volume

    Adds a volume to a bookshelf.

    :param shelf: ID of bookshelf to which to add a volume.
    :type shelf: str
    :param volume_id: ID of volume to add.
    :type volume_id: str
    :param xgafv: V1 error format.
    :type xgafv: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param alt: Data format for response.
    :type alt: str
    :param param_callback: JSONP
    :type param_callback: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str
    :param reason: The reason for which the book is added to the library.
    :type reason: str
    :param source: String to identify the originator of this request.
    :type source: str

    """
    return web.Response(status=200)


async def books_mylibrary_bookshelves_clear_volumes(request: web.Request, shelf, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, source=None) -> web.Response:
    """books_mylibrary_bookshelves_clear_volumes

    Clears all volumes from a bookshelf.

    :param shelf: ID of bookshelf from which to remove a volume.
    :type shelf: str
    :param xgafv: V1 error format.
    :type xgafv: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param alt: Data format for response.
    :type alt: str
    :param param_callback: JSONP
    :type param_callback: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str
    :param source: String to identify the originator of this request.
    :type source: str

    """
    return web.Response(status=200)


async def books_mylibrary_bookshelves_get(request: web.Request, shelf, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, source=None) -> web.Response:
    """books_mylibrary_bookshelves_get

    Retrieves metadata for a specific bookshelf belonging to the authenticated user.

    :param shelf: ID of bookshelf to retrieve.
    :type shelf: str
    :param xgafv: V1 error format.
    :type xgafv: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param alt: Data format for response.
    :type alt: str
    :param param_callback: JSONP
    :type param_callback: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str
    :param source: String to identify the originator of this request.
    :type source: str

    """
    return web.Response(status=200)


async def books_mylibrary_bookshelves_list(request: web.Request, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, source=None) -> web.Response:
    """books_mylibrary_bookshelves_list

    Retrieves a list of bookshelves belonging to the authenticated user.

    :param xgafv: V1 error format.
    :type xgafv: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param alt: Data format for response.
    :type alt: str
    :param param_callback: JSONP
    :type param_callback: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str
    :param source: String to identify the originator of this request.
    :type source: str

    """
    return web.Response(status=200)


async def books_mylibrary_bookshelves_move_volume(request: web.Request, shelf, volume_id, volume_position, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, source=None) -> web.Response:
    """books_mylibrary_bookshelves_move_volume

    Moves a volume within a bookshelf.

    :param shelf: ID of bookshelf with the volume.
    :type shelf: str
    :param volume_id: ID of volume to move.
    :type volume_id: str
    :param volume_position: Position on shelf to move the item (0 puts the item before the current first item, 1 puts it between the first and the second and so on.)
    :type volume_position: int
    :param xgafv: V1 error format.
    :type xgafv: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param alt: Data format for response.
    :type alt: str
    :param param_callback: JSONP
    :type param_callback: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str
    :param source: String to identify the originator of this request.
    :type source: str

    """
    return web.Response(status=200)


async def books_mylibrary_bookshelves_remove_volume(request: web.Request, shelf, volume_id, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, reason=None, source=None) -> web.Response:
    """books_mylibrary_bookshelves_remove_volume

    Removes a volume from a bookshelf.

    :param shelf: ID of bookshelf from which to remove a volume.
    :type shelf: str
    :param volume_id: ID of volume to remove.
    :type volume_id: str
    :param xgafv: V1 error format.
    :type xgafv: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param alt: Data format for response.
    :type alt: str
    :param param_callback: JSONP
    :type param_callback: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str
    :param reason: The reason for which the book is removed from the library.
    :type reason: str
    :param source: String to identify the originator of this request.
    :type source: str

    """
    return web.Response(status=200)


async def books_mylibrary_bookshelves_volumes_list(request: web.Request, shelf, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, country=None, max_results=None, projection=None, q=None, show_preorders=None, source=None, start_index=None) -> web.Response:
    """books_mylibrary_bookshelves_volumes_list

    Gets volume information for volumes on a bookshelf.

    :param shelf: The bookshelf ID or name retrieve volumes for.
    :type shelf: str
    :param xgafv: V1 error format.
    :type xgafv: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param alt: Data format for response.
    :type alt: str
    :param param_callback: JSONP
    :type param_callback: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str
    :param country: ISO-3166-1 code to override the IP-based location.
    :type country: str
    :param max_results: Maximum number of results to return
    :type max_results: int
    :param projection: Restrict information returned to a set of selected fields.
    :type projection: str
    :param q: Full-text search query string in this bookshelf.
    :type q: str
    :param show_preorders: Set to true to show pre-ordered books. Defaults to false.
    :type show_preorders: bool
    :param source: String to identify the originator of this request.
    :type source: str
    :param start_index: Index of the first element to return (starts at 0)
    :type start_index: int

    """
    return web.Response(status=200)


async def books_mylibrary_readingpositions_get(request: web.Request, volume_id, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, content_version=None, source=None) -> web.Response:
    """books_mylibrary_readingpositions_get

    Retrieves my reading position information for a volume.

    :param volume_id: ID of volume for which to retrieve a reading position.
    :type volume_id: str
    :param xgafv: V1 error format.
    :type xgafv: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param alt: Data format for response.
    :type alt: str
    :param param_callback: JSONP
    :type param_callback: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str
    :param content_version: Volume content version for which this reading position is requested.
    :type content_version: str
    :param source: String to identify the originator of this request.
    :type source: str

    """
    return web.Response(status=200)


async def books_mylibrary_readingpositions_set_position(request: web.Request, volume_id, position, timestamp, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, action=None, content_version=None, device_cookie=None, source=None) -> web.Response:
    """books_mylibrary_readingpositions_set_position

    Sets my reading position information for a volume.

    :param volume_id: ID of volume for which to update the reading position.
    :type volume_id: str
    :param position: Position string for the new volume reading position.
    :type position: str
    :param timestamp: RFC 3339 UTC format timestamp associated with this reading position.
    :type timestamp: str
    :param xgafv: V1 error format.
    :type xgafv: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param alt: Data format for response.
    :type alt: str
    :param param_callback: JSONP
    :type param_callback: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str
    :param action: Action that caused this reading position to be set.
    :type action: str
    :param content_version: Volume content version for which this reading position applies.
    :type content_version: str
    :param device_cookie: Random persistent device cookie optional on set position.
    :type device_cookie: str
    :param source: String to identify the originator of this request.
    :type source: str

    """
    return web.Response(status=200)
