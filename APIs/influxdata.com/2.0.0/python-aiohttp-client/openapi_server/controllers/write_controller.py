from typing import List, Dict
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.line_protocol_error import LineProtocolError
from openapi_server.models.line_protocol_length_error import LineProtocolLengthError
from openapi_server.models.write_precision import WritePrecision
from openapi_server import util


async def post_write(request: web.Request, org, bucket, body, zap_trace_span=None, content_encoding=None, content_type=None, content_length=None, accept=None, org_id=None, precision=None) -> web.Response:
    """Write time series data into InfluxDB

    

    :param org: Specifies the destination organization for writes. Takes either the ID or Name interchangeably. If both &#x60;orgID&#x60; and &#x60;org&#x60; are specified, &#x60;org&#x60; takes precedence.
    :type org: str
    :param bucket: The destination bucket for writes.
    :type bucket: str
    :param body: Line protocol body
    :type body: str
    :param zap_trace_span: OpenTracing span context
    :type zap_trace_span: str
    :param content_encoding: When present, its value indicates to the database that compression is applied to the line-protocol body.
    :type content_encoding: str
    :param content_type: Content-Type is used to indicate the format of the data sent to the server.
    :type content_type: str
    :param content_length: Content-Length is an entity header is indicating the size of the entity-body, in bytes, sent to the database. If the length is greater than the database max body configuration option, a 413 response is sent.
    :type content_length: int
    :param accept: Specifies the return content format.
    :type accept: str
    :param org_id: Specifies the ID of the destination organization for writes. If both &#x60;orgID&#x60; and &#x60;org&#x60; are specified, &#x60;org&#x60; takes precedence.
    :type org_id: str
    :param precision: The precision for the unix timestamps within the body line-protocol.
    :type precision: dict | bytes

    """
    precision = .from_dict(precision)
    return web.Response(status=200)
