# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.account_config_update200_response import AccountConfigUpdate200Response
from openapi_server.models.attribute_delete200_response import AttributeDelete200Response
from openapi_server.models.cart_config_update200_response import CartConfigUpdate200Response
from openapi_server.models.cart_validate200_response import CartValidate200Response
from openapi_server.models.model_response_product_attribute_list import ModelResponseProductAttributeList
from openapi_server.models.model_response_product_child_item_list import ModelResponseProductChildItemList
from openapi_server.models.model_response_product_list import ModelResponseProductList
from openapi_server.models.product_add import ProductAdd
from openapi_server.models.product_add200_response import ProductAdd200Response
from openapi_server.models.product_attribute_value_set200_response import ProductAttributeValueSet200Response
from openapi_server.models.product_attribute_value_unset200_response import ProductAttributeValueUnset200Response
from openapi_server.models.product_brand_list200_response import ProductBrandList200Response
from openapi_server.models.product_child_item_find200_response import ProductChildItemFind200Response
from openapi_server.models.product_child_item_info200_response import ProductChildItemInfo200Response
from openapi_server.models.product_count200_response import ProductCount200Response
from openapi_server.models.product_currency_add200_response import ProductCurrencyAdd200Response
from openapi_server.models.product_currency_list200_response import ProductCurrencyList200Response
from openapi_server.models.product_delete200_response import ProductDelete200Response
from openapi_server.models.product_find200_response import ProductFind200Response
from openapi_server.models.product_image_add import ProductImageAdd
from openapi_server.models.product_image_add200_response import ProductImageAdd200Response
from openapi_server.models.product_image_update200_response import ProductImageUpdate200Response
from openapi_server.models.product_info200_response import ProductInfo200Response
from openapi_server.models.product_manufacturer_add200_response import ProductManufacturerAdd200Response
from openapi_server.models.product_option_add200_response import ProductOptionAdd200Response
from openapi_server.models.product_option_assign200_response import ProductOptionAssign200Response
from openapi_server.models.product_option_list200_response import ProductOptionList200Response
from openapi_server.models.product_option_value_add200_response import ProductOptionValueAdd200Response
from openapi_server.models.product_option_value_assign200_response import ProductOptionValueAssign200Response
from openapi_server.models.product_price_add import ProductPriceAdd
from openapi_server.models.product_price_update import ProductPriceUpdate
from openapi_server.models.product_review_list200_response import ProductReviewList200Response
from openapi_server.models.product_tax_add import ProductTaxAdd
from openapi_server.models.product_tax_add200_response import ProductTaxAdd200Response
from openapi_server.models.product_update import ProductUpdate
from openapi_server.models.product_variant_add import ProductVariantAdd
from openapi_server.models.product_variant_add200_response import ProductVariantAdd200Response
from openapi_server.models.product_variant_count200_response import ProductVariantCount200Response
from openapi_server.models.product_variant_image_add import ProductVariantImageAdd
from openapi_server.models.product_variant_list200_response import ProductVariantList200Response
from openapi_server.models.product_variant_price_add import ProductVariantPriceAdd
from openapi_server.models.product_variant_price_update import ProductVariantPriceUpdate
from openapi_server.models.product_variant_update import ProductVariantUpdate


pytestmark = pytest.mark.asyncio

