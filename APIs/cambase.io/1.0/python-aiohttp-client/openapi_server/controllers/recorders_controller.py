from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def api_v1_recorders_create(request: web.Request, vendor_id, recorder_model, recorder_name, recorder_recorder_type, recorder_resolution=None, recorder_onvif=None, recorder_psia=None, recorder_ptz=None, recorder_discontinued=None, recorder_support_3rdparty=None, recorder_sd_card=None, recorder_upnp=None, recorder_hot_swap=None, recorder_hdmi=None, recorder_digital_io=None, recorder_audio_in=None, recorder_audio_out=None, recorder_input_channels=None, recorder_playback_channels=None, recorder_usb=None, recorder_sdhc=None, recorder_mobile_access=None, recorder_alarms=None, recorder_raid_support=None, recorder_storage=None, recorder_additional_information=None, recorder_default_username=None, recorder_default_password=None, recorder_jpeg_url=None, recorder_h264_url=None, recorder_mjpeg_url=None, recorder_official_url=None) -> web.Response:
    """Creates a new Recorder

    

    :param vendor_id: Vendor ID
    :type vendor_id: str
    :param recorder_model: Model
    :type recorder_model: str
    :param recorder_name: Name
    :type recorder_name: str
    :param recorder_recorder_type: Type
    :type recorder_recorder_type: str
    :param recorder_resolution: Resolution
    :type recorder_resolution: str
    :param recorder_onvif: ONVIF
    :type recorder_onvif: str
    :param recorder_psia: PSIA
    :type recorder_psia: str
    :param recorder_ptz: PTZ
    :type recorder_ptz: str
    :param recorder_discontinued: Discontinued
    :type recorder_discontinued: str
    :param recorder_support_3rdparty: 3rd pparty Camera Support
    :type recorder_support_3rdparty: str
    :param recorder_sd_card: SD Card
    :type recorder_sd_card: str
    :param recorder_upnp: UPnP
    :type recorder_upnp: str
    :param recorder_hot_swap: Hot Swap
    :type recorder_hot_swap: str
    :param recorder_hdmi: HDMI Support
    :type recorder_hdmi: str
    :param recorder_digital_io: Digital I/O
    :type recorder_digital_io: str
    :param recorder_audio_in: Audio In
    :type recorder_audio_in: str
    :param recorder_audio_out: Audio Out
    :type recorder_audio_out: str
    :param recorder_input_channels: Input Channels
    :type recorder_input_channels: str
    :param recorder_playback_channels: Playback Channels
    :type recorder_playback_channels: str
    :param recorder_usb: USB Ports
    :type recorder_usb: str
    :param recorder_sdhc: SD Card (GB)
    :type recorder_sdhc: str
    :param recorder_mobile_access: Mobile Access
    :type recorder_mobile_access: str
    :param recorder_alarms: Alarms
    :type recorder_alarms: str
    :param recorder_raid_support: Raid Support
    :type recorder_raid_support: str
    :param recorder_storage: Internal Storage
    :type recorder_storage: str
    :param recorder_additional_information: Additional Information
    :type recorder_additional_information: str
    :param recorder_default_username: Default Username
    :type recorder_default_username: str
    :param recorder_default_password: Default Password
    :type recorder_default_password: str
    :param recorder_jpeg_url: JPEG URL
    :type recorder_jpeg_url: str
    :param recorder_h264_url: H264 URL
    :type recorder_h264_url: str
    :param recorder_mjpeg_url: MJPEG URL
    :type recorder_mjpeg_url: str
    :param recorder_official_url: Official URL
    :type recorder_official_url: str

    """
    return web.Response(status=200)


