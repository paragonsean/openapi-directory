from typing import List, Dict
from aiohttp import web

from openapi_server.models.adult_content_post_request import AdultContentPostRequest
from openapi_server.models.task import Task
from openapi_server import util


async def adult_content_post(request: web.Request, body) -> web.Response:
    """Image contains nudity or sexually explicit content? [ image_url -&gt; id ]

    Creates a new adult_content task that tells the if the image has nudity or sexual content.

    :param body: The image to analyze
    :type body: dict | bytes

    """
    body = AdultContentPostRequest.from_dict(body)
    return web.Response(status=200)


async def adult_content_task_id_get(request: web.Request, task_id) -> web.Response:
    """Gets the adult_content task [ id -&gt; adult content task ]

    Gets the adult_content task.

    :param task_id: An internal id for the task
    :type task_id: str

    """
    return web.Response(status=200)


async def detect_object_post(request: web.Request, body) -> web.Response:
    """What is that object? [ image_url -&gt; id ]

    Creates a new detect object task that recognizes the object in the image.

    :param body: The image to analyze
    :type body: dict | bytes

    """
    body = AdultContentPostRequest.from_dict(body)
    return web.Response(status=200)


async def detect_object_task_id_get(request: web.Request, task_id) -> web.Response:
    """Gets the detect_object task [ id -&gt; detect object task]

    Gets the detect_object task.

    :param task_id: An internal id for the task
    :type task_id: str

    """
    return web.Response(status=200)


async def face_age_post(request: web.Request, body) -> web.Response:
    """How old is the person in the image? [ image_url -&gt; id ]

    Creates a new face age task that approximates the age of the person in the image.

    :param body: The image to analyze
    :type body: dict | bytes

    """
    body = AdultContentPostRequest.from_dict(body)
    return web.Response(status=200)


async def face_age_task_id_get(request: web.Request, task_id) -> web.Response:
    """Gets the face_age task [ id -&gt; face age task ]

    Gets the face_age task.

    :param task_id: An internal id for the task
    :type task_id: str

    """
    return web.Response(status=200)


async def face_post(request: web.Request, body) -> web.Response:
    """Find all faces in the image [ image_url -&gt; id ]

    Get a list of all the locations of the faces in the image.

    :param body: The image to analyze
    :type body: dict | bytes

    """
    body = AdultContentPostRequest.from_dict(body)
    return web.Response(status=200)


async def face_task_id_get(request: web.Request, task_id) -> web.Response:
    """Gets the face task [ id -&gt; face task ]

    Gets the face task.

    :param task_id: An internal id for the task
    :type task_id: str

    """
    return web.Response(status=200)
