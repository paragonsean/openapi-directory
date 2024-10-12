from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def search_aspect_id_fullsearch_get(request: web.Request, aspect_id, q, s, e, n_frag, l_frag) -> web.Response:
    """A listing of metadata available for the specified aspect and search term from the BCLaws legislative repository

    

    :param aspect_id: The identifier of the &#39;aspect&#39; (content group) to search
    :type aspect_id: str
    :param q: query term
    :type q: str
    :param s: first hit (start index)
    :type s: str
    :param e: last hit (end index)
    :type e: int
    :param n_frag: number of fragment snippets to return (&lt; 10)
    :type n_frag: int
    :param l_frag: length of fragment snippets (&lt; 200)
    :type l_frag: int

    """
    return web.Response(status=200)
