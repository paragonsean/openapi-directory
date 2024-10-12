# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.billbee_interfaces_billbee_api_model_article_api_model import BillbeeInterfacesBillbeeAPIModelArticleApiModel
from openapi_server.models.billbee_interfaces_billbee_api_model_article_image_relation_api_model import BillbeeInterfacesBillbeeAPIModelArticleImageRelationApiModel
from openapi_server.models.billbee_interfaces_billbee_api_model_update_stock_api_model import BillbeeInterfacesBillbeeAPIModelUpdateStockApiModel
from openapi_server.models.billbee_interfaces_billbee_api_model_update_stock_code_api_model import BillbeeInterfacesBillbeeAPIModelUpdateStockCodeApiModel
from openapi_server.models.rechnungsdruck_web_app_controllers_api_api_paged_result_system_collections_generic_list_billbee_interfaces_billbee_api_model_article_api_custom_field_definition_model import RechnungsdruckWebAppControllersApiApiPagedResultSystemCollectionsGenericListBillbeeInterfacesBillbeeAPIModelArticleApiCustomFieldDefinitionModel
from openapi_server.models.rechnungsdruck_web_app_controllers_api_api_paged_result_system_collections_generic_list_billbee_interfaces_billbee_api_model_article_api_model import RechnungsdruckWebAppControllersApiApiPagedResultSystemCollectionsGenericListBillbeeInterfacesBillbeeAPIModelArticleApiModel
from openapi_server.models.rechnungsdruck_web_app_controllers_api_api_result_billbee_interfaces_billbee_api_model_article_api_custom_field_definition_model import RechnungsdruckWebAppControllersApiApiResultBillbeeInterfacesBillbeeAPIModelArticleApiCustomFieldDefinitionModel
from openapi_server.models.rechnungsdruck_web_app_controllers_api_api_result_billbee_interfaces_billbee_api_model_article_api_model import RechnungsdruckWebAppControllersApiApiResultBillbeeInterfacesBillbeeAPIModelArticleApiModel
from openapi_server.models.rechnungsdruck_web_app_controllers_api_api_result_billbee_interfaces_billbee_api_model_article_image_relation_api_model import RechnungsdruckWebAppControllersApiApiResultBillbeeInterfacesBillbeeAPIModelArticleImageRelationApiModel
from openapi_server.models.rechnungsdruck_web_app_controllers_api_api_result_billbee_interfaces_billbee_api_model_deleted_images_model import RechnungsdruckWebAppControllersApiApiResultBillbeeInterfacesBillbeeAPIModelDeletedImagesModel
from openapi_server.models.rechnungsdruck_web_app_controllers_api_api_result_billbee_interfaces_billbee_api_model_get_reserved_amount_response_data import RechnungsdruckWebAppControllersApiApiResultBillbeeInterfacesBillbeeAPIModelGetReservedAmountResponseData
from openapi_server.models.rechnungsdruck_web_app_controllers_api_api_result_billbee_interfaces_billbee_api_model_update_stock_code_response_data import RechnungsdruckWebAppControllersApiApiResultBillbeeInterfacesBillbeeAPIModelUpdateStockCodeResponseData
from openapi_server.models.rechnungsdruck_web_app_controllers_api_api_result_billbee_interfaces_billbee_api_model_update_stock_response_data import RechnungsdruckWebAppControllersApiApiResultBillbeeInterfacesBillbeeAPIModelUpdateStockResponseData
from openapi_server.models.rechnungsdruck_web_app_controllers_api_api_result_rechnungsdruck_web_app_controllers_api_search_controller_search_results_model import RechnungsdruckWebAppControllersApiApiResultRechnungsdruckWebAppControllersApiSearchControllerSearchResultsModel
from openapi_server.models.rechnungsdruck_web_app_controllers_api_api_result_system_collections_generic_list_billbee_interfaces_billbee_api_model_article_image_relation_api_model import RechnungsdruckWebAppControllersApiApiResultSystemCollectionsGenericListBillbeeInterfacesBillbeeAPIModelArticleImageRelationApiModel
from openapi_server.models.rechnungsdruck_web_app_controllers_api_api_result_system_collections_generic_list_billbee_interfaces_billbee_api_model_stock_response_data import RechnungsdruckWebAppControllersApiApiResultSystemCollectionsGenericListBillbeeInterfacesBillbeeAPIModelStockResponseData
from openapi_server.models.rechnungsdruck_web_app_controllers_api_search_controller_search_model import RechnungsdruckWebAppControllersApiSearchControllerSearchModel


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_article_create_article(client):
    """Test case for article_create_article

    Creates a new product
    """
    body = openapi_server.BillbeeInterfacesBillbeeAPIModelArticleApiModel()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/products',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_article_delete_article(client):
    """Test case for article_delete_article

    Deletes a product
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v1/products/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_article_delete_image(client):
    """Test case for article_delete_image

    Deletes a single image by id
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v1/products/images/{image_id}'.format(image_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_article_delete_image_from_product(client):
    """Test case for article_delete_image_from_product

    Deletes a single image from a product
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v1/products/{product_id}/images/{image_id}'.format(product_id=56, image_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_article_delete_images(client):
    """Test case for article_delete_images

    Delete multiple images by id
    """
    body = [56]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/products/images/delete',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_article_get_article(client):
    """Test case for article_get_article

    Queries a single article by id or by sku
    """
    params = [('lookupBy', 'lookup_by_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/products/{id}'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_article_get_category(client):
    """Test case for article_get_category

    GEts a list of all defined categories
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/products/category',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_article_get_custom_field(client):
    """Test case for article_get_custom_field

    Queries a single custom field
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/products/custom-fields/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_article_get_custom_fields(client):
    """Test case for article_get_custom_fields

    Queries a list of all custom fields
    """
    params = [('page', 56),
                    ('pageSize', 56)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/products/custom-fields',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_article_get_image(client):
    """Test case for article_get_image

    Returns a single image by id
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/products/images/{image_id}'.format(image_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_article_get_image_from_product(client):
    """Test case for article_get_image_from_product

    Returns a single image by id
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/products/{product_id}/images/{image_id}'.format(product_id=56, image_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_article_get_images(client):
    """Test case for article_get_images

    Returns a list of all images of the product
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/products/{product_id}/images'.format(product_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_article_get_list(client):
    """Test case for article_get_list

    Get a list of all products
    """
    params = [('page', 56),
                    ('pageSize', 56),
                    ('minCreatedAt', '2013-10-20T19:20:30+01:00'),
                    ('minimumBillBeeArticleId', 56),
                    ('maximumBillBeeArticleId', 56)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/products',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_article_get_patchable_fields(client):
    """Test case for article_get_patchable_fields

    Returns a list of fields which can be updated with the patch call
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/products/PatchableFields',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_article_get_reserved_amount(client):
    """Test case for article_get_reserved_amount

    Queries the reserved amount for a single article by id or by sku
    """
    params = [('id', 'id_example'),
                    ('lookupBy', 'lookup_by_example'),
                    ('stockId', 56)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/products/reservedamount',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_article_get_stocks(client):
    """Test case for article_get_stocks

    Query all defined stock locations
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/products/stocks',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_article_patch_article(client):
    """Test case for article_patch_article

    Updates one or more fields of a product
    """
    body = None
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PATCH',
        path='/api/v1/products/{id}'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_article_put_image(client):
    """Test case for article_put_image

    Add or update an existing image of a product
    """
    body = openapi_server.BillbeeInterfacesBillbeeAPIModelArticleImageRelationApiModel()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/api/v1/products/{product_id}/images/{image_id}'.format(product_id=56, image_id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_article_put_images(client):
    """Test case for article_put_images

    Add multiple images to a product or replace the product images by the given images
    """
    body = [openapi_server.BillbeeInterfacesBillbeeAPIModelArticleImageRelationApiModel()]
    params = [('replace', True)]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/api/v1/products/{product_id}/images'.format(product_id=56),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_article_update_stock(client):
    """Test case for article_update_stock

    Update the stock qty of an article
    """
    body = openapi_server.BillbeeInterfacesBillbeeAPIModelUpdateStockApiModel()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/products/updatestock',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_article_update_stock_code(client):
    """Test case for article_update_stock_code

    Update the stock code of an article
    """
    body = openapi_server.BillbeeInterfacesBillbeeAPIModelUpdateStockCodeApiModel()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/products/updatestockcode',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_article_update_stock_multiple(client):
    """Test case for article_update_stock_multiple

    Update the stock qty for multiple articles at once
    """
    body = [openapi_server.BillbeeInterfacesBillbeeAPIModelUpdateStockApiModel()]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/products/updatestockmultiple',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_search_search(client):
    """Test case for search_search

    Search for products, customers and orders.  Type can be \"order\", \"product\" and / or \"customer\"  Term can contains lucene query syntax
    """
    body = openapi_server.RechnungsdruckWebAppControllersApiSearchControllerSearchModel()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/search',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

