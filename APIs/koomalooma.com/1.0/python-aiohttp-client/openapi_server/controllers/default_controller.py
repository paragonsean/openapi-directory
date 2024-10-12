from typing import List, Dict
from aiohttp import web

from openapi_server.models.commitment import Commitment
from openapi_server.models.commitment_request import CommitmentRequest
from openapi_server.models.user import User
from openapi_server import util


async def users_post(request: web.Request, ) -> web.Response:
    """Create a User

    


    """
    return web.Response(status=200)


async def users_user_id_commitments_post(request: web.Request, user_id, commitment_request) -> web.Response:
    """Assign points to a User

    

    :param user_id: user_id of the user to assign points to
    :type user_id: str
    :param commitment_request: 
    :type commitment_request: dict | bytes

    """
    commitment_request = CommitmentRequest.from_dict(commitment_request)
    return web.Response(status=200)
