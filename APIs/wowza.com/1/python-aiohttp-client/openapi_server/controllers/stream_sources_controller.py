from typing import List, Dict
from aiohttp import web

from openapi_server.models.create_stream_source200_response import CreateStreamSource200Response
from openapi_server.models.error401 import Error401
from openapi_server.models.error403 import Error403
from openapi_server.models.error404 import Error404
from openapi_server.models.error410 import Error410
from openapi_server.models.error422 import Error422
from openapi_server.models.stream_source_create_input import StreamSourceCreateInput
from openapi_server.models.stream_source_update_input import StreamSourceUpdateInput
from openapi_server.models.stream_sources import StreamSources
from openapi_server import util


async def add_stream_source(request: web.Request, stream_source) -> web.Response:
    """Deprecated operation

    POST /stream_sources/add/ is deprecated. To add a stream source, use POST /stream_sources instead.

    :param stream_source: Provide the details of the stream source to add in the body of the request.
    :type stream_source: dict | bytes

    """
    stream_source = StreamSourceCreateInput.from_dict(stream_source)
    return web.Response(status=200)


async def create_stream_source(request: web.Request, stream_source) -> web.Response:
    """Add a stream source

    This operation adds a stream source.

    :param stream_source: Provide the details of the stream source to add in the body of the request.
    :type stream_source: dict | bytes

    """
    stream_source = StreamSourceCreateInput.from_dict(stream_source)
    return web.Response(status=200)


async def delete_stream_source(request: web.Request, id) -> web.Response:
    """Delete a stream source

    This operation deletes a stream source.

    :param id: The unique alphanumeric string that identifies the stream source.
    :type id: str

    """
    return web.Response(status=200)


async def list_stream_sources(request: web.Request, page=None, per_page=None) -> web.Response:
    """Fetch all stream sources

    This operation shows the details of all of your stream sources.

    :param page: Returns a paginated view of results from the HTTP request. Specify a positive integer to indicate which page of the results should be displayed first. &lt;strong&gt;Next&lt;/strong&gt; and &lt;strong&gt;Previous&lt;/strong&gt; links allow you to navigate multiple pages of results. Omit the &lt;em&gt;page&lt;/em&gt; parameter or specify an integer that&#39;s less than or equal to &lt;strong&gt;0&lt;/strong&gt; to view all (unpaginated) results.
    :type page: int
    :param per_page: For use with the &lt;em&gt;page&lt;/em&gt; parameter. Indicates how many records should be included on each page of results. A valid value is any positive integer. The default is &lt;strong&gt;10&lt;/strong&gt;.
    :type per_page: int

    """
    return web.Response(status=200)


async def show_stream_source(request: web.Request, id) -> web.Response:
    """Fetch a stream source

    This operation shows details of a specific stream source.

    :param id: The unique alphanumeric string that identifies the stream source.
    :type id: str

    """
    return web.Response(status=200)


async def update_stream_source(request: web.Request, id, stream_source) -> web.Response:
    """Update a stream source

    This operation updates a stream source.

    :param id: The unique alphanumeric string that identifies the stream source.
    :type id: str
    :param stream_source: Provide the details of the stream source to update in the body of the request.
    :type stream_source: dict | bytes

    """
    stream_source = StreamSourceUpdateInput.from_dict(stream_source)
    return web.Response(status=200)
