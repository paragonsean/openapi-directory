from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def applicant_delete_attributes_v2(request: web.Request, email, name, pool=None, common_app_year=None) -> web.Response:
    """Deletes a custom attribute for an applicant.

    

    :param email: The email address of the applicant.
    :type email: str
    :param name: The name of the attribute to be deleted.
    :type name: str
    :param pool: 
    :type pool: str
    :param common_app_year: 
    :type common_app_year: int

    """
    return web.Response(status=200)


async def applicant_get_attribute_names_v2(request: web.Request, ) -> web.Response:
    """Gets the custom applicant attributes used by the organization.

    


    """
    return web.Response(status=200)


async def applicant_get_attributes_v2(request: web.Request, email, pool=None, common_app_year=None) -> web.Response:
    """Gets the custom attributes for an applicant.

    

    :param email: The email address of the applicant.
    :type email: str
    :param pool: 
    :type pool: str
    :param common_app_year: 
    :type common_app_year: int

    """
    return web.Response(status=200)


async def applicant_post_attributes_v2(request: web.Request, email, data, pool=None, common_app_year=None) -> web.Response:
    """Updates the custom attributes for an applicant.

    This method only adds or updates attributes. Null values will be updated as nulls, but not deleted. API Import is available in the Advanced Plan.

    :param email: The email address of the applicant.
    :type email: str
    :param data: The name/value pairs of the attributes.
    :type data: Dict[str, str]
    :param pool: 
    :type pool: str
    :param common_app_year: 
    :type common_app_year: int

    """
    return web.Response(status=200)
