from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def get_v3_sidekiq_compound_metrics(request: web.Request, ) -> web.Response:
    """Get the Sidekiq Compound metrics. Includes queue, process, and job statistics

    Get the Sidekiq Compound metrics. Includes queue, process, and job statistics


    """
    return web.Response(status=200)


async def get_v3_sidekiq_job_stats(request: web.Request, ) -> web.Response:
    """Get the Sidekiq job statistics

    Get the Sidekiq job statistics


    """
    return web.Response(status=200)


async def get_v3_sidekiq_process_metrics(request: web.Request, ) -> web.Response:
    """Get the Sidekiq process metrics

    Get the Sidekiq process metrics


    """
    return web.Response(status=200)


async def get_v3_sidekiq_queue_metrics(request: web.Request, ) -> web.Response:
    """Get the Sidekiq queue metrics

    Get the Sidekiq queue metrics


    """
    return web.Response(status=200)
