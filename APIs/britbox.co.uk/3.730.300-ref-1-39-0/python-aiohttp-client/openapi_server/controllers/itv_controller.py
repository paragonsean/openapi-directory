from typing import List, Dict
from aiohttp import web

from openapi_server.models.access_token import AccessToken
from openapi_server.models.item_list import ItemList
from openapi_server.models.itv_billing_history import ItvBillingHistory
from openapi_server.models.itv_billing_history_request import ItvBillingHistoryRequest
from openapi_server.models.itv_cancel_subscription_request import ItvCancelSubscriptionRequest
from openapi_server.models.itv_card_details import ItvCardDetails
from openapi_server.models.itv_change_card_details_request import ItvChangeCardDetailsRequest
from openapi_server.models.itv_change_email_request import ItvChangeEmailRequest
from openapi_server.models.itv_change_marketing_request import ItvChangeMarketingRequest
from openapi_server.models.itv_current_subscription import ItvCurrentSubscription
from openapi_server.models.itv_delete_account_request import ItvDeleteAccountRequest
from openapi_server.models.itv_entitlement_current import ItvEntitlementCurrent
from openapi_server.models.itv_entitlements_history import ItvEntitlementsHistory
from openapi_server.models.itv_feature_flag import ItvFeatureFlag
from openapi_server.models.itv_get_card_details_request import ItvGetCardDetailsRequest
from openapi_server.models.itv_get_discount_response import ItvGetDiscountResponse
from openapi_server.models.itv_google_pay_subscription_request import ItvGooglePaySubscriptionRequest
from openapi_server.models.itv_had_entitlement import ItvHadEntitlement
from openapi_server.models.itv_pin_auth_request import ItvPinAuthRequest
from openapi_server.models.itv_plans import ItvPlans
from openapi_server.models.itv_profile_token import ItvProfileToken
from openapi_server.models.itv_profile_token_request import ItvProfileTokenRequest
from openapi_server.models.itv_purchase import ItvPurchase
from openapi_server.models.itv_purchase_request import ItvPurchaseRequest
from openapi_server.models.itv_purchase_strong_request import ItvPurchaseStrongRequest
from openapi_server.models.itv_purchase_strong_response import ItvPurchaseStrongResponse
from openapi_server.models.itv_purchase_with_offer_request import ItvPurchaseWithOfferRequest
from openapi_server.models.itv_purchase_with_offer_response import ItvPurchaseWithOfferResponse
from openapi_server.models.itv_roku_transaction_request import ItvRokuTransactionRequest
from openapi_server.models.itv_subscription_full_price_renewal import ItvSubscriptionFullPriceRenewal
from openapi_server.models.itv_subscription_state import ItvSubscriptionState
from openapi_server.models.itv_subscription_status_response import ItvSubscriptionStatusResponse
from openapi_server.models.itv_update_intent_strong_request import ItvUpdateIntentStrongRequest
from openapi_server.models.itv_update_intent_strong_response import ItvUpdateIntentStrongResponse
from openapi_server.models.itv_update_payment_strong_request import ItvUpdatePaymentStrongRequest
from openapi_server.models.itv_update_profile_request import ItvUpdateProfileRequest
from openapi_server.models.itv_upgrade_plan_request import ItvUpgradePlanRequest
from openapi_server.models.itv_voucher import ItvVoucher
from openapi_server.models.itv_voucher_request import ItvVoucherRequest
from openapi_server.models.roku_plans import RokuPlans
from openapi_server.models.samsung_preview import SamsungPreview
from openapi_server.models.service_error import ServiceError
from openapi_server import util


async def activate_save_offer(request: web.Request, body, lang=None) -> web.Response:
    """activate_save_offer

    Activates the discount for a user. Only Stripe platform is currently supported.

    :param body: The coupon id to be checked.
    :type body: str
    :param lang: Language code for the preferred language to be returned in the response.  Parameter value is case-insensitive and should be   - a valid 2 letter language code without region such as en, de   - or with region such as en_us, en_au  If undefined then defaults to &#39;en&#39;, unless the server has been configured with a custom default.  See https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes 
    :type lang: str

    """
    return web.Response(status=200)


