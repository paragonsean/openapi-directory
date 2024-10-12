from typing import List, Dict
from aiohttp import web

from openapi_server.models.bad_request import BadRequest
from openapi_server.models.cluster_request import ClusterRequest
from openapi_server.models.cluster_response import ClusterResponse
from openapi_server.models.get_cluster_solution404_response import GetClusterSolution404Response
from openapi_server.models.internal_error_message import InternalErrorMessage
from openapi_server.models.job_id import JobId
from openapi_server import util


async def async_clustering_problem(request: web.Request, body) -> web.Response:
    """Batch Cluster Endpoint

     Prefer the [synchronous endpoint](#operation/solveClusteringProblem) and use this Batch Cluster endpoint for long running problems only. The work flow is asynchronous:  - send a POST request towards &#x60;https://graphhopper.com/api/1/cluster/calculate?key&#x3D;&lt;your_key&gt;&#x60; and fetch the job_id. - poll the solution every 500ms until it gives &#x60;status&#x3D;finished&#x60;. Do this with a GET request   towards &#x60;https://graphhopper.com/api/1/cluster/solution/&lt;job_id&gt;?key&#x3D;&lt;your_key&gt;&#x60;. 

    :param body: Request object that contains the problem to be solved
    :type body: dict | bytes

    """
    body = ClusterRequest.from_dict(body)
    return web.Response(status=200)


async def get_cluster_solution(request: web.Request, job_id) -> web.Response:
    """GET Batch Solution Endpoint

    This endpoint returns the solution of the clustering problems submitted to the [Batch Cluster endpoint](#operation/asyncClusteringProblem). You can fetch it with the job_id, you have been sent. 

    :param job_id: Request solution with jobId
    :type job_id: str

    """
    return web.Response(status=200)


async def solve_clustering_problem(request: web.Request, body) -> web.Response:
    """POST Cluster Endpoint

     The Cluster endpoint is used with a POST request towards &#x60;https://graphhopper.com/api/1/cluster?key&#x3D;&lt;your_key&gt;&#x60;. The solution will be provided in the JSON response. Please note that for problems that take longer than 10 seconds a bad request error is returned. In this case please use the asynchronous [Batch Cluster Endpoint](#operation/asyncClusteringProblem) instead. 

    :param body: Request object that contains the problem to be solved
    :type body: dict | bytes

    """
    body = ClusterRequest.from_dict(body)
    return web.Response(status=200)
