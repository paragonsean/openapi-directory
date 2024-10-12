# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.agco_power_services_models_ecu import AGCOPowerServicesModelsECU
from openapi_server.models.agco_power_services_models_production_data import AGCOPowerServicesModelsProductionData
from openapi_server.models.agco_power_services_models_user_status import AGCOPowerServicesModelsUserStatus
from openapi_server.models.api_models_api_error import APIModelsApiError


pytestmark = pytest.mark.asyncio

async def test_aftermarket_services_get_certs(client):
    """Test case for aftermarket_services_get_certs

    No Documentation Found.
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/AftermarketServices/Certificates',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_aftermarket_services_get_connection_status(client):
    """Test case for aftermarket_services_get_connection_status

    Check whether there is connectivity to AGCO Power Web Services
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/AftermarketServices/Hello',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_aftermarket_services_get_engine_iqa_codes(client):
    """Test case for aftermarket_services_get_engine_iqa_codes

    Get injector codes given engine.
    """
    params = [('EDTInstanceId', 'edt_instance_id_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/AftermarketServices/Engines/{serial_number}/IQACodes'.format(serial_number='serial_number_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_aftermarket_services_get_production_data(client):
    """Test case for aftermarket_services_get_production_data

    Get production calibration data for given engine.
    """
    params = [('EDTInstanceId', 'edt_instance_id_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/AftermarketServices/Engines/{serial_number}/ProductionData'.format(serial_number='serial_number_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_aftermarket_services_get_user_status(client):
    """Test case for aftermarket_services_get_user_status

    Retrieve the status of an EDT Kit Registration with AGCO Power Web Services
    """
    params = [('voucherCode', 'voucher_code_example'),
                    ('dealerCode', 'dealer_code_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/AftermarketServices/UserStatuses',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_aftermarket_services_put_ecu(client):
    """Test case for aftermarket_services_put_ecu

    Activate or Deactivate an ECU, or Report an ECU as Damaged.
    """
    body = openapi_server.AGCOPowerServicesModelsECU()
    params = [('EDTInstanceId', 'edt_instance_id_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/api/v2/AftermarketServices/ECUs/{serial_number}'.format(serial_number='serial_number_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_aftermarket_services_put_iqa_codes(client):
    """Test case for aftermarket_services_put_iqa_codes

    Report the IQA codes used by an engine
    """
    body = ['body_example']
    params = [('EDTInstanceId', 'edt_instance_id_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/api/v2/AftermarketServices/Engines/{serial_number}/IQACodes'.format(serial_number='serial_number_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_aftermarket_services_update_user_status(client):
    """Test case for aftermarket_services_update_user_status

    Update the status of an EDT Kit Registration with AGCO Power Web Services
    """
    body = openapi_server.AGCOPowerServicesModelsUserStatus()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/api/v2/AftermarketServices/UserStatuses',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

