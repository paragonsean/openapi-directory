from typing import List, Dict
from aiohttp import web

from openapi_server.models.activity import Activity
from openapi_server.models.activity_list import ActivityList
from openapi_server.models.comment import Comment
from openapi_server.models.comment_list import CommentList
from openapi_server.models.error import Error
from openapi_server.models.new_sales_activity import NewSalesActivity
from openapi_server.models.operation_status import OperationStatus
from openapi_server.models.sales_activities import SalesActivities
from openapi_server.models.sales_activity_type import SalesActivityType
from openapi_server import util


async def get_activities(request: web.Request, project_id, page=None, per_page=None) -> web.Response:
    """Monitor project activities

    Get a list of real-time activities in the project, such as translation suggestion and translation approval.

    :param project_id: Project ID
    :type project_id: int
    :param page: 
    :type page: int
    :param per_page: 
    :type per_page: int

    """
    return web.Response(status=200)


async def get_activity(request: web.Request, project_id, activity_id) -> web.Response:
    """View an activity

    View the details of an activity in the project.

    :param project_id: Project ID
    :type project_id: int
    :param activity_id: Activity ID
    :type activity_id: int

    """
    return web.Response(status=200)


async def get_activity_comments(request: web.Request, project_id, activity_id) -> web.Response:
    """View activity comments

    View a list of comments added to this activity.

    :param project_id: Project ID
    :type project_id: int
    :param activity_id: Activity ID
    :type activity_id: int

    """
    return web.Response(status=200)


async def get_comments(request: web.Request, project_id, page=None, per_page=None) -> web.Response:
    """View all project comments

    View a list of activity comments in the project.

    :param project_id: Project ID
    :type project_id: int
    :param page: 
    :type page: int
    :param per_page: 
    :type per_page: int

    """
    return web.Response(status=200)


async def get_sales_activities(request: web.Request, id, exclude_owner=None, type=None) -> web.Response:
    """Get sales activities for a project

    

    :param id: Project ID
    :type id: int
    :param exclude_owner: 
    :type exclude_owner: str
    :param type: 
    :type type: dict | bytes

    """
    type = .from_dict(type)
    return web.Response(status=200)


async def insert_sales_activity(request: web.Request, id, body=None) -> web.Response:
    """Insert sales activity for a project

    

    :param id: Project ID
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = NewSalesActivity.from_dict(body)
    return web.Response(status=200)


async def submit_comment(request: web.Request, project_id, activity_id, body=None) -> web.Response:
    """Submit comment to an activity

    Submit a comment to an activity in the project, such as translation or editing.

    :param project_id: Project ID
    :type project_id: int
    :param activity_id: Activity ID
    :type activity_id: int
    :param body: 
    :type body: dict | bytes

    """
    body = Comment.from_dict(body)
    return web.Response(status=200)
