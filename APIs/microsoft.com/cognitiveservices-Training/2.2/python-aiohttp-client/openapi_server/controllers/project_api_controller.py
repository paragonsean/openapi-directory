from typing import List, Dict
from aiohttp import web

from openapi_server.models.export import Export
from openapi_server.models.image_performance import ImagePerformance
from openapi_server.models.iteration import Iteration
from openapi_server.models.iteration_performance import IterationPerformance
from openapi_server.models.project import Project
from openapi_server import util


async def create_project(request: web.Request, name, training_key, description=None, domain_id=None, classification_type=None) -> web.Response:
    """Create a project.

    

    :param name: Name of the project.
    :type name: str
    :param training_key: 
    :type training_key: str
    :param description: The description of the project.
    :type description: str
    :param domain_id: The id of the domain to use for this project. Defaults to General.
    :type domain_id: str
    :type domain_id: str
    :param classification_type: The type of classifier to create for this project.
    :type classification_type: str

    """
    return web.Response(status=200)


async def delete_iteration(request: web.Request, project_id, iteration_id, training_key) -> web.Response:
    """Delete a specific iteration of a project.

    

    :param project_id: The project id.
    :type project_id: str
    :type project_id: str
    :param iteration_id: The iteration id.
    :type iteration_id: str
    :type iteration_id: str
    :param training_key: 
    :type training_key: str

    """
    return web.Response(status=200)


async def delete_project(request: web.Request, project_id, training_key) -> web.Response:
    """Delete a specific project.

    

    :param project_id: The project id.
    :type project_id: str
    :type project_id: str
    :param training_key: 
    :type training_key: str

    """
    return web.Response(status=200)


async def export_iteration(request: web.Request, project_id, iteration_id, platform, training_key, flavor=None) -> web.Response:
    """Export a trained iteration.

    

    :param project_id: The project id.
    :type project_id: str
    :type project_id: str
    :param iteration_id: The iteration id.
    :type iteration_id: str
    :type iteration_id: str
    :param platform: The target platform.
    :type platform: str
    :param training_key: 
    :type training_key: str
    :param flavor: The flavor of the target platform.
    :type flavor: str

    """
    return web.Response(status=200)


async def get_exports(request: web.Request, project_id, iteration_id, training_key) -> web.Response:
    """Get the list of exports for a specific iteration.

    

    :param project_id: The project id.
    :type project_id: str
    :type project_id: str
    :param iteration_id: The iteration id.
    :type iteration_id: str
    :type iteration_id: str
    :param training_key: 
    :type training_key: str

    """
    return web.Response(status=200)


async def get_image_performance_count(request: web.Request, project_id, iteration_id, training_key, tag_ids=None) -> web.Response:
    """Gets the number of images tagged with the provided {tagIds} that have prediction results from  training for the provided iteration {iterationId}.

    The filtering is on an and/or relationship. For example, if the provided tag ids are for the \&quot;Dog\&quot; and  \&quot;Cat\&quot; tags, then only images tagged with Dog and/or Cat will be returned

    :param project_id: The project id.
    :type project_id: str
    :type project_id: str
    :param iteration_id: The iteration id. Defaults to workspace.
    :type iteration_id: str
    :type iteration_id: str
    :param training_key: 
    :type training_key: str
    :param tag_ids: A list of tags ids to filter the images to count. Defaults to all tags when null.
    :type tag_ids: List[str]

    """
    return web.Response(status=200)


async def get_image_performances(request: web.Request, project_id, iteration_id, training_key, tag_ids=None, order_by=None, take=None, skip=None) -> web.Response:
    """Get image with its prediction for a given project iteration.

    This API supports batching and range selection. By default it will only return first 50 images matching images.  Use the {take} and {skip} parameters to control how many images to return in a given batch.  The filtering is on an and/or relationship. For example, if the provided tag ids are for the \&quot;Dog\&quot; and  \&quot;Cat\&quot; tags, then only images tagged with Dog and/or Cat will be returned

    :param project_id: The project id.
    :type project_id: str
    :type project_id: str
    :param iteration_id: The iteration id. Defaults to workspace.
    :type iteration_id: str
    :type iteration_id: str
    :param training_key: 
    :type training_key: str
    :param tag_ids: A list of tags ids to filter the images. Defaults to all tagged images when null. Limited to 20.
    :type tag_ids: List[str]
    :param order_by: The ordering. Defaults to newest.
    :type order_by: str
    :param take: Maximum number of images to return. Defaults to 50, limited to 256.
    :type take: int
    :param skip: Number of images to skip before beginning the image batch. Defaults to 0.
    :type skip: int

    """
    return web.Response(status=200)


async def get_iteration(request: web.Request, project_id, iteration_id, training_key) -> web.Response:
    """Get a specific iteration.

    

    :param project_id: The id of the project the iteration belongs to.
    :type project_id: str
    :type project_id: str
    :param iteration_id: The id of the iteration to get.
    :type iteration_id: str
    :type iteration_id: str
    :param training_key: 
    :type training_key: str

    """
    return web.Response(status=200)


async def get_iteration_performance(request: web.Request, project_id, iteration_id, training_key, threshold=None, overlap_threshold=None) -> web.Response:
    """Get detailed performance information about an iteration.

    

    :param project_id: The id of the project the iteration belongs to.
    :type project_id: str
    :type project_id: str
    :param iteration_id: The id of the iteration to get.
    :type iteration_id: str
    :type iteration_id: str
    :param training_key: 
    :type training_key: str
    :param threshold: The threshold used to determine true predictions.
    :type threshold: float
    :param overlap_threshold: If applicable, the bounding box overlap threshold used to determine true predictions.
    :type overlap_threshold: float

    """
    return web.Response(status=200)


async def get_iterations(request: web.Request, project_id, training_key) -> web.Response:
    """Get iterations for the project.

    

    :param project_id: The project id.
    :type project_id: str
    :type project_id: str
    :param training_key: 
    :type training_key: str

    """
    return web.Response(status=200)


async def get_project(request: web.Request, project_id, training_key) -> web.Response:
    """Get a specific project.

    

    :param project_id: The id of the project to get.
    :type project_id: str
    :type project_id: str
    :param training_key: 
    :type training_key: str

    """
    return web.Response(status=200)


async def get_projects(request: web.Request, training_key) -> web.Response:
    """Get your projects.

    

    :param training_key: 
    :type training_key: str

    """
    return web.Response(status=200)


async def train_project(request: web.Request, project_id, training_key) -> web.Response:
    """Queues project for training.

    

    :param project_id: The project id.
    :type project_id: str
    :type project_id: str
    :param training_key: 
    :type training_key: str

    """
    return web.Response(status=200)


async def update_iteration(request: web.Request, project_id, iteration_id, training_key, body) -> web.Response:
    """Update a specific iteration.

    

    :param project_id: Project id.
    :type project_id: str
    :type project_id: str
    :param iteration_id: Iteration id.
    :type iteration_id: str
    :type iteration_id: str
    :param training_key: 
    :type training_key: str
    :param body: The updated iteration model.
    :type body: dict | bytes

    """
    body = Iteration.from_dict(body)
    return web.Response(status=200)


async def update_project(request: web.Request, project_id, training_key, body) -> web.Response:
    """Update a specific project.

    

    :param project_id: The id of the project to update.
    :type project_id: str
    :type project_id: str
    :param training_key: 
    :type training_key: str
    :param body: The updated project model.
    :type body: dict | bytes

    """
    body = Project.from_dict(body)
    return web.Response(status=200)
