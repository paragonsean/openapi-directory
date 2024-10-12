from typing import List, Dict
from aiohttp import web

from openapi_server.models.model_and_view import ModelAndView
from openapi_server import util


async def get_single_record_json(request: web.Request, collection_id, record_id, wskey, param_callback=None, lang=None, profile=None) -> web.Response:
    """get a single record in JSON format

    

    :param collection_id: collectionId
    :type collection_id: str
    :param record_id: recordId
    :type record_id: str
    :param wskey: wskey
    :type wskey: str
    :param param_callback: callback
    :type param_callback: str
    :param lang: lang
    :type lang: str
    :param profile: profile
    :type profile: str

    """
    return web.Response(status=200)


async def get_single_record_json_ld(request: web.Request, collection_id, record_id, wskey, param_callback=None, lang=None, profile=None) -> web.Response:
    """get single record in JSON LD format

    

    :param collection_id: collectionId
    :type collection_id: str
    :param record_id: recordId
    :type record_id: str
    :param wskey: wskey
    :type wskey: str
    :param param_callback: callback
    :type param_callback: str
    :param lang: lang
    :type lang: str
    :param profile: profile
    :type profile: str

    """
    return web.Response(status=200)


async def get_single_record_rdf(request: web.Request, collection_id, record_id, wskey, lang=None, profile=None) -> web.Response:
    """get single record in RDF format)

    

    :param collection_id: collectionId
    :type collection_id: str
    :param record_id: recordId
    :type record_id: str
    :param wskey: wskey
    :type wskey: str
    :param lang: lang
    :type lang: str
    :param profile: profile
    :type profile: str

    """
    return web.Response(status=200)


async def get_single_record_schema_org(request: web.Request, collection_id, record_id, wskey, param_callback=None, lang=None, profile=None) -> web.Response:
    """get single record in Schema.org JSON LD format

    

    :param collection_id: collectionId
    :type collection_id: str
    :param record_id: recordId
    :type record_id: str
    :param wskey: wskey
    :type wskey: str
    :param param_callback: callback
    :type param_callback: str
    :param lang: lang
    :type lang: str
    :param profile: profile
    :type profile: str

    """
    return web.Response(status=200)


async def get_single_record_turtle(request: web.Request, collection_id, record_id, wskey, lang=None, profile=None) -> web.Response:
    """get single record in turtle format)

    

    :param collection_id: collectionId
    :type collection_id: str
    :param record_id: recordId
    :type record_id: str
    :param wskey: wskey
    :type wskey: str
    :param lang: lang
    :type lang: str
    :param profile: profile
    :type profile: str

    """
    return web.Response(status=200)
