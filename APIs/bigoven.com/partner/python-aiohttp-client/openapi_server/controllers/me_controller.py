from typing import List, Dict
from aiohttp import web

from openapi_server.models.api2_controllers_web_apime_controller_preference_options import API2ControllersWebAPIMeControllerPreferenceOptions
from openapi_server.models.api2_models_big_oven_user import API2ModelsBigOvenUser
from openapi_server.models.api2_models_personal import API2ModelsPersonal
from openapi_server.models.api2_models_preference import API2ModelsPreference
from openapi_server.models.api2_models_profile import API2ModelsProfile
from openapi_server import util


async def me_get_options(request: web.Request, ) -> web.Response:
    """Gets the options.

    


    """
    return web.Response(status=200)


async def me_index(request: web.Request, ) -> web.Response:
    """Indexes this instance.

    


    """
    return web.Response(status=200)


async def me_profile_put(request: web.Request, body) -> web.Response:
    """Puts me.

    

    :param body: The req.
    :type body: dict | bytes

    """
    body = API2ModelsProfile.from_dict(body)
    return web.Response(status=200)


async def me_put_me(request: web.Request, body) -> web.Response:
    """Puts me.

    

    :param body: The req.
    :type body: dict | bytes

    """
    body = API2ModelsBigOvenUser.from_dict(body)
    return web.Response(status=200)


async def me_put_me_personal(request: web.Request, body) -> web.Response:
    """Puts me personal.

    

    :param body: The req.
    :type body: dict | bytes

    """
    body = API2ModelsPersonal.from_dict(body)
    return web.Response(status=200)


async def me_put_me_preferences(request: web.Request, body) -> web.Response:
    """Puts me preferences.

    

    :param body: The req.
    :type body: dict | bytes

    """
    body = API2ModelsPreference.from_dict(body)
    return web.Response(status=200)


async def me_skinny(request: web.Request, ) -> web.Response:
    """Skinnies this instance.

    


    """
    return web.Response(status=200)
