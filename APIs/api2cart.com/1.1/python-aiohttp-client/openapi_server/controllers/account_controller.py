from typing import List, Dict
from aiohttp import web

from openapi_server.models.account_cart_add import AccountCartAdd
from openapi_server.models.account_cart_add200_response import AccountCartAdd200Response
from openapi_server.models.account_cart_list200_response import AccountCartList200Response
from openapi_server.models.account_config_update200_response import AccountConfigUpdate200Response
from openapi_server.models.account_failed_webhooks200_response import AccountFailedWebhooks200Response
from openapi_server.models.account_supported_platforms200_response import AccountSupportedPlatforms200Response
from openapi_server import util


async def account_cart_add(request: web.Request, body) -> web.Response:
    """account_cart_add

    Add store to the account

    :param body: 
    :type body: dict | bytes

    """
    body = AccountCartAdd.from_dict(body)
    return web.Response(status=200)


async def account_cart_list(request: web.Request, params=None, exclude=None, request_from_date=None, request_to_date=None, store_url=None, store_key=None) -> web.Response:
    """account_cart_list

    Get list of carts.

    :param params: Set this parameter in order to choose which entity fields you want to retrieve
    :type params: str
    :param exclude: Set this parameter in order to choose which entity fields you want to ignore. Works only if parameter &#x60;params&#x60; equal force_all
    :type exclude: str
    :param request_from_date: Retrieve entities from their creation date
    :type request_from_date: str
    :param request_to_date: Retrieve entities to their creation date
    :type request_to_date: str
    :param store_url: A web address of a store
    :type store_url: str
    :param store_key: Find store by store key
    :type store_key: str

    """
    return web.Response(status=200)


