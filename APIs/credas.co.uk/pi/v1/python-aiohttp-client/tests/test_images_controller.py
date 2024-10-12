# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.credas_api_models_errors_error_response import CredasApiModelsErrorsErrorResponse
from openapi_server.models.credas_api_models_images_add_id_document_image_request import CredasApiModelsImagesAddIdDocumentImageRequest
from openapi_server.models.credas_api_models_images_add_id_document_image_response import CredasApiModelsImagesAddIdDocumentImageResponse
from openapi_server.models.credas_api_models_images_add_liveness_image_request import CredasApiModelsImagesAddLivenessImageRequest
from openapi_server.models.credas_api_models_images_add_selfie_image_request import CredasApiModelsImagesAddSelfieImageRequest
from openapi_server.models.credas_api_models_images_add_selfie_image_response import CredasApiModelsImagesAddSelfieImageResponse
from openapi_server.models.credas_api_models_images_get_id_document_image_response import CredasApiModelsImagesGetIdDocumentImageResponse
from openapi_server.models.credas_api_models_images_get_liveness_image_response import CredasApiModelsImagesGetLivenessImageResponse
from openapi_server.models.credas_api_models_images_get_liveness_performed_image_response import CredasApiModelsImagesGetLivenessPerformedImageResponse
from openapi_server.models.credas_api_models_images_get_selfie_image_response import CredasApiModelsImagesGetSelfieImageResponse


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_add_id_document_image(client):
    """Test case for add_id_document_image

    Add an id document image to the specified registration.
    """
    body = openapi_server.CredasApiModelsImagesAddIdDocumentImageRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/*+json',
        'apikey': 'apikey_example',
    }
    response = await client.request(
        method='POST',
        path='/api/images/id-document',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_add_liveness_image(client):
    """Test case for add_liveness_image

    Add a liveness image (UAP) to the specified registration.
    """
    body = openapi_server.CredasApiModelsImagesAddLivenessImageRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/*+json',
        'apikey': 'apikey_example',
    }
    response = await client.request(
        method='POST',
        path='/api/images/liveness',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_add_selfie_image(client):
    """Test case for add_selfie_image

    Add a selfie image to the registration.
    """
    body = openapi_server.CredasApiModelsImagesAddSelfieImageRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/*+json',
        'apikey': 'apikey_example',
    }
    response = await client.request(
        method='POST',
        path='/api/images/selfie',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_id_document_images(client):
    """Test case for get_id_document_images

    Get all id document images associated with a registration.
    """
    headers = { 
        'Accept': 'application/json',
        'apikey': 'apikey_example',
    }
    response = await client.request(
        method='GET',
        path='/api/images/id-document/{registration_id}'.format(registration_id='registration_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_liveness_image(client):
    """Test case for get_liveness_image

    Retrieve the liveness action image (UAP) associated with a registration.
    """
    headers = { 
        'Accept': 'application/json',
        'apikey': 'apikey_example',
    }
    response = await client.request(
        method='GET',
        path='/api/images/liveness/{registration_id}'.format(registration_id='registration_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_liveness_performed_image(client):
    """Test case for get_liveness_performed_image

    Retrieve the liveness performed image associated with a registration.
    """
    headers = { 
        'Accept': 'application/json',
        'apikey': 'apikey_example',
    }
    response = await client.request(
        method='GET',
        path='/api/images/liveness-performed/{registration_id}'.format(registration_id='registration_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_scan_report_pdf(client):
    """Test case for get_scan_report_pdf

    Returns a detailed report on the analysis that has taken place of a scanned document
    """
    headers = { 
        'Accept': 'application/json',
        'apikey': 'apikey_example',
    }
    response = await client.request(
        method='GET',
        path='/api/images/scan-report-pdf/{scan_id}'.format(scan_id='scan_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_selfie_image(client):
    """Test case for get_selfie_image

    Retrieve the selfie image associated with a registration.
    """
    headers = { 
        'Accept': 'application/json',
        'apikey': 'apikey_example',
    }
    response = await client.request(
        method='GET',
        path='/api/images/selfie/{registration_id}'.format(registration_id='registration_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

