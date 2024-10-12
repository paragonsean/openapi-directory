from typing import List, Dict
from aiohttp import web

from openapi_server.models.books_volumes_recommended_rate_response import BooksVolumesRecommendedRateResponse
from openapi_server.models.volume import Volume
from openapi_server.models.volumes import Volumes
from openapi_server import util


async def books_volumes_associated_list(request: web.Request, volume_id, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, association=None, locale=None, max_allowed_maturity_rating=None, source=None) -> web.Response:
    """books_volumes_associated_list

    Return a list of associated books.

    :param volume_id: ID of the source volume.
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
    :param association: Association type.
    :type association: str
    :param locale: ISO-639-1 language and ISO-3166-1 country code. Ex: &#39;en_US&#39;. Used for generating recommendations.
    :type locale: str
    :param max_allowed_maturity_rating: The maximum allowed maturity rating of returned recommendations. Books with a higher maturity rating are filtered out.
    :type max_allowed_maturity_rating: str
    :param source: String to identify the originator of this request.
    :type source: str

    """
    return web.Response(status=200)


async def books_volumes_get(request: web.Request, volume_id, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, country=None, include_non_comics_series=None, partner=None, projection=None, source=None, user_library_consistent_read=None) -> web.Response:
    """books_volumes_get

    Gets volume information for a single volume.

    :param volume_id: ID of volume to retrieve.
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
    :param country: ISO-3166-1 code to override the IP-based location.
    :type country: str
    :param include_non_comics_series: Set to true to include non-comics series. Defaults to false.
    :type include_non_comics_series: bool
    :param partner: Brand results for partner ID.
    :type partner: str
    :param projection: Restrict information returned to a set of selected fields.
    :type projection: str
    :param source: string to identify the originator of this request.
    :type source: str
    :param user_library_consistent_read: 
    :type user_library_consistent_read: bool

    """
    return web.Response(status=200)


async def books_volumes_list(request: web.Request, q, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, download=None, filter=None, lang_restrict=None, library_restrict=None, max_allowed_maturity_rating=None, max_results=None, order_by=None, partner=None, print_type=None, projection=None, show_preorders=None, source=None, start_index=None) -> web.Response:
    """books_volumes_list

    Performs a book search.

    :param q: Full-text search query string.
    :type q: str
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
    :param download: Restrict to volumes by download availability.
    :type download: str
    :param filter: Filter search results.
    :type filter: str
    :param lang_restrict: Restrict results to books with this language code.
    :type lang_restrict: str
    :param library_restrict: Restrict search to this user&#39;s library.
    :type library_restrict: str
    :param max_allowed_maturity_rating: The maximum allowed maturity rating of returned recommendations. Books with a higher maturity rating are filtered out.
    :type max_allowed_maturity_rating: str
    :param max_results: Maximum number of results to return.
    :type max_results: int
    :param order_by: Sort search results.
    :type order_by: str
    :param partner: Restrict and brand results for partner ID.
    :type partner: str
    :param print_type: Restrict to books or magazines.
    :type print_type: str
    :param projection: Restrict information returned to a set of selected fields.
    :type projection: str
    :param show_preorders: Set to true to show books available for preorder. Defaults to false.
    :type show_preorders: bool
    :param source: String to identify the originator of this request.
    :type source: str
    :param start_index: Index of the first result to return (starts at 0)
    :type start_index: int

    """
    return web.Response(status=200)


async def books_volumes_mybooks_list(request: web.Request, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, acquire_method=None, country=None, locale=None, max_results=None, processing_state=None, source=None, start_index=None) -> web.Response:
    """books_volumes_mybooks_list

    Return a list of books in My Library.

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
    :param acquire_method: How the book was acquired
    :type acquire_method: List[str]
    :param country: ISO-3166-1 code to override the IP-based location.
    :type country: str
    :param locale: ISO-639-1 language and ISO-3166-1 country code. Ex:&#39;en_US&#39;. Used for generating recommendations.
    :type locale: str
    :param max_results: Maximum number of results to return.
    :type max_results: int
    :param processing_state: The processing state of the user uploaded volumes to be returned. Applicable only if the UPLOADED is specified in the acquireMethod.
    :type processing_state: List[str]
    :param source: String to identify the originator of this request.
    :type source: str
    :param start_index: Index of the first result to return (starts at 0)
    :type start_index: int

    """
    return web.Response(status=200)


async def books_volumes_recommended_list(request: web.Request, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, locale=None, max_allowed_maturity_rating=None, source=None) -> web.Response:
    """books_volumes_recommended_list

    Return a list of recommended books for the current user.

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
    :param locale: ISO-639-1 language and ISO-3166-1 country code. Ex: &#39;en_US&#39;. Used for generating recommendations.
    :type locale: str
    :param max_allowed_maturity_rating: The maximum allowed maturity rating of returned recommendations. Books with a higher maturity rating are filtered out.
    :type max_allowed_maturity_rating: str
    :param source: String to identify the originator of this request.
    :type source: str

    """
    return web.Response(status=200)


async def books_volumes_recommended_rate(request: web.Request, rating, volume_id, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, locale=None, source=None) -> web.Response:
    """books_volumes_recommended_rate

    Rate a recommended book for the current user.

    :param rating: Rating to be given to the volume.
    :type rating: str
    :param volume_id: ID of the source volume.
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
    :param locale: ISO-639-1 language and ISO-3166-1 country code. Ex: &#39;en_US&#39;. Used for generating recommendations.
    :type locale: str
    :param source: String to identify the originator of this request.
    :type source: str

    """
    return web.Response(status=200)


async def books_volumes_useruploaded_list(request: web.Request, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, locale=None, max_results=None, processing_state=None, source=None, start_index=None, volume_id=None) -> web.Response:
    """books_volumes_useruploaded_list

    Return a list of books uploaded by the current user.

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
    :param locale: ISO-639-1 language and ISO-3166-1 country code. Ex: &#39;en_US&#39;. Used for generating recommendations.
    :type locale: str
    :param max_results: Maximum number of results to return.
    :type max_results: int
    :param processing_state: The processing state of the user uploaded volumes to be returned.
    :type processing_state: List[str]
    :param source: String to identify the originator of this request.
    :type source: str
    :param start_index: Index of the first result to return (starts at 0)
    :type start_index: int
    :param volume_id: The ids of the volumes to be returned. If not specified all that match the processingState are returned.
    :type volume_id: List[str]

    """
    return web.Response(status=200)
