from typing import List, Dict
from aiohttp import web

from openapi_server.models.account_cart_add200_response import AccountCartAdd200Response
from openapi_server.models.attribute_add200_response import AttributeAdd200Response
from openapi_server.models.attribute_delete200_response import AttributeDelete200Response
from openapi_server.models.basket_live_shipping_service_delete200_response import BasketLiveShippingServiceDelete200Response
from openapi_server.models.bridge_delete200_response import BridgeDelete200Response
from openapi_server.models.cart_bridge200_response import CartBridge200Response
from openapi_server.models.cart_catalog_price_rules_count200_response import CartCatalogPriceRulesCount200Response
from openapi_server.models.cart_clear_cache200_response import CartClearCache200Response
from openapi_server.models.cart_config200_response import CartConfig200Response
from openapi_server.models.cart_config_update import CartConfigUpdate
from openapi_server.models.cart_config_update200_response import CartConfigUpdate200Response
from openapi_server.models.cart_coupon_add import CartCouponAdd
from openapi_server.models.cart_coupon_add200_response import CartCouponAdd200Response
from openapi_server.models.cart_coupon_count200_response import CartCouponCount200Response
from openapi_server.models.cart_delete200_response import CartDelete200Response
from openapi_server.models.cart_disconnect200_response import CartDisconnect200Response
from openapi_server.models.cart_giftcard_add200_response import CartGiftcardAdd200Response
from openapi_server.models.cart_giftcard_count200_response import CartGiftcardCount200Response
from openapi_server.models.cart_info200_response import CartInfo200Response
from openapi_server.models.cart_list200_response import CartList200Response
from openapi_server.models.cart_methods200_response import CartMethods200Response
from openapi_server.models.cart_plugin_list200_response import CartPluginList200Response
from openapi_server.models.cart_script_add200_response import CartScriptAdd200Response
from openapi_server.models.cart_shipping_zones_list200_response import CartShippingZonesList200Response
from openapi_server.models.cart_validate200_response import CartValidate200Response
from openapi_server.models.model_response_cart_catalog_price_rules_list import ModelResponseCartCatalogPriceRulesList
from openapi_server.models.model_response_cart_coupon_list import ModelResponseCartCouponList
from openapi_server.models.model_response_cart_gift_card_list import ModelResponseCartGiftCardList
from openapi_server.models.model_response_cart_meta_data_list import ModelResponseCartMetaDataList
from openapi_server.models.model_response_cart_script_list import ModelResponseCartScriptList
from openapi_server import util


async def bridge_download(request: web.Request, whitelabel=None) -> web.Response:
    """bridge_download

    Download bridge for store

    :param whitelabel: Identifies if there is a necessity to download whitelabel bridge.
    :type whitelabel: bool

    """
    return web.Response(status=200)


async def cart_bridge(request: web.Request, ) -> web.Response:
    """cart_bridge

    Get bridge key and store key


    """
    return web.Response(status=200)


async def cart_catalog_price_rules_count(request: web.Request, ) -> web.Response:
    """cart_catalog_price_rules_count

    Get count of cart catalog price rules discounts.


    """
    return web.Response(status=200)


async def cart_catalog_price_rules_list(request: web.Request, page_cursor=None, start=None, count=None, ids=None, params=None, response_fields=None, exclude=None) -> web.Response:
    """cart_catalog_price_rules_list

    Get cart catalog price rules discounts.

    :param page_cursor: Used to retrieve entities via cursor-based pagination (it can&#39;t be used with any other filtering parameter)
    :type page_cursor: str
    :param start: This parameter sets the number from which you want to get entities
    :type start: int
    :param count: This parameter sets the entity amount that has to be retrieved. Max allowed count&#x3D;250
    :type count: int
    :param ids: Retrieves  catalog_price_rules by ids
    :type ids: str
    :param params: Set this parameter in order to choose which entity fields you want to retrieve
    :type params: str
    :param response_fields: Set this parameter in order to choose which entity fields you want to retrieve
    :type response_fields: str
    :param exclude: Set this parameter in order to choose which entity fields you want to ignore. Works only if parameter &#x60;params&#x60; equal force_all
    :type exclude: str

    """
    return web.Response(status=200)


