# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.beez_up_common_error_response_message import BeezUPCommonErrorResponseMessage
from openapi_server.models.copy_optimisation_request import CopyOptimisationRequest
from openapi_server.models.copy_optimisation_response import CopyOptimisationResponse
from openapi_server.models.optimise_all_request import OptimiseAllRequest
from openapi_server.models.optimise_request import OptimiseRequest


pytestmark = pytest.mark.asyncio

async def test_copy_optimisation(client):
    """Test case for copy_optimisation

    Copy product optimisations between 2 channels
    """
    body = openapi_server.CopyOptimisationRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v2/user/analytics/{store_id}/optimisations/copy'.format(store_id='store_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_optimise(client):
    """Test case for optimise

    Optimise products by page
    """
    body = openapi_server.OptimiseRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v2/user/analytics/{store_id}/optimisations/{action_name}'.format(store_id='store_id_example', action_name='action_name_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_optimise_all(client):
    """Test case for optimise_all

    Optimise all products
    """
    body = openapi_server.OptimiseAllRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v2/user/analytics/{store_id}/optimisations/all/{action_name}'.format(store_id='store_id_example', action_name='action_name_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_optimise_by_category(client):
    """Test case for optimise_by_category

    Optimise products by category
    """
    body = ['body_example']
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v2/user/analytics/{store_id}/optimisations/bycategory/{catalog_category_id}/{action_name}'.format(store_id='store_id_example', catalog_category_id='catalog_category_id_example', action_name='action_name_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_optimise_by_channel(client):
    """Test case for optimise_by_channel

    Optimise products by channel
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v2/user/analytics/{store_id}/optimisations/bychannel/{channel_id}/{action_name}'.format(store_id='store_id_example', channel_id='channel_id_example', action_name='action_name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_optimise_by_product(client):
    """Test case for optimise_by_product

    Optimise product
    """
    body = ['body_example']
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v2/user/analytics/{store_id}/optimisations/byproduct/{product_id}/{action_name}'.format(store_id='store_id_example', product_id='product_id_example', action_name='action_name_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

