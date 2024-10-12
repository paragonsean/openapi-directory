# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.get_pci_url_request import GetPciUrlRequest
from openapi_server.models.get_pci_url_response import GetPciUrlResponse
from openapi_server.models.service_error import ServiceError


pytestmark = pytest.mark.asyncio

async def test_post_get_pci_questionnaire_url(client):
    """Test case for post_get_pci_questionnaire_url

    Get a link to a PCI compliance questionnaire
    """
    body = {"accountHolderCode":"accountHolderCode","returnUrl":"returnUrl"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/cal/services/Hop/v5/getPciQuestionnaireUrl',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

