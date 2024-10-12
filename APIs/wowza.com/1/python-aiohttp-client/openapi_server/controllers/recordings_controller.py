from typing import List, Dict
from aiohttp import web

from openapi_server.models.error401 import Error401
from openapi_server.models.error403 import Error403
from openapi_server.models.error404 import Error404
from openapi_server.models.error410 import Error410
from openapi_server.models.error422 import Error422
from openapi_server.models.recordings import Recordings
from openapi_server.models.show_recording200_response import ShowRecording200Response
from openapi_server.models.show_recording_state200_response import ShowRecordingState200Response
from openapi_server import util


async def delete_recording(request: web.Request, id) -> web.Response:
    """Delete a recording

    This operation deletes a recording.

    :param id: The unique alphanumeric string that identifies the recording.
    :type id: str

    """
    return web.Response(status=200)


async def list_recordings(request: web.Request, page=None, per_page=None) -> web.Response:
    """Fetch all recordings

    This operation shows the details of all of your recordings.

    :param page: Returns a paginated view of results from the HTTP request. Specify a positive integer to indicate which page of the results should be displayed first. &lt;strong&gt;Next&lt;/strong&gt; and &lt;strong&gt;Previous&lt;/strong&gt; links allow you to navigate multiple pages of results. Omit the &lt;em&gt;page&lt;/em&gt; parameter or specify an integer that&#39;s less than or equal to &lt;strong&gt;0&lt;/strong&gt; to view all (unpaginated) results.
    :type page: int
    :param per_page: For use with the &lt;em&gt;page&lt;/em&gt; parameter. Indicates how many records should be included on each page of results. A valid value is any positive integer. The default is &lt;strong&gt;10&lt;/strong&gt;.
    :type per_page: int

    """
    return web.Response(status=200)


async def show_recording(request: web.Request, id) -> web.Response:
    """Fetch a recording

    This operation shows the details of a specific recording.

    :param id: The unique alphanumeric string that identifies the recording.
    :type id: str

    """
    return web.Response(status=200)


async def show_recording_state(request: web.Request, id) -> web.Response:
    """Fetch the state of a recording

    This operation shows the current state of a recording.

    :param id: The unique alphanumeric string that identifies the recording.
    :type id: str

    """
    return web.Response(status=200)
