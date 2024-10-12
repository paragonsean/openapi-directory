from typing import List, Dict
from aiohttp import web

from openapi_server.models.custom_bidding_algorithm import CustomBiddingAlgorithm
from openapi_server.models.custom_bidding_algorithm_rules import CustomBiddingAlgorithmRules
from openapi_server.models.custom_bidding_algorithm_rules_ref import CustomBiddingAlgorithmRulesRef
from openapi_server.models.custom_bidding_script import CustomBiddingScript
from openapi_server.models.custom_bidding_script_ref import CustomBiddingScriptRef
from openapi_server.models.list_custom_bidding_algorithm_rules_response import ListCustomBiddingAlgorithmRulesResponse
from openapi_server.models.list_custom_bidding_algorithms_response import ListCustomBiddingAlgorithmsResponse
from openapi_server.models.list_custom_bidding_scripts_response import ListCustomBiddingScriptsResponse
from openapi_server import util


async def displayvideo_custom_bidding_algorithms_create(request: web.Request, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """displayvideo_custom_bidding_algorithms_create

    Creates a new custom bidding algorithm. Returns the newly created custom bidding algorithm if successful.

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
    body = CustomBiddingAlgorithm.from_dict(body)
    return web.Response(status=200)


async def displayvideo_custom_bidding_algorithms_get(request: web.Request, custom_bidding_algorithm_id, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, advertiser_id=None, partner_id=None) -> web.Response:
    """displayvideo_custom_bidding_algorithms_get

    Gets a custom bidding algorithm.

    :param custom_bidding_algorithm_id: Required. The ID of the custom bidding algorithm to fetch.
    :type custom_bidding_algorithm_id: str
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
    :param advertiser_id: The ID of the DV360 partner that has access to the custom bidding algorithm.
    :type advertiser_id: str
    :param partner_id: The ID of the DV360 partner that has access to the custom bidding algorithm.
    :type partner_id: str

    """
    return web.Response(status=200)


async def displayvideo_custom_bidding_algorithms_list(request: web.Request, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, advertiser_id=None, filter=None, order_by=None, page_size=None, page_token=None, partner_id=None) -> web.Response:
    """displayvideo_custom_bidding_algorithms_list

    Lists custom bidding algorithms that are accessible to the current user and can be used in bidding stratgies. The order is defined by the order_by parameter.

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
    :param advertiser_id: The ID of the DV360 advertiser that has access to the custom bidding algorithm.
    :type advertiser_id: str
    :param filter: Allows filtering by custom bidding algorithm fields. Supported syntax: * Filter expressions are made up of one or more restrictions. * Restrictions can be combined by &#x60;AND&#x60;. A sequence of restrictions implicitly uses &#x60;AND&#x60;. * A restriction has the form of &#x60;{field} {operator} {value}&#x60;. * The &#x60;customBiddingAlgorithmType&#x60; field must use the &#x60;EQUALS (&#x3D;)&#x60; operator. * The &#x60;displayName&#x60; field must use the &#x60;HAS (:)&#x60; operator. Supported fields: * &#x60;customBiddingAlgorithmType&#x60; * &#x60;displayName&#x60; Examples: * All custom bidding algorithms for which the display name contains \&quot;politics\&quot;: &#x60;displayName:\&quot;politics\&quot;&#x60;. * All custom bidding algorithms for which the type is \&quot;SCRIPT_BASED\&quot;: &#x60;customBiddingAlgorithmType&#x3D;SCRIPT_BASED&#x60; The length of this field should be no more than 500 characters. Reference our [filter &#x60;LIST&#x60; requests](/display-video/api/guides/how-tos/filters) guide for more information.
    :type filter: str
    :param order_by: Field by which to sort the list. Acceptable values are: * &#x60;displayName&#x60; (default) The default sorting order is ascending. To specify descending order for a field, a suffix \&quot;desc\&quot; should be added to the field name. Example: &#x60;displayName desc&#x60;.
    :type order_by: str
    :param page_size: Requested page size. Must be between &#x60;1&#x60; and &#x60;200&#x60;. If unspecified will default to &#x60;100&#x60;. Returns error code &#x60;INVALID_ARGUMENT&#x60; if an invalid value is specified.
    :type page_size: int
    :param page_token: A token identifying a page of results the server should return. Typically, this is the value of next_page_token returned from the previous call to &#x60;ListCustomBiddingAlgorithms&#x60; method. If not specified, the first page of results will be returned.
    :type page_token: str
    :param partner_id: The ID of the DV360 partner that has access to the custom bidding algorithm.
    :type partner_id: str

    """
    return web.Response(status=200)


async def displayvideo_custom_bidding_algorithms_patch(request: web.Request, custom_bidding_algorithm_id, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, update_mask=None, body=None) -> web.Response:
    """displayvideo_custom_bidding_algorithms_patch

    Updates an existing custom bidding algorithm. Returns the updated custom bidding algorithm if successful.

    :param custom_bidding_algorithm_id: Output only. The unique ID of the custom bidding algorithm. Assigned by the system.
    :type custom_bidding_algorithm_id: str
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
    :param update_mask: Required. The mask to control which fields to update.
    :type update_mask: str
    :param body: 
    :type body: dict | bytes

    """
    body = CustomBiddingAlgorithm.from_dict(body)
    return web.Response(status=200)


async def displayvideo_custom_bidding_algorithms_rules_create(request: web.Request, custom_bidding_algorithm_id, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, advertiser_id=None, partner_id=None, body=None) -> web.Response:
    """displayvideo_custom_bidding_algorithms_rules_create

    Creates a new rules resource. Returns the newly created rules resource if successful.

    :param custom_bidding_algorithm_id: Required. The ID of the custom bidding algorithm that owns the rules resource.
    :type custom_bidding_algorithm_id: str
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
    :param advertiser_id: The ID of the advertiser that owns the parent custom bidding algorithm.
    :type advertiser_id: str
    :param partner_id: The ID of the partner that owns the parent custom bidding algorithm. Only this partner will have write access to this rules resource.
    :type partner_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = CustomBiddingAlgorithmRules.from_dict(body)
    return web.Response(status=200)


async def displayvideo_custom_bidding_algorithms_rules_get(request: web.Request, custom_bidding_algorithm_id, custom_bidding_algorithm_rules_id, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, advertiser_id=None, partner_id=None) -> web.Response:
    """displayvideo_custom_bidding_algorithms_rules_get

    Retrieves a rules resource.

    :param custom_bidding_algorithm_id: Required. The ID of the custom bidding algorithm that owns the rules resource.
    :type custom_bidding_algorithm_id: str
    :param custom_bidding_algorithm_rules_id: Required. The ID of the rules resource to fetch.
    :type custom_bidding_algorithm_rules_id: str
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
    :param advertiser_id: The ID of the advertiser that owns the parent custom bidding algorithm.
    :type advertiser_id: str
    :param partner_id: The ID of the partner that owns the parent custom bidding algorithm.
    :type partner_id: str

    """
    return web.Response(status=200)


async def displayvideo_custom_bidding_algorithms_rules_list(request: web.Request, custom_bidding_algorithm_id, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, advertiser_id=None, order_by=None, page_size=None, page_token=None, partner_id=None) -> web.Response:
    """displayvideo_custom_bidding_algorithms_rules_list

    Lists rules resources that belong to the given algorithm. The order is defined by the order_by parameter.

    :param custom_bidding_algorithm_id: Required. The ID of the custom bidding algorithm that owns the rules resource.
    :type custom_bidding_algorithm_id: str
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
    :param advertiser_id: The ID of the advertiser that owns the parent custom bidding algorithm.
    :type advertiser_id: str
    :param order_by: Field by which to sort the list. Acceptable values are: * &#x60;createTime desc&#x60; (default) The default sorting order is descending. To specify ascending order for a field, the suffix \&quot;desc\&quot; should be removed. Example: &#x60;createTime&#x60;.
    :type order_by: str
    :param page_size: Requested page size. Must be between &#x60;1&#x60; and &#x60;200&#x60;. If unspecified will default to &#x60;100&#x60;. Returns error code &#x60;INVALID_ARGUMENT&#x60; if an invalid value is specified.
    :type page_size: int
    :param page_token: A token identifying a page of results the server should return. Typically, this is the value of next_page_token returned from the previous call to &#x60;ListCustomBiddingAlgorithmRules&#x60; method. If not specified, the first page of results will be returned.
    :type page_token: str
    :param partner_id: The ID of the partner that owns the parent custom bidding algorithm.
    :type partner_id: str

    """
    return web.Response(status=200)


async def displayvideo_custom_bidding_algorithms_scripts_create(request: web.Request, custom_bidding_algorithm_id, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, advertiser_id=None, partner_id=None, body=None) -> web.Response:
    """displayvideo_custom_bidding_algorithms_scripts_create

    Creates a new custom bidding script. Returns the newly created script if successful.

    :param custom_bidding_algorithm_id: Required. The ID of the custom bidding algorithm that owns the script.
    :type custom_bidding_algorithm_id: str
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
    :param advertiser_id: The ID of the advertiser that owns the parent custom bidding algorithm.
    :type advertiser_id: str
    :param partner_id: The ID of the partner that owns the parent custom bidding algorithm. Only this partner will have write access to this custom bidding script.
    :type partner_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = CustomBiddingScript.from_dict(body)
    return web.Response(status=200)


async def displayvideo_custom_bidding_algorithms_scripts_get(request: web.Request, custom_bidding_algorithm_id, custom_bidding_script_id, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, advertiser_id=None, partner_id=None) -> web.Response:
    """displayvideo_custom_bidding_algorithms_scripts_get

    Gets a custom bidding script.

    :param custom_bidding_algorithm_id: Required. The ID of the custom bidding algorithm owns the script.
    :type custom_bidding_algorithm_id: str
    :param custom_bidding_script_id: Required. The ID of the custom bidding script to fetch.
    :type custom_bidding_script_id: str
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
    :param advertiser_id: The ID of the advertiser that owns the parent custom bidding algorithm.
    :type advertiser_id: str
    :param partner_id: The ID of the partner that owns the parent custom bidding algorithm. Only this partner will have write access to this custom bidding script.
    :type partner_id: str

    """
    return web.Response(status=200)


async def displayvideo_custom_bidding_algorithms_scripts_list(request: web.Request, custom_bidding_algorithm_id, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, advertiser_id=None, order_by=None, page_size=None, page_token=None, partner_id=None) -> web.Response:
    """displayvideo_custom_bidding_algorithms_scripts_list

    Lists custom bidding scripts that belong to the given algorithm. The order is defined by the order_by parameter.

    :param custom_bidding_algorithm_id: Required. The ID of the custom bidding algorithm owns the script.
    :type custom_bidding_algorithm_id: str
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
    :param advertiser_id: The ID of the advertiser that owns the parent custom bidding algorithm.
    :type advertiser_id: str
    :param order_by: Field by which to sort the list. Acceptable values are: * &#x60;createTime desc&#x60; (default) The default sorting order is descending. To specify ascending order for a field, the suffix \&quot;desc\&quot; should be removed. Example: &#x60;createTime&#x60;.
    :type order_by: str
    :param page_size: Requested page size. Must be between &#x60;1&#x60; and &#x60;200&#x60;. If unspecified will default to &#x60;100&#x60;. Returns error code &#x60;INVALID_ARGUMENT&#x60; if an invalid value is specified.
    :type page_size: int
    :param page_token: A token identifying a page of results the server should return. Typically, this is the value of next_page_token returned from the previous call to &#x60;ListCustomBiddingScripts&#x60; method. If not specified, the first page of results will be returned.
    :type page_token: str
    :param partner_id: The ID of the partner that owns the parent custom bidding algorithm. Only this partner will have write access to this custom bidding script.
    :type partner_id: str

    """
    return web.Response(status=200)


async def displayvideo_custom_bidding_algorithms_upload_rules(request: web.Request, custom_bidding_algorithm_id, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, advertiser_id=None, partner_id=None) -> web.Response:
    """displayvideo_custom_bidding_algorithms_upload_rules

    Creates a rules reference object for an AlgorithmRules file. The resulting reference object provides a resource path where the AlgorithmRules file should be uploaded. This reference object should be included when creating a new CustomBiddingAlgorithmRules resource.

    :param custom_bidding_algorithm_id: Required. The ID of the custom bidding algorithm that owns the rules resource.
    :type custom_bidding_algorithm_id: str
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
    :param advertiser_id: The ID of the advertiser that owns the parent custom bidding algorithm.
    :type advertiser_id: str
    :param partner_id: The ID of the partner that owns the parent custom bidding algorithm.
    :type partner_id: str

    """
    return web.Response(status=200)


async def displayvideo_custom_bidding_algorithms_upload_script(request: web.Request, custom_bidding_algorithm_id, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, advertiser_id=None, partner_id=None) -> web.Response:
    """displayvideo_custom_bidding_algorithms_upload_script

    Creates a custom bidding script reference object for a script file. The resulting reference object provides a resource path to which the script file should be uploaded. This reference object should be included in when creating a new custom bidding script object.

    :param custom_bidding_algorithm_id: Required. The ID of the custom bidding algorithm owns the script.
    :type custom_bidding_algorithm_id: str
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
    :param advertiser_id: The ID of the advertiser that owns the parent custom bidding algorithm.
    :type advertiser_id: str
    :param partner_id: The ID of the partner that owns the parent custom bidding algorithm. Only this partner will have write access to this custom bidding script.
    :type partner_id: str

    """
    return web.Response(status=200)
