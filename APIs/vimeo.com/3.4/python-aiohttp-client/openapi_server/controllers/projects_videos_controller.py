from typing import List, Dict
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.video import Video
from openapi_server import util


async def add_video_to_project(request: web.Request, project_id, user_id, video_id) -> web.Response:
    """Add a specific video to a project

    This method adds a single video to the specified project.

    :param project_id: The ID of the project.
    :type project_id: 
    :param user_id: The ID of the user.
    :type user_id: 
    :param video_id: The ID of the video.
    :type video_id: 

    """
    return web.Response(status=200)


async def add_video_to_project_alt1(request: web.Request, project_id, video_id) -> web.Response:
    """Add a specific video to a project

    This method adds a single video to the specified project.

    :param project_id: The ID of the project.
    :type project_id: 
    :param video_id: The ID of the video.
    :type video_id: 

    """
    return web.Response(status=200)


async def add_videos_to_project(request: web.Request, project_id, user_id, uris) -> web.Response:
    """Add a list of videos to a project

    This method adds multiple videos to the specified project.

    :param project_id: The ID of the project.
    :type project_id: 
    :param user_id: The ID of the user.
    :type user_id: 
    :param uris: A comma-separated list of video URIs to add.
    :type uris: str

    """
    return web.Response(status=200)


async def add_videos_to_project_alt1(request: web.Request, project_id, uris) -> web.Response:
    """Add a list of videos to a project

    This method adds multiple videos to the specified project.

    :param project_id: The ID of the project.
    :type project_id: 
    :param uris: A comma-separated list of video URIs to add.
    :type uris: str

    """
    return web.Response(status=200)


async def get_project_videos(request: web.Request, project_id, user_id, direction=None, page=None, per_page=None, sort=None) -> web.Response:
    """Get all the videos in a project

    This method gets all the videos that belong to the specified project.

    :param project_id: The ID of the project.
    :type project_id: 
    :param user_id: The ID of the user.
    :type user_id: 
    :param direction: The sort direction of the results.
    :type direction: str
    :param page: The page number of the results to show.
    :type page: 
    :param per_page: The number of items to show on each page of results, up to a maximum of 100.
    :type per_page: 
    :param sort: The way to sort the results.
    :type sort: str

    """
    return web.Response(status=200)


async def get_project_videos_alt1(request: web.Request, project_id, direction=None, page=None, per_page=None, sort=None) -> web.Response:
    """Get all the videos in a project

    This method gets all the videos that belong to the specified project.

    :param project_id: The ID of the project.
    :type project_id: 
    :param direction: The sort direction of the results.
    :type direction: str
    :param page: The page number of the results to show.
    :type page: 
    :param per_page: The number of items to show on each page of results, up to a maximum of 100.
    :type per_page: 
    :param sort: The way to sort the results.
    :type sort: str

    """
    return web.Response(status=200)


async def remove_video_from_project(request: web.Request, project_id, user_id, video_id) -> web.Response:
    """Remove a specific video from a project

    This method removes a single video from the specified project.

    :param project_id: The ID of the project.
    :type project_id: 
    :param user_id: The ID of the user.
    :type user_id: 
    :param video_id: The ID of the video.
    :type video_id: 

    """
    return web.Response(status=200)


async def remove_video_from_project_alt1(request: web.Request, project_id, video_id) -> web.Response:
    """Remove a specific video from a project

    This method removes a single video from the specified project.

    :param project_id: The ID of the project.
    :type project_id: 
    :param video_id: The ID of the video.
    :type video_id: 

    """
    return web.Response(status=200)


async def remove_videos_from_project(request: web.Request, project_id, user_id, uris, should_delete_clips=None) -> web.Response:
    """Remove a list of videos from a project

    This method removed multiple videos from the specified project.

    :param project_id: The ID of the project.
    :type project_id: 
    :param user_id: The ID of the user.
    :type user_id: 
    :param uris: A comma-separated list of the video URIs to remove.
    :type uris: str
    :param should_delete_clips: Whether to delete the videos when removing them from the project.
    :type should_delete_clips: bool

    """
    return web.Response(status=200)


async def remove_videos_from_project_alt1(request: web.Request, project_id, uris, should_delete_clips=None) -> web.Response:
    """Remove a list of videos from a project

    This method removed multiple videos from the specified project.

    :param project_id: The ID of the project.
    :type project_id: 
    :param uris: A comma-separated list of the video URIs to remove.
    :type uris: str
    :param should_delete_clips: Whether to delete the videos when removing them from the project.
    :type should_delete_clips: bool

    """
    return web.Response(status=200)
