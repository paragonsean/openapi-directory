from typing import List, Dict
from aiohttp import web

from openapi_server.models.api_exception import ApiException
from openapi_server.models.api_response import ApiResponse
from openapi_server.models.article_dto import ArticleDTO
from openapi_server.models.default_response_dtoof_article_dto import DefaultResponseDTOOfArticleDTO
from openapi_server.models.default_response_dtoof_integer import DefaultResponseDTOOfInteger
from openapi_server.models.default_response_dtoof_list_of_article_search_dto import DefaultResponseDTOOfListOfArticleSearchDTO
from openapi_server.models.default_response_dtoof_status_dto import DefaultResponseDTOOfStatusDTO
from openapi_server.models.gym_article_details_dto import GymArticleDetailsDTO
from openapi_server.models.measure_unit_dto import MeasureUnitDTO
from openapi_server import util


async def article_add_measure_unit(request: web.Request, body) -> web.Response:
    """Add measure unit

    

    :param body: list of measureUnit
    :type body: list | bytes

    """
    body = [MeasureUnitDTO.from_dict(d) for d in body]
    return web.Response(status=200)


async def article_delete(request: web.Request, article_id=None) -> web.Response:
    """Delete article from the system             

    

    :param article_id: indentity number(primary key) for article object
    :type article_id: int

    """
    return web.Response(status=200)


async def article_get(request: web.Request, article_id) -> web.Response:
    """Get article details This will return all properties related to article entity             

    

    :param article_id: indentity number (primary key) for article object
    :type article_id: int

    """
    return web.Response(status=200)


async def article_get_addons(request: web.Request, search_text=None, gym_ids=None, type=None, limit=None, offset=None) -> web.Response:
    """article_get_addons

    

    :param search_text: Search text - will be search by the name
    :type search_text: str
    :param gym_ids: Comma separated gymIds deafult \&quot;-1\&quot; for all gyms
    :type gym_ids: str
    :param type: 
    :type type: str
    :param limit: 
    :type limit: int
    :param offset: 
    :type offset: int

    """
    return web.Response(status=200)


async def article_get_measure_units(request: web.Request, type=None) -> web.Response:
    """Get mesure units

    

    :param type: type of the measure unit (all, item, service)
    :type type: str

    """
    return web.Response(status=200)


async def article_get_revenue_accounts(request: web.Request, ) -> web.Response:
    """Get Revenue Accounts 

    


    """
    return web.Response(status=200)


async def article_gym_article_details(request: web.Request, article_id, gym_id) -> web.Response:
    """Get Gym specific properties for article             

    

    :param article_id: indentity number(primary key) for article object
    :type article_id: int
    :param gym_id: indentity number(primary key) for gym object
    :type gym_id: int

    """
    return web.Response(status=200)


async def article_post(request: web.Request, body) -> web.Response:
    """Add new article             

    

    :param body: article object
    :type body: dict | bytes

    """
    body = ArticleDTO.from_dict(body)
    return web.Response(status=200)


async def article_put(request: web.Request, body) -> web.Response:
    """update existing article             

    

    :param body: article object
    :type body: dict | bytes

    """
    body = ArticleDTO.from_dict(body)
    return web.Response(status=200)


async def article_search(request: web.Request, search_text=None, gym_id=None, type=None, order_by=None, limit=None, offset=None, active_status=None) -> web.Response:
    """Search articles It will only return basic information of article             

    

    :param search_text: part of article name
    :type search_text: str
    :param gym_id: -1 for all gyms 
    :type gym_id: int
    :param type: filter article type. default is &#39;all&#39;
    :type type: str
    :param order_by: order by column.!-- invalid column will give internal server error
    :type order_by: str
    :param limit: number of recode in result and default is 100. use negative numbers to order by desc
    :type limit: int
    :param offset: number of recodes to skip
    :type offset: int
    :param active_status: Active Status 1 : Active, 2: Inactive, 3: All, Default : 1
    :type active_status: int

    """
    return web.Response(status=200)


async def article_update_article_gym_details(request: web.Request, body) -> web.Response:
    """Add article details that associate with a Gym             

    

    :param body: 
    :type body: list | bytes

    """
    body = [GymArticleDetailsDTO.from_dict(d) for d in body]
    return web.Response(status=200)


async def article_update_status(request: web.Request, article_id=None, status=None, user_name=None) -> web.Response:
    """Deactivate existing article 

    

    :param article_id: 
    :type article_id: int
    :param status: 1 : activate , 2 deactivate
    :type status: int
    :param user_name: Updating user
    :type user_name: str

    """
    return web.Response(status=200)
