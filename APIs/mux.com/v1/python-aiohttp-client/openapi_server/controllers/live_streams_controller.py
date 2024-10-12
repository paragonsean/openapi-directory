from typing import List, Dict
from aiohttp import web

from openapi_server.models.create_live_stream_request import CreateLiveStreamRequest
from openapi_server.models.create_playback_id_request import CreatePlaybackIDRequest
from openapi_server.models.create_playback_id_response import CreatePlaybackIDResponse
from openapi_server.models.create_simulcast_target_request import CreateSimulcastTargetRequest
from openapi_server.models.disable_live_stream_response import DisableLiveStreamResponse
from openapi_server.models.enable_live_stream_response import EnableLiveStreamResponse
from openapi_server.models.get_live_stream_playback_id_response import GetLiveStreamPlaybackIDResponse
from openapi_server.models.list_live_streams_response import ListLiveStreamsResponse
from openapi_server.models.live_stream_response import LiveStreamResponse
from openapi_server.models.live_stream_status import LiveStreamStatus
from openapi_server.models.signal_live_stream_complete_response import SignalLiveStreamCompleteResponse
from openapi_server.models.simulcast_target_response import SimulcastTargetResponse
from openapi_server.models.update_live_stream_embedded_subtitles_request import UpdateLiveStreamEmbeddedSubtitlesRequest
from openapi_server.models.update_live_stream_generated_subtitles_request import UpdateLiveStreamGeneratedSubtitlesRequest
from openapi_server.models.update_live_stream_request import UpdateLiveStreamRequest
from openapi_server import util


async def create_live_stream(request: web.Request, body) -> web.Response:
    """Create a live stream

    Creates a new live stream. Once created, an encoder can connect to Mux via the specified stream key and begin streaming to an audience.

    :param body: 
    :type body: dict | bytes

    """
    body = CreateLiveStreamRequest.from_dict(body)
    return web.Response(status=200)


async def create_live_stream_playback_id(request: web.Request, live_stream_id, body) -> web.Response:
    """Create a live stream playback ID

    Create a new playback ID for this live stream, through which a viewer can watch the streamed content of the live stream.

    :param live_stream_id: The live stream ID
    :type live_stream_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = CreatePlaybackIDRequest.from_dict(body)
    return web.Response(status=200)


async def create_live_stream_simulcast_target(request: web.Request, live_stream_id, body) -> web.Response:
    """Create a live stream simulcast target

    Create a simulcast target for the parent live stream. Simulcast target can only be created when the parent live stream is in idle state. Only one simulcast target can be created at a time with this API.

    :param live_stream_id: The live stream ID
    :type live_stream_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = CreateSimulcastTargetRequest.from_dict(body)
    return web.Response(status=200)


async def delete_live_stream(request: web.Request, live_stream_id) -> web.Response:
    """Delete a live stream

    Deletes a live stream from the current environment. If the live stream is currently active and being streamed to, ingest will be terminated and the encoder will be disconnected.

    :param live_stream_id: The live stream ID
    :type live_stream_id: str

    """
    return web.Response(status=200)


async def delete_live_stream_playback_id(request: web.Request, live_stream_id, playback_id) -> web.Response:
    """Delete a live stream playback ID

    Deletes the playback ID for the live stream. This will not disable ingest (as the live stream still exists). New attempts to play back the live stream will fail immediately. However, current viewers will be able to continue watching the stream for some period of time.

    :param live_stream_id: The live stream ID
    :type live_stream_id: str
    :param playback_id: The live stream&#39;s playback ID.
    :type playback_id: str

    """
    return web.Response(status=200)


async def delete_live_stream_simulcast_target(request: web.Request, live_stream_id, simulcast_target_id) -> web.Response:
    """Delete a Live Stream Simulcast Target

    Delete the simulcast target using the simulcast target ID returned when creating the simulcast target. Simulcast Target can only be deleted when the parent live stream is in idle state.

    :param live_stream_id: The live stream ID
    :type live_stream_id: str
    :param simulcast_target_id: The ID of the simulcast target.
    :type simulcast_target_id: str

    """
    return web.Response(status=200)


async def disable_live_stream(request: web.Request, live_stream_id) -> web.Response:
    """Disable a live stream

    Disables a live stream, making it reject incoming RTMP streams until re-enabled. The API also ends the live stream recording immediately when active. Ending the live stream recording adds the &#x60;EXT-X-ENDLIST&#x60; tag to the HLS manifest which notifies the player that this live stream is over.  Mux also closes the encoder connection immediately. Any attempt from the encoder to re-establish connection will fail till the live stream is re-enabled. 

    :param live_stream_id: The live stream ID
    :type live_stream_id: str

    """
    return web.Response(status=200)