async def api_v1_recorders_id_json_patch(request: web.Request, id, vendor_id, recorder_model, recorder_name, recorder_recorder_type, recorder_resolution=None, recorder_onvif=None, recorder_psia=None, recorder_ptz=None, recorder_discontinued=None, recorder_support_3rdparty=None, recorder_sd_card=None, recorder_upnp=None, recorder_hot_swap=None, recorder_hdmi=None, recorder_digital_io=None, recorder_audio_in=None, recorder_audio_out=None, recorder_input_channels=None, recorder_playback_channels=None, recorder_usb=None, recorder_sdhc=None, recorder_mobile_access=None, recorder_alarms=None, recorder_raid_support=None, recorder_storage=None, recorder_additional_information=None, recorder_default_username=None, recorder_default_password=None, recorder_jpeg_url=None, recorder_h264_url=None, recorder_mjpeg_url=None, recorder_official_url=None) -> web.Response:
    """Updates an existing Recorder

    

    :param id: Recorder ID
    :type id: str
    :param vendor_id: Vendor ID
    :type vendor_id: str
    :param recorder_model: Model
    :type recorder_model: str
    :param recorder_name: Name
    :type recorder_name: str
    :param recorder_recorder_type: Type
    :type recorder_recorder_type: str
    :param recorder_resolution: Resolution
    :type recorder_resolution: str
    :param recorder_onvif: ONVIF
    :type recorder_onvif: str
    :param recorder_psia: PSIA
    :type recorder_psia: str
    :param recorder_ptz: PTZ
    :type recorder_ptz: str
    :param recorder_discontinued: Discontinued
    :type recorder_discontinued: str
    :param recorder_support_3rdparty: 3rd pparty Camera Support
    :type recorder_support_3rdparty: str
    :param recorder_sd_card: SD Card
    :type recorder_sd_card: str
    :param recorder_upnp: UPnP
    :type recorder_upnp: str
    :param recorder_hot_swap: Hot Swap
    :type recorder_hot_swap: str
    :param recorder_hdmi: HDMI Support
    :type recorder_hdmi: str
    :param recorder_digital_io: Digital I/O
    :type recorder_digital_io: str
    :param recorder_audio_in: Audio In
    :type recorder_audio_in: str
    :param recorder_audio_out: Audio Out
    :type recorder_audio_out: str
    :param recorder_input_channels: Input Channels
    :type recorder_input_channels: str
    :param recorder_playback_channels: Playback Channels
    :type recorder_playback_channels: str
    :param recorder_usb: USB Ports
    :type recorder_usb: str
    :param recorder_sdhc: SD Card (GB)
    :type recorder_sdhc: str
    :param recorder_mobile_access: Mobile Access
    :type recorder_mobile_access: str
    :param recorder_alarms: Alarms
    :type recorder_alarms: str
    :param recorder_raid_support: Raid Support
    :type recorder_raid_support: str
    :param recorder_storage: Internal Storage
    :type recorder_storage: str
    :param recorder_additional_information: Additional Information
    :type recorder_additional_information: str
    :param recorder_default_username: Default Username
    :type recorder_default_username: str
    :param recorder_default_password: Default Password
    :type recorder_default_password: str
    :param recorder_jpeg_url: JPEG URL
    :type recorder_jpeg_url: str
    :param recorder_h264_url: H264 URL
    :type recorder_h264_url: str
    :param recorder_mjpeg_url: MJPEG URL
    :type recorder_mjpeg_url: str
    :param recorder_official_url: Official URL
    :type recorder_official_url: str

    """
    return web.Response(status=200)


