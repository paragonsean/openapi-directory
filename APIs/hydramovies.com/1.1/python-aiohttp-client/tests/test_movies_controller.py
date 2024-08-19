# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_current_movie_data_csv_get(client):
    """Test case for current_movie_data_csv_get

    getMovieByIMDBid
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/api-v2/%3Fsource=http:/hydramovies.com/api-v2/current-Movie-Data.csv&imdb_id={IMDBid}'.format(imd_bid='imd_bid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_current_movie_data_csv_get2(client):
    """Test case for current_movie_data_csv_get2

    getMovieByYear
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/api-v2/%3Fsource=http:/hydramovies.com/api-v2/current-Movie-Data.csv&movie_year={MovieYear}'.format(movie_year='movie_year_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

