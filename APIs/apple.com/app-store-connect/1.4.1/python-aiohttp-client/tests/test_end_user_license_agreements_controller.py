# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.end_user_license_agreement_create_request import EndUserLicenseAgreementCreateRequest
from openapi_server.models.end_user_license_agreement_response import EndUserLicenseAgreementResponse
from openapi_server.models.end_user_license_agreement_update_request import EndUserLicenseAgreementUpdateRequest
from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.territories_response import TerritoriesResponse


pytestmark = pytest.mark.asyncio

async def test_end_user_license_agreements_create_instance(client):
    """Test case for end_user_license_agreements_create_instance

    
    """
    body = {"data":{"relationships":{"app":{"data":{"id":"id","type":"apps"}},"territories":{"data":[{"id":"id","type":"territories"},{"id":"id","type":"territories"}]}},"attributes":{"agreementText":"agreementText"},"type":"endUserLicenseAgreements"}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/endUserLicenseAgreements',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_end_user_license_agreements_delete_instance(client):
    """Test case for end_user_license_agreements_delete_instance

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/v1/endUserLicenseAgreements/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_end_user_license_agreements_get_instance(client):
    """Test case for end_user_license_agreements_get_instance

    
    """
    params = [('fields[endUserLicenseAgreements]', ['fields_end_user_license_agreements_example']),
                    ('include', ['include_example']),
                    ('fields[territories]', ['fields_territories_example']),
                    ('limit[territories]', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/endUserLicenseAgreements/{id}'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_end_user_license_agreements_territories_get_to_many_related(client):
    """Test case for end_user_license_agreements_territories_get_to_many_related

    
    """
    params = [('fields[territories]', ['fields_territories_example']),
                    ('limit', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/endUserLicenseAgreements/{id}/territories'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_end_user_license_agreements_update_instance(client):
    """Test case for end_user_license_agreements_update_instance

    
    """
    body = {"data":{"relationships":{"territories":{"data":[{"id":"id","type":"territories"},{"id":"id","type":"territories"}]}},"attributes":{"agreementText":"agreementText"},"id":"id","type":"endUserLicenseAgreements"}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/v1/endUserLicenseAgreements/{id}'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

