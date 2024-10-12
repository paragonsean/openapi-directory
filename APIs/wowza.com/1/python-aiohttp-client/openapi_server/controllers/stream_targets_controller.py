from typing import List, Dict
from aiohttp import web

from openapi_server.models.create_stream_target200_response import CreateStreamTarget200Response
from openapi_server.models.create_stream_target_property200_response import CreateStreamTargetProperty200Response
from openapi_server.models.error401 import Error401
from openapi_server.models.error403 import Error403
from openapi_server.models.error404 import Error404
from openapi_server.models.error410 import Error410
from openapi_server.models.error422 import Error422
from openapi_server.models.geoblock_create_input import GeoblockCreateInput
from openapi_server.models.geoblock_update_input import GeoblockUpdateInput
from openapi_server.models.regenerate_connection_code_stream_target200_response import RegenerateConnectionCodeStreamTarget200Response
from openapi_server.models.show_stream_target_geoblock200_response import ShowStreamTargetGeoblock200Response
from openapi_server.models.show_stream_target_metrics_current200_response import ShowStreamTargetMetricsCurrent200Response
from openapi_server.models.show_stream_target_metrics_historic200_response import ShowStreamTargetMetricsHistoric200Response
from openapi_server.models.show_stream_target_token_auth200_response import ShowStreamTargetTokenAuth200Response
from openapi_server.models.stream_target_create_input import StreamTargetCreateInput
from openapi_server.models.stream_target_properties import StreamTargetProperties
from openapi_server.models.stream_target_property_create_input import StreamTargetPropertyCreateInput
from openapi_server.models.stream_target_update_input import StreamTargetUpdateInput
from openapi_server.models.stream_targets import StreamTargets
from openapi_server.models.token_auth_create_input import TokenAuthCreateInput
from openapi_server.models.token_auth_update_input import TokenAuthUpdateInput
from openapi_server.models.wowza_stream_target_input import WowzaStreamTargetInput
from openapi_server import util


async def add_stream_target(request: web.Request, stream_target) -> web.Response:
    """Deprecated operation

    POST /stream_targets/add/ is deprecated. To add a stream target, use POST /stream_targets instead.

    :param stream_target: Provide the details of the stream target to add in the body of the request.
    :type stream_target: dict | bytes

    """
    stream_target = WowzaStreamTargetInput.from_dict(stream_target)
    return web.Response(status=200)


async def create_stream_target(request: web.Request, stream_target) -> web.Response:
    """Create a stream target

    This operation creates a stream target. There are three types of targets that you can create: &lt;strong&gt;CustomStreamTarget&lt;/strong&gt; for an an external, third-party destination; &lt;strong&gt;WowzaStreamTarget&lt;/strong&gt; for a Wowza CDN target; or &lt;strong&gt;UltraLowLatencyStreamTarget&lt;/strong&gt; for an ultra low latency Wowza CDN target. The availability of many parameters depends on the type of target you create.

    :param stream_target: Provide the details of the stream target to create in the body of the request.
    :type stream_target: dict | bytes

    """
    stream_target = StreamTargetCreateInput.from_dict(stream_target)
    return web.Response(status=200)


async def create_stream_target_geoblock(request: web.Request, stream_target_id, geoblock) -> web.Response:
    """Create geo-blocking for a stream target

    This operation allows you to block or whitelist viewing of a stream target by geographic location. Only stream targets whose &lt;em&gt;type&lt;/em&gt; is &lt;strong&gt;WowzaStreamTarget&lt;/strong&gt; can be geo-blocked. For more information see the technical article [How to geo-block stream targets by using the Wowza Streaming Cloud REST API](https://www.wowza.com/docs/how-to-geo-block-stream-targets-by-using-the-wowza-streaming-cloud-rest-api).

    :param stream_target_id: The unique alphanumeric string that identifies the stream target.
    :type stream_target_id: str
    :param geoblock: Provide the details of the geo-blocking to create in the body of the request.
    :type geoblock: dict | bytes

    """
    geoblock = GeoblockCreateInput.from_dict(geoblock)
    return web.Response(status=200)


async def create_stream_target_property(request: web.Request, stream_target_id, _property) -> web.Response:
    """Create a property for a stream target

    This operation creates a property for a stream target. Properties can be applied to a &lt;strong&gt;CustomStreamTarget&lt;/strong&gt; or &lt;strong&gt;WowzaStreamTarget&lt;/strong&gt; whose &lt;em&gt;provider&lt;/em&gt; is &lt;strong&gt;akamai_cupertino&lt;/strong&gt;. For more information see the technical article [How to set advanced properties by using the Wowza Streaming Cloud REST API](https://www.wowza.com/docs/how-to-set-advanced-properties-by-using-the-wowza-streaming-cloud-rest-api).

    :param stream_target_id: The unique alphanumeric string that identifies the stream target.
    :type stream_target_id: str
    :param _property: Provide the details of the property to create in the body of the request.
    :type _property: dict | bytes

    """
    _property = StreamTargetPropertyCreateInput.from_dict(_property)
    return web.Response(status=200)


