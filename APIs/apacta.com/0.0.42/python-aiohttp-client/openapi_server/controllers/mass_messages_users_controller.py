from typing import List, Dict
from aiohttp import web

from openapi_server.models.clocking_records_clocking_record_id_put200_response import ClockingRecordsClockingRecordIdPut200Response
from openapi_server.models.mass_messages_users_get200_response import MassMessagesUsersGet200Response
from openapi_server.models.mass_messages_users_mass_messages_user_id_get200_response import MassMessagesUsersMassMessagesUserIdGet200Response
from openapi_server import util


async def mass_messages_users_get(request: web.Request, is_read=None) -> web.Response:
    """View list of mass messages for specific user

    

    :param is_read: Used to filter on the &#x60;is_read&#x60; of the mass messages
    :type is_read: bool

    """
    return web.Response(status=200)


async def mass_messages_users_mass_messages_user_id_get(request: web.Request, mass_messages_user_id) -> web.Response:
    """View mass message

    

    :param mass_messages_user_id: 
    :type mass_messages_user_id: str

    """
    return web.Response(status=200)


async def mass_messages_users_mass_messages_user_id_put(request: web.Request, mass_messages_user_id) -> web.Response:
    """Edit mass message

    

    :param mass_messages_user_id: 
    :type mass_messages_user_id: str

    """
    return web.Response(status=200)
