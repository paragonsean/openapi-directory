# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.download_history_data_list import DownloadHistoryDataList
from openapi_server.models.editorial_category_results import EditorialCategoryResults
from openapi_server.models.editorial_content import EditorialContent
from openapi_server.models.editorial_content_data_list import EditorialContentDataList
from openapi_server.models.editorial_image_category_results import EditorialImageCategoryResults
from openapi_server.models.editorial_image_content_data_list import EditorialImageContentDataList
from openapi_server.models.editorial_image_livefeed import EditorialImageLivefeed
from openapi_server.models.editorial_image_livefeed_list import EditorialImageLivefeedList
from openapi_server.models.editorial_livefeed import EditorialLivefeed
from openapi_server.models.editorial_livefeed_list import EditorialLivefeedList
from openapi_server.models.editorial_search_results import EditorialSearchResults
from openapi_server.models.editorial_updated_results import EditorialUpdatedResults
from openapi_server.models.license_editorial_content_request import LicenseEditorialContentRequest
from openapi_server.models.license_editorial_content_results import LicenseEditorialContentResults


pytestmark = pytest.mark.asyncio

async def test_get_editorial_categories(client):
    """Test case for get_editorial_categories

    (Deprecated) List editorial categories
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v2/editorial/categories',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_editorial_image(client):
    """Test case for get_editorial_image

    Get editorial content details
    """
    params = [('country', 'USA')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v2/editorial/images/{id}'.format(id='9926131a'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_editorial_image_license_list(client):
    """Test case for get_editorial_image_license_list

    List editorial image licenses
    """
    params = [('image_id', '12345678'),
                    ('license', 'premier_editorial_all_digital'),
                    ('page', 1),
                    ('per_page', 20),
                    ('sort', newest),
                    ('username', 'aUniqueUsername'),
                    ('start_date', '2021-03-29T13:25:13.521Z'),
                    ('end_date', '2021-03-29T13:25:13.521Z'),
                    ('download_availability', all),
                    ('team_history', False)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v2/editorial/images/licenses',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_editorial_image_livefeed(client):
    """Test case for get_editorial_image_livefeed

    Get editorial livefeed
    """
    params = [('country', 'USA')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v2/editorial/images/livefeeds/{id}'.format(id='2018%2F10%2F15%2FWomen%20of%20the%20Year%20Lunch%20%26%20Awards%2C%20London'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_editorial_image_livefeed_items(client):
    """Test case for get_editorial_image_livefeed_items

    Get editorial livefeed items
    """
    params = [('country', 'USA')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v2/editorial/images/livefeeds/{id}/items'.format(id='2018%2F10%2F15%2FWomen%20of%20the%20Year%20Lunch%20%26%20Awards%2C%20London'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_editorial_image_livefeed_list(client):
    """Test case for get_editorial_image_livefeed_list

    Get editorial livefeed list
    """
    params = [('country', 'USA'),
                    ('page', 1),
                    ('per_page', 20)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v2/editorial/images/livefeeds',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_editorial_livefeed(client):
    """Test case for get_editorial_livefeed

    (Deprecated) Get editorial livefeed
    """
    params = [('country', 'USA')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v2/editorial/livefeeds/{id}'.format(id='2018%2F10%2F15%2FWomen%20of%20the%20Year%20Lunch%20%26%20Awards%2C%20London'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_editorial_livefeed_items(client):
    """Test case for get_editorial_livefeed_items

    (Deprecated) Get editorial livefeed items
    """
    params = [('country', 'USA')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v2/editorial/livefeeds/{id}/items'.format(id='2018%2F10%2F15%2FWomen%20of%20the%20Year%20Lunch%20%26%20Awards%2C%20London'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_editorial_livefeed_list(client):
    """Test case for get_editorial_livefeed_list

    (Deprecated) Get editorial livefeed list
    """
    params = [('country', 'USA'),
                    ('page', 1),
                    ('per_page', 20)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v2/editorial/livefeeds',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_updated_editorial_image(client):
    """Test case for get_updated_editorial_image

    (Deprecated) List updated content
    """
    params = [('type', 'edit'),
                    ('date_updated_start', '2021-03-29T13:25:13.521Z'),
                    ('date_updated_end', '2021-03-29T13:25:13.521Z'),
                    ('date_taken_start', '2020-02-04'),
                    ('date_taken_end', '2020-02-05'),
                    ('cursor', 'eyJ2IjoxLCJzIjoyfQ=='),
                    ('sort', newest),
                    ('supplier_code', ['ABC']),
                    ('country', 'USA'),
                    ('per_page', 500)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v2/editorial/updated',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_updated_editorial_images(client):
    """Test case for get_updated_editorial_images

    List updated content
    """
    params = [('type', 'edit'),
                    ('date_updated_start', '2021-03-29T13:25:13.521Z'),
                    ('date_updated_end', '2021-03-29T13:25:13.521Z'),
                    ('date_taken_start', '2020-02-04'),
                    ('date_taken_end', '2020-02-05'),
                    ('cursor', 'eyJ2IjoxLCJzIjoyfQ=='),
                    ('sort', newest),
                    ('supplier_code', ['ABC']),
                    ('country', 'USA'),
                    ('per_page', 500)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v2/editorial/images/updated',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_license_editorial_image(client):
    """Test case for license_editorial_image

    (Deprecated) License editorial content
    """
    body = {"country":"USA","editorial":[{"editorial_id":"10687730b","license":"premier_editorial_comp","metadata":{"customer_id":"12345","geo_location":"US","number_viewed":"15","search_term":"dog"},"size":"original"}]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v2/editorial/licenses',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_license_editorial_images(client):
    """Test case for license_editorial_images

    License editorial content
    """
    body = {"country":"USA","editorial":[{"editorial_id":"10687730b","license":"premier_editorial_comp","metadata":{"customer_id":"12345","geo_location":"US","number_viewed":"15","search_term":"dog"},"size":"original"}]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v2/editorial/images/licenses',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_editorial_image_categories(client):
    """Test case for list_editorial_image_categories

    List editorial categories
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v2/editorial/images/categories',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_search_editorial(client):
    """Test case for search_editorial

    (Deprecated) Search editorial content
    """
    params = [('query', 'query_example'),
                    ('sort', relevant),
                    ('category', 'category_example'),
                    ('country', 'USA'),
                    ('supplier_code', ['supplier_code_example']),
                    ('date_start', '2013-10-20'),
                    ('date_end', '2013-10-20'),
                    ('per_page', 20),
                    ('cursor', 'cursor_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v2/editorial/search',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_search_editorial_images(client):
    """Test case for search_editorial_images

    Search editorial images
    """
    params = [('query', 'The Academy Awards'),
                    ('sort', relevant),
                    ('category', 'Alone,Performing'),
                    ('country', 'USA'),
                    ('supplier_code', ['supplier_code_example']),
                    ('date_start', '2020-05-29'),
                    ('date_end', '2021-05-29'),
                    ('per_page', 20),
                    ('cursor', 'eyJ2IjoxLCJzIjoxfQ==')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v2/editorial/images/search',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_v2_editorial_id_get(client):
    """Test case for v2_editorial_id_get

    (Deprecated) Get editorial content details
    """
    params = [('country', 'USA'),
                    ('search_id', '00000000-0000-0000-0000-000000000000')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v2/editorial/{id}'.format(id='9926131a'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

