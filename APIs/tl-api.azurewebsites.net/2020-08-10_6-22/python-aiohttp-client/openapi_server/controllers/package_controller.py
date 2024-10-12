from typing import List, Dict
from aiohttp import web

from openapi_server.models.api_exception import ApiException
from openapi_server.models.default_response_dtoof_boolean import DefaultResponseDTOOfBoolean
from openapi_server.models.default_response_dtoof_list_of_package_search_dto import DefaultResponseDTOOfListOfPackageSearchDTO
from openapi_server.models.default_response_dtoof_package_dto import DefaultResponseDTOOfPackageDTO
from openapi_server.models.default_response_dtoof_package_search_dto import DefaultResponseDTOOfPackageSearchDTO
from openapi_server.models.default_response_dtoof_status_dto import DefaultResponseDTOOfStatusDTO
from openapi_server.models.default_response_dtoof_string import DefaultResponseDTOOfString
from openapi_server.models.package_dto import PackageDTO
from openapi_server import util


async def package_delete(request: web.Request, package_id=None) -> web.Response:
    """Delete existing package             

    

    :param package_id: primary key of package entity
    :type package_id: int

    """
    return web.Response(status=200)


async def package_get(request: web.Request, package_id=None) -> web.Response:
    """Get package details by packageId             

    

    :param package_id: primary key of package entity
    :type package_id: int

    """
    return web.Response(status=200)


async def package_post(request: web.Request, body) -> web.Response:
    """Insert new package into the system             

    

    :param body: package object
    :type body: dict | bytes

    """
    body = PackageDTO.from_dict(body)
    return web.Response(status=200)


async def package_put(request: web.Request, body) -> web.Response:
    """Update existing package by its ID             

    

    :param body: package object
    :type body: dict | bytes

    """
    body = PackageDTO.from_dict(body)
    return web.Response(status=200)


async def package_search(request: web.Request, search_text=None, gym_id=None, type=None, order_by=None, limit=None, offset=None, active_status=None, category_id=None, startp_price=None, end_price=None, request_source=None) -> web.Response:
    """Search packages             

    

    :param search_text: part of package name
    :type search_text: str
    :param gym_id: primary key of TL gym entity
    :type gym_id: int
    :param type: filter package type.!-- default is &#39;all&#39;
    :type type: str
    :param order_by: order by column.!-- invalid column will give internal server error
    :type order_by: str
    :param limit: number of recode in result and default is 100. use negative numbers to order by desc
    :type limit: int
    :param offset: number of recodes to skip
    :type offset: int
    :param active_status: active status active : 1, inactive : 2, all 3, deafult : 1
    :type active_status: int
    :param category_id: Packge Category Id
    :type category_id: int
    :param startp_price: Start price of the price Range
    :type startp_price: 
    :param end_price: End Price of the price Range
    :type end_price: 
    :param request_source: 1 : MRM, 2 : Mobile 
    :type request_source: int

    """
    return web.Response(status=200)


async def package_update_status(request: web.Request, package_id=None, status=None, user_name=None) -> web.Response:
    """Status update of existing package 

    

    :param package_id: package Id
    :type package_id: int
    :param status: status : 1 activate, 2 : deactivate
    :type status: int
    :param user_name: Status updated User
    :type user_name: str

    """
    return web.Response(status=200)