async def cart_clear_cache(request: web.Request, cache_type) -> web.Response:
    """cart_clear_cache

    Clear cache on store.

    :param cache_type: Defines which cache should be cleared.
    :type cache_type: str

    """
    return web.Response(status=200)


async def cart_config(request: web.Request, params=None, exclude=None) -> web.Response:
    """cart_config

    Get list of cart configs

    :param params: Set this parameter in order to choose which entity fields you want to retrieve
    :type params: str
    :param exclude: Set this parameter in order to choose which entity fields you want to ignore. Works only if parameter &#x60;params&#x60; equal force_all
    :type exclude: str

    """
    return web.Response(status=200)


async def cart_config_update(request: web.Request, body) -> web.Response:
    """cart_config_update

    Use this API method to update custom data in client database.

    :param body: 
    :type body: dict | bytes

    """
    body = CartConfigUpdate.from_dict(body)
    return web.Response(status=200)


async def cart_coupon_add(request: web.Request, body) -> web.Response:
    """cart_coupon_add

    Create new coupon

    :param body: 
    :type body: dict | bytes

    """
    body = CartCouponAdd.from_dict(body)
    return web.Response(status=200)


async def cart_coupon_condition_add(request: web.Request, coupon_id, entity, key, operator, value, store_id=None, target=None) -> web.Response:
    """cart_coupon_condition_add

    Create new coupon condition

    :param coupon_id: Coupon Id
    :type coupon_id: str
    :param entity: Defines condition entity type
    :type entity: str
    :param key: Defines condition entity attribute key
    :type key: str
    :param operator: Defines condition operator
    :type operator: str
    :param value: Defines condition value, can be comma separated according to the operator.
    :type value: str
    :param store_id: Store Id
    :type store_id: str
    :param target: Defines condition operator
    :type target: str

    """
    return web.Response(status=200)


async def cart_coupon_count(request: web.Request, store_id=None, date_start_from=None, date_start_to=None, date_end_from=None, date_end_to=None, avail=None) -> web.Response:
    """cart_coupon_count

    Get cart coupons count.

    :param store_id: Store Id
    :type store_id: str
    :param date_start_from: Filter entity by date_start (greater or equal)
    :type date_start_from: str
    :param date_start_to: Filter entity by date_start (less or equal)
    :type date_start_to: str
    :param date_end_from: Filter entity by date_end (greater or equal)
    :type date_end_from: str
    :param date_end_to: Filter entity by date_end (less or equal)
    :type date_end_to: str
    :param avail: Defines category&#39;s visibility status
    :type avail: bool

    """
    return web.Response(status=200)


async def cart_coupon_delete(request: web.Request, id, store_id=None) -> web.Response:
    """cart_coupon_delete

    Delete coupon

    :param id: Entity id
    :type id: str
    :param store_id: Store Id
    :type store_id: str

    """
    return web.Response(status=200)


async def cart_coupon_list(request: web.Request, page_cursor=None, start=None, count=None, coupons_ids=None, store_id=None, date_start_from=None, date_start_to=None, date_end_from=None, date_end_to=None, avail=None, lang_id=None, params=None, response_fields=None, exclude=None) -> web.Response:
    """cart_coupon_list

    Get cart coupon discounts.

    :param page_cursor: Used to retrieve entities via cursor-based pagination (it can&#39;t be used with any other filtering parameter)
    :type page_cursor: str
    :param start: This parameter sets the number from which you want to get entities
    :type start: int
    :param count: This parameter sets the entity amount that has to be retrieved. Max allowed count&#x3D;250
    :type count: int
    :param coupons_ids: Filter coupons by ids
    :type coupons_ids: str
    :param store_id: Filter coupons by store id
    :type store_id: str
    :param date_start_from: Filter entity by date_start (greater or equal)
    :type date_start_from: str
    :param date_start_to: Filter entity by date_start (less or equal)
    :type date_start_to: str
    :param date_end_from: Filter entity by date_end (greater or equal)
    :type date_end_from: str
    :param date_end_to: Filter entity by date_end (less or equal)
    :type date_end_to: str
    :param avail: Filter coupons by avail status
    :type avail: bool
    :param lang_id: Language id
    :type lang_id: str
    :param params: Set this parameter in order to choose which entity fields you want to retrieve
    :type params: str
    :param response_fields: Set this parameter in order to choose which entity fields you want to retrieve
    :type response_fields: str
    :param exclude: Set this parameter in order to choose which entity fields you want to ignore. Works only if parameter &#x60;params&#x60; equal force_all
    :type exclude: str

    """
    return web.Response(status=200)


