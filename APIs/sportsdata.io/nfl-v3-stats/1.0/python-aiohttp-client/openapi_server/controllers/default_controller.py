from typing import List, Dict
from aiohttp import web

from openapi_server.models.box_score import BoxScore
from openapi_server.models.box_score_v3 import BoxScoreV3
from openapi_server.models.bye import Bye
from openapi_server.models.daily_fantasy_player import DailyFantasyPlayer
from openapi_server.models.daily_fantasy_scoring import DailyFantasyScoring
from openapi_server.models.dfs_slate import DfsSlate
from openapi_server.models.fantasy_defense_game import FantasyDefenseGame
from openapi_server.models.fantasy_defense_season import FantasyDefenseSeason
from openapi_server.models.fantasy_player import FantasyPlayer
from openapi_server.models.game import Game
from openapi_server.models.injury import Injury
from openapi_server.models.news import News
from openapi_server.models.player import Player
from openapi_server.models.player_detail import PlayerDetail
from openapi_server.models.player_game import PlayerGame
from openapi_server.models.player_game_red_zone import PlayerGameRedZone
from openapi_server.models.player_info import PlayerInfo
from openapi_server.models.player_ownership import PlayerOwnership
from openapi_server.models.player_season import PlayerSeason
from openapi_server.models.player_season_red_zone import PlayerSeasonRedZone
from openapi_server.models.player_season_third_down import PlayerSeasonThirdDown
from openapi_server.models.schedule import Schedule
from openapi_server.models.score import Score
from openapi_server.models.stadium import Stadium
from openapi_server.models.standing import Standing
from openapi_server.models.team import Team
from openapi_server.models.team_game import TeamGame
from openapi_server.models.team_season import TeamSeason
from openapi_server.models.timeframe import Timeframe
from openapi_server import util


async def are_games_in_progress(request: web.Request, format) -> web.Response:
    """Are Games In Progress

    Returns &lt;code&gt;true&lt;/code&gt; if there is at least one game being played at the time of the request or &lt;code&gt;false&lt;/code&gt; if there are none.

    :param format: Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;.
    :type format: str

    """
    return web.Response(status=200)


async def box_score_by_scoreid_v(request: web.Request, format, scoreid) -> web.Response:
    """Box Score by ScoreID V3

    

    :param format: Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;.
    :type format: str
    :param scoreid: The ScoreID of the game. Possible values include: &lt;code&gt;16247&lt;/code&gt;, &lt;code&gt;16245&lt;/code&gt;, etc.
    :type scoreid: str

    """
    return web.Response(status=200)


async def box_score_v(request: web.Request, format, season, week, hometeam) -> web.Response:
    """Box Score V3

    

    :param format: Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;.
    :type format: str
    :param season: Year of the season and the season type. If no season type is provided, then the default is regular season.           &lt;br&gt;Examples: &lt;code&gt;2015REG&lt;/code&gt;, &lt;code&gt;2015PRE&lt;/code&gt;, &lt;code&gt;2015POST&lt;/code&gt;.         
    :type season: str
    :param week: Week of the season. Valid values are as follows: Preseason 0 to 4, Regular Season 1 to 17, Postseason 1 to 4.           Example: &lt;code&gt;1&lt;/code&gt;         
    :type week: str
    :param hometeam: Abbreviation of a team playing in this game. Example: &lt;code&gt;WAS&lt;/code&gt;.
    :type hometeam: str

    """
    return web.Response(status=200)


async def box_scores_delta_v(request: web.Request, format, season, week, playerstoinclude, minutes) -> web.Response:
    """Box Scores Delta V3

    This method returns all box scores for a given season and week, but only returns player stats that have changed in the last X minutes. You can also filter by type of player stats to include, such as traditional fantasy players, IDP players or all players.

    :param format: Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;.
    :type format: str
    :param season: Year of the season and the season type. If no season type is provided, then the default is regular season.           &lt;br&gt;Examples: &lt;code&gt;2015REG&lt;/code&gt;, &lt;code&gt;2015PRE&lt;/code&gt;, &lt;code&gt;2015POST&lt;/code&gt;.         
    :type season: str
    :param week: Week of the season. Valid values are as follows: Preseason 0 to 4, Regular Season 1 to 17, Postseason 1 to 4.           Example: &lt;code&gt;1&lt;/code&gt;         
    :type week: str
    :param playerstoinclude: The subcategory of players to include in the returned PlayerGame records. Possible values include:&lt;br&gt;&lt;br&gt; &lt;code&gt;all&lt;/code&gt; Returns all players&lt;br&gt; &lt;code&gt;fantasy&lt;/code&gt; Returns traditional fantasy players (QB, RB, WR, TE, K, DST)&lt;br&gt; &lt;code&gt;idp&lt;/code&gt; Returns traditional fantasy players and IDP players.
    :type playerstoinclude: str
    :param minutes: Only returns player statistics that have changed in the last X minutes.  You specify how many minutes in time to go back.  Valid entries are:&lt;br&gt;&lt;code&gt;1&lt;/code&gt;,  &lt;code&gt;2&lt;/code&gt;, etc.         
    :type minutes: str

    """
    return web.Response(status=200)


