from typing import List, Dict
from aiohttp import web

from openapi_server.models.subscription import Subscription
from openapi_server import util


async def add_repository(request: web.Request, repository, autosubscribe=None, dryrun=None, x_anchore_account=None) -> web.Response:
    """Add repository to watch

    

    :param repository: full repository to add e.g. docker.io/library/alpine
    :type repository: str
    :param autosubscribe: flag to enable/disable auto tag_update activation when new images from a repo are added
    :type autosubscribe: bool
    :param dryrun: flag to return tags in the repository without actually watching the repository, default is false
    :type dryrun: bool
    :param x_anchore_account: An account name to change the resource scope of the request to that account, if permissions allow (admin only)
    :type x_anchore_account: str

    """
    return web.Response(status=200)
