from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def organism_attribute_search_query_get(request: web.Request, organism, query, limit=None, attr_name=None) -> web.Response:
    """organism_attribute_search_query_get

    Returns a list of xrefs and associated attributes that contain the query string for a given organism. Results are not restricted to exact matches. Optionally limit results to a specified number per data source, or by the type of attribute. See possible attribute types via /{organism}/attributeSet. 

    :param organism: Organism [Latin name](http://vocabularies.bridgedb.org/#latinName) or [short name](http://vocabularies.bridgedb.org/#shortName).
    :type organism: str
    :param query: Text to find in attributes
    :type query: str
    :param limit: Number of results
    :type limit: int
    :param attr_name: Restrict search by attribute name (case sensitive). Use GET /{organism}/attributeSet to find out which attributes are supported.
    :type attr_name: str

    """
    return web.Response(status=200)


async def organism_attribute_set_get(request: web.Request, organism) -> web.Response:
    """organism_attribute_set_get

    Returns the supported attributes to the given Organism.

    :param organism: Organism [Latin name](http://vocabularies.bridgedb.org/#latinName) or [short name](http://vocabularies.bridgedb.org/#shortName).
    :type organism: str

    """
    return web.Response(status=200)


async def organism_attributes_system_code_identifier_get(request: web.Request, organism, system_code, identifier, attr_name=None) -> web.Response:
    """organism_attributes_system_code_identifier_get

    Returns the attributes for a given identifier, data source, organism. Optionally display only a specified attribute

    :param organism: Organism [Latin name](http://vocabularies.bridgedb.org/#latinName) or [short name](http://vocabularies.bridgedb.org/#shortName).
    :type organism: str
    :param system_code: System
    :type system_code: str
    :param identifier: Identifier
    :type identifier: str
    :param attr_name: Type of attribute
    :type attr_name: str

    """
    return web.Response(status=200)


async def organism_is_free_search_supported_get(request: web.Request, organism) -> web.Response:
    """organism_is_free_search_supported_get

    Returns &#x60;true&#x60; or &#x60;false&#x60; based on whether or not /{organism}/search/{query} is supported for a given organism.

    :param organism: Organism [Latin name](http://vocabularies.bridgedb.org/#latinName) or [short name](http://vocabularies.bridgedb.org/#shortName).
    :type organism: str

    """
    return web.Response(status=200)


async def organism_is_mapping_supported_source_system_code_target_system_code_get(request: web.Request, organism, source_system_code, target_system_code) -> web.Response:
    """organism_is_mapping_supported_source_system_code_target_system_code_get

    Returns &#x60;true&#x60; or &#x60;false&#x60; based on whether or not /{organism}/xrefs/{systemCode}/{identifier} would possibly return a {targetSystemCode} result given a {sourceSystemCode} query. This function basically combines the results of /{organism}/sourceDataSources and /{organism}/targetDataSources into a single boolean result.

    :param organism: Organism [Latin name](http://vocabularies.bridgedb.org/#latinName) or [short name](http://vocabularies.bridgedb.org/#shortName).
    :type organism: str
    :param source_system_code: [System code](http://vocabularies.bridgedb.org/#systemCode) for source (input/query) data source
    :type source_system_code: str
    :param target_system_code: [System code](http://vocabularies.bridgedb.org/#systemCode) for target (output/result) data source
    :type target_system_code: str

    """
    return web.Response(status=200)


async def organism_properties_get(request: web.Request, organism) -> web.Response:
    """organism_properties_get

    Returns the list of properties available for a given organism 

    :param organism: Organism [Latin name](http://vocabularies.bridgedb.org/#latinName) or [short name](http://vocabularies.bridgedb.org/#shortName).
    :type organism: str

    """
    return web.Response(status=200)


async def organism_search_query_get(request: web.Request, organism, query, limit=None) -> web.Response:
    """organism_search_query_get

    Returns a list of xrefs with identifiers that contain the query string for a given organism. Results are not restricted to exact matches. Optionally limit results to a specified number per data source.

    :param organism: Organism [Latin name](http://vocabularies.bridgedb.org/#latinName) or [short name](http://vocabularies.bridgedb.org/#shortName).
    :type organism: str
    :param query: Identifier query
    :type query: str
    :param limit: Number of results per data source
    :type limit: int

    """
    return web.Response(status=200)


