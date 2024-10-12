# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.app_response import AppResponse
from openapi_server.models.beta_license_agreement_response import BetaLicenseAgreementResponse
from openapi_server.models.beta_license_agreement_update_request import BetaLicenseAgreementUpdateRequest
from openapi_server.models.beta_license_agreements_response import BetaLicenseAgreementsResponse
from openapi_server.models.error_response import ErrorResponse


pytestmark = pytest.mark.asyncio

async def test_beta_license_agreements_app_get_to_one_related(client):
    """Test case for beta_license_agreements_app_get_to_one_related

    
    """
    params = [('fields[apps]', ['fields_apps_example'])]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/betaLicenseAgreements/{id}/app'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_beta_license_agreements_get_collection(client):
    """Test case for beta_license_agreements_get_collection

    
    """
    params = [('filter[app]', ['filter_app_example']),
                    ('fields[betaLicenseAgreements]', ['fields_beta_license_agreements_example']),
                    ('limit', 56),
                    ('include', ['include_example']),
                    ('fields[apps]', ['fields_apps_example'])]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/betaLicenseAgreements',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_beta_license_agreements_get_instance(client):
    """Test case for beta_license_agreements_get_instance

    
    """
    params = [('fields[betaLicenseAgreements]', ['fields_beta_license_agreements_example']),
                    ('include', ['include_example']),
                    ('fields[apps]', ['fields_apps_example'])]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/betaLicenseAgreements/{id}'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_beta_license_agreements_update_instance(client):
    """Test case for beta_license_agreements_update_instance

    
    """
    body = {"data":{"attributes":{"agreementText":"agreementText"},"id":"id","type":"betaLicenseAgreements"}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/v1/betaLicenseAgreements/{id}'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

