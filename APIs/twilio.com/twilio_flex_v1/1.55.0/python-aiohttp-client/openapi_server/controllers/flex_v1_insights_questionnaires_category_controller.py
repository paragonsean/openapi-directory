from typing import List, Dict
from aiohttp import web

from openapi_server.models.flex_v1_insights_questionnaires_category import FlexV1InsightsQuestionnairesCategory
from openapi_server.models.list_insights_questionnaires_category_response import ListInsightsQuestionnairesCategoryResponse
from openapi_server import util


async def create_insights_questionnaires_category(request: web.Request, name, authorization=None) -> web.Response:
    """create_insights_questionnaires_category

    To create a category for Questions

    :param name: The name of this category.
    :type name: str
    :param authorization: The Authorization HTTP request header
    :type authorization: str

    """
    return web.Response(status=200)


async def delete_insights_questionnaires_category(request: web.Request, category_sid, authorization=None) -> web.Response:
    """delete_insights_questionnaires_category

    

    :param category_sid: The SID of the category to be deleted
    :type category_sid: str
    :param authorization: The Authorization HTTP request header
    :type authorization: str

    """
    return web.Response(status=200)


async def list_insights_questionnaires_category(request: web.Request, authorization=None, page_size=None, page=None, page_token=None) -> web.Response:
    """list_insights_questionnaires_category

    To get all the categories

    :param authorization: The Authorization HTTP request header
    :type authorization: str
    :param page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
    :type page_size: int
    :param page: The page index. This value is simply for client state.
    :type page: int
    :param page_token: The page token. This is provided by the API.
    :type page_token: str

    """
    return web.Response(status=200)


async def update_insights_questionnaires_category(request: web.Request, category_sid, name, authorization=None) -> web.Response:
    """update_insights_questionnaires_category

    To update the category for Questions

    :param category_sid: The SID of the category to be updated
    :type category_sid: str
    :param name: The name of this category.
    :type name: str
    :param authorization: The Authorization HTTP request header
    :type authorization: str

    """
    return web.Response(status=200)
