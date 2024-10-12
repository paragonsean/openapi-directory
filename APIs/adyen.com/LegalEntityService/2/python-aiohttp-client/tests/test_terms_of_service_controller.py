# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.accept_terms_of_service_request import AcceptTermsOfServiceRequest
from openapi_server.models.accept_terms_of_service_response import AcceptTermsOfServiceResponse
from openapi_server.models.calculate_terms_of_service_status_response import CalculateTermsOfServiceStatusResponse
from openapi_server.models.get_terms_of_service_acceptance_infos_response import GetTermsOfServiceAcceptanceInfosResponse
from openapi_server.models.get_terms_of_service_document_request import GetTermsOfServiceDocumentRequest
from openapi_server.models.get_terms_of_service_document_response import GetTermsOfServiceDocumentResponse
from openapi_server.models.service_error import ServiceError


pytestmark = pytest.mark.asyncio

async def test_get_legal_entities_id_terms_of_service_acceptance_infos(client):
    """Test case for get_legal_entities_id_terms_of_service_acceptance_infos

    Get Terms of Service information for a legal entity
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/lem/v2/legalEntities/{id}/termsOfServiceAcceptanceInfos'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_legal_entities_id_terms_of_service_status(client):
    """Test case for get_legal_entities_id_terms_of_service_status

    Get Terms of Service status
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/lem/v2/legalEntities/{id}/termsOfServiceStatus'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_patch_legal_entities_id_terms_of_service_termsofservicedocumentid(client):
    """Test case for patch_legal_entities_id_terms_of_service_termsofservicedocumentid

    Accept Terms of Service
    """
    body = {"ipAddress":"ipAddress","acceptedBy":"acceptedBy"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/lem/v2/legalEntities/{id}/termsOfService/{termsofservicedocumentid}'.format(id='id_example', termsofservicedocumentid='termsofservicedocumentid_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_legal_entities_id_terms_of_service(client):
    """Test case for post_legal_entities_id_terms_of_service

    Get Terms of Service document
    """
    body = {"language":"language","type":"adyenAccount"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/lem/v2/legalEntities/{id}/termsOfService'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

