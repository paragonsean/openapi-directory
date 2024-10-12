# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.batch_delete_catalog_objects_request import BatchDeleteCatalogObjectsRequest
from openapi_server.models.batch_delete_catalog_objects_response import BatchDeleteCatalogObjectsResponse
from openapi_server.models.batch_retrieve_catalog_objects_request import BatchRetrieveCatalogObjectsRequest
from openapi_server.models.batch_retrieve_catalog_objects_response import BatchRetrieveCatalogObjectsResponse
from openapi_server.models.batch_upsert_catalog_objects_request import BatchUpsertCatalogObjectsRequest
from openapi_server.models.batch_upsert_catalog_objects_response import BatchUpsertCatalogObjectsResponse
from openapi_server.models.catalog_info_response import CatalogInfoResponse
from openapi_server.models.delete_catalog_object_response import DeleteCatalogObjectResponse
from openapi_server.models.list_catalog_response import ListCatalogResponse
from openapi_server.models.retrieve_catalog_object_response import RetrieveCatalogObjectResponse
from openapi_server.models.search_catalog_items_request import SearchCatalogItemsRequest
from openapi_server.models.search_catalog_items_response import SearchCatalogItemsResponse
from openapi_server.models.search_catalog_objects_request import SearchCatalogObjectsRequest
from openapi_server.models.search_catalog_objects_response import SearchCatalogObjectsResponse
from openapi_server.models.update_item_modifier_lists_request import UpdateItemModifierListsRequest
from openapi_server.models.update_item_modifier_lists_response import UpdateItemModifierListsResponse
from openapi_server.models.update_item_taxes_request import UpdateItemTaxesRequest
from openapi_server.models.update_item_taxes_response import UpdateItemTaxesResponse
from openapi_server.models.upsert_catalog_object_request import UpsertCatalogObjectRequest
from openapi_server.models.upsert_catalog_object_response import UpsertCatalogObjectResponse


pytestmark = pytest.mark.asyncio

