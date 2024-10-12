from typing import List, Dict
from aiohttp import web

from openapi_server.models.google_cloud_payments_reseller_subscription_v1_cancel_subscription_request import GoogleCloudPaymentsResellerSubscriptionV1CancelSubscriptionRequest
from openapi_server.models.google_cloud_payments_reseller_subscription_v1_cancel_subscription_response import GoogleCloudPaymentsResellerSubscriptionV1CancelSubscriptionResponse
from openapi_server.models.google_cloud_payments_reseller_subscription_v1_entitle_subscription_request import GoogleCloudPaymentsResellerSubscriptionV1EntitleSubscriptionRequest
from openapi_server.models.google_cloud_payments_reseller_subscription_v1_entitle_subscription_response import GoogleCloudPaymentsResellerSubscriptionV1EntitleSubscriptionResponse
from openapi_server.models.google_cloud_payments_reseller_subscription_v1_extend_subscription_request import GoogleCloudPaymentsResellerSubscriptionV1ExtendSubscriptionRequest
from openapi_server.models.google_cloud_payments_reseller_subscription_v1_extend_subscription_response import GoogleCloudPaymentsResellerSubscriptionV1ExtendSubscriptionResponse
from openapi_server.models.google_cloud_payments_reseller_subscription_v1_find_eligible_promotions_request import GoogleCloudPaymentsResellerSubscriptionV1FindEligiblePromotionsRequest
from openapi_server.models.google_cloud_payments_reseller_subscription_v1_find_eligible_promotions_response import GoogleCloudPaymentsResellerSubscriptionV1FindEligiblePromotionsResponse
from openapi_server.models.google_cloud_payments_reseller_subscription_v1_list_products_response import GoogleCloudPaymentsResellerSubscriptionV1ListProductsResponse
from openapi_server.models.google_cloud_payments_reseller_subscription_v1_list_promotions_response import GoogleCloudPaymentsResellerSubscriptionV1ListPromotionsResponse
from openapi_server.models.google_cloud_payments_reseller_subscription_v1_subscription import GoogleCloudPaymentsResellerSubscriptionV1Subscription
from openapi_server.models.google_cloud_payments_reseller_subscription_v1_undo_cancel_subscription_response import GoogleCloudPaymentsResellerSubscriptionV1UndoCancelSubscriptionResponse
from openapi_server import util


async def paymentsresellersubscription_partners_products_list(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, filter=None, page_size=None, page_token=None) -> web.Response:
    """paymentsresellersubscription_partners_products_list

    To retrieve the products that can be resold by the partner. It should be autenticated with a service account.

    :param parent: Required. The parent, the partner that can resell. Format: partners/{partner}
    :type parent: str
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
    :param filter: Optional. Specifies the filters for the product results. The syntax is defined in https://google.aip.dev/160 with the following caveats: 1. Only the following features are supported: - Logical operator &#x60;AND&#x60; - Comparison operator &#x60;&#x3D;&#x60; (no wildcards &#x60;*&#x60;) - Traversal operator &#x60;.&#x60; - Has operator &#x60;:&#x60; (no wildcards &#x60;*&#x60;) 2. Only the following fields are supported: - &#x60;regionCodes&#x60; - &#x60;youtubePayload.partnerEligibilityId&#x60; - &#x60;youtubePayload.postalCode&#x60; 3. Unless explicitly mentioned above, other features are not supported. Example: &#x60;regionCodes:US AND youtubePayload.postalCode&#x3D;94043 AND youtubePayload.partnerEligibilityId&#x3D;eligibility-id&#x60;
    :type filter: str
    :param page_size: Optional. The maximum number of products to return. The service may return fewer than this value. If unspecified, at most 50 products will be returned. The maximum value is 1000; values above 1000 will be coerced to 1000.
    :type page_size: int
    :param page_token: Optional. A page token, received from a previous &#x60;ListProducts&#x60; call. Provide this to retrieve the subsequent page. When paginating, all other parameters provided to &#x60;ListProducts&#x60; must match the call that provided the page token.
    :type page_token: str

    """
    return web.Response(status=200)