async def box_scores_v_simulation(request: web.Request, format, numberofplays) -> web.Response:
    """Box Scores V3 Simulation

    Gets simulated live box scores of NFL games, covering the Conference Championship games on January 21, 2018.

    :param format: Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;.
    :type format: str
    :param numberofplays: The number of plays to progress in this NFL live game simulation. Example entries are &lt;code&gt;0&lt;/code&gt;, &lt;code&gt;1&lt;/code&gt;, &lt;code&gt;2&lt;/code&gt;, &lt;code&gt;3&lt;/code&gt;, &lt;code&gt;150&lt;/code&gt;, &lt;code&gt;200&lt;/code&gt;, etc.
    :type numberofplays: str

    """
    return web.Response(status=200)


async def bye_weeks(request: web.Request, format, season) -> web.Response:
    """Bye Weeks

    Get bye weeks for the teams during a specified NFL season. 

    :param format: Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;.
    :type format: str
    :param season:            Year of the season and the season type. If no season type is provided, then the default is regular season.           &lt;br&gt;Examples: &lt;code&gt;2015REG&lt;/code&gt;, &lt;code&gt;2015PRE&lt;/code&gt;, &lt;code&gt;2015POST&lt;/code&gt;.         
    :type season: str

    """
    return web.Response(status=200)


async def daily_fantasy_players(request: web.Request, format, _date) -> web.Response:
    """Daily Fantasy Players

    

    :param format: Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;.
    :type format: str
    :param _date:            The date of the contest for which you&#39;re pulling players           &lt;code&gt;2014-SEP-21&lt;/code&gt;,           &lt;code&gt;2014-NOV-15&lt;/code&gt;, etc         
    :type _date: str

    """
    return web.Response(status=200)


async def daily_fantasy_scoring(request: web.Request, format, _date) -> web.Response:
    """Daily Fantasy Scoring

    

    :param format: Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;.
    :type format: str
    :param _date: The date of the contest for which you&#39;re pulling players           &lt;code&gt;2014-SEP-21&lt;/code&gt;,           &lt;code&gt;2014-NOV-15&lt;/code&gt;, etc
    :type _date: str

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
    :param season: Year of the season and the season type. If no season type is provided, then the default is regular season.           &lt;br&gt;Examples: &lt;code&gt;2015REG&lt;/code&gt;, &lt;code&gt;2015PRE&lt;/code&gt;, &lt;code&gt;2015POST&lt;/code&gt;.         
    :type season: str
    :param week: Week of the season. Valid values are as follows: Preseason 0 to 4, Regular Season 1 to 17, Postseason 1 to 4.           Example: &lt;code&gt;1&lt;/code&gt;         
    :type week: str

    """
    return web.Response(status=200)


async def fantasy_defense_game_stats(request: web.Request, format, season, week) -> web.Response:
    """Fantasy Defense Game Stats

    

    :param format: Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;.
    :type format: str
    :param season:            Year of the season and the season type. If no season type is provided, then the default is regular season.           &lt;br&gt;Examples: &lt;code&gt;2015REG&lt;/code&gt;, &lt;code&gt;2015PRE&lt;/code&gt;, &lt;code&gt;2015POST&lt;/code&gt;.         
    :type season: str
    :param week:            Week of the season. Valid values are as follows: Preseason 0 to 4, Regular Season 1 to 17, Postseason 1 to 4.           Example: &lt;code&gt;1&lt;/code&gt;         
    :type week: str

    """
    return web.Response(status=200)


