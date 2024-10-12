# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.estimate_details import EstimateDetails
from openapi_server.models.estimate_list import EstimateList
from openapi_server.models.new_estimate import NewEstimate


pytestmark = pytest.mark.asyncio

async def test_estimate_get(client):
    """Test case for estimate_get

    Gets list of Estimates
    """
    params = [('UpdatedAfter', '2013-10-20T19:20:30+01:00'),
                    ('pageSize', 56),
                    ('pageNumber', 56),
                    ('Sort', 'sort_example'),
                    ('CompanyIDFK', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/Estimate',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_estimate_get_by_id(client):
    """Test case for estimate_get_by_id

    Gets Estimate by Estimate ID
    """
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/Estimate/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_estimate_post(client):
    """Test case for estimate_post

    Create a new draft Estimate
    """
    model = {"EstimatePrefix":"EstimatePrefix","ExchangeRate":6.027456183070403,"LineItems":[{"InventoryItemName":"InventoryItemName","UnitPrice":3.616076749251911,"Description":"Description","Discount":5.962133916683182,"TaxIDFK":7,"TaxName":"TaxName","InventoryItemIDFK":5,"Quantity":2.3021358869347655,"TaxPercent":9.301444243932576},{"InventoryItemName":"InventoryItemName","UnitPrice":3.616076749251911,"Description":"Description","Discount":5.962133916683182,"TaxIDFK":7,"TaxName":"TaxName","InventoryItemIDFK":5,"Quantity":2.3021358869347655,"TaxPercent":9.301444243932576}],"Email":"Email","Lastname":"Lastname","EstimateTaxConfigCode":"EstimateTaxConfigCode","CompanyIDFK":0,"Subject":"Subject","EstimateNumber":"EstimateNumber","CurrencyCode":"CurrencyCode","Firstname":"Firstname","CompanyName":"CompanyName","CustomerPONumber":"CustomerPONumber","DateIssued":"2000-01-23T04:56:07.000+00:00","InvoiceTemplateIDFK":1,"DueDate":"2000-01-23T04:56:07.000+00:00","Notes":"Notes"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/Estimate',
        headers=headers,
        json=model,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

