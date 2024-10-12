from typing import List, Dict
from aiohttp import web

from openapi_server.models.rest_response import RestResponse
from openapi_server import util


async def counter_using_post(request: web.Request, access_key, secret_key, collection_ids=None, stream_ids=None, start_date_time=None, end_date_time=None, visit_duration=None, max_iterations=None, max_batch_iterations=None, min_neighbors_merged_per_iteration=None, merging_step=None, shuffling=None) -> web.Response:
    """Count individuals in streams or collections

    

    :param access_key: The accessKey provided by VisageCloud
    :type access_key: str
    :param secret_key: The secretKey or readOnlyKey provided by VisageCloud
    :type secret_key: str
    :param collection_ids: Collection ids
    :type collection_ids: List[str]
    :param stream_ids: Stream Ids
    :type stream_ids: List[str]
    :param start_date_time: startDateTime
    :type start_date_time: str
    :param end_date_time: endDateTime
    :type end_date_time: str
    :param visit_duration: visitDuration
    :type visit_duration: int
    :param max_iterations: maxIterations
    :type max_iterations: int
    :param max_batch_iterations: maxBatchIterations
    :type max_batch_iterations: int
    :param min_neighbors_merged_per_iteration: minNeighborsMergedPerIteration
    :type min_neighbors_merged_per_iteration: int
    :param merging_step: mergingStep
    :type merging_step: float
    :param shuffling: shuffling
    :type shuffling: bool

    """
    start_date_time = util.deserialize_datetime(start_date_time)
    end_date_time = util.deserialize_datetime(end_date_time)
    return web.Response(status=200)


async def presence_timeseries_using_post(request: web.Request, access_key, secret_key, attributes, stream_ids=None, start_date_time=None, end_date_time=None, step=None) -> web.Response:
    """Show audience (based on number of occurrences of each person) breakdown per declared attribute (age, gender).

    

    :param access_key: The accessKey provided by VisageCloud
    :type access_key: str
    :param secret_key: The secretKey or readOnlyKey provided by VisageCloud
    :type secret_key: str
    :param attributes: attributes
    :type attributes: List[str]
    :param stream_ids: Stream Ids
    :type stream_ids: List[str]
    :param start_date_time: startDateTime
    :type start_date_time: str
    :param end_date_time: endDateTime
    :type end_date_time: str
    :param step: step
    :type step: int

    """
    start_date_time = util.deserialize_datetime(start_date_time)
    end_date_time = util.deserialize_datetime(end_date_time)
    return web.Response(status=200)


async def presence_total_using_post(request: web.Request, access_key, secret_key, stream_ids, attributes, start_date_time=None, end_date_time=None) -> web.Response:
    """Show presence (based on number of occurences of each face) breakdown per declared attribute (age, gender)

    

    :param access_key: The accessKey provided by VisageCloud
    :type access_key: str
    :param secret_key: The secretKey or readOnlyKey provided by VisageCloud
    :type secret_key: str
    :param stream_ids: Stream Ids
    :type stream_ids: List[str]
    :param attributes: attributes
    :type attributes: List[str]
    :param start_date_time: startDateTime
    :type start_date_time: str
    :param end_date_time: endDateTime
    :type end_date_time: str

    """
    start_date_time = util.deserialize_datetime(start_date_time)
    end_date_time = util.deserialize_datetime(end_date_time)
    return web.Response(status=200)