async def cart_create(request: web.Request, cart_id, store_url, etsy_client_id, etsy_refresh_token, store_id, bridge_url=None, store_root=None, store_key=None, shared_secret=None, validate_version=None, verify=None, db_tables_prefix=None, ftp_host=None, ftp_user=None, ftp_password=None, ftp_port=None, ftp_store_dir=None, api_key_3dcart=None, admin_account=None, api_path=None, api_key=None, client_id=None, access_token=None, context=None, access_token2=None, api_key_shopify=None, api_password=None, access_token_shopify=None, api_key2=None, api_username=None, encrypted_password=None, login=None, api_user_adnsf=None, api_pass=None, private_key=None, app_token=None, etsy_keystring=None, etsy_shared_secret=None, token_secret=None, ebay_client_id=None, ebay_client_secret=None, ebay_runame=None, ebay_access_token=None, ebay_refresh_token=None, ebay_environment=None, ebay_site_id=None, dw_client_id=None, dw_api_pass=None, demandware_user_name=None, demandware_user_password=None, seller_id=None, amazon_secret_key=None, amazon_access_key_id=None, marketplaces_ids=None, environment=None, hybris_client_id=None, hybris_client_secret=None, hybris_username=None, hybris_password=None, hybris_websites=None, walmart_client_id=None, walmart_client_secret=None, walmart_environment=None, walmart_channel_type=None, lightspeed_api_key=None, lightspeed_api_secret=None, shopware_access_key=None, shopware_api_key=None, shopware_api_secret=None, commercehq_api_key=None, commercehq_api_password=None, _3dcart_private_key=None, _3dcart_access_token=None, wc_consumer_key=None, wc_consumer_secret=None, magento_consumer_key=None, magento_consumer_secret=None, magento_access_token=None, magento_token_secret=None, prestashop_webservice_key=None, wix_app_id=None, wix_app_secret_key=None, wix_refresh_token=None, mercado_libre_app_id=None, mercado_libre_app_secret_key=None, mercado_libre_refresh_token=None, zid_client_id=None, zid_client_secret=None, zid_access_token=None, zid_authorization=None, zid_refresh_token=None) -> web.Response:
    """cart_create

    Add store to the account

    :param cart_id: Store’s identifier which you can get from cart_list method
    :type cart_id: str
    :param store_url: A web address of a store that you would like to connect to API2Cart
    :type store_url: str
    :param etsy_client_id: Etsy Client Id
    :type etsy_client_id: str
    :param etsy_refresh_token: Etsy Refresh token
    :type etsy_refresh_token: str
    :param store_id: Store Id
    :type store_id: str
    :param bridge_url: This parameter allows to set up store with custom bridge url (also you must use store_root parameter if a bridge folder is not in the root folder of the store)
    :type bridge_url: str
    :param store_root: Absolute path to the store root directory (used with \&quot;bridge_url\&quot; parameter)
    :type store_root: str
    :param store_key: Set this parameter if bridge is already uploaded to store
    :type store_key: str
    :param shared_secret: Shared secret
    :type shared_secret: str
    :param validate_version: Specify if api2cart should validate cart version
    :type validate_version: bool
    :param verify: Enables or disables cart&#39;s verification
    :type verify: bool
    :param db_tables_prefix: DB tables prefix
    :type db_tables_prefix: str
    :param ftp_host: FTP connection host
    :type ftp_host: str
    :param ftp_user: FTP User
    :type ftp_user: str
    :param ftp_password: FTP Password
    :type ftp_password: str
    :param ftp_port: FTP Port
    :type ftp_port: int
    :param ftp_store_dir: FTP Store dir
    :type ftp_store_dir: str
    :param api_key_3dcart: 3DCart API Key
    :type api_key_3dcart: str
    :param admin_account: It&#39;s a BigCommerce account for which API is enabled
    :type admin_account: str
    :param api_path: BigCommerce API URL
    :type api_path: str
    :param api_key: Bigcommerce API Key
    :type api_key: str
    :param client_id: Client ID of the requesting app
    :type client_id: str
    :param access_token: Access token authorizing the app to access resources on behalf of a user
    :type access_token: str
    :param context: API Path section unique to the store
    :type context: str
    :param access_token2: Access token authorizing the app to access resources on behalf of a user
    :type access_token2: str
    :param api_key_shopify: Shopify API Key
    :type api_key_shopify: str
    :param api_password: Shopify API Password
    :type api_password: str
    :param access_token_shopify: Access token authorizing the app to access resources on behalf of a user
    :type access_token_shopify: str
    :param api_key2: Neto API Key
    :type api_key2: str
    :param api_username: Neto User Name
    :type api_username: str
    :param encrypted_password: Volusion API Password
    :type encrypted_password: str
    :param login: It&#39;s a Volusion account for which API is enabled
    :type login: str
    :param api_user_adnsf: It&#39;s a AspDotNetStorefront account for which API is available
    :type api_user_adnsf: str
    :param api_pass: AspDotNetStorefront API Password
    :type api_pass: str
    :param private_key: 3DCart Application Private Key
    :type private_key: str
    :param app_token: 3DCart Token from Application
    :type app_token: str
    :param etsy_keystring: Etsy keystring
    :type etsy_keystring: str
    :param etsy_shared_secret: Etsy shared secret
    :type etsy_shared_secret: str
    :param token_secret: Secret token authorizing the app to access resources on behalf of a user
    :type token_secret: str
    :param ebay_client_id: Application ID (AppID).
    :type ebay_client_id: str
    :param ebay_client_secret: Shared Secret from eBay application
    :type ebay_client_secret: str
    :param ebay_runame: The RuName value that eBay assigns to your application.
    :type ebay_runame: str
    :param ebay_access_token: Used to authenticate API requests.
    :type ebay_access_token: str
    :param ebay_refresh_token: Used to renew the access token.
    :type ebay_refresh_token: str
    :param ebay_environment: eBay environment
    :type ebay_environment: str
    :param ebay_site_id: eBay global ID
    :type ebay_site_id: int
    :param dw_client_id: Demandware client id
    :type dw_client_id: str
    :param dw_api_pass: Demandware api password
    :type dw_api_pass: str
    :param demandware_user_name: Demandware user name
    :type demandware_user_name: str
    :param demandware_user_password: Demandware user password
    :type demandware_user_password: str
    :param seller_id: Seller Id
    :type seller_id: str
    :param amazon_secret_key: Amazon Secret Key
    :type amazon_secret_key: str
    :param amazon_access_key_id: Amazon Secret Key Id
    :type amazon_access_key_id: str
    :param marketplaces_ids: Comma separated marketplaces ids
    :type marketplaces_ids: str
    :param environment: 
    :type environment: str
    :param hybris_client_id: Omni Commerce Connector Client ID
    :type hybris_client_id: str
    :param hybris_client_secret: Omni Commerce Connector Client Secret
    :type hybris_client_secret: str
    :param hybris_username: User Name
    :type hybris_username: str
    :param hybris_password: User password
    :type hybris_password: str
    :param hybris_websites: Websites to stores mapping data
    :type hybris_websites: List[str]
    :param walmart_client_id: Walmart client ID
    :type walmart_client_id: str
    :param walmart_client_secret: Walmart client secret
    :type walmart_client_secret: str
    :param walmart_environment: Walmart environment
    :type walmart_environment: str
    :param walmart_channel_type: Walmart WM_CONSUMER.CHANNEL.TYPE header
    :type walmart_channel_type: str
    :param lightspeed_api_key: LightSpeed api key
    :type lightspeed_api_key: str
    :param lightspeed_api_secret: LightSpeed api secret
    :type lightspeed_api_secret: str
    :param shopware_access_key: Shopware access key
    :type shopware_access_key: str
    :param shopware_api_key: Shopware api key
    :type shopware_api_key: str
    :param shopware_api_secret: Shopware client secret access key
    :type shopware_api_secret: str
    :param commercehq_api_key: CommerceHQ api key
    :type commercehq_api_key: str
    :param commercehq_api_password: CommerceHQ api password
    :type commercehq_api_password: str
    :param _3dcart_private_key: 3DCart Private Key
    :type _3dcart_private_key: str
    :param _3dcart_access_token: 3DCart Token
    :type _3dcart_access_token: str
    :param wc_consumer_key: Woocommerce consumer key
    :type wc_consumer_key: str
    :param wc_consumer_secret: Woocommerce consumer secret
    :type wc_consumer_secret: str
    :param magento_consumer_key: Magento Consumer Key
    :type magento_consumer_key: str
    :param magento_consumer_secret: Magento Consumer Secret
    :type magento_consumer_secret: str
    :param magento_access_token: Magento Access Token
    :type magento_access_token: str
    :param magento_token_secret: Magento Token Secret
    :type magento_token_secret: str
    :param prestashop_webservice_key: Prestashop webservice key
    :type prestashop_webservice_key: str
    :param wix_app_id: Wix App ID
    :type wix_app_id: str
    :param wix_app_secret_key: Wix App Secret Key
    :type wix_app_secret_key: str
    :param wix_refresh_token: Wix refresh token
    :type wix_refresh_token: str
    :param mercado_libre_app_id: Mercado Libre App ID
    :type mercado_libre_app_id: str
    :param mercado_libre_app_secret_key: Mercado Libre App Secret Key
    :type mercado_libre_app_secret_key: str
    :param mercado_libre_refresh_token: Mercado Libre Refresh Token
    :type mercado_libre_refresh_token: str
    :param zid_client_id: Zid Client ID
    :type zid_client_id: int
    :param zid_client_secret: Zid Client Secret
    :type zid_client_secret: str
    :param zid_access_token: Zid Access Token
    :type zid_access_token: str
    :param zid_authorization: Zid Authorization
    :type zid_authorization: str
    :param zid_refresh_token: Zid refresh token
    :type zid_refresh_token: str

    """
    return web.Response(status=200)


