# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.full_product_update_request import FullProductUpdateRequest
from openapi_server.models.product_count_response import ProductCountResponse
from openapi_server.models.product_create_request import ProductCreateRequest
from openapi_server.models.product_response import ProductResponse
from openapi_server.models.variant_options_response import VariantOptionsResponse


pytestmark = pytest.mark.asyncio

async def test_count_all_products(client):
    """Test case for count_all_products

    Retrieve the count of existing products
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/organizations/{organization_uuid}/products/v2/count'.format(organization_uuid='organization_uuid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_product(client):
    """Test case for create_product

    Create a new product
    """
    body = {"metadata":{"inPos":True,"source":{"external":True,"name":"name"}},"taxExempt":True,"unitName":"unitName","description":"description","variants":[{"presentation":{"backgroundColor":"backgroundColor","imageUrl":"imageUrl","textColor":"textColor"},"price":{"amount":0,"currencyId":"AED"},"vatPercentage":14.658129805029452,"costPrice":{"amount":0,"currencyId":"AED"},"name":"name","options":[{"name":"name","value":"value"},{"name":"name","value":"value"},{"name":"name","value":"value"},{"name":"name","value":"value"},{"name":"name","value":"value"}],"description":"description","sku":"sku","barcode":"barcode","uuid":"046b6c7f-0b8a-43b9-b35d-6489e6daee91"},{"presentation":{"backgroundColor":"backgroundColor","imageUrl":"imageUrl","textColor":"textColor"},"price":{"amount":0,"currencyId":"AED"},"vatPercentage":14.658129805029452,"costPrice":{"amount":0,"currencyId":"AED"},"name":"name","options":[{"name":"name","value":"value"},{"name":"name","value":"value"},{"name":"name","value":"value"},{"name":"name","value":"value"},{"name":"name","value":"value"}],"description":"description","sku":"sku","barcode":"barcode","uuid":"046b6c7f-0b8a-43b9-b35d-6489e6daee91"}],"taxCode":"taxCode","uuid":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","externalReference":"externalReference","presentation":{"backgroundColor":"backgroundColor","imageUrl":"imageUrl","textColor":"textColor"},"taxRates":["046b6c7f-0b8a-43b9-b35d-6489e6daee91","046b6c7f-0b8a-43b9-b35d-6489e6daee91"],"vatPercentage":8.008281904610115,"createWithDefaultTax":True,"name":"name","online":{"presentation":{"displayImageUrl":"http://example.com/aeiou","additionalImageUrls":["http://example.com/aeiou","http://example.com/aeiou","http://example.com/aeiou","http://example.com/aeiou","http://example.com/aeiou"],"mediaUrls":["http://example.com/aeiou","http://example.com/aeiou","http://example.com/aeiou","http://example.com/aeiou","http://example.com/aeiou"]},"shipping":{"shippingPricingModel":"FREE","weightInGrams":1294386358,"weight":{"unit":"kg","weight":0.08008281904610115}},"description":"description","seo":{"title":"title","metaDescription":"metaDescription","slug":"slug"},"title":"title","status":"ACTIVE"},"categories":["categories","categories"],"imageLookupKeys":["imageLookupKeys","imageLookupKeys"],"category":{"name":"name","uuid":"046b6c7f-0b8a-43b9-b35d-6489e6daee91"},"variantOptionDefinitions":{"definitions":[{"name":"name","properties":[{"imageUrl":"imageUrl","value":"value"},{"imageUrl":"imageUrl","value":"value"},{"imageUrl":"imageUrl","value":"value"},{"imageUrl":"imageUrl","value":"value"},{"imageUrl":"imageUrl","value":"value"}]},{"name":"name","properties":[{"imageUrl":"imageUrl","value":"value"},{"imageUrl":"imageUrl","value":"value"},{"imageUrl":"imageUrl","value":"value"},{"imageUrl":"imageUrl","value":"value"},{"imageUrl":"imageUrl","value":"value"}]},{"name":"name","properties":[{"imageUrl":"imageUrl","value":"value"},{"imageUrl":"imageUrl","value":"value"},{"imageUrl":"imageUrl","value":"value"},{"imageUrl":"imageUrl","value":"value"},{"imageUrl":"imageUrl","value":"value"}]}]}}
    params = [('returnEntity', False)]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/organizations/{organization_uuid}/products'.format(organization_uuid='organization_uuid_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_product(client):
    """Test case for delete_product

    Delete a single product
    """
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/organizations/{organization_uuid}/products/{product_uuid}'.format(organization_uuid='organization_uuid_example', product_uuid='product_uuid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_products(client):
    """Test case for delete_products

    Delete a list of products
    """
    params = [('uuid', ['uuid_example'])]
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/organizations/{organization_uuid}/products'.format(organization_uuid='organization_uuid_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_all_options(client):
    """Test case for get_all_options

    Retrieve an aggregate of active Options in the library
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/organizations/{organization_uuid}/products/options'.format(organization_uuid='organization_uuid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_all_products_in_pos(client):
    """Test case for get_all_products_in_pos

    Retrieve all products visible in POS
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/organizations/{organization_uuid}/products'.format(organization_uuid='organization_uuid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_all_products_v2(client):
    """Test case for get_all_products_v2

    Retrieve all products visible in POS – v2
    """
    params = [('sort', True)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/organizations/{organization_uuid}/products/v2'.format(organization_uuid='organization_uuid_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_product(client):
    """Test case for get_product

    Retrieve a single product
    """
    headers = { 
        'Accept': 'application/json',
        'if_none_match': 'if_none_match_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/organizations/{organization_uuid}/products/{product_uuid}'.format(organization_uuid='organization_uuid_example', product_uuid='product_uuid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_product(client):
    """Test case for update_product

    Update a single product
    """
    body = {"metadata":{"inPos":True,"source":{"external":True,"name":"name"}},"taxExempt":True,"unitName":"unitName","description":"description","variants":[{"presentation":{"backgroundColor":"backgroundColor","imageUrl":"imageUrl","textColor":"textColor"},"price":{"amount":0,"currencyId":"AED"},"vatPercentage":14.658129805029452,"costPrice":{"amount":0,"currencyId":"AED"},"name":"name","options":[{"name":"name","value":"value"},{"name":"name","value":"value"},{"name":"name","value":"value"},{"name":"name","value":"value"},{"name":"name","value":"value"}],"description":"description","sku":"sku","barcode":"barcode","uuid":"046b6c7f-0b8a-43b9-b35d-6489e6daee91"},{"presentation":{"backgroundColor":"backgroundColor","imageUrl":"imageUrl","textColor":"textColor"},"price":{"amount":0,"currencyId":"AED"},"vatPercentage":14.658129805029452,"costPrice":{"amount":0,"currencyId":"AED"},"name":"name","options":[{"name":"name","value":"value"},{"name":"name","value":"value"},{"name":"name","value":"value"},{"name":"name","value":"value"},{"name":"name","value":"value"}],"description":"description","sku":"sku","barcode":"barcode","uuid":"046b6c7f-0b8a-43b9-b35d-6489e6daee91"}],"taxCode":"taxCode","uuid":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","externalReference":"externalReference","presentation":{"backgroundColor":"backgroundColor","imageUrl":"imageUrl","textColor":"textColor"},"taxRates":["046b6c7f-0b8a-43b9-b35d-6489e6daee91","046b6c7f-0b8a-43b9-b35d-6489e6daee91"],"vatPercentage":59.621339166831824,"name":"name","online":{"presentation":{"displayImageUrl":"http://example.com/aeiou","additionalImageUrls":["http://example.com/aeiou","http://example.com/aeiou","http://example.com/aeiou","http://example.com/aeiou","http://example.com/aeiou"],"mediaUrls":["http://example.com/aeiou","http://example.com/aeiou","http://example.com/aeiou","http://example.com/aeiou","http://example.com/aeiou"]},"shipping":{"shippingPricingModel":"FREE","weightInGrams":1294386358,"weight":{"unit":"kg","weight":0.08008281904610115}},"description":"description","seo":{"title":"title","metaDescription":"metaDescription","slug":"slug"},"title":"title","status":"ACTIVE"},"categories":["categories"],"imageLookupKeys":["imageLookupKeys","imageLookupKeys"],"category":{"name":"name","uuid":"046b6c7f-0b8a-43b9-b35d-6489e6daee91"},"variantOptionDefinitions":{"definitions":[{"name":"name","properties":[{"imageUrl":"imageUrl","value":"value"},{"imageUrl":"imageUrl","value":"value"},{"imageUrl":"imageUrl","value":"value"},{"imageUrl":"imageUrl","value":"value"},{"imageUrl":"imageUrl","value":"value"}]},{"name":"name","properties":[{"imageUrl":"imageUrl","value":"value"},{"imageUrl":"imageUrl","value":"value"},{"imageUrl":"imageUrl","value":"value"},{"imageUrl":"imageUrl","value":"value"},{"imageUrl":"imageUrl","value":"value"}]},{"name":"name","properties":[{"imageUrl":"imageUrl","value":"value"},{"imageUrl":"imageUrl","value":"value"},{"imageUrl":"imageUrl","value":"value"},{"imageUrl":"imageUrl","value":"value"},{"imageUrl":"imageUrl","value":"value"}]}]}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'if_match': 'if_match_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/organizations/{organization_uuid}/products/v2/{product_uuid}'.format(organization_uuid='organization_uuid_example', product_uuid='product_uuid_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