async def change_card_details(request: web.Request, platform, body, lang=None) -> web.Response:
    """change_card_details

    Change payment card details.

    :param platform: The identifier of the payment platform (stripe/itunes).
    :type platform: str
    :param body: Details of change card details request.
    :type body: dict | bytes
    :param lang: Language code for the preferred language to be returned in the response.  Parameter value is case-insensitive and should be   - a valid 2 letter language code without region such as en, de   - or with region such as en_us, en_au  If undefined then defaults to &#39;en&#39;, unless the server has been configured with a custom default.  See https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes 
    :type lang: str

    """
    body = ItvChangeCardDetailsRequest.from_dict(body)
    return web.Response(status=200)


async def change_email(request: web.Request, body, ff=None, lang=None) -> web.Response:
    """change_email

    Change email address related to account/profile.  The expected token scope is Settings. 

    :param body: New email address &amp; ITV profile token.
    :type body: dict | bytes
    :param ff: The set of opt in feature flags which cause breaking changes to responses.  While Rocket APIs look to avoid breaking changes under the active major version, the formats of responses may need to evolve over this time.  These feature flags allow clients to select which response formats they expect and avoid breaking clients as these formats evolve under the current major version.  ### Flags  - &#x60;all&#x60; - Enable all flags. Useful for testing. _Don&#39;t use in production_. - &#x60;idp&#x60; - Dynamic item detail pages with schedulable rows. - &#x60;ldp&#x60; - Dynamic list detail pages with schedulable rows. - &#x60;hb&#x60; - Hubble formatted image urls. - &#x60;rpt&#x60; - Updated resume point threshold logic. - &#x60;cas&#x60; - \&quot;Custom Asset Search\&quot;, inlcude &#x60;customAssets&#x60; in search results. - &#x60;lrl&#x60; - Do not pre-populate related list if more than &#x60;max_list_prefetch&#x60; down the page. - &#x60;cd&#x60; - Custom Destination support.  See the &#x60;feature-flags.md&#x60; for available flag details. 
    :type ff: List[str]
    :param lang: Language code for the preferred language to be returned in the response.  Parameter value is case-insensitive and should be   - a valid 2 letter language code without region such as en, de   - or with region such as en_us, en_au  If undefined then defaults to &#39;en&#39;, unless the server has been configured with a custom default.  See https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes 
    :type lang: str

    """
    body = ItvChangeEmailRequest.from_dict(body)
    return web.Response(status=200)


async def change_marketing(request: web.Request, body, ff=None, lang=None) -> web.Response:
    """change_marketing

    Change marketing preferences related to account/profile.  The expected token scope is Settings. 

    :param body: Updated marketing preferences &amp; ITV profile token.
    :type body: dict | bytes
    :param ff: The set of opt in feature flags which cause breaking changes to responses.  While Rocket APIs look to avoid breaking changes under the active major version, the formats of responses may need to evolve over this time.  These feature flags allow clients to select which response formats they expect and avoid breaking clients as these formats evolve under the current major version.  ### Flags  - &#x60;all&#x60; - Enable all flags. Useful for testing. _Don&#39;t use in production_. - &#x60;idp&#x60; - Dynamic item detail pages with schedulable rows. - &#x60;ldp&#x60; - Dynamic list detail pages with schedulable rows. - &#x60;hb&#x60; - Hubble formatted image urls. - &#x60;rpt&#x60; - Updated resume point threshold logic. - &#x60;cas&#x60; - \&quot;Custom Asset Search\&quot;, inlcude &#x60;customAssets&#x60; in search results. - &#x60;lrl&#x60; - Do not pre-populate related list if more than &#x60;max_list_prefetch&#x60; down the page. - &#x60;cd&#x60; - Custom Destination support.  See the &#x60;feature-flags.md&#x60; for available flag details. 
    :type ff: List[str]
    :param lang: Language code for the preferred language to be returned in the response.  Parameter value is case-insensitive and should be   - a valid 2 letter language code without region such as en, de   - or with region such as en_us, en_au  If undefined then defaults to &#39;en&#39;, unless the server has been configured with a custom default.  See https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes 
    :type lang: str

    """
    body = ItvChangeMarketingRequest.from_dict(body)
    return web.Response(status=200)


