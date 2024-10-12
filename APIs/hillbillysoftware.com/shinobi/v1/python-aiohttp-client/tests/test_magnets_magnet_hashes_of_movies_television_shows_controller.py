# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.magnets import Magnets


pytestmark = pytest.mark.asyncio

async def test_magnets_by_date_get_async(client):
    """Test case for magnets_by_date_get_async

    Gets available magnet hashes on passed date (yyyy-mm-dd).  Feature not available on free plan, please donate to be able to use this feature.
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/Magnets/ByDate/{access_token}/{_date}'.format(access_token='access_token_example', _date='_date_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_magnets_byimdb_id_get_async(client):
    """Test case for magnets_byimdb_id_get_async

    Returns list of magnet hashes for passed IMDBID.  Feature not available on free plan, please donate to be able to use this feature.
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/Magnets/ByIMDB/{access_token}/{imdb_id}'.format(access_token='access_token_example', imdb_id='imdb_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_magnets_movie_by_id_get_async(client):
    """Test case for magnets_movie_by_id_get_async

    Try and find magnet links for queried movie.  Feature not available on free plan, please donate to be able to use this feature
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/Magnets/Search/{access_token}/{query}'.format(access_token='access_token_example', query='query_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_t_v_showsearch_get(client):
    """Test case for t_v_showsearch_get

    Returns results based on query, Feature not available on free plan, please donate to be able to use this feature.
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/Magnets/TVShow/{access_token}/{tv_show}'.format(access_token='access_token_example', tv_show='tv_show_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

