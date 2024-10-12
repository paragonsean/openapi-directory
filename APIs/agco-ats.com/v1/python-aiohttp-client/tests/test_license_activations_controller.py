# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.api_models_api_error import APIModelsApiError
from openapi_server.models.dealer_db_models_edt_lite_registration import DealerDBModelsEDTLiteRegistration
from openapi_server.models.dealer_db_models_license_activation import DealerDBModelsLicenseActivation
from openapi_server.models.dealer_db_models_license_activation_confirm import DealerDBModelsLicenseActivationConfirm
from openapi_server.models.dealer_db_models_license_activation_create import DealerDBModelsLicenseActivationCreate
from openapi_server.models.dealer_db_models_license_activation_update import DealerDBModelsLicenseActivationUpdate


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_license_activations_post(client):
    """Test case for license_activations_post

    Create a license activation.
    """
    body = openapi_server.DealerDBModelsLicenseActivationCreate()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/v2/LicenseActivations',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_license_activations_post_register_edt_lite(client):
    """Test case for license_activations_post_register_edt_lite

    Register an EDT Lite with the Server
    """
    body = openapi_server.DealerDBModelsEDTLiteRegistration()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/v2/LicenseActivations/RegisterEDTLite',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_license_activations_put(client):
    """Test case for license_activations_put

    Update a license activiation.
    """
    body = openapi_server.DealerDBModelsLicenseActivationUpdate()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/api/v2/LicenseActivations/{id}'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_license_activations_put_confirm(client):
    """Test case for license_activations_put_confirm

    Confirm that the client has applied the updated license.
    """
    body = openapi_server.DealerDBModelsLicenseActivationConfirm()
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/api/v2/LicenseActivations/{id}/Confirm'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

