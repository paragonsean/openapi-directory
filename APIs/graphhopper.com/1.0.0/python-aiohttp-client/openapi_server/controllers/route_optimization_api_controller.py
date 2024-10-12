from typing import List, Dict
from aiohttp import web

from openapi_server.models.bad_request import BadRequest
from openapi_server.models.get_cluster_solution404_response import GetClusterSolution404Response
from openapi_server.models.internal_error_message import InternalErrorMessage
from openapi_server.models.job_id import JobId
from openapi_server.models.request import Request
from openapi_server.models.response import Response
from openapi_server import util


async def async_vrp(request: web.Request, body) -> web.Response:
    """POST route optimization problem (batch mode)

     To solve a vehicle routing problem, perform the following steps:  1.) Make a HTTP POST to this URL  &#x60;&#x60;&#x60; https://graphhopper.com/api/1/vrp/optimize?key&#x3D;&lt;your_key&gt; &#x60;&#x60;&#x60;  It returns a job id (job_id).  2.) Take the job id and fetch the solution for the vehicle routing problem from this URL:  &#x60;&#x60;&#x60; https://graphhopper.com/api/1/vrp/solution/&lt;job_id&gt;?key&#x3D;&lt;your_key&gt; &#x60;&#x60;&#x60;  We recommend to query the solution every 500ms until it returns &#39;status&#x3D;finished&#39;.  **Note**: Since the workflow is a bit more cumbersome and since you lose some time in fetching the solution, you should always prefer the [synchronous endpoint](#operation/solveVRP). You should use the batch mode only for long running problems. 

    :param body: The request that contains the problem to be solved.
    :type body: dict | bytes

    """
    body = Request.from_dict(body)
    return web.Response(status=200)


async def get_solution(request: web.Request, job_id) -> web.Response:
    """GET the solution (batch mode)

     Take the job id and fetch the solution for the vehicle routing problem from this URL:  &#x60;&#x60;&#x60; https://graphhopper.com/api/1/vrp/solution/&lt;job_id&gt;?key&#x3D;&lt;your_key&gt; &#x60;&#x60;&#x60;  You get the job id by sending a vehicle routing problem to the [batch mode URL](#operation/asyncVRP). 

    :param job_id: Request solution with jobId
    :type job_id: str

    """
    return web.Response(status=200)


async def solve_vrp(request: web.Request, body) -> web.Response:
    """POST route optimization problem

     To get started with the Route Optimization API, please read the [introduction](#tag/Route-Optimization-API).  To solve a new vehicle routing problem, make a HTTP POST to this URL  &#x60;&#x60;&#x60; https://graphhopper.com/api/1/vrp?key&#x3D;&lt;your_key&gt; &#x60;&#x60;&#x60;  It returns the solution to this problem in the JSON response.  Please note that this URL is very well suited to solve minor problems. Larger vehicle routing problems, which take longer than 10 seconds to solve, cannot be solved. To solve them, please use the [batch mode URL](#operation/asyncVRP) instead. 

    :param body: The request that contains the vehicle routing problem to be solved.
    :type body: dict | bytes

    """
    body = Request.from_dict(body)
    return web.Response(status=200)
