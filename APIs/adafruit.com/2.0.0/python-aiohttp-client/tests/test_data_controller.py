# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.chart_data200_response import ChartData200Response
from openapi_server.models.create_data_request import CreateDataRequest
from openapi_server.models.create_group_data_request import CreateGroupDataRequest
from openapi_server.models.create_webhook_feed_data_request import CreateWebhookFeedDataRequest
from openapi_server.models.data import Data
from openapi_server.models.data_response import DataResponse


pytestmark = pytest.mark.asyncio

async def test_all_data(client):
    """Test case for all_data

    Get all data for the given feed
    """
    params = [('start_time', '2013-10-20T19:20:30+01:00'),
                    ('end_time', '2013-10-20T19:20:30+01:00'),
                    ('limit', 56),
                    ('include', 'include_example')]
    headers = { 
        'Accept': 'application/json',
        'HeaderSignature': 'special-key',
        'QueryKey': 'special-key',
        'HeaderKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/{username}/feeds/{feed_key}/data'.format(username='username_example', feed_key='feed_key_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_all_group_feed_data(client):
    """Test case for all_group_feed_data

    All data for current feed in a specific group
    """
    params = [('start_time', '2013-10-20T19:20:30+01:00'),
                    ('end_time', '2013-10-20T19:20:30+01:00'),
                    ('limit', 56)]
    headers = { 
        'Accept': 'application/json',
        'HeaderSignature': 'special-key',
        'QueryKey': 'special-key',
        'HeaderKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/{username}/groups/{group_key}/feeds/{feed_key}/data'.format(username='username_example', group_key='group_key_example', feed_key='feed_key_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_batch_create_data(client):
    """Test case for batch_create_data

    Create multiple new Data records
    """
    data = [openapi_server.CreateDataRequest()]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'HeaderSignature': 'special-key',
        'QueryKey': 'special-key',
        'HeaderKey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v2/{username}/feeds/{feed_key}/data/batch'.format(username='username_example', feed_key='feed_key_example'),
        headers=headers,
        json=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_batch_create_group_feed_data(client):
    """Test case for batch_create_group_feed_data

    Create multiple new Data records in a feed belonging to a particular group
    """
    data = [openapi_server.CreateDataRequest()]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'HeaderSignature': 'special-key',
        'QueryKey': 'special-key',
        'HeaderKey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v2/{username}/groups/{group_key}/feeds/{feed_key}/data/batch'.format(username='username_example', group_key='group_key_example', feed_key='feed_key_example'),
        headers=headers,
        json=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_chart_data(client):
    """Test case for chart_data

    Chart data for current feed
    """
    params = [('start_time', '2013-10-20T19:20:30+01:00'),
                    ('end_time', '2013-10-20T19:20:30+01:00'),
                    ('resolution', 56),
                    ('hours', 56)]
    headers = { 
        'Accept': 'application/json',
        'HeaderSignature': 'special-key',
        'QueryKey': 'special-key',
        'HeaderKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/{username}/feeds/{feed_key}/data/chart'.format(username='username_example', feed_key='feed_key_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_create_data(client):
    """Test case for create_data

    Create new Data
    """
    datum = openapi_server.CreateDataRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'HeaderSignature': 'special-key',
        'QueryKey': 'special-key',
        'HeaderKey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v2/{username}/feeds/{feed_key}/data'.format(username='username_example', feed_key='feed_key_example'),
        headers=headers,
        json=datum,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_create_group_data(client):
    """Test case for create_group_data

    Create new data for multiple feeds in a group
    """
    group_feed_data = openapi_server.CreateGroupDataRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'HeaderSignature': 'special-key',
        'QueryKey': 'special-key',
        'HeaderKey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v2/{username}/groups/{group_key}/data'.format(username='username_example', group_key='group_key_example'),
        headers=headers,
        json=group_feed_data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_create_group_feed_data(client):
    """Test case for create_group_feed_data

    Create new Data in a feed belonging to a particular group
    """
    datum = openapi_server.CreateDataRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'HeaderSignature': 'special-key',
        'QueryKey': 'special-key',
        'HeaderKey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v2/{username}/groups/{group_key}/feeds/{feed_key}/data'.format(username='username_example', group_key='group_key_example', feed_key='feed_key_example'),
        headers=headers,
        json=datum,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_raw_webhook_feed_data_0(client):
    """Test case for create_raw_webhook_feed_data_0

    Send arbitrary data to a feed via webhook URL.
    """
    headers = { 
        'Accept': 'application/json',
        'HeaderSignature': 'special-key',
        'QueryKey': 'special-key',
        'HeaderKey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v2/webhooks/feed/:token/raw',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_create_webhook_feed_data_0(client):
    """Test case for create_webhook_feed_data_0

    Send data to a feed via webhook URL.
    """
    payload = openapi_server.CreateWebhookFeedDataRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'HeaderSignature': 'special-key',
        'QueryKey': 'special-key',
        'HeaderKey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v2/webhooks/feed/:token',
        headers=headers,
        json=payload,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_destroy_data(client):
    """Test case for destroy_data

    Delete existing Data
    """
    headers = { 
        'Accept': 'application/json',
        'HeaderSignature': 'special-key',
        'QueryKey': 'special-key',
        'HeaderKey': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v2/{username}/feeds/{feed_key}/data/{id}'.format(username='username_example', feed_key='feed_key_example', id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_first_data(client):
    """Test case for first_data

    First Data in Queue
    """
    params = [('include', 'include_example')]
    headers = { 
        'Accept': 'application/json',
        'HeaderSignature': 'special-key',
        'QueryKey': 'special-key',
        'HeaderKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/{username}/feeds/{feed_key}/data/first'.format(username='username_example', feed_key='feed_key_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_data(client):
    """Test case for get_data

    Returns data based on feed key
    """
    params = [('include', 'include_example')]
    headers = { 
        'Accept': 'application/json',
        'HeaderSignature': 'special-key',
        'QueryKey': 'special-key',
        'HeaderKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/{username}/feeds/{feed_key}/data/{id}'.format(username='username_example', feed_key='feed_key_example', id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_last_data(client):
    """Test case for last_data

    Last Data in Queue
    """
    params = [('include', 'include_example')]
    headers = { 
        'Accept': 'application/json',
        'HeaderSignature': 'special-key',
        'QueryKey': 'special-key',
        'HeaderKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/{username}/feeds/{feed_key}/data/last'.format(username='username_example', feed_key='feed_key_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_next_data(client):
    """Test case for next_data

    Next Data in Queue
    """
    params = [('include', 'include_example')]
    headers = { 
        'Accept': 'application/json',
        'HeaderSignature': 'special-key',
        'QueryKey': 'special-key',
        'HeaderKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/{username}/feeds/{feed_key}/data/next'.format(username='username_example', feed_key='feed_key_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_previous_data(client):
    """Test case for previous_data

    Previous Data in Queue
    """
    params = [('include', 'include_example')]
    headers = { 
        'Accept': 'application/json',
        'HeaderSignature': 'special-key',
        'QueryKey': 'special-key',
        'HeaderKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/{username}/feeds/{feed_key}/data/previous'.format(username='username_example', feed_key='feed_key_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_replace_data(client):
    """Test case for replace_data

    Replace existing Data
    """
    datum = openapi_server.CreateDataRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'HeaderSignature': 'special-key',
        'QueryKey': 'special-key',
        'HeaderKey': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v2/{username}/feeds/{feed_key}/data/{id}'.format(username='username_example', feed_key='feed_key_example', id='id_example'),
        headers=headers,
        json=datum,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_retain_data(client):
    """Test case for retain_data

    Last Data in MQTT CSV format
    """
    headers = { 
        'Accept': 'text/csv',
        'HeaderSignature': 'special-key',
        'QueryKey': 'special-key',
        'HeaderKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/{username}/feeds/{feed_key}/data/retain'.format(username='username_example', feed_key='feed_key_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_update_data(client):
    """Test case for update_data

    Update properties of existing Data
    """
    datum = openapi_server.CreateDataRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'HeaderSignature': 'special-key',
        'QueryKey': 'special-key',
        'HeaderKey': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/v2/{username}/feeds/{feed_key}/data/{id}'.format(username='username_example', feed_key='feed_key_example', id='id_example'),
        headers=headers,
        json=datum,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

