from typing import List, Dict
from aiohttp import web

from openapi_server.models.ast_response import ASTResponse
from openapi_server.models.analyze_query_response import AnalyzeQueryResponse
from openapi_server.models.error import Error
from openapi_server.models.flux_suggestion import FluxSuggestion
from openapi_server.models.flux_suggestions import FluxSuggestions
from openapi_server.models.language_request import LanguageRequest
from openapi_server.models.post_query_request import PostQueryRequest
from openapi_server.models.query import Query
from openapi_server import util


async def get_query_suggestions(request: web.Request, zap_trace_span=None) -> web.Response:
    """Retrieve query suggestions

    

    :param zap_trace_span: OpenTracing span context
    :type zap_trace_span: str

    """
    return web.Response(status=200)


async def get_query_suggestions_name(request: web.Request, name, zap_trace_span=None) -> web.Response:
    """Retrieve query suggestions for a branching suggestion

    

    :param name: The name of the branching suggestion.
    :type name: str
    :param zap_trace_span: OpenTracing span context
    :type zap_trace_span: str

    """
    return web.Response(status=200)


async def post_query(request: web.Request, zap_trace_span=None, accept_encoding=None, content_type=None, org=None, org_id=None, body=None) -> web.Response:
    """Query InfluxDB

    

    :param zap_trace_span: OpenTracing span context
    :type zap_trace_span: str
    :param accept_encoding: The Accept-Encoding request HTTP header advertises which content encoding, usually a compression algorithm, the client is able to understand.
    :type accept_encoding: str
    :param content_type: 
    :type content_type: str
    :param org: Specifies the name of the organization executing the query. Takes either the ID or Name interchangeably. If both &#x60;orgID&#x60; and &#x60;org&#x60; are specified, &#x60;org&#x60; takes precedence.
    :type org: str
    :param org_id: Specifies the ID of the organization executing the query. If both &#x60;orgID&#x60; and &#x60;org&#x60; are specified, &#x60;org&#x60; takes precedence.
    :type org_id: str
    :param body: Flux query or specification to execute
    :type body: dict | bytes

    """
    body = PostQueryRequest.from_dict(body)
    return web.Response(status=200)


async def post_query_analyze(request: web.Request, zap_trace_span=None, content_type=None, body=None) -> web.Response:
    """Analyze an InfluxQL or Flux query

    

    :param zap_trace_span: OpenTracing span context
    :type zap_trace_span: str
    :param content_type: 
    :type content_type: str
    :param body: Flux or InfluxQL query to analyze
    :type body: dict | bytes

    """
    body = Query.from_dict(body)
    return web.Response(status=200)


async def post_query_ast(request: web.Request, zap_trace_span=None, content_type=None, body=None) -> web.Response:
    """Generate an Abstract Syntax Tree (AST) from a query

    Analyzes flux query and generates a query specification.

    :param zap_trace_span: OpenTracing span context
    :type zap_trace_span: str
    :param content_type: 
    :type content_type: str
    :param body: Analyzed Flux query to generate abstract syntax tree.
    :type body: dict | bytes

    """
    body = LanguageRequest.from_dict(body)
    return web.Response(status=200)