async def cart_delete(request: web.Request, delete_bridge=None) -> web.Response:
    """cart_delete

    Remove store from API2Cart

    :param delete_bridge: Identifies if there is a necessity to delete bridge
    :type delete_bridge: bool

    """
    return web.Response(status=200)


async def cart_disconnect(request: web.Request, delete_bridge=None) -> web.Response:
    """cart_disconnect

    Disconnect with the store and clear store session data.

    :param delete_bridge: Identifies if there is a necessity to delete bridge
    :type delete_bridge: bool

    """
    return web.Response(status=200)


async def cart_giftcard_add(request: web.Request, amount, code=None, owner_email=None, recipient_email=None) -> web.Response:
    """cart_giftcard_add

    Create new gift card

    :param amount: Defines the gift card amount value.
    :type amount: 
    :param code: Gift card code
    :type code: str
    :param owner_email: Gift card owner email
    :type owner_email: str
    :param recipient_email: Gift card recipient email
    :type recipient_email: str

    """
    return web.Response(status=200)


async def cart_giftcard_count(request: web.Request, store_id=None) -> web.Response:
    """cart_giftcard_count

    Get gift cards count.

    :param store_id: Store Id
    :type store_id: str

    """
    return web.Response(status=200)


async def cart_giftcard_list(request: web.Request, page_cursor=None, start=None, count=None, store_id=None, params=None, response_fields=None, exclude=None) -> web.Response:
    """cart_giftcard_list

    Get gift cards list.

    :param page_cursor: Used to retrieve entities via cursor-based pagination (it can&#39;t be used with any other filtering parameter)
    :type page_cursor: str
    :param start: This parameter sets the number from which you want to get entities
    :type start: int
    :param count: This parameter sets the entity amount that has to be retrieved. Max allowed count&#x3D;250
    :type count: int
    :param store_id: Store Id
    :type store_id: str
    :param params: Set this parameter in order to choose which entity fields you want to retrieve
    :type params: str
    :param response_fields: Set this parameter in order to choose which entity fields you want to retrieve
    :type response_fields: str
    :param exclude: Set this parameter in order to choose which entity fields you want to ignore. Works only if parameter &#x60;params&#x60; equal force_all
    :type exclude: str

    """
    return web.Response(status=200)


