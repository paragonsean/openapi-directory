from typing import List, Dict
from aiohttp import web

from openapi_server.models.log_read import LogRead
from openapi_server import util


async def get_log_collection(request: web.Request, page=None, project_id=None, created_at=None, source=None, target=None, status_code=None, referrer=None, user_agent=None, user_agent_type=None, simplified_user_agent=None, rule_id=None, instance_name=None, exclude_urls=None, exclude_empty_referrer=None, created_at_gt=None, created_at_gte=None, created_at_lt=None, created_at_lte=None, status_code_gt=None, status_code_gte=None, status_code_lt=None, status_code_lte=None) -> web.Response:
    """Retrieves the collection of Log resources.

    

    :param page: The collection page number
    :type page: int
    :param project_id: 
    :type project_id: str
    :param created_at: 
    :type created_at: str
    :param source: 
    :type source: str
    :param target: 
    :type target: str
    :param status_code: 
    :type status_code: str
    :param referrer: 
    :type referrer: str
    :param user_agent: 
    :type user_agent: str
    :param user_agent_type: 
    :type user_agent_type: str
    :param simplified_user_agent: 
    :type simplified_user_agent: str
    :param rule_id: 
    :type rule_id: str
    :param instance_name: 
    :type instance_name: str
    :param exclude_urls: 
    :type exclude_urls: str
    :param exclude_empty_referrer: 
    :type exclude_empty_referrer: str
    :param created_at_gt: 
    :type created_at_gt: str
    :param created_at_gte: 
    :type created_at_gte: str
    :param created_at_lt: 
    :type created_at_lt: str
    :param created_at_lte: 
    :type created_at_lte: str
    :param status_code_gt: 
    :type status_code_gt: str
    :param status_code_gte: 
    :type status_code_gte: str
    :param status_code_lt: 
    :type status_code_lt: str
    :param status_code_lte: 
    :type status_code_lte: str

    """
    return web.Response(status=200)


async def get_log_item(request: web.Request, id) -> web.Response:
    """Retrieves a Log resource.

    

    :param id: 
    :type id: str

    """
    return web.Response(status=200)
