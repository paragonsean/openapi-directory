from typing import List, Dict
from aiohttp import web

from openapi_server.models.device_profile import DeviceProfile
from openapi_server.models.device_profile_info import DeviceProfileInfo
from openapi_server.models.problem_details import ProblemDetails
from openapi_server import util


async def create_profile(request: web.Request, body=None) -> web.Response:
    """Creates a profile.

    

    :param body: Device profile.
    :type body: dict | bytes

    """
    body = DeviceProfile.from_dict(body)
    return web.Response(status=200)


async def delete_profile(request: web.Request, profile_id) -> web.Response:
    """Deletes a profile.

    

    :param profile_id: Profile id.
    :type profile_id: str

    """
    return web.Response(status=200)


async def get_default_profile(request: web.Request, ) -> web.Response:
    """Gets the default profile.

    


    """
    return web.Response(status=200)


async def get_profile(request: web.Request, profile_id) -> web.Response:
    """Gets a single profile.

    

    :param profile_id: Profile Id.
    :type profile_id: str

    """
    return web.Response(status=200)


async def get_profile_infos(request: web.Request, ) -> web.Response:
    """Get profile infos.

    


    """
    return web.Response(status=200)


async def update_profile(request: web.Request, profile_id, body=None) -> web.Response:
    """Updates a profile.

    

    :param profile_id: Profile id.
    :type profile_id: str
    :param body: Device profile.
    :type body: dict | bytes

    """
    body = DeviceProfile.from_dict(body)
    return web.Response(status=200)
