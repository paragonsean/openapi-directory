from typing import List, Dict
from aiohttp import web

from openapi_server.models.http_status_vo import HTTPStatusVO
from openapi_server.models.task_created_vo import TaskCreatedVO
from openapi_server.models.task_expand_vo import TaskExpandVO
from openapi_server.models.task_expand_workgroup_level_vo import TaskExpandWorkgroupLevelVO
from openapi_server.models.task_list_vo import TaskListVO
from openapi_server.models.task_persist_vo import TaskPersistVO
from openapi_server.models.task_priority_list_vo import TaskPriorityListVO
from openapi_server.models.task_status_list_vo import TaskStatusListVO
from openapi_server.models.task_type_list_vo import TaskTypeListVO
from openapi_server.models.task_workgroup_level_list_vo import TaskWorkgroupLevelListVO
from openapi_server.models.wg_task_status_list_vo import WgTaskStatusListVO
from openapi_server import util


async def get_custom_task_types_of_wg(request: web.Request, workgroup_id) -> web.Response:
    """Get custom task types of workgroup level

    Get custom task types of workgroup level

    :param workgroup_id: 
    :type workgroup_id: str

    """
    return web.Response(status=200)


async def get_default_task_status_list(request: web.Request, workgroup_id) -> web.Response:
    """Get default task status list

    Get default task status list

    :param workgroup_id: 
    :type workgroup_id: str

    """
    return web.Response(status=200)


async def get_task_list_of_project(request: web.Request, workgroup_id, project_id) -> web.Response:
    """Get task list of project level

    Get task list of project level

    :param workgroup_id: 
    :type workgroup_id: str
    :param project_id: 
    :type project_id: str

    """
    return web.Response(status=200)


async def get_task_list_of_workgroup(request: web.Request, workgroup_id) -> web.Response:
    """Get task list of workgroup level

    Get task list of workgroup level

    :param workgroup_id: 
    :type workgroup_id: str

    """
    return web.Response(status=200)


async def get_task_of_project(request: web.Request, workgroup_id, project_id, task_id) -> web.Response:
    """Get a sepcific task of project level

    Get a sepcific task of project level

    :param workgroup_id: 
    :type workgroup_id: str
    :param project_id: 
    :type project_id: str
    :param task_id: 
    :type task_id: str

    """
    return web.Response(status=200)


async def get_task_of_workgroup(request: web.Request, workgroup_id, task_id) -> web.Response:
    """Get a sepcific task of workgroup level

    Get a sepcific task of workgroup level

    :param workgroup_id: 
    :type workgroup_id: str
    :param task_id: 
    :type task_id: str

    """
    return web.Response(status=200)


async def get_task_types_of_workgroup(request: web.Request, workgroup_id) -> web.Response:
    """Get task types of workgroup level

    Get task types of workgroup level

    :param workgroup_id: 
    :type workgroup_id: str

    """
    return web.Response(status=200)


async def get_wg_task_status_list_of_workgroup(request: web.Request, workgroup_id) -> web.Response:
    """Get custom task status of workgroup level

    Get custom task status of workgroup level

    :param workgroup_id: 
    :type workgroup_id: str

    """
    return web.Response(status=200)


async def post_task_for_project(request: web.Request, workgroup_id, project_id, body=None) -> web.Response:
    """Create a new task

    Create a new task

    :param workgroup_id: 
    :type workgroup_id: str
    :param project_id: 
    :type project_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = TaskPersistVO.from_dict(body)
    return web.Response(status=200)


async def task_priority_list(request: web.Request, workgroup_id) -> web.Response:
    """Get default task priority list

    Get default task priority list

    :param workgroup_id: 
    :type workgroup_id: str

    """
    return web.Response(status=200)