async def cart_info(request: web.Request, params=None, response_fields=None, exclude=None, store_id=None) -> web.Response:
    """cart_info

    Get cart information

    :param params: Set this parameter in order to choose which entity fields you want to retrieve
    :type params: str
    :param response_fields: Set this parameter in order to choose which entity fields you want to retrieve
    :type response_fields: str
    :param exclude: Set this parameter in order to choose which entity fields you want to ignore. Works only if parameter &#x60;params&#x60; equal force_all
    :type exclude: str
    :param store_id: Store Id
    :type store_id: str

    """
    return web.Response(status=200)


async def cart_list(request: web.Request, ) -> web.Response:
    """cart_list

    Get list of supported carts


    """
    return web.Response(status=200)


async def cart_meta_data_list(request: web.Request, entity_id, entity=None, store_id=None, lang_id=None, key=None, count=None, page_cursor=None, params=None, response_fields=None, exclude=None) -> web.Response:
    """cart_meta_data_list

    Get entity meta data

    :param entity_id: Entity Id
    :type entity_id: str
    :param entity: Entity
    :type entity: str
    :param store_id: Store Id
    :type store_id: str
    :param lang_id: Language id
    :type lang_id: str
    :param key: Key
    :type key: str
    :param count: This parameter sets the entity amount that has to be retrieved. Max allowed count&#x3D;250
    :type count: int
    :param page_cursor: Used to retrieve entities via cursor-based pagination (it can&#39;t be used with any other filtering parameter)
    :type page_cursor: str
    :param params: Set this parameter in order to choose which entity fields you want to retrieve
    :type params: str
    :param response_fields: Set this parameter in order to choose which entity fields you want to retrieve
    :type response_fields: str
    :param exclude: Set this parameter in order to choose which entity fields you want to ignore. Works only if parameter &#x60;params&#x60; equal force_all
    :type exclude: str

    """
    return web.Response(status=200)