async def create_stream_target_token_auth(request: web.Request, stream_target_id, token_auth) -> web.Response:
    """Create token authorization for a stream target

    This operation creates token authorization for a stream target. Only stream targets whose &lt;em&gt;type&lt;/em&gt; is &lt;strong&gt;WowzaStreamTarget&lt;/strong&gt; can use token authorization. For more information see the technical article [How to protect stream targets with token authorization by using the Wowza Streaming Cloud REST API](https://www.wowza.com/docs/how-to-protect-streams-with-token-authorization-by-using-the-wowza-streaming-cloud-rest-api).

    :param stream_target_id: The unique alphanumeric string that identifies the stream target.
    :type stream_target_id: str
    :param token_auth: Provide the details of the token authorization to create in the body of the request.
    :type token_auth: dict | bytes

    """
    token_auth = TokenAuthCreateInput.from_dict(token_auth)
    return web.Response(status=200)


async def delete_stream_target(request: web.Request, id) -> web.Response:
    """Delete a stream target

    This operation deletes a stream target.

    :param id: The unique alphanumeric string that identifies the stream target.
    :type id: str

    """
    return web.Response(status=200)


async def delete_stream_target_property(request: web.Request, stream_target_id, id) -> web.Response:
    """Delete a stream target property

    This operation removes a property from a stream target.

    :param stream_target_id: The unique alphanumeric string that identifies the stream target.
    :type stream_target_id: str
    :param id: The unique string that identifies the stream target property. The string contains the &lt;em&gt;section&lt;/em&gt; and the &lt;em&gt;key&lt;/em&gt;, connected by a dash. For example, &lt;strong&gt;hls-chunkSize&lt;/strong&gt;.
    :type id: str

    """
    return web.Response(status=200)


async def list_stream_target_properties(request: web.Request, stream_target_id) -> web.Response:
    """Fetch all properties of a stream target

    This operation shows the details of all of the properties assigned to a specific stream target. Properties can be applied to a &lt;strong&gt;CustomStreamTarget&lt;/strong&gt; or &lt;strong&gt;WowzaStreamTarget&lt;/strong&gt; whose &lt;em&gt;provider&lt;/em&gt; is &lt;strong&gt;akamai_cupertino&lt;/strong&gt;.

    :param stream_target_id: The unique alphanumeric string that identifies the stream target.
    :type stream_target_id: str

    """
    return web.Response(status=200)


async def list_stream_targets(request: web.Request, page=None, per_page=None) -> web.Response:
    """Fetch all stream targets

    This operation lists the details of all of your stream targets.

    :param page: Returns a paginated view of results from the HTTP request. Specify a positive integer to indicate which page of the results should be displayed first. &lt;strong&gt;Next&lt;/strong&gt; and &lt;strong&gt;Previous&lt;/strong&gt; links allow you to navigate multiple pages of results. Omit the &lt;em&gt;page&lt;/em&gt; parameter or specify an integer that&#39;s less than or equal to &lt;strong&gt;0&lt;/strong&gt; to view all (unpaginated) results.
    :type page: int
    :param per_page: For use with the &lt;em&gt;page&lt;/em&gt; parameter. Indicates how many records should be included on each page of results. A valid value is any positive integer. The default is &lt;strong&gt;10&lt;/strong&gt;.
    :type per_page: int

    """
    return web.Response(status=200)


async def regenerate_connection_code_stream_target(request: web.Request, id) -> web.Response:
    """Regenerate the connection code for a stream target

    This operation regenerates the connection code of a stream target.

    :param id: The unique alphanumeric string that identifies the stream target.
    :type id: str

    """
    return web.Response(status=200)


async def show_stream_target(request: web.Request, id) -> web.Response:
    """Fetch a stream target

    This operation shows details of a specific stream target.

    :param id: The unique alphanumeric string that identifies the stream target.
    :type id: str

    """
    return web.Response(status=200)


async def show_stream_target_geoblock(request: web.Request, stream_target_id) -> web.Response:
    """Fetch geo-blocking for a stream target

    This operation shows the details of geo-blocking applied to a specific stream target. Only stream targets whose &lt;em&gt;type&lt;/em&gt; is &lt;strong&gt;WowzaStreamTarget&lt;/strong&gt; can be geo-blocked.

    :param stream_target_id: The unique alphanumeric string that identifies the stream target.
    :type stream_target_id: str

    """
    return web.Response(status=200)


