from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def search_type_metameta_dictionary(request: web.Request, text=None, name=None, description=None, fromdate=None, todate=None, createdate_from=None, createdate_to=None, changedate_from=None, changedate_to=None, group=None, filesuffix=None, maxlatitude=None, minlongitude=None, minlatitude=None, maxlongitude=None, max=None, skip=None, search_type_metameta_dictionary_field_index=None, search_type_metameta_dictionary_dictionary_type=None, search_type_metameta_dictionary_short_name=None, search_type_metameta_dictionary_super_type=None, search_type_metameta_dictionary_isgroup=None, search_type_metameta_dictionary_handler_class=None, search_type_metameta_dictionary_properties=None, search_type_metameta_dictionary_wiki_text=None) -> web.Response:
    """Search API for &#39;Metadata Dictionary&#39; entry type

    API to search for entries of type Metadata Dictionary

    :param text: Search text
    :type text: str
    :param name: Search name
    :type name: str
    :param description: Search description
    :type description: str
    :param fromdate: From date
    :type fromdate: str
    :param todate: To date
    :type todate: str
    :param createdate_from: Archive create date from
    :type createdate_from: str
    :param createdate_to: Archive create date to
    :type createdate_to: str
    :param changedate_from: Archive change date from
    :type changedate_from: str
    :param changedate_to: Archive change date to
    :type changedate_to: str
    :param group: Parent entry
    :type group: str
    :param filesuffix: File suffix
    :type filesuffix: str
    :param maxlatitude: Northern bounds of search
    :type maxlatitude: float
    :param minlongitude: Western bounds of search
    :type minlongitude: float
    :param minlatitude: Southern bounds of search
    :type minlatitude: float
    :param maxlongitude: Eastern bounds of search
    :type maxlongitude: float
    :param max: Max number of results
    :type max: int
    :param skip: Number to skip
    :type skip: int
    :param search_type_metameta_dictionary_field_index: Index
    :type search_type_metameta_dictionary_field_index: int
    :param search_type_metameta_dictionary_dictionary_type: Type
    :type search_type_metameta_dictionary_dictionary_type: str
    :param search_type_metameta_dictionary_short_name: Short Name
    :type search_type_metameta_dictionary_short_name: str
    :param search_type_metameta_dictionary_super_type: Super Type
    :type search_type_metameta_dictionary_super_type: str
    :param search_type_metameta_dictionary_isgroup: Is Group
    :type search_type_metameta_dictionary_isgroup: bool
    :param search_type_metameta_dictionary_handler_class: Handler Class
    :type search_type_metameta_dictionary_handler_class: str
    :param search_type_metameta_dictionary_properties: Properties
    :type search_type_metameta_dictionary_properties: str
    :param search_type_metameta_dictionary_wiki_text: Wiki Text
    :type search_type_metameta_dictionary_wiki_text: str

    """
    fromdate = util.deserialize_datetime(fromdate)
    todate = util.deserialize_datetime(todate)
    createdate_from = util.deserialize_datetime(createdate_from)
    createdate_to = util.deserialize_datetime(createdate_to)
    changedate_from = util.deserialize_datetime(changedate_from)
    changedate_to = util.deserialize_datetime(changedate_to)
    return web.Response(status=200)
