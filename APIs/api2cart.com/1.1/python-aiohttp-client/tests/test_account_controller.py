# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.account_cart_add import AccountCartAdd
from openapi_server.models.account_cart_add200_response import AccountCartAdd200Response
from openapi_server.models.account_cart_list200_response import AccountCartList200Response
from openapi_server.models.account_config_update200_response import AccountConfigUpdate200Response
from openapi_server.models.account_failed_webhooks200_response import AccountFailedWebhooks200Response
from openapi_server.models.account_supported_platforms200_response import AccountSupportedPlatforms200Response


pytestmark = pytest.mark.asyncio

async def test_account_cart_add(client):
    """Test case for account_cart_add

    
    """
    body = {"db_tables_prefix":"db_tables_prefix","zid_client_id":1,"bigcommerceapi_access_token":"bigcommerceapi_access_token","prestashop_webservice_key":"prestashop_webservice_key","squarespace_api_key":"squarespace_api_key","mercado_libre_app_id":"mercado_libre_app_id","ftp_user":"ftp_user","walmart_client_id":"walmart_client_id","bigcommerceapi_context":"bigcommerceapi_context","shopware_api_key":"shopware_api_key","3dcart_private_key":"3dcart_private_key","wix_app_secret_key":"wix_app_secret_key","amazon_seller_id":"amazon_seller_id","hybris_username":"hybris_username","ebay_access_token":"ebay_access_token","shopify_access_token":"shopify_access_token","validate_version":False,"shopify_shared_secret":"shopify_shared_secret","etsy_client_id":"etsy_client_id","ebay_client_id":"ebay_client_id","amazon_sp_client_id":"amazon_sp_client_id","ebay_environment":"production","amazon_marketplaces_ids":"amazon_marketplaces_ids","ecwid_acess_token":"ecwid_acess_token","hybris_websites":[{"uid":"uid","storeIds":["storeIds","storeIds"],"url":"url"},{"uid":"uid","storeIds":["storeIds","storeIds"],"url":"url"}],"hybris_client_id":"hybris_client_id","aspdotnetstorefront_api_user":"aspdotnetstorefront_api_user","amazon_access_key_id":"amazon_access_key_id","ecwid_store_id":"ecwid_store_id","verify":True,"amazon_sp_aws_user_secret":"amazon_sp_aws_user_secret","walmart_environment":"production","demandware_user_password":"demandware_user_password","wc_consumer_key":"wc_consumer_key","amazon_sp_client_secret":"amazon_sp_client_secret","wix_app_id":"wix_app_id","ebay_client_secret":"ebay_client_secret","ebay_runame":"ebay_runame","mercado_libre_app_secret_key":"mercado_libre_app_secret_key","wix_refresh_token":"wix_refresh_token","magento_consumer_secret":"magento_consumer_secret","store_root":"store_root","ftp_store_dir":"ftp_store_dir","amazon_sp_aws_role_arn":"amazon_sp_aws_role_arn","zid_access_token":"zid_access_token","amazon_sp_aws_region":"eu-west-1","bigcommerceapi_api_path":"bigcommerceapi_api_path","lightspeed_api_key":"lightspeed_api_key","volusion_login":"volusion_login","3dcartapi_api_key":"3dcartapi_api_key","zid_refresh_token":"zid_refresh_token","etsy_access_token":"etsy_access_token","3dcart_access_token":"3dcart_access_token","neto_api_key":"neto_api_key","cart_id":"3DCart","bigcommerceapi_admin_account":"bigcommerceapi_admin_account","demandware_user_name":"demandware_user_name","aspdotnetstorefront_api_pass":"aspdotnetstorefront_api_pass","magento_access_token":"magento_access_token","wc_consumer_secret":"wc_consumer_secret","etsy_refresh_token":"etsy_refresh_token","ftp_password":"ftp_password","ftp_port":6,"magento_token_secret":"magento_token_secret","amazon_access_token":"amazon_access_token","etsy_shared_secret":"etsy_shared_secret","lightspeed_api_secret":"lightspeed_api_secret","bigcommerceapi_api_key":"bigcommerceapi_api_key","amazon_secret_key":"amazon_secret_key","hybris_password":"hybris_password","shopify_api_key":"shopify_api_key","neto_api_username":"neto_api_username","hybris_client_secret":"hybris_client_secret","etsy_token_secret":"etsy_token_secret","amazon_sp_aws_user_key_id":"amazon_sp_aws_user_key_id","store_url":"store_url","bigcommerceapi_client_id":"bigcommerceapi_client_id","commercehq_api_key":"commercehq_api_key","etsy_keystring":"etsy_keystring","bridge_url":"bridge_url","shopware_access_key":"shopware_access_key","store_key":"store_key","amazon_sp_api_environment":"production","ebay_site_id":0,"shopify_api_password":"shopify_api_password","shopware_api_secret":"shopware_api_secret","ebay_refresh_token":"ebay_refresh_token","magento_consumer_key":"magento_consumer_key","walmart_client_secret":"walmart_client_secret","amazon_sp_refresh_token":"amazon_sp_refresh_token","commercehq_api_password":"commercehq_api_password","mercado_libre_refresh_token":"mercado_libre_refresh_token","ftp_host":"ftp_host","zid_client_secret":"zid_client_secret","walmart_channel_type":"walmart_channel_type","demandware_api_password":"demandware_api_password","volusion_password":"volusion_password","zid_authorization":"zid_authorization","demandware_client_id":"demandware_client_id"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1.1/account.cart.add.json',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_account_cart_list(client):
    """Test case for account_cart_list

    
    """
    params = [('params', 'force_all'),
                    ('exclude', 'exclude_example'),
                    ('request_from_date', 'request_from_date_example'),
                    ('request_to_date', 'request_to_date_example'),
                    ('store_url', 'store_url_example'),
                    ('store_key', 'store_key_example')]
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1.1/account.cart.list.json',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_account_config_update(client):
    """Test case for account_config_update

    
    """
    params = [('new_store_key', 'new_store_key_example'),
                    ('bridge_url', 'bridge_url_example'),
                    ('store_root', 'store_root_example'),
                    ('db_tables_prefix', 'db_tables_prefix_example'),
                    ('3dcart_private_key', '_3dcart_private_key_example'),
                    ('3dcart_access_token', '_3dcart_access_token_example'),
                    ('3dcartapi_api_key', '_3dcartapi_api_key_example'),
                    ('amazon_sp_client_id', 'amazon_sp_client_id_example'),
                    ('amazon_sp_client_secret', 'amazon_sp_client_secret_example'),
                    ('amazon_sp_aws_user_key_id', 'amazon_sp_aws_user_key_id_example'),
                    ('amazon_sp_aws_user_secret', 'amazon_sp_aws_user_secret_example'),
                    ('amazon_sp_aws_region', 'amazon_sp_aws_region_example'),
                    ('amazon_sp_aws_role_arn', 'amazon_sp_aws_role_arn_example'),
                    ('amazon_sp_refresh_token', 'amazon_sp_refresh_token_example'),
                    ('amazon_sp_api_environment', 'production'),
                    ('amazon_access_token', 'amazon_access_token_example'),
                    ('amazon_seller_id', 'amazon_seller_id_example'),
                    ('amazon_marketplaces_ids', 'amazon_marketplaces_ids_example'),
                    ('amazon_secret_key', 'amazon_secret_key_example'),
                    ('amazon_access_key_id', 'amazon_access_key_id_example'),
                    ('aspdotnetstorefront_api_user', 'aspdotnetstorefront_api_user_example'),
                    ('aspdotnetstorefront_api_pass', 'aspdotnetstorefront_api_pass_example'),
                    ('bigcommerceapi_admin_account', 'bigcommerceapi_admin_account_example'),
                    ('bigcommerceapi_api_path', 'bigcommerceapi_api_path_example'),
                    ('bigcommerceapi_api_key', 'bigcommerceapi_api_key_example'),
                    ('bigcommerceapi_client_id', 'bigcommerceapi_client_id_example'),
                    ('bigcommerceapi_access_token', 'bigcommerceapi_access_token_example'),
                    ('bigcommerceapi_context', 'bigcommerceapi_context_example'),
                    ('demandware_client_id', 'demandware_client_id_example'),
                    ('demandware_api_password', 'demandware_api_password_example'),
                    ('demandware_user_name', 'demandware_user_name_example'),
                    ('demandware_user_password', 'demandware_user_password_example'),
                    ('ebay_client_id', 'ebay_client_id_example'),
                    ('ebay_client_secret', 'ebay_client_secret_example'),
                    ('ebay_runame', 'ebay_runame_example'),
                    ('ebay_access_token', 'ebay_access_token_example'),
                    ('ebay_refresh_token', 'ebay_refresh_token_example'),
                    ('ebay_environment', 'ebay_environment_example'),
                    ('ebay_site_id', 0),
                    ('ecwid_acess_token', 'ecwid_acess_token_example'),
                    ('ecwid_store_id', 'ecwid_store_id_example'),
                    ('etsy_keystring', 'etsy_keystring_example'),
                    ('etsy_shared_secret', 'etsy_shared_secret_example'),
                    ('etsy_access_token', 'etsy_access_token_example'),
                    ('etsy_token_secret', 'etsy_token_secret_example'),
                    ('etsy_client_id', 'etsy_client_id_example'),
                    ('etsy_refresh_token', 'etsy_refresh_token_example'),
                    ('neto_api_key', 'neto_api_key_example'),
                    ('neto_api_username', 'neto_api_username_example'),
                    ('shopify_api_key', 'shopify_api_key_example'),
                    ('shopify_api_password', 'shopify_api_password_example'),
                    ('shopify_shared_secret', 'shopify_shared_secret_example'),
                    ('shopify_access_token', 'shopify_access_token_example'),
                    ('shopware_access_key', 'shopware_access_key_example'),
                    ('shopware_api_key', 'shopware_api_key_example'),
                    ('shopware_api_secret', 'shopware_api_secret_example'),
                    ('volusion_login', 'volusion_login_example'),
                    ('volusion_password', 'volusion_password_example'),
                    ('walmart_client_id', 'walmart_client_id_example'),
                    ('walmart_client_secret', 'walmart_client_secret_example'),
                    ('walmart_environment', 'production'),
                    ('walmart_channel_type', 'walmart_channel_type_example'),
                    ('squarespace_api_key', 'squarespace_api_key_example'),
                    ('hybris_client_id', 'hybris_client_id_example'),
                    ('hybris_client_secret', 'hybris_client_secret_example'),
                    ('hybris_username', 'hybris_username_example'),
                    ('hybris_password', 'hybris_password_example'),
                    ('hybris_websites', ['hybris_websites_example']),
                    ('lightspeed_api_key', 'lightspeed_api_key_example'),
                    ('lightspeed_api_secret', 'lightspeed_api_secret_example'),
                    ('commercehq_api_key', 'commercehq_api_key_example'),
                    ('commercehq_api_password', 'commercehq_api_password_example'),
                    ('wc_consumer_key', 'wc_consumer_key_example'),
                    ('wc_consumer_secret', 'wc_consumer_secret_example'),
                    ('magento_consumer_key', 'magento_consumer_key_example'),
                    ('magento_consumer_secret', 'magento_consumer_secret_example'),
                    ('magento_access_token', 'magento_access_token_example'),
                    ('magento_token_secret', 'magento_token_secret_example'),
                    ('prestashop_webservice_key', 'prestashop_webservice_key_example'),
                    ('wix_app_id', 'wix_app_id_example'),
                    ('wix_app_secret_key', 'wix_app_secret_key_example'),
                    ('wix_refresh_token', 'wix_refresh_token_example'),
                    ('mercado_libre_app_id', 'mercado_libre_app_id_example'),
                    ('mercado_libre_app_secret_key', 'mercado_libre_app_secret_key_example'),
                    ('mercado_libre_refresh_token', 'mercado_libre_refresh_token_example'),
                    ('zid_client_id', 56),
                    ('zid_client_secret', 'zid_client_secret_example'),
                    ('zid_access_token', 'zid_access_token_example'),
                    ('zid_authorization', 'zid_authorization_example'),
                    ('zid_refresh_token', 'zid_refresh_token_example')]
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
        'store_key': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/v1.1/account.config.update.json',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_account_failed_webhooks(client):
    """Test case for account_failed_webhooks

    
    """
    params = [('count', 10),
                    ('start', 0),
                    ('ids', 'ids_example')]
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1.1/account.failed_webhooks.json',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_account_supported_platforms(client):
    """Test case for account_supported_platforms

    
    """
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1.1/account.supported_platforms.json',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

