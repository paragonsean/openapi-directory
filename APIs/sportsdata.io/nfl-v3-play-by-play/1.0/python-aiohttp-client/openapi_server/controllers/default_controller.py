from typing import List, Dict
from aiohttp import web

from openapi_server.models.play_by_play import PlayByPlay
from openapi_server import util


async def play_by_play(request: web.Request, format, season, week, hometeam) -> web.Response:
    """Play By Play

    

    :param format: Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;.
    :type format: str
    :param season: Year of the season and the season type. If no season type is provided, then the default is regular season.           &lt;br&gt;Examples: &lt;code&gt;2015REG&lt;/code&gt;, &lt;code&gt;2015PRE&lt;/code&gt;, &lt;code&gt;2015POST&lt;/code&gt;.         
    :type season: str
    :param week: Week of the season. Valid values are as follows: Preseason 0 to 4, Regular Season 1 to 17, Postseason 1 to 4.           Example: &lt;code&gt;1&lt;/code&gt;         
    :type week: str
    :param hometeam: Abbreviation of the home team. Example: &lt;code&gt;WAS&lt;/code&gt;.
    :type hometeam: str

    """
    return web.Response(status=200)


async def play_by_play_delta(request: web.Request, format, season, week, minutes) -> web.Response:
    """Play By Play Delta

    

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


async def play_by_play_simulation(request: web.Request, format, numberofplays) -> web.Response:
    """Play By Play Simulation

    Gets simulated live play-by-play of NFL games, covering the Conference Championship games on January 21, 2018.

    :param format: Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;.
    :type format: str
    :param numberofplays: The number of plays to progress in this NFL live game simulation. Example entries are &lt;code&gt;0&lt;/code&gt;, &lt;code&gt;1&lt;/code&gt;, &lt;code&gt;2&lt;/code&gt;, &lt;code&gt;3&lt;/code&gt;, &lt;code&gt;150&lt;/code&gt;, &lt;code&gt;200&lt;/code&gt;, etc.
    :type numberofplays: str

    """
    return web.Response(status=200)
