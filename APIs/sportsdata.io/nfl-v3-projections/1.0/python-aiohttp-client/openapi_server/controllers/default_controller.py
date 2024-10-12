from typing import List, Dict
from aiohttp import web

from openapi_server.models.dfs_slate import DfsSlate
from openapi_server.models.dfs_slate_with_ownership_projection import DfsSlateWithOwnershipProjection
from openapi_server.models.fantasy_defense_game_projection import FantasyDefenseGameProjection
from openapi_server.models.fantasy_defense_season_projection import FantasyDefenseSeasonProjection
from openapi_server.models.player import Player
from openapi_server.models.player_game_projection import PlayerGameProjection
from openapi_server.models.player_season_projection import PlayerSeasonProjection
from openapi_server import util


async def dfs_slate_ownership_projections_by_slateid(request: web.Request, format, slate_id) -> web.Response:
    """DFS Slate Ownership Projections by SlateID

    Slate Ownership Projections for a specific slate. Projections are for GPP format ownership. Will return an empty list if the slate is not yet projected or not a slate we have projections for.

    :param format: Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;.
    :type format: str
    :param slate_id: SlateID of the DFS Slate you wish to get ownership projections for. Will have an empty SlateOwnershipProjections if this slate was not projected
    :type slate_id: str

    """
    return web.Response(status=200)


async def dfs_slates_by_date(request: web.Request, format, _date) -> web.Response:
    """DFS Slates by Date

    

    :param format: Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;.
    :type format: str
    :param _date: The date of the slates. &lt;br&gt;Examples: &lt;code&gt;2017-SEP-25&lt;/code&gt;, &lt;code&gt;2017-10-31&lt;/code&gt;.
    :type _date: str

    """
    return web.Response(status=200)


async def dfs_slates_by_week(request: web.Request, format, season, week) -> web.Response:
    """DFS Slates by Week

    

    :param format: Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;.
    :type format: str
    :param season: Year of the season and the season type. If no season type is provided, then the default is regular season.           &lt;br&gt;Examples: &lt;code&gt;2015REG&lt;/code&gt;, &lt;code&gt;2015PRE&lt;/code&gt;, &lt;code&gt;2015POST&lt;/code&gt;
    :type season: str
    :param week: Week of the season. Valid values are as follows: Preseason 0 to 4, Regular Season 1 to 17, Postseason 1 to 4.           Example: &lt;code&gt;1&lt;/code&gt;
    :type week: str

    """
    return web.Response(status=200)


async def idp_projected_player_game_stats_by_player_w_injuries_lineups_dfs_salaries(request: web.Request, format, season, week, playerid) -> web.Response:
    """IDP Projected Player Game Stats by Player (w/ Injuries, Lineups, DFS Salaries)

    

    :param format: Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;.
    :type format: str
    :param season: Year of the season and the season type. If no season type is provided, then the default is regular season.           &lt;br&gt;Examples: &lt;code&gt;2015REG&lt;/code&gt;, &lt;code&gt;2015PRE&lt;/code&gt;, &lt;code&gt;2015POST&lt;/code&gt;.         
    :type season: str
    :param week: Week of the season. Valid values are as follows: Preseason 0 to 4, Regular Season 1 to 17, Postseason 1 to 4.           Example: &lt;code&gt;1&lt;/code&gt;         
    :type week: str
    :param playerid: Each NFL player has a unique ID assigned by FantasyData. Player IDs can be determined by pulling player related data. Example:&lt;code&gt;14257&lt;/code&gt;.
    :type playerid: str

    """
    return web.Response(status=200)


async def idp_projected_player_game_stats_by_team_w_injuries_lineups_dfs_salaries(request: web.Request, format, season, week, team) -> web.Response:
    """IDP Projected Player Game Stats by Team (w/ Injuries, Lineups, DFS Salaries)

    

    :param format: Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;.
    :type format: str
    :param season: Year of the season and the season type. If no season type is provided, then the default is regular season.           &lt;br&gt;Examples: &lt;code&gt;2015REG&lt;/code&gt;, &lt;code&gt;2015PRE&lt;/code&gt;, &lt;code&gt;2015POST&lt;/code&gt;.         
    :type season: str
    :param week: Week of the season. Valid values are as follows: Preseason 0 to 4, Regular Season 1 to 17, Postseason 1 to 4.           Example: &lt;code&gt;1&lt;/code&gt;         
    :type week: str
    :param team: Abbreviation of the team. Example: &lt;code&gt;WAS&lt;/code&gt;.
    :type team: str

    """
    return web.Response(status=200)