async def show_stream_target_metrics_current(request: web.Request, id) -> web.Response:
    """Fetch current health metrics for an active Wowza ultra low latency stream target

    This operation returns a snapshot of the current connection and throughput details for an active target whose &lt;em&gt;type&lt;/em&gt; is &lt;strong&gt;UltraLowLatencyStreamTarget&lt;/strong&gt;. The interval for current metrics is 30 seconds from the moment of the query.

    :param id: The unique alphanumeric string that identifies the stream target.
    :type id: str

    """
    return web.Response(status=200)


async def show_stream_target_metrics_historic(request: web.Request, id, _from=None, to=None, interval=None) -> web.Response:
    """Fetch historic health metrics for a Wowza ultra low latency stream target

    This operation shows historic connection and throughput details for target whose &lt;em&gt;type&lt;/em&gt; is &lt;strong&gt;UltraLowLatencyStreamTarget&lt;/strong&gt;.

    :param id: The unique alphanumeric string that identifies the stream target.
    :type id: str
    :param _from: The start of the range of time used to aggregate the metrics. Express the value by using the ISO 8601 standard of &lt;strong&gt;YYYY-MM-DDTHH:MM:SSZ&lt;/strong&gt; where &lt;strong&gt;HH&lt;/strong&gt; is a 24-hour clock in UTC.
    :type _from: str
    :param to: The end of the range of time used to aggregate the metrics. Express the value by using the ISO 8601 standard of &lt;strong&gt;YYYY-MM-DDTHH:MM:SSZ&lt;/strong&gt; where &lt;strong&gt;HH&lt;/strong&gt; is a 24-hour clock in UTC.
    :type to: str
    :param interval: The length of time for a block of metrics. The default is **10m** (10 minutes).
    :type interval: str

    """
    return web.Response(status=200)


async def show_stream_target_property(request: web.Request, stream_target_id, id) -> web.Response:
    """Fetch a property of a stream target

    This operation shows the details of a specific property assigned to a specific stream target. Properties can be applied to a &lt;strong&gt;CustomStreamTarget&lt;/strong&gt; or &lt;strong&gt;WowzaStreamTarget&lt;/strong&gt; whose &lt;em&gt;provider&lt;/em&gt; is &lt;strong&gt;akamai_cupertino&lt;/strong&gt;.

    :param stream_target_id: The unique alphanumeric string that identifies the stream target.
    :type stream_target_id: str
    :param id: The unique string that identifies the stream target property. The string contains the &lt;em&gt;section&lt;/em&gt; and the &lt;em&gt;key&lt;/em&gt;, connected by a dash. For example, &lt;strong&gt;hls-chunkSize&lt;/strong&gt;.
    :type id: str

    """
    return web.Response(status=200)


async def show_stream_target_token_auth(request: web.Request, stream_target_id) -> web.Response:
    """Fetch token authorization for a stream target

    This operation shows the details of the token authorization applied to a stream target. Only stream targets whose &lt;em&gt;type&lt;/em&gt; is &lt;strong&gt;WowzaStreamTarget&lt;/strong&gt; can use token authorization.

    :param stream_target_id: The unique alphanumeric string that identifies the stream target.
    :type stream_target_id: str

    """
    return web.Response(status=200)


async def update_stream_target(request: web.Request, id, stream_target) -> web.Response:
    """Update a stream target

    This operation updates a stream target.

    :param id: The unique alphanumeric string that identifies the stream target.
    :type id: str
    :param stream_target: Provide the details of the stream target to update in the body of the request.
    :type stream_target: dict | bytes

    """
    stream_target = StreamTargetUpdateInput.from_dict(stream_target)
    return web.Response(status=200)


async def update_stream_target_geoblock(request: web.Request, stream_target_id, geoblock) -> web.Response:
    """Update geo-blocking for a stream target

    This operation updates the geo-blocking applied to a stream target. Only stream targets whose &lt;em&gt;type&lt;/em&gt; is &lt;strong&gt;WowzaStreamTarget&lt;/strong&gt; can be geo-blocked.

    :param stream_target_id: The unique alphanumeric string that identifies the stream target.
    :type stream_target_id: str
    :param geoblock: Provide the details of the geo-blocking to update in the body of the request.
    :type geoblock: dict | bytes

    """
    geoblock = GeoblockUpdateInput.from_dict(geoblock)
    return web.Response(status=200)


async def update_stream_target_token_auth(request: web.Request, stream_target_id, token_auth) -> web.Response:
    """Update token authorization for a stream target

    This operation updates the token authorization applied to a stream target. Only stream targets whose &lt;em&gt;type&lt;/em&gt; is &lt;strong&gt;WowzaStreamTarget&lt;/strong&gt; can use token authorization.

    :param stream_target_id: The unique alphanumeric string that identifies the stream target.
    :type stream_target_id: str
    :param token_auth: Provide the details of the token authorization to update in the body of the request.
    :type token_auth: dict | bytes

    """
    token_auth = TokenAuthUpdateInput.from_dict(token_auth)
    return web.Response(status=200)