async def enable_live_stream(request: web.Request, live_stream_id) -> web.Response:
    """Enable a live stream

    Enables a live stream, allowing it to accept an incoming RTMP stream.

    :param live_stream_id: The live stream ID
    :type live_stream_id: str

    """
    return web.Response(status=200)


async def get_live_stream(request: web.Request, live_stream_id) -> web.Response:
    """Retrieve a live stream

    Retrieves the details of a live stream that has previously been created. Supply the unique live stream ID that was returned from your previous request, and Mux will return the corresponding live stream information. The same information is returned when creating a live stream.

    :param live_stream_id: The live stream ID
    :type live_stream_id: str

    """
    return web.Response(status=200)


async def get_live_stream_playback_id(request: web.Request, live_stream_id, playback_id) -> web.Response:
    """Retrieve a live stream playback ID

    Fetches information about a live stream&#39;s playback ID, through which a viewer can watch the streamed content from this live stream.

    :param live_stream_id: The live stream ID
    :type live_stream_id: str
    :param playback_id: The live stream&#39;s playback ID.
    :type playback_id: str

    """
    return web.Response(status=200)


async def get_live_stream_simulcast_target(request: web.Request, live_stream_id, simulcast_target_id) -> web.Response:
    """Retrieve a Live Stream Simulcast Target

    Retrieves the details of the simulcast target created for the parent live stream. Supply the unique live stream ID and simulcast target ID that was returned in the response of create simulcast target request, and Mux will return the corresponding information.

    :param live_stream_id: The live stream ID
    :type live_stream_id: str
    :param simulcast_target_id: The ID of the simulcast target.
    :type simulcast_target_id: str

    """
    return web.Response(status=200)


async def list_live_streams(request: web.Request, limit=None, page=None, stream_key=None, status=None) -> web.Response:
    """List live streams

    Lists the live streams that currently exist in the current environment.

    :param limit: Number of items to include in the response
    :type limit: int
    :param page: Offset by this many pages, of the size of &#x60;limit&#x60;
    :type page: int
    :param stream_key: Filter response to return live stream for this stream key only
    :type stream_key: str
    :param status: Filter response to return live streams with the specified status only
    :type status: dict | bytes

    """
    status = .from_dict(status)
    return web.Response(status=200)


async def reset_stream_key(request: web.Request, live_stream_id) -> web.Response:
    """Reset a live stream&#39;s stream key

    Reset a live stream key if you want to immediately stop the current stream key from working and create a new stream key that can be used for future broadcasts.

    :param live_stream_id: The live stream ID
    :type live_stream_id: str

    """
    return web.Response(status=200)


async def signal_live_stream_complete(request: web.Request, live_stream_id) -> web.Response:
    """Signal a live stream is finished

    (Optional) End the live stream recording immediately instead of waiting for the reconnect_window. &#x60;EXT-X-ENDLIST&#x60; tag is added to the HLS manifest which notifies the player that this live stream is over.  Mux does not close the encoder connection immediately. Encoders are often configured to re-establish connections immediately which would result in a new recorded asset. For this reason, Mux waits for 60s before closing the connection with the encoder. This 60s timeframe is meant to give encoder operators a chance to disconnect from their end. 

    :param live_stream_id: The live stream ID
    :type live_stream_id: str

    """
    return web.Response(status=200)


async def update_live_stream(request: web.Request, live_stream_id, body) -> web.Response:
    """Update a live stream

    Updates the parameters of a previously-created live stream. This currently supports a subset of variables. Supply the live stream ID and the updated parameters and Mux will return the corresponding live stream information. The information returned will be the same after update as for subsequent get live stream requests.

    :param live_stream_id: The live stream ID
    :type live_stream_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateLiveStreamRequest.from_dict(body)
    return web.Response(status=200)


async def update_live_stream_embedded_subtitles(request: web.Request, live_stream_id, body) -> web.Response:
    """Update a live stream&#39;s embedded subtitles

    Configures a live stream to receive embedded closed captions. The resulting Asset&#39;s subtitle text track will have &#x60;closed_captions: true&#x60; set. 

    :param live_stream_id: The live stream ID
    :type live_stream_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateLiveStreamEmbeddedSubtitlesRequest.from_dict(body)
    return web.Response(status=200)


async def update_live_stream_generated_subtitles(request: web.Request, live_stream_id, body) -> web.Response:
    """Update a live stream&#39;s generated subtitles

    Updates a live stream&#39;s automatic-speech-recognition-generated subtitle configuration. Automatic speech recognition subtitles can be removed by sending an empty array in the request payload. 

    :param live_stream_id: The live stream ID
    :type live_stream_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateLiveStreamGeneratedSubtitlesRequest.from_dict(body)
    return web.Response(status=200)