async def fantasy_defense_game_stats_by_team(request: web.Request, format, season, week, team) -> web.Response:
    """Fantasy Defense Game Stats by Team

    

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


async def fantasy_defense_season_stats(request: web.Request, format, season) -> web.Response:
    """Fantasy Defense Season Stats

    

    :param format: Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;.
    :type format: str
    :param season:            Year of the season and the season type. If no season type is provided, then the default is regular season.           &lt;br&gt;Examples: &lt;code&gt;2015REG&lt;/code&gt;, &lt;code&gt;2015PRE&lt;/code&gt;, &lt;code&gt;2015POST&lt;/code&gt;.         
    :type season: str

    """
    return web.Response(status=200)


async def fantasy_defense_season_stats_by_team(request: web.Request, format, season, team) -> web.Response:
    """Fantasy Defense Season Stats by Team

    

    :param format: Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;.
    :type format: str
    :param season: Year of the season and the season type. If no season type is provided, then the default is regular season.           &lt;br&gt;Examples: &lt;code&gt;2015REG&lt;/code&gt;, &lt;code&gt;2015PRE&lt;/code&gt;, &lt;code&gt;2015POST&lt;/code&gt;.         
    :type season: str
    :param team: Abbreviation of the team. Example: &lt;code&gt;WAS&lt;/code&gt;.
    :type team: str

    """
    return web.Response(status=200)


async def fantasy_player_ownership_percentages_season_long(request: web.Request, format, season, week) -> web.Response:
    """Fantasy Player Ownership Percentages (Season-Long)

    

    :param format: Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;.
    :type format: str
    :param season: Year of the season and the season type. If no season type is provided, then the default is regular season.           &lt;br&gt;Examples: &lt;code&gt;2015REG&lt;/code&gt;, &lt;code&gt;2015PRE&lt;/code&gt;, &lt;code&gt;2015POST&lt;/code&gt;.         
    :type season: str
    :param week: Week of the season. Valid values are as follows: Preseason 0 to 4, Regular Season 1 to 17, Postseason 1 to 4.           Example: &lt;code&gt;1&lt;/code&gt;         
    :type week: str

    """
    return web.Response(status=200)


async def fantasy_players_with_adp(request: web.Request, format) -> web.Response:
    """Fantasy Players with ADP

    This method returns a comprehensive list of draftable fantasy football players, including QB, RB, WR, TE, K and DEF.  Players are sorted by ADP (AverageDraftPosition).

    :param format: Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;.
    :type format: str

    """
    return web.Response(status=200)


async def game_stats_by_season_deprecated_use_team_game_stats_instead(request: web.Request, format, season) -> web.Response:
    """Game Stats by Season (Deprecated, use Team Game Stats instead)

    Game stats for a specified season.

    :param format: Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;.
    :type format: str
    :param season:            Year of the season and the season type. If no season type is provided, then the default is regular season.           &lt;br&gt;Examples: &lt;code&gt;2015REG&lt;/code&gt;, &lt;code&gt;2015PRE&lt;/code&gt;, &lt;code&gt;2015POST&lt;/code&gt;.         
    :type season: str

    """
    return web.Response(status=200)


async def game_stats_by_week_deprecated_use_team_game_stats_instead(request: web.Request, format, season, week) -> web.Response:
    """Game Stats by Week (Deprecated, use Team Game Stats instead)

    Game stats for a specified season and week.

    :param format: Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;.
    :type format: str
    :param season:            Year of the season and the season type. If no season type is provided, then the default is regular season.           &lt;br&gt;Examples: &lt;code&gt;2015REG&lt;/code&gt;, &lt;code&gt;2015PRE&lt;/code&gt;, &lt;code&gt;2015POST&lt;/code&gt;.         
    :type season: str
    :param week:            Week of the season. Valid values are as follows: Preseason 0 to 4, Regular Season 1 to 17, Postseason 1 to 4.           Example: &lt;code&gt;1&lt;/code&gt;         
    :type week: str

    """
    return web.Response(status=200)


async def idp_fantasy_players_with_adp(request: web.Request, format) -> web.Response:
    """IDP Fantasy Players with ADP

    This method returns the top 300+ IDP Fantasy Players for the current or upcoming season, ordered by AverageDraftPositionIDP.

    :param format: Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;.
    :type format: str

    """
    return web.Response(status=200)


async def injuries(request: web.Request, format, season, week) -> web.Response:
    """Injuries

    

    :param format: Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;.
    :type format: str
    :param season:            Year of the season and the season type. If no season type is provided, then the default is regular season.           &lt;br&gt;Examples: &lt;code&gt;2015REG&lt;/code&gt;, &lt;code&gt;2015PRE&lt;/code&gt;, &lt;code&gt;2015POST&lt;/code&gt;.         
    :type season: str
    :param week:            Week of the season. Valid values are as follows: Preseason 0 to 4, Regular Season 1 to 17, Postseason 1 to 4.           Example: &lt;code&gt;1&lt;/code&gt;         
    :type week: str

    """
    return web.Response(status=200)


async def injuries_by_team(request: web.Request, format, season, week, team) -> web.Response:
    """Injuries by Team

    

    :param format: Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;.
    :type format: str
    :param season:            Year of the season and the season type. If no season type is provided, then the default is regular season.           &lt;br&gt;Examples: &lt;code&gt;2015REG&lt;/code&gt;, &lt;code&gt;2015PRE&lt;/code&gt;, &lt;code&gt;2015POST&lt;/code&gt;.         
    :type season: str
    :param week:            Week of the season. Valid values are as follows: Preseason 0 to 4, Regular Season 1 to 17, Postseason 1 to 4.           Example: &lt;code&gt;1&lt;/code&gt;         
    :type week: str
    :param team: Abbreviation of the team. Example: &lt;code&gt;WAS&lt;/code&gt;.
    :type team: str

    """
    return web.Response(status=200)


async def league_leaders_by_season(request: web.Request, format, season, position, column) -> web.Response:
    """League Leaders by Season

    

    :param format: Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;.
    :type format: str
    :param season:            Year of the season and the season type. If no season type is provided, then the default is regular season.           &lt;br&gt;Examples: &lt;code&gt;2015REG&lt;/code&gt;, &lt;code&gt;2015PRE&lt;/code&gt;, &lt;code&gt;2015POST&lt;/code&gt;.         
    :type season: str
    :param position: Playerâ€™s position that you would like to filter by.
    :type position: str
    :param column: Response member you would like results sorted by.
    :type column: str

    """
    return web.Response(status=200)


async def league_leaders_by_week(request: web.Request, format, season, week, position, column) -> web.Response:
    """League Leaders by Week

    

    :param format:            Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;.         
    :type format: str
    :param season:            Year of the season and the season type. If no season type is provided, then the default is regular season.           &lt;br&gt;Examples: &lt;code&gt;2015REG&lt;/code&gt;, &lt;code&gt;2015PRE&lt;/code&gt;, &lt;code&gt;2015POST&lt;/code&gt;.         
    :type season: str
    :param week:            Week of the season. Valid values are as follows: Preseason 0 to 4, Regular Season 1 to 17, Postseason 1 to 4.           Example: &lt;code&gt;1&lt;/code&gt;         
    :type week: str
    :param position: Playerâ€™s position that you would like to filter by.
    :type position: str
    :param column: Response member you would like results sorted by.
    :type column: str

    """
    return web.Response(status=200)


async def legacy_box_score(request: web.Request, format, season, week, hometeam) -> web.Response:
    """Legacy Box Score

    

    :param format: Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;.
    :type format: str
    :param season:            Year of the season and the season type. If no season type is provided, then the default is regular season.           &lt;br&gt;Examples: &lt;code&gt;2015REG&lt;/code&gt;, &lt;code&gt;2015PRE&lt;/code&gt;, &lt;code&gt;2015POST&lt;/code&gt;.         
    :type season: str
    :param week:            Week of the season. Valid values are as follows: Preseason 0 to 4, Regular Season 1 to 17, Postseason 1 to 4.           Example: &lt;code&gt;1&lt;/code&gt;         
    :type week: str
    :param hometeam: Abbreviation of the home team. Example: &lt;code&gt;WAS&lt;/code&gt;.
    :type hometeam: str

    """
    return web.Response(status=200)


async def legacy_box_scores(request: web.Request, format, season, week) -> web.Response:
    """Legacy Box Scores

    This method returns all box scores for a given season and week.

    :param format: Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;.
    :type format: str
    :param season:            Year of the season and the season type. If no season type is provided, then the default is regular season.           &lt;br&gt;Examples: &lt;code&gt;2015REG&lt;/code&gt;, &lt;code&gt;2015PRE&lt;/code&gt;, &lt;code&gt;2015POST&lt;/code&gt;.         
    :type season: str
    :param week:            Week of the season. Valid values are as follows: Preseason 0 to 4, Regular Season 1 to 17, Postseason 1 to 4.           Example: &lt;code&gt;1&lt;/code&gt;         
    :type week: str

    """
    return web.Response(status=200)


async def legacy_box_scores_active(request: web.Request, format) -> web.Response:
    """Legacy Box Scores Active

    This method returns box scores for all games that are either in-progress or have been updated within the last 30 minutes.

    :param format: Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;.
    :type format: str

    """
    return web.Response(status=200)


async def legacy_box_scores_delta(request: web.Request, format, season, week, minutes) -> web.Response:
    """Legacy Box Scores Delta

    This method returns all box scores for a given season and week, but only returns player stats that have changed in the last X minutes.

    :param format: Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;.
    :type format: str
    :param season: Year of the season and the season type. If no season type is provided, then the default is regular season.           &lt;br&gt;Examples: &lt;code&gt;2015REG&lt;/code&gt;, &lt;code&gt;2015PRE&lt;/code&gt;, &lt;code&gt;2015POST&lt;/code&gt;.         
    :type season: str
    :param week: Week of the season. Valid values are as follows: Preseason 0 to 4, Regular Season 1 to 17, Postseason 1 to 4.           Example: &lt;code&gt;1&lt;/code&gt;         
    :type week: str
    :param minutes: Only returns player statistics that have changed in the last X minutes.  You specify how many minutes in time to go back.  Valid entries are:&lt;br&gt;           &lt;code&gt;1&lt;/code&gt; or &lt;code&gt;2&lt;/code&gt;.         
    :type minutes: str

    """
    return web.Response(status=200)


async def legacy_box_scores_delta_current_week(request: web.Request, format, minutes) -> web.Response:
    """Legacy Box Scores Delta (Current Week)

    

    :param format: Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;.
    :type format: str
    :param minutes: Only returns player statistics that have changed in the last X minutes.  You specify how many minutes in time to go back.  Valid entries are:&lt;br&gt;           &lt;code&gt;1&lt;/code&gt; or &lt;code&gt;2&lt;/code&gt;.         
    :type minutes: str

    """
    return web.Response(status=200)


async def legacy_box_scores_final(request: web.Request, format) -> web.Response:
    """Legacy Box Scores Final

    

    :param format: Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;.
    :type format: str

    """
    return web.Response(status=200)


async def legacy_box_scores_live(request: web.Request, format) -> web.Response:
    """Legacy Box Scores Live

    

    :param format: Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;.
    :type format: str

    """
    return web.Response(status=200)


async def news(request: web.Request, format) -> web.Response:
    """News

    

    :param format: Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;.
    :type format: str

    """
    return web.Response(status=200)


async def news_by_date(request: web.Request, format, _date) -> web.Response:
    """News by Date

    

    :param format: Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;.
    :type format: str
    :param _date: The date of the news. &lt;br&gt;Examples: &lt;code&gt;2017-JUL-31&lt;/code&gt;, &lt;code&gt;2017-SEP-01&lt;/code&gt;.
    :type _date: str

    """
    return web.Response(status=200)


async def news_by_player(request: web.Request, format, playerid) -> web.Response:
    """News by Player

    

    :param format:            Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;.         
    :type format: str
    :param playerid: Each NFL player has a unique ID assigned by FantasyData. Player IDs can be determined by pulling player related data. Example:&lt;code&gt;14257&lt;/code&gt;.
    :type playerid: str

    """
    return web.Response(status=200)


async def news_by_team(request: web.Request, format, team) -> web.Response:
    """News by Team

    

    :param format: Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;.
    :type format: str
    :param team: Abbreviation of the team. Example: &lt;code&gt;WAS&lt;/code&gt;.
    :type team: str

    """
    return web.Response(status=200)


async def player_details_by_available(request: web.Request, format) -> web.Response:
    """Player Details by Available

    

    :param format: Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;.
    :type format: str

    """
    return web.Response(status=200)


async def player_details_by_free_agents(request: web.Request, format) -> web.Response:
    """Player Details by Free Agents

    

    :param format: Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;.
    :type format: str

    """
    return web.Response(status=200)


async def player_details_by_player(request: web.Request, format, playerid) -> web.Response:
    """Player Details by Player

    

    :param format: Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;.
    :type format: str
    :param playerid: Each NFL player has a unique ID assigned by FantasyData. Player IDs can be determined by pulling player related data. Example:&lt;code&gt;732&lt;/code&gt;.
    :type playerid: str

    """
    return web.Response(status=200)


async def player_details_by_rookie_draft_year(request: web.Request, format, season) -> web.Response:
    """Player Details by Rookie Draft Year

    

    :param format: Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;.
    :type format: str
    :param season: Year of the season.&lt;br&gt;Examples: &lt;code&gt;2018&lt;/code&gt;, &lt;code&gt;2019&lt;/code&gt;, etc.
    :type season: str

    """
    return web.Response(status=200)


async def player_details_by_team(request: web.Request, format, team) -> web.Response:
    """Player Details by Team

    

    :param format: Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;.
    :type format: str
    :param team: Abbreviation of the team. Example: &lt;code&gt;WAS&lt;/code&gt;.
    :type team: str

    """
    return web.Response(status=200)


async def player_game_logs_by_season(request: web.Request, format, season, playerid, numberofgames) -> web.Response:
    """Player Game Logs By Season

    

    :param format: Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;.
    :type format: str
    :param season: Season to get games from. Example &lt;code&gt;2019POST&lt;/code&gt;, &lt;code&gt;2020&lt;/code&gt;
    :type season: str
    :param playerid: Unique FantasyData Player ID. Example:&lt;code&gt;17920&lt;/code&gt;.
    :type playerid: str
    :param numberofgames: How many games to return. Example &lt;code&gt;all&lt;/code&gt;, &lt;code&gt;10&lt;/code&gt;, &lt;code&gt;25&lt;/code&gt;
    :type numberofgames: str

    """
    return web.Response(status=200)


async def player_game_red_zone_stats(request: web.Request, format, season, week) -> web.Response:
    """Player Game Red Zone Stats

    

    :param format: Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;.
    :type format: str
    :param season: Year of the season and the season type. If no season type is provided, then the default is regular season.           &lt;br&gt;Examples: &lt;code&gt;2015REG&lt;/code&gt;, &lt;code&gt;2015PRE&lt;/code&gt;, &lt;code&gt;2015POST&lt;/code&gt;.         
    :type season: str
    :param week: Week of the season. Valid values are as follows: Preseason 0 to 4, Regular Season 1 to 17, Postseason 1 to 4.           Example: &lt;code&gt;1&lt;/code&gt;         
    :type week: str

    """
    return web.Response(status=200)


async def player_game_red_zone_stats_inside_five(request: web.Request, format, season, week) -> web.Response:
    """Player Game Red Zone Stats Inside Five

    

    :param format: Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;.
    :type format: str
    :param season: Year of the season and the season type. If no season type is provided, then the default is regular season.           &lt;br&gt;Examples: &lt;code&gt;2015REG&lt;/code&gt;, &lt;code&gt;2015PRE&lt;/code&gt;, &lt;code&gt;2015POST&lt;/code&gt;.         
    :type season: str
    :param week: Week of the season. Valid values are as follows: Preseason 0 to 4, Regular Season 1 to 17, Postseason 1 to 4.           Example: &lt;code&gt;1&lt;/code&gt;         
    :type week: str

    """
    return web.Response(status=200)


async def player_game_red_zone_stats_inside_ten(request: web.Request, format, season, week) -> web.Response:
    """Player Game Red Zone Stats Inside Ten

    

    :param format: Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;.
    :type format: str
    :param season: Year of the season and the season type. If no season type is provided, then the default is regular season.           &lt;br&gt;Examples: &lt;code&gt;2015REG&lt;/code&gt;, &lt;code&gt;2015PRE&lt;/code&gt;, &lt;code&gt;2015POST&lt;/code&gt;.         
    :type season: str
    :param week: Week of the season. Valid values are as follows: Preseason 0 to 4, Regular Season 1 to 17, Postseason 1 to 4.           Example: &lt;code&gt;1&lt;/code&gt;         
    :type week: str

    """
    return web.Response(status=200)


async def player_game_stats_by_player(request: web.Request, format, season, week, playerid) -> web.Response:
    """Player Game Stats by Player

    

    :param format: Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;.
    :type format: str
    :param season:            Year of the season and the season type. If no season type is provided, then the default is regular season.           &lt;br&gt;Examples: &lt;code&gt;2015REG&lt;/code&gt;, &lt;code&gt;2015PRE&lt;/code&gt;, &lt;code&gt;2015POST&lt;/code&gt;.         
    :type season: str
    :param week:            Week of the season. Valid values are as follows: Preseason 0 to 4, Regular Season 1 to 17, Postseason 1 to 4.           Example: &lt;code&gt;1&lt;/code&gt;         
    :type week: str
    :param playerid: Each NFL player has a unique ID assigned by FantasyData. Player IDs can be determined by pulling player related data. Example:&lt;code&gt;732&lt;/code&gt;.
    :type playerid: str

    """
    return web.Response(status=200)


async def player_game_stats_by_team(request: web.Request, format, season, week, team) -> web.Response:
    """Player Game Stats by Team

    

    :param format: Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;.
    :type format: str
    :param season:            Year of the season and the season type. If no season type is provided, then the default is regular season.           &lt;br&gt;Examples: &lt;code&gt;2015REG&lt;/code&gt;, &lt;code&gt;2015PRE&lt;/code&gt;, &lt;code&gt;2015POST&lt;/code&gt;.         
    :type season: str
    :param week:            Week of the season. Valid values are as follows: Preseason 0 to 4, Regular Season 1 to 17, Postseason 1 to 4.           Example: &lt;code&gt;1&lt;/code&gt;         
    :type week: str
    :param team: Abbreviation of the team. Example: &lt;code&gt;WAS&lt;/code&gt;.
    :type team: str

    """
    return web.Response(status=200)


async def player_game_stats_by_week(request: web.Request, format, season, week) -> web.Response:
    """Player Game Stats by Week

    

    :param format: Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;.
    :type format: str
    :param season:            Year of the season and the season type. If no season type is provided, then the default is regular season.           &lt;br&gt;Examples: &lt;code&gt;2015REG&lt;/code&gt;, &lt;code&gt;2015PRE&lt;/code&gt;, &lt;code&gt;2015POST&lt;/code&gt;.         
    :type season: str
    :param week:            Week of the season. Valid values are as follows: Preseason 0 to 4, Regular Season 1 to 17, Postseason 1 to 4.           Example: &lt;code&gt;1&lt;/code&gt;         
    :type week: str

    """
    return web.Response(status=200)


async def player_game_stats_by_week_delta(request: web.Request, format, season, week, minutes) -> web.Response:
    """Player Game Stats by Week Delta

    

    :param format: Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;.
    :type format: str
    :param season:            Year of the season and the season type. If no season type is provided, then the default is regular season.           &lt;br&gt;Examples: &lt;code&gt;2015REG&lt;/code&gt;, &lt;code&gt;2015PRE&lt;/code&gt;, &lt;code&gt;2015POST&lt;/code&gt;.         
    :type season: str
    :param week:            Week of the season. Valid values are as follows: Preseason 0 to 4, Regular Season 1 to 17, Postseason 1 to 4.           Example: &lt;code&gt;1&lt;/code&gt;         
    :type week: str
    :param minutes: Only returns player statistics that have changed in the last X minutes.  You specify how many minutes in time to go back.  Valid entries are:&lt;br&gt;           &lt;code&gt;1&lt;/code&gt; or &lt;code&gt;2&lt;/code&gt;.         
    :type minutes: str

    """
    return web.Response(status=200)


async def player_game_stats_delta(request: web.Request, format, minutes) -> web.Response:
    """Player Game Stats Delta

    

    :param format: Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;.
    :type format: str
    :param minutes:            Only returns player statistics that have changed in the last X minutes.  You specify how many minutes in time to go back.  Valid entries are:           &lt;code&gt;1&lt;/code&gt; or &lt;code&gt;2&lt;/code&gt;.         
    :type minutes: str

    """
    return web.Response(status=200)


async def player_season_red_zone_stats(request: web.Request, format, season) -> web.Response:
    """Player Season Red Zone Stats

    

    :param format: Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;.
    :type format: str
    :param season: Year of the season and the season type. If no season type is provided, then the default is regular season.           &lt;br&gt;Examples: &lt;code&gt;2015REG&lt;/code&gt;, &lt;code&gt;2015PRE&lt;/code&gt;, &lt;code&gt;2015POST&lt;/code&gt;.         
    :type season: str

    """
    return web.Response(status=200)


async def player_season_red_zone_stats_inside_five(request: web.Request, format, season) -> web.Response:
    """Player Season Red Zone Stats Inside Five

    

    :param format: Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;.
    :type format: str
    :param season: Year of the season and the season type. If no season type is provided, then the default is regular season.           &lt;br&gt;Examples: &lt;code&gt;2015REG&lt;/code&gt;, &lt;code&gt;2015PRE&lt;/code&gt;, &lt;code&gt;2015POST&lt;/code&gt;.         
    :type season: str

    """
    return web.Response(status=200)


async def player_season_red_zone_stats_inside_ten(request: web.Request, format, season) -> web.Response:
    """Player Season Red Zone Stats Inside Ten

    

    :param format: Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;.
    :type format: str
    :param season: Year of the season and the season type. If no season type is provided, then the default is regular season.           &lt;br&gt;Examples: &lt;code&gt;2015REG&lt;/code&gt;, &lt;code&gt;2015PRE&lt;/code&gt;, &lt;code&gt;2015POST&lt;/code&gt;.         
    :type season: str

    """
    return web.Response(status=200)


async def player_season_stats(request: web.Request, format, season) -> web.Response:
    """Player Season Stats

    

    :param format: Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;.
    :type format: str
    :param season:            Year of the season and the season type. If no season type is provided, then the default is regular season.           &lt;br&gt;Examples: &lt;code&gt;2015REG&lt;/code&gt;, &lt;code&gt;2015PRE&lt;/code&gt;, &lt;code&gt;2015POST&lt;/code&gt;.         
    :type season: str

    """
    return web.Response(status=200)


async def player_season_stats_by_player(request: web.Request, format, season, playerid) -> web.Response:
    """Player Season Stats by Player

    

    :param format: Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;.
    :type format: str
    :param season:            Year of the season and the season type. If no season type is provided, then the default is regular season.           &lt;br&gt;Examples: &lt;code&gt;2015REG&lt;/code&gt;, &lt;code&gt;2015PRE&lt;/code&gt;, &lt;code&gt;2015POST&lt;/code&gt;.         
    :type season: str
    :param playerid: Each NFL player has a unique ID assigned by FantasyData. Player IDs can be determined by pulling player related data. Example:&lt;code&gt;732&lt;/code&gt;.
    :type playerid: str

    """
    return web.Response(status=200)


async def player_season_stats_by_team(request: web.Request, format, season, team) -> web.Response:
    """Player Season Stats by Team

    

    :param format: Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;.
    :type format: str
    :param season:            Year of the season and the season type. If no season type is provided, then the default is regular season.           &lt;br&gt;Examples: &lt;code&gt;2015REG&lt;/code&gt;, &lt;code&gt;2015PRE&lt;/code&gt;, &lt;code&gt;2015POST&lt;/code&gt;.         
    :type season: str
    :param team: Abbreviation of the team. Example: &lt;code&gt;WAS&lt;/code&gt;.
    :type team: str

    """
    return web.Response(status=200)


async def player_season_third_down_stats(request: web.Request, format, season) -> web.Response:
    """Player Season Third Down Stats

    

    :param format: Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;.
    :type format: str
    :param season:            Year of the season and the season type. If no season type is provided, then the default is regular season.           &lt;br&gt;Examples: &lt;code&gt;2015REG&lt;/code&gt;, &lt;code&gt;2015PRE&lt;/code&gt;, &lt;code&gt;2015POST&lt;/code&gt;.         
    :type season: str

    """
    return web.Response(status=200)


async def pro_bowlers(request: web.Request, format, season) -> web.Response:
    """Pro Bowlers

    

    :param format: Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;.
    :type format: str
    :param season: Year of the season &lt;br&gt;Examples: &lt;code&gt;2016&lt;/code&gt;, &lt;code&gt;2017&lt;/code&gt;
    :type season: str

    """
    return web.Response(status=200)


async def schedule(request: web.Request, format, season) -> web.Response:
    """Schedule

    Game schedule for a specified season.

    :param format: Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;.
    :type format: str
    :param season: Year of the season (with optional season type).&lt;br&gt;Examples: &lt;code&gt;2018&lt;/code&gt;, &lt;code&gt;2018PRE&lt;/code&gt;, &lt;code&gt;2018POST&lt;/code&gt;, &lt;code&gt;2018STAR&lt;/code&gt;, &lt;code&gt;2019&lt;/code&gt;, etc.
    :type season: str

    """
    return web.Response(status=200)


async def scores_by_date(request: web.Request, format, _date) -> web.Response:
    """Scores by Date

    Get game scores for a specified week of a season.

    :param format: Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;.
    :type format: str
    :param _date: The date of the games.&lt;br&gt;Examples: &lt;code&gt;2021-SEP-12&lt;/code&gt;, &lt;code&gt;2021-NOV-28&lt;/code&gt;.
    :type _date: str

    """
    return web.Response(status=200)


async def scores_by_season(request: web.Request, format, season) -> web.Response:
    """Scores by Season 

    Game scores for a specified season.

    :param format: Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;.
    :type format: str
    :param season: Year of the season (with optional season type).&lt;br&gt;Examples: &lt;code&gt;2018&lt;/code&gt;, &lt;code&gt;2018PRE&lt;/code&gt;, &lt;code&gt;2018POST&lt;/code&gt;, &lt;code&gt;2018STAR&lt;/code&gt;, &lt;code&gt;2019&lt;/code&gt;, etc.
    :type season: str

    """
    return web.Response(status=200)


async def scores_by_week(request: web.Request, format, season, week) -> web.Response:
    """Scores by Week

    Get game scores for a specified week of a season.

    :param format: Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;.
    :type format: str
    :param season:            Year of the season and the season type. If no season type is provided, then the default is regular season.           &lt;br&gt;Examples: &lt;code&gt;2015REG&lt;/code&gt;, &lt;code&gt;2015PRE&lt;/code&gt;, &lt;code&gt;2015POST&lt;/code&gt;.         
    :type season: str
    :param week:            Week of the season. Valid values are as follows: Preseason 0 to 4, Regular Season 1 to 17, Postseason 1 to 4.           Example: &lt;code&gt;1&lt;/code&gt;         
    :type week: str

    """
    return web.Response(status=200)


async def scores_by_week_simulation(request: web.Request, format, numberofplays) -> web.Response:
    """Scores by Week Simulation

    Gets simulated live scores of NFL games, covering the Conference Championship games on January 21, 2018.

    :param format: Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;.
    :type format: str
    :param numberofplays: The number of plays to progress in this NFL live game simulation. Example entries are &lt;code&gt;0&lt;/code&gt;, &lt;code&gt;1&lt;/code&gt;, &lt;code&gt;2&lt;/code&gt;, &lt;code&gt;3&lt;/code&gt;, &lt;code&gt;150&lt;/code&gt;, &lt;code&gt;200&lt;/code&gt;, etc.
    :type numberofplays: str

    """
    return web.Response(status=200)


async def season_current(request: web.Request, format) -> web.Response:
    """Season Current

    Year of the current NFL season. This value changes at the start of the new NFL league year. The earliest season for Fantasy data is 2001. The earliest season for Team data is 1985. The earliest season for Fantasy data is 2001. The earliest season for Team data is 1985.

    :param format: Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;.
    :type format: str

    """
    return web.Response(status=200)


async def season_last_completed(request: web.Request, format) -> web.Response:
    """Season Last Completed

    Year of the most recently completed season. this value changes immediately after the Super Bowl. The earliest season for Fantasy data is 2001. The earliest season for Team data is 1985.

    :param format: Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;.
    :type format: str

    """
    return web.Response(status=200)


async def season_upcoming(request: web.Request, format) -> web.Response:
    """Season Upcoming

    Year of the current NFL season, if we are in the mid-season. If we are in the off-season, then year of the next upcoming season. This value changes immediately after the Super Bowl. The earliest season for Fantasy data is 2001. The earliest season for Team data is 1985.

    :param format: Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;.
    :type format: str

    """
    return web.Response(status=200)


async def stadiums(request: web.Request, format) -> web.Response:
    """Stadiums

    This method returns all stadiums.

    :param format: Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;.
    :type format: str

    """
    return web.Response(status=200)


async def standings(request: web.Request, format, season) -> web.Response:
    """Standings

    

    :param format: Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;.
    :type format: str
    :param season:            Year of the season and the season type. If no season type is provided, then the default is regular season.           &lt;br&gt;Examples: &lt;code&gt;2015REG&lt;/code&gt;, &lt;code&gt;2015PRE&lt;/code&gt;, &lt;code&gt;2015POST&lt;/code&gt;.         
    :type season: str

    """
    return web.Response(status=200)


async def team_game_logs_by_season(request: web.Request, format, season, teamid, numberofgames) -> web.Response:
    """Team Game Logs By Season

    Game by game log of total team statistics.

    :param format: Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;.
    :type format: str
    :param season: Season to get games from. Example &lt;code&gt;2019POST&lt;/code&gt;, &lt;code&gt;2020&lt;/code&gt;
    :type season: str
    :param teamid: Unique ID of team.  Example &lt;code&gt; 8 &lt;/code&gt;
    :type teamid: str
    :param numberofgames: How many games to return. Example &lt;code&gt;all&lt;/code&gt;, &lt;code&gt;10&lt;/code&gt;, &lt;code&gt;25&lt;/code&gt;
    :type numberofgames: str

    """
    return web.Response(status=200)


async def team_game_stats(request: web.Request, format, season, week) -> web.Response:
    """Team Game Stats

    

    :param format: Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;.
    :type format: str
    :param season:            Year of the season and the season type. If no season type is provided, then the default is regular season.           &lt;br&gt;Examples: &lt;code&gt;2015REG&lt;/code&gt;, &lt;code&gt;2015PRE&lt;/code&gt;, &lt;code&gt;2015POST&lt;/code&gt;.         
    :type season: str
    :param week:            Week of the season. Valid values are as follows: Preseason 0 to 4, Regular Season 1 to 17, Postseason 1 to 4.           Example: &lt;code&gt;1&lt;/code&gt;         
    :type week: str

    """
    return web.Response(status=200)


async def team_season_stats(request: web.Request, format, season) -> web.Response:
    """Team Season Stats

    

    :param format: Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;.
    :type format: str
    :param season:            Year of the season and the season type. If no season type is provided, then the default is regular season.           &lt;br&gt;Examples: &lt;code&gt;2015REG&lt;/code&gt;, &lt;code&gt;2015PRE&lt;/code&gt;, &lt;code&gt;2015POST&lt;/code&gt;.         
    :type season: str

    """
    return web.Response(status=200)


async def teams_active(request: web.Request, format) -> web.Response:
    """Teams (Active)

    Gets all active teams.

    :param format: Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;.
    :type format: str

    """
    return web.Response(status=200)


async def teams_all(request: web.Request, format) -> web.Response:
    """Teams (All)

    Gets all teams, including pro bowl teams.

    :param format: Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;.
    :type format: str

    """
    return web.Response(status=200)


async def teams_by_season(request: web.Request, format, season) -> web.Response:
    """Teams by Season

    List of teams playing in a specified season.

    :param format: Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;.
    :type format: str
    :param season:            Year of the season and the season type. If no season type is provided, then the default is regular season.           &lt;br&gt;Examples: &lt;code&gt;2015REG&lt;/code&gt;, &lt;code&gt;2015PRE&lt;/code&gt;, &lt;code&gt;2015POST&lt;/code&gt;.         
    :type season: str

    """
    return web.Response(status=200)


async def timeframes(request: web.Request, format, type) -> web.Response:
    """Timeframes

    Get detailed information about past, present, and future timeframes.

    :param format: Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;.
    :type format: str
    :param type: The type of timeframes to return.  Valid entries are &lt;code&gt;current&lt;/code&gt; or &lt;code&gt;upcoming&lt;/code&gt; or &lt;code&gt;completed&lt;/code&gt; or &lt;code&gt;recent&lt;/code&gt; or &lt;code&gt;all&lt;/code&gt;.
    :type type: str

    """
    return web.Response(status=200)


async def week_current(request: web.Request, format) -> web.Response:
    """Week Current

    Number of the current week of the NFL season. This value usually changes on Tuesday nights or Wednesday mornings at midnight ET.

    :param format: Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;.
    :type format: str

    """
    return web.Response(status=200)


async def week_last_completed(request: web.Request, format) -> web.Response:
    """Week Last Completed

    Number of the current week of the NFL season. This value usually changes on Tuesday nights or Wednesday mornings at midnight ET.

    :param format: Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;.
    :type format: str

    """
    return web.Response(status=200)


async def week_upcoming(request: web.Request, format) -> web.Response:
    """Week Upcoming

    Number of the current week of the NFL season. This value usually changes on Tuesday nights or Wednesday mornings at midnight ET.

    :param format: Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;.
    :type format: str

    """
    return web.Response(status=200)
