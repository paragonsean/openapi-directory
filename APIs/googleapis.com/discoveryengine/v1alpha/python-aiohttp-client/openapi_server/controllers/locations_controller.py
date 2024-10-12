from typing import List, Dict
from aiohttp import web

from openapi_server.models.google_cloud_discoveryengine_v1alpha_lookup_widget_config_request import GoogleCloudDiscoveryengineV1alphaLookupWidgetConfigRequest
from openapi_server.models.google_cloud_discoveryengine_v1alpha_lookup_widget_config_response import GoogleCloudDiscoveryengineV1alphaLookupWidgetConfigResponse
from openapi_server.models.google_cloud_discoveryengine_v1alpha_widget_complete_query_request import GoogleCloudDiscoveryengineV1alphaWidgetCompleteQueryRequest
from openapi_server.models.google_cloud_discoveryengine_v1alpha_widget_complete_query_response import GoogleCloudDiscoveryengineV1alphaWidgetCompleteQueryResponse
from openapi_server.models.google_cloud_discoveryengine_v1alpha_widget_converse_conversation_request import GoogleCloudDiscoveryengineV1alphaWidgetConverseConversationRequest
from openapi_server.models.google_cloud_discoveryengine_v1alpha_widget_converse_conversation_response import GoogleCloudDiscoveryengineV1alphaWidgetConverseConversationResponse
from openapi_server.models.google_cloud_discoveryengine_v1alpha_widget_search_request import GoogleCloudDiscoveryengineV1alphaWidgetSearchRequest
from openapi_server.models.google_cloud_discoveryengine_v1alpha_widget_search_response import GoogleCloudDiscoveryengineV1alphaWidgetSearchResponse
from openapi_server import util


async def discoveryengine_locations_lookup_widget_config(request: web.Request, location, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """discoveryengine_locations_lookup_widget_config

    Gets the Widget Config using the uuid.

    :param location: Required. The location resource where lookup widget will be performed. Format: &#x60;locations/{location}&#x60;
    :type location: str
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
    :param body: 
    :type body: dict | bytes

    """
    body = GoogleCloudDiscoveryengineV1alphaLookupWidgetConfigRequest.from_dict(body)
    return web.Response(status=200)


async def discoveryengine_locations_widget_complete_query(request: web.Request, location, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """discoveryengine_locations_widget_complete_query

    Performs a user input completion with keyword suggestion. Similar to the CompletionService.CompleteQuery method, but a widget version that allows CompleteQuery without API Key. It supports CompleteQuery with or without JWT token.

    :param location: Required. The location resource where widget complete query will be performed. Format: &#x60;locations/{location}&#x60;
    :type location: str
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
    :param body: 
    :type body: dict | bytes

    """
    body = GoogleCloudDiscoveryengineV1alphaWidgetCompleteQueryRequest.from_dict(body)
    return web.Response(status=200)


async def discoveryengine_locations_widget_converse_conversation(request: web.Request, location, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """discoveryengine_locations_widget_converse_conversation

    Converse a conversation with Widget.

    :param location: Required. The location resource where widget converse conversation will be performed. Format: &#x60;locations/{location}&#x60;
    :type location: str
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
    :param body: 
    :type body: dict | bytes

    """
    body = GoogleCloudDiscoveryengineV1alphaWidgetConverseConversationRequest.from_dict(body)
    return web.Response(status=200)


async def discoveryengine_locations_widget_search(request: web.Request, location, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """discoveryengine_locations_widget_search

    Performs a search. Similar to the SearchService.Search method, but a widget version that allows search without API Key. It supports search with or without JWT token.

    :param location: Required. The location resource where widget search will be performed. Format: &#x60;locations/{location}&#x60;
    :type location: str
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
    :param body: 
    :type body: dict | bytes

    """
    body = GoogleCloudDiscoveryengineV1alphaWidgetSearchRequest.from_dict(body)
    return web.Response(status=200)
