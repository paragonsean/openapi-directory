from typing import List, Dict
from aiohttp import web

from openapi_server.models.input_collection_conversion import InputCollectionConversion
from openapi_server.models.input_collection_conversion_xml import InputCollectionConversionXML
from openapi_server.models.input_collection_count import InputCollectionCount
from openapi_server.models.input_collection_filter import InputCollectionFilter
from openapi_server.models.input_collection_modify import InputCollectionModify
from openapi_server.models.input_collection_replace import InputCollectionReplace
from openapi_server.models.input_collection_search import InputCollectionSearch
from openapi_server.models.input_collection_search_numeric import InputCollectionSearchNumeric
from openapi_server.models.input_collection_sort import InputCollectionSort
from openapi_server.models.input_collection_split import InputCollectionSplit
from openapi_server.models.output_collection_number import OutputCollectionNumber
from openapi_server.models.output_collection_result import OutputCollectionResult
from openapi_server.models.output_collection_string import OutputCollectionString
from openapi_server.models.output_multi_collection import OutputMultiCollection
from openapi_server.models.output_number import OutputNumber
from openapi_server.models.output_string import OutputString
from openapi_server import util


async def add_to_collection(request: web.Request, collection_modify=None) -> web.Response:
    """Collections - Add to collection

    Add an item to a collection

    :param collection_modify: Collection modification parameters
    :type collection_modify: dict | bytes

    """
    collection_modify = InputCollectionModify.from_dict(collection_modify)
    return web.Response(status=200)


async def collection_contains_number(request: web.Request, collection_search=None) -> web.Response:
    """Collections - Contains number

    Determine if a collection contains a specific number

    :param collection_search: Collection search parameters
    :type collection_search: dict | bytes

    """
    collection_search = InputCollectionSearchNumeric.from_dict(collection_search)
    return web.Response(status=200)


async def collection_contains_string(request: web.Request, collection_search=None) -> web.Response:
    """Collections - Contains string

    Determine if any items in a collection contain a specific string

    :param collection_search: Collection search parameters
    :type collection_search: dict | bytes

    """
    collection_search = InputCollectionSearch.from_dict(collection_search)
    return web.Response(status=200)


async def collection_ends_with_string(request: web.Request, collection_search=None) -> web.Response:
    """Collections - Ends with string

    Determine if any items in a collection end with a specific string

    :param collection_search: Collection search parameters
    :type collection_search: dict | bytes

    """
    collection_search = InputCollectionSearch.from_dict(collection_search)
    return web.Response(status=200)


async def collection_starts_with_string(request: web.Request, collection_search=None) -> web.Response:
    """Collections - Starts with string

    Determine if any items in a collection start with a specific string

    :param collection_search: Collection search parameters
    :type collection_search: dict | bytes

    """
    collection_search = InputCollectionSearch.from_dict(collection_search)
    return web.Response(status=200)


async def collection_to_json(request: web.Request, collection_conversion=None) -> web.Response:
    """Collections - Collection to JSON

    Convert a collection to a named JSON object

    :param collection_conversion: 
    :type collection_conversion: dict | bytes

    """
    collection_conversion = InputCollectionConversion.from_dict(collection_conversion)
    return web.Response(status=200)


async def collection_to_xml(request: web.Request, collection_conversion_xml=None) -> web.Response:
    """Collections - Collection to XML

    Convert a collection to an XML string

    :param collection_conversion_xml: 
    :type collection_conversion_xml: dict | bytes

    """
    collection_conversion_xml = InputCollectionConversionXML.from_dict(collection_conversion_xml)
    return web.Response(status=200)


async def count_collection(request: web.Request, collection_count=None) -> web.Response:
    """Collections - Count collection

    Count a collection of items

    :param collection_count: Count collection parameters
    :type collection_count: dict | bytes

    """
    collection_count = InputCollectionCount.from_dict(collection_count)
    return web.Response(status=200)


async def filter_collection(request: web.Request, collection_filter=None) -> web.Response:
    """Collections - Filter collection

    Filter a collection of strings by keyword

    :param collection_filter: Filter collection parameters
    :type collection_filter: dict | bytes

    """
    collection_filter = InputCollectionFilter.from_dict(collection_filter)
    return web.Response(status=200)


async def remove_from_collection(request: web.Request, collection_modify=None) -> web.Response:
    """Collections - Remove from collection

    Remove an item from a collection

    :param collection_modify: Collection modification parameters
    :type collection_modify: dict | bytes

    """
    collection_modify = InputCollectionModify.from_dict(collection_modify)
    return web.Response(status=200)


async def replace_values_in_collection(request: web.Request, collection_replace=None) -> web.Response:
    """Collections - Replace values in collection

    Replace whole or partial strings in a collection

    :param collection_replace: Replace values in collection parameters
    :type collection_replace: dict | bytes

    """
    collection_replace = InputCollectionReplace.from_dict(collection_replace)
    return web.Response(status=200)


async def sort_collection(request: web.Request, collection_sort=None) -> web.Response:
    """Collections - Sort collection

    Sort a collection of strings

    :param collection_sort: Sort collection parameters
    :type collection_sort: dict | bytes

    """
    collection_sort = InputCollectionSort.from_dict(collection_sort)
    return web.Response(status=200)


async def split_collection(request: web.Request, collection_split=None) -> web.Response:
    """Collections - Split collection

    Split a collection of items by matching value or index

    :param collection_split: Split collection parameters
    :type collection_split: dict | bytes

    """
    collection_split = InputCollectionSplit.from_dict(collection_split)
    return web.Response(status=200)
