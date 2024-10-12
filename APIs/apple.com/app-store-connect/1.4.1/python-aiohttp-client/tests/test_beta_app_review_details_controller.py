# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.app_response import AppResponse
from openapi_server.models.beta_app_review_detail_response import BetaAppReviewDetailResponse
from openapi_server.models.beta_app_review_detail_update_request import BetaAppReviewDetailUpdateRequest
from openapi_server.models.beta_app_review_details_response import BetaAppReviewDetailsResponse
from openapi_server.models.error_response import ErrorResponse


pytestmark = pytest.mark.asyncio

async def test_beta_app_review_details_app_get_to_one_related(client):
    """Test case for beta_app_review_details_app_get_to_one_related

    
    """
    params = [('fields[apps]', ['fields_apps_example'])]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/betaAppReviewDetails/{id}/app'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_beta_app_review_details_get_collection(client):
    """Test case for beta_app_review_details_get_collection

    
    """
    params = [('filter[app]', ['filter_app_example']),
                    ('fields[betaAppReviewDetails]', ['fields_beta_app_review_details_example']),
                    ('limit', 56),
                    ('include', ['include_example']),
                    ('fields[apps]', ['fields_apps_example'])]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/betaAppReviewDetails',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_beta_app_review_details_get_instance(client):
    """Test case for beta_app_review_details_get_instance

    
    """
    params = [('fields[betaAppReviewDetails]', ['fields_beta_app_review_details_example']),
                    ('include', ['include_example']),
                    ('fields[apps]', ['fields_apps_example'])]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/betaAppReviewDetails/{id}'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_beta_app_review_details_update_instance(client):
    """Test case for beta_app_review_details_update_instance

    
    """
    body = {"data":{"attributes":{"demoAccountPassword":"demoAccountPassword","notes":"notes","contactEmail":"contactEmail","contactFirstName":"contactFirstName","demoAccountRequired":True,"demoAccountName":"demoAccountName","contactLastName":"contactLastName","contactPhone":"contactPhone"},"id":"id","type":"betaAppReviewDetails"}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/v1/betaAppReviewDetails/{id}'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

