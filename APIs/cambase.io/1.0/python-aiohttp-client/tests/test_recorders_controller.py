# coding: utf-8

import pytest
import json
from aiohttp import web
from aiohttp import FormData
from aiohttp import FormData
from aiohttp import FormData



pytestmark = pytest.mark.asyncio

@pytest.mark.skip("multipart/form-data not supported by Connexion")
async def test_api_v1_recorders_create(client):
    """Test case for api_v1_recorders_create

    Creates a new Recorder
    """
    headers = { 
        'Content-Type': 'multipart/form-data',
    }
    data = FormData()
    data.add_field('vendor_id', 'vendor_id_example')
    data.add_field('recorder_model', 'recorder_model_example')
    data.add_field('recorder_name', 'recorder_name_example')
    data.add_field('recorder_recorder_type', 'recorder_recorder_type_example')
    data.add_field('recorder_resolution', 'recorder_resolution_example')
    data.add_field('recorder_onvif', 'recorder_onvif_example')
    data.add_field('recorder_psia', 'recorder_psia_example')
    data.add_field('recorder_ptz', 'recorder_ptz_example')
    data.add_field('recorder_discontinued', 'recorder_discontinued_example')
    data.add_field('recorder_support_3rdparty', 'recorder_support_3rdparty_example')
    data.add_field('recorder_sd_card', 'recorder_sd_card_example')
    data.add_field('recorder_upnp', 'recorder_upnp_example')
    data.add_field('recorder_hot_swap', 'recorder_hot_swap_example')
    data.add_field('recorder_hdmi', 'recorder_hdmi_example')
    data.add_field('recorder_digital_io', 'recorder_digital_io_example')
    data.add_field('recorder_audio_in', 'recorder_audio_in_example')
    data.add_field('recorder_audio_out', 'recorder_audio_out_example')
    data.add_field('recorder_input_channels', 'recorder_input_channels_example')
    data.add_field('recorder_playback_channels', 'recorder_playback_channels_example')
    data.add_field('recorder_usb', 'recorder_usb_example')
    data.add_field('recorder_sdhc', 'recorder_sdhc_example')
    data.add_field('recorder_mobile_access', 'recorder_mobile_access_example')
    data.add_field('recorder_alarms', 'recorder_alarms_example')
    data.add_field('recorder_raid_support', 'recorder_raid_support_example')
    data.add_field('recorder_storage', 'recorder_storage_example')
    data.add_field('recorder_additional_information', 'recorder_additional_information_example')
    data.add_field('recorder_default_username', 'recorder_default_username_example')
    data.add_field('recorder_default_password', 'recorder_default_password_example')
    data.add_field('recorder_jpeg_url', 'recorder_jpeg_url_example')
    data.add_field('recorder_h264_url', 'recorder_h264_url_example')
    data.add_field('recorder_mjpeg_url', 'recorder_mjpeg_url_example')
    data.add_field('recorder_official_url', 'recorder_official_url_example')
    response = await client.request(
        method='POST',
        path='/api/v1/recorders.json',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("multipart/form-data not supported by Connexion")
async def test_api_v1_recorders_id_json_patch(client):
    """Test case for api_v1_recorders_id_json_patch

    Updates an existing Recorder
    """
    headers = { 
        'Content-Type': 'multipart/form-data',
    }
    data = FormData()
    data.add_field('vendor_id', 'vendor_id_example')
    data.add_field('recorder_model', 'recorder_model_example')
    data.add_field('recorder_name', 'recorder_name_example')
    data.add_field('recorder_recorder_type', 'recorder_recorder_type_example')
    data.add_field('recorder_resolution', 'recorder_resolution_example')
    data.add_field('recorder_onvif', 'recorder_onvif_example')
    data.add_field('recorder_psia', 'recorder_psia_example')
    data.add_field('recorder_ptz', 'recorder_ptz_example')
    data.add_field('recorder_discontinued', 'recorder_discontinued_example')
    data.add_field('recorder_support_3rdparty', 'recorder_support_3rdparty_example')
    data.add_field('recorder_sd_card', 'recorder_sd_card_example')
    data.add_field('recorder_upnp', 'recorder_upnp_example')
    data.add_field('recorder_hot_swap', 'recorder_hot_swap_example')
    data.add_field('recorder_hdmi', 'recorder_hdmi_example')
    data.add_field('recorder_digital_io', 'recorder_digital_io_example')
    data.add_field('recorder_audio_in', 'recorder_audio_in_example')
    data.add_field('recorder_audio_out', 'recorder_audio_out_example')
    data.add_field('recorder_input_channels', 'recorder_input_channels_example')
    data.add_field('recorder_playback_channels', 'recorder_playback_channels_example')
    data.add_field('recorder_usb', 'recorder_usb_example')
    data.add_field('recorder_sdhc', 'recorder_sdhc_example')
    data.add_field('recorder_mobile_access', 'recorder_mobile_access_example')
    data.add_field('recorder_alarms', 'recorder_alarms_example')
    data.add_field('recorder_raid_support', 'recorder_raid_support_example')
    data.add_field('recorder_storage', 'recorder_storage_example')
    data.add_field('recorder_additional_information', 'recorder_additional_information_example')
    data.add_field('recorder_default_username', 'recorder_default_username_example')
    data.add_field('recorder_default_password', 'recorder_default_password_example')
    data.add_field('recorder_jpeg_url', 'recorder_jpeg_url_example')
    data.add_field('recorder_h264_url', 'recorder_h264_url_example')
    data.add_field('recorder_mjpeg_url', 'recorder_mjpeg_url_example')
    data.add_field('recorder_official_url', 'recorder_official_url_example')
    response = await client.request(
        method='PATCH',
        path='/api/v1/recorders/{id_jso}'.format(id='id_example'),
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("multipart/form-data not supported by Connexion")
async def test_api_v1_recorders_id_json_put(client):
    """Test case for api_v1_recorders_id_json_put

    Updates an existing Recorder
    """
    headers = { 
        'Content-Type': 'multipart/form-data',
    }
    data = FormData()
    data.add_field('vendor_id', 'vendor_id_example')
    data.add_field('recorder_model', 'recorder_model_example')
    data.add_field('recorder_name', 'recorder_name_example')
    data.add_field('recorder_recorder_type', 'recorder_recorder_type_example')
    data.add_field('recorder_resolution', 'recorder_resolution_example')
    data.add_field('recorder_onvif', 'recorder_onvif_example')
    data.add_field('recorder_psia', 'recorder_psia_example')
    data.add_field('recorder_ptz', 'recorder_ptz_example')
    data.add_field('recorder_discontinued', 'recorder_discontinued_example')
    data.add_field('recorder_support_3rdparty', 'recorder_support_3rdparty_example')
    data.add_field('recorder_sd_card', 'recorder_sd_card_example')
    data.add_field('recorder_upnp', 'recorder_upnp_example')
    data.add_field('recorder_hot_swap', 'recorder_hot_swap_example')
    data.add_field('recorder_hdmi', 'recorder_hdmi_example')
    data.add_field('recorder_digital_io', 'recorder_digital_io_example')
    data.add_field('recorder_audio_in', 'recorder_audio_in_example')
    data.add_field('recorder_audio_out', 'recorder_audio_out_example')
    data.add_field('recorder_input_channels', 'recorder_input_channels_example')
    data.add_field('recorder_playback_channels', 'recorder_playback_channels_example')
    data.add_field('recorder_usb', 'recorder_usb_example')
    data.add_field('recorder_sdhc', 'recorder_sdhc_example')
    data.add_field('recorder_mobile_access', 'recorder_mobile_access_example')
    data.add_field('recorder_alarms', 'recorder_alarms_example')
    data.add_field('recorder_raid_support', 'recorder_raid_support_example')
    data.add_field('recorder_storage', 'recorder_storage_example')
    data.add_field('recorder_additional_information', 'recorder_additional_information_example')
    data.add_field('recorder_default_username', 'recorder_default_username_example')
    data.add_field('recorder_default_password', 'recorder_default_password_example')
    data.add_field('recorder_jpeg_url', 'recorder_jpeg_url_example')
    data.add_field('recorder_h264_url', 'recorder_h264_url_example')
    data.add_field('recorder_mjpeg_url', 'recorder_mjpeg_url_example')
    data.add_field('recorder_official_url', 'recorder_official_url_example')
    response = await client.request(
        method='PUT',
        path='/api/v1/recorders/{id_jso}'.format(id='id_example'),
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_v1_recorders_index(client):
    """Test case for api_v1_recorders_index

    Fetches all Recorders
    """
    params = [('page', 56),
                    ('order', 'order_example')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/api/v1/recorders.json',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_v1_recorders_search(client):
    """Test case for api_v1_recorders_search

    Searches all Recorders
    """
    params = [('page', 56),
                    ('q[model_cont]', 'q_model_cont_example'),
                    ('q[vendor_name_cont]', 'q_vendor_name_cont_example'),
                    ('q[sdhc_eq]', 'q_sdhc_eq_example'),
                    ('q[type_eq]', 'q_type_eq_example'),
                    ('q[resolution_eq]', 'q_resolution_eq_example'),
                    ('q[input_channels_eq]', 'q_input_channels_eq_example'),
                    ('q[playback_channels_eq]', 'q_playback_channels_eq_example'),
                    ('q[onvif_true]', 'q_onvif_true_example'),
                    ('q[psia_true]', 'q_psia_true_example'),
                    ('q[ptz_true]', 'q_ptz_true_example'),
                    ('q[sd_card_true]', 'q_sd_card_true_example'),
                    ('q[upnp_true]', 'q_upnp_true_example'),
                    ('q[audio_in_true]', 'q_audio_in_true_example'),
                    ('q[audio_out_true]', 'q_audio_out_true_example'),
                    ('q[hdmi_true]', 'q_hdmi_true_example'),
                    ('q[hot_swap_true]', 'q_hot_swap_true_example'),
                    ('q[support_3rdparty_true]', 'q_support_3rdparty_true_example'),
                    ('q[digital_io_true]', 'q_digital_io_true_example')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/api/v1/recorders/search.json',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_v1_recorders_show(client):
    """Test case for api_v1_recorders_show

    Fetches a single Recorder
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/api/v1/recorders/{id_jso}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

