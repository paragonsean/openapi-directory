# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.eff_rest_services_get_effluent_chart_get200_response import EffRestServicesGetEffluentChartGet200Response
from openapi_server.models.eff_rest_services_get_summary_chart_get200_response import EffRestServicesGetSummaryChartGet200Response


pytestmark = pytest.mark.asyncio

async def test_eff_rest_services_download_effluent_chart_get(client):
    """Test case for eff_rest_services_download_effluent_chart_get

    Effluent Charts Download Service
    """
    params = [('p_id', 'p_id_example'),
                    ('outfall', 'outfall_example'),
                    ('parameter_code', 'parameter_code_example'),
                    ('start_date', 'start_date_example'),
                    ('end_date', 'end_date_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/echo/eff_rest_services.download_effluent_chart',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_eff_rest_services_download_effluent_chart_post(client):
    """Test case for eff_rest_services_download_effluent_chart_post

    Effluent Charts Download Service
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
    }
    data = {
        'p_id': 'p_id_example',
        'outfall': 'outfall_example',
        'parameter_code': 'parameter_code_example',
        'start_date': 'start_date_example',
        'end_date': 'end_date_example'
        }
    response = await client.request(
        method='POST',
        path='/echo/eff_rest_services.download_effluent_chart',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_eff_rest_services_get_effluent_chart_get(client):
    """Test case for eff_rest_services_get_effluent_chart_get

    Detailed Effluent Chart Service
    """
    params = [('p_id', 'p_id_example'),
                    ('outfall', 'outfall_example'),
                    ('parameter_code', 'parameter_code_example'),
                    ('start_date', 'start_date_example'),
                    ('end_date', 'end_date_example'),
                    ('output', 'output_example'),
                    ('callback', 'param_callback_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/echo/eff_rest_services.get_effluent_chart',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_eff_rest_services_get_effluent_chart_post(client):
    """Test case for eff_rest_services_get_effluent_chart_post

    Detailed Effluent Chart Service
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
    }
    data = {
        'p_id': 'p_id_example',
        'outfall': 'outfall_example',
        'parameter_code': 'parameter_code_example',
        'start_date': 'start_date_example',
        'end_date': 'end_date_example',
        'output': 'output_example',
        'param_callback': 'param_callback_example'
        }
    response = await client.request(
        method='POST',
        path='/echo/eff_rest_services.get_effluent_chart',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_eff_rest_services_get_summary_chart_get(client):
    """Test case for eff_rest_services_get_summary_chart_get

    Summary Effluent Chart Service
    """
    params = [('p_id', 'p_id_example'),
                    ('output', 'output_example'),
                    ('callback', 'param_callback_example'),
                    ('start_date', 'start_date_example'),
                    ('end_date', 'end_date_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/echo/eff_rest_services.get_summary_chart',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_eff_rest_services_get_summary_chart_post(client):
    """Test case for eff_rest_services_get_summary_chart_post

    Summary Effluent Chart Service
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
    }
    data = {
        'p_id': 'p_id_example',
        'output': 'output_example',
        'param_callback': 'param_callback_example',
        'start_date': 'start_date_example',
        'end_date': 'end_date_example'
        }
    response = await client.request(
        method='POST',
        path='/echo/eff_rest_services.get_summary_chart',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

