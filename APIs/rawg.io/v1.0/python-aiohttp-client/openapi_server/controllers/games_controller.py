from typing import List, Dict
from aiohttp import web

from openapi_server.models.game_single import GameSingle
from openapi_server.models.games_development_team_list200_response import GamesDevelopmentTeamList200Response
from openapi_server.models.games_list200_response import GamesList200Response
from openapi_server.models.games_screenshots_list200_response import GamesScreenshotsList200Response
from openapi_server.models.games_stores_list200_response import GamesStoresList200Response
from openapi_server.models.movie import Movie
from openapi_server.models.parent_achievement import ParentAchievement
from openapi_server.models.reddit import Reddit
from openapi_server.models.twitch import Twitch
from openapi_server.models.youtube import Youtube
from openapi_server import util


async def games_achievements_read(request: web.Request, id) -> web.Response:
    """Get a list of game achievements.

    

    :param id: An ID or a slug identifying this Game.
    :type id: str

    """
    return web.Response(status=200)


async def games_additions_list(request: web.Request, game_pk, page=None, page_size=None) -> web.Response:
    """Get a list of DLC&#39;s for the game, GOTY and other editions, companion apps, etc.

    

    :param game_pk: 
    :type game_pk: str
    :param page: A page number within the paginated result set.
    :type page: int
    :param page_size: Number of results to return per page.
    :type page_size: int

    """
    return web.Response(status=200)


async def games_development_team_list(request: web.Request, game_pk, ordering=None, page=None, page_size=None) -> web.Response:
    """Get a list of individual creators that were part of the development team.

    

    :param game_pk: 
    :type game_pk: str
    :param ordering: Which field to use when ordering the results.
    :type ordering: str
    :param page: A page number within the paginated result set.
    :type page: int
    :param page_size: Number of results to return per page.
    :type page_size: int

    """
    return web.Response(status=200)


async def games_game_series_list(request: web.Request, game_pk, page=None, page_size=None) -> web.Response:
    """Get a list of games that are part of the same series.

    

    :param game_pk: 
    :type game_pk: str
    :param page: A page number within the paginated result set.
    :type page: int
    :param page_size: Number of results to return per page.
    :type page_size: int

    """
    return web.Response(status=200)


async def games_list(request: web.Request, page=None, page_size=None, search=None, search_precise=None, search_exact=None, parent_platforms=None, platforms=None, stores=None, developers=None, publishers=None, genres=None, tags=None, creators=None, dates=None, updated=None, platforms_count=None, metacritic=None, exclude_collection=None, exclude_additions=None, exclude_parents=None, exclude_game_series=None, exclude_stores=None, ordering=None) -> web.Response:
    """Get a list of games.

    

    :param page: A page number within the paginated result set.
    :type page: int
    :param page_size: Number of results to return per page.
    :type page_size: int
    :param search: Search query.
    :type search: str
    :param search_precise: Disable fuzziness for the search query.
    :type search_precise: bool
    :param search_exact: Mark the search query as exact.
    :type search_exact: bool
    :param parent_platforms: Filter by parent platforms, for example: &#x60;1,2,3&#x60;.
    :type parent_platforms: str
    :param platforms: Filter by platforms, for example: &#x60;4,5&#x60;.
    :type platforms: str
    :param stores: Filter by stores, for example: &#x60;5,6&#x60;.
    :type stores: str
    :param developers: Filter by developers, for example: &#x60;1612,18893&#x60; or &#x60;valve-software,feral-interactive&#x60;.
    :type developers: str
    :param publishers: Filter by publishers, for example: &#x60;354,20987&#x60; or &#x60;electronic-arts,microsoft-studios&#x60;.
    :type publishers: str
    :param genres: Filter by genres, for example: &#x60;4,51&#x60; or &#x60;action,indie&#x60;.
    :type genres: str
    :param tags: Filter by tags, for example: &#x60;31,7&#x60; or &#x60;singleplayer,multiplayer&#x60;.
    :type tags: str
    :param creators: Filter by creators, for example: &#x60;78,28&#x60; or &#x60;cris-velasco,mike-morasky&#x60;.
    :type creators: str
    :param dates: Filter by a release date, for example: &#x60;2010-01-01,2018-12-31.1960-01-01,1969-12-31&#x60;.
    :type dates: str
    :param updated: Filter by an update date, for example: &#x60;2020-12-01,2020-12-31&#x60;.
    :type updated: str
    :param platforms_count: Filter by platforms count, for example: &#x60;1&#x60;.
    :type platforms_count: int
    :param metacritic: Filter by a metacritic rating, for example: &#x60;80,100&#x60;.
    :type metacritic: str
    :param exclude_collection: Exclude games from a particular collection, for example: &#x60;123&#x60;.
    :type exclude_collection: int
    :param exclude_additions: Exclude additions.
    :type exclude_additions: bool
    :param exclude_parents: Exclude games which have additions.
    :type exclude_parents: bool
    :param exclude_game_series: Exclude games which included in a game series.
    :type exclude_game_series: bool
    :param exclude_stores: Exclude stores, for example: &#x60;5,6&#x60;.
    :type exclude_stores: str
    :param ordering: Available fields: &#x60;name&#x60;, &#x60;released&#x60;, &#x60;added&#x60;, &#x60;created&#x60;, &#x60;updated&#x60;, &#x60;rating&#x60;, &#x60;metacritic&#x60;. You can reverse the sort order adding a hyphen, for example: &#x60;-released&#x60;.
    :type ordering: str

    """
    return web.Response(status=200)


