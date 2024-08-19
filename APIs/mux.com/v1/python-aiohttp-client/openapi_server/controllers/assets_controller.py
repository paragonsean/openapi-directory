from typing import List, Dict
from aiohttp import web

from openapi_server.models.asset_response import AssetResponse
from openapi_server.models.create_asset_request import CreateAssetRequest
from openapi_server.models.create_playback_id_request import CreatePlaybackIDRequest
from openapi_server.models.create_playback_id_response import CreatePlaybackIDResponse
from openapi_server.models.create_track_request import CreateTrackRequest
from openapi_server.models.create_track_response import CreateTrackResponse
from openapi_server.models.get_asset_input_info_response import GetAssetInputInfoResponse
from openapi_server.models.get_asset_playback_id_response import GetAssetPlaybackIDResponse
from openapi_server.models.list_assets_response import ListAssetsResponse
from openapi_server.models.update_asset_mp4_support_request import UpdateAssetMP4SupportRequest
from openapi_server.models.update_asset_master_access_request import UpdateAssetMasterAccessRequest
from openapi_server.models.update_asset_request import UpdateAssetRequest
from openapi_server import util


async def create_asset(request: web.Request, body) -> web.Response:
    """Create an asset

    Create a new Mux Video asset.

    :param body: 
    :type body: dict | bytes

    """
    body = CreateAssetRequest.from_dict(body)
    return web.Response(status=200)


async def create_asset_playback_id(request: web.Request, asset_id, body) -> web.Response:
    """Create a playback ID

    Creates a playback ID that can be used to stream the asset to a viewer.

    :param asset_id: The asset ID.
    :type asset_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = CreatePlaybackIDRequest.from_dict(body)
    return web.Response(status=200)


async def create_asset_track(request: web.Request, asset_id, body) -> web.Response:
    """Create an asset track

    Adds an asset track (for example, subtitles, or an alternate audio track) to an asset.

    :param asset_id: The asset ID.
    :type asset_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = CreateTrackRequest.from_dict(body)
    return web.Response(status=200)


async def delete_asset(request: web.Request, asset_id) -> web.Response:
    """Delete an asset

    Deletes a video asset and all its data.

    :param asset_id: The asset ID.
    :type asset_id: str

    """
    return web.Response(status=200)


async def delete_asset_playback_id(request: web.Request, asset_id, playback_id) -> web.Response:
    """Delete a playback ID

    Deletes a playback ID, rendering it nonfunctional for viewing an asset&#39;s video content. Please note that deleting the playback ID removes access to the underlying asset; a viewer who started playback before the playback ID was deleted may be able to watch the entire video for a limited duration.

    :param asset_id: The asset ID.
    :type asset_id: str
    :param playback_id: The live stream&#39;s playback ID.
    :type playback_id: str

    """
    return web.Response(status=200)


async def delete_asset_track(request: web.Request, asset_id, track_id) -> web.Response:
    """Delete an asset track

    Removes a text track from an asset. Audio and video tracks on assets cannot be removed.

    :param asset_id: The asset ID.
    :type asset_id: str
    :param track_id: The track ID.
    :type track_id: str

    """
    return web.Response(status=200)


async def get_asset(request: web.Request, asset_id) -> web.Response:
    """Retrieve an asset

    Retrieves the details of an asset that has previously been created. Supply the unique asset ID that was returned from your previous request, and Mux will return the corresponding asset information. The same information is returned when creating an asset.

    :param asset_id: The asset ID.
    :type asset_id: str

    """
    return web.Response(status=200)


async def get_asset_input_info(request: web.Request, asset_id) -> web.Response:
    """Retrieve asset input info

    Returns a list of the input objects that were used to create the asset along with any settings that were applied to each input.

    :param asset_id: The asset ID.
    :type asset_id: str

    """
    return web.Response(status=200)


async def get_asset_playback_id(request: web.Request, asset_id, playback_id) -> web.Response:
    """Retrieve a playback ID

    Retrieves information about the specified playback ID.

    :param asset_id: The asset ID.
    :type asset_id: str
    :param playback_id: The live stream&#39;s playback ID.
    :type playback_id: str

    """
    return web.Response(status=200)


async def list_assets(request: web.Request, limit=None, page=None, live_stream_id=None, upload_id=None) -> web.Response:
    """List assets

    List all Mux assets.

    :param limit: Number of items to include in the response
    :type limit: int
    :param page: Offset by this many pages, of the size of &#x60;limit&#x60;
    :type page: int
    :param live_stream_id: Filter response to return all the assets for this live stream only
    :type live_stream_id: str
    :param upload_id: Filter response to return an asset created from this direct upload only
    :type upload_id: str

    """
    return web.Response(status=200)


async def update_asset(request: web.Request, asset_id, body) -> web.Response:
    """Update an Asset

    Updates the details of an already-created Asset with the provided Asset ID. This currently supports only the &#x60;passthrough&#x60; field.

    :param asset_id: The asset ID.
    :type asset_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateAssetRequest.from_dict(body)
    return web.Response(status=200)


async def update_asset_master_access(request: web.Request, asset_id, body) -> web.Response:
    """Update master access

    Allows you to add temporary access to the master (highest-quality) version of the asset in MP4 format. A URL will be created that can be used to download the master version for 24 hours. After 24 hours Master Access will revert to \&quot;none\&quot;. This master version is not optimized for web and not meant to be streamed, only downloaded for purposes like archiving or editing the video offline.

    :param asset_id: The asset ID.
    :type asset_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateAssetMasterAccessRequest.from_dict(body)
    return web.Response(status=200)


async def update_asset_mp4_support(request: web.Request, asset_id, body) -> web.Response:
    """Update MP4 support

    Allows you to add or remove mp4 support for assets that were created without it. Currently there are two values supported in this request, &#x60;standard&#x60; and &#x60;none&#x60;. &#x60;none&#x60; means that an asset *does not* have mp4 support, so submitting a request with &#x60;mp4_support&#x60; set to &#x60;none&#x60; will delete the mp4 assets from the asset in question.

    :param asset_id: The asset ID.
    :type asset_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateAssetMP4SupportRequest.from_dict(body)
    return web.Response(status=200)
