# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.list_result_product_details_api_model import ListResultProductDetailsApiModel
from openapi_server.models.product_create_api_model import ProductCreateApiModel
from openapi_server.models.product_delete_api_model import ProductDeleteApiModel
from openapi_server.models.product_full_details_api_model import ProductFullDetailsApiModel
from openapi_server.models.product_update_api_model import ProductUpdateApiModel


pytestmark = pytest.mark.asyncio

async def test_product_api_all(client):
    """Test case for product_api_all

    Return all products for the account
    """
    params = [('queryOptions.page', 56),
                    ('queryOptions.pageSize', 56)]
    headers = { 
        'Accept': 'application/json',
        'x_auth_key': '[authentication key]',
        'x_auth_secret': '[authentication secret]',
    }
    response = await client.request(
        method='GET',
        path='/api/product/all',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_product_api_delete(client):
    """Test case for product_api_delete

    Delete an existing product
    """
    body = {"Id":0}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_auth_key': '[authentication key]',
        'x_auth_secret': '[authentication secret]',
    }
    response = await client.request(
        method='POST',
        path='/api/product/delete',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_product_api_details(client):
    """Test case for product_api_details

    Return product details
    """
    params = [('id', 56)]
    headers = { 
        'Accept': 'application/json',
        'x_auth_key': '[authentication key]',
        'x_auth_secret': '[authentication secret]',
    }
    response = await client.request(
        method='GET',
        path='/api/product/details',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_product_api_new(client):
    """Test case for product_api_new

    Create a product
    """
    body = {"Status":"Active","Description":"Description","ShippingAmount":6.027456183070403,"ButtonCallToAction":"ButtonCallToAction","Discounts":[{"DiscountPercentage":9.301444243932576,"ValidTo":"2000-01-23T04:56:07.000+00:00","ValidFrom":"2000-01-23T04:56:07.000+00:00","Id":3,"DiscountAmount":7.061401241503109,"Name":"Name"},{"DiscountPercentage":9.301444243932576,"ValidTo":"2000-01-23T04:56:07.000+00:00","ValidFrom":"2000-01-23T04:56:07.000+00:00","Id":3,"DiscountAmount":7.061401241503109,"Name":"Name"}],"Attachments":[{"Type":"External","OriginalFileName":"OriginalFileName","Size":6,"Id":0,"Link":"Link","ObfuscatedFileName":"ObfuscatedFileName"},{"Type":"External","OriginalFileName":"OriginalFileName","Size":6,"Id":0,"Link":"Link","ObfuscatedFileName":"ObfuscatedFileName"}],"CurrencyId":0,"IsFeatured":True,"Name":"Name","ShippingDescription":"ShippingDescription","PaymentGateways":[{"Name":"Name"},{"Name":"Name"}],"AfterPaymentDescription":"AfterPaymentDescription","WhatHappensNextDescription":"WhatHappensNextDescription","Items":[{"WorkTypeId":4,"TaxAmount":1.4894159098541704,"Description":"Description","ReferenceId":"ReferenceId","TaxPercentage":7.457744773683766,"Id":7,"TaxId":6,"TotalAmount":1.1730742509559433,"Cost":4.145608029883936,"MinimumQuantity":1.2315135367772556,"SubTotalAmount":1.0246457001441578},{"WorkTypeId":4,"TaxAmount":1.4894159098541704,"Description":"Description","ReferenceId":"ReferenceId","TaxPercentage":7.457744773683766,"Id":7,"TaxId":6,"TotalAmount":1.1730742509559433,"Cost":4.145608029883936,"MinimumQuantity":1.2315135367772556,"SubTotalAmount":1.0246457001441578}],"Coupons":[{"DiscountPercentage":5.962133916683182,"Id":5,"Code":"Code","DiscountAmount":1.4658129805029452,"ValidUntil":"2000-01-23T04:56:07.000+00:00"},{"DiscountPercentage":5.962133916683182,"Id":5,"Code":"Code","DiscountAmount":1.4658129805029452,"ValidUntil":"2000-01-23T04:56:07.000+00:00"}]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_auth_key': '[authentication key]',
        'x_auth_secret': '[authentication secret]',
    }
    response = await client.request(
        method='POST',
        path='/api/product/new',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_product_api_update(client):
    """Test case for product_api_update

    Update an existing product
    """
    body = {"Status":"Active","Description":"Description","ShippingAmount":1.4658129805029452,"ButtonCallToAction":"ButtonCallToAction","Discounts":[{"DiscountPercentage":9.301444243932576,"ValidTo":"2000-01-23T04:56:07.000+00:00","ValidFrom":"2000-01-23T04:56:07.000+00:00","Id":3,"DiscountAmount":7.061401241503109,"Name":"Name"},{"DiscountPercentage":9.301444243932576,"ValidTo":"2000-01-23T04:56:07.000+00:00","ValidFrom":"2000-01-23T04:56:07.000+00:00","Id":3,"DiscountAmount":7.061401241503109,"Name":"Name"}],"Attachments":[{"Type":"External","OriginalFileName":"OriginalFileName","Size":6,"Id":0,"Link":"Link","ObfuscatedFileName":"ObfuscatedFileName"},{"Type":"External","OriginalFileName":"OriginalFileName","Size":6,"Id":0,"Link":"Link","ObfuscatedFileName":"ObfuscatedFileName"}],"CurrencyId":0,"IsFeatured":True,"Name":"Name","ShippingDescription":"ShippingDescription","PaymentGateways":[{"Name":"Name"},{"Name":"Name"}],"AfterPaymentDescription":"AfterPaymentDescription","WhatHappensNextDescription":"WhatHappensNextDescription","Items":[{"WorkTypeId":4,"TaxAmount":1.4894159098541704,"Description":"Description","ReferenceId":"ReferenceId","TaxPercentage":7.457744773683766,"Id":7,"TaxId":6,"TotalAmount":1.1730742509559433,"Cost":4.145608029883936,"MinimumQuantity":1.2315135367772556,"SubTotalAmount":1.0246457001441578},{"WorkTypeId":4,"TaxAmount":1.4894159098541704,"Description":"Description","ReferenceId":"ReferenceId","TaxPercentage":7.457744773683766,"Id":7,"TaxId":6,"TotalAmount":1.1730742509559433,"Cost":4.145608029883936,"MinimumQuantity":1.2315135367772556,"SubTotalAmount":1.0246457001441578}],"Id":6,"Coupons":[{"DiscountPercentage":5.962133916683182,"Id":5,"Code":"Code","DiscountAmount":1.4658129805029452,"ValidUntil":"2000-01-23T04:56:07.000+00:00"},{"DiscountPercentage":5.962133916683182,"Id":5,"Code":"Code","DiscountAmount":1.4658129805029452,"ValidUntil":"2000-01-23T04:56:07.000+00:00"}]}
    headers = { 
        'Content-Type': 'application/json',
        'x_auth_key': '[authentication key]',
        'x_auth_secret': '[authentication secret]',
    }
    response = await client.request(
        method='POST',
        path='/api/product/update',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

