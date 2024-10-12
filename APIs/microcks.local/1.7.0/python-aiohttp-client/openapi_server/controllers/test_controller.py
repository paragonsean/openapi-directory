from typing import List, Dict
from aiohttp import web

from openapi_server.models.counter import Counter
from openapi_server.models.request_response_pair import RequestResponsePair
from openapi_server.models.test_case_result import TestCaseResult
from openapi_server.models.test_case_return_dto import TestCaseReturnDTO
from openapi_server.models.test_request import TestRequest
from openapi_server.models.test_result import TestResult
from openapi_server.models.unidirectional_event import UnidirectionalEvent
from openapi_server import util


async def create_test(request: web.Request, body) -> web.Response:
    """Create a new Test

    

    :param body: 
    :type body: dict | bytes

    """
    body = TestRequest.from_dict(body)
    return web.Response(status=200)


async def get_events_by_test_case(request: web.Request, id, test_case_id) -> web.Response:
    """Get events for TestCase

    

    :param id: Unique identifier of TestResult to manage
    :type id: str
    :param test_case_id: Unique identifier of TetsCaseResult to manage
    :type test_case_id: str

    """
    return web.Response(status=200)


async def get_messages_by_test_case(request: web.Request, id, test_case_id) -> web.Response:
    """Get messages for TestCase

    

    :param id: Unique identifier of TestResult to manage
    :type id: str
    :param test_case_id: Unique identifier of TetsCaseResult to manage
    :type test_case_id: str

    """
    return web.Response(status=200)


async def get_test_result(request: web.Request, id) -> web.Response:
    """Get TestResult

    

    :param id: Unique identifier of TestResult to manage
    :type id: str

    """
    return web.Response(status=200)


async def get_test_results_by_service(request: web.Request, service_id) -> web.Response:
    """Get TestResults by Service

    

    :param service_id: Unique identifier of Service to manage TestResults for
    :type service_id: str

    """
    return web.Response(status=200)


async def get_test_results_by_service_counter(request: web.Request, service_id) -> web.Response:
    """Get the TestResults for Service counter

    

    :param service_id: Unique identifier of Service to manage TestResults for
    :type service_id: str

    """
    return web.Response(status=200)


async def report_test_case_result(request: web.Request, id, body) -> web.Response:
    """Report and create a new TestCaseResult

    Report a TestCaseResult (typically used by a Test runner)

    :param id: Unique identifier of TestResult to manage
    :type id: str
    :param body: TestCase return wrapper object
    :type body: dict | bytes

    """
    body = TestCaseReturnDTO.from_dict(body)
    return web.Response(status=200)
