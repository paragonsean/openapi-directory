# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.aggregation_audio_item_list_document import AggregationAudioItemListDocument
from openapi_server.models.audio_item_list_document import AudioItemListDocument
from openapi_server.models.channels_document import ChannelsDocument
from openapi_server.models.error_document import ErrorDocument
from openapi_server.models.organization_category_audio_list_document import OrganizationCategoryAudioListDocument
from openapi_server.models.organization_overview_document import OrganizationOverviewDocument
from openapi_server.models.rating_data import RatingData
from openapi_server.models.search_list_document import SearchListDocument


pytestmark = pytest.mark.asyncio

async def test_get_agg_recommendations(client):
    """Test case for get_agg_recommendations

    Get a set of recommendations for an aggregation independent of the user's listening history
    """
    params = [('startNum', 0)]
    headers = { 
        'Accept': 'application/json',
        'authorization': 'authorization_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v2/aggregation/{agg_id}/recommendations'.format(agg_id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_channels(client):
    """Test case for get_channels

    Get the list of available channels
    """
    params = [('exploreOnly', False)]
    headers = { 
        'Accept': 'application/json',
        'authorization': 'authorization_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v2/channels',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_history(client):
    """Test case for get_history

    Get recent ratings the logged-in user has submitted
    """
    headers = { 
        'Accept': 'application/json',
        'authorization': 'authorization_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v2/history',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_organization_category(client):
    """Test case for get_organization_category

    Get a list of recommendations from a category of content from an organization
    """
    headers = { 
        'Accept': 'application/json',
        'authorization': 'authorization_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v2/organizations/{org_id}/categories/{category}/recommendations'.format(org_id=56, category=story),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_organization_overview(client):
    """Test case for get_organization_overview

    Get a variety of details about an organization including various lists of recent audio items
    """
    headers = { 
        'Accept': 'application/json',
        'authorization': 'authorization_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v2/organizations/{org_id}/recommendations'.format(org_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_promo(client):
    """Test case for get_promo

    Retrieve the most recent promo audio heard by the logged-in user
    """
    headers = { 
        'Accept': 'application/json',
        'authorization': 'authorization_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v2/promo/recommendations',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_recommendations(client):
    """Test case for get_recommendations

    Get a list of media for the logged-in user from NPR's recommendation engine
    """
    params = [('channel', npr),
                    ('sharedMediaId', 'shared_media_id_example'),
                    ('notifiedMediaId', 'notified_media_id_example')]
    headers = { 
        'Accept': 'application/json',
        'authorization': 'authorization_example',
        'x_advertising_id': 'x_advertising_id_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v2/recommendations',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_search_recommendations(client):
    """Test case for get_search_recommendations

    Get a list of recent audio and aggregation items associated with search terms
    """
    params = [('searchTerms', 'search_terms_example')]
    headers = { 
        'Accept': 'application/json',
        'authorization': 'authorization_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v2/search/recommendations',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_rating(client):
    """Test case for post_rating

    Collect new ratings for media previously recommended to the logged-in user
    """
    body = {"duration":5636,"elapsed":2301,"origin":"origin","channel":"npr","rating":"rating","affiliations":["{}","{}"],"cohort":"cohort","mediaId":"mediaId","timestamp":"2000-01-23T04:56:07.000+00:00"}
    params = [('channel', npr),
                    ('recommend', True)]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'authorization': 'authorization_example',
        'x_advertising_id': 'x_advertising_id_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v2/ratings',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