async def test_product_add(client):
    """Test case for product_add

    
    """
    body = {"ordered_count":2,"seo_url":"seo_url","paypal_email":"paypal_email","sprice_create":"sprice_create","type":"simple","listing_duration":"listing_duration","product_class":"product_class","image_name":"image_name","payment_methods":["payment_methods","payment_methods"],"clear_cache":True,"marketplace_item_properties":"false","price":7.061401241503109,"viewed_count":1,"wholesale_price":6.84685269835264,"model":"model","sku":"sku","barcode":"barcode","height":1.4658129805029452,"shipping_template_id":2,"visible":"visible","meta_title":"meta_title","taxable":True,"image_url":"image_url","old_price":5.637376656633329,"country_of_origin":"country_of_origin","stores_ids":"0","listing_type":"FixedPrice","upc":"upc","weight":1.4894159098541704,"brand_name":"brand_name","mpn":"mpn","avail_from":"avail_from","tags":"tags","attribute_set_name":"Default","meta_description":"meta_description","condition":"condition","weight_unit":"weight_unit","name":"name","files":[{"name":"name","url":"url"},{"name":"name","url":"url"}],"sprice_expire":"sprice_expire","harmonized_system_code":"harmonized_system_code","best_offer":["best_offer","best_offer"],"status":"status","short_description":"short_description","downloadable":False,"isbn":"isbn","shipping_details":[{"shipping_service":"shipping_service","shipping_cost":3.616076749251911,"shipping_type":"shipping_type"},{"shipping_service":"shipping_service","shipping_cost":3.616076749251911,"shipping_type":"shipping_type"}],"created_at":"created_at","description":"description","return_accepted":True,"seller_profiles":{"payment_profile_id":"payment_profile_id","return_profile_id":"return_profile_id","shipping_profile_id":"shipping_profile_id"},"tier_prices":[{"quantity":1.2315135367772556,"price":7.386281948385884},{"quantity":1.2315135367772556,"price":7.386281948385884}],"meta_keywords":"meta_keywords","search_keywords":"search_keywords","manufacturer":"manufacturer","ean":"ean","category_id":"category_id","package_details":["package_details","package_details"],"attribute_name":"attribute_name","sprice_modified":"sprice_modified","available_for_sale":True,"cost_price":0.8008281904610115,"store_id":"store_id","manage_stock":True,"gtin":"gtin","quantity":9.301444243932576,"length":5.962133916683182,"tax_class_id":"tax_class_id","lang_id":"lang_id","url":"url","group_prices":[{"group_id":"group_id","price":6.027456183070403},{"group_id":"group_id","price":6.027456183070403}],"sales_tax":["sales_tax","sales_tax"],"special_price":4.145608029883936,"width":7.457744773683766,"backorder_status":"backorder_status","categories_ids":"categories_ids","available_for_view":True,"specifics":["specifics","specifics"],"warehouse_id":"warehouse_id"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'api_key': 'special-key',
        'store_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1.1/product.add.json',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_product_attribute_list(client):
    """Test case for product_attribute_list

    
    """
    params = [('product_id', 'product_id_example'),
                    ('attribute_id', 'attribute_id_example'),
                    ('variant_id', 'variant_id_example'),
                    ('page_cursor', 'page_cursor_example'),
                    ('start', 0),
                    ('count', 10),
                    ('attribute_group_id', 'attribute_group_id_example'),
                    ('set_name', 'set_name_example'),
                    ('lang_id', 'lang_id_example'),
                    ('store_id', 'store_id_example'),
                    ('sort_by', 'attribute_id'),
                    ('sort_direction', 'asc'),
                    ('params', 'attribute_id,name'),
                    ('response_fields', 'response_fields_example'),
                    ('exclude', 'exclude_example')]
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
        'store_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1.1/product.attribute.list.json',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_product_attribute_value_set(client):
    """Test case for product_attribute_value_set

    
    """
    params = [('product_id', 'product_id_example'),
                    ('attribute_id', 'attribute_id_example'),
                    ('attribute_group_id', 'attribute_group_id_example'),
                    ('attribute_name', 'attribute_name_example'),
                    ('value', 'value_example'),
                    ('value_id', 56),
                    ('lang_id', 'lang_id_example'),
                    ('store_id', 'store_id_example')]
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
        'store_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1.1/product.attribute.value.set.json',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_product_attribute_value_unset(client):
    """Test case for product_attribute_value_unset

    
    """
    params = [('product_id', 'product_id_example'),
                    ('attribute_id', 'attribute_id_example'),
                    ('store_id', 'store_id_example'),
                    ('include_default', False),
                    ('reindex', True),
                    ('clear_cache', True)]
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
        'store_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1.1/product.attribute.value.unset.json',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_product_brand_list(client):
    """Test case for product_brand_list

    
    """
    params = [('start', 0),
                    ('count', 10),
                    ('params', 'id,name,short_description,active,url'),
                    ('brand_ids', 'brand_ids_example'),
                    ('exclude', 'exclude_example'),
                    ('store_id', 'store_id_example'),
                    ('lang_id', 'lang_id_example'),
                    ('created_from', 'created_from_example'),
                    ('created_to', 'created_to_example'),
                    ('modified_from', 'modified_from_example'),
                    ('modified_to', 'modified_to_example'),
                    ('response_fields', 'response_fields_example')]
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
        'store_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1.1/product.brand.list.json',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_product_child_item_find(client):
    """Test case for product_child_item_find

    
    """
    params = [('find_value', 'find_value_example'),
                    ('find_where', 'name'),
                    ('find_params', 'whole_words'),
                    ('store_id', 'store_id_example')]
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
        'store_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1.1/product.child_item.find.json',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_product_child_item_info(client):
    """Test case for product_child_item_info

    
    """
    params = [('params', 'force_all'),
                    ('response_fields', 'response_fields_example'),
                    ('exclude', 'exclude_example'),
                    ('product_id', 'product_id_example'),
                    ('id', 'id_example'),
                    ('store_id', 'store_id_example'),
                    ('lang_id', 'lang_id_example'),
                    ('currency_id', 'currency_id_example')]
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
        'store_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1.1/product.child_item.info.json',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_product_child_item_list(client):
    """Test case for product_child_item_list

    
    """
    params = [('page_cursor', 'page_cursor_example'),
                    ('start', 0),
                    ('count', 10),
                    ('params', 'force_all'),
                    ('response_fields', 'response_fields_example'),
                    ('exclude', 'exclude_example'),
                    ('created_from', 'created_from_example'),
                    ('created_to', 'created_to_example'),
                    ('modified_from', 'modified_from_example'),
                    ('modified_to', 'modified_to_example'),
                    ('product_id', 'product_id_example'),
                    ('product_ids', 'product_ids_example'),
                    ('store_id', 'store_id_example'),
                    ('lang_id', 'lang_id_example'),
                    ('currency_id', 'currency_id_example'),
                    ('avail_sale', True),
                    ('report_request_id', 'report_request_id_example'),
                    ('disable_report_cache', False)]
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
        'store_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1.1/product.child_item.list.json',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_product_count(client):
    """Test case for product_count

    
    """
    params = [('category_id', 'category_id_example'),
                    ('created_from', 'created_from_example'),
                    ('created_to', 'created_to_example'),
                    ('modified_from', 'modified_from_example'),
                    ('modified_to', 'modified_to_example'),
                    ('avail_view', True),
                    ('avail_sale', True),
                    ('store_id', 'store_id_example'),
                    ('lang_id', 'lang_id_example'),
                    ('product_ids', 'product_ids_example'),
                    ('report_request_id', 'report_request_id_example'),
                    ('disable_report_cache', False),
                    ('brand_name', 'brand_name_example'),
                    ('product_attributes', ['product_attributes_example']),
                    ('status', 'status_example'),
                    ('type', 'type_example')]
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
        'store_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1.1/product.count.json',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_product_currency_add(client):
    """Test case for product_currency_add

    
    """
    params = [('iso3', 'iso3_example'),
                    ('rate', 3.4),
                    ('name', 'name_example'),
                    ('avail', True),
                    ('symbol_left', 'symbol_left_example'),
                    ('symbol_right', 'symbol_right_example'),
                    ('default', False)]
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
        'store_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1.1/product.currency.add.json',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_product_currency_list(client):
    """Test case for product_currency_list

    
    """
    params = [('start', 0),
                    ('count', 10),
                    ('params', 'name,iso3,default,avail'),
                    ('page_cursor', 'page_cursor_example'),
                    ('exclude', 'exclude_example'),
                    ('response_fields', 'response_fields_example'),
                    ('default', True),
                    ('avail', True)]
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
        'store_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1.1/product.currency.list.json',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_product_delete(client):
    """Test case for product_delete

    
    """
    params = [('id', 'id_example')]
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
        'store_key': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/v1.1/product.delete.json',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_product_fields(client):
    """Test case for product_fields

    
    """
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
        'store_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1.1/product.fields.json',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_product_find(client):
    """Test case for product_find

    
    """
    params = [('find_value', 'find_value_example'),
                    ('find_where', 'name'),
                    ('find_params', 'whole_words'),
                    ('find_what', 'product'),
                    ('lang_id', 'lang_id_example'),
                    ('store_id', 'store_id_example')]
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
        'store_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1.1/product.find.json',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_product_image_add(client):
    """Test case for product_image_add

    
    """
    body = {"store_id":"store_id","image_name":"image_name","mime":"mime","product_id":"product_id","lang_id":"lang_id","variant_ids":"variant_ids","label":"label","position":0,"product_variant_id":6,"type":"small","content":"content","url":"url"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'api_key': 'special-key',
        'store_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1.1/product.image.add.json',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_product_image_delete(client):
    """Test case for product_image_delete

    
    """
    params = [('product_id', 'product_id_example'),
                    ('id', 'id_example'),
                    ('store_id', 'store_id_example')]
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
        'store_key': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/v1.1/product.image.delete.json',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_product_image_update(client):
    """Test case for product_image_update

    
    """
    params = [('product_id', 'product_id_example'),
                    ('variant_ids', 'variant_ids_example'),
                    ('image_name', 'image_name_example'),
                    ('type', 'additional'),
                    ('label', 'label_example'),
                    ('position', 56),
                    ('id', 'id_example'),
                    ('store_id', 'store_id_example'),
                    ('lang_id', 'lang_id_example'),
                    ('hidden', True)]
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
        'store_key': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/v1.1/product.image.update.json',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_product_info(client):
    """Test case for product_info

    
    """
    params = [('id', 'id_example'),
                    ('params', 'id,name,description,price,categories_ids'),
                    ('response_fields', 'response_fields_example'),
                    ('exclude', 'exclude_example'),
                    ('store_id', 'store_id_example'),
                    ('lang_id', 'lang_id_example'),
                    ('currency_id', 'currency_id_example'),
                    ('report_request_id', 'report_request_id_example'),
                    ('disable_report_cache', False)]
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
        'store_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1.1/product.info.json',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_product_list(client):
    """Test case for product_list

    
    """
    params = [('page_cursor', 'page_cursor_example'),
                    ('start', 0),
                    ('count', 10),
                    ('params', 'id,name,description,price,categories_ids'),
                    ('response_fields', 'response_fields_example'),
                    ('exclude', 'exclude_example'),
                    ('category_id', 'category_id_example'),
                    ('created_from', 'created_from_example'),
                    ('created_to', 'created_to_example'),
                    ('modified_from', 'modified_from_example'),
                    ('modified_to', 'modified_to_example'),
                    ('avail_view', True),
                    ('avail_sale', True),
                    ('store_id', 'store_id_example'),
                    ('lang_id', 'lang_id_example'),
                    ('currency_id', 'currency_id_example'),
                    ('product_ids', 'product_ids_example'),
                    ('since_id', 56),
                    ('report_request_id', 'report_request_id_example'),
                    ('disable_report_cache', False),
                    ('sort_by', 'id'),
                    ('sort_direction', 'asc'),
                    ('sku', 'sku_example'),
                    ('disable_cache', False),
                    ('brand_name', 'brand_name_example'),
                    ('product_attributes', ['product_attributes_example']),
                    ('status', 'status_example'),
                    ('type', 'type_example')]
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
        'store_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1.1/product.list.json',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_product_manufacturer_add(client):
    """Test case for product_manufacturer_add

    
    """
    params = [('product_id', 'product_id_example'),
                    ('manufacturer', 'manufacturer_example')]
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
        'store_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1.1/product.manufacturer.add.json',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_product_option_add(client):
    """Test case for product_option_add

    
    """
    params = [('name', 'name_example'),
                    ('type', 'type_example'),
                    ('product_id', 'product_id_example'),
                    ('default_option_value', 'default_option_value_example'),
                    ('option_values', 'option_values_example'),
                    ('description', 'description_example'),
                    ('avail', True),
                    ('sort_order', 0),
                    ('required', False),
                    ('clear_cache', True)]
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
        'store_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1.1/product.option.add.json',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_product_option_assign(client):
    """Test case for product_option_assign

    
    """
    params = [('product_id', 'product_id_example'),
                    ('option_id', 'option_id_example'),
                    ('required', False),
                    ('sort_order', 0),
                    ('option_values', 'option_values_example'),
                    ('clear_cache', True)]
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
        'store_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1.1/product.option.assign.json',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_product_option_list(client):
    """Test case for product_option_list

    
    """
    params = [('start', 0),
                    ('count', 10),
                    ('params', 'id,name,description'),
                    ('exclude', 'exclude_example'),
                    ('response_fields', 'response_fields_example'),
                    ('product_id', 'product_id_example'),
                    ('lang_id', 'lang_id_example'),
                    ('store_id', 'store_id_example')]
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
        'store_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1.1/product.option.list.json',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_product_option_value_add(client):
    """Test case for product_option_value_add

    
    """
    params = [('product_id', 'product_id_example'),
                    ('option_id', 'option_id_example'),
                    ('option_value', 'option_value_example'),
                    ('sort_order', 0),
                    ('clear_cache', True)]
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
        'store_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1.1/product.option.value.add.json',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_product_option_value_assign(client):
    """Test case for product_option_value_assign

    
    """
    params = [('product_option_id', 56),
                    ('option_value_id', 56),
                    ('clear_cache', True)]
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
        'store_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1.1/product.option.value.assign.json',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_product_option_value_update(client):
    """Test case for product_option_value_update

    
    """
    params = [('product_id', 'product_id_example'),
                    ('option_id', 'option_id_example'),
                    ('option_value_id', 56),
                    ('option_value', 'option_value_example'),
                    ('price', 3.4),
                    ('quantity', 3.4),
                    ('clear_cache', True)]
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
        'store_key': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/v1.1/product.option.value.update.json',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_product_price_add(client):
    """Test case for product_price_add

    
    """
    body = {"group_prices":[{"group_id":"group_id","price":6.027456183070403},{"group_id":"group_id","price":6.027456183070403}],"product_id":"product_id"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'api_key': 'special-key',
        'store_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1.1/product.price.add.json',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_product_price_delete(client):
    """Test case for product_price_delete

    
    """
    params = [('product_id', 'product_id_example'),
                    ('group_prices', 'group_prices_example')]
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
        'store_key': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/v1.1/product.price.delete.json',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_product_price_update(client):
    """Test case for product_price_update

    
    """
    body = {"group_prices":[{"group_id":"group_id","price":6.027456183070403,"id":0},{"group_id":"group_id","price":6.027456183070403,"id":0}],"product_id":"product_id"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'api_key': 'special-key',
        'store_key': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/v1.1/product.price.update.json',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_product_review_list(client):
    """Test case for product_review_list

    
    """
    params = [('start', 0),
                    ('page_cursor', 'page_cursor_example'),
                    ('count', 10),
                    ('product_id', 'product_id_example'),
                    ('ids', 'ids_example'),
                    ('store_id', 'store_id_example'),
                    ('status', 'status_example'),
                    ('params', 'id,customer_id,email,message,status,product_id,nick_name,summary,rating,ratings,status,created_time'),
                    ('exclude', 'exclude_example'),
                    ('response_fields', 'response_fields_example')]
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
        'store_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1.1/product.review.list.json',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_product_store_assign(client):
    """Test case for product_store_assign

    
    """
    params = [('product_id', 'product_id_example'),
                    ('store_id', 'store_id_example')]
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
        'store_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1.1/product.store.assign.json',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_product_tax_add(client):
    """Test case for product_tax_add

    
    """
    body = {"product_id":"product_id","name":"name","tax_rates":[{"name":"name","type":"type","value":0.8008281904610115},{"name":"name","type":"type","value":0.8008281904610115}]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'api_key': 'special-key',
        'store_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1.1/product.tax.add.json',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_product_update(client):
    """Test case for product_update

    
    """
    body = {"short_description":"short_description","seo_url":"seo_url","reserve_quantity":3.616076749251911,"description":"description","reduce_quantity":9.301444243932576,"sprice_create":"sprice_create","in_stock":True,"meta_keywords":"meta_keywords","search_keywords":"search_keywords","retail_price":2.027123023002322,"manufacturer":"manufacturer","product_class":"product_class","clear_cache":True,"increase_quantity":1.4658129805029452,"price":2.3021358869347655,"model":"model","id":"id","sku":"sku","barcode":"barcode","cost_price":0.8008281904610115,"height":6.027456183070403,"store_id":"store_id","manage_stock":True,"gtin":"gtin","manufacturer_id":"manufacturer_id","quantity":7.061401241503109,"visible":"visible","meta_title":"meta_title","reindex":True,"taxable":True,"old_price":5.637376656633329,"country_of_origin":"country_of_origin","length":5.962133916683182,"lang_id":"lang_id","weight":7.386281948385884,"disable_report_cache":False,"tags":"tags","report_request_id":"report_request_id","meta_description":"meta_description","special_price":4.145608029883936,"name":"name","width":1.2315135367772556,"sprice_expire":"sprice_expire","harmonized_system_code":"harmonized_system_code","backorder_status":"backorder_status","categories_ids":"categories_ids","status":"status","warehouse_id":"warehouse_id"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'api_key': 'special-key',
        'store_key': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/v1.1/product.update.json',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_product_variant_add(client):
    """Test case for product_variant_add

    
    """
    body = {"short_description":"short_description","created_at":"created_at","description":"description","sprice_create":"sprice_create","meta_keywords":"meta_keywords","manufacturer":"manufacturer","clear_cache":True,"price":5.637376656633329,"product_id":"product_id","model":"model","sku":"sku","sprice_modified":"sprice_modified","barcode":"barcode","available_for_sale":True,"cost_price":6.027456183070403,"height":1.4658129805029452,"store_id":"store_id","manage_stock":True,"quantity":2.3021358869347655,"meta_title":"meta_title","taxable":True,"country_of_origin":"country_of_origin","length":5.962133916683182,"tax_class_id":"tax_class_id","lang_id":"lang_id","weight":9.301444243932576,"url":"url","meta_description":"meta_description","weight_unit":"weight_unit","special_price":7.061401241503109,"name":"name","width":3.616076749251911,"sprice_expire":"sprice_expire","attributes":[{"attribute_name":"attribute_name","attribute_value":"attribute_value","attribute_price":0.8008281904610115},{"attribute_name":"attribute_name","attribute_value":"attribute_value","attribute_price":0.8008281904610115}],"harmonized_system_code":"harmonized_system_code","available_for_view":True,"warehouse_id":"warehouse_id"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'api_key': 'special-key',
        'store_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1.1/product.variant.add.json',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_product_variant_count(client):
    """Test case for product_variant_count

    
    """
    params = [('created_from', 'created_from_example'),
                    ('created_to', 'created_to_example'),
                    ('modified_from', 'modified_from_example'),
                    ('modified_to', 'modified_to_example'),
                    ('category_id', 'category_id_example'),
                    ('product_id', 'product_id_example'),
                    ('store_id', 'store_id_example')]
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
        'store_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1.1/product.variant.count.json',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_product_variant_delete(client):
    """Test case for product_variant_delete

    
    """
    params = [('id', 'id_example'),
                    ('product_id', 'product_id_example')]
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
        'store_key': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/v1.1/product.variant.delete.json',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_product_variant_image_add(client):
    """Test case for product_variant_image_add

    
    """
    body = {"store_id":"store_id","image_name":"image_name","mime":"mime","product_id":"product_id","option_id":"option_id","label":"label","position":0,"product_variant_id":6,"type":"base","content":"content","url":"url"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'api_key': 'special-key',
        'store_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1.1/product.variant.image.add.json',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_product_variant_image_delete(client):
    """Test case for product_variant_image_delete

    
    """
    params = [('product_id', 'product_id_example'),
                    ('product_variant_id', 56),
                    ('id', 'id_example'),
                    ('store_id', 'store_id_example')]
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
        'store_key': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/v1.1/product.variant.image.delete.json',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_product_variant_info(client):
    """Test case for product_variant_info

    
    """
    params = [('params', 'id,name,description,price'),
                    ('exclude', 'exclude_example'),
                    ('id', 'id_example'),
                    ('store_id', 'store_id_example')]
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
        'store_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1.1/product.variant.info.json',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_product_variant_list(client):
    """Test case for product_variant_list

    
    """
    params = [('start', 0),
                    ('count', 10),
                    ('params', 'id,name,description,price'),
                    ('exclude', 'exclude_example'),
                    ('created_from', 'created_from_example'),
                    ('created_to', 'created_to_example'),
                    ('modified_from', 'modified_from_example'),
                    ('modified_to', 'modified_to_example'),
                    ('category_id', 'category_id_example'),
                    ('product_id', 'product_id_example'),
                    ('store_id', 'store_id_example')]
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
        'store_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1.1/product.variant.list.json',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_product_variant_price_add(client):
    """Test case for product_variant_price_add

    
    """
    body = {"group_prices":[{"group_id":"group_id","price":6.027456183070403},{"group_id":"group_id","price":6.027456183070403}],"product_id":"product_id","id":"id"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'api_key': 'special-key',
        'store_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1.1/product.variant.price.add.json',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_product_variant_price_delete(client):
    """Test case for product_variant_price_delete

    
    """
    params = [('id', 'id_example'),
                    ('product_id', 'product_id_example'),
                    ('group_prices', 'group_prices_example')]
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
        'store_key': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/v1.1/product.variant.price.delete.json',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_product_variant_price_update(client):
    """Test case for product_variant_price_update

    
    """
    body = {"group_prices":[{"group_id":"group_id","price":6.027456183070403,"id":0},{"group_id":"group_id","price":6.027456183070403,"id":0}],"product_id":"product_id","id":"id"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'api_key': 'special-key',
        'store_key': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/v1.1/product.variant.price.update.json',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_product_variant_update(client):
    """Test case for product_variant_update

    
    """
    body = {"short_description":"short_description","reserve_quantity":3.616076749251911,"description":"description","reduce_quantity":9.301444243932576,"sprice_create":"sprice_create","in_stock":True,"meta_keywords":"meta_keywords","retail_price":2.027123023002322,"clear_cache":True,"increase_quantity":1.4658129805029452,"price":2.3021358869347655,"product_id":"product_id","options":[{"option_value":"option_value","option_name":"option_name"},{"option_value":"option_value","option_name":"option_name"}],"model":"model","id":"id","sku":"sku","barcode":"barcode","available_for_sale":True,"cost_price":0.8008281904610115,"height":6.027456183070403,"store_id":"store_id","manage_stock":True,"gtin":"gtin","quantity":7.061401241503109,"visible":"visible","meta_title":"meta_title","reindex":True,"taxable":True,"old_price":5.637376656633329,"country_of_origin":"country_of_origin","length":5.962133916683182,"lang_id":"lang_id","weight":7.386281948385884,"meta_description":"meta_description","special_price":4.145608029883936,"name":"name","width":1.2315135367772556,"sprice_expire":"sprice_expire","harmonized_system_code":"harmonized_system_code","backorder_status":"backorder_status","status":"status","warehouse_id":"warehouse_id"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'api_key': 'special-key',
        'store_key': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/v1.1/product.variant.update.json',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