async def idp_projected_player_game_stats_by_week_w_injuries_lineups_dfs_salaries(request: web.Request, format, season, week) -> web.Response:
    """IDP Projected Player Game Stats by Week (w/ Injuries, Lineups, DFS Salaries)

    

    :param format: Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;.
    :type format: str
    :param season: Year of the season and the season type. If no season type is provided, then the default is regular season.           &lt;br&gt;Examples: &lt;code&gt;2015REG&lt;/code&gt;, &lt;code&gt;2015PRE&lt;/code&gt;, &lt;code&gt;2015POST&lt;/code&gt;.         
    :type season: str
    :param week: Week of the season. Valid values are as follows: Preseason 0 to 4, Regular Season 1 to 17, Postseason 1 to 4.           Example: &lt;code&gt;1&lt;/code&gt;         
    :type week: str

    """
    return web.Response(status=200)


async def injured_players(request: web.Request, format) -> web.Response:
    """Injured Players

    This endpoint provides all currently injured NFL players, along with injury details.

    :param format: Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;.
    :type format: str

    """
    return web.Response(status=200)


async def projected_fantasy_defense_game_stats_w_dfs_salaries(request: web.Request, format, season, week) -> web.Response:
    """Projected Fantasy Defense Game Stats (w/ DFS Salaries)

    

    :param format: Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;.
    :type format: str
    :param season: Year of the season and the season type. If no season type is provided, then the default is regular season.           &lt;br&gt;Examples: &lt;code&gt;2015REG&lt;/code&gt;, &lt;code&gt;2015PRE&lt;/code&gt;, &lt;code&gt;2015POST&lt;/code&gt;.         
    :type season: str
    :param week: Week of the season. Valid values are as follows: Preseason 0 to 4, Regular Season 1 to 17, Postseason 1 to 4.           Example: &lt;code&gt;1&lt;/code&gt;         
    :type week: str

    """
    return web.Response(status=200)


async def projected_fantasy_defense_season_stats_w_adp(request: web.Request, format, season) -> web.Response:
    """Projected Fantasy Defense Season Stats (w/ ADP)

    

    :param format: Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;.
    :type format: str
    :param season: Year of the season and the season type. If no season type is provided, then the default is regular season.           &lt;br&gt;Examples: &lt;code&gt;2015REG&lt;/code&gt;, &lt;code&gt;2015PRE&lt;/code&gt;, &lt;code&gt;2015POST&lt;/code&gt;.         
    :type season: str

    """
    return web.Response(status=200)


async def projected_player_game_stats_by_player_w_injuries_lineups_dfs_salaries(request: web.Request, format, season, week, playerid) -> web.Response:
    """Projected Player Game Stats by Player (w/ Injuries, Lineups, DFS Salaries)

    

    :param format: Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;.
    :type format: str
    :param season: Year of the season and the season type. If no season type is provided, then the default is regular season.           &lt;br&gt;Examples: &lt;code&gt;2015REG&lt;/code&gt;, &lt;code&gt;2015PRE&lt;/code&gt;, &lt;code&gt;2015POST&lt;/code&gt;.         
    :type season: str
    :param week:            Week of the season. Valid values are as follows: Preseason 0 to 4, Regular Season 1 to 17, Postseason 1 to 4.           Example: &lt;code&gt;1&lt;/code&gt;         
    :type week: str
    :param playerid: Each NFL player has a unique ID assigned by FantasyData. Player IDs can be determined by pulling player related data. Example:&lt;code&gt;14257&lt;/code&gt;.
    :type playerid: str

    """
    return web.Response(status=200)


