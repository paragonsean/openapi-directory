from typing import List, Dict
from aiohttp import web

from openapi_server.models.export import Export
from openapi_server.models.iteration import Iteration
from openapi_server.models.iteration_performance import IterationPerformance
from openapi_server.models.project import Project
from openapi_server import util


async def create_project(request: web.Request, name, training_key, description=None, domain_id=None) -> web.Response:
    """Create a project

    

    :param name: Name of the project
    :type name: str
    :param training_key: 
    :type training_key: str
    :param description: The description of the project
    :type description: str
    :param domain_id: The id of the domain to use for this project. Defaults to General
    :type domain_id: str
    :type domain_id: str

    """
    return web.Response(status=200)


async def delete_iteration(request: web.Request, project_id, iteration_id, training_key) -> web.Response:
    """Delete a specific iteration of a project

    

    :param project_id: The project id
    :type project_id: str
    :type project_id: str
    :param iteration_id: The iteration id
    :type iteration_id: str
    :type iteration_id: str
    :param training_key: 
    :type training_key: str

    """
    return web.Response(status=200)


async def delete_project(request: web.Request, project_id, training_key) -> web.Response:
    """Delete a specific project

    

    :param project_id: The project id
    :type project_id: str
    :type project_id: str
    :param training_key: 
    :type training_key: str

    """
    return web.Response(status=200)


async def export_iteration(request: web.Request, project_id, iteration_id, platform, training_key) -> web.Response:
    """Export a trained iteration

    

    :param project_id: The project id
    :type project_id: str
    :type project_id: str
    :param iteration_id: The iteration id
    :type iteration_id: str
    :type iteration_id: str
    :param platform: The target platform (coreml or tensorflow)
    :type platform: str
    :param training_key: 
    :type training_key: str

    """
    return web.Response(status=200)


async def get_exports(request: web.Request, project_id, iteration_id, training_key) -> web.Response:
    """Get the list of exports for a specific iteration

    

    :param project_id: The project id
    :type project_id: str
    :type project_id: str
    :param iteration_id: The iteration id
    :type iteration_id: str
    :type iteration_id: str
    :param training_key: 
    :type training_key: str

    """
    return web.Response(status=200)


async def get_iteration(request: web.Request, project_id, iteration_id, training_key) -> web.Response:
    """Get a specific iteration

    

    :param project_id: The id of the project the iteration belongs to
    :type project_id: str
    :type project_id: str
    :param iteration_id: The id of the iteration to get
    :type iteration_id: str
    :type iteration_id: str
    :param training_key: 
    :type training_key: str

    """
    return web.Response(status=200)


async def get_iteration_performance(request: web.Request, project_id, iteration_id, threshold, training_key) -> web.Response:
    """Get detailed performance information about a trained iteration

    

    :param project_id: The project id
    :type project_id: str
    :type project_id: str
    :param iteration_id: The id of the trained iteration
    :type iteration_id: str
    :type iteration_id: str
    :param threshold: The 0 to 1 threshold to determine positive prediction
    :type threshold: float
    :param training_key: 
    :type training_key: str

    """
    return web.Response(status=200)


async def get_iterations(request: web.Request, project_id, training_key) -> web.Response:
    """Get iterations for the project

    

    :param project_id: The project id
    :type project_id: str
    :type project_id: str
    :param training_key: 
    :type training_key: str

    """
    return web.Response(status=200)


async def get_project(request: web.Request, project_id, training_key) -> web.Response:
    """Get a specific project

    

    :param project_id: The id of the project to get
    :type project_id: str
    :type project_id: str
    :param training_key: 
    :type training_key: str

    """
    return web.Response(status=200)


async def get_projects(request: web.Request, training_key) -> web.Response:
    """Get your projects

    

    :param training_key: 
    :type training_key: str

    """
    return web.Response(status=200)


async def train_project(request: web.Request, project_id, training_key) -> web.Response:
    """Queues project for training

    

    :param project_id: The project id
    :type project_id: str
    :type project_id: str
    :param training_key: 
    :type training_key: str

    """
    return web.Response(status=200)


async def update_iteration(request: web.Request, project_id, iteration_id, training_key, body) -> web.Response:
    """Update a specific iteration

    

    :param project_id: Project id
    :type project_id: str
    :type project_id: str
    :param iteration_id: Iteration id
    :type iteration_id: str
    :type iteration_id: str
    :param training_key: 
    :type training_key: str
    :param body: The updated iteration model
    :type body: dict | bytes

    """
    body = Iteration.from_dict(body)
    return web.Response(status=200)


async def update_project(request: web.Request, project_id, training_key, body) -> web.Response:
    """Update a specific project

    

    :param project_id: The id of the project to update
    :type project_id: str
    :type project_id: str
    :param training_key: 
    :type training_key: str
    :param body: The updated project model
    :type body: dict | bytes

    """
    body = Project.from_dict(body)
    return web.Response(status=200)
