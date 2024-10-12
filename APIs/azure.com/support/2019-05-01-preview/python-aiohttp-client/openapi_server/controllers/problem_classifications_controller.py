from typing import List, Dict
from aiohttp import web

from openapi_server.models.exception_response import ExceptionResponse
from openapi_server.models.problem_classification import ProblemClassification
from openapi_server.models.problem_classifications_list_result import ProblemClassificationsListResult
from openapi_server import util


async def problem_classifications_get(request: web.Request, service_name, problem_classification_name, api_version) -> web.Response:
    """problem_classifications_get

    Gets the details of a specific problem classification for a specific Azure service.

    :param service_name: Name of Azure service available for support.
    :type service_name: str
    :param problem_classification_name: Name of problem classification.
    :type problem_classification_name: str
    :param api_version: Api version
    :type api_version: str

    """
    return web.Response(status=200)


async def problem_classifications_list(request: web.Request, service_name, api_version) -> web.Response:
    """problem_classifications_list

    Lists all the problem classifications (categories) available for a specific Azure service.&lt;br/&gt;&lt;br/&gt; Always use the service and problem classifications obtained programmatically. This practice ensures that you always have the most recent set of service and problem classification Ids.

    :param service_name: Name of Azure service for which the problem classifications need to be retrieved.
    :type service_name: str
    :param api_version: Api version
    :type api_version: str

    """
    return web.Response(status=200)
