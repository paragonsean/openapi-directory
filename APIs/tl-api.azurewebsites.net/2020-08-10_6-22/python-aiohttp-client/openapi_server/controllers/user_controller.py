from typing import List, Dict
from aiohttp import web

from openapi_server.models.user_dto import UserDTO
from openapi_server import util


async def user_get(request: web.Request, ) -> web.Response:
    """Get all Users detail This will return all properties related to User entity             

    


    """
    return web.Response(status=200)


async def user_register_user(request: web.Request, user_id=None, account_number=None, gym_number=None, external_entity_number=None, name=None, number=None, introduce_by=None, guardian=None, type_id=None) -> web.Response:
    """Register a new User             

    

    :param user_id: Indentity number(primary key) for user object. Generated in DB table when inserting a record.             
    :type user_id: int
    :param account_number: Account number of the user.It can be any stakeholder of the application.even can be a gym.             
    :type account_number: str
    :param gym_number: If this user is a gym, then the gym number.             
    :type gym_number: str
    :param external_entity_number: Entity number that make a relationship with BOX API DB.             
    :type external_entity_number: str
    :param name: Name of the user.             
    :type name: str
    :param number: Unique number maintain by application to idenify user.             
    :type number: str
    :param introduce_by: If Someone introduced this user to the system, then that user&#39;s UserId.             
    :type introduce_by: int
    :param guardian: Gaurdian of the this user if he/she is under 18 years old.             
    :type guardian: int
    :param type_id: Type of the user.             
    :type type_id: int

    """
    return web.Response(status=200)


async def user_update_user(request: web.Request, user_id=None, account_number=None, gym_number=None, external_entity_number=None, name=None, number=None, introduce_by=None, guardian=None, type_id=None) -> web.Response:
    """Update an exsisting User             

    

    :param user_id: Indentity number(primary key) for user object. Generated in DB table when inserting a record.             
    :type user_id: int
    :param account_number: Account number of the user.It can be any stakeholder of the application.even can be a gym.             
    :type account_number: str
    :param gym_number: If this user is a gym, then the gym number.             
    :type gym_number: str
    :param external_entity_number: Entity number that make a relationship with BOX API DB.             
    :type external_entity_number: str
    :param name: Name of the user.             
    :type name: str
    :param number: Unique number maintain by application to idenify user.             
    :type number: str
    :param introduce_by: If Someone introduced this user to the system, then that user&#39;s UserId.             
    :type introduce_by: int
    :param guardian: Gaurdian of the this user if he/she is under 18 years old.             
    :type guardian: int
    :param type_id: Type of the user.             
    :type type_id: int

    """
    return web.Response(status=200)
