from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.record import Record
from openapi_server.models.trial import Trial
from openapi_server.models.trial_search_results import TrialSearchResults
from openapi_server import util


async def get_record(request: web.Request, trial_id, id) -> web.Response:
    """get_record

    Returns a trial&#39;s raw record from its sources

    :param trial_id: ID of the trial
    :type trial_id: str
    :param id: ID of the trial&#39;s record
    :type id: str

    """
    return web.Response(status=200)


async def get_records(request: web.Request, id) -> web.Response:
    """get_records

    Returns a trial&#39;s raw records from its sources

    :param id: ID of the trial
    :type id: str

    """
    return web.Response(status=200)


async def get_trial(request: web.Request, id) -> web.Response:
    """get_trial

    Returns a trial&#39;s details and related entities (e.g. &#x60;conditions&#x60;).

    :param id: ID of the trial
    :type id: str

    """
    return web.Response(status=200)


async def search_trials(request: web.Request, q=None, page=None, per_page=None) -> web.Response:
    """search_trials

    Returns trials based on a search query. By default, it&#39;ll search in all of a trial&#39;s attributes. - &#x60;q&#x60; is a [ElasticSearch query string](https://www.elastic.co/guide/en/elasticsearch/reference/2.3/query-dsl-query-string-query.html#query-string-syntax) (e.g. &#x60;public_title:(depressive OR depression)&#x60;) - &#x60;page&#x60; can take a value between &#x60;1&#x60; and &#x60;100&#x60; - &#x60;per_page&#x60; can take a value between &#x60;10&#x60; and &#x60;100&#x60;

    :param q: The search query (follows the [ElasticSearch Query String](https://www.elastic.co/guide/en/elasticsearch/reference/2.3/query-dsl-query-string-query.html#query-string-syntax) syntax)
    :type q: str
    :param page: The page number
    :type page: int
    :param per_page: Number of items per page
    :type per_page: int

    """
    return web.Response(status=200)