async def check_previous_entitlements(request: web.Request, lang=None) -> web.Response:
    """check_previous_entitlements

    Check whether the user has been previously entitled.

    :param lang: Language code for the preferred language to be returned in the response.  Parameter value is case-insensitive and should be   - a valid 2 letter language code without region such as en, de   - or with region such as en_us, en_au  If undefined then defaults to &#39;en&#39;, unless the server has been configured with a custom default.  See https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes 
    :type lang: str

    """
    return web.Response(status=200)


async def check_voucher(request: web.Request, platform, body, lang=None) -> web.Response:
    """check_voucher

    Validates the coupon/voucher for specified payment platform.

    :param platform: The identifier of the payment platform (stripe/itunes).
    :type platform: str
    :param body: Coupon/voucher.
    :type body: dict | bytes
    :param lang: Language code for the preferred language to be returned in the response.  Parameter value is case-insensitive and should be   - a valid 2 letter language code without region such as en, de   - or with region such as en_us, en_au  If undefined then defaults to &#39;en&#39;, unless the server has been configured with a custom default.  See https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes 
    :type lang: str

    """
    body = ItvVoucherRequest.from_dict(body)
    return web.Response(status=200)


async def confirm_purchase(request: web.Request, platform, body, lang=None) -> web.Response:
    """confirm_purchase

    Confirms purchase and returns the details of purchased subscription for specified payment platform.

    :param platform: The identifier of the payment platform (stripe/itunes).
    :type platform: str
    :param body: Details of a purchase request.
    :type body: dict | bytes
    :param lang: Language code for the preferred language to be returned in the response.  Parameter value is case-insensitive and should be   - a valid 2 letter language code without region such as en, de   - or with region such as en_us, en_au  If undefined then defaults to &#39;en&#39;, unless the server has been configured with a custom default.  See https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes 
    :type lang: str

    """
    body = ItvPurchaseRequest.from_dict(body)
    return web.Response(status=200)


async def confirm_purchase_strong(request: web.Request, platform, body, lang=None) -> web.Response:
    """confirm_purchase_strong

    Confirms purchase and returns the details of purchased subscription for specified payment platform.

    :param platform: The identifier of the payment platform (stripe/itunes).
    :type platform: str
    :param body: Details of a purchase request.
    :type body: dict | bytes
    :param lang: Language code for the preferred language to be returned in the response.  Parameter value is case-insensitive and should be   - a valid 2 letter language code without region such as en, de   - or with region such as en_us, en_au  If undefined then defaults to &#39;en&#39;, unless the server has been configured with a custom default.  See https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes 
    :type lang: str

    """
    body = ItvPurchaseStrongRequest.from_dict(body)
    return web.Response(status=200)


async def confirm_purchase_with_offer(request: web.Request, platform, body, lang=None) -> web.Response:
    """confirm_purchase_with_offer

    Confirms purchase and returns the details of purchased subscription for specified payment platform.

    :param platform: The identifier of the payment platform (stripe/itunes).
    :type platform: str
    :param body: Details of a purchase request.
    :type body: dict | bytes
    :param lang: Language code for the preferred language to be returned in the response.  Parameter value is case-insensitive and should be   - a valid 2 letter language code without region such as en, de   - or with region such as en_us, en_au  If undefined then defaults to &#39;en&#39;, unless the server has been configured with a custom default.  See https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes 
    :type lang: str

    """
    body = ItvPurchaseWithOfferRequest.from_dict(body)
    return web.Response(status=200)


async def delete_account(request: web.Request, body, ff=None, lang=None) -> web.Response:
    """delete_account

    Delete account in compliance with GDPR.  The expected token scope is Settings. 

    :param body: New email address &amp; ITV profile token.
    :type body: dict | bytes
    :param ff: The set of opt in feature flags which cause breaking changes to responses.  While Rocket APIs look to avoid breaking changes under the active major version, the formats of responses may need to evolve over this time.  These feature flags allow clients to select which response formats they expect and avoid breaking clients as these formats evolve under the current major version.  ### Flags  - &#x60;all&#x60; - Enable all flags. Useful for testing. _Don&#39;t use in production_. - &#x60;idp&#x60; - Dynamic item detail pages with schedulable rows. - &#x60;ldp&#x60; - Dynamic list detail pages with schedulable rows. - &#x60;hb&#x60; - Hubble formatted image urls. - &#x60;rpt&#x60; - Updated resume point threshold logic. - &#x60;cas&#x60; - \&quot;Custom Asset Search\&quot;, inlcude &#x60;customAssets&#x60; in search results. - &#x60;lrl&#x60; - Do not pre-populate related list if more than &#x60;max_list_prefetch&#x60; down the page. - &#x60;cd&#x60; - Custom Destination support.  See the &#x60;feature-flags.md&#x60; for available flag details. 
    :type ff: List[str]
    :param lang: Language code for the preferred language to be returned in the response.  Parameter value is case-insensitive and should be   - a valid 2 letter language code without region such as en, de   - or with region such as en_us, en_au  If undefined then defaults to &#39;en&#39;, unless the server has been configured with a custom default.  See https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes 
    :type lang: str

    """
    body = ItvDeleteAccountRequest.from_dict(body)
    return web.Response(status=200)