async def organism_source_data_sources_get(request: web.Request, organism) -> web.Response:
    """organism_source_data_sources_get

    Returns a list of data sources available as xref sources for a given organism.

    :param organism: Organism [Latin name](http://vocabularies.bridgedb.org/#latinName) or [short name](http://vocabularies.bridgedb.org/#shortName).
    :type organism: str

    """
    return web.Response(status=200)


async def organism_target_data_sources_get(request: web.Request, organism) -> web.Response:
    """organism_target_data_sources_get

    Returns a list of data sources available as xref targets for a given organism.

    :param organism: Organism [Latin name](http://vocabularies.bridgedb.org/#latinName) or [short name](http://vocabularies.bridgedb.org/#shortName).
    :type organism: str

    """
    return web.Response(status=200)


async def organism_xref_exists_system_code_identifier_get(request: web.Request, organism, system_code, identifier) -> web.Response:
    """organism_xref_exists_system_code_identifier_get

    Returns &#x60;true&#x60; or &#x60;false&#x60; based on whether or not an xref exists in the database given an identifier, data source, and organism.

    :param organism: Organism [Latin name](http://vocabularies.bridgedb.org/#latinName) or [short name](http://vocabularies.bridgedb.org/#shortName).
    :type organism: str
    :param system_code: Source (input) data source [system code](https://bridgedb.github.io/pages/system-codes.html)
    :type system_code: str
    :param identifier: Identifier
    :type identifier: str

    """
    return web.Response(status=200)


async def organism_xrefs_batch_post(request: web.Request, organism, body, data_source=None) -> web.Response:
    """organism_xrefs_batch_post

    Returns a list of xrefs, per identifier, that maps to a given list of identifiers an data source given an organism.

    :param organism: Organism [Latin name](http://vocabularies.bridgedb.org/#latinName) or [short name](http://vocabularies.bridgedb.org/#shortName).
    :type organism: str
    :param body: List of tab separated values: id&lt;tab&gt;systemcode\\n
    :type body: str
    :param data_source: (Optional) Restrict results by data source [system code](https://bridgedb.github.io/pages/system-codes.html)
    :type data_source: str

    """
    return web.Response(status=200)


async def organism_xrefs_batch_system_code_post(request: web.Request, organism, system_code, body, data_source=None) -> web.Response:
    """organism_xrefs_batch_system_code_post

    Returns a list of xrefs, that maps to a given list of identifiers to a given data source and organism.

    :param organism: Organism [Latin name](http://vocabularies.bridgedb.org/#latinName) or [short name](http://vocabularies.bridgedb.org/#shortName).
    :type organism: str
    :param system_code: Source (input) data source [system code](http://vocabularies.bridgedb.org/#systemCode)
    :type system_code: str
    :param body: List of identifiers. The separator is a new line (\\n)
    :type body: str
    :param data_source: (Optional) Restrict results by data source [system code](https://bridgedb.github.io/pages/system-codes.html)
    :type data_source: str

    """
    return web.Response(status=200)


async def organism_xrefs_system_code_identifier_get(request: web.Request, organism, system_code, identifier, data_source=None) -> web.Response:
    """organism_xrefs_system_code_identifier_get

    Returns a list of xrefs that map to a given identifier, data source, and organism.

    :param organism: Organism [Latin name](http://vocabularies.bridgedb.org/#latinName) or [short name](http://vocabularies.bridgedb.org/#shortName).
    :type organism: str
    :param system_code: Source (input) data source [system code](https://bridgedb.github.io/pages/system-codes.html)
    :type system_code: str
    :param identifier: Identifier
    :type identifier: str
    :param data_source: (Optional) Restrict results by data source [system code](https://bridgedb.github.io/pages/system-codes.html)
    :type data_source: str

    """
    return web.Response(status=200)