async def games_movies_read(request: web.Request, id) -> web.Response:
    """Get a list of game trailers.

    

    :param id: An ID or a slug identifying this Game.
    :type id: str

    """
    return web.Response(status=200)


async def games_parent_games_list(request: web.Request, game_pk, page=None, page_size=None) -> web.Response:
    """Get a list of parent games for DLC&#39;s and editions.

    

    :param game_pk: 
    :type game_pk: str
    :param page: A page number within the paginated result set.
    :type page: int
    :param page_size: Number of results to return per page.
    :type page_size: int

    """
    return web.Response(status=200)


async def games_read(request: web.Request, id) -> web.Response:
    """Get details of the game.

    

    :param id: An ID or a slug identifying this Game.
    :type id: str

    """
    return web.Response(status=200)


async def games_reddit_read(request: web.Request, id) -> web.Response:
    """Get a list of most recent posts from the game&#39;s subreddit.

    

    :param id: An ID or a slug identifying this Game.
    :type id: str

    """
    return web.Response(status=200)


async def games_screenshots_list(request: web.Request, game_pk, ordering=None, page=None, page_size=None) -> web.Response:
    """Get screenshots for the game.

    

    :param game_pk: 
    :type game_pk: str
    :param ordering: Which field to use when ordering the results.
    :type ordering: str
    :param page: A page number within the paginated result set.
    :type page: int
    :param page_size: Number of results to return per page.
    :type page_size: int

    """
    return web.Response(status=200)


async def games_stores_list(request: web.Request, game_pk, ordering=None, page=None, page_size=None) -> web.Response:
    """Get links to the stores that sell the game.

    

    :param game_pk: 
    :type game_pk: str
    :param ordering: Which field to use when ordering the results.
    :type ordering: str
    :param page: A page number within the paginated result set.
    :type page: int
    :param page_size: Number of results to return per page.
    :type page_size: int

    """
    return web.Response(status=200)


async def games_suggested_read(request: web.Request, id) -> web.Response:
    """Get a list of visually similar games, available only for business and enterprise API users.

    

    :param id: An ID or a slug identifying this Game.
    :type id: str

    """
    return web.Response(status=200)


async def games_twitch_read(request: web.Request, id) -> web.Response:
    """Get streams on Twitch associated with the game, available only for business and enterprise API users.

    

    :param id: An ID or a slug identifying this Game.
    :type id: str

    """
    return web.Response(status=200)


async def games_youtube_read(request: web.Request, id) -> web.Response:
    """Get videos from YouTube associated with the game, available only for business and enterprise API users.

    

    :param id: An ID or a slug identifying this Game.
    :type id: str

    """
    return web.Response(status=200)
