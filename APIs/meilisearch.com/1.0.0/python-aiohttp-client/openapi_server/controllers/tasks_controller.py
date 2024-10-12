from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def cancel_tasks(request: web.Request, uids=None, index_uids=None, types=None, statuses=None, before_enqueued_at=None, after_enqueued_at=None, before_started_at=None, after_started_at=None, before_finished_at=None, after_finished_at=None, canceled_by=None, limit=None, _from=None) -> web.Response:
    """Cancel tasks

    Cancel tasks

    :param uids: 
    :type uids: str
    :param index_uids: 
    :type index_uids: str
    :param types: 
    :type types: str
    :param statuses: 
    :type statuses: str
    :param before_enqueued_at: 
    :type before_enqueued_at: str
    :param after_enqueued_at: 
    :type after_enqueued_at: str
    :param before_started_at: 
    :type before_started_at: str
    :param after_started_at: 
    :type after_started_at: str
    :param before_finished_at: 
    :type before_finished_at: str
    :param after_finished_at: 
    :type after_finished_at: str
    :param canceled_by: 
    :type canceled_by: str
    :param limit: 
    :type limit: str
    :param _from: 
    :type _from: str

    """
    return web.Response(status=200)


async def delete_tasks(request: web.Request, uids=None, index_uids=None, types=None, statuses=None, before_enqueued_at=None, after_enqueued_at=None, before_started_at=None, after_started_at=None, before_finished_at=None, after_finished_at=None, canceled_by=None, limit=None, _from=None) -> web.Response:
    """Delete tasks

    Delete tasks

    :param uids: 
    :type uids: str
    :param index_uids: 
    :type index_uids: str
    :param types: 
    :type types: str
    :param statuses: 
    :type statuses: str
    :param before_enqueued_at: 
    :type before_enqueued_at: str
    :param after_enqueued_at: 
    :type after_enqueued_at: str
    :param before_started_at: 
    :type before_started_at: str
    :param after_started_at: 
    :type after_started_at: str
    :param before_finished_at: 
    :type before_finished_at: str
    :param after_finished_at: 
    :type after_finished_at: str
    :param canceled_by: 
    :type canceled_by: str
    :param limit: 
    :type limit: str
    :param _from: 
    :type _from: str

    """
    return web.Response(status=200)


async def get_all_tasks(request: web.Request, uids=None, index_uids=None, types=None, statuses=None, before_enqueued_at=None, after_enqueued_at=None, before_started_at=None, after_started_at=None, before_finished_at=None, after_finished_at=None, canceled_by=None, limit=None, _from=None) -> web.Response:
    """Get all tasks

    Get all tasks

    :param uids: 
    :type uids: str
    :param index_uids: 
    :type index_uids: str
    :param types: 
    :type types: str
    :param statuses: 
    :type statuses: str
    :param before_enqueued_at: 
    :type before_enqueued_at: str
    :param after_enqueued_at: 
    :type after_enqueued_at: str
    :param before_started_at: 
    :type before_started_at: str
    :param after_started_at: 
    :type after_started_at: str
    :param before_finished_at: 
    :type before_finished_at: str
    :param after_finished_at: 
    :type after_finished_at: str
    :param canceled_by: 
    :type canceled_by: str
    :param limit: 
    :type limit: str
    :param _from: 
    :type _from: str

    """
    return web.Response(status=200)


async def get_one_task(request: web.Request, ) -> web.Response:
    """Get one task

    Get one task


    """
    return web.Response(status=200)
