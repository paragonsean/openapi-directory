# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.atom import Atom


pytestmark = pytest.mark.asyncio

async def test_a_to_z_landing_feed(client):
    """Test case for a_to_z_landing_feed

    A to Z Landing Feed
    """
    params = [('platform', 'platform_example')]
    headers = { 
        'Accept': 'application/xml',
        'apikey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/pmlsd/atoz.atom',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_a_to_z_letter_feed(client):
    """Test case for a_to_z_letter_feed

    A to Z Letter Feed
    """
    params = [('platform', 'platform_example')]
    headers = { 
        'Accept': 'application/xml',
        'apikey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/pmlsd/atoz/{start_letter_ato}'.format(start_letter='start_letter_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_a_to_z_letter_feed2(client):
    """Test case for a_to_z_letter_feed2

    A to Z Letter Feed(2)
    """
    params = [('platform', 'platform_example')]
    headers = { 
        'Accept': 'application/xml',
        'apikey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/pmlsd/atoz/{start_letter}/page-{pageno}.atom'.format(start_letter='start_letter_example', pageno=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_all_programmes_by_title(client):
    """Test case for all_programmes_by_title

    All Programmes by Title
    """
    params = [('platform', 'platform_example')]
    headers = { 
        'Accept': 'application/xml',
        'apikey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/pmlsd/categories/{category}/title.atom'.format(category='category_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_all_programmes_by_title2(client):
    """Test case for all_programmes_by_title2

    All Programmes by Title(2)
    """
    params = [('platform', 'platform_example')]
    headers = { 
        'Accept': 'application/xml',
        'apikey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/pmlsd/categories/{category}/channel/{channel}/title.atom'.format(category='category_example', channel='channel_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_all_programmes_by_title3(client):
    """Test case for all_programmes_by_title3

    All Programmes by Title(3)
    """
    params = [('platform', 'platform_example')]
    headers = { 
        'Accept': 'application/xml',
        'apikey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/pmlsd/categories/{category}/derived/ad/title.atom'.format(category='category_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_all_programmes_by_title4(client):
    """Test case for all_programmes_by_title4

    All Programmes by Title(4)
    """
    params = [('platform', 'platform_example')]
    headers = { 
        'Accept': 'application/xml',
        'apikey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/pmlsd/categories/{category}/title/page-{pageno}.atom'.format(category='category_example', pageno=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_all_programmes_by_title5(client):
    """Test case for all_programmes_by_title5

    All Programmes by Title(5)
    """
    params = [('platform', 'platform_example')]
    headers = { 
        'Accept': 'application/xml',
        'apikey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/pmlsd/categories/{category}/channel/{channel}/title/page-{pageno}.atom'.format(category='category_example', channel='channel_example', pageno=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_all_programmes_by_title6(client):
    """Test case for all_programmes_by_title6

    All Programmes by Title(6)
    """
    params = [('platform', 'platform_example')]
    headers = { 
        'Accept': 'application/xml',
        'apikey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/pmlsd/categories/{category}/derived/ad/title/page-{pageno}.atom'.format(category='category_example', pageno=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_all_programmes_by_tx_date(client):
    """Test case for all_programmes_by_tx_date

    All Programmes by TX Date
    """
    params = [('platform', 'platform_example')]
    headers = { 
        'Accept': 'application/xml',
        'apikey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/pmlsd/categories/{category_ato}'.format(category='category_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_all_programmes_by_tx_date2(client):
    """Test case for all_programmes_by_tx_date2

    All Programmes by TX Date(2)
    """
    params = [('platform', 'platform_example')]
    headers = { 
        'Accept': 'application/xml',
        'apikey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/pmlsd/categories/{category}/channel/{channel_ato}'.format(category='category_example', channel='channel_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_all_programmes_by_tx_date3(client):
    """Test case for all_programmes_by_tx_date3

    All Programmes by TX Date(3)
    """
    params = [('platform', 'platform_example')]
    headers = { 
        'Accept': 'application/xml',
        'apikey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/pmlsd/categories/{category}/derived/ad.atom'.format(category='category_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_all_programmes_by_tx_date4(client):
    """Test case for all_programmes_by_tx_date4

    All Programmes by TX Date(4)
    """
    params = [('platform', 'platform_example')]
    headers = { 
        'Accept': 'application/xml',
        'apikey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/pmlsd/categories/{category}/page-{pageno}.atom'.format(category='category_example', pageno=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_all_programmes_by_tx_date5(client):
    """Test case for all_programmes_by_tx_date5

    All Programmes by TX Date(5)
    """
    params = [('platform', 'platform_example')]
    headers = { 
        'Accept': 'application/xml',
        'apikey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/pmlsd/categories/{category}/channel/{channel}/page-{pageno}.atom'.format(category='category_example', channel='channel_example', pageno=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_all_programmes_by_tx_date6(client):
    """Test case for all_programmes_by_tx_date6

    All Programmes by TX Date(6)
    """
    params = [('platform', 'platform_example')]
    headers = { 
        'Accept': 'application/xml',
        'apikey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/pmlsd/categories/{category}/derived/ad/page-{pageno}.atom'.format(category='category_example', pageno=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_call4o_d_browse_by_date_feed(client):
    """Test case for call4o_d_browse_by_date_feed

    4oD Browse by Date Feed
    """
    params = [('platform', 'platform_example')]
    headers = { 
        'Accept': 'application/xml',
        'apikey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/pmlsd/4od/episode-list/date/{yyyy}/{mm}/{dd_ato}'.format(yyyy='yyyy_example', mm='mm_example', dd='dd_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_call4o_d_clips_catch_up_feed(client):
    """Test case for call4o_d_clips_catch_up_feed

    4oD Clips Catch Up Feed
    """
    params = [('platform', 'platform_example')]
    headers = { 
        'Accept': 'application/xml',
        'apikey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/pmlsd/4od/recently-added/videos.atom',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_call4o_d_most_popular_episodes_feed(client):
    """Test case for call4o_d_most_popular_episodes_feed

    4oD Most Popular Episodes Feed
    """
    params = [('platform', 'platform_example')]
    headers = { 
        'Accept': 'application/xml',
        'apikey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/pmlsd/4od/episode-list/popular.atom',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_call4o_d_popular_all_brands_feed(client):
    """Test case for call4o_d_popular_all_brands_feed

    4oD Popular All Brands Feed
    """
    params = [('platform', 'platform_example')]
    headers = { 
        'Accept': 'application/xml',
        'apikey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/pmlsd/brands/4od/popular.atom',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_call4o_d_popular_all_brands_feed2(client):
    """Test case for call4o_d_popular_all_brands_feed2

    4oD Popular All Brands Feed(2)
    """
    params = [('platform', 'platform_example')]
    headers = { 
        'Accept': 'application/xml',
        'apikey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/pmlsd/brands/4od/popular/page-{pageno}.atom'.format(pageno=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_call4o_d_programmes_by_title(client):
    """Test case for call4o_d_programmes_by_title

    4oD Programmes by Title
    """
    params = [('platform', 'platform_example')]
    headers = { 
        'Accept': 'application/xml',
        'apikey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/pmlsd/categories/{category}/4od/title.atom'.format(category='category_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_call4o_d_programmes_by_title2(client):
    """Test case for call4o_d_programmes_by_title2

    4oD Programmes by Title(2)
    """
    params = [('platform', 'platform_example')]
    headers = { 
        'Accept': 'application/xml',
        'apikey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/pmlsd/categories/{category}/channel/{channel}/4od/title.atom'.format(category='category_example', channel='channel_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_call4o_d_programmes_by_title3(client):
    """Test case for call4o_d_programmes_by_title3

    4oD Programmes by Title(3)
    """
    params = [('platform', 'platform_example')]
    headers = { 
        'Accept': 'application/xml',
        'apikey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/pmlsd/categories/{category}/derived/ad/4od/title.atom'.format(category='category_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_call4o_d_programmes_by_title4(client):
    """Test case for call4o_d_programmes_by_title4

    4oD Programmes by Title(4)
    """
    params = [('platform', 'platform_example')]
    headers = { 
        'Accept': 'application/xml',
        'apikey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/pmlsd/categories/{category}/4od/title/page-{pageno}.atom'.format(category='category_example', pageno=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_call4o_d_programmes_by_title5(client):
    """Test case for call4o_d_programmes_by_title5

    4oD Programmes by Title(5)
    """
    params = [('platform', 'platform_example')]
    headers = { 
        'Accept': 'application/xml',
        'apikey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/pmlsd/categories/{category}/channel/{channel}/4od/title/page-{pageno}.atom'.format(category='category_example', channel='channel_example', pageno=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_call4o_d_programmes_by_title6(client):
    """Test case for call4o_d_programmes_by_title6

    4oD Programmes by Title(6)
    """
    params = [('platform', 'platform_example')]
    headers = { 
        'Accept': 'application/xml',
        'apikey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/pmlsd/categories/{category}/derived/ad/4od/title/page-{pageno}.atom'.format(category='category_example', pageno=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_call4o_d_programmes_by_tx_date(client):
    """Test case for call4o_d_programmes_by_tx_date

    4oD Programmes by TX Date
    """
    params = [('platform', 'platform_example')]
    headers = { 
        'Accept': 'application/xml',
        'apikey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/pmlsd/categories/{category}/4od.atom'.format(category='category_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_call4o_d_programmes_by_tx_date2(client):
    """Test case for call4o_d_programmes_by_tx_date2

    4oD Programmes by TX Date(2)
    """
    params = [('platform', 'platform_example')]
    headers = { 
        'Accept': 'application/xml',
        'apikey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/pmlsd/categories/{category}/channel/{channel}/4od.atom'.format(category='category_example', channel='channel_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_call4o_d_programmes_by_tx_date3(client):
    """Test case for call4o_d_programmes_by_tx_date3

    4oD Programmes by TX Date(3)
    """
    params = [('platform', 'platform_example')]
    headers = { 
        'Accept': 'application/xml',
        'apikey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/pmlsd/categories/{category}/derived/ad/4od.atom'.format(category='category_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_call4o_d_programmes_by_tx_date4(client):
    """Test case for call4o_d_programmes_by_tx_date4

    4oD Programmes by TX Date(4)
    """
    params = [('platform', 'platform_example')]
    headers = { 
        'Accept': 'application/xml',
        'apikey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/pmlsd/categories/{category}/4od/page-{pageno}.atom'.format(category='category_example', pageno=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_call4o_d_programmes_by_tx_date5(client):
    """Test case for call4o_d_programmes_by_tx_date5

    4oD Programmes by TX Date(5)
    """
    params = [('platform', 'platform_example')]
    headers = { 
        'Accept': 'application/xml',
        'apikey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/pmlsd/categories/{category}/channel/{channel}/4od/page-{pageno}.atom'.format(category='category_example', channel='channel_example', pageno=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_call4o_d_programmes_by_tx_date6(client):
    """Test case for call4o_d_programmes_by_tx_date6

    4oD Programmes by TX Date(6)
    """
    params = [('platform', 'platform_example')]
    headers = { 
        'Accept': 'application/xml',
        'apikey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/pmlsd/categories/{category}/derived/ad/4od/page-{pageno}.atom'.format(category='category_example', pageno=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_call4o_d_title_all_brands_feed(client):
    """Test case for call4o_d_title_all_brands_feed

    4oD Title All Brands Feed
    """
    params = [('platform', 'platform_example')]
    headers = { 
        'Accept': 'application/xml',
        'apikey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/pmlsd/brands/4od.atom',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_call4o_d_title_all_brands_feed2(client):
    """Test case for call4o_d_title_all_brands_feed2

    4oD Title All Brands Feed(2)
    """
    params = [('platform', 'platform_example')]
    headers = { 
        'Accept': 'application/xml',
        'apikey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/pmlsd/brands/4od/page-{pageno}.atom'.format(pageno=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_categories_landing_feed(client):
    """Test case for categories_landing_feed

    Categories Landing Feed
    """
    params = [('platform', 'platform_example')]
    headers = { 
        'Accept': 'application/xml',
        'apikey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/pmlsd/categories.atom',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_collections_feed(client):
    """Test case for collections_feed

    Collections Feed
    """
    params = [('platform', 'platform_example')]
    headers = { 
        'Accept': 'application/xml',
        'apikey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/pmlsd/collections/{collection_name}/4od.atom'.format(collection_name='collection_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_collections_feed2(client):
    """Test case for collections_feed2

    Collections Feed(2)
    """
    params = [('platform', 'platform_example')]
    headers = { 
        'Accept': 'application/xml',
        'apikey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/pmlsd/collections/{collection_name_ato}'.format(collection_name='collection_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_flattened_collection_feed(client):
    """Test case for flattened_collection_feed

    Flattened Collection Feed
    """
    params = [('platform', 'platform_example')]
    headers = { 
        'Accept': 'application/xml',
        'apikey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/pmlsd/collections/{collection_name}/flattened/4od.atom'.format(collection_name='collection_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_flattened_collection_feed2(client):
    """Test case for flattened_collection_feed2

    Flattened Collection Feed(2)
    """
    params = [('platform', 'platform_example')]
    headers = { 
        'Accept': 'application/xml',
        'apikey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/pmlsd/collections/{collection_name}/flattened.atom'.format(collection_name='collection_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_most_popular_brands_feed(client):
    """Test case for most_popular_brands_feed

    Most Popular Brands Feed
    """
    params = [('platform', 'platform_example')]
    headers = { 
        'Accept': 'application/xml',
        'apikey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/pmlsd/categories/{category}/4od/popular.atom'.format(category='category_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_most_popular_brands_feed2(client):
    """Test case for most_popular_brands_feed2

    Most Popular Brands Feed(2)
    """
    params = [('platform', 'platform_example')]
    headers = { 
        'Accept': 'application/xml',
        'apikey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/pmlsd/categories/{category}/popular.atom'.format(category='category_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_most_popular_brands_feed3(client):
    """Test case for most_popular_brands_feed3

    Most Popular Brands Feed(3)
    """
    params = [('platform', 'platform_example')]
    headers = { 
        'Accept': 'application/xml',
        'apikey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/pmlsd/categories/{category}/channel/{channel}/4od/popular.atom'.format(category='category_example', channel='channel_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_most_popular_brands_feed4(client):
    """Test case for most_popular_brands_feed4

    Most Popular Brands Feed(4)
    """
    params = [('platform', 'platform_example')]
    headers = { 
        'Accept': 'application/xml',
        'apikey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/pmlsd/categories/{category}/derived/ad/4od/popular.atom'.format(category='category_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_most_popular_brands_feed5(client):
    """Test case for most_popular_brands_feed5

    Most Popular Brands Feed(5)
    """
    params = [('platform', 'platform_example')]
    headers = { 
        'Accept': 'application/xml',
        'apikey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/pmlsd/categories/{category}/4od/popular/page-{pageno}.atom'.format(category='category_example', pageno=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_most_popular_brands_feed6(client):
    """Test case for most_popular_brands_feed6

    Most Popular Brands Feed(6)
    """
    params = [('platform', 'platform_example')]
    headers = { 
        'Accept': 'application/xml',
        'apikey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/pmlsd/categories/{category}/popular/page-{pageno}.atom'.format(category='category_example', pageno=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_most_popular_brands_feed7(client):
    """Test case for most_popular_brands_feed7

    Most Popular Brands Feed(7)
    """
    params = [('platform', 'platform_example')]
    headers = { 
        'Accept': 'application/xml',
        'apikey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/pmlsd/categories/{category}/channel/{channel}/4od/popular/page-{pageno}.atom'.format(category='category_example', channel='channel_example', pageno=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_most_popular_brands_feed8(client):
    """Test case for most_popular_brands_feed8

    Most Popular Brands Feed(8)
    """
    params = [('platform', 'platform_example')]
    headers = { 
        'Accept': 'application/xml',
        'apikey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/pmlsd/categories/{category}/derived/ad/4od/popular/page-{pageno}.atom'.format(category='category_example', pageno=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_popular_brands_feed(client):
    """Test case for popular_brands_feed

    Popular Brands Feed
    """
    params = [('platform', 'platform_example')]
    headers = { 
        'Accept': 'application/xml',
        'apikey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/pmlsd/brands/popular.atom',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_popular_brands_feed2(client):
    """Test case for popular_brands_feed2

    Popular Brands Feed(2)
    """
    params = [('platform', 'platform_example')]
    headers = { 
        'Accept': 'application/xml',
        'apikey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/pmlsd/brands/popular/page-{pageno}.atom'.format(pageno=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_search_feed(client):
    """Test case for search_feed

    Search Feed
    """
    params = [('platform', 'platform_example'),
                    ('q', 'q_example')]
    headers = { 
        'Accept': 'application/xml',
        'apikey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/pmlsd/search.atom',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_search_feed2(client):
    """Test case for search_feed2

    Search Feed(2)
    """
    params = [('platform', 'platform_example')]
    headers = { 
        'Accept': 'application/xml',
        'apikey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/pmlsd/search/{q_ato}'.format(q='q_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_search_feed3(client):
    """Test case for search_feed3

    Search Feed(3)
    """
    params = [('platform', 'platform_example'),
                    ('q', 'q_example')]
    headers = { 
        'Accept': 'application/xml',
        'apikey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/pmlsd/search/page-{pageno}.atom'.format(pageno=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_search_feed4(client):
    """Test case for search_feed4

    Search Feed(4)
    """
    params = [('platform', 'platform_example')]
    headers = { 
        'Accept': 'application/xml',
        'apikey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/pmlsd/search/{q}/page-{pageno}.atom'.format(q='q_example', pageno=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_t_v_listings_feed(client):
    """Test case for t_v_listings_feed

    TV Listings Feed
    """
    params = [('platform', 'platform_example')]
    headers = { 
        'Accept': 'application/xml',
        'apikey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/pmlsd/tv-listings/daily/{yyyy}/{mm}/{dd_ato}'.format(yyyy='yyyy_example', mm='mm_example', dd='dd_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_t_v_listings_feed2(client):
    """Test case for t_v_listings_feed2

    TV Listings Feed(2)
    """
    params = [('platform', 'platform_example')]
    headers = { 
        'Accept': 'application/xml',
        'apikey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/pmlsd/tv-listings/daily/{yyyy}/{mm}/{dd}/{channel_ato}'.format(yyyy='yyyy_example', mm='mm_example', dd='dd_example', channel='channel_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

