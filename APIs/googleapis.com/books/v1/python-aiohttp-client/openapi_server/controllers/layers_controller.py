from typing import List, Dict
from aiohttp import web

from openapi_server.models.annotationsdata import Annotationsdata
from openapi_server.models.dictionary_annotationdata import DictionaryAnnotationdata
from openapi_server.models.layersummaries import Layersummaries
from openapi_server.models.layersummary import Layersummary
from openapi_server.models.volumeannotation import Volumeannotation
from openapi_server.models.volumeannotations import Volumeannotations
from openapi_server import util


async def books_layers_annotation_data_get(request: web.Request, volume_id, layer_id, annotation_data_id, content_version, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, allow_web_definitions=None, h=None, locale=None, scale=None, source=None, w=None) -> web.Response:
    """books_layers_annotation_data_get

    Gets the annotation data.

    :param volume_id: The volume to retrieve annotations for.
    :type volume_id: str
    :param layer_id: The ID for the layer to get the annotations.
    :type layer_id: str
    :param annotation_data_id: The ID of the annotation data to retrieve.
    :type annotation_data_id: str
    :param content_version: The content version for the volume you are trying to retrieve.
    :type content_version: str
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
    :param allow_web_definitions: For the dictionary layer. Whether or not to allow web definitions.
    :type allow_web_definitions: bool
    :param h: The requested pixel height for any images. If height is provided width must also be provided.
    :type h: int
    :param locale: The locale information for the data. ISO-639-1 language and ISO-3166-1 country code. Ex: &#39;en_US&#39;.
    :type locale: str
    :param scale: The requested scale for the image.
    :type scale: int
    :param source: String to identify the originator of this request.
    :type source: str
    :param w: The requested pixel width for any images. If width is provided height must also be provided.
    :type w: int

    """
    return web.Response(status=200)


async def books_layers_annotation_data_list(request: web.Request, volume_id, layer_id, content_version, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, annotation_data_id=None, h=None, locale=None, max_results=None, page_token=None, scale=None, source=None, updated_max=None, updated_min=None, w=None) -> web.Response:
    """books_layers_annotation_data_list

    Gets the annotation data for a volume and layer.

    :param volume_id: The volume to retrieve annotation data for.
    :type volume_id: str
    :param layer_id: The ID for the layer to get the annotation data.
    :type layer_id: str
    :param content_version: The content version for the requested volume.
    :type content_version: str
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
    :param annotation_data_id: The list of Annotation Data Ids to retrieve. Pagination is ignored if this is set.
    :type annotation_data_id: List[str]
    :param h: The requested pixel height for any images. If height is provided width must also be provided.
    :type h: int
    :param locale: The locale information for the data. ISO-639-1 language and ISO-3166-1 country code. Ex: &#39;en_US&#39;.
    :type locale: str
    :param max_results: Maximum number of results to return
    :type max_results: int
    :param page_token: The value of the nextToken from the previous page.
    :type page_token: str
    :param scale: The requested scale for the image.
    :type scale: int
    :param source: String to identify the originator of this request.
    :type source: str
    :param updated_max: RFC 3339 timestamp to restrict to items updated prior to this timestamp (exclusive).
    :type updated_max: str
    :param updated_min: RFC 3339 timestamp to restrict to items updated since this timestamp (inclusive).
    :type updated_min: str
    :param w: The requested pixel width for any images. If width is provided height must also be provided.
    :type w: int

    """
    return web.Response(status=200)


async def books_layers_get(request: web.Request, volume_id, summary_id, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, content_version=None, source=None) -> web.Response:
    """books_layers_get

    Gets the layer summary for a volume.

    :param volume_id: The volume to retrieve layers for.
    :type volume_id: str
    :param summary_id: The ID for the layer to get the summary for.
    :type summary_id: str
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
    :param source: String to identify the originator of this request.
    :type source: str

    """
    return web.Response(status=200)


async def books_layers_list(request: web.Request, volume_id, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, content_version=None, max_results=None, page_token=None, source=None) -> web.Response:
    """books_layers_list

    List the layer summaries for a volume.

    :param volume_id: The volume to retrieve layers for.
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
    :param content_version: The content version for the requested volume.
    :type content_version: str
    :param max_results: Maximum number of results to return
    :type max_results: int
    :param page_token: The value of the nextToken from the previous page.
    :type page_token: str
    :param source: String to identify the originator of this request.
    :type source: str

    """
    return web.Response(status=200)


async def books_layers_volume_annotations_get(request: web.Request, volume_id, layer_id, annotation_id, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, locale=None, source=None) -> web.Response:
    """books_layers_volume_annotations_get

    Gets the volume annotation.

    :param volume_id: The volume to retrieve annotations for.
    :type volume_id: str
    :param layer_id: The ID for the layer to get the annotations.
    :type layer_id: str
    :param annotation_id: The ID of the volume annotation to retrieve.
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
    :param locale: The locale information for the data. ISO-639-1 language and ISO-3166-1 country code. Ex: &#39;en_US&#39;.
    :type locale: str
    :param source: String to identify the originator of this request.
    :type source: str

    """
    return web.Response(status=200)


async def books_layers_volume_annotations_list(request: web.Request, volume_id, layer_id, content_version, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, end_offset=None, end_position=None, locale=None, max_results=None, page_token=None, show_deleted=None, source=None, start_offset=None, start_position=None, updated_max=None, updated_min=None, volume_annotations_version=None) -> web.Response:
    """books_layers_volume_annotations_list

    Gets the volume annotations for a volume and layer.

    :param volume_id: The volume to retrieve annotations for.
    :type volume_id: str
    :param layer_id: The ID for the layer to get the annotations.
    :type layer_id: str
    :param content_version: The content version for the requested volume.
    :type content_version: str
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
    :param end_offset: The end offset to end retrieving data from.
    :type end_offset: str
    :param end_position: The end position to end retrieving data from.
    :type end_position: str
    :param locale: The locale information for the data. ISO-639-1 language and ISO-3166-1 country code. Ex: &#39;en_US&#39;.
    :type locale: str
    :param max_results: Maximum number of results to return
    :type max_results: int
    :param page_token: The value of the nextToken from the previous page.
    :type page_token: str
    :param show_deleted: Set to true to return deleted annotations. updatedMin must be in the request to use this. Defaults to false.
    :type show_deleted: bool
    :param source: String to identify the originator of this request.
    :type source: str
    :param start_offset: The start offset to start retrieving data from.
    :type start_offset: str
    :param start_position: The start position to start retrieving data from.
    :type start_position: str
    :param updated_max: RFC 3339 timestamp to restrict to items updated prior to this timestamp (exclusive).
    :type updated_max: str
    :param updated_min: RFC 3339 timestamp to restrict to items updated since this timestamp (inclusive).
    :type updated_min: str
    :param volume_annotations_version: The version of the volume annotations that you are requesting.
    :type volume_annotations_version: str

    """
    return web.Response(status=200)