async def paymentsresellersubscription_partners_promotions_find_eligible(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """paymentsresellersubscription_partners_promotions_find_eligible

    To find eligible promotions for the current user. The API requires user authorization via OAuth. The bare minimum oauth scope &#x60;openid&#x60; is sufficient, which will skip the consent screen.

    :param parent: Required. The parent, the partner that can resell. Format: partners/{partner}
    :type parent: str
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
    body = GoogleCloudPaymentsResellerSubscriptionV1FindEligiblePromotionsRequest.from_dict(body)
    return web.Response(status=200)


async def paymentsresellersubscription_partners_promotions_list(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, filter=None, page_size=None, page_token=None) -> web.Response:
    """paymentsresellersubscription_partners_promotions_list

    To retrieve the promotions, such as free trial, that can be used by the partner. It should be autenticated with a service account.

    :param parent: Required. The parent, the partner that can resell. Format: partners/{partner}
    :type parent: str
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
    :param filter: Optional. Specifies the filters for the promotion results. The syntax is defined in https://google.aip.dev/160 with the following caveats: 1. Only the following features are supported: - Logical operator &#x60;AND&#x60; - Comparison operator &#x60;&#x3D;&#x60; (no wildcards &#x60;*&#x60;) - Traversal operator &#x60;.&#x60; - Has operator &#x60;:&#x60; (no wildcards &#x60;*&#x60;) 2. Only the following fields are supported: - &#x60;applicableProducts&#x60; - &#x60;regionCodes&#x60; - &#x60;youtubePayload.partnerEligibilityId&#x60; - &#x60;youtubePayload.postalCode&#x60; 3. Unless explicitly mentioned above, other features are not supported. Example: &#x60;applicableProducts:partners/partner1/products/product1 AND regionCodes:US AND youtubePayload.postalCode&#x3D;94043 AND youtubePayload.partnerEligibilityId&#x3D;eligibility-id&#x60;
    :type filter: str
    :param page_size: Optional. The maximum number of promotions to return. The service may return fewer than this value. If unspecified, at most 50 products will be returned. The maximum value is 1000; values above 1000 will be coerced to 1000.
    :type page_size: int
    :param page_token: Optional. A page token, received from a previous &#x60;ListPromotions&#x60; call. Provide this to retrieve the subsequent page. When paginating, all other parameters provided to &#x60;ListPromotions&#x60; must match the call that provided the page token.
    :type page_token: str

    """
    return web.Response(status=200)


async def paymentsresellersubscription_partners_subscriptions_cancel(request: web.Request, name, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """paymentsresellersubscription_partners_subscriptions_cancel

    Used by partners to cancel a subscription service either immediately or by the end of the current billing cycle for their customers. It should be called directly by the partner using service accounts.

    :param name: Required. The name of the subscription resource to be cancelled. It will have the format of \&quot;partners/{partner_id}/subscriptions/{subscription_id}\&quot;
    :type name: str
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
    body = GoogleCloudPaymentsResellerSubscriptionV1CancelSubscriptionRequest.from_dict(body)
    return web.Response(status=200)


async def paymentsresellersubscription_partners_subscriptions_create(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, subscription_id=None, body=None) -> web.Response:
    """paymentsresellersubscription_partners_subscriptions_create

    Used by partners to create a subscription for their customers. The created subscription is associated with the end user inferred from the end user credentials. This API must be authorized by the end user using OAuth.

    :param parent: Required. The parent resource name, which is the identifier of the partner. It will have the format of \&quot;partners/{partner_id}\&quot;.
    :type parent: str
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
    :param subscription_id: Required. Identifies the subscription resource on the Partner side. The value is restricted to 63 ASCII characters at the maximum. If a subscription was previously created with the same subscription_id, we will directly return that one.
    :type subscription_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = GoogleCloudPaymentsResellerSubscriptionV1Subscription.from_dict(body)
    return web.Response(status=200)


async def paymentsresellersubscription_partners_subscriptions_entitle(request: web.Request, name, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """paymentsresellersubscription_partners_subscriptions_entitle

    Used by partners to entitle a previously provisioned subscription to the current end user. The end user identity is inferred from the authorized credential of the request. This API must be authorized by the end user using OAuth.

    :param name: Required. The name of the subscription resource that is entitled to the current end user. It will have the format of \&quot;partners/{partner_id}/subscriptions/{subscription_id}\&quot;
    :type name: str
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
    body = GoogleCloudPaymentsResellerSubscriptionV1EntitleSubscriptionRequest.from_dict(body)
    return web.Response(status=200)


async def paymentsresellersubscription_partners_subscriptions_extend(request: web.Request, name, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """paymentsresellersubscription_partners_subscriptions_extend

    [Opt-in only] Most partners should be on auto-extend by default. Used by partners to extend a subscription service for their customers on an ongoing basis for the subscription to remain active and renewable. It should be called directly by the partner using service accounts.

    :param name: Required. The name of the subscription resource to be extended. It will have the format of \&quot;partners/{partner_id}/subscriptions/{subscription_id}\&quot;.
    :type name: str
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
    body = GoogleCloudPaymentsResellerSubscriptionV1ExtendSubscriptionRequest.from_dict(body)
    return web.Response(status=200)


async def paymentsresellersubscription_partners_subscriptions_get(request: web.Request, name, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None) -> web.Response:
    """paymentsresellersubscription_partners_subscriptions_get

    Used by partners to get a subscription by id. It should be called directly by the partner using service accounts.

    :param name: Required. The name of the subscription resource to retrieve. It will have the format of \&quot;partners/{partner_id}/subscriptions/{subscription_id}\&quot;
    :type name: str
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

    """
    return web.Response(status=200)


async def paymentsresellersubscription_partners_subscriptions_provision(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, subscription_id=None, body=None) -> web.Response:
    """paymentsresellersubscription_partners_subscriptions_provision

    Used by partners to provision a subscription for their customers. This creates a subscription without associating it with the end user account. EntitleSubscription must be called separately using OAuth in order for the end user account to be associated with the subscription. It should be called directly by the partner using service accounts.

    :param parent: Required. The parent resource name, which is the identifier of the partner. It will have the format of \&quot;partners/{partner_id}\&quot;.
    :type parent: str
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
    :param subscription_id: Required. Identifies the subscription resource on the Partner side. The value is restricted to 63 ASCII characters at the maximum. If a subscription was previously created with the same subscription_id, we will directly return that one.
    :type subscription_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = GoogleCloudPaymentsResellerSubscriptionV1Subscription.from_dict(body)
    return web.Response(status=200)


async def paymentsresellersubscription_partners_subscriptions_undo_cancel(request: web.Request, name, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """paymentsresellersubscription_partners_subscriptions_undo_cancel

    Used by partners to revoke the pending cancellation of a subscription, which is currently in &#x60;STATE_CANCEL_AT_END_OF_CYCLE&#x60; state. If the subscription is already cancelled, the request will fail. It should be called directly by the partner using service accounts.

    :param name: Required. The name of the subscription resource whose pending cancellation needs to be undone. It will have the format of \&quot;partners/{partner_id}/subscriptions/{subscription_id}\&quot;
    :type name: str
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
    :type body: 

    """
    return web.Response(status=200)
