# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_search_tmdbmovies(client):
    """Test case for search_tmdbmovies

    Search API for 'Tmdb Movies' entry type
    """
    params = [('text', 'text_example'),
                    ('name', 'name_example'),
                    ('description', 'description_example'),
                    ('fromdate', '2013-10-20T19:20:30+01:00'),
                    ('todate', '2013-10-20T19:20:30+01:00'),
                    ('createdate.from', '2013-10-20T19:20:30+01:00'),
                    ('createdate.to', '2013-10-20T19:20:30+01:00'),
                    ('changedate.from', '2013-10-20T19:20:30+01:00'),
                    ('changedate.to', '2013-10-20T19:20:30+01:00'),
                    ('group', 'group_example'),
                    ('filesuffix', 'filesuffix_example'),
                    ('maxlatitude', 3.4),
                    ('minlongitude', 3.4),
                    ('minlatitude', 3.4),
                    ('maxlongitude', 3.4),
                    ('max', 56),
                    ('skip', 56),
                    ('search.db_tmdbmovies.original_title', 'search_db_tmdbmovies_original_title_example'),
                    ('search.db_tmdbmovies.overview', 'search_db_tmdbmovies_overview_example'),
                    ('search.db_tmdbmovies.budget', 3.4),
                    ('search.db_tmdbmovies.genres', 'search_db_tmdbmovies_genres_example'),
                    ('search.db_tmdbmovies.homepage', 'search_db_tmdbmovies_homepage_example'),
                    ('search.db_tmdbmovies.movie_id', 'search_db_tmdbmovies_movie_id_example'),
                    ('search.db_tmdbmovies.keywords', 'search_db_tmdbmovies_keywords_example'),
                    ('search.db_tmdbmovies.original_language', 'search_db_tmdbmovies_original_language_example'),
                    ('search.db_tmdbmovies.popularity', 3.4),
                    ('search.db_tmdbmovies.production_companies', 'search_db_tmdbmovies_production_companies_example'),
                    ('search.db_tmdbmovies.production_countries', 'search_db_tmdbmovies_production_countries_example'),
                    ('search.db_tmdbmovies.release_date', 'search_db_tmdbmovies_release_date_example'),
                    ('search.db_tmdbmovies.revenue', 3.4),
                    ('search.db_tmdbmovies.runtime', 3.4),
                    ('search.db_tmdbmovies.spoken_languages', 'search_db_tmdbmovies_spoken_languages_example'),
                    ('search.db_tmdbmovies.status', 'search_db_tmdbmovies_status_example'),
                    ('search.db_tmdbmovies.tagline', 'search_db_tmdbmovies_tagline_example'),
                    ('search.db_tmdbmovies.title', 'search_db_tmdbmovies_title_example'),
                    ('search.db_tmdbmovies.vote_average', 3.4),
                    ('search.db_tmdbmovies.vote_count', 3.4)]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/repository/search/type/tmdbmovies',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