async def execute_transaction(request: web.Request, transactionid, body, lang=None) -> web.Response:
    """execute_transaction

    Sends request to execute specified transaction.

    :param transactionid: The identifier of the Roku transaction (subscribe/upgrade/downgrade/cancellation).
    :type transactionid: str
    :param body: Details of a transaction request.
    :type body: dict | bytes
    :param lang: Language code for the preferred language to be returned in the response.  Parameter value is case-insensitive and should be   - a valid 2 letter language code without region such as en, de   - or with region such as en_us, en_au  If undefined then defaults to &#39;en&#39;, unless the server has been configured with a custom default.  See https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes 
    :type lang: str

    """
    body = ItvRokuTransactionRequest.from_dict(body)
    return web.Response(status=200)


async def get_account_token_with_pin(request: web.Request, body, ff=None, lang=None) -> web.Response:
    """get_account_token_with_pin

    Provides authorization with parental control pin.  Returns an array containing account token with Playback scope.  Requires access token with Catalog scope.  Pin must be a 4-digit string 

    :param body: Details of token request.
    :type body: dict | bytes
    :param ff: The set of opt in feature flags which cause breaking changes to responses.  While Rocket APIs look to avoid breaking changes under the active major version, the formats of responses may need to evolve over this time.  These feature flags allow clients to select which response formats they expect and avoid breaking clients as these formats evolve under the current major version.  ### Flags  - &#x60;all&#x60; - Enable all flags. Useful for testing. _Don&#39;t use in production_. - &#x60;idp&#x60; - Dynamic item detail pages with schedulable rows. - &#x60;ldp&#x60; - Dynamic list detail pages with schedulable rows. - &#x60;hb&#x60; - Hubble formatted image urls. - &#x60;rpt&#x60; - Updated resume point threshold logic. - &#x60;cas&#x60; - \&quot;Custom Asset Search\&quot;, inlcude &#x60;customAssets&#x60; in search results. - &#x60;lrl&#x60; - Do not pre-populate related list if more than &#x60;max_list_prefetch&#x60; down the page. - &#x60;cd&#x60; - Custom Destination support.  See the &#x60;feature-flags.md&#x60; for available flag details. 
    :type ff: List[str]
    :param lang: Language code for the preferred language to be returned in the response.  Parameter value is case-insensitive and should be   - a valid 2 letter language code without region such as en, de   - or with region such as en_us, en_au  If undefined then defaults to &#39;en&#39;, unless the server has been configured with a custom default.  See https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes 
    :type lang: str

    """
    body = ItvPinAuthRequest.from_dict(body)
    return web.Response(status=200)


async def get_billing_history(request: web.Request, platform, body, lang=None) -> web.Response:
    """get_billing_history

    Returns the list of billing records for specified payment platform.

    :param platform: The identifier of the payment platform (stripe/itunes).
    :type platform: str
    :param body: Details of a billing history request.
    :type body: dict | bytes
    :param lang: Language code for the preferred language to be returned in the response.  Parameter value is case-insensitive and should be   - a valid 2 letter language code without region such as en, de   - or with region such as en_us, en_au  If undefined then defaults to &#39;en&#39;, unless the server has been configured with a custom default.  See https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes 
    :type lang: str

    """
    body = ItvBillingHistoryRequest.from_dict(body)
    return web.Response(status=200)


