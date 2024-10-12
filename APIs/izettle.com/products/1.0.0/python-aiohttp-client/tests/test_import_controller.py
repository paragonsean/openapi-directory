# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.bulk_import_request import BulkImportRequest
from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.import_response import ImportResponse


pytestmark = pytest.mark.asyncio

async def test_get_latest_import_status(client):
    """Test case for get_latest_import_status

    Get status for latest import
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/organizations/{organization_uuid}/import/status'.format(organization_uuid='organization_uuid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_status_by_uuid(client):
    """Test case for get_status_by_uuid

    Get status for an import
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/organizations/{organization_uuid}/import/status/{import_uuid}'.format(organization_uuid='organization_uuid_example', import_uuid='import_uuid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_import_library_v2(client):
    """Test case for import_library_v2

    Import library items
    """
    body = {"products":[{"metadata":{"inPos":True,"source":{"external":True,"name":"name"}},"taxExempt":True,"unitName":"unitName","description":"description","variants":[{"presentation":{"backgroundColor":"backgroundColor","imageUrl":"imageUrl","textColor":"textColor"},"price":{"amount":0,"currencyId":"AED"},"vatPercentage":14.658129805029452,"costPrice":{"amount":0,"currencyId":"AED"},"name":"name","options":[{"name":"name","value":"value"},{"name":"name","value":"value"},{"name":"name","value":"value"},{"name":"name","value":"value"},{"name":"name","value":"value"}],"description":"description","sku":"sku","barcode":"barcode","uuid":"046b6c7f-0b8a-43b9-b35d-6489e6daee91"},{"presentation":{"backgroundColor":"backgroundColor","imageUrl":"imageUrl","textColor":"textColor"},"price":{"amount":0,"currencyId":"AED"},"vatPercentage":14.658129805029452,"costPrice":{"amount":0,"currencyId":"AED"},"name":"name","options":[{"name":"name","value":"value"},{"name":"name","value":"value"},{"name":"name","value":"value"},{"name":"name","value":"value"},{"name":"name","value":"value"}],"description":"description","sku":"sku","barcode":"barcode","uuid":"046b6c7f-0b8a-43b9-b35d-6489e6daee91"}],"taxCode":"taxCode","uuid":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","externalReference":"externalReference","presentation":{"backgroundColor":"backgroundColor","imageUrl":"imageUrl","textColor":"textColor"},"taxRates":["046b6c7f-0b8a-43b9-b35d-6489e6daee91","046b6c7f-0b8a-43b9-b35d-6489e6daee91"],"vatPercentage":59.621339166831824,"name":"name","online":{"presentation":{"displayImageUrl":"http://example.com/aeiou","additionalImageUrls":["http://example.com/aeiou","http://example.com/aeiou","http://example.com/aeiou","http://example.com/aeiou","http://example.com/aeiou"],"mediaUrls":["http://example.com/aeiou","http://example.com/aeiou","http://example.com/aeiou","http://example.com/aeiou","http://example.com/aeiou"]},"shipping":{"shippingPricingModel":"FREE","weightInGrams":1294386358,"weight":{"unit":"kg","weight":0.08008281904610115}},"description":"description","seo":{"title":"title","metaDescription":"metaDescription","slug":"slug"},"title":"title","status":"ACTIVE"},"categories":["categories"],"imageLookupKeys":["imageLookupKeys","imageLookupKeys"],"category":{"name":"name","uuid":"046b6c7f-0b8a-43b9-b35d-6489e6daee91"},"variantOptionDefinitions":{"definitions":[{"name":"name","properties":[{"imageUrl":"imageUrl","value":"value"},{"imageUrl":"imageUrl","value":"value"},{"imageUrl":"imageUrl","value":"value"},{"imageUrl":"imageUrl","value":"value"},{"imageUrl":"imageUrl","value":"value"}]},{"name":"name","properties":[{"imageUrl":"imageUrl","value":"value"},{"imageUrl":"imageUrl","value":"value"},{"imageUrl":"imageUrl","value":"value"},{"imageUrl":"imageUrl","value":"value"},{"imageUrl":"imageUrl","value":"value"}]},{"name":"name","properties":[{"imageUrl":"imageUrl","value":"value"},{"imageUrl":"imageUrl","value":"value"},{"imageUrl":"imageUrl","value":"value"},{"imageUrl":"imageUrl","value":"value"},{"imageUrl":"imageUrl","value":"value"}]}]}},{"metadata":{"inPos":True,"source":{"external":True,"name":"name"}},"taxExempt":True,"unitName":"unitName","description":"description","variants":[{"presentation":{"backgroundColor":"backgroundColor","imageUrl":"imageUrl","textColor":"textColor"},"price":{"amount":0,"currencyId":"AED"},"vatPercentage":14.658129805029452,"costPrice":{"amount":0,"currencyId":"AED"},"name":"name","options":[{"name":"name","value":"value"},{"name":"name","value":"value"},{"name":"name","value":"value"},{"name":"name","value":"value"},{"name":"name","value":"value"}],"description":"description","sku":"sku","barcode":"barcode","uuid":"046b6c7f-0b8a-43b9-b35d-6489e6daee91"},{"presentation":{"backgroundColor":"backgroundColor","imageUrl":"imageUrl","textColor":"textColor"},"price":{"amount":0,"currencyId":"AED"},"vatPercentage":14.658129805029452,"costPrice":{"amount":0,"currencyId":"AED"},"name":"name","options":[{"name":"name","value":"value"},{"name":"name","value":"value"},{"name":"name","value":"value"},{"name":"name","value":"value"},{"name":"name","value":"value"}],"description":"description","sku":"sku","barcode":"barcode","uuid":"046b6c7f-0b8a-43b9-b35d-6489e6daee91"}],"taxCode":"taxCode","uuid":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","externalReference":"externalReference","presentation":{"backgroundColor":"backgroundColor","imageUrl":"imageUrl","textColor":"textColor"},"taxRates":["046b6c7f-0b8a-43b9-b35d-6489e6daee91","046b6c7f-0b8a-43b9-b35d-6489e6daee91"],"vatPercentage":59.621339166831824,"name":"name","online":{"presentation":{"displayImageUrl":"http://example.com/aeiou","additionalImageUrls":["http://example.com/aeiou","http://example.com/aeiou","http://example.com/aeiou","http://example.com/aeiou","http://example.com/aeiou"],"mediaUrls":["http://example.com/aeiou","http://example.com/aeiou","http://example.com/aeiou","http://example.com/aeiou","http://example.com/aeiou"]},"shipping":{"shippingPricingModel":"FREE","weightInGrams":1294386358,"weight":{"unit":"kg","weight":0.08008281904610115}},"description":"description","seo":{"title":"title","metaDescription":"metaDescription","slug":"slug"},"title":"title","status":"ACTIVE"},"categories":["categories"],"imageLookupKeys":["imageLookupKeys","imageLookupKeys"],"category":{"name":"name","uuid":"046b6c7f-0b8a-43b9-b35d-6489e6daee91"},"variantOptionDefinitions":{"definitions":[{"name":"name","properties":[{"imageUrl":"imageUrl","value":"value"},{"imageUrl":"imageUrl","value":"value"},{"imageUrl":"imageUrl","value":"value"},{"imageUrl":"imageUrl","value":"value"},{"imageUrl":"imageUrl","value":"value"}]},{"name":"name","properties":[{"imageUrl":"imageUrl","value":"value"},{"imageUrl":"imageUrl","value":"value"},{"imageUrl":"imageUrl","value":"value"},{"imageUrl":"imageUrl","value":"value"},{"imageUrl":"imageUrl","value":"value"}]},{"name":"name","properties":[{"imageUrl":"imageUrl","value":"value"},{"imageUrl":"imageUrl","value":"value"},{"imageUrl":"imageUrl","value":"value"},{"imageUrl":"imageUrl","value":"value"},{"imageUrl":"imageUrl","value":"value"}]}]}}]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/organizations/{organization_uuid}/import/v2'.format(organization_uuid='organization_uuid_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