async def test_batch_delete_catalog_objects(client):
    """Test case for batch_delete_catalog_objects

    BatchDeleteCatalogObjects
    """
    body = {"request_body":{"object_ids":["W62UWFY35CWMYGVWK6TWJDNI","AA27W3M2GGTF3H6AVPNB77CK"]}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v2/catalog/batch-delete',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_batch_retrieve_catalog_objects(client):
    """Test case for batch_retrieve_catalog_objects

    BatchRetrieveCatalogObjects
    """
    body = {"request_body":{"include_related_objects":True,"object_ids":["W62UWFY35CWMYGVWK6TWJDNI","AA27W3M2GGTF3H6AVPNB77CK"]}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v2/catalog/batch-retrieve',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_batch_upsert_catalog_objects(client):
    """Test case for batch_upsert_catalog_objects

    BatchUpsertCatalogObjects
    """
    body = {"request_body":{"batches":[{"objects":[{"id":"#Tea","item_data":{"category_id":"#Beverages","description":"Hot Leaf Juice","name":"Tea","tax_ids":["#SalesTax"],"variations":[{"id":"#Tea_Mug","item_variation_data":{"item_id":"#Tea","name":"Mug","price_money":{"amount":150,"currency":"USD"},"pricing_type":"FIXED_PRICING"},"present_at_all_locations":True,"type":"ITEM_VARIATION"}]},"present_at_all_locations":True,"type":"ITEM"},{"id":"#Coffee","item_data":{"category_id":"#Beverages","description":"Hot Bean Juice","name":"Coffee","tax_ids":["#SalesTax"],"variations":[{"id":"#Coffee_Regular","item_variation_data":{"item_id":"#Coffee","name":"Regular","price_money":{"amount":250,"currency":"USD"},"pricing_type":"FIXED_PRICING"},"present_at_all_locations":True,"type":"ITEM_VARIATION"},{"id":"#Coffee_Large","item_variation_data":{"item_id":"#Coffee","name":"Large","price_money":{"amount":350,"currency":"USD"},"pricing_type":"FIXED_PRICING"},"present_at_all_locations":True,"type":"ITEM_VARIATION"}]},"present_at_all_locations":True,"type":"ITEM"},{"category_data":{"name":"Beverages"},"id":"#Beverages","present_at_all_locations":True,"type":"CATEGORY"},{"id":"#SalesTax","present_at_all_locations":True,"tax_data":{"applies_to_custom_amounts":True,"calculation_phase":"TAX_SUBTOTAL_PHASE","enabled":True,"inclusion_type":"ADDITIVE","name":"Sales Tax","percentage":"5.0"},"type":"TAX"}]}],"idempotency_key":"789ff020-f723-43a9-b4b5-43b5dc1fa3dc"}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v2/catalog/batch-upsert',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_catalog_info(client):
    """Test case for catalog_info

    CatalogInfo
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v2/catalog/info',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_catalog_object(client):
    """Test case for delete_catalog_object

    DeleteCatalogObject
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/v2/catalog/object/{object_id}'.format(object_id='object_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_catalog(client):
    """Test case for list_catalog

    ListCatalog
    """
    params = [('cursor', 'cursor_example'),
                    ('types', 'types_example'),
                    ('catalog_version', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v2/catalog/list',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_retrieve_catalog_object(client):
    """Test case for retrieve_catalog_object

    RetrieveCatalogObject
    """
    params = [('include_related_objects', True),
                    ('catalog_version', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v2/catalog/object/{object_id}'.format(object_id='object_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_search_catalog_items(client):
    """Test case for search_catalog_items

    SearchCatalogItems
    """
    body = {"request_body":{"category_ids":["WINE_CATEGORY_ID"],"custom_attribute_filters":[{"bool_filter":True,"custom_attribute_definition_id":"VEGAN_DEFINITION_ID"},{"custom_attribute_definition_id":"BRAND_DEFINITION_ID","string_filter":"Dark Horse"},{"key":"VINTAGE","number_filter":{"max":2018,"min":2017}},{"custom_attribute_definition_id":"VARIETAL_DEFINITION_ID","selection_ids_filter":"MERLOT_SELECTION_ID"}],"enabled_location_ids":["ATL_LOCATION_ID"],"limit":100,"product_types":["REGULAR"],"sort_order":"ASC","stock_levels":["OUT","LOW"],"text_filter":"red"}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v2/catalog/search-catalog-items',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_search_catalog_objects(client):
    """Test case for search_catalog_objects

    SearchCatalogObjects
    """
    body = {"request_body":{"limit":100,"object_types":["ITEM"],"query":{"prefix_query":{"attribute_name":"name","attribute_prefix":"tea"}}}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v2/catalog/search',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_item_modifier_lists(client):
    """Test case for update_item_modifier_lists

    UpdateItemModifierLists
    """
    body = {"request_body":{"item_ids":["H42BRLUJ5KTZTTMPVSLFAACQ","2JXOBJIHCWBQ4NZ3RIXQGJA6"],"modifier_lists_to_disable":["7WRC16CJZDVLSNDQ35PP6YAD"],"modifier_lists_to_enable":["H42BRLUJ5KTZTTMPVSLFAACQ","2JXOBJIHCWBQ4NZ3RIXQGJA6"]}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v2/catalog/update-item-modifier-lists',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_item_taxes(client):
    """Test case for update_item_taxes

    UpdateItemTaxes
    """
    body = {"request_body":{"item_ids":["H42BRLUJ5KTZTTMPVSLFAACQ","2JXOBJIHCWBQ4NZ3RIXQGJA6"],"taxes_to_disable":["AQCEGCEBBQONINDOHRGZISEX"],"taxes_to_enable":["4WRCNHCJZDVLSNDQ35PP6YAD"]}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v2/catalog/update-item-taxes',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_upsert_catalog_object(client):
    """Test case for upsert_catalog_object

    UpsertCatalogObject
    """
    body = {"request_body":{"idempotency_key":"af3d1afc-7212-4300-b463-0bfc5314a5ae","object":{"id":"#Cocoa","item_data":{"abbreviation":"Ch","description":"Hot Chocolate","name":"Cocoa","variations":[{"id":"#Small","item_variation_data":{"item_id":"#Cocoa","name":"Small","pricing_type":"VARIABLE_PRICING"},"type":"ITEM_VARIATION"},{"id":"#Large","item_variation_data":{"item_id":"#Cocoa","name":"Large","price_money":{"amount":400,"currency":"USD"},"pricing_type":"FIXED_PRICING"},"type":"ITEM_VARIATION"}]},"type":"ITEM"}}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v2/catalog/object',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

