from typing import List, Dict
from aiohttp import web

from openapi_server.models.area import Area
from openapi_server.models.canceled_membership import CanceledMembership
from openapi_server.models.competition import Competition
from openapi_server.models.competition_detail import CompetitionDetail
from openapi_server.models.game import Game
from openapi_server.models.membership import Membership
from openapi_server.models.player import Player
from openapi_server.models.season_team import SeasonTeam
from openapi_server.models.standing import Standing
from openapi_server.models.team import Team
from openapi_server.models.team_game import TeamGame
from openapi_server.models.team_season import TeamSeason
from openapi_server.models.venue import Venue
from openapi_server import util


async def areas_countries(request: web.Request, format) -> web.Response:
    """Areas (Countries)

    

    :param format: Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;.
    :type format: str

    """
    return web.Response(status=200)


async def canceled_memberships(request: web.Request, format) -> web.Response:
    """Canceled Memberships

    

    :param format: Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;.
    :type format: str

    """
    return web.Response(status=200)


async def competition_fixtures_league_details(request: web.Request, format, competition) -> web.Response:
    """Competition Fixtures (League Details)

    

    :param format: Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;.
    :type format: str
    :param competition: An indication of a soccer competition/league. This value can be the CompetitionId or the Competition Key. Possible values include: &lt;code&gt;EPL&lt;/code&gt;, &lt;code&gt;1&lt;/code&gt;, &lt;code&gt;MLS&lt;/code&gt;, &lt;code&gt;8&lt;/code&gt;, etc.
    :type competition: str

    """
    return web.Response(status=200)


async def competition_hierarchy_league_hierarchy(request: web.Request, format) -> web.Response:
    """Competition Hierarchy (League Hierarchy)

    

    :param format: Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;.
    :type format: str

    """
    return web.Response(status=200)


async def competitions_leagues(request: web.Request, format) -> web.Response:
    """Competitions (Leagues)

    

    :param format: Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;.
    :type format: str

    """
    return web.Response(status=200)


async def games_by_date(request: web.Request, format, _date) -> web.Response:
    """Games by Date

    

    :param format: Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;.
    :type format: str
    :param _date: The date of the game(s). &lt;br&gt;Examples: &lt;code&gt;2017-02-27&lt;/code&gt;, &lt;code&gt;2017-09-01&lt;/code&gt;.
    :type _date: str

    """
    return web.Response(status=200)


async def memberships_active(request: web.Request, format) -> web.Response:
    """Memberships (Active)

    

    :param format: Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;.
    :type format: str

    """
    return web.Response(status=200)


async def memberships_by_competition_active(request: web.Request, format, competition) -> web.Response:
    """Memberships by Competition (Active)

    

    :param format: Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;.
    :type format: str
    :param competition: An indication of a soccer competition/league. This value can be the CompetitionId or the Competition Key. Possible values include: &lt;code&gt;EPL&lt;/code&gt;, &lt;code&gt;1&lt;/code&gt;, &lt;code&gt;MLS&lt;/code&gt;, &lt;code&gt;8&lt;/code&gt;, etc.
    :type competition: str

    """
    return web.Response(status=200)


async def memberships_by_competition_historical(request: web.Request, format, competition) -> web.Response:
    """Memberships by Competition (Historical)

    

    :param format: Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;.
    :type format: str
    :param competition: An indication of a soccer competition/league. This value can be the CompetitionId or the Competition Key. Possible values include: &lt;code&gt;EPL&lt;/code&gt;, &lt;code&gt;1&lt;/code&gt;, &lt;code&gt;MLS&lt;/code&gt;, &lt;code&gt;8&lt;/code&gt;, etc.
    :type competition: str

    """
    return web.Response(status=200)


async def memberships_by_team_active(request: web.Request, format, teamid) -> web.Response:
    """Memberships by Team (Active)

    

    :param format: Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;.
    :type format: str
    :param teamid: Unique FantasyData Team ID.  Example:&lt;code&gt;516&lt;/code&gt;.
    :type teamid: str

    """
    return web.Response(status=200)


async def memberships_by_team_historical(request: web.Request, format, teamid) -> web.Response:
    """Memberships by Team (Historical)

    

    :param format: Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;.
    :type format: str
    :param teamid: Unique FantasyData Team ID.  Example:&lt;code&gt;516&lt;/code&gt;.
    :type teamid: str

    """
    return web.Response(status=200)


async def memberships_historical(request: web.Request, format) -> web.Response:
    """Memberships (Historical)

    

    :param format: Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;.
    :type format: str

    """
    return web.Response(status=200)