async def cart_meta_data_set(request: web.Request, entity_id, key, value, namespace, entity=None, store_id=None, lang_id=None) -> web.Response:
    """cart_meta_data_set

    Set meta data for a specific entity

    :param entity_id: Entity Id
    :type entity_id: str
    :param key: Key
    :type key: str
    :param value: Value
    :type value: str
    :param namespace: Metafield namespace
    :type namespace: str
    :param entity: Entity
    :type entity: str
    :param store_id: Store Id
    :type store_id: str
    :param lang_id: Language id
    :type lang_id: str

    """
    return web.Response(status=200)


async def cart_meta_data_unset(request: web.Request, entity_id, key, id, entity=None, store_id=None) -> web.Response:
    """cart_meta_data_unset

    Unset meta data for a specific entity

    :param entity_id: Entity Id
    :type entity_id: str
    :param key: Key
    :type key: str
    :param id: Entity id
    :type id: str
    :param entity: Entity
    :type entity: str
    :param store_id: Store Id
    :type store_id: str

    """
    return web.Response(status=200)


async def cart_methods(request: web.Request, ) -> web.Response:
    """cart_methods

    Get list of cart methods


    """
    return web.Response(status=200)


async def cart_plugin_list(request: web.Request, store_key=None, store_id=None, start=None, count=None) -> web.Response:
    """cart_plugin_list

    Get list of installed plugins

    :param store_key: Set this parameter if bridge is already uploaded to store
    :type store_key: str
    :param store_id: Store Id
    :type store_id: str
    :param start: This parameter sets the number from which you want to get entities
    :type start: int
    :param count: This parameter sets the entity amount that has to be retrieved. Max allowed count&#x3D;250
    :type count: int

    """
    return web.Response(status=200)


