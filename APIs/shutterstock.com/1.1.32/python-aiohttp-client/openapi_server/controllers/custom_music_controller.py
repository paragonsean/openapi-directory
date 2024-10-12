from typing import List, Dict
from aiohttp import web

from openapi_server.models.audio_renders_list_results import AudioRendersListResults
from openapi_server.models.create_audio_renders_request import CreateAudioRendersRequest
from openapi_server.models.descriptors_list_result import DescriptorsListResult
from openapi_server.models.instruments_list_result import InstrumentsListResult
from openapi_server import util


async def create_audio_renders(request: web.Request, body) -> web.Response:
    """Create rendered audio

    This endpoint creates rendered audio from timeline data. It returns a render ID that you can use to download the finished audio when it is ready. The render ID is valid for up to 48 hours.

    :param body: Parameters for the audio, including the timeline and information about the output file
    :type body: dict | bytes

    """
    body = CreateAudioRendersRequest.from_dict(body)
    return web.Response(status=200)


async def fetch_renders(request: web.Request, id) -> web.Response:
    """Get details about audio renders

    This endpoint shows the status of one or more audio renders, including download links for completed audio.

    :param id: One or more render IDs
    :type id: List[str]

    """
    return web.Response(status=200)


async def list_custom_descriptors(request: web.Request, render_speed_over=None, band_id=None, band_name=None, page=None, per_page=None, id=None, instrument_name=None, instrument_id=None, tempo=None, tempo_to=None, tempo_from=None, name=None, tag=None) -> web.Response:
    """List computer audio descriptors

    This endpoint lists the descriptors that you can use in the audio regions in an audio render.

    :param render_speed_over: Show descriptors with an average render speed that is greater than or equal to the specified value
    :type render_speed_over: 
    :param band_id: Show descriptors that contain the specified band (case-sentsitive)
    :type band_id: str
    :param band_name: Show descriptors with the specified band name (case-sensitive)
    :type band_name: str
    :param page: Page number
    :type page: int
    :param per_page: Number of results per page
    :type per_page: int
    :param id: Show descriptors with the specified IDs (case-sensitive)
    :type id: List[str]
    :param instrument_name: Show descriptors with the specified instrument name (case-sensitive)
    :type instrument_name: str
    :param instrument_id: Show descriptors with the specified instrument ID (case-sensitive)
    :type instrument_id: str
    :param tempo: Show descriptors whose tempo range includes the specified tempo in beats per minute
    :type tempo: 
    :param tempo_to: Show descriptors with a tempo that is less than or equal to the specified number
    :type tempo_to: 
    :param tempo_from: Show descriptors that have a tempo range that includes the specified tempo in beats per minute
    :type tempo_from: 
    :param name: Show descriptors with the specified name (case-sensitive)
    :type name: str
    :param tag: Show descriptors with the specified tag, such as Cinematic or Roomy (case-sensitive)
    :type tag: str

    """
    return web.Response(status=200)


async def list_custom_instruments(request: web.Request, id=None, per_page=None, page=None, name=None, tag=None) -> web.Response:
    """List computer audio instruments

    This endpoint lists the instruments that you can include in computer audio. If you specify more than one search parameter, the API uses an AND condition.

    :param id: Show instruments with the specified ID
    :type id: List[str]
    :param per_page: Number of results per page
    :type per_page: int
    :param page: Page number
    :type page: int
    :param name: Show instruments with the specified name (case-sensitive)
    :type name: str
    :param tag: Show instruments with the specified tag, such as Percussion or Strings (case-sensitive)
    :type tag: str

    """
    return web.Response(status=200)
