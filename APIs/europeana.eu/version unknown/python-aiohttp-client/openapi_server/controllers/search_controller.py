from typing import List, Dict
from aiohttp import web

from openapi_server.models.model_and_view import ModelAndView
from openapi_server.models.search_request import SearchRequest
from openapi_server import util


async def open_search(request: web.Request, search_terms, count=None, start_index=None) -> web.Response:
    """basic search function following the OpenSearch specification

    

    :param search_terms: searchTerms
    :type search_terms: str
    :param count: count
    :type count: int
    :param start_index: startIndex
    :type start_index: int

    """
    return web.Response(status=200)


async def search_records(request: web.Request, query, wskey, boost=None, param_callback=None, colourpalette=None, cursor=None, facet=None, hit_fl=None, hit_selectors=None, landingpage=None, lang=None, media=None, profile=None, q_source=None, q_target=None, qf=None, reusability=None, rows=None, sort=None, start=None, text_fulltext=None, theme=None, thumbnail=None) -> web.Response:
    """search for records

    

    :param query: query
    :type query: str
    :param wskey: wskey
    :type wskey: str
    :param boost: boost
    :type boost: str
    :param param_callback: callback
    :type param_callback: str
    :param colourpalette: colourpalette
    :type colourpalette: List[str]
    :param cursor: cursor
    :type cursor: str
    :param facet: facet
    :type facet: List[str]
    :param hit_fl: hit.fl
    :type hit_fl: str
    :param hit_selectors: hit.selectors
    :type hit_selectors: str
    :param landingpage: landingpage
    :type landingpage: bool
    :param lang: lang
    :type lang: str
    :param media: media
    :type media: bool
    :param profile: profile
    :type profile: str
    :param q_source: q.source
    :type q_source: str
    :param q_target: q.target
    :type q_target: str
    :param qf: qf
    :type qf: List[str]
    :param reusability: reusability
    :type reusability: List[str]
    :param rows: rows
    :type rows: int
    :param sort: sort
    :type sort: str
    :param start: start
    :type start: int
    :param text_fulltext: text_fulltext
    :type text_fulltext: bool
    :param theme: theme
    :type theme: str
    :param thumbnail: thumbnail
    :type thumbnail: bool

    """
    return web.Response(status=200)


async def search_records_post(request: web.Request, wskey, search_request) -> web.Response:
    """search for records post

    

    :param wskey: wskey
    :type wskey: str
    :param search_request: searchRequest
    :type search_request: dict | bytes

    """
    search_request = SearchRequest.from_dict(search_request)
    return web.Response(status=200)


async def translate_query_using_get(request: web.Request, language_codes, term, wskey, param_callback=None, profile=None) -> web.Response:
    """translate a term to different languages

    

    :param language_codes: languageCodes
    :type language_codes: List[str]
    :param term: term
    :type term: str
    :param wskey: wskey
    :type wskey: str
    :param param_callback: callback
    :type param_callback: str
    :param profile: profile
    :type profile: str

    """
    return web.Response(status=200)
