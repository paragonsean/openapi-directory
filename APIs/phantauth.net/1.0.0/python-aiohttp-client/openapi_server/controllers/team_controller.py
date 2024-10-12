from typing import List, Dict
from aiohttp import web

from openapi_server.models.team_teamname_get200_response import TeamTeamnameGet200Response
from openapi_server import util


async def team_teamname_get(request: web.Request, teamname) -> web.Response:
    """Get a Team

    Use this endpoint to generate a random group of users. The team is generated in a deterministic way, on the basis of the team name given as the path parameter. In the case of identical team names, the endpoint will generate the same team object. The properties of the generated team object are randomly generated on the basis of the team name. In lack of a team name, all calls generate a different team object to the randomly generated team name.

    :param teamname:  The identifier or email address of the team; it is integrated in the &#x60;sub&#x60; property and is the basis of the other generated properties. 
    :type teamname: str

    """
    return web.Response(status=200)