async def get_card_details(request: web.Request, platform, body, lang=None) -> web.Response:
    """get_card_details

    Get payment card details.

    :param platform: The identifier of the payment platform (stripe/itunes).
    :type platform: str
    :param body: ITV profile token in body.
    :type body: dict | bytes
    :param lang: Language code for the preferred language to be returned in the response.  Parameter value is case-insensitive and should be   - a valid 2 letter language code without region such as en, de   - or with region such as en_us, en_au  If undefined then defaults to &#39;en&#39;, unless the server has been configured with a custom default.  See https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes 
    :type lang: str

    """
    body = ItvGetCardDetailsRequest.from_dict(body)
    return web.Response(status=200)


async def get_current_entitlement(request: web.Request, lang=None) -> web.Response:
    """get_current_entitlement

    Returns current entitlement.

    :param lang: Language code for the preferred language to be returned in the response.  Parameter value is case-insensitive and should be   - a valid 2 letter language code without region such as en, de   - or with region such as en_us, en_au  If undefined then defaults to &#39;en&#39;, unless the server has been configured with a custom default.  See https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes 
    :type lang: str

    """
    return web.Response(status=200)


async def get_current_subscription(request: web.Request, platform, lang=None) -> web.Response:
    """get_current_subscription

    Returns the details of current subscription for specified payment platform.

    :param platform: The identifier of the payment platform (stripe/itunes).
    :type platform: str
    :param lang: Language code for the preferred language to be returned in the response.  Parameter value is case-insensitive and should be   - a valid 2 letter language code without region such as en, de   - or with region such as en_us, en_au  If undefined then defaults to &#39;en&#39;, unless the server has been configured with a custom default.  See https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes 
    :type lang: str

    """
    return web.Response(status=200)


async def get_entitlements_history(request: web.Request, lang=None) -> web.Response:
    """get_entitlements_history

    Returns the state of subscription for any payment platform.

    :param lang: Language code for the preferred language to be returned in the response.  Parameter value is case-insensitive and should be   - a valid 2 letter language code without region such as en, de   - or with region such as en_us, en_au  If undefined then defaults to &#39;en&#39;, unless the server has been configured with a custom default.  See https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes 
    :type lang: str

    """
    return web.Response(status=200)


async def get_feature_flag(request: web.Request, feature, lang=None) -> web.Response:
    """get_feature_flag

    Gets info whether or not a feature is enabled or disabled using a feature flag. Feature flags are set as a custom field within PM. It also supports custom feature flag data if needed. Such data can be return as well.

    :param feature: The identifier of the feature to check for feature flag.
    :type feature: str
    :param lang: Language code for the preferred language to be returned in the response.  Parameter value is case-insensitive and should be   - a valid 2 letter language code without region such as en, de   - or with region such as en_us, en_au  If undefined then defaults to &#39;en&#39;, unless the server has been configured with a custom default.  See https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes 
    :type lang: str

    """
    return web.Response(status=200)


async def get_full_price_renewal(request: web.Request, lang=None) -> web.Response:
    """get_full_price_renewal

    Returns full price renewal state and reason for specific user.

    :param lang: Language code for the preferred language to be returned in the response.  Parameter value is case-insensitive and should be   - a valid 2 letter language code without region such as en, de   - or with region such as en_us, en_au  If undefined then defaults to &#39;en&#39;, unless the server has been configured with a custom default.  See https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes 
    :type lang: str

    """
    return web.Response(status=200)


async def get_itv_profile_token(request: web.Request, body, lang=None) -> web.Response:
    """get_itv_profile_token

    Returns the ITV profile token.

    :param body: Details of token request.
    :type body: dict | bytes
    :param lang: Language code for the preferred language to be returned in the response.  Parameter value is case-insensitive and should be   - a valid 2 letter language code without region such as en, de   - or with region such as en_us, en_au  If undefined then defaults to &#39;en&#39;, unless the server has been configured with a custom default.  See https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes 
    :type lang: str

    """
    body = ItvProfileTokenRequest.from_dict(body)
    return web.Response(status=200)


async def get_public_preview(request: web.Request, ) -> web.Response:
    """get_public_preview

    Returns public preview for Samsung based on the page &#39;/samsung-preview&#39; configured in PresentationManager. There is a hard limit of max 40 items to be returned. It splits evenly items count into the page rows, remaining items are added into the first row. 


    """
    return web.Response(status=200)


