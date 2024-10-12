from typing import List, Dict
from aiohttp import web

from openapi_server.models.area import Area
from openapi_server.models.box_score import BoxScore
from openapi_server.models.competition import Competition
from openapi_server.models.competition_detail import CompetitionDetail
from openapi_server.models.game import Game
from openapi_server.models.membership import Membership
from openapi_server.models.player import Player
from openapi_server.models.season_team import SeasonTeam
from openapi_server.models.standing import Standing
from openapi_server.models.team import Team
from openapi_server.models.venue import Venue
from openapi_server import util


async def areas_countries(request: web.Request, format) -> web.Response:
    """Areas (Countries)

    Areas (Countries)

    :param format: Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;.
    :type format: str

    """
    return web.Response(status=200)


async def box_score(request: web.Request, format, gameid) -> web.Response:
    """Box Score

    Box Scores by Date

    :param format: Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;.
    :type format: str
    :param gameid: Unique GameId for the desired box scores. Examples: &lt;code&gt;100000091&lt;/code&gt;
    :type gameid: str

    """
    return web.Response(status=200)


async def box_scores_by_date(request: web.Request, format, _date) -> web.Response:
    """Box Scores by Date

    Box Scores by Date

    :param format: Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;.
    :type format: str
    :param _date: The date of the game(s). &lt;br&gt;Examples: &lt;code&gt;2018-01-13&lt;/code&gt;, &lt;code&gt;2018-06-13&lt;/code&gt;.
    :type _date: str

    """
    return web.Response(status=200)


async def competition_fixtures_league_details(request: web.Request, format, competitionid) -> web.Response:
    """Competition Fixtures (League Details)

    Competition Fixtures (League Details)

    :param format: Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;.
    :type format: str
    :param competitionid: A CS:GO competition/league unique CompetitionId. Possible values include: &lt;code&gt;100000009&lt;/code&gt;, etc.
    :type competitionid: str

    """
    return web.Response(status=200)


async def competitions_leagues(request: web.Request, format) -> web.Response:
    """Competitions (Leagues)

    Competitions (Leagues)

    :param format: Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;.
    :type format: str

    """
    return web.Response(status=200)


async def games_by_date(request: web.Request, format, _date) -> web.Response:
    """Games by Date

    Games by Date

    :param format: Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;.
    :type format: str
    :param _date: The date of the game(s). &lt;br&gt;Examples: &lt;code&gt;2018-01-13&lt;/code&gt;, &lt;code&gt;2018-06-13&lt;/code&gt;.
    :type _date: str

    """
    return web.Response(status=200)


async def memberships_active(request: web.Request, format) -> web.Response:
    """Memberships (Active)

    Memberships (Active)

    :param format: Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;.
    :type format: str

    """
    return web.Response(status=200)


async def memberships_by_team_active(request: web.Request, format, teamid) -> web.Response:
    """Memberships by Team (Active)

    Memberships by Team (Active)

    :param format: Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;.
    :type format: str
    :param teamid: Unique FantasyData Team ID.  Example:&lt;code&gt;100000001&lt;/code&gt;.
    :type teamid: str

    """
    return web.Response(status=200)


async def memberships_by_team_historical(request: web.Request, format, teamid) -> web.Response:
    """Memberships by Team (Historical)

    Memberships by Team (Historical)

    :param format: Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;.
    :type format: str
    :param teamid: Unique FantasyData Team ID.  Example:&lt;code&gt;100000001&lt;/code&gt;.
    :type teamid: str

    """
    return web.Response(status=200)


async def memberships_historical(request: web.Request, format) -> web.Response:
    """Memberships (Historical)

    Memberships (Historical)

    :param format: Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;.
    :type format: str

    """
    return web.Response(status=200)


async def player(request: web.Request, format, playerid) -> web.Response:
    """Player

    Player

    :param format: Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;.
    :type format: str
    :param playerid: Unique FantasyData Player ID. Example:&lt;code&gt;100000576&lt;/code&gt;.
    :type playerid: str

    """
    return web.Response(status=200)


async def players(request: web.Request, format) -> web.Response:
    """Players

    Players

    :param format: Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;.
    :type format: str

    """
    return web.Response(status=200)


async def players_by_team(request: web.Request, format, teamid) -> web.Response:
    """Players by Team

    Players by Team

    :param format: Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;.
    :type format: str
    :param teamid: Unique FantasyData Team ID.  Example:&lt;code&gt;100000001&lt;/code&gt;.
    :type teamid: str

    """
    return web.Response(status=200)


async def schedule(request: web.Request, format, roundid) -> web.Response:
    """Schedule

    Schedule

    :param format: Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;.
    :type format: str
    :param roundid: Unique FantasyData Round ID. RoundIDs can be found in the Competitions and Competition Details endpoints.  Examples: &lt;code&gt;100000138&lt;/code&gt;, &lt;code&gt;1000001412&lt;/code&gt;, etc
    :type roundid: str

    """
    return web.Response(status=200)


async def season_teams(request: web.Request, format, seasonid) -> web.Response:
    """Season Teams

    Season Teams

    :param format: Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;.
    :type format: str
    :param seasonid: Unique FantasyData Season ID. SeasonIDs can be found in the Competitions and Competition Details endpoints.  Examples: &lt;code&gt;100000023&lt;/code&gt;, &lt;code&gt;100000024&lt;/code&gt;, etc
    :type seasonid: str

    """
    return web.Response(status=200)


async def standings(request: web.Request, format, roundid) -> web.Response:
    """Standings

    Schedule

    :param format: Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;.
    :type format: str
    :param roundid: Unique FantasyData Round ID. RoundIDs can be found in the Competitions and Competition Details endpoints.  Example: &lt;code&gt;100000138&lt;/code&gt;, etc
    :type roundid: str

    """
    return web.Response(status=200)


async def teams(request: web.Request, format) -> web.Response:
    """Teams

    Teams

    :param format: Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;.
    :type format: str

    """
    return web.Response(status=200)


async def venues(request: web.Request, format) -> web.Response:
    """Venues

    Venues

    :param format: Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;.
    :type format: str

    """
    return web.Response(status=200)
