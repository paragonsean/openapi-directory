# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.regional_inventory import RegionalInventory
from openapi_server.models.regionalinventory_custom_batch_request import RegionalinventoryCustomBatchRequest
from openapi_server.models.regionalinventory_custom_batch_response import RegionalinventoryCustomBatchResponse


pytestmark = pytest.mark.asyncio

async def test_content_regionalinventory_custombatch(client):
    """Test case for content_regionalinventory_custombatch

    
    """
    body = {"entries":[{"method":"method","productId":"productId","merchantId":"merchantId","regionalInventory":{"regionId":"regionId","salePrice":{"currency":"currency","value":"value"},"kind":"kind","price":{"currency":"currency","value":"value"},"salePriceEffectiveDate":"salePriceEffectiveDate","availability":"availability","customAttributes":[{"groupValues":[null,null],"name":"name","value":"value"},{"groupValues":[null,null],"name":"name","value":"value"}]},"batchId":0},{"method":"method","productId":"productId","merchantId":"merchantId","regionalInventory":{"regionId":"regionId","salePrice":{"currency":"currency","value":"value"},"kind":"kind","price":{"currency":"currency","value":"value"},"salePriceEffectiveDate":"salePriceEffectiveDate","availability":"availability","customAttributes":[{"groupValues":[null,null],"name":"name","value":"value"},{"groupValues":[null,null],"name":"name","value":"value"}]},"batchId":0}]}
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/content/v2.1/regionalinventory/batch',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_content_regionalinventory_insert(client):
    """Test case for content_regionalinventory_insert

    
    """
    body = {"regionId":"regionId","salePrice":{"currency":"currency","value":"value"},"kind":"kind","price":{"currency":"currency","value":"value"},"salePriceEffectiveDate":"salePriceEffectiveDate","availability":"availability","customAttributes":[{"groupValues":[null,null],"name":"name","value":"value"},{"groupValues":[null,null],"name":"name","value":"value"}]}
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/content/v2.1/{merchant_id}/products/{product_id}/regionalinventory'.format(merchant_id='merchant_id_example', product_id='product_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

