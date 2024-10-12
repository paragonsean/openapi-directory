# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.personalised_radio_batch_request import PersonalisedRadioBatchRequest
from openapi_server.models.personalised_radio_error_response import PersonalisedRadioErrorResponse
from openapi_server.models.personalised_radio_request import PersonalisedRadioRequest
from openapi_server.models.personalised_radio_response import PersonalisedRadioResponse
from openapi_server.models.personalised_radio_success_response import PersonalisedRadioSuccessResponse


pytestmark = pytest.mark.asyncio

async def test_delete_personalised_radio_by_activity_type_by_id(client):
    """Test case for delete_personalised_radio_by_activity_type_by_id

    Favourite Episode or Clip
    """
    headers = { 
        'Accept': 'application/json',
        'authorization': 'Bearer OAUTH_TOKEN',
        'x_authentication_provider': 'idv5',
        'x_api_key': 'x_api_key_example',
    }
    response = await client.request(
        method='DELETE',
        path='/my/radio/favourites/{type}/{pid}'.format(type='type_example', pid='pid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_personalised_radio_follows_by_type_by_id(client):
    """Test case for delete_personalised_radio_follows_by_type_by_id

    Followed Brand or Series
    """
    headers = { 
        'Accept': 'application/json',
        'authorization': 'Bearer OAUTH_TOKEN',
        'x_authentication_provider': 'idv5',
        'x_api_key': 'x_api_key_example',
    }
    response = await client.request(
        method='DELETE',
        path='/my/radio/follows/{type}/{pid}'.format(type='type_example', pid='pid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_personalised_radio_by_activity_type_by_id(client):
    """Test case for get_personalised_radio_by_activity_type_by_id

    Favourite Episode or Clip
    """
    params = [('show_all_activity', True)]
    headers = { 
        'Accept': 'application/json',
        'authorization': 'Bearer OAUTH_TOKEN',
        'x_authentication_provider': 'idv5',
        'x_api_key': 'x_api_key_example',
    }
    response = await client.request(
        method='GET',
        path='/my/radio/favourites/{type}/{pid}'.format(type='type_example', pid='pid_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_personalised_radio_favourites(client):
    """Test case for get_personalised_radio_favourites

    Favourite Episodes and Clips
    """
    params = [('offset', 56),
                    ('limit', 56),
                    ('sort', 'sort_example'),
                    ('show_all_activity', True)]
    headers = { 
        'Accept': 'application/json',
        'authorization': 'Bearer OAUTH_TOKEN',
        'x_authentication_provider': 'idv5',
        'x_api_key': 'x_api_key_example',
    }
    response = await client.request(
        method='GET',
        path='/my/radio/favourites',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_personalised_radio_favourites_by_type(client):
    """Test case for get_personalised_radio_favourites_by_type

    Favourite Episodes and Clips by Type
    """
    params = [('sort', 'sort_example'),
                    ('show_all_activity', True),
                    ('offset', 56),
                    ('limit', 56)]
    headers = { 
        'Accept': 'application/json',
        'authorization': 'Bearer OAUTH_TOKEN',
        'x_authentication_provider': 'idv5',
        'x_api_key': 'x_api_key_example',
    }
    response = await client.request(
        method='GET',
        path='/my/radio/favourites/{type}'.format(type='type_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_personalised_radio_follows(client):
    """Test case for get_personalised_radio_follows

    Followed Brands and Series
    """
    params = [('offset', 56),
                    ('limit', 56),
                    ('sort', 'sort_example'),
                    ('show_all_activity', True)]
    headers = { 
        'Accept': 'application/json',
        'authorization': 'Bearer OAUTH_TOKEN',
        'x_authentication_provider': 'idv5',
        'x_api_key': 'x_api_key_example',
    }
    response = await client.request(
        method='GET',
        path='/my/radio/follows',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_personalised_radio_follows_by_type(client):
    """Test case for get_personalised_radio_follows_by_type

    Followed Brands or Series by Type
    """
    params = [('sort', 'sort_example'),
                    ('offset', 56),
                    ('limit', 56),
                    ('show_all_activity', True)]
    headers = { 
        'Accept': 'application/json',
        'authorization': 'Bearer OAUTH_TOKEN',
        'x_authentication_provider': 'idv5',
        'x_api_key': 'x_api_key_example',
    }
    response = await client.request(
        method='GET',
        path='/my/radio/follows/{type}'.format(type='type_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_personalised_radio_follows_by_type_by_id(client):
    """Test case for get_personalised_radio_follows_by_type_by_id

    Followed Brand or Series
    """
    headers = { 
        'Accept': 'application/json',
        'authorization': 'Bearer OAUTH_TOKEN',
        'x_authentication_provider': 'idv5',
        'x_api_key': 'x_api_key_example',
    }
    response = await client.request(
        method='GET',
        path='/my/radio/follows/{type}/{pid}'.format(type='type_example', pid='pid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_personalised_radio_plays(client):
    """Test case for get_personalised_radio_plays

    Played Episode or Clip
    """
    params = [('offset', 56),
                    ('limit', 56),
                    ('sort', 'sort_example'),
                    ('show_all_activity', True)]
    headers = { 
        'Accept': 'application/json',
        'authorization': 'Bearer OAUTH_TOKEN',
        'x_authentication_provider': 'idv5',
        'x_api_key': 'x_api_key_example',
    }
    response = await client.request(
        method='GET',
        path='/my/radio/plays',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_personalised_radio_batch(client):
    """Test case for post_personalised_radio_batch

    Favourite Episodes and Clips
    """
    body = {"added_at":"added_at","metadata":{"key":"key"},"context":"context","action":"action","id":"id","type":"type"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'authorization': 'Bearer OAUTH_TOKEN',
        'x_authentication_provider': 'idv5',
        'x_api_key': 'x_api_key_example',
    }
    response = await client.request(
        method='POST',
        path='/my/radio/favourites',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_personalised_radio_by_activity_type_by_id(client):
    """Test case for post_personalised_radio_by_activity_type_by_id

    Favourite Episode or Clip
    """
    body = {"added_at":"added_at","metadata":{"key":"key"},"context":"context","action":"action"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'authorization': 'Bearer OAUTH_TOKEN',
        'x_authentication_provider': 'idv5',
        'x_api_key': 'x_api_key_example',
    }
    response = await client.request(
        method='POST',
        path='/my/radio/favourites/{type}/{pid}'.format(type='type_example', pid='pid_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_personalised_radio_follows_batch(client):
    """Test case for post_personalised_radio_follows_batch

    Followed Brands and Series
    """
    body = {"added_at":"added_at","metadata":{"key":"key"},"context":"context","action":"action","id":"id","type":"type"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'authorization': 'Bearer OAUTH_TOKEN',
        'x_authentication_provider': 'idv5',
        'x_api_key': 'x_api_key_example',
    }
    response = await client.request(
        method='POST',
        path='/my/radio/follows',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_personalised_radio_follows_by_type_by_id(client):
    """Test case for post_personalised_radio_follows_by_type_by_id

    Followed Brand or Series
    """
    body = {"added_at":"added_at","metadata":{"key":"key"},"context":"context","action":"action"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'authorization': 'Bearer OAUTH_TOKEN',
        'x_authentication_provider': 'idv5',
        'x_api_key': 'x_api_key_example',
    }
    response = await client.request(
        method='POST',
        path='/my/radio/follows/{type}/{pid}'.format(type='type_example', pid='pid_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_put_personalised_radio_batch(client):
    """Test case for put_personalised_radio_batch

    Favourite Episodes and Clips
    """
    body = {"added_at":"added_at","metadata":{"key":"key"},"context":"context","action":"action","id":"id","type":"type"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'authorization': 'Bearer OAUTH_TOKEN',
        'x_authentication_provider': 'idv5',
        'x_api_key': 'x_api_key_example',
    }
    response = await client.request(
        method='PUT',
        path='/my/radio/favourites',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_put_personalised_radio_by_activity_type_by_id(client):
    """Test case for put_personalised_radio_by_activity_type_by_id

    Favourite Episode or Clip
    """
    body = {"added_at":"added_at","metadata":{"key":"key"},"context":"context","action":"action"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'authorization': 'Bearer OAUTH_TOKEN',
        'x_authentication_provider': 'idv5',
        'x_api_key': 'x_api_key_example',
    }
    response = await client.request(
        method='PUT',
        path='/my/radio/favourites/{type}/{pid}'.format(type='type_example', pid='pid_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_put_personalised_radio_follows_batch(client):
    """Test case for put_personalised_radio_follows_batch

    Followed Brands and Series
    """
    body = {"added_at":"added_at","metadata":{"key":"key"},"context":"context","action":"action","id":"id","type":"type"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'authorization': 'Bearer OAUTH_TOKEN',
        'x_authentication_provider': 'idv5',
        'x_api_key': 'x_api_key_example',
    }
    response = await client.request(
        method='PUT',
        path='/my/radio/follows',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_put_personalised_radio_follows_by_type_by_id(client):
    """Test case for put_personalised_radio_follows_by_type_by_id

    Followed Brand or Series
    """
    body = {"added_at":"added_at","metadata":{"key":"key"},"context":"context","action":"action"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'authorization': 'Bearer OAUTH_TOKEN',
        'x_authentication_provider': 'idv5',
        'x_api_key': 'x_api_key_example',
    }
    response = await client.request(
        method='PUT',
        path='/my/radio/follows/{type}/{pid}'.format(type='type_example', pid='pid_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

