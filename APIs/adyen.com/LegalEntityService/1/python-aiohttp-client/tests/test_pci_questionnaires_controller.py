# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.generate_pci_description_request import GeneratePciDescriptionRequest
from openapi_server.models.generate_pci_description_response import GeneratePciDescriptionResponse
from openapi_server.models.get_pci_questionnaire_infos_response import GetPciQuestionnaireInfosResponse
from openapi_server.models.get_pci_questionnaire_response import GetPciQuestionnaireResponse
from openapi_server.models.pci_signing_request import PciSigningRequest
from openapi_server.models.pci_signing_response import PciSigningResponse
from openapi_server.models.service_error import ServiceError


pytestmark = pytest.mark.asyncio

async def test_get_legal_entities_id_pci_questionnaires(client):
    """Test case for get_legal_entities_id_pci_questionnaires

    Get PCI questionnaire details
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/lem/v1/legalEntities/{id}/pciQuestionnaires'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_legal_entities_id_pci_questionnaires_pciid(client):
    """Test case for get_legal_entities_id_pci_questionnaires_pciid

    Get PCI questionnaire
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/lem/v1/legalEntities/{id}/pciQuestionnaires/{pciid}'.format(id='id_example', pciid='pciid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_legal_entities_id_pci_questionnaires_generate_pci_templates(client):
    """Test case for post_legal_entities_id_pci_questionnaires_generate_pci_templates

    Generate PCI questionnaire
    """
    body = {"additionalSalesChannels":["eCommerce","eCommerce"],"language":"language"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/lem/v1/legalEntities/{id}/pciQuestionnaires/generatePciTemplates'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_legal_entities_id_pci_questionnaires_sign_pci_templates(client):
    """Test case for post_legal_entities_id_pci_questionnaires_sign_pci_templates

    Sign PCI questionnaire
    """
    body = {"signedBy":"signedBy","pciTemplateReferences":["pciTemplateReferences","pciTemplateReferences"]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/lem/v1/legalEntities/{id}/pciQuestionnaires/signPciTemplates'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