async def cart_script_add(request: web.Request, name=None, description=None, html=None, src=None, load_method=None, scope=None, store_id=None) -> web.Response:
    """cart_script_add

    Add new script to the storefront

    :param name: The user-friendly script name
    :type name: str
    :param description: The user-friendly description
    :type description: str
    :param html: An html string containing exactly one &#x60;script&#x60; tag.
    :type html: str
    :param src: The URL of the remote script
    :type src: str
    :param load_method: The load method to use for the script
    :type load_method: str
    :param scope: The page or pages on the online store where the script should be included
    :type scope: str
    :param store_id: Store Id
    :type store_id: str

    """
    return web.Response(status=200)


async def cart_script_delete(request: web.Request, id, store_id=None) -> web.Response:
    """cart_script_delete

    Remove script from the storefront

    :param id: Entity id
    :type id: str
    :param store_id: Store Id
    :type store_id: str

    """
    return web.Response(status=200)


async def cart_script_list(request: web.Request, page_cursor=None, start=None, count=None, created_from=None, created_to=None, modified_from=None, modified_to=None, script_ids=None, store_id=None, params=None, response_fields=None, exclude=None) -> web.Response:
    """cart_script_list

    Get scripts installed to the storefront

    :param page_cursor: Used to retrieve entities via cursor-based pagination (it can&#39;t be used with any other filtering parameter)
    :type page_cursor: str
    :param start: This parameter sets the number from which you want to get entities
    :type start: int
    :param count: This parameter sets the entity amount that has to be retrieved. Max allowed count&#x3D;250
    :type count: int
    :param created_from: Retrieve entities from their creation date
    :type created_from: str
    :param created_to: Retrieve entities to their creation date
    :type created_to: str
    :param modified_from: Retrieve entities from their modification date
    :type modified_from: str
    :param modified_to: Retrieve entities to their modification date
    :type modified_to: str
    :param script_ids: Retrieves only scripts with specific ids
    :type script_ids: str
    :param store_id: Store Id
    :type store_id: str
    :param params: Set this parameter in order to choose which entity fields you want to retrieve
    :type params: str
    :param response_fields: Set this parameter in order to choose which entity fields you want to retrieve
    :type response_fields: str
    :param exclude: Set this parameter in order to choose which entity fields you want to ignore. Works only if parameter &#x60;params&#x60; equal force_all
    :type exclude: str

    """
    return web.Response(status=200)


async def cart_shipping_zones_list(request: web.Request, store_id=None, start=None, count=None, params=None, response_fields=None, exclude=None) -> web.Response:
    """cart_shipping_zones_list

    Get list of shipping zones

    :param store_id: Store Id
    :type store_id: str
    :param start: This parameter sets the number from which you want to get entities
    :type start: int
    :param count: This parameter sets the entity amount that has to be retrieved. Max allowed count&#x3D;250
    :type count: int
    :param params: Set this parameter in order to choose which entity fields you want to retrieve
    :type params: str
    :param response_fields: Set this parameter in order to choose which entity fields you want to retrieve
    :type response_fields: str
    :param exclude: Set this parameter in order to choose which entity fields you want to ignore. Works only if parameter &#x60;params&#x60; equal force_all
    :type exclude: str

    """
    return web.Response(status=200)


async def cart_validate(request: web.Request, validate_version=None) -> web.Response:
    """cart_validate

    Check store availability, bridge connection for the downloadable carts, identify DB prefix, validate API accesses for API carts.

    :param validate_version: Specify if api2cart should validate cart version
    :type validate_version: bool

    """
    return web.Response(status=200)