async def projected_player_game_stats_by_team_w_injuries_lineups_dfs_salaries(request: web.Request, format, season, week, team) -> web.Response:
    """Projected Player Game Stats by Team (w/ Injuries, Lineups, DFS Salaries)

    

    :param format: Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;.
    :type format: str
    :param season: Year of the season and the season type. If no season type is provided, then the default is regular season.           &lt;br&gt;Examples: &lt;code&gt;2015REG&lt;/code&gt;, &lt;code&gt;2015PRE&lt;/code&gt;, &lt;code&gt;2015POST&lt;/code&gt;.         
    :type season: str
    :param week: Week of the season. Valid values are as follows: Preseason 0 to 4, Regular Season 1 to 17, Postseason 1 to 4.           Example: &lt;code&gt;1&lt;/code&gt;         
    :type week: str
    :param team: Abbreviation of the team. Example: &lt;code&gt;WAS&lt;/code&gt;.
    :type team: str

    """
    return web.Response(status=200)


async def projected_player_game_stats_by_week_w_injuries_lineups_dfs_salaries(request: web.Request, format, season, week) -> web.Response:
    """Projected Player Game Stats by Week (w/ Injuries, Lineups, DFS Salaries)

    

    :param format: Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;.
    :type format: str
    :param season: Year of the season and the season type. If no season type is provided, then the default is regular season.           &lt;br&gt;Examples: &lt;code&gt;2015REG&lt;/code&gt;, &lt;code&gt;2015PRE&lt;/code&gt;, &lt;code&gt;2015POST&lt;/code&gt;.         
    :type season: str
    :param week:            Week of the season. Valid values are as follows: Preseason 0 to 4, Regular Season 1 to 17, Postseason 1 to 4.           Example: &lt;code&gt;1&lt;/code&gt;         
    :type week: str

    """
    return web.Response(status=200)


async def projected_player_season_stats_by_player_w_adp(request: web.Request, format, season, playerid) -> web.Response:
    """Projected Player Season Stats by Player (w/ ADP)

    

    :param format: Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;.
    :type format: str
    :param season: Year of the season and the season type. If no season type is provided, then the default is regular season.           &lt;br&gt;Examples: &lt;code&gt;2015REG&lt;/code&gt;, &lt;code&gt;2015PRE&lt;/code&gt;, &lt;code&gt;2015POST&lt;/code&gt;.         
    :type season: str
    :param playerid: Each NFL player has a unique ID assigned by FantasyData. Player IDs can be determined by pulling player related data. Example:&lt;code&gt;14257&lt;/code&gt;.
    :type playerid: str

    """
    return web.Response(status=200)


async def projected_player_season_stats_by_team_w_adp(request: web.Request, format, season, team) -> web.Response:
    """Projected Player Season Stats by Team (w/ ADP)

    

    :param format: Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;.
    :type format: str
    :param season: Year of the season and the season type. If no season type is provided, then the default is regular season.           &lt;br&gt;Examples: &lt;code&gt;2015REG&lt;/code&gt;, &lt;code&gt;2015PRE&lt;/code&gt;, &lt;code&gt;2015POST&lt;/code&gt;.         
    :type season: str
    :param team: Abbreviation of the team. Example: &lt;code&gt;WAS&lt;/code&gt;.
    :type team: str

    """
    return web.Response(status=200)


async def projected_player_season_stats_w_adp(request: web.Request, format, season) -> web.Response:
    """Projected Player Season Stats (w/ ADP)

    

    :param format: Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;.
    :type format: str
    :param season: Year of the season and the season type. If no season type is provided, then the default is regular season.           &lt;br&gt;Examples: &lt;code&gt;2015REG&lt;/code&gt;, &lt;code&gt;2015PRE&lt;/code&gt;, &lt;code&gt;2015POST&lt;/code&gt;.         
    :type season: str

    """
    return web.Response(status=200)


async def upcoming_dfs_slate_ownership_projections(request: web.Request, format) -> web.Response:
    """Upcoming DFS Slate Ownership Projections

    Grabs DFS Slates which have not yet started for which we have DFS Ownership projections. 

    :param format: Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;.
    :type format: str

    """
    return web.Response(status=200)
