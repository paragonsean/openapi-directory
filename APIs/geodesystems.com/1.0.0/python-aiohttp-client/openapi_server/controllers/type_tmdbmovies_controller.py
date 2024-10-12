from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def search_tmdbmovies(request: web.Request, text=None, name=None, description=None, fromdate=None, todate=None, createdate_from=None, createdate_to=None, changedate_from=None, changedate_to=None, group=None, filesuffix=None, maxlatitude=None, minlongitude=None, minlatitude=None, maxlongitude=None, max=None, skip=None, search_db_tmdbmovies_original_title=None, search_db_tmdbmovies_overview=None, search_db_tmdbmovies_budget=None, search_db_tmdbmovies_genres=None, search_db_tmdbmovies_homepage=None, search_db_tmdbmovies_movie_id=None, search_db_tmdbmovies_keywords=None, search_db_tmdbmovies_original_language=None, search_db_tmdbmovies_popularity=None, search_db_tmdbmovies_production_companies=None, search_db_tmdbmovies_production_countries=None, search_db_tmdbmovies_release_date=None, search_db_tmdbmovies_revenue=None, search_db_tmdbmovies_runtime=None, search_db_tmdbmovies_spoken_languages=None, search_db_tmdbmovies_status=None, search_db_tmdbmovies_tagline=None, search_db_tmdbmovies_title=None, search_db_tmdbmovies_vote_average=None, search_db_tmdbmovies_vote_count=None) -> web.Response:
    """Search API for &#39;Tmdb Movies&#39; entry type

    API to search for entries of type Tmdb Movies

    :param text: Search text
    :type text: str
    :param name: Search name
    :type name: str
    :param description: Search description
    :type description: str
    :param fromdate: From date
    :type fromdate: str
    :param todate: To date
    :type todate: str
    :param createdate_from: Archive create date from
    :type createdate_from: str
    :param createdate_to: Archive create date to
    :type createdate_to: str
    :param changedate_from: Archive change date from
    :type changedate_from: str
    :param changedate_to: Archive change date to
    :type changedate_to: str
    :param group: Parent entry
    :type group: str
    :param filesuffix: File suffix
    :type filesuffix: str
    :param maxlatitude: Northern bounds of search
    :type maxlatitude: float
    :param minlongitude: Western bounds of search
    :type minlongitude: float
    :param minlatitude: Southern bounds of search
    :type minlatitude: float
    :param maxlongitude: Eastern bounds of search
    :type maxlongitude: float
    :param max: Max number of results
    :type max: int
    :param skip: Number to skip
    :type skip: int
    :param search_db_tmdbmovies_original_title: Original Title
    :type search_db_tmdbmovies_original_title: str
    :param search_db_tmdbmovies_overview: Overview
    :type search_db_tmdbmovies_overview: str
    :param search_db_tmdbmovies_budget: Budget
    :type search_db_tmdbmovies_budget: float
    :param search_db_tmdbmovies_genres: Genres
    :type search_db_tmdbmovies_genres: str
    :param search_db_tmdbmovies_homepage: Homepage
    :type search_db_tmdbmovies_homepage: str
    :param search_db_tmdbmovies_movie_id: Id
    :type search_db_tmdbmovies_movie_id: str
    :param search_db_tmdbmovies_keywords: Keywords
    :type search_db_tmdbmovies_keywords: str
    :param search_db_tmdbmovies_original_language: Original Language
    :type search_db_tmdbmovies_original_language: str
    :param search_db_tmdbmovies_popularity: Popularity
    :type search_db_tmdbmovies_popularity: float
    :param search_db_tmdbmovies_production_companies: Production Companies
    :type search_db_tmdbmovies_production_companies: str
    :param search_db_tmdbmovies_production_countries: Production Countries
    :type search_db_tmdbmovies_production_countries: str
    :param search_db_tmdbmovies_release_date: Release Date
    :type search_db_tmdbmovies_release_date: str
    :param search_db_tmdbmovies_revenue: Revenue
    :type search_db_tmdbmovies_revenue: float
    :param search_db_tmdbmovies_runtime: Runtime
    :type search_db_tmdbmovies_runtime: float
    :param search_db_tmdbmovies_spoken_languages: Spoken Languages
    :type search_db_tmdbmovies_spoken_languages: str
    :param search_db_tmdbmovies_status: Status
    :type search_db_tmdbmovies_status: str
    :param search_db_tmdbmovies_tagline: Tagline
    :type search_db_tmdbmovies_tagline: str
    :param search_db_tmdbmovies_title: Title
    :type search_db_tmdbmovies_title: str
    :param search_db_tmdbmovies_vote_average: Vote Average
    :type search_db_tmdbmovies_vote_average: float
    :param search_db_tmdbmovies_vote_count: Vote Count
    :type search_db_tmdbmovies_vote_count: float

    """
    fromdate = util.deserialize_datetime(fromdate)
    todate = util.deserialize_datetime(todate)
    createdate_from = util.deserialize_datetime(createdate_from)
    createdate_to = util.deserialize_datetime(createdate_to)
    changedate_from = util.deserialize_datetime(changedate_from)
    changedate_to = util.deserialize_datetime(changedate_to)
    return web.Response(status=200)
