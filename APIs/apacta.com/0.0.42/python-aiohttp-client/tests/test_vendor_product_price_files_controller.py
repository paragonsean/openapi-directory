# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.bad_request_response import BadRequestResponse
from openapi_server.models.create_success_response import CreateSuccessResponse
from openapi_server.models.error_not_found import ErrorNotFound
from openapi_server.models.vendor_product_price_files_get200_response import VendorProductPriceFilesGet200Response
from openapi_server.models.vendor_product_price_files_vendor_product_price_file_id_get200_response import VendorProductPriceFilesVendorProductPriceFileIdGet200Response


pytestmark = pytest.mark.asyncio

async def test_vendor_product_price_files_get(client):
    """Test case for vendor_product_price_files_get

    Get a list of price files
    """
    params = [('file_name', 'file_name_example'),
                    ('vendor_name', 'vendor_name_example'),
                    ('vendor_ids', ['vendor_ids_example']),
                    ('status', 'status_example')]
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
        'X-Auth-Token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/vendor_product_price_files',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_vendor_product_price_files_post(client):
    """Test case for vendor_product_price_files_post

    Upload a vendor price file
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'api_key': 'special-key',
        'X-Auth-Token': 'special-key',
    }
    data = {
        'companies_vendor_id': 'companies_vendor_id_example',
        'file': '/path/to/file'
        }
    response = await client.request(
        method='POST',
        path='/api/v1/vendor_product_price_files',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_vendor_product_price_files_vendor_product_price_file_id_get(client):
    """Test case for vendor_product_price_files_vendor_product_price_file_id_get

    Get a single price file
    """
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
        'X-Auth-Token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/vendor_product_price_files/{vendor_product_price_file_id}'.format(vendor_product_price_file_id='vendor_product_price_file_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