async def memberships_recently_changed(request: web.Request, format, days) -> web.Response:
    """Memberships (Recently Changed)

    

    :param format: Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;.
    :type format: str
    :param days: The number of days since memberships were updated. For example, if you pass &lt;code&gt;3&lt;/code&gt;, you&#39;ll receive all memberships that have been updated in the past 3 days. Valid entries are: &lt;code&gt;1&lt;/code&gt;, &lt;code&gt;2&lt;/code&gt; ... &lt;code&gt;30&lt;/code&gt;
    :type days: str

    """
    return web.Response(status=200)


async def player(request: web.Request, format, playerid) -> web.Response:
    """Player

    

    :param format: Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;.
    :type format: str
    :param playerid: Unique FantasyData Player ID. Example:&lt;code&gt;90026231&lt;/code&gt;.
    :type playerid: str

    """
    return web.Response(status=200)


async def players(request: web.Request, format) -> web.Response:
    """Players

    

    :param format: Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;.
    :type format: str

    """
    return web.Response(status=200)


async def players_by_team(request: web.Request, format, teamid) -> web.Response:
    """Players by Team

    

    :param format: Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;.
    :type format: str
    :param teamid: Unique FantasyData Team ID.  Example:&lt;code&gt;516&lt;/code&gt;.
    :type teamid: str

    """
    return web.Response(status=200)


async def schedule(request: web.Request, format, roundid) -> web.Response:
    """Schedule

    

    :param format: Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;.
    :type format: str
    :param roundid: Unique FantasyData Round ID. RoundIDs can be found in the Competition Hierarchy (League Hierarchy).  Examples: &lt;code&gt;1&lt;/code&gt;, &lt;code&gt;2&lt;/code&gt;, &lt;code&gt;3&lt;/code&gt;, etc
    :type roundid: str

    """
    return web.Response(status=200)


async def season_teams(request: web.Request, format, seasonid) -> web.Response:
    """Season Teams

    

    :param format: Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;.
    :type format: str
    :param seasonid: Unique FantasyData Season ID. SeasonIDs can be found in the Competition Hierarchy (League Hierarchy).  Examples: &lt;code&gt;1&lt;/code&gt;, &lt;code&gt;2&lt;/code&gt;, &lt;code&gt;3&lt;/code&gt;, etc
    :type seasonid: str

    """
    return web.Response(status=200)


async def standings(request: web.Request, format, roundid) -> web.Response:
    """Standings

    

    :param format: Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;.
    :type format: str
    :param roundid: Unique FantasyData Round ID. RoundIDs can be found in the Competition Hierarchy (League Hierarchy).  Examples: &lt;code&gt;1&lt;/code&gt;, &lt;code&gt;2&lt;/code&gt;, &lt;code&gt;3&lt;/code&gt;, etc
    :type roundid: str

    """
    return web.Response(status=200)


async def team_game_stats_by_date(request: web.Request, format, _date) -> web.Response:
    """Team Game Stats by Date

    

    :param format: Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;.
    :type format: str
    :param _date: The date of the game(s). &lt;br&gt;Examples: &lt;code&gt;2017-02-27&lt;/code&gt;, &lt;code&gt;2017-09-01&lt;/code&gt;.
    :type _date: str

    """
    return web.Response(status=200)


async def team_season_stats(request: web.Request, format, roundid) -> web.Response:
    """Team Season Stats

    

    :param format: Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;.
    :type format: str
    :param roundid: Unique FantasyData Round ID. RoundIDs can be found in the Competition Hierarchy (League Hierarchy).  Examples: &lt;code&gt;1&lt;/code&gt;, &lt;code&gt;2&lt;/code&gt;, &lt;code&gt;3&lt;/code&gt;, etc
    :type roundid: str

    """
    return web.Response(status=200)


async def teams(request: web.Request, format) -> web.Response:
    """Teams

    

    :param format: Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;.
    :type format: str

    """
    return web.Response(status=200)


async def upcoming_schedule_by_player(request: web.Request, format, playerid) -> web.Response:
    """Upcoming Schedule By Player

    

    :param format: Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;.
    :type format: str
    :param playerid: Unique FantasyData Player ID. Example:&lt;code&gt;90026231&lt;/code&gt;.
    :type playerid: str

    """
    return web.Response(status=200)


async def venues(request: web.Request, format) -> web.Response:
    """Venues

    

    :param format: Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;.
    :type format: str

    """
    return web.Response(status=200)
