from typing import List, Dict
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.split_test import SplitTest
from openapi_server.models.split_test_setup import SplitTestSetup
from openapi_server import util


async def create_split_test(request: web.Request, site_id, branch_tests) -> web.Response:
    """create_split_test

    

    :param site_id: 
    :type site_id: str
    :param branch_tests: 
    :type branch_tests: dict | bytes

    """
    branch_tests = SplitTestSetup.from_dict(branch_tests)
    return web.Response(status=200)


async def disable_split_test(request: web.Request, site_id, split_test_id) -> web.Response:
    """disable_split_test

    

    :param site_id: 
    :type site_id: str
    :param split_test_id: 
    :type split_test_id: str

    """
    return web.Response(status=200)


async def enable_split_test(request: web.Request, site_id, split_test_id) -> web.Response:
    """enable_split_test

    

    :param site_id: 
    :type site_id: str
    :param split_test_id: 
    :type split_test_id: str

    """
    return web.Response(status=200)


async def get_split_test(request: web.Request, site_id, split_test_id) -> web.Response:
    """get_split_test

    

    :param site_id: 
    :type site_id: str
    :param split_test_id: 
    :type split_test_id: str

    """
    return web.Response(status=200)


async def get_split_tests(request: web.Request, site_id) -> web.Response:
    """get_split_tests

    

    :param site_id: 
    :type site_id: str

    """
    return web.Response(status=200)


async def update_split_test(request: web.Request, site_id, split_test_id, branch_tests) -> web.Response:
    """update_split_test

    

    :param site_id: 
    :type site_id: str
    :param split_test_id: 
    :type split_test_id: str
    :param branch_tests: 
    :type branch_tests: dict | bytes

    """
    branch_tests = SplitTestSetup.from_dict(branch_tests)
    return web.Response(status=200)
