# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.data_notification import DataNotification
from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.hiu_health_information_request_response import HIUHealthInformationRequestResponse


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_v05_health_information_hiu_on_request_post(client):
    """Test case for v05_health_information_hiu_on_request_post

    Health information data request
    """
    body = {"resp":{"requestId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91"},"requestId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","error":{"code":0,"message":"message"},"hiRequest":{"sessionStatus":"REQUESTED","transactionId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91"},"timestamp":"2000-01-23T04:56:07.000+00:00"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'authorization': 'authorization_example',
        'x_hiu_id': 'x_hiu_id_example',
    }
    response = await client.request(
        method='POST',
        path='/gateway/v0.5/health-information/hiu/on-request',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_v05_health_information_transfer_post(client):
    """Test case for v05_health_information_transfer_post

    health information transfer API
    """
    body = {"keyMaterial":{"curve":"Curve25519","cryptoAlg":"ECDH","dhPublicKey":{"keyValue":"keyValue","expiry":"2000-01-23T04:56:07.000+00:00","parameters":"Curve25519/32byte random key"},"nonce":"3fa85f64-5717-4562-b3fc-2c963f66afa6"},"entries":[{"careContextReference":"RVH1008","checksum":"checksum","media":"application/fhir+json","content":"Encrypted content of data packaged in FHIR bundle"},{"careContextReference":"RVH1008","checksum":"checksum","media":"application/fhir+json","content":"Encrypted content of data packaged in FHIR bundle"}],"pageCount":0,"pageNumber":6,"transactionId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'authorization': 'authorization_example',
    }
    response = await client.request(
        method='POST',
        path='/gateway/v0.5/health-information/transfer',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

