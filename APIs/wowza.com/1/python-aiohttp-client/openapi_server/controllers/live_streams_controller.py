from typing import List, Dict
from aiohttp import web

from openapi_server.models.create_live_stream200_response import CreateLiveStream200Response
from openapi_server.models.error401 import Error401
from openapi_server.models.error403 import Error403
from openapi_server.models.error404 import Error404
from openapi_server.models.error410 import Error410
from openapi_server.models.error422 import Error422
from openapi_server.models.live_stream_create_input import LiveStreamCreateInput
from openapi_server.models.live_stream_update_input import LiveStreamUpdateInput
from openapi_server.models.live_streams import LiveStreams
from openapi_server.models.regenerate_connection_code_live_stream200_response import RegenerateConnectionCodeLiveStream200Response
from openapi_server.models.reset_live_stream200_response import ResetLiveStream200Response
from openapi_server.models.show_live_stream_state200_response import ShowLiveStreamState200Response
from openapi_server.models.show_live_stream_stats200_response import ShowLiveStreamStats200Response
from openapi_server.models.show_live_stream_thumbnail_url200_response import ShowLiveStreamThumbnailUrl200Response
from openapi_server.models.start_live_stream200_response import StartLiveStream200Response
from openapi_server import util


async def create_live_stream(request: web.Request, live_stream) -> web.Response:
    """Create a live stream

    This operation creates a live stream.

    :param live_stream: Provide the details of the live stream to create in the body of the request.
    :type live_stream: dict | bytes

    """
    live_stream = LiveStreamCreateInput.from_dict(live_stream)
    return web.Response(status=200)


async def delete_live_stream(request: web.Request, id) -> web.Response:
    """Delete a live stream

    This operation deletes a live stream, including all assigned outputs and targets.

    :param id: The unique alphanumeric string that identifies the live stream.
    :type id: str

    """
    return web.Response(status=200)


async def list_live_streams(request: web.Request, page=None, per_page=None) -> web.Response:
    """Fetch all live streams

    This operation shows the details of all of your live streams.

    :param page: Returns a paginated view of results from the HTTP request. Specify a positive integer to indicate which page of the results should be displayed first. &lt;strong&gt;Next&lt;/strong&gt; and &lt;strong&gt;Previous&lt;/strong&gt; links allow you to navigate multiple pages of results. Omit the &lt;em&gt;page&lt;/em&gt; parameter or specify an integer that&#39;s less than or equal to &lt;strong&gt;0&lt;/strong&gt; to view all (unpaginated) results.
    :type page: int
    :param per_page: For use with the &lt;em&gt;page&lt;/em&gt; parameter. Indicates how many records should be included on each page of results. A valid value is any positive integer. The default is &lt;strong&gt;10&lt;/strong&gt;.
    :type per_page: int

    """
    return web.Response(status=200)


async def regenerate_connection_code_live_stream(request: web.Request, id) -> web.Response:
    """Regenerate the connection code for a live stream

    This operation regenerates the connection code of a live stream.

    :param id: The unique alphanumeric string that identifies the live stream.
    :type id: str

    """
    return web.Response(status=200)


async def reset_live_stream(request: web.Request, id) -> web.Response:
    """Reset a live stream

    This operation resets a live stream.

    :param id: The unique alphanumeric string that identifies the live stream.
    :type id: str

    """
    return web.Response(status=200)


async def show_live_stream(request: web.Request, id) -> web.Response:
    """Fetch a live stream

    This operation shows the details of a specific live stream.

    :param id: The unique alphanumeric string that identifies the live stream.
    :type id: str

    """
    return web.Response(status=200)


async def show_live_stream_state(request: web.Request, id) -> web.Response:
    """Fetch the state of a live stream

    This operation shows the current state of a live stream.

    :param id: The unique alphanumeric string that identifies the live stream.
    :type id: str

    """
    return web.Response(status=200)


async def show_live_stream_stats(request: web.Request, id) -> web.Response:
    """Fetch metrics for an active live stream

    This operation returns a hash of metrics keys, each of which identifies a status, text description, unit, and value.

    :param id: The unique alphanumeric string that identifies the live stream.
    :type id: str

    """
    return web.Response(status=200)


async def show_live_stream_thumbnail_url(request: web.Request, id) -> web.Response:
    """Fetch the thumbnail URL of a live stream

    This operation shows the thumbnail URL of a started live stream.

    :param id: The unique alphanumeric string that identifies the live stream.
    :type id: str

    """
    return web.Response(status=200)


async def start_live_stream(request: web.Request, id) -> web.Response:
    """Start a live stream

    This operation starts a live stream.

    :param id: The unique alphanumeric string that identifies the live stream.
    :type id: str

    """
    return web.Response(status=200)


async def stop_live_stream(request: web.Request, id) -> web.Response:
    """Stop a live stream

    This operation stops a live stream.

    :param id: The unique alphanumeric string that identifies the live stream.
    :type id: str

    """
    return web.Response(status=200)


async def update_live_stream(request: web.Request, id, live_stream) -> web.Response:
    """Update a live stream

    This operation updates a live stream.

    :param id: The unique alphanumeric string that identifies the live stream.
    :type id: str
    :param live_stream: Provide the details of the live stream to update in the body of the request.
    :type live_stream: dict | bytes

    """
    live_stream = LiveStreamUpdateInput.from_dict(live_stream)
    return web.Response(status=200)
