from typing import List, Dict
from aiohttp import web

from openapi_server.models.candidate_search_list import CandidateSearchList
from openapi_server.models.committee_search_list import CommitteeSearchList
from openapi_server import util


async def names_candidates_get(request: web.Request, api_key, q) -> web.Response:
    """names_candidates_get

     Search for candidates or committees by name. If you&#39;re looking for information on a particular person or group, using a name to find the &#x60;candidate_id&#x60; or &#x60;committee_id&#x60; on this endpoint can be a helpful first step. 

    :param api_key:  API key for https://api.data.gov. Get one at https://api.data.gov/signup. 
    :type api_key: str
    :param q: Name (candidate or committee) to search for
    :type q: List[str]

    """
    return web.Response(status=200)


async def names_committees_get(request: web.Request, api_key, q) -> web.Response:
    """names_committees_get

     Search for candidates or committees by name. If you&#39;re looking for information on a particular person or group, using a name to find the &#x60;candidate_id&#x60; or &#x60;committee_id&#x60; on this endpoint can be a helpful first step. 

    :param api_key:  API key for https://api.data.gov. Get one at https://api.data.gov/signup. 
    :type api_key: str
    :param q: Name (candidate or committee) to search for
    :type q: List[str]

    """
    return web.Response(status=200)