async def get_recommended_list(request: web.Request, item_types=None, page=None, page_size=None, device=None, sub=None, segments=None, ff=None, lang=None) -> web.Response:
    """get_recommended_list

    Get the list of recommended items under the active profile.

    :param item_types: List of item types to filter the recommendation list
    :type item_types: List[str]
    :param page: The page of items to load. Starts from page 1.
    :type page: int
    :param page_size: The number of items to return in a page.
    :type page_size: int
    :param device: The type of device the content is targeting.
    :type device: str
    :param sub: The active subscription code.
    :type sub: str
    :param segments: The list of segments to filter the response by.
    :type segments: List[str]
    :param ff: The set of opt in feature flags which cause breaking changes to responses.  While Rocket APIs look to avoid breaking changes under the active major version, the formats of responses may need to evolve over this time.  These feature flags allow clients to select which response formats they expect and avoid breaking clients as these formats evolve under the current major version.  ### Flags  - &#x60;all&#x60; - Enable all flags. Useful for testing. _Don&#39;t use in production_. - &#x60;idp&#x60; - Dynamic item detail pages with schedulable rows. - &#x60;ldp&#x60; - Dynamic list detail pages with schedulable rows. - &#x60;hb&#x60; - Hubble formatted image urls. - &#x60;rpt&#x60; - Updated resume point threshold logic. - &#x60;cas&#x60; - \&quot;Custom Asset Search\&quot;, inlcude &#x60;customAssets&#x60; in search results. - &#x60;lrl&#x60; - Do not pre-populate related list if more than &#x60;max_list_prefetch&#x60; down the page. - &#x60;cd&#x60; - Custom Destination support.  See the &#x60;feature-flags.md&#x60; for available flag details. 
    :type ff: List[str]
    :param lang: Language code for the preferred language to be returned in the response.  Parameter value is case-insensitive and should be   - a valid 2 letter language code without region such as en, de   - or with region such as en_us, en_au  If undefined then defaults to &#39;en&#39;, unless the server has been configured with a custom default.  See https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes 
    :type lang: str

    """
    return web.Response(status=200)


async def get_save_offer(request: web.Request, lang=None) -> web.Response:
    """get_save_offer

    Checks the provided coupon id for a user. Only Stripe platform is currently supported.

    :param lang: Language code for the preferred language to be returned in the response.  Parameter value is case-insensitive and should be   - a valid 2 letter language code without region such as en, de   - or with region such as en_us, en_au  If undefined then defaults to &#39;en&#39;, unless the server has been configured with a custom default.  See https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes 
    :type lang: str

    """
    return web.Response(status=200)


async def get_subscription_state(request: web.Request, lang=None) -> web.Response:
    """get_subscription_state

    Returns the state of subscription for any payment platform.

    :param lang: Language code for the preferred language to be returned in the response.  Parameter value is case-insensitive and should be   - a valid 2 letter language code without region such as en, de   - or with region such as en_us, en_au  If undefined then defaults to &#39;en&#39;, unless the server has been configured with a custom default.  See https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes 
    :type lang: str

    """
    return web.Response(status=200)


async def get_subscription_status(request: web.Request, platform, lang=None) -> web.Response:
    """get_subscription_status

    Returns status of latest payment intent.

    :param platform: The identifier of the payment platform (stripe/itunes).
    :type platform: str
    :param lang: Language code for the preferred language to be returned in the response.  Parameter value is case-insensitive and should be   - a valid 2 letter language code without region such as en, de   - or with region such as en_us, en_au  If undefined then defaults to &#39;en&#39;, unless the server has been configured with a custom default.  See https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes 
    :type lang: str

    """
    return web.Response(status=200)


async def get_upcoming_invoice(request: web.Request, lang=None) -> web.Response:
    """get_upcoming_invoice

    Returns an upcoming invoice

    :param lang: Language code for the preferred language to be returned in the response.  Parameter value is case-insensitive and should be   - a valid 2 letter language code without region such as en, de   - or with region such as en_us, en_au  If undefined then defaults to &#39;en&#39;, unless the server has been configured with a custom default.  See https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes 
    :type lang: str

    """
    return web.Response(status=200)


