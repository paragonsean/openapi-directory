from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def api_v1_models_create(request: web.Request, vendor_id, model_model, model_shape=None, model_resolution=None, model_onvif=None, model_psia=None, model_ptz=None, model_infrared=None, model_varifocal=None, model_sd_card=None, model_upnp=None, model_audio_in=None, model_audio_out=None, model_default_username=None, model_default_password=None, model_jpeg_url=None, model_h264_url=None, model_mjpeg_url=None) -> web.Response:
    """Creates a new Model

    

    :param vendor_id: Vendor ID
    :type vendor_id: str
    :param model_model: Model
    :type model_model: str
    :param model_shape: Shape
    :type model_shape: str
    :param model_resolution: Resolution
    :type model_resolution: str
    :param model_onvif: ONVIF
    :type model_onvif: str
    :param model_psia: PSIA
    :type model_psia: str
    :param model_ptz: PTZ
    :type model_ptz: str
    :param model_infrared: Infrared
    :type model_infrared: str
    :param model_varifocal: Varifocal
    :type model_varifocal: str
    :param model_sd_card: SD Card
    :type model_sd_card: str
    :param model_upnp: UPnP
    :type model_upnp: str
    :param model_audio_in: UPnP
    :type model_audio_in: str
    :param model_audio_out: UPnP
    :type model_audio_out: str
    :param model_default_username: Default Username
    :type model_default_username: str
    :param model_default_password: Default Password
    :type model_default_password: str
    :param model_jpeg_url: JPEG URL
    :type model_jpeg_url: str
    :param model_h264_url: H264 URL
    :type model_h264_url: str
    :param model_mjpeg_url: MJPEG URL
    :type model_mjpeg_url: str

    """
    return web.Response(status=200)


async def api_v1_models_id_json_patch(request: web.Request, id, vendor_id, model_model=None, model_shape=None, model_resolution=None, model_onvif=None, model_psia=None, model_ptz=None, model_infrared=None, model_varifocal=None, model_sd_card=None, model_upnp=None, model_audio_in=None, model_audio_out=None, model_default_username=None, model_default_password=None, model_jpeg_url=None, model_h264_url=None, model_mjpeg_url=None) -> web.Response:
    """Updates an existing Model

    

    :param id: Model ID
    :type id: str
    :param vendor_id: Vendor ID
    :type vendor_id: str
    :param model_model: Model
    :type model_model: str
    :param model_shape: Shape
    :type model_shape: str
    :param model_resolution: Resolution
    :type model_resolution: str
    :param model_onvif: ONVIF
    :type model_onvif: str
    :param model_psia: PSIA
    :type model_psia: str
    :param model_ptz: PTZ
    :type model_ptz: str
    :param model_infrared: Infrared
    :type model_infrared: str
    :param model_varifocal: Varifocal
    :type model_varifocal: str
    :param model_sd_card: SD Card
    :type model_sd_card: str
    :param model_upnp: UPnP
    :type model_upnp: str
    :param model_audio_in: Audio In
    :type model_audio_in: str
    :param model_audio_out: Audio Out
    :type model_audio_out: str
    :param model_default_username: Default Username
    :type model_default_username: str
    :param model_default_password: Default Password
    :type model_default_password: str
    :param model_jpeg_url: JPEG URL
    :type model_jpeg_url: str
    :param model_h264_url: H264 URL
    :type model_h264_url: str
    :param model_mjpeg_url: MJPEG URL
    :type model_mjpeg_url: str

    """
    return web.Response(status=200)


async def api_v1_models_id_json_put(request: web.Request, id, vendor_id, model_model=None, model_shape=None, model_resolution=None, model_onvif=None, model_psia=None, model_ptz=None, model_infrared=None, model_varifocal=None, model_sd_card=None, model_upnp=None, model_audio_in=None, model_audio_out=None, model_default_username=None, model_default_password=None, model_jpeg_url=None, model_h264_url=None, model_mjpeg_url=None) -> web.Response:
    """Updates an existing Model

    

    :param id: Model ID
    :type id: str
    :param vendor_id: Vendor ID
    :type vendor_id: str
    :param model_model: Model
    :type model_model: str
    :param model_shape: Shape
    :type model_shape: str
    :param model_resolution: Resolution
    :type model_resolution: str
    :param model_onvif: ONVIF
    :type model_onvif: str
    :param model_psia: PSIA
    :type model_psia: str
    :param model_ptz: PTZ
    :type model_ptz: str
    :param model_infrared: Infrared
    :type model_infrared: str
    :param model_varifocal: Varifocal
    :type model_varifocal: str
    :param model_sd_card: SD Card
    :type model_sd_card: str
    :param model_upnp: UPnP
    :type model_upnp: str
    :param model_audio_in: Audio In
    :type model_audio_in: str
    :param model_audio_out: Audio Out
    :type model_audio_out: str
    :param model_default_username: Default Username
    :type model_default_username: str
    :param model_default_password: Default Password
    :type model_default_password: str
    :param model_jpeg_url: JPEG URL
    :type model_jpeg_url: str
    :param model_h264_url: H264 URL
    :type model_h264_url: str
    :param model_mjpeg_url: MJPEG URL
    :type model_mjpeg_url: str

    """
    return web.Response(status=200)


async def api_v1_models_index(request: web.Request, page=None, order=None) -> web.Response:
    """Fetches all Models

    

    :param page: Page number
    :type page: int
    :param order: Sort order
    :type order: str

    """
    return web.Response(status=200)


async def api_v1_models_search(request: web.Request, page=None, q_model_cont=None, q_manufacturer_name_cont=None, q_shape_eq=None, q_resolution_eq=None, q_onvif_true=None, q_psia_true=None, q_ptz_true=None, q_infrared_true=None, q_varifocal_true=None, q_sd_card_true=None, q_upnp_true=None, q_audio_in_true=None, q_audio_out_true=None) -> web.Response:
    """Searches all Models

    

    :param page: Page number
    :type page: int
    :param q_model_cont: Model
    :type q_model_cont: str
    :param q_manufacturer_name_cont: Vendor
    :type q_manufacturer_name_cont: str
    :param q_shape_eq: Shape
    :type q_shape_eq: str
    :param q_resolution_eq: Resolution
    :type q_resolution_eq: str
    :param q_onvif_true: ONVIF
    :type q_onvif_true: str
    :param q_psia_true: PSIA
    :type q_psia_true: str
    :param q_ptz_true: PTZ
    :type q_ptz_true: str
    :param q_infrared_true: Infrared
    :type q_infrared_true: str
    :param q_varifocal_true: Varifocal
    :type q_varifocal_true: str
    :param q_sd_card_true: SD Card
    :type q_sd_card_true: str
    :param q_upnp_true: UPnP
    :type q_upnp_true: str
    :param q_audio_in_true: Audio In
    :type q_audio_in_true: str
    :param q_audio_out_true: Audio Out
    :type q_audio_out_true: str

    """
    return web.Response(status=200)


async def api_v1_models_show(request: web.Request, id) -> web.Response:
    """Fetches a single Model

    

    :param id: Model ID
    :type id: int

    """
    return web.Response(status=200)
