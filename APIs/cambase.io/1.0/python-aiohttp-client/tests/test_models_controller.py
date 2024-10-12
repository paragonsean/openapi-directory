# coding: utf-8

import pytest
import json
from aiohttp import web
from aiohttp import FormData
from aiohttp import FormData
from aiohttp import FormData



pytestmark = pytest.mark.asyncio

@pytest.mark.skip("multipart/form-data not supported by Connexion")
async def test_api_v1_models_create(client):
    """Test case for api_v1_models_create

    Creates a new Model
    """
    headers = { 
        'Content-Type': 'multipart/form-data',
    }
    data = FormData()
    data.add_field('vendor_id', 'vendor_id_example')
    data.add_field('model_model', 'model_model_example')
    data.add_field('model_shape', 'model_shape_example')
    data.add_field('model_resolution', 'model_resolution_example')
    data.add_field('model_onvif', 'model_onvif_example')
    data.add_field('model_psia', 'model_psia_example')
    data.add_field('model_ptz', 'model_ptz_example')
    data.add_field('model_infrared', 'model_infrared_example')
    data.add_field('model_varifocal', 'model_varifocal_example')
    data.add_field('model_sd_card', 'model_sd_card_example')
    data.add_field('model_upnp', 'model_upnp_example')
    data.add_field('model_audio_in', 'model_audio_in_example')
    data.add_field('model_audio_out', 'model_audio_out_example')
    data.add_field('model_default_username', 'model_default_username_example')
    data.add_field('model_default_password', 'model_default_password_example')
    data.add_field('model_jpeg_url', 'model_jpeg_url_example')
    data.add_field('model_h264_url', 'model_h264_url_example')
    data.add_field('model_mjpeg_url', 'model_mjpeg_url_example')
    response = await client.request(
        method='POST',
        path='/api/v1/models.json',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("multipart/form-data not supported by Connexion")
async def test_api_v1_models_id_json_patch(client):
    """Test case for api_v1_models_id_json_patch

    Updates an existing Model
    """
    headers = { 
        'Content-Type': 'multipart/form-data',
    }
    data = FormData()
    data.add_field('vendor_id', 'vendor_id_example')
    data.add_field('model_model', 'model_model_example')
    data.add_field('model_shape', 'model_shape_example')
    data.add_field('model_resolution', 'model_resolution_example')
    data.add_field('model_onvif', 'model_onvif_example')
    data.add_field('model_psia', 'model_psia_example')
    data.add_field('model_ptz', 'model_ptz_example')
    data.add_field('model_infrared', 'model_infrared_example')
    data.add_field('model_varifocal', 'model_varifocal_example')
    data.add_field('model_sd_card', 'model_sd_card_example')
    data.add_field('model_upnp', 'model_upnp_example')
    data.add_field('model_audio_in', 'model_audio_in_example')
    data.add_field('model_audio_out', 'model_audio_out_example')
    data.add_field('model_default_username', 'model_default_username_example')
    data.add_field('model_default_password', 'model_default_password_example')
    data.add_field('model_jpeg_url', 'model_jpeg_url_example')
    data.add_field('model_h264_url', 'model_h264_url_example')
    data.add_field('model_mjpeg_url', 'model_mjpeg_url_example')
    response = await client.request(
        method='PATCH',
        path='/api/v1/models/{id_jso}'.format(id='id_example'),
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("multipart/form-data not supported by Connexion")
async def test_api_v1_models_id_json_put(client):
    """Test case for api_v1_models_id_json_put

    Updates an existing Model
    """
    headers = { 
        'Content-Type': 'multipart/form-data',
    }
    data = FormData()
    data.add_field('vendor_id', 'vendor_id_example')
    data.add_field('model_model', 'model_model_example')
    data.add_field('model_shape', 'model_shape_example')
    data.add_field('model_resolution', 'model_resolution_example')
    data.add_field('model_onvif', 'model_onvif_example')
    data.add_field('model_psia', 'model_psia_example')
    data.add_field('model_ptz', 'model_ptz_example')
    data.add_field('model_infrared', 'model_infrared_example')
    data.add_field('model_varifocal', 'model_varifocal_example')
    data.add_field('model_sd_card', 'model_sd_card_example')
    data.add_field('model_upnp', 'model_upnp_example')
    data.add_field('model_audio_in', 'model_audio_in_example')
    data.add_field('model_audio_out', 'model_audio_out_example')
    data.add_field('model_default_username', 'model_default_username_example')
    data.add_field('model_default_password', 'model_default_password_example')
    data.add_field('model_jpeg_url', 'model_jpeg_url_example')
    data.add_field('model_h264_url', 'model_h264_url_example')
    data.add_field('model_mjpeg_url', 'model_mjpeg_url_example')
    response = await client.request(
        method='PUT',
        path='/api/v1/models/{id_jso}'.format(id='id_example'),
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_v1_models_index(client):
    """Test case for api_v1_models_index

    Fetches all Models
    """
    params = [('page', 56),
                    ('order', 'order_example')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/api/v1/models.json',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_v1_models_search(client):
    """Test case for api_v1_models_search

    Searches all Models
    """
    params = [('page', 56),
                    ('q[model_cont]', 'q_model_cont_example'),
                    ('q[manufacturer_name_cont]', 'q_manufacturer_name_cont_example'),
                    ('q[shape_eq]', 'q_shape_eq_example'),
                    ('q[resolution_eq]', 'q_resolution_eq_example'),
                    ('q[onvif_true]', 'q_onvif_true_example'),
                    ('q[psia_true]', 'q_psia_true_example'),
                    ('q[ptz_true]', 'q_ptz_true_example'),
                    ('q[infrared_true]', 'q_infrared_true_example'),
                    ('q[varifocal_true]', 'q_varifocal_true_example'),
                    ('q[sd_card_true]', 'q_sd_card_true_example'),
                    ('q[upnp_true]', 'q_upnp_true_example'),
                    ('q[audio_in_true]', 'q_audio_in_true_example'),
                    ('q[audio_out_true]', 'q_audio_out_true_example')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/api/v1/models/search.json',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_v1_models_show(client):
    """Test case for api_v1_models_show

    Fetches a single Model
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/api/v1/models/{id_jso}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