async def get_voucher_by_id(request: web.Request, voucher_id, plan_id, lang=None) -> web.Response:
    """get_voucher_by_id

    Checks the provided coupon id for a user. Only Stripe platform is currently supported.

    :param voucher_id: The identifier of the voucher.
    :type voucher_id: str
    :param plan_id: The identifier of the plan.
    :type plan_id: str
    :param lang: Language code for the preferred language to be returned in the response.  Parameter value is case-insensitive and should be   - a valid 2 letter language code without region such as en, de   - or with region such as en_us, en_au  If undefined then defaults to &#39;en&#39;, unless the server has been configured with a custom default.  See https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes 
    :type lang: str

    """
    return web.Response(status=200)


async def google_pay_subscription(request: web.Request, body, lang=None) -> web.Response:
    """google_pay_subscription

    Get the list of recommended items under the active profile.

    :param body: Details of googlePay subscription request.
    :type body: dict | bytes
    :param lang: Language code for the preferred language to be returned in the response.  Parameter value is case-insensitive and should be   - a valid 2 letter language code without region such as en, de   - or with region such as en_us, en_au  If undefined then defaults to &#39;en&#39;, unless the server has been configured with a custom default.  See https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes 
    :type lang: str

    """
    body = ItvGooglePaySubscriptionRequest.from_dict(body)
    return web.Response(status=200)


async def itv_itemsummary_external_id_get(request: web.Request, external_id) -> web.Response:
    """itv_itemsummary_external_id_get

    Redirects to corresponding Axis Item details page.

    :param external_id: The external identifier of the item.
    :type external_id: str

    """
    return web.Response(status=200)


async def itv_plans_platform_get(request: web.Request, platform, lang=None) -> web.Response:
    """itv_plans_platform_get

    Returns the plans available for specified payment platform.

    :param platform: The identifier of the payment platform (stripe/itunes).
    :type platform: str
    :param lang: Language code for the preferred language to be returned in the response.  Parameter value is case-insensitive and should be   - a valid 2 letter language code without region such as en, de   - or with region such as en_us, en_au  If undefined then defaults to &#39;en&#39;, unless the server has been configured with a custom default.  See https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes 
    :type lang: str

    """
    return web.Response(status=200)


async def itv_profile_get(request: web.Request, lang=None) -> web.Response:
    """itv_profile_get

    Returns the ITV profile object.

    :param lang: Language code for the preferred language to be returned in the response.  Parameter value is case-insensitive and should be   - a valid 2 letter language code without region such as en, de   - or with region such as en_us, en_au  If undefined then defaults to &#39;en&#39;, unless the server has been configured with a custom default.  See https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes 
    :type lang: str

    """
    return web.Response(status=200)


async def itv_purchase_platform_delete(request: web.Request, platform, body, lang=None) -> web.Response:
    """itv_purchase_platform_delete

    Cancel a plan subscription.  A cancelled subscription will continue to be valid until the subscription expiry date or next renewal date. 

    :param platform: The identifier of the payment platform (stripe/itunes).
    :type platform: str
    :param body: Details of a cancellation request.
    :type body: dict | bytes
    :param lang: Language code for the preferred language to be returned in the response.  Parameter value is case-insensitive and should be   - a valid 2 letter language code without region such as en, de   - or with region such as en_us, en_au  If undefined then defaults to &#39;en&#39;, unless the server has been configured with a custom default.  See https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes 
    :type lang: str

    """
    body = ItvCancelSubscriptionRequest.from_dict(body)
    return web.Response(status=200)


async def itv_roku_plans_get(request: web.Request, lang=None) -> web.Response:
    """itv_roku_plans_get

    Gets available Roku plans.

    :param lang: Language code for the preferred language to be returned in the response.  Parameter value is case-insensitive and should be   - a valid 2 letter language code without region such as en, de   - or with region such as en_us, en_au  If undefined then defaults to &#39;en&#39;, unless the server has been configured with a custom default.  See https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes 
    :type lang: str

    """
    return web.Response(status=200)


async def resubscribe(request: web.Request, plan_id, platform, lang=None) -> web.Response:
    """resubscribe

    Resubscription for a user.

    :param plan_id: The id of the plan to renew.
    :type plan_id: str
    :param platform: The identifier of the payment platform (stripe/itunes). Only stripe is currently supported.
    :type platform: str
    :param lang: Language code for the preferred language to be returned in the response.  Parameter value is case-insensitive and should be   - a valid 2 letter language code without region such as en, de   - or with region such as en_us, en_au  If undefined then defaults to &#39;en&#39;, unless the server has been configured with a custom default.  See https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes 
    :type lang: str

    """
    return web.Response(status=200)


