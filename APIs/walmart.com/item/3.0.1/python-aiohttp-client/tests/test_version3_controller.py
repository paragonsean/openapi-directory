# coding: utf-8

import pytest
import json
from aiohttp import web
from aiohttp import FormData



pytestmark = pytest.mark.asyncio

@pytest.mark.skip("multipart/form-data not supported by Connexion")
async def test_v3do_post_multi_part(client):
    """Test case for v3do_post_multi_part

    Upload an item feed
    """
    params = [('feedType', item)]
    headers = { 
        'Content-Type': 'multipart/form-data',
        'wm_consumer_channel_type': SWAGGER_CHANNEL_TYPE,
        'wm_consumer_id': 'wm_consumer_id_example',
        'wm_sec_timestamp': 'Auto populated',
        'wm_sec_auth_signature': 'Auto populated',
        'wm_svc_name': 'Walmart Marketplace',
        'wm_qos_correlation_id': '123456abcdef',
    }
    data = FormData()
    data.add_field('file', '/path/to/file')
    response = await client.request(
        method='POST',
        path='/proxy/item-api-doc-app/rest/v3/feeds',
        headers=headers,
        data=data,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_v3get_all_items_status(client):
    """Test case for v3get_all_items_status

    Get status of an item within a feed
    """
    params = [('includeDetails', 'false'),
                    ('offset', '0'),
                    ('limit', '50')]
    headers = { 
        'wm_consumer_channel_type': SWAGGER_CHANNEL_TYPE,
        'wm_consumer_id': 'wm_consumer_id_example',
        'wm_sec_timestamp': 'Auto populated',
        'wm_sec_auth_signature': 'Auto populated',
        'wm_svc_name': 'Walmart Marketplace',
        'wm_qos_correlation_id': '123456abcdef',
    }
    response = await client.request(
        method='GET',
        path='/proxy/item-api-doc-app/rest/v3/feeds/{feed_id}'.format(feed_id='feed_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_v3get_feed_item_status(client):
    """Test case for v3get_feed_item_status

    Get status of an item feed
    """
    params = [('feedId', 'feed_id_example'),
                    ('includeDetails', 'false'),
                    ('offset', '0'),
                    ('limit', '50')]
    headers = { 
        'wm_consumer_channel_type': SWAGGER_CHANNEL_TYPE,
        'wm_consumer_id': 'wm_consumer_id_example',
        'wm_sec_timestamp': 'Auto populated',
        'wm_sec_auth_signature': 'Auto populated',
        'wm_svc_name': 'Walmart Marketplace',
        'wm_qos_correlation_id': '123456abcdef',
    }
    response = await client.request(
        method='GET',
        path='/proxy/item-api-doc-app/rest/v3/feeds',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