async def account_config_update(request: web.Request, new_store_key=None, bridge_url=None, store_root=None, db_tables_prefix=None, _3dcart_private_key=None, _3dcart_access_token=None, _3dcartapi_api_key=None, amazon_sp_client_id=None, amazon_sp_client_secret=None, amazon_sp_aws_user_key_id=None, amazon_sp_aws_user_secret=None, amazon_sp_aws_region=None, amazon_sp_aws_role_arn=None, amazon_sp_refresh_token=None, amazon_sp_api_environment=None, amazon_access_token=None, amazon_seller_id=None, amazon_marketplaces_ids=None, amazon_secret_key=None, amazon_access_key_id=None, aspdotnetstorefront_api_user=None, aspdotnetstorefront_api_pass=None, bigcommerceapi_admin_account=None, bigcommerceapi_api_path=None, bigcommerceapi_api_key=None, bigcommerceapi_client_id=None, bigcommerceapi_access_token=None, bigcommerceapi_context=None, demandware_client_id=None, demandware_api_password=None, demandware_user_name=None, demandware_user_password=None, ebay_client_id=None, ebay_client_secret=None, ebay_runame=None, ebay_access_token=None, ebay_refresh_token=None, ebay_environment=None, ebay_site_id=None, ecwid_acess_token=None, ecwid_store_id=None, etsy_keystring=None, etsy_shared_secret=None, etsy_access_token=None, etsy_token_secret=None, etsy_client_id=None, etsy_refresh_token=None, neto_api_key=None, neto_api_username=None, shopify_api_key=None, shopify_api_password=None, shopify_shared_secret=None, shopify_access_token=None, shopware_access_key=None, shopware_api_key=None, shopware_api_secret=None, volusion_login=None, volusion_password=None, walmart_client_id=None, walmart_client_secret=None, walmart_environment=None, walmart_channel_type=None, squarespace_api_key=None, hybris_client_id=None, hybris_client_secret=None, hybris_username=None, hybris_password=None, hybris_websites=None, lightspeed_api_key=None, lightspeed_api_secret=None, commercehq_api_key=None, commercehq_api_password=None, wc_consumer_key=None, wc_consumer_secret=None, magento_consumer_key=None, magento_consumer_secret=None, magento_access_token=None, magento_token_secret=None, prestashop_webservice_key=None, wix_app_id=None, wix_app_secret_key=None, wix_refresh_token=None, mercado_libre_app_id=None, mercado_libre_app_secret_key=None, mercado_libre_refresh_token=None, zid_client_id=None, zid_client_secret=None, zid_access_token=None, zid_authorization=None, zid_refresh_token=None) -> web.Response:
    """account_config_update

    Update configs in the API2Cart database.

    :param new_store_key: Update store key
    :type new_store_key: str
    :param bridge_url: This parameter allows to set up store with custom bridge url (also you must use store_root parameter if a bridge folder is not in the root folder of the store)
    :type bridge_url: str
    :param store_root: Absolute path to the store root directory (used with \&quot;bridge_url\&quot; parameter)
    :type store_root: str
    :param db_tables_prefix: DB tables prefix
    :type db_tables_prefix: str
    :param _3dcart_private_key: 3DCart Private Key
    :type _3dcart_private_key: str
    :param _3dcart_access_token: 3DCart Token
    :type _3dcart_access_token: str
    :param _3dcartapi_api_key: 3DCart API Key
    :type _3dcartapi_api_key: str
    :param amazon_sp_client_id: Amazon SP API app client id
    :type amazon_sp_client_id: str
    :param amazon_sp_client_secret: Amazon SP API app client secret
    :type amazon_sp_client_secret: str
    :param amazon_sp_aws_user_key_id: Amazon AWS user access key ID
    :type amazon_sp_aws_user_key_id: str
    :param amazon_sp_aws_user_secret: Amazon AWS user secret access key
    :type amazon_sp_aws_user_secret: str
    :param amazon_sp_aws_region: Amazon AWS Region
    :type amazon_sp_aws_region: str
    :param amazon_sp_aws_role_arn: Amazon AWS Role ARN
    :type amazon_sp_aws_role_arn: str
    :param amazon_sp_refresh_token: Amazon SP API OAuth refresh token
    :type amazon_sp_refresh_token: str
    :param amazon_sp_api_environment: Amazon SP API environment
    :type amazon_sp_api_environment: str
    :param amazon_access_token: MWS Auth Token. Access token authorizing the app to access resources on behalf of a user
    :type amazon_access_token: str
    :param amazon_seller_id: Amazon Seller ID (Merchant token)
    :type amazon_seller_id: str
    :param amazon_marketplaces_ids: Amazon Marketplace IDs comma separated string
    :type amazon_marketplaces_ids: str
    :param amazon_secret_key: Amazon Secret Key
    :type amazon_secret_key: str
    :param amazon_access_key_id: Amazon Secret Key Id
    :type amazon_access_key_id: str
    :param aspdotnetstorefront_api_user: It&#39;s a AspDotNetStorefront account for which API is available
    :type aspdotnetstorefront_api_user: str
    :param aspdotnetstorefront_api_pass: AspDotNetStorefront API Password
    :type aspdotnetstorefront_api_pass: str
    :param bigcommerceapi_admin_account: It&#39;s a BigCommerce account for which API is enabled
    :type bigcommerceapi_admin_account: str
    :param bigcommerceapi_api_path: BigCommerce API URL
    :type bigcommerceapi_api_path: str
    :param bigcommerceapi_api_key: Bigcommerce API Key
    :type bigcommerceapi_api_key: str
    :param bigcommerceapi_client_id: Client ID of the requesting app
    :type bigcommerceapi_client_id: str
    :param bigcommerceapi_access_token: Access token authorizing the app to access resources on behalf of a user
    :type bigcommerceapi_access_token: str
    :param bigcommerceapi_context: API Path section unique to the store
    :type bigcommerceapi_context: str
    :param demandware_client_id: Demandware client id
    :type demandware_client_id: str
    :param demandware_api_password: Demandware api password
    :type demandware_api_password: str
    :param demandware_user_name: Demandware user name
    :type demandware_user_name: str
    :param demandware_user_password: Demandware user password
    :type demandware_user_password: str
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
    :param ecwid_acess_token: Access token authorizing the app to access resources on behalf of a user
    :type ecwid_acess_token: str
    :param ecwid_store_id: Store Id
    :type ecwid_store_id: str
    :param etsy_keystring: Etsy keystring
    :type etsy_keystring: str
    :param etsy_shared_secret: Etsy shared secret
    :type etsy_shared_secret: str
    :param etsy_access_token: Access token authorizing the app to access resources on behalf of a user
    :type etsy_access_token: str
    :param etsy_token_secret: Secret token authorizing the app to access resources on behalf of a user
    :type etsy_token_secret: str
    :param etsy_client_id: Etsy Client Id
    :type etsy_client_id: str
    :param etsy_refresh_token: Etsy Refresh token
    :type etsy_refresh_token: str
    :param neto_api_key: Neto API Key
    :type neto_api_key: str
    :param neto_api_username: Neto User Name
    :type neto_api_username: str
    :param shopify_api_key: Shopify API Key
    :type shopify_api_key: str
    :param shopify_api_password: Shopify API Password
    :type shopify_api_password: str
    :param shopify_shared_secret: Shared secret
    :type shopify_shared_secret: str
    :param shopify_access_token: Access token authorizing the app to access resources on behalf of a user
    :type shopify_access_token: str
    :param shopware_access_key: Shopware access key
    :type shopware_access_key: str
    :param shopware_api_key: Shopware api key
    :type shopware_api_key: str
    :param shopware_api_secret: Shopware client secret access key
    :type shopware_api_secret: str
    :param volusion_login: It&#39;s a Volusion account for which API is enabled
    :type volusion_login: str
    :param volusion_password: Volusion API Password
    :type volusion_password: str
    :param walmart_client_id: Walmart client ID
    :type walmart_client_id: str
    :param walmart_client_secret: Walmart client secret
    :type walmart_client_secret: str
    :param walmart_environment: Walmart environment
    :type walmart_environment: str
    :param walmart_channel_type: Walmart WM_CONSUMER.CHANNEL.TYPE header
    :type walmart_channel_type: str
    :param squarespace_api_key: Squarespace API Key
    :type squarespace_api_key: str
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
    :param lightspeed_api_key: LightSpeed api key
    :type lightspeed_api_key: str
    :param lightspeed_api_secret: LightSpeed api secret
    :type lightspeed_api_secret: str
    :param commercehq_api_key: CommerceHQ api key
    :type commercehq_api_key: str
    :param commercehq_api_password: CommerceHQ api password
    :type commercehq_api_password: str
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


async def account_failed_webhooks(request: web.Request, count=None, start=None, ids=None) -> web.Response:
    """account_failed_webhooks

    List webhooks that was not delivered to the callback.

    :param count: This parameter sets the entity amount that has to be retrieved. Max allowed count&#x3D;250
    :type count: int
    :param start: This parameter sets the number from which you want to get entities
    :type start: int
    :param ids: List of сomma-separated webhook ids
    :type ids: str

    """
    return web.Response(status=200)


async def account_supported_platforms(request: web.Request, ) -> web.Response:
    """account_supported_platforms

    Get list of supported platforms


    """
    return web.Response(status=200)