async def update_payment_intent_strong(request: web.Request, platform, body, lang=None) -> web.Response:
    """update_payment_intent_strong

    Change payment method details.

    :param platform: The identifier of the payment platform (stripe only is currently supported).
    :type platform: str
    :param body: Details of change card details request.
    :type body: dict | bytes
    :param lang: Language code for the preferred language to be returned in the response.  Parameter value is case-insensitive and should be   - a valid 2 letter language code without region such as en, de   - or with region such as en_us, en_au  If undefined then defaults to &#39;en&#39;, unless the server has been configured with a custom default.  See https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes 
    :type lang: str

    """
    body = ItvUpdateIntentStrongRequest.from_dict(body)
    return web.Response(status=200)


async def update_payment_method_strong(request: web.Request, platform, body, lang=None) -> web.Response:
    """update_payment_method_strong

    Change payment method details.

    :param platform: The identifier of the payment platform (stripe only is currently supported).
    :type platform: str
    :param body: Details of change card details request.
    :type body: dict | bytes
    :param lang: Language code for the preferred language to be returned in the response.  Parameter value is case-insensitive and should be   - a valid 2 letter language code without region such as en, de   - or with region such as en_us, en_au  If undefined then defaults to &#39;en&#39;, unless the server has been configured with a custom default.  See https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes 
    :type lang: str

    """
    body = ItvUpdatePaymentStrongRequest.from_dict(body)
    return web.Response(status=200)


async def update_profile(request: web.Request, body, ff=None, lang=None) -> web.Response:
    """update_profile

    Update ITV profile.  The expected token scope is Settings. 

    :param body: ITV profile object with updated values &amp; ITV profile token.
    :type body: dict | bytes
    :param ff: The set of opt in feature flags which cause breaking changes to responses.  While Rocket APIs look to avoid breaking changes under the active major version, the formats of responses may need to evolve over this time.  These feature flags allow clients to select which response formats they expect and avoid breaking clients as these formats evolve under the current major version.  ### Flags  - &#x60;all&#x60; - Enable all flags. Useful for testing. _Don&#39;t use in production_. - &#x60;idp&#x60; - Dynamic item detail pages with schedulable rows. - &#x60;ldp&#x60; - Dynamic list detail pages with schedulable rows. - &#x60;hb&#x60; - Hubble formatted image urls. - &#x60;rpt&#x60; - Updated resume point threshold logic. - &#x60;cas&#x60; - \&quot;Custom Asset Search\&quot;, inlcude &#x60;customAssets&#x60; in search results. - &#x60;lrl&#x60; - Do not pre-populate related list if more than &#x60;max_list_prefetch&#x60; down the page. - &#x60;cd&#x60; - Custom Destination support.  See the &#x60;feature-flags.md&#x60; for available flag details. 
    :type ff: List[str]
    :param lang: Language code for the preferred language to be returned in the response.  Parameter value is case-insensitive and should be   - a valid 2 letter language code without region such as en, de   - or with region such as en_us, en_au  If undefined then defaults to &#39;en&#39;, unless the server has been configured with a custom default.  See https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes 
    :type lang: str

    """
    body = ItvUpdateProfileRequest.from_dict(body)
    return web.Response(status=200)


async def upgrade_plan(request: web.Request, platform, body, lang=None) -> web.Response:
    """upgrade_plan

    Upgrades the plan for the current user.

    :param platform: The identifier of the payment platform (stripe/itunes). Only Stripe is supported
    :type platform: str
    :param body: Details of an upgrade request.
    :type body: dict | bytes
    :param lang: Language code for the preferred language to be returned in the response.  Parameter value is case-insensitive and should be   - a valid 2 letter language code without region such as en, de   - or with region such as en_us, en_au  If undefined then defaults to &#39;en&#39;, unless the server has been configured with a custom default.  See https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes 
    :type lang: str

    """
    body = ItvUpgradePlanRequest.from_dict(body)
    return web.Response(status=200)
