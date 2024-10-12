# coding: utf-8

import pytest
import json
from aiohttp import web
from aiohttp import FormData

from openapi_server.models.create_strategy200_response import CreateStrategy200Response
from openapi_server.models.create_strategy_request import CreateStrategyRequest
from openapi_server.models.delete_strategy200_response import DeleteStrategy200Response
from openapi_server.models.get_repricer_feed200_response import GetRepricerFeed200Response
from openapi_server.models.get_repricer_feed_request import GetRepricerFeedRequest
from openapi_server.models.get_strategies200_response import GetStrategies200Response
from openapi_server.models.opt_cap_program_in_price200_response import OptCapProgramInPrice200Response
from openapi_server.models.opt_cap_program_in_price_request import OptCapProgramInPriceRequest
from openapi_server.models.price_bulk_uploads200_response import PriceBulkUploads200Response
from openapi_server.models.update_price200_response import UpdatePrice200Response
from openapi_server.models.update_price_request import UpdatePriceRequest


pytestmark = pytest.mark.asyncio

async def test_create_strategy(client):
    """Test case for create_strategy

    Create Repricer Strategy
    """
    body = openapi_server.CreateStrategyRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'wm_sec_access_token': 'eyJraWQiOiIzZjVhYTFmNS1hYWE5LTQzM.....',
        'wm_consumer_channel_type': 'wm_consumer_channel_type_example',
        'wm_qos_correlation_id': 'b3261d2d-028a-4ef7-8602-633c23200af6',
        'wm_svc_name': 'Walmart Service Name',
    }
    response = await client.request(
        method='POST',
        path='/v3/repricer/strategy',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_strategy(client):
    """Test case for delete_strategy

    Delete Repricer Strategy
    """
    headers = { 
        'Accept': 'application/json',
        'wm_sec_access_token': 'eyJraWQiOiIzZjVhYTFmNS1hYWE5LTQzM.....',
        'wm_consumer_channel_type': 'wm_consumer_channel_type_example',
        'wm_qos_correlation_id': 'b3261d2d-028a-4ef7-8602-633c23200af6',
        'wm_svc_name': 'Walmart Service Name',
    }
    response = await client.request(
        method='DELETE',
        path='/v3/repricer/strategy/{strategy_collection_id}'.format(strategy_collection_id='strategy_collection_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_repricer_feed(client):
    """Test case for get_repricer_feed

    Assign/Unassign items to/from Repricer Strategy
    """
    body = openapi_server.GetRepricerFeedRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'wm_sec_access_token': 'eyJraWQiOiIzZjVhYTFmNS1hYWE5LTQzM.....',
        'wm_consumer_channel_type': 'wm_consumer_channel_type_example',
        'wm_qos_correlation_id': 'b3261d2d-028a-4ef7-8602-633c23200af6',
        'wm_svc_name': 'Walmart Service Name',
    }
    response = await client.request(
        method='POST',
        path='/v3/repricerFeeds',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_strategies(client):
    """Test case for get_strategies

    List of Repricer Strategies
    """
    headers = { 
        'Accept': 'application/json',
        'wm_sec_access_token': 'eyJraWQiOiIzZjVhYTFmNS1hYWE5LTQzM.....',
        'wm_consumer_channel_type': 'wm_consumer_channel_type_example',
        'wm_qos_correlation_id': 'b3261d2d-028a-4ef7-8602-633c23200af6',
        'wm_svc_name': 'Walmart Service Name',
    }
    response = await client.request(
        method='GET',
        path='/v3/repricer/strategies',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_opt_cap_program_in_price(client):
    """Test case for opt_cap_program_in_price

    Set up CAP SKU All
    """
    body = openapi_server.OptCapProgramInPriceRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'wm_sec_access_token': 'eyJraWQiOiIzZjVhYTFmNS1hYWE5LTQzM.....',
        'wm_consumer_channel_type': 'wm_consumer_channel_type_example',
        'wm_qos_correlation_id': 'b3261d2d-028a-4ef7-8602-633c23200af6',
        'wm_svc_name': 'Walmart Service Name',
    }
    response = await client.request(
        method='POST',
        path='/v3/cppreference',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("multipart/form-data not supported by Connexion")
async def test_price_bulk_uploads(client):
    """Test case for price_bulk_uploads

    Update bulk prices (Multiple)
    """
    params = [('feedType', 'feed_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'multipart/form-data',
        'wm_sec_access_token': 'eyJraWQiOiIzZjVhYTFmNS1hYWE5LTQzM.....',
        'wm_consumer_channel_type': 'wm_consumer_channel_type_example',
        'wm_qos_correlation_id': 'b3261d2d-028a-4ef7-8602-633c23200af6',
        'wm_svc_name': 'Walmart Service Name',
    }
    data = FormData()
    data.add_field('file', '/path/to/file')
    response = await client.request(
        method='POST',
        path='/v3/feeds',
        headers=headers,
        data=data,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_price(client):
    """Test case for update_price

    Update a price
    """
    body = {"pricing":[{"currentPrice":{"amount":10,"currency":"USD"},"currentPriceType":"BASE"}],"sku":"97964_KFTest"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'wm_sec_access_token': 'eyJraWQiOiIzZjVhYTFmNS1hYWE5LTQzM.....',
        'wm_consumer_channel_type': 'wm_consumer_channel_type_example',
        'wm_qos_correlation_id': 'b3261d2d-028a-4ef7-8602-633c23200af6',
        'wm_svc_name': 'Walmart Service Name',
    }
    response = await client.request(
        method='PUT',
        path='/v3/price',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_strategy(client):
    """Test case for update_strategy

    Update Repricer Strategy
    """
    body = openapi_server.CreateStrategyRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'wm_sec_access_token': 'eyJraWQiOiIzZjVhYTFmNS1hYWE5LTQzM.....',
        'wm_consumer_channel_type': 'wm_consumer_channel_type_example',
        'wm_qos_correlation_id': 'b3261d2d-028a-4ef7-8602-633c23200af6',
        'wm_svc_name': 'Walmart Service Name',
    }
    response = await client.request(
        method='PUT',
        path='/v3/repricer/strategy/{strategy_collection_id}'.format(strategy_collection_id='strategy_collection_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

