# coding: utf-8

import pytest
import json
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


pytestmark = pytest.mark.asyncio

async def test_bridge_download(client):
    """Test case for bridge_download

    
    """
    params = [('whitelabel', False)]
    headers = { 
        'Accept': 'application/zip',
        'api_key': 'special-key',
        'store_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1.1/bridge.download.file',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_cart_bridge(client):
    """Test case for cart_bridge

    
    """
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1.1/cart.bridge.json',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_cart_catalog_price_rules_count(client):
    """Test case for cart_catalog_price_rules_count

    
    """
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
        'store_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1.1/cart.catalog_price_rules.count.json',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_cart_catalog_price_rules_list(client):
    """Test case for cart_catalog_price_rules_list

    
    """
    params = [('page_cursor', 'page_cursor_example'),
                    ('start', 0),
                    ('count', 10),
                    ('ids', 'ids_example'),
                    ('params', 'id,name,description'),
                    ('response_fields', 'response_fields_example'),
                    ('exclude', 'exclude_example')]
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
        'store_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1.1/cart.catalog_price_rules.list.json',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_cart_clear_cache(client):
    """Test case for cart_clear_cache

    
    """
    params = [('cache_type', 'cache_type_example')]
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
        'store_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1.1/cart.clear_cache.json',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_cart_config(client):
    """Test case for cart_config

    
    """
    params = [('params', 'store_name,store_url,db_prefix'),
                    ('exclude', 'exclude_example')]
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
        'store_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1.1/cart.config.json',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_cart_config_update(client):
    """Test case for cart_config_update

    
    """
    body = {"store_id":"store_id","db_tables_prefix":"db_tables_prefix","custom_fields":"{}"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'api_key': 'special-key',
        'store_key': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/v1.1/cart.config.update.json',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_cart_coupon_add(client):
    """Test case for cart_coupon_add

    
    """
    body = {"store_id":"store_id","codes":["codes","codes"],"action_scope":"order","usage_limit":6,"action_apply_to":"order_total","code":"code","usage_limit_per_customer":1,"action_type":"percent","date_end":"date_end","action_amount":0.8008281904610115,"action_condition_operator":"action_condition_operator","date_start":"now","action_condition_key":"action_condition_key","name":"name","action_condition_entity":"action_condition_entity","action_condition_value":"action_condition_value"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'api_key': 'special-key',
        'store_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1.1/cart.coupon.add.json',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_cart_coupon_condition_add(client):
    """Test case for cart_coupon_condition_add

    
    """
    params = [('store_id', 'store_id_example'),
                    ('coupon_id', 'coupon_id_example'),
                    ('target', 'coupon_prerequisite'),
                    ('entity', 'entity_example'),
                    ('key', 'key_example'),
                    ('operator', 'operator_example'),
                    ('value', 'value_example')]
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
        'store_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1.1/cart.coupon.condition.add.json',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_cart_coupon_count(client):
    """Test case for cart_coupon_count

    
    """
    params = [('store_id', 'store_id_example'),
                    ('date_start_from', 'date_start_from_example'),
                    ('date_start_to', 'date_start_to_example'),
                    ('date_end_from', 'date_end_from_example'),
                    ('date_end_to', 'date_end_to_example'),
                    ('avail', True)]
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
        'store_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1.1/cart.coupon.count.json',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_cart_coupon_delete(client):
    """Test case for cart_coupon_delete

    
    """
    params = [('id', 'id_example'),
                    ('store_id', 'store_id_example')]
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
        'store_key': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/v1.1/cart.coupon.delete.json',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_cart_coupon_list(client):
    """Test case for cart_coupon_list

    
    """
    params = [('page_cursor', 'page_cursor_example'),
                    ('start', 0),
                    ('count', 10),
                    ('coupons_ids', 'coupons_ids_example'),
                    ('store_id', 'store_id_example'),
                    ('date_start_from', 'date_start_from_example'),
                    ('date_start_to', 'date_start_to_example'),
                    ('date_end_from', 'date_end_from_example'),
                    ('date_end_to', 'date_end_to_example'),
                    ('avail', True),
                    ('lang_id', 'lang_id_example'),
                    ('params', 'id,code,name,description'),
                    ('response_fields', 'response_fields_example'),
                    ('exclude', 'exclude_example')]
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
        'store_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1.1/cart.coupon.list.json',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_cart_create(client):
    """Test case for cart_create

    
    """
    params = [('cart_id', 'cart_id_example'),
                    ('store_url', 'store_url_example'),
                    ('bridge_url', 'bridge_url_example'),
                    ('store_root', 'store_root_example'),
                    ('store_key', 'store_key_example'),
                    ('shared_secret', 'shared_secret_example'),
                    ('validate_version', False),
                    ('verify', True),
                    ('db_tables_prefix', 'db_tables_prefix_example'),
                    ('ftp_host', 'ftp_host_example'),
                    ('ftp_user', 'ftp_user_example'),
                    ('ftp_password', 'ftp_password_example'),
                    ('ftp_port', 56),
                    ('ftp_store_dir', 'ftp_store_dir_example'),
                    ('apiKey_3dcart', 'api_key_3dcart_example'),
                    ('AdminAccount', 'admin_account_example'),
                    ('ApiPath', 'api_path_example'),
                    ('ApiKey', 'api_key_example'),
                    ('client_id', 'client_id_example'),
                    ('accessToken', 'access_token_example'),
                    ('context', 'context_example'),
                    ('access_token2', 'access_token_example'),
                    ('apiKey_shopify', 'api_key_shopify_example'),
                    ('apiPassword', 'api_password_example'),
                    ('accessToken_shopify', 'access_token_shopify_example'),
                    ('apiKey', 'api_key_example'),
                    ('apiUsername', 'api_username_example'),
                    ('EncryptedPassword', 'encrypted_password_example'),
                    ('Login', 'login_example'),
                    ('apiUser_adnsf', 'api_user_adnsf_example'),
                    ('apiPass', 'api_pass_example'),
                    ('privateKey', 'private_key_example'),
                    ('appToken', 'app_token_example'),
                    ('etsy_keystring', 'etsy_keystring_example'),
                    ('etsy_shared_secret', 'etsy_shared_secret_example'),
                    ('tokenSecret', 'token_secret_example'),
                    ('etsy_client_id', 'etsy_client_id_example'),
                    ('etsy_refresh_token', 'etsy_refresh_token_example'),
                    ('ebay_client_id', 'ebay_client_id_example'),
                    ('ebay_client_secret', 'ebay_client_secret_example'),
                    ('ebay_runame', 'ebay_runame_example'),
                    ('ebay_access_token', 'ebay_access_token_example'),
                    ('ebay_refresh_token', 'ebay_refresh_token_example'),
                    ('ebay_environment', 'production'),
                    ('ebay_site_id', 0),
                    ('dw_client_id', 'dw_client_id_example'),
                    ('dw_api_pass', 'dw_api_pass_example'),
                    ('demandware_user_name', 'demandware_user_name_example'),
                    ('demandware_user_password', 'demandware_user_password_example'),
                    ('store_id', 'store_id_example'),
                    ('seller_id', 'seller_id_example'),
                    ('amazon_secret_key', 'amazon_secret_key_example'),
                    ('amazon_access_key_id', 'amazon_access_key_id_example'),
                    ('marketplaces_ids', 'marketplaces_ids_example'),
                    ('environment', 'production'),
                    ('hybris_client_id', 'hybris_client_id_example'),
                    ('hybris_client_secret', 'hybris_client_secret_example'),
                    ('hybris_username', 'hybris_username_example'),
                    ('hybris_password', 'hybris_password_example'),
                    ('hybris_websites', ['hybris_websites_example']),
                    ('walmart_client_id', 'walmart_client_id_example'),
                    ('walmart_client_secret', 'walmart_client_secret_example'),
                    ('walmart_environment', 'production'),
                    ('walmart_channel_type', 'walmart_channel_type_example'),
                    ('lightspeed_api_key', 'lightspeed_api_key_example'),
                    ('lightspeed_api_secret', 'lightspeed_api_secret_example'),
                    ('shopware_access_key', 'shopware_access_key_example'),
                    ('shopware_api_key', 'shopware_api_key_example'),
                    ('shopware_api_secret', 'shopware_api_secret_example'),
                    ('commercehq_api_key', 'commercehq_api_key_example'),
                    ('commercehq_api_password', 'commercehq_api_password_example'),
                    ('3dcart_private_key', '_3dcart_private_key_example'),
                    ('3dcart_access_token', '_3dcart_access_token_example'),
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
    }
    response = await client.request(
        method='POST',
        path='/v1.1/cart.create.json',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_cart_delete(client):
    """Test case for cart_delete

    
    """
    params = [('delete_bridge', True)]
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
        'store_key': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/v1.1/cart.delete.json',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_cart_disconnect(client):
    """Test case for cart_disconnect

    
    """
    params = [('delete_bridge', False)]
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
        'store_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1.1/cart.disconnect.json',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_cart_giftcard_add(client):
    """Test case for cart_giftcard_add

    
    """
    params = [('amount', 3.4),
                    ('code', 'code_example'),
                    ('owner_email', 'owner_email_example'),
                    ('recipient_email', 'recipient_email_example')]
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
        'store_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1.1/cart.giftcard.add.json',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_cart_giftcard_count(client):
    """Test case for cart_giftcard_count

    
    """
    params = [('store_id', 'store_id_example')]
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
        'store_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1.1/cart.giftcard.count.json',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_cart_giftcard_list(client):
    """Test case for cart_giftcard_list

    
    """
    params = [('page_cursor', 'page_cursor_example'),
                    ('start', 0),
                    ('count', 10),
                    ('store_id', 'store_id_example'),
                    ('params', 'id,code,name'),
                    ('response_fields', 'response_fields_example'),
                    ('exclude', 'exclude_example')]
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
        'store_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1.1/cart.giftcard.list.json',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_cart_info(client):
    """Test case for cart_info

    
    """
    params = [('params', 'store_name,store_url,db_prefix'),
                    ('response_fields', 'response_fields_example'),
                    ('exclude', 'exclude_example'),
                    ('store_id', 'store_id_example')]
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
        'store_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1.1/cart.info.json',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_cart_list(client):
    """Test case for cart_list

    
    """
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1.1/cart.list.json',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_cart_meta_data_list(client):
    """Test case for cart_meta_data_list

    
    """
    params = [('entity_id', 'entity_id_example'),
                    ('entity', 'product'),
                    ('store_id', 'store_id_example'),
                    ('lang_id', 'lang_id_example'),
                    ('key', 'key_example'),
                    ('count', 10),
                    ('page_cursor', 'page_cursor_example'),
                    ('params', 'key,value'),
                    ('response_fields', 'response_fields_example'),
                    ('exclude', 'exclude_example')]
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
        'store_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1.1/cart.meta_data.list.json',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_cart_meta_data_set(client):
    """Test case for cart_meta_data_set

    
    """
    params = [('entity_id', 'entity_id_example'),
                    ('entity', 'product'),
                    ('store_id', 'store_id_example'),
                    ('lang_id', 'lang_id_example'),
                    ('key', 'key_example'),
                    ('value', 'value_example'),
                    ('namespace', 'namespace_example')]
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
        'store_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1.1/cart.meta_data.set.json',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_cart_meta_data_unset(client):
    """Test case for cart_meta_data_unset

    
    """
    params = [('entity_id', 'entity_id_example'),
                    ('entity', 'product'),
                    ('store_id', 'store_id_example'),
                    ('key', 'key_example'),
                    ('id', 'id_example')]
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
        'store_key': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/v1.1/cart.meta_data.unset.json',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_cart_methods(client):
    """Test case for cart_methods

    
    """
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
        'store_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1.1/cart.methods.json',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_cart_plugin_list(client):
    """Test case for cart_plugin_list

    
    """
    params = [('store_key', 'store_key_example'),
                    ('store_id', 'store_id_example'),
                    ('start', 0),
                    ('count', 10)]
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
        'store_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1.1/cart.plugin.list.json',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_cart_script_add(client):
    """Test case for cart_script_add

    
    """
    params = [('name', 'name_example'),
                    ('description', 'description_example'),
                    ('html', 'html_example'),
                    ('src', 'src_example'),
                    ('load_method', 'load_method_example'),
                    ('scope', 'storefront'),
                    ('store_id', 'store_id_example')]
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
        'store_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1.1/cart.script.add.json',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_cart_script_delete(client):
    """Test case for cart_script_delete

    
    """
    params = [('id', 'id_example'),
                    ('store_id', 'store_id_example')]
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
        'store_key': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/v1.1/cart.script.delete.json',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_cart_script_list(client):
    """Test case for cart_script_list

    
    """
    params = [('page_cursor', 'page_cursor_example'),
                    ('start', 0),
                    ('count', 10),
                    ('created_from', 'created_from_example'),
                    ('created_to', 'created_to_example'),
                    ('modified_from', 'modified_from_example'),
                    ('modified_to', 'modified_to_example'),
                    ('script_ids', 'script_ids_example'),
                    ('store_id', 'store_id_example'),
                    ('params', 'id,name,description'),
                    ('response_fields', 'response_fields_example'),
                    ('exclude', 'exclude_example')]
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
        'store_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1.1/cart.script.list.json',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_cart_shipping_zones_list(client):
    """Test case for cart_shipping_zones_list

    
    """
    params = [('store_id', 'store_id_example'),
                    ('start', 0),
                    ('count', 10),
                    ('params', 'id,name,enabled'),
                    ('response_fields', 'response_fields_example'),
                    ('exclude', 'exclude_example')]
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
        'store_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1.1/cart.shipping_zones.list.json',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_cart_validate(client):
    """Test case for cart_validate

    
    """
    params = [('validate_version', False)]
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
        'store_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1.1/cart.validate.json',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

