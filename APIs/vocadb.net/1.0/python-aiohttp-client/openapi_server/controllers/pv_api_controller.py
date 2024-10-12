from typing import List, Dict
from aiohttp import web

from openapi_server.models.content_language_preference import ContentLanguagePreference
from openapi_server.models.pv_for_song_contract_partial_find_result import PVForSongContractPartialFindResult
from openapi_server.models.pv_service import PVService
from openapi_server import util


async def api_pvs_for_songs_get(request: web.Request, name=None, author=None, service=None, max_results=None, get_total_count=None, lang=None) -> web.Response:
    """api_pvs_for_songs_get

    

    :param name: 
    :type name: str
    :param author: 
    :type author: str
    :param service: 
    :type service: dict | bytes
    :param max_results: 
    :type max_results: int
    :param get_total_count: 
    :type get_total_count: bool
    :param lang: 
    :type lang: dict | bytes

    """
    service = .from_dict(service)
    lang = .from_dict(lang)
    return web.Response(status=200)
