from typing import List, Dict
from aiohttp import web

from openapi_server.models.get_directive_compliance_id200_response import GetDirectiveComplianceId200Response
from openapi_server.models.get_directives_compliance200_response import GetDirectivesCompliance200Response
from openapi_server.models.get_global_compliance200_response import GetGlobalCompliance200Response
from openapi_server.models.get_node_compliance200_response import GetNodeCompliance200Response
from openapi_server.models.get_nodes_compliance200_response import GetNodesCompliance200Response
from openapi_server.models.get_rule_compliance200_response import GetRuleCompliance200Response
from openapi_server.models.get_rules_compliance200_response import GetRulesCompliance200Response
from openapi_server import util


async def get_directive_compliance_id(request: web.Request, directive_id, format=None) -> web.Response:
    """Compliance details by directive

    Get current compliance of a directive of a Rudder server

    :param directive_id: Id of the directive
    :type directive_id: str
    :type directive_id: str
    :param format: format of export
    :type format: str

    """
    return web.Response(status=200)


async def get_directives_compliance(request: web.Request, ) -> web.Response:
    """Compliance details for all directives

    Get current compliance of all the nodes of a Rudder server


    """
    return web.Response(status=200)


async def get_global_compliance(request: web.Request, precision=None) -> web.Response:
    """Global compliance

    Get current global compliance of a Rudder server

    :param precision: Number of digits after comma in compliance percent figures
    :type precision: int

    """
    return web.Response(status=200)


async def get_node_compliance(request: web.Request, node_id, level=None, precision=None) -> web.Response:
    """Compliance details by node

    Get current compliance of a node of a Rudder server

    :param node_id: Id of the target node
    :type node_id: str
    :param level: Number of depth level of compliance objects to display (1:rules, 2:directives, 3:components, 4:nodes, 5:values, 6:reports)
    :type level: int
    :param precision: Number of digits after comma in compliance percent figures
    :type precision: int

    """
    return web.Response(status=200)


async def get_nodes_compliance(request: web.Request, level=None, precision=None) -> web.Response:
    """Compliance details for all nodes

    Get current compliance of all the nodes of a Rudder server

    :param level: Number of depth level of compliance objects to display (1:rules, 2:directives, 3:components, 4:nodes, 5:values, 6:reports)
    :type level: int
    :param precision: Number of digits after comma in compliance percent figures
    :type precision: int

    """
    return web.Response(status=200)


async def get_rule_compliance(request: web.Request, rule_id, level=None, precision=None) -> web.Response:
    """Compliance details by rule

    Get current compliance of a rule of a Rudder server

    :param rule_id: Id of the target rule
    :type rule_id: str
    :type rule_id: str
    :param level: Number of depth level of compliance objects to display (1:rules, 2:directives, 3:components, 4:nodes, 5:values, 6:reports)
    :type level: int
    :param precision: Number of digits after comma in compliance percent figures
    :type precision: int

    """
    return web.Response(status=200)


async def get_rules_compliance(request: web.Request, level=None, precision=None) -> web.Response:
    """Compliance details for all rules

    Get current compliance of all the rules of a Rudder server

    :param level: Number of depth level of compliance objects to display (1:rules, 2:directives, 3:components, 4:nodes, 5:values, 6:reports)
    :type level: int
    :param precision: Number of digits after comma in compliance percent figures
    :type precision: int

    """
    return web.Response(status=200)