async def api_v1_recorders_id_json_put(request: web.Request, id, vendor_id, recorder_model, recorder_name, recorder_recorder_type, recorder_resolution=None, recorder_onvif=None, recorder_psia=None, recorder_ptz=None, recorder_discontinued=None, recorder_support_3rdparty=None, recorder_sd_card=None, recorder_upnp=None, recorder_hot_swap=None, recorder_hdmi=None, recorder_digital_io=None, recorder_audio_in=None, recorder_audio_out=None, recorder_input_channels=None, recorder_playback_channels=None, recorder_usb=None, recorder_sdhc=None, recorder_mobile_access=None, recorder_alarms=None, recorder_raid_support=None, recorder_storage=None, recorder_additional_information=None, recorder_default_username=None, recorder_default_password=None, recorder_jpeg_url=None, recorder_h264_url=None, recorder_mjpeg_url=None, recorder_official_url=None) -> web.Response:
    """Updates an existing Recorder

    

    :param id: Recorder ID
    :type id: str
    :param vendor_id: Vendor ID
    :type vendor_id: str
    :param recorder_model: Model
    :type recorder_model: str
    :param recorder_name: Name
    :type recorder_name: str
    :param recorder_recorder_type: Type
    :type recorder_recorder_type: str
    :param recorder_resolution: Resolution
    :type recorder_resolution: str
    :param recorder_onvif: ONVIF
    :type recorder_onvif: str
    :param recorder_psia: PSIA
    :type recorder_psia: str
    :param recorder_ptz: PTZ
    :type recorder_ptz: str
    :param recorder_discontinued: Discontinued
    :type recorder_discontinued: str
    :param recorder_support_3rdparty: 3rd pparty Camera Support
    :type recorder_support_3rdparty: str
    :param recorder_sd_card: SD Card
    :type recorder_sd_card: str
    :param recorder_upnp: UPnP
    :type recorder_upnp: str
    :param recorder_hot_swap: Hot Swap
    :type recorder_hot_swap: str
    :param recorder_hdmi: HDMI Support
    :type recorder_hdmi: str
    :param recorder_digital_io: Digital I/O
    :type recorder_digital_io: str
    :param recorder_audio_in: Audio In
    :type recorder_audio_in: str
    :param recorder_audio_out: Audio Out
    :type recorder_audio_out: str
    :param recorder_input_channels: Input Channels
    :type recorder_input_channels: str
    :param recorder_playback_channels: Playback Channels
    :type recorder_playback_channels: str
    :param recorder_usb: USB Ports
    :type recorder_usb: str
    :param recorder_sdhc: SD Card (GB)
    :type recorder_sdhc: str
    :param recorder_mobile_access: Mobile Access
    :type recorder_mobile_access: str
    :param recorder_alarms: Alarms
    :type recorder_alarms: str
    :param recorder_raid_support: Raid Support
    :type recorder_raid_support: str
    :param recorder_storage: Internal Storage
    :type recorder_storage: str
    :param recorder_additional_information: Additional Information
    :type recorder_additional_information: str
    :param recorder_default_username: Default Username
    :type recorder_default_username: str
    :param recorder_default_password: Default Password
    :type recorder_default_password: str
    :param recorder_jpeg_url: JPEG URL
    :type recorder_jpeg_url: str
    :param recorder_h264_url: H264 URL
    :type recorder_h264_url: str
    :param recorder_mjpeg_url: MJPEG URL
    :type recorder_mjpeg_url: str
    :param recorder_official_url: Official URL
    :type recorder_official_url: str

    """
    return web.Response(status=200)


async def api_v1_recorders_index(request: web.Request, page=None, order=None) -> web.Response:
    """Fetches all Recorders

    

    :param page: Page number
    :type page: int
    :param order: Sort order
    :type order: str

    """
    return web.Response(status=200)


async def api_v1_recorders_search(request: web.Request, page=None, q_model_cont=None, q_vendor_name_cont=None, q_sdhc_eq=None, q_type_eq=None, q_resolution_eq=None, q_input_channels_eq=None, q_playback_channels_eq=None, q_onvif_true=None, q_psia_true=None, q_ptz_true=None, q_sd_card_true=None, q_upnp_true=None, q_audio_in_true=None, q_audio_out_true=None, q_hdmi_true=None, q_hot_swap_true=None, q_support_3rdparty_true=None, q_digital_io_true=None) -> web.Response:
    """Searches all Recorders

    

    :param page: Page number
    :type page: int
    :param q_model_cont: Model
    :type q_model_cont: str
    :param q_vendor_name_cont: Vendor
    :type q_vendor_name_cont: str
    :param q_sdhc_eq: SD Card (GB)
    :type q_sdhc_eq: str
    :param q_type_eq: Type
    :type q_type_eq: str
    :param q_resolution_eq: Resolution
    :type q_resolution_eq: str
    :param q_input_channels_eq: Input Channels
    :type q_input_channels_eq: str
    :param q_playback_channels_eq: Playback Channels
    :type q_playback_channels_eq: str
    :param q_onvif_true: ONVIF
    :type q_onvif_true: str
    :param q_psia_true: PSIA
    :type q_psia_true: str
    :param q_ptz_true: PTZ
    :type q_ptz_true: str
    :param q_sd_card_true: SD Card
    :type q_sd_card_true: str
    :param q_upnp_true: UPnP
    :type q_upnp_true: str
    :param q_audio_in_true: Audio In
    :type q_audio_in_true: str
    :param q_audio_out_true: Audio Out
    :type q_audio_out_true: str
    :param q_hdmi_true: HDMI Support
    :type q_hdmi_true: str
    :param q_hot_swap_true: Hot Swap
    :type q_hot_swap_true: str
    :param q_support_3rdparty_true: 3rd pparty Camera Support
    :type q_support_3rdparty_true: str
    :param q_digital_io_true: Digital I/O
    :type q_digital_io_true: str

    """
    return web.Response(status=200)


async def api_v1_recorders_show(request: web.Request, id) -> web.Response:
    """Fetches a single Recorder

    

    :param id: Recorder ID
    :type id: int

    """
    return web.Response(status=200)
