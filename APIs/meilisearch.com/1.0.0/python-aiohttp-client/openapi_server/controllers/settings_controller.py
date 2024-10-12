from typing import List, Dict
from aiohttp import web

from openapi_server.models.update_faceting_request import UpdateFacetingRequest
from openapi_server.models.update_pagination_request import UpdatePaginationRequest
from openapi_server.models.update_settings_request import UpdateSettingsRequest
from openapi_server.models.update_synonyms_request import UpdateSynonymsRequest
from openapi_server.models.update_typo_tolerance_request import UpdateTypoToleranceRequest
from openapi_server import util


async def get_all_settings(request: web.Request, ) -> web.Response:
    """Get all settings

    Get all settings


    """
    return web.Response(status=200)


async def get_displayed_attributes(request: web.Request, ) -> web.Response:
    """Get displayed attributes

    Get displayed attributes


    """
    return web.Response(status=200)


async def get_distinct_attribute(request: web.Request, ) -> web.Response:
    """Get distinct attribute

    Get distinct attribute


    """
    return web.Response(status=200)


async def get_faceting(request: web.Request, ) -> web.Response:
    """Get faceting

    Get faceting


    """
    return web.Response(status=200)


async def get_filterable_attributes(request: web.Request, ) -> web.Response:
    """Get filterable attributes

    Get filterable attributes


    """
    return web.Response(status=200)


async def get_pagination(request: web.Request, ) -> web.Response:
    """Get pagination

    Get pagination


    """
    return web.Response(status=200)


async def get_ranking_rules(request: web.Request, ) -> web.Response:
    """Get ranking rules

    Get ranking rules


    """
    return web.Response(status=200)


async def get_searchable_attributes(request: web.Request, ) -> web.Response:
    """Get searchable attributes

    Get searchable attributes


    """
    return web.Response(status=200)


async def get_sortable_attributes(request: web.Request, ) -> web.Response:
    """Get sortable attributes

    Get sortable attributes


    """
    return web.Response(status=200)


async def get_stop_words(request: web.Request, body=None) -> web.Response:
    """Get stop-words

    Get stop-words

    :param body: 
    :type body: List[str]

    """
    return web.Response(status=200)


async def get_synonyms(request: web.Request, ) -> web.Response:
    """Get synonyms

    Get synonyms


    """
    return web.Response(status=200)


async def get_typo_tolerance(request: web.Request, ) -> web.Response:
    """Get typo-tolerance

    Get typo-tolerance


    """
    return web.Response(status=200)


async def reset_all_settings(request: web.Request, ) -> web.Response:
    """Reset all settings

    Reset all settings


    """
    return web.Response(status=200)


async def reset_displayed_attributes(request: web.Request, ) -> web.Response:
    """Reset displayed attributes

    Reset displayed attributes


    """
    return web.Response(status=200)


async def reset_distinct_attribute(request: web.Request, ) -> web.Response:
    """Reset distinct attribute

    Reset distinct attribute


    """
    return web.Response(status=200)


async def reset_faceting(request: web.Request, ) -> web.Response:
    """Reset faceting

    Reset faceting


    """
    return web.Response(status=200)


async def reset_filterable_attributes(request: web.Request, ) -> web.Response:
    """Reset filterable attributes

    Reset filterable attributes


    """
    return web.Response(status=200)


async def reset_pagination(request: web.Request, ) -> web.Response:
    """Reset pagination

    Reset pagination


    """
    return web.Response(status=200)


async def reset_ranking_rules(request: web.Request, ) -> web.Response:
    """Reset ranking rules

    Reset ranking rules


    """
    return web.Response(status=200)


async def reset_searchable_attributes(request: web.Request, ) -> web.Response:
    """Reset searchable attributes

    Reset searchable attributes


    """
    return web.Response(status=200)


async def reset_sortable_attributes(request: web.Request, ) -> web.Response:
    """Reset sortable attributes

    Reset sortable attributes


    """
    return web.Response(status=200)


async def reset_stop_words(request: web.Request, ) -> web.Response:
    """Reset stop-words

    Reset stop-words


    """
    return web.Response(status=200)


async def reset_synonyms(request: web.Request, ) -> web.Response:
    """Reset synonyms

    Reset synonyms


    """
    return web.Response(status=200)


async def reset_typo_tolerance(request: web.Request, ) -> web.Response:
    """Reset typo-tolerance

    Reset typo-tolerance


    """
    return web.Response(status=200)


async def update_displayed_attributes(request: web.Request, body=None) -> web.Response:
    """Update displayed attributes

    Update displayed attributes

    :param body: 
    :type body: List[str]

    """
    return web.Response(status=200)


async def update_distinct_attribute(request: web.Request, ) -> web.Response:
    """Update distinct attribute

    Update distinct attribute


    """
    return web.Response(status=200)


async def update_faceting(request: web.Request, body=None) -> web.Response:
    """Update faceting

    Update faceting

    :param body: 
    :type body: dict | bytes

    """
    body = UpdateFacetingRequest.from_dict(body)
    return web.Response(status=200)


async def update_filterable_attributes(request: web.Request, body=None) -> web.Response:
    """Update filterable attributes

    Update filterable attributes

    :param body: 
    :type body: List[str]

    """
    return web.Response(status=200)


async def update_pagination(request: web.Request, body=None) -> web.Response:
    """Update pagination

    Update pagination

    :param body: 
    :type body: dict | bytes

    """
    body = UpdatePaginationRequest.from_dict(body)
    return web.Response(status=200)


async def update_ranking_rules(request: web.Request, body=None) -> web.Response:
    """Update ranking rules

    Update ranking rules

    :param body: 
    :type body: List[str]

    """
    return web.Response(status=200)


async def update_searchable_attributes(request: web.Request, body=None) -> web.Response:
    """Update searchable attributes

    Update searchable attributes

    :param body: 
    :type body: List[str]

    """
    return web.Response(status=200)


async def update_settings(request: web.Request, body=None) -> web.Response:
    """Update settings

    Update settings

    :param body: 
    :type body: dict | bytes

    """
    body = UpdateSettingsRequest.from_dict(body)
    return web.Response(status=200)


async def update_sortable_attributes(request: web.Request, body=None) -> web.Response:
    """Update sortable attributes

    Update sortable attributes

    :param body: 
    :type body: List[str]

    """
    return web.Response(status=200)


async def update_stop_words(request: web.Request, body=None) -> web.Response:
    """Update stop-words

    Update stop-words

    :param body: 
    :type body: List[str]

    """
    return web.Response(status=200)


async def update_synonyms(request: web.Request, body=None) -> web.Response:
    """Update synonyms

    Update synonyms

    :param body: 
    :type body: dict | bytes

    """
    body = UpdateSynonymsRequest.from_dict(body)
    return web.Response(status=200)


async def update_typo_tolerance(request: web.Request, body=None) -> web.Response:
    """Update typo-tolerance

    Update typo-tolerance

    :param body: 
    :type body: dict | bytes

    """
    body = UpdateTypoToleranceRequest.from_dict(body)
    return web.Response(status=200)
