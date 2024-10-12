from typing import List, Dict
from aiohttp import web

from openapi_server.models.seriestype import Seriestype
from openapi_server.models.seriestyperule import Seriestyperule
from openapi_server.models.seriestyperuleattribute import Seriestyperuleattribute
from openapi_server.models.seriestypeupdatestatus import Seriestypeupdatestatus
from openapi_server import util


async def seriestypes_get(request: web.Request, startindex=None, count=None) -> web.Response:
    """seriestypes_get

    get a list of all added series types. By filtering search results for certain series types, it is easier for applications to ensure that they read images of applicable types.

    :param startindex: start index of returned slice of series types
    :type startindex: int
    :param count: size of returned slice of series types
    :type count: int

    """
    return web.Response(status=200)


async def seriestypes_id_delete(request: web.Request, id) -> web.Response:
    """seriestypes_id_delete

    remove the series type corresponding to the supplied ID

    :param id: id of series type to remove
    :type id: int

    """
    return web.Response(status=200)


async def seriestypes_id_put(request: web.Request, id) -> web.Response:
    """seriestypes_id_put

    request an asynchronous update of all series, labelling appropriate series with the series type corresponding to the supplied ID.

    :param id: id of series type to update series labels for
    :type id: int

    """
    return web.Response(status=200)


async def seriestypes_post(request: web.Request, series_type=None) -> web.Response:
    """seriestypes_post

    add a new series type

    :param series_type: Series type information. The ID property is irrelevant, the ID of the inserted record is present in the returned data.
    :type series_type: dict | bytes

    """
    series_type = Seriestype.from_dict(series_type)
    return web.Response(status=200)


async def seriestypes_rules_get(request: web.Request, seriestypeid) -> web.Response:
    """seriestypes_rules_get

    get a list of rules for assigning series types to series. A rule connects to a series of attributes with values and a resulting series type. If a series has the required values of the listed attributes, it is assigned to the series type of the rule.

    :param seriestypeid: ID of series type to list rules for
    :type seriestypeid: int

    """
    return web.Response(status=200)


async def seriestypes_rules_id_attributes_get(request: web.Request, id) -> web.Response:
    """seriestypes_rules_id_attributes_get

    get the list of attributes for the series type rule with the supplied ID.

    :param id: index of series type rule to list rule attributes for
    :type id: int

    """
    return web.Response(status=200)


async def seriestypes_rules_id_attributes_post(request: web.Request, id, series_type_rule_attribute=None) -> web.Response:
    """seriestypes_rules_id_attributes_post

    add a new series type rule attribute

    :param id: ID of rule
    :type id: int
    :param series_type_rule_attribute: Series type rule attribute information. The ID property is irrelevant, the ID of the inserted record is present in the returned data.
    :type series_type_rule_attribute: dict | bytes

    """
    series_type_rule_attribute = Seriestyperuleattribute.from_dict(series_type_rule_attribute)
    return web.Response(status=200)


async def seriestypes_rules_id_delete(request: web.Request, id) -> web.Response:
    """seriestypes_rules_id_delete

    remove the series type rule corresponding to the supplied ID

    :param id: id of series type rule to remove
    :type id: int

    """
    return web.Response(status=200)


async def seriestypes_rules_post(request: web.Request, series_type_rule=None) -> web.Response:
    """seriestypes_rules_post

    add a new series type rule

    :param series_type_rule: Series type rule information. The ID property is irrelevant, the ID of the inserted record is present in the returned data.
    :type series_type_rule: dict | bytes

    """
    series_type_rule = Seriestyperule.from_dict(series_type_rule)
    return web.Response(status=200)


async def seriestypes_rules_rule_id_attributes_attribute_id_delete(request: web.Request, rule_id, attribute_id) -> web.Response:
    """seriestypes_rules_rule_id_attributes_attribute_id_delete

    remove the series type rule attribute corresponding to the supplied series type and attribute IDs

    :param rule_id: id of series type rule for which to remove an attribute
    :type rule_id: int
    :param attribute_id: id of attribute to remove
    :type attribute_id: int

    """
    return web.Response(status=200)


async def seriestypes_rules_updatestatus_get(request: web.Request, ) -> web.Response:
    """seriestypes_rules_updatestatus_get

    get the status of the internal process of updating series types for series following a change of series types, rules or attributes.


    """
    return web.Response(status=200)
