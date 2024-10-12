from typing import List, Dict
from aiohttp import web

from openapi_server.models.legacy_error import LegacyError
from openapi_server.models.video import Video
from openapi_server import util


async def add_video_to_portfolio(request: web.Request, portfolio_id, user_id, video_id) -> web.Response:
    """Add a video to a portfolio

    

    :param portfolio_id: The ID of the portfolio.
    :type portfolio_id: 
    :param user_id: The ID of the user.
    :type user_id: 
    :param video_id: The ID of the video.
    :type video_id: 

    """
    return web.Response(status=200)


async def add_video_to_portfolio_alt1(request: web.Request, portfolio_id, video_id) -> web.Response:
    """Add a video to a portfolio

    

    :param portfolio_id: The ID of the portfolio.
    :type portfolio_id: 
    :param video_id: The ID of the video.
    :type video_id: 

    """
    return web.Response(status=200)


async def delete_video_from_portfolio(request: web.Request, portfolio_id, user_id, video_id) -> web.Response:
    """Remove a video from a portfolio

    

    :param portfolio_id: The ID of the portfolio.
    :type portfolio_id: 
    :param user_id: The ID of the user.
    :type user_id: 
    :param video_id: The ID of the video.
    :type video_id: 

    """
    return web.Response(status=200)


async def delete_video_from_portfolio_alt1(request: web.Request, portfolio_id, video_id) -> web.Response:
    """Remove a video from a portfolio

    

    :param portfolio_id: The ID of the portfolio.
    :type portfolio_id: 
    :param video_id: The ID of the video.
    :type video_id: 

    """
    return web.Response(status=200)


async def get_portfolio_video(request: web.Request, portfolio_id, user_id, video_id) -> web.Response:
    """Get a specific video in a portfolio

    

    :param portfolio_id: The ID of the portfolio.
    :type portfolio_id: 
    :param user_id: The ID of the user.
    :type user_id: 
    :param video_id: The ID of the video.
    :type video_id: 

    """
    return web.Response(status=200)


async def get_portfolio_video_alt1(request: web.Request, portfolio_id, video_id) -> web.Response:
    """Get a specific video in a portfolio

    

    :param portfolio_id: The ID of the portfolio.
    :type portfolio_id: 
    :param video_id: The ID of the video.
    :type video_id: 

    """
    return web.Response(status=200)


async def get_portfolio_videos(request: web.Request, portfolio_id, user_id, containing_uri=None, filter=None, filter_embeddable=None, page=None, per_page=None, sort=None) -> web.Response:
    """Get all the videos in a portfolio

    

    :param portfolio_id: The ID of the portfolio.
    :type portfolio_id: 
    :param user_id: The ID of the user.
    :type user_id: 
    :param containing_uri: The page that contains the video URI.
    :type containing_uri: str
    :param filter: The attribute by which to filter the results.
    :type filter: str
    :param filter_embeddable: Whether to filter the results by embeddable videos (&#x60;true&#x60;) or non-embeddable videos (&#x60;false&#x60;). Required only if **filter** is &#x60;embeddable&#x60;.
    :type filter_embeddable: bool
    :param page: The page number of the results to show.
    :type page: 
    :param per_page: The number of items to show on each page of results, up to a maximum of 100.
    :type per_page: 
    :param sort: The way to sort the results.  Option descriptions:  * &#x60;default&#x60; - This will sort to the default sort set on the portfolio. 
    :type sort: str

    """
    return web.Response(status=200)


async def get_portfolio_videos_alt1(request: web.Request, portfolio_id, containing_uri=None, filter=None, filter_embeddable=None, page=None, per_page=None, sort=None) -> web.Response:
    """Get all the videos in a portfolio

    

    :param portfolio_id: The ID of the portfolio.
    :type portfolio_id: 
    :param containing_uri: The page that contains the video URI.
    :type containing_uri: str
    :param filter: The attribute by which to filter the results.
    :type filter: str
    :param filter_embeddable: Whether to filter the results by embeddable videos (&#x60;true&#x60;) or non-embeddable videos (&#x60;false&#x60;). Required only if **filter** is &#x60;embeddable&#x60;.
    :type filter_embeddable: bool
    :param page: The page number of the results to show.
    :type page: 
    :param per_page: The number of items to show on each page of results, up to a maximum of 100.
    :type per_page: 
    :param sort: The way to sort the results.  Option descriptions:  * &#x60;default&#x60; - This will sort to the default sort set on the portfolio. 
    :type sort: str

    """
    return web.Response(status=200)
